#ifndef PRIVANNA_BEHAVIOR_TREE_HPP
#define PRIVANNA_BEHAVIOR_TREE_HPP

#include <vector>
#include <memory>
#include <string>
#include <functional>
#include <unordered_map>
#include "src/core/entity.hpp"

namespace privanna {
namespace ai {

// Behavior Tree Node Types
enum class NodeType {
    SEQUENCE,        // Execute children in order until one fails
    SELECTOR,        // Execute children in order until one succeeds
    PARALLEL,        // Execute all children simultaneously
    DECORATOR,       // Modify child node behavior
    ACTION,          // Perform specific action
    CONDITION        // Check condition, return success/failure
};

enum class NodeStatus {
    SUCCESS,
    FAILURE,
    RUNNING
};

// Forward declarations
class BehaviorNode;
class Blackboard;

// Behavior Tree Context
class AIContext {
public:
    Entity* entity;
    GameState* game_state;
    double delta_time;
    std::unordered_map<std::string, float> memory;
    std::unordered_map<std::string, std::string> observations;
};

// Blackboard for shared data between nodes
class Blackboard {
public:
    template<typename T>
    void set(const std::string& key, const T& value) {
        data_[key] = std::any(value);
    }
    
    template<typename T>
    T get(const std::string& key, const T& default_value = T{}) const {
        auto it = data_.find(key);
        if (it != data_.end()) {
            try {
                return std::any_cast<T>(it->second);
            } catch (const std::bad_any_cast&) {
                return default_value;
            }
        }
        return default_value;
    }
    
    bool has(const std::string& key) const {
        return data_.find(key) != data_.end();
    }
    
    void clear() { data_.clear(); }
    
private:
    std::unordered_map<std::string, std::any> data_;
};

// Base Behavior Node
class BehaviorNode {
public:
    BehaviorNode(NodeType type, const std::string& name = "");
    virtual ~BehaviorNode() = default;
    
    virtual NodeStatus execute(AIContext& context, Blackboard& blackboard) = 0;
    virtual void reset() {}
    
    // Node management
    void addChild(std::shared_ptr<BehaviorNode> child);
    void removeChild(std::shared_ptr<BehaviorNode> child);
    const std::vector<std::shared_ptr<BehaviorNode>>& getChildren() const;
    
    // Properties
    const std::string& getName() const { return name_; }
    NodeType getType() const { return type_; }
    void setDebugMode(bool debug) { debug_mode_ = debug; }
    
protected:
    NodeType type_;
    std::string name_;
    std::vector<std::shared_ptr<BehaviorNode>> children_;
    bool debug_mode_;
    
    void logDebug(const std::string& message, NodeStatus status);
};

// Composite Nodes
class SequenceNode : public BehaviorNode {
public:
    SequenceNode(const std::string& name = "Sequence");
    NodeStatus execute(AIContext& context, Blackboard& blackboard) override;
    void reset() override;
    
private:
    size_t current_child_;
};

class SelectorNode : public BehaviorNode {
public:
    SelectorNode(const std::string& name = "Selector");
    NodeStatus execute(AIContext& context, Blackboard& blackboard) override;
    void reset() override;
    
private:
    size_t current_child_;
};

class ParallelNode : public BehaviorNode {
public:
    enum class Policy {
        SUCCEED_ON_ONE,
        SUCCEED_ON_ALL,
        FAIL_ON_ONE,
        FAIL_ON_ALL
    };
    
    ParallelNode(Policy success_policy = Policy::SUCCEED_ON_ALL, 
                 Policy failure_policy = Policy::FAIL_ON_ONE,
                 const std::string& name = "Parallel");
    
