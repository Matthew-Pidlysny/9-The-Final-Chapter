#ifndef ASTRATECHNICA_AI_SYSTEM_HPP
#define ASTRATECHNICA_AI_SYSTEM_HPP

#include <vector>
#include <map>
#include <string>
#include <memory>
#include <thread>
#include <mutex>
#include <atomic>
#include <functional>
#include <random>
#include <chrono>
#include <queue>
#include "../core/game_engine.hpp"

// Include AI libraries
#include <torch/torch.h>
#include <mlpack/core.hpp>
#include <opencv2/opencv.hpp>

namespace AstraTechnica {

    // AI Behavior Types
    enum class AIBehaviorType {
        NEUTRAL,
        AGGRESSIVE,
        DEFENSIVE,
        OPPORTUNISTIC,
        STRATEGIC,
        CHAOTIC
    };

    // AI Decision Types
    enum class AIDecisionType {
        INVESTMENT,
        HACKING,
        DEFENSE,
        EXPANSION,
        ESPIONAGE,
        ALLIANCE,
        BETRAYAL
    };

    // AI Personality Traits
    struct AIPersonality {
        double aggression = 0.5;        // 0.0 - 1.0
        double risk_taking = 0.5;        // 0.0 - 1.0
        double cooperation = 0.5;        // 0.0 - 1.0
        double innovation = 0.5;         // 0.0 - 1.0
        double patience = 0.5;           // 0.0 - 1.0
        double greed = 0.5;              // 0.0 - 1.0
        double paranoia = 0.5;           // 0.0 - 1.0
        double loyalty = 0.5;            // 0.0 - 1.0
    };

    // AI Decision Structure
    struct AIDecision {
        std::string decision_id;
        AIDecisionType type;
        std::string target;
        std::map<std::string, double> parameters;
        double confidence;
        std::chrono::system_clock::time_point timestamp;
        std::string reasoning;
    };

    // Neural Network Models
    class AINeuralNetwork {
    private:
        torch::nn::Sequential decision_network;
        torch::nn::Sequential prediction_network;
        torch::nn::Sequential behavior_network;
        bool initialized = false;

    public:
        AINeuralNetwork();
        ~AINeuralNetwork() = default;

        bool initialize(int input_size, int hidden_size, int output_size);
        torch::Tensor predict_decision(const torch::Tensor& input);
        torch::Tensor predict_behavior(const torch::Tensor& input);
        void train(const std::vector<torch::Tensor>& inputs, 
                  const std::vector<torch::Tensor>& targets, int epochs);
        void save_model(const std::string& filepath);
        bool load_model(const std::string& filepath);
        void update_learning_rate(double new_rate);
    };

    // Game State Analyzer
    class GameStateAnalyzer {
    private:
        std::map<std::string, double> current_state_metrics;
        std::vector<std::map<std::string, double>> historical_states;
        
    public:
        GameStateAnalyzer() = default;
        ~GameStateAnalyzer() = default;

        void analyze_state(const GameEngine* game_engine);
        void analyze_character(const Character* character);
        void analyze_company(const Company* company);
        
        std::map<std::string, double> get_state_metrics() const { return current_state_metrics; }
        std::vector<double> get_feature_vector() const;
        
        double calculate_threat_level(const std::string& target);
        double calculate_opportunity_score(const std::string& opportunity);
        double predict_success_probability(const AIDecision& decision);
        
        void update_historical_record();
        std::vector<std::vector<double>> get_time_series_data(int steps_back = 10);
    };

    // AI Agent
    class AIAgent {
    private:
        std::string agent_id;
        std::string agent_name;
        AIPersonality personality;
        AIBehaviorType current_behavior;
        
        std::unique_ptr<AINeuralNetwork> neural_network;
        std::unique_ptr<GameStateAnalyzer> state_analyzer;
        
        std::queue<AIDecision> decision_queue;
        std::map<std::string, double> memory_weights;
        std::vector<std::string> known_allies;
        std::vector<std::string> known_enemies;
        
        int experience_points = 0;
        int decisions_made = 0;
        int successful_decisions = 0;
        
        std::atomic<bool> active{true};

    public:
        AIAgent(const std::string& id, const std::string& name, const AIPersonality& personality);
        ~AIAgent() = default;

        // Core AI operations
        void initialize();
        void shutdown();
        void update_state(const GameEngine* game_engine);
        AIDecision make_decision();
        void execute_decision(const AIDecision& decision);
        void learn_from_outcome(const AIDecision& decision, bool success, double reward);
        
        // Personality and behavior
        void set_personality(const AIPersonality& new_personality) { personality = new_personality; }
        const AIPersonality& get_personality() const { return personality; }
        void update_behavior(AIBehaviorType new_behavior);
        AIBehaviorType get_current_behavior() const { return current_behavior; }
        
        // Memory and learning
        void update_memory(const std::string& event, double weight);
        void form_alliance(const std::string& target, double strength);
        void form_enemy(const std::string& target, double hostility);
        bool knows_alliance(const std::string& target) const;
        bool knows_enemy(const std::string& target) const;
        
        // Decision making
        std::vector<AIDecision> generate_possible_decisions();
        double evaluate_decision(const AIDecision& decision);
        AIDecision select_best_decision(const std::vector<AIDecision>& decisions);
        
        // Specialized AI functions
        AIDecision make_investment_decision();
        AIDecision make_hacking_decision();
        AIDecision make_defense_decision();
        AIDecision make_espionage_decision();
        
