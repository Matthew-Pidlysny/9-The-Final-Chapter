/*
 * Privanna AI System
 * Advanced AI with PyTorch C++ integration
 * Strategic, tactical, and creative AI systems
 */

#ifndef PRIVANNA_AI_SYSTEM_HPP
#define PRIVANNA_AI_SYSTEM_HPP

#include "../core/privanna_engine.hpp"
#include "../game/faction_manager.hpp"
#include <torch/torch.h>
#include <opencv2/opencv.hpp>
#include <memory>
#include <vector>
#include <unordered_map>
#include <thread>
#include <atomic>
#include <chrono>

namespace privanna {

// AI decision types
enum class AIDecisionType {
    STRATEGIC,      // Long-term planning
    TACTICAL,       // Battle decisions
    ECONOMIC,       // Resource management
    DIPLOMATIC,     // Alliance/war decisions
    MAGIC,          // Spell usage
    CREATIVE        // Content generation
};

// AI difficulty levels
enum class AIDifficulty {
    TUTORIAL,       // Learning difficulty
    EASY,           // Beginner friendly
    NORMAL,         // Standard challenge
    HARD,           // Experienced players
    EXPERT,         // Very challenging
    INSANE,         // Maximum difficulty
    ADAPTIVE        // Dynamic difficulty adjustment
};

// Neural network models for different AI aspects
class StrategicAI;
class TacticalAI;
class EconomicAI;
class DiplomaticAI;
class CreativeAI;

// AI decision structure
struct AIDecision {
    AIDecisionType type;
    FactionType faction;
    double confidence = 0.0;
    std::string reasoning;
    std::unordered_map<std::string, double> parameters;
    std::chrono::system_clock::time_point decision_time;
    
    // Decision-specific data
    std::variant<
        std::string,        // Strategic decision description
        std::vector<int>,   // Tactical unit movements
        std::pair<int, int>, // Economic action (type, amount)
        FactionType,        // Diplomatic target
        std::string         // Magic spell
    > decision_data;
};

// Game state representation for AI
struct GameState {
    // Faction states
    std::unordered_map<FactionType, FactionState> faction_states;
    
    // Territory information
    std::vector<TerritoryInfo> territories;
    
    // Military positions
    std::vector<UnitPosition> unit_positions;
    
    // Resource distribution
    std::unordered_map<std::string, double> global_resources;
    
    // Current turn information
    uint32_t current_turn = 0;
    FactionType current_faction = FactionType::SHENZAN;
    
    // AI-specific data
    std::vector<double> encoded_state;  // Neural network input
    cv::Mat visual_representation;     // Computer vision input
    
    // Metadata
    std::chrono::system_clock::time_point timestamp;
    double game_progress = 0.0;
};

// AI learning data
struct LearningData {
    GameState game_state;
    AIDecision decision;
    double outcome_score = 0.0;
    bool was_successful = false;
    std::string player_feedback;
    
    // Training labels
    torch::Tensor target_output;
    std::vector<double> reward_signals;
};

// AI system configuration
struct AISystemConfig {
    // Model paths
    std::string strategic_model_path = "models/strategic_ai.pt";
    std::string tactical_model_path = "models/tactical_ai.pt";
    std::string economic_model_path = "models/economic_ai.pt";
    std::string diplomatic_model_path = "models/diplomatic_ai.pt";
    std::string creative_model_path = "models/creative_ai.pt";
    
    // Training parameters
    double learning_rate = 0.001;
    size_t batch_size = 32;
    size_t memory_size = 10000;  // Experience replay buffer
    double exploration_rate = 0.1;
    double discount_factor = 0.99;
    
    // Performance settings
    size_t max_threads = 4;
    double decision_timeout_ms = 1000.0;
    bool enable_gpu_acceleration = true;
    bool enable_learning = true;
    
    // Creative AI settings
    bool enable_procedural_content = true;
    double creativity_level = 0.7;
    std::string content_output_path = "generated_content/";
};

// Main AI system class
class AISystem {
private:
    // Configuration
    AISystemConfig config_;
    EngineConfig engine_config_;
    