    NodeStatus execute(AIContext& context, Blackboard& blackboard) override;
    void reset() override;
    
private:
    Policy success_policy_;
    Policy failure_policy_;
    std::unordered_map<BehaviorNode*, NodeStatus> child_status_;
};

// Decorator Nodes
class InverterNode : public BehaviorNode {
public:
    InverterNode(const std::string& name = "Inverter");
    NodeStatus execute(AIContext& context, Blackboard& blackboard) override;
};

class RepeaterNode : public BehaviorNode {
public:
    RepeaterNode(int repeat_count = -1, const std::string& name = "Repeater");
    NodeStatus execute(AIContext& context, Blackboard& blackboard) override;
    void reset() override;
    
private:
    int repeat_count_;
    int current_count_;
};

class RetryNode : public BehaviorNode {
public:
    RetryNode(int max_attempts = 3, const std::string& name = "Retry");
    NodeStatus execute(AIContext& context, Blackboard& blackboard) override;
    void reset() override;
    
private:
    int max_attempts_;
    int current_attempts_;
};

class TimerNode : public BehaviorNode {
public:
    TimerNode(double duration_seconds, const std::string& name = "Timer");
    NodeStatus execute(AIContext& context, Blackboard& blackboard) override;
    void reset() override;
    
private:
    double duration_;
    double elapsed_time_;
};

// Action Nodes
class ActionNode : public BehaviorNode {
public:
    using ActionFunction = std::function<NodeStatus(AIContext&, Blackboard&)>;
    
    ActionNode(ActionFunction action, const std::string& name = "Action");
    NodeStatus execute(AIContext& context, Blackboard& blackboard) override;
    
private:
    ActionFunction action_;
};

// Condition Nodes
class ConditionNode : public BehaviorNode {
public:
    using ConditionFunction = std::function<bool(AIContext&, Blackboard&)>;
    
    ConditionNode(ConditionFunction condition, const std::string& name = "Condition");
    NodeStatus execute(AIContext& context, Blackboard& blackboard) override;
    
private:
    ConditionFunction condition_;
};

// Built-in Actions for Privanna
namespace actions {
    // Movement Actions
    NodeStatus moveToPosition(AIContext& context, Blackboard& blackboard);
    NodeStatus followTarget(AIContext& context, Blackboard& blackboard);
    NodeStatus patrolArea(AIContext& context, Blackboard& blackboard);
    NodeStatus retreatToSafety(AIContext& context, Blackboard& blackboard);
    
    // Combat Actions
    NodeStatus attackNearestEnemy(AIContext& context, Blackboard& blackboard);
    NodeStatus defendPosition(AIContext& context, Blackboard& blackboard);
    NodeStatus useSpecialAbility(AIContext& context, Blackboard& blackboard);
    NodeStatus coordinateWithAllies(AIContext& context, Blackboard& blackboard);
    
    // Economic Actions
    NodeStatus collectResources(AIContext& context, Blackboard& blackboard);
    NodeStatus buildStructure(AIContext& context, Blackboard& blackboard);
    NodeStatus upgradeUnit(AIContext& context, Blackboard& blackboard);
    NodeStatus tradeWithFaction(AIContext& context, Blackboard& blackboard);
    
    // Diplomatic Actions
    NodeStatus negotiatePeace(AIContext& context, Blackboard& blackboard);
    NodeStatus formAlliance(AIContext& context, Blackboard& blackboard);
    NodeStatus declareWar(AIContext& context, Blackboard& blackboard);
    NodeStatus sendGift(AIContext& context, Blackboard& blackboard);
}

// Built-in Conditions for Privanna
namespace conditions {
    // Health and Status Conditions
    bool isHealthy(AIContext& context, Blackboard& blackboard);
    bool isInDanger(AIContext& context, Blackboard& blackboard);
    bool hasLowResources(AIContext& context, Blackboard& blackboard);
    bool isUnderAttack(AIContext& context, Blackboard& blackboard);
    
