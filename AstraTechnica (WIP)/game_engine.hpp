#ifndef ASTRATECHNICA_GAME_ENGINE_HPP
#define ASTRATECHNICA_GAME_ENGINE_HPP

#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <memory>
#include <thread>
#include <mutex>
#include <chrono>
#include <ctime>
#include <random>
#include <atomic>
#include <queue>
#include <functional>
#include <condition_variable>

// AstraTechnica - EXTREMELY EPIC Game Engine
// "Pave the way for a greater tomorrow!"

namespace AstraTechnica {
    
    // Forward declarations
    class Character;
    class Company;
    class GameApp;
    class WorldMap;
    class PhoneIntegration;
    class AISystem;
    
    // Core game state
    enum class GameState {
        SETUP,
        PLAYING,
        COMPANY_MANAGEMENT,
        INVESTIGATION,
        ASSASSINATION,
        GAME_OVER,
        VICTORY
    };
    
    // Character stats (22 variables from document)
    struct CharacterStats {
        int intelligence = 0;
        int literacy = 0;
        int rationale = 0;
        int science = 0;
        int mathematics = 0;
        int obesity = 0;
        int wounds = 0;
        int happiness = 0;
        int entertainment = 0;
        int depression = 0;
        int stubbornness = 0;
        
        // Computer skills
        int legacy_hardware = 0;
        int modern_hardware = 0;
        int mobile_hardware = 0;
        int coding_protocols = 0;
        int network_configurations = 0;
        int server_management = 0;
        int virus_technology = 0;
        int laws_regulations = 0;
        int dark_web_knowledge = 0;
        int firewall_vpn_knowledge = 0;
        int hacker_techniques = 0;
    };
    
    // Crew member structure
    struct CrewMember {
        std::string name;
        std::string handle;
        int threat_rating = 1;    // 1-6
        int spirit = 1;           // 1-4
        int action = 1;           // 1-4
        int health = 1;           // 1-4
        int skill = 1;            // 1-4
        int unity = 1;            // 1-6
    };
    
    // Company structure
    struct Company {
        std::string name;
        std::string online_handle;
        double capital = 0.0;
        int employees = 0;
        int corruption = 0;
        
        // Systems
        int server_health = 100;
        int it_infrastructure = 50;
        int ai_processing_level = 1;
        
        // Asset pools
        std::vector<std::string> assets;
        std::vector<std::string> contracts;
        std::vector<std::string> active_orders;
    };
    
    // Asset Pool Tokens (21 types)
    enum class AssetToken {
        CONTRACT, SOFA, TV, SMARTPHONE, LAPTOP, COMPUTER, SERVER,
        SECURITY_CAMERA, VEHICLE, WEAPON, CHAIR, BED, BIKE,
        AI_ASSISTANT, WEBCAM, MICROPHONE, HEADSET, GAME_SYSTEM,
        MOVIE_PLAYER, MINING_RIG, VR_HEADSET, BOOKSHELF
    };
    
    // Main Game Engine
    class GameEngine {
    private:
        // Core systems
        std::unique_ptr<Character> player_character;
        std::unique_ptr<Company> player_company;
        std::unique_ptr<GameApp> game_app;
        std::unique_ptr<WorldMap> world_map;
        std::unique_ptr<PhoneIntegration> phone_integration;
        std::unique_ptr<AISystem> ai_system;
        
        // Game state
        GameState current_state = GameState::SETUP;
        int turn_counter = 0;
        bool game_running = false;
        std::atomic<bool> real_time_enabled{true};
        
        // Threading for real-time mechanics
        std::thread game_loop_thread;
        std::thread real_time_thread;
        std::mutex game_mutex;
        std::condition_variable game_cv;
        
        // Time management
        std::chrono::steady_clock::time_point last_update;
        std::chrono::milliseconds update_interval{1000}; // 1 second updates
        
        // Random number generation
        std::mt19937 rng;
        
        // Event queue
        std::queue<std::function<void()>> event_queue;
        std::mutex event_mutex;
        
        // The Ghazarkhan shadow government
        struct GhazarkhanSystem {
            bool discovered = false;
            int threat_level = 1;
            int influence_points = 0;
            std::vector<std::string> active_operations;
        } ghazarkhan;
        
    public:
        GameEngine();
        ~GameEngine();
        
        // Core initialization
        bool initialize();
        void shutdown();
        void run_game_loop();
        
        // Character management
        void create_character(const std::string& character_name);
        void update_character_stats();
        void apply_stat_changes(const CharacterStats& changes);
        
        // Company management
        void start_company(const std::string& company_name);
        void manage_company();
        void process_company_turn();
        
        // Real-time systems
        void start_real_time_processing();
        void update_world_state();
        void process_random_events();
        
        // Phone integration
        void initialize_phone_system();
        void send_push_notification(const std::string& title, const std::string& message);
        void handle_phone_response(const std::string& response);
        
        // AI integration
        void initialize_ai_systems();
        void process_ai_decisions();
        void update_ai_behaviors();
        
        // Game mechanics
        void process_turn();
        void handle_investigations();
        void process_ghazarkhan_actions();
        void check_win_conditions();
        
        // Asset management
        void add_asset(AssetToken token);
        void remove_asset(AssetToken token);
        bool has_asset(AssetToken token) const;
        
        // Event system
        void queue_event(std::function<void()> event);
        void process_event_queue();
        
        // Utility functions
        int random_int(int min, int max);
        double random_double(double min, double max);
        std::string generate_uuid();
        
        // State accessors
        GameState get_game_state() const { return current_state; }
        int get_turn_counter() const { return turn_counter; }
        bool is_game_running() const { return game_running; }
        
        // File I/O
        bool save_game_state(const std::string& filename);
        bool load_game_state(const std::string& filename);
    };
    
    // Utility functions
    std::string asset_token_to_string(AssetToken token);
    AssetToken string_to_asset_token(const std::string& token_str);
    std::string game_state_to_string(GameState state);
    
} // namespace AstraTechnica

#endif // ASTRATECHNICA_GAME_ENGINE_HPP