    // AI models
    std::unique_ptr<StrategicAI> strategic_ai_;
    std::unique_ptr<TacticalAI> tactical_ai_;
    std::unique_ptr<EconomicAI> economic_ai_;
    std::unique_ptr<DiplomaticAI> diplomatic_ai_;
    std::unique_ptr<CreativeAI> creative_ai_;
    
    // Learning systems
    std::vector<LearningData> experience_buffer_;
    std::unordered_map<FactionType, std::vector<LearningData>> faction_learning_data_;
    
    // Thread management
    std::vector<std::thread> worker_threads_;
    std::atomic<bool> should_stop_;
    std::mutex decision_mutex_;
    std::condition_variable decision_cv_;
    
    // Decision making
    std::unordered_map<FactionType, AIDecision> current_decisions_;
    std::unordered_map<FactionType, std::vector<AIDecision>> decision_history_;
    
    // Performance monitoring
    std::unordered_map<FactionType, double> ai_performance_ratings_;
    std::chrono::high_resolution_clock::time_point last_update_time_;
    size_t decisions_made_ = 0;
    size_t successful_decisions_ = 0;
    
    // Adaptive difficulty
    std::unordered_map<FactionType, AIDifficulty> current_difficulties_;
    std::unordered_map<FactionType, double> player_skill_assessments_;
    double adaptive_difficulty_threshold_ = 0.1;
    
    // State tracking
    GameState current_game_state_;
    std::vector<GameState> state_history_;
    
public:
    // Constructor/Destructor
    explicit AISystem(const EngineConfig& engine_config);
    ~AISystem();
    
    // Initialization
    bool initialize();
    void shutdown();
    
    // Main update function
    void process_ai_frame(double delta_time);
    
    // Decision making interface
    AIDecision make_strategic_decision(FactionType faction, const GameState& state);
    AIDecision make_tactical_decision(FactionType faction, const GameState& state);
    AIDecision make_economic_decision(FactionType faction, const GameState& state);
    AIDecision make_diplomatic_decision(FactionType faction, const GameState& state);
    AIDecision make_magic_decision(FactionType faction, const GameState& state);
    
    // Learning systems
    void add_learning_experience(const LearningData& data);
    void train_models();
    void save_models();
    void load_models();
    
    // Adaptive difficulty
    void set_ai_difficulty(FactionType faction, AIDifficulty difficulty);
    void update_player_skill_assessment(FactionType faction, double performance);
    AIDifficulty get_adaptive_difficulty(FactionType faction);
    
    // Creative AI
    std::string generate_story_event(const GameState& state);
    std::string generate_quest(FactionType faction, const GameState& state);
    std::string generate_dynamic_event(const GameState& state);
    std::vector<std::string> generate_dialogue(FactionType faction, const std::string& context);
    
    // Performance monitoring
    double get_ai_performance(FactionType faction) const;
    double get_overall_performance() const;
    std::unordered_map<FactionType, std::vector<AIDecision>> get_decision_history(FactionType faction) const;
    
    // State management
    void update_game_state(const GameState& state);
    GameState get_current_game_state() const;
    
    // Configuration
    void update_config(const AISystemConfig& new_config);
    const AISystemConfig& get_config() const;
    
private:
    // AI system initialization
    bool initialize_neural_networks();
    bool initialize_strategic_ai();
    bool initialize_tactical_ai();
    bool initialize_economic_ai();
    bool initialize_diplomatic_ai();
    bool initialize_creative_ai();
    bool initialize_worker_threads();
    
    // State encoding for neural networks
    torch::Tensor encode_game_state(const GameState& state) const;
    cv::Mat create_visual_representation(const GameState& state) const;
    std::vector<double> create_feature_vector(const GameState& state, FactionType faction) const;
    
    // Decision processing
    void process_decision_requests();
    void execute_decision(const AIDecision& decision);
    void evaluate_decision_outcome(const AIDecision& decision, double outcome);
    
    // Learning algorithms
    void update_experience_replay(const LearningData& data);
    void perform_reinforcement_learning();
    void update_neural_network_parameters();
    double calculate_reward(const LearningData& data) const;
    
    // Adaptive difficulty algorithms
    void assess_player_skill(FactionType faction);
    void adjust_ai_difficulty(FactionType faction);
    double calculate_difficulty_adjustment(FactionType faction) const;
    