    // Combat Conditions
    bool hasEnemiesNearby(AIContext& context, Blackboard& blackboard);
    bool canWinCombat(AIContext& context, Blackboard& blackboard);
    bool hasAdvantageousPosition(AIContext& context, Blackboard& blackboard);
    bool abilitiesAvailable(AIContext& context, Blackboard& blackboard);
    
    // Economic Conditions
    bool canAffordUpgrade(AIContext& context, Blackboard& blackboard);
    bool resourcesAvailable(AIContext& context, Blackboard& blackboard);
    bool economyStrong(AIContext& context, Blackboard& blackboard);
    bool tradeOpportunityExists(AIContext& context, Blackboard& blackboard);
    
    // Diplomatic Conditions
    bool atWar(AIContext& context, Blackboard& blackboard);
    bool hasAllies(AIContext& context, Blackboard& blackboard);
    bool canNegotiate(AIContext& context, Blackboard& blackboard);
    bool neutralAvailable(AIContext& context, Blackboard& blackboard);
}

// Behavior Tree Builder
class BehaviorTreeBuilder {
public:
    BehaviorTreeBuilder();
    
    // Tree construction
    BehaviorTreeBuilder& sequence(const std::string& name = "");
    BehaviorTreeBuilder& selector(const std::string& name = "");
    BehaviorTreeBuilder& parallel(ParallelNode::Policy success = ParallelNode::Policy::SUCCEED_ON_ALL,
                                 ParallelNode::Policy failure = ParallelNode::Policy::FAIL_ON_ONE,
                                 const std::string& name = "");
    
    BehaviorTreeBuilder& inverter(const std::string& name = "");
    BehaviorTreeBuilder& repeater(int count = -1, const std::string& name = "");
    BehaviorTreeBuilder& retry(int attempts = 3, const std::string& name = "");
    BehaviorTreeBuilder& timer(double duration, const std::string& name = "");
    
    BehaviorTreeBuilder& action(ActionNode::ActionFunction action, const std::string& name = "");
    BehaviorTreeBuilder& condition(ConditionNode::ConditionFunction condition, const std::string& name = "");
    
    BehaviorTreeBuilder& end();  // End current composite node
    
    // Build final tree
    std::shared_ptr<BehaviorNode> build();
    
private:
    std::vector<std::shared_ptr<BehaviorNode>> node_stack_;
    std::shared_ptr<BehaviorNode> root_;
    
    void addToCurrentNode(std::shared_ptr<BehaviorNode> node);
};

// Complete Behavior Tree
class BehaviorTree {
public:
    BehaviorTree(std::shared_ptr<BehaviorNode> root);
    
    NodeStatus execute(AIContext& context);
    void reset();
    void setDebugMode(bool debug);
    
    // Tree inspection
    std::shared_ptr<BehaviorNode> getRoot() const { return root_; }
    Blackboard& getBlackboard() { return blackboard_; }
    
private:
    std::shared_ptr<BehaviorNode> root_;
    Blackboard blackboard_;
    bool debug_mode_;
};

// Tree Templates for different unit types
class BehaviorTreeTemplates {
public:
    static std::shared_ptr<BehaviorTree> createWarriorTree();
    static std::shared_ptr<BehaviorTree> createScoutTree();
    static std::shared_ptr<BehaviorTree> createBuilderTree();
    static std::shared_ptr<BehaviorTree> createLeaderTree();
    static std::shared_ptr<BehaviorTree> createDefenderTree();
    static std::shared_ptr<BehaviorTree> createEconomistTree();
    static std::shared_ptr<BehaviorTree> createDiplomatTree();
    
private:
    static BehaviorTreeBuilder createBaseBehaviorTree();
    static void addCombatBehavior(BehaviorTreeBuilder& builder);
    static void addEconomicBehavior(BehaviorTreeBuilder& builder);
    static void addDiplomaticBehavior(BehaviorTreeBuilder& builder);
};

} // namespace ai
} // namespace privanna

#endif // PRIVANNA_BEHAVIOR_TREE_HPP