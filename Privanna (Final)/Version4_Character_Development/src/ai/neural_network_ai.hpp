#ifndef PRIVANNA_NEURAL_NETWORK_AI_HPP
#define PRIVANNA_NEURAL_NETWORK_AI_HPP

#include <torch/torch.h>
#include <vector>
#include <memory>
#include "src/game/faction_manager.hpp"

namespace privanna {
namespace ai {

enum class AITaskType {
    STRATEGIC_PLANNING,
    TACTICAL_COMBAT,
    RESOURCE_MANAGEMENT,
    DIPLOMATIC_NEGOTIATION,
    ECONOMIC_FORECASTING,
    THREAT_ASSESSMENT,
    ALLIANCE_FORMATION,
    TERRITORY_EXPANSION
};

struct AIDecision {
    AITaskType task_type;
    std::vector<float> action_probabilities;
    float confidence_score;
    std::string reasoning;
    int priority_level;
    double expected_outcome;
};

class NeuralNetworkAI {
public:
    NeuralNetworkAI();
    ~NeuralNetworkAI();
    
    // Core AI Systems
    bool initialize();
    void shutdown();
    
    // Strategic Planning Neural Networks
    AIDecision planStrategicMove(Faction* faction, const GameState& game_state);
    float evaluatePosition(const GameState& game_state, Faction* faction);
    std::vector<GameState> predictOpponentMoves(const GameState& game_state, int turns_ahead);
    
    // Tactical Combat AI
    AIDecision selectCombatAction(const CombatState& combat_state, Unit* unit);
    std::vector<Vector2> calculateOptimalPositioning(const std::vector<Unit*>& units, const Terrain& terrain);
    float evaluateCombatOutcome(const CombatState& combat_state);
    
    // Learning Systems
    void trainFromExperience(const std::vector<GameExperience>& experiences);
    void updateModelWeights(float learning_rate);
    void saveModel(const std::string& model_path);
    bool loadModel(const std::string& model_path);
    
    // Adaptive Difficulty
    void adjustDifficulty(float player_performance);
    void setPersonalityTraits(const std::unordered_map<std::string, float>& traits);
    
private:
    // Neural Network Models
    std::unique_ptr<torch::nn::Module> strategic_model_;
    std::unique_ptr<torch::nn::Module> tactical_model_;
    std::unique_ptr<torch::nn::Module> economic_model_;
    std::unique_ptr<torch::nn::Module> diplomatic_model_;
    
    // Training Data
    std::vector<GameExperience> experience_buffer_;
    torch::optim::Optimizer* optimizer_;
    
    // AI Personality
    std::unordered_map<std::string, float> personality_traits_;
    float difficulty_level_;
    
    // Performance Metrics
    std::vector<float> decision_history_;
    float average_confidence_;
    int successful_predictions_;
    
    // Internal Methods
    void createNeuralNetworks();
    std::vector<float> extractGameStateFeatures(const GameState& game_state, Faction* faction);
    torch::Tensor preprocessInput(const std::vector<float>& features);
    std::vector<float> postprocessOutput(const torch::Tensor& output);
    
    // Learning Algorithms
    void reinforcementLearningUpdate(const GameExperience& experience);
    void supervisedLearningUpdate(const std::vector<TrainingExample>& examples);
    void unsupervisedPatternRecognition(const std::vector<GameState>& states);
    
    // Evaluation Systems
    float calculateDecisionQuality(const AIDecision& decision, const GameState& outcome);
    bool isNovelSituation(const GameState& game_state);
    void recordDecisionMetrics(const AIDecision& decision);
};

class MultiAgentCoordinator {
public:
    MultiAgentCoordinator();
    
    void addAgent(Faction* faction, std::unique_ptr<NeuralNetworkAI> ai);
    void coordinateAgents(const GameState& game_state);
    std::vector<AIDecision> getCoordinatedDecisions();
    
    // Agent Communication
    void broadcastMessage(const AIMessage& message);
    void establishAlliance(Faction* faction1, Faction* faction2);
    void breakAlliance(Faction* faction1, Faction* faction2);
    
private:
    std::unordered_map<Faction*, std::unique_ptr<NeuralNetworkAI>> agents_;
    std::vector<AIMessage> message_queue_;
    std::vector<Alliance> active_alliances_;
    
    void processMessageQueue();
    void resolveConflictingDecisions();
    void synchronizeAgentStrategies();
};

} // namespace ai
} // namespace privanna

#endif // PRIVANNA_NEURAL_NETWORK_AI_HPP