        // Agent status
        const std::string& get_agent_id() const { return agent_id; }
        const std::string& get_agent_name() const { return agent_name; }
        int get_experience() const { return experience_points; }
        double get_success_rate() const { 
            return decisions_made > 0 ? static_cast<double>(successful_decisions) / decisions_made : 0.0; 
        }
        
        void set_active(bool status) { active.store(status); }
        bool is_active() const { return active.load(); }
    };

    // Main AI System
    class AISystem {
    private:
        std::vector<std::unique_ptr<AIAgent>> agents;
        std::map<std::string, std::unique_ptr<AIAgent>> agent_map;
        
        std::unique_ptr<AINeuralNetwork> global_network;
        std::unique_ptr<GameStateAnalyzer> global_analyzer;
        
        std::thread ai_thread;
        std::mutex ai_mutex;
        std::atomic<bool> ai_running{false};
        std::atomic<bool> should_stop{false};
        
        // AI configuration
        int max_agents = 10;
        int decision_frequency_ms = 5000;
        double learning_rate = 0.001;
        int memory_size = 1000;
        
        // Performance metrics
        std::map<std::string, double> performance_metrics;
        int total_ai_decisions = 0;
        int successful_ai_decisions = 0;
        
        // Callbacks for game integration
        std::map<std::string, std::function<void(const AIDecision&)>> decision_callbacks;

    public:
        AISystem();
        ~AISystem();

        // System management
        bool initialize();
        void shutdown();
        void start_ai_processing();
        void stop_ai_processing();
        
        // Agent management
        std::string create_agent(const std::string& name, const AIPersonality& personality);
        void remove_agent(const std::string& agent_id);
        AIAgent* get_agent(const std::string& agent_id);
        std::vector<std::string> get_all_agent_ids() const;
        
        // AI processing
        void update_all_agents(const GameEngine* game_engine);
        void process_agent_decisions();
        void train_neural_networks();
        
        // Global AI functions
        void analyze_global_state(const GameEngine* game_engine);
        AIDecision get_global_recommendation();
        void coordinate_agent_actions();
        
        // Learning and adaptation
        void record_decision_outcome(const std::string& agent_id, const AIDecision& decision, 
                                   bool success, double reward);
        void adjust_difficulty();
        void evolve_ai_behaviors();
        
        // Advanced AI features
        void implement_reinforcement_learning();
        void use_genetic_algorithms();
        void apply_transfer_learning();
        void enable_meta_learning();
        
        // Configuration
        void set_max_agents(int max) { max_agents = max; }
        void set_decision_frequency(int frequency_ms) { decision_frequency_ms = frequency_ms; }
        void set_learning_rate(double rate) { learning_rate = rate; }
        void set_memory_size(int size) { memory_size = size; }
        
        // Monitoring and debugging
        std::map<std::string, double> get_performance_metrics() const { return performance_metrics; }
        double get_overall_success_rate() const;
        std::vector<std::string> get_ai_logs() const;
        void dump_ai_state() const;
        
        // Specialized AI systems
        void initialize_ghazarkhan_ai();
        void initialize_hacker_ai();
        void initialize_investor_ai();
        void initialize_law_enforcement_ai();
        
        // Callbacks
        void register_decision_callback(const std::string& decision_type, 
                                      std::function<void(const AIDecision&)> callback);

    private:
        // Internal methods
        void ai_worker_thread();
        void update_performance_metrics();
        void cleanup_inactive_agents();
        void save_ai_state();
        bool load_ai_state();
        
        // AI learning algorithms
        void apply_q_learning(AIAgent* agent, const AIDecision& decision, double reward);
        void apply_policy_gradient(AIAgent* agent, const std::vector<AIDecision>& decisions);
        void apply_evolutionary_pressure();
        
        // AI coordination
        std::vector<AIDecision> resolve_conflicting_decisions(const std::vector<AIDecision>& decisions);
        void synchronize_agent_memories();
    };

    // AI Factory for creating specialized agents
    class AIFactory {
    public:
        static std::unique_ptr<AIAgent> create_ghazarkhan_agent();
        static std::unique_ptr<AIAgent> create_hacker_agent();
        static std::unique_ptr<AIAgent> create_investor_agent();
        static std::unique_ptr<AIAgent> create_law_enforcement_agent();
        static std::unique_ptr<AIAgent> create_corporate_agent();
        static std::unique_ptr<AIAgent> create_player_companion_agent();
        
        static AIPersonality generate_random_personality();
        static AIPersonality generate_specialized_personality(const std::string& specialization);
    };

    // Advanced AI Features
    class AdvancedAI {
    public:
        // Natural Language Processing
        static std::string analyze_text_sentiment(const std::string& text);
        static std::vector<std::string> extract_entities(const std::string& text);
        static std::string generate_response(const std::string& input, const std::string& context);
        
        // Computer Vision (for potential visual features)
        static cv::Mat analyze_image(const cv::Mat& image);
        static std::vector<std::string> detect_objects(const cv::Mat& image);
        static bool verify_user_identity(const cv::Mat& face_image);
        
        // Predictive Analytics
        static std::vector<double> predict_market_trends(const std::vector<double>& historical_data);
        static double predict_security_threat(const std::map<std::string, double>& security_metrics);
        static std::vector<std::string> suggest_optimal_actions(const GameStateAnalyzer* analyzer);
    };

} // namespace AstraTechnica

#endif // ASTRATECHNICA_AI_SYSTEM_HPP