    // Creative AI algorithms
    std::string generate_procedural_content(const std::string& content_type, const GameState& state);
    std::vector<std::string> generate_narrative_elements(const GameState& state);
    double calculate_creativity_score(const std::string& content) const;
    
    // Performance optimization
    void optimize_neural_network_performance();
    void balance_ai_workload();
    void cache_frequently_used_states();
    
    // Utility functions
    bool is_valid_decision(const AIDecision& decision) const;
    double calculate_decision_confidence(const AIDecision& decision) const;
    void log_ai_decision(const AIDecision& decision) const;
    
    // Thread management
    void worker_thread_function(size_t thread_id);
    void stop_worker_threads();
    
    // Model management
    bool load_pytorch_model(const std::string& path, torch::nn::Module& module);
    bool save_pytorch_model(const std::string& path, const torch::nn::Module& module);
    void optimize_model_for_inference(torch::nn::Module& module);
};

// Strategic AI class - long-term planning
class StrategicAI {
private:
    torch::nn::Module model_;
    torch::optim::Optimizer* optimizer_;
    AISystemConfig config_;
    
public:
    StrategicAI(const AISystemConfig& config);
    ~StrategicAI();
    
    bool initialize();
    AIDecision make_decision(FactionType faction, const GameState& state);
    void train(const std::vector<LearningData>& batch);
    
private:
    torch::Tensor process_strategic_input(const GameState& state, FactionType faction);
    std::string interpret_strategic_output(const torch::Tensor& output);
};

// Tactical AI class - battle decisions
class TacticalAI {
private:
    torch::nn::Module model_;
    torch::optim::Optimizer* optimizer_;
    AISystemConfig config_;
    
public:
    TacticalAI(const AISystemConfig& config);
    ~TacticalAI();
    
    bool initialize();
    AIDecision make_decision(FactionType faction, const GameState& state);
    void train(const std::vector<LearningData>& batch);
    
private:
    torch::Tensor process_tactical_input(const GameState& state, FactionType faction);
    std::vector<int> interpret_tactical_output(const torch::Tensor& output);
};

// Economic AI class - resource management
class EconomicAI {
private:
    torch::nn::Module model_;
    torch::optim::Optimizer* optimizer_;
    AISystemConfig config_;
    
public:
    EconomicAI(const AISystemConfig& config);
    ~EconomicAI();
    
    bool initialize();
    AIDecision make_decision(FactionType faction, const GameState& state);
    void train(const std::vector<LearningData>& batch);
    
private:
    torch::Tensor process_economic_input(const GameState& state, FactionType faction);
    std::pair<int, int> interpret_economic_output(const torch::Tensor& output);
};

// Diplomatic AI class - alliance and war decisions
class DiplomaticAI {
private:
    torch::nn::Module model_;
    torch::optim::Optimizer* optimizer_;
    AISystemConfig config_;
    
public:
    DiplomaticAI(const AISystemConfig& config);
    ~DiplomaticAI();
    
    bool initialize();
    AIDecision make_decision(FactionType faction, const GameState& state);
    void train(const std::vector<LearningData>& batch);
    
private:
    torch::Tensor process_diplomatic_input(const GameState& state, FactionType faction);
    FactionType interpret_diplomatic_output(const torch::Tensor& output);
};

// Creative AI class - content generation
class CreativeAI {
private:
    torch::nn::Module model_;
    AISystemConfig config_;
    
public:
    CreativeAI(const AISystemConfig& config);
    ~CreativeAI();
    
    bool initialize();
    std::string generate_content(const std::string& content_type, const GameState& state);
    std::string generate_story(const GameState& state);
    std::string generate_quest(FactionType faction, const GameState& state);
    
private:
    torch::Tensor process_creative_input(const GameState& state, const std::string& content_type);
    std::string interpret_creative_output(const torch::Tensor& output);
};

// Utility functions
std::string ai_decision_type_to_string(AIDecisionType type);
std::string ai_difficulty_to_string(AIDifficulty difficulty);
double calculate_ai_confidence(const torch::Tensor& output);
bool is_valid_ai_action(FactionType faction, const AIDecision& decision);

} // namespace privanna

#endif // PRIVANNA_AI_SYSTEM_HPP