#include "game_engine.hpp"
#include "game_app.hpp"
#include "world_map.hpp"
#include "../character/character_system.hpp"
#include "../phone/phone_integration.hpp"
#include "../ai/ai_system.hpp"
#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <ctime>
#include <random>
#include <thread>
#include <chrono>
#include <iomanip>

namespace AstraTechnica {

    // Utility functions
    std::string asset_token_to_string(AssetToken token) {
        switch (token) {
            case AssetToken::CONTRACT: return "Contract";
            case AssetToken::SOFA: return "Sofa";
            case AssetToken::TV: return "TV";
            case AssetToken::SMARTPHONE: return "Smartphone";
            case AssetToken::LAPTOP: return "Laptop";
            case AssetToken::COMPUTER: return "Computer";
            case AssetToken::SERVER: return "Server";
            case AssetToken::SECURITY_CAMERA: return "Security Camera";
            case AssetToken::VEHICLE: return "Vehicle";
            case AssetToken::WEAPON: return "Weapon";
            case AssetToken::CHAIR: return "Chair";
            case AssetToken::BED: return "Bed";
            case AssetToken::BIKE: return "Bike";
            case AssetToken::AI_ASSISTANT: return "AI Assistant";
            case AssetToken::WEBCAM: return "Webcam";
            case AssetToken::MICROPHONE: return "Microphone";
            case AssetToken::HEADSET: return "Headset";
            case AssetToken::GAME_SYSTEM: return "Game System";
            case AssetToken::MOVIE_PLAYER: return "Movie Player";
            case AssetToken::MINING_RIG: return "Mining Rig";
            case AssetToken::VR_HEADSET: return "VR Headset";
            case AssetToken::BOOKSHELF: return "Bookshelf";
            default: return "Unknown";
        }
    }

    AssetToken string_to_asset_token(const std::string& token_str) {
        if (token_str == "Contract") return AssetToken::CONTRACT;
        if (token_str == "Sofa") return AssetToken::SOFA;
        if (token_str == "TV") return AssetToken::TV;
        if (token_str == "Smartphone") return AssetToken::SMARTPHONE;
        if (token_str == "Laptop") return AssetToken::LAPTOP;
        if (token_str == "Computer") return AssetToken::COMPUTER;
        if (token_str == "Server") return AssetToken::SERVER;
        if (token_str == "Security Camera") return AssetToken::SECURITY_CAMERA;
        if (token_str == "Vehicle") return AssetToken::VEHICLE;
        if (token_str == "Weapon") return AssetToken::WEAPON;
        if (token_str == "Chair") return AssetToken::CHAIR;
        if (token_str == "Bed") return AssetToken::BED;
        if (token_str == "Bike") return AssetToken::BIKE;
        if (token_str == "AI Assistant") return AssetToken::AI_ASSISTANT;
        if (token_str == "Webcam") return AssetToken::WEBCAM;
        if (token_str == "Microphone") return AssetToken::MICROPHONE;
        if (token_str == "Headset") return AssetToken::HEADSET;
        if (token_str == "Game System") return AssetToken::GAME_SYSTEM;
        if (token_str == "Movie Player") return AssetToken::MOVIE_PLAYER;
        if (token_str == "Mining Rig") return AssetToken::MINING_RIG;
        if (token_str == "VR Headset") return AssetToken::VR_HEADSET;
        if (token_str == "Bookshelf") return AssetToken::BOOKSHELF;
        return AssetToken::CONTRACT; // Default
    }

    std::string game_state_to_string(GameState state) {
        switch (state) {
            case GameState::SETUP: return "Setup";
            case GameState::PLAYING: return "Playing";
            case GameState::COMPANY_MANAGEMENT: return "Company Management";
            case GameState::INVESTIGATION: return "Investigation";
            case GameState::ASSASSINATION: return "Assassination";
            case GameState::GAME_OVER: return "Game Over";
            case GameState::VICTORY: return "Victory";
            default: return "Unknown";
        }
    }

    // GameEngine Implementation
    GameEngine::GameEngine() : rng(std::random_device{}()) {
        last_update = std::chrono::steady_clock::now();
        std::cout << "Game Engine initialized" << std::endl;
    }

    GameEngine::~GameEngine() {
        shutdown();
    }

    bool GameEngine::initialize() {
        try {
            std::cout << "Initializing AstraTechnica Game Engine..." << std::endl;
            
            // Initialize core systems
            game_app = std::make_unique<GameApp>();
            world_map = std::make_unique<WorldMap>();
            ai_system = std::make_unique<AISystem>();
            phone_integration = std::make_unique<PhoneIntegration>();
            
            // Initialize phone integration
            if (!phone_integration->initialize()) {
                std::cerr << "Warning: Failed to initialize phone integration" << std::endl;
            }
            
            // Initialize AI system
            if (!ai_system->initialize()) {
                std::cerr << "Warning: Failed to initialize AI system" << std::endl;
            }
            
            // Set game state to setup
            current_state = GameState::SETUP;
            turn_counter = 0;
            
            std::cout << "Game Engine initialized successfully!" << std::endl;
            return true;
            
        } catch (const std::exception& e) {
            std::cerr << "Failed to initialize game engine: " << e.what() << std::endl;
            return false;
        }
    }

    void GameEngine::shutdown() {
        std::cout << "Shutting down game engine..." << std::endl;
        
        game_running = false;
        should_stop.store(true);
        
        // Stop threads
        if (game_loop_thread.joinable()) {
            game_loop_thread.join();
        }
        
        if (real_time_thread.joinable()) {
            real_time_thread.join();
        }
        
        // Shutdown subsystems
        if (phone_integration) {
            phone_integration->shutdown();
        }
        
        if (ai_system) {
            ai_system->shutdown();
        }
        
        std::cout << "Game engine shutdown complete" << std::endl;
    }

    void GameEngine::run_game_loop() {
        game_running = true;
        
        // Start real-time processing
        start_real_time_processing();
        
        // Start AI processing
        if (ai_system) {
            ai_system->start_ai_processing();
        }
        
        std::cout << "\n=== ASTRATECHICA GAME START ===" << std::endl;
        std::cout << "Time passes in real-time... Phone notifications enabled!" << std::endl;
        std::cout << "AI systems are monitoring your progress..." << std::endl;
        std::cout << "The Ghazarkhan watches from the shadows..." << std::endl;
        
        // Main game loop
        while (game_running) {
            try {
                // Process events
                process_event_queue();
                
                // Update game state based on current state
                switch (current_state) {
                    case GameState::SETUP:
                        // Setup phase - wait for character creation
                        std::this_thread::sleep_for(std::chrono::milliseconds(100));
                        break;
                        
                    case GameState::PLAYING:
                        process_turn();
                        break;
                        
                    case GameState::COMPANY_MANAGEMENT:
                        process_company_turn();
                        break;
                        
                    case GameState::INVESTIGATION:
                        handle_investigations();
                        break;
                        
                    case GameState::ASSASSINATION:
                        // Handle assassination mechanics
                        break;
                        
                    case GameState::GAME_OVER:
                    case GameState::VICTORY:
                        game_running = false;
                        break;
                }
                
                // Check win conditions
                check_win_conditions();
                
                // Update world state
                update_world_state();
                
                // Small delay to prevent CPU spinning
                std::this_thread::sleep_for(std::chrono::milliseconds(50));
                
            } catch (const std::exception& e) {
                std::cerr << "Error in game loop: " << e.what() << std::endl;
                // Continue running despite errors
            }
        }
        
        std::cout << "\n=== GAME LOOP ENDED ===" << std::endl;
    }

    void GameEngine::create_character(const std::string& character_name) {
        auto factory = CharacterFactory::create_character(character_name);
        if (factory) {
            player_character = std::move(factory);
            std::cout << "Character created: " << player_character->get_name() << std::endl;
            std::cout << "Handle: " << player_character->get_handle() << std::endl;
            std::cout << "Starting Money: $" << player_character->get_money() << std::endl;
            std::cout << "Hunger Level: " << player_character->get_hunger() << "/100" << std::endl;
            
            // Send phone notification
            if (phone_integration) {
                phone_integration->send_notification(
                    "Welcome to AstraTechnica", 
                    "Your character " + player_character->get_name() + " is ready!",
                    4, "character"
                );
            }
            
            current_state = GameState::PLAYING;
        } else {
            std::cerr << "Failed to create character: " << character_name << std::endl;
        }
    }

    void GameEngine::start_company(const std::string& company_name) {
        if (!player_character) {
            std::cerr << "Cannot start company without character" << std::endl;
            return;
        }
        
        if (!player_character->can_start_company()) {
            std::cout << "Character cannot start company yet" << std::endl;
            return;
        }
        
        player_company = std::make_unique<Company>();
        player_company->name = company_name;
        player_company->employees = 1;
        player_company->capital = player_character->get_money() * 0.5; // Use half the money
        
        player_character->spend_money(player_company->capital);
        
        current_state = GameState::COMPANY_MANAGEMENT;
        
        std::cout << "Company started: " << company_name << std::endl;
        std::cout << "Initial Capital: $" << player_company->capital << std::endl;
        
        // Send phone notification
        if (phone_integration) {
            phone_integration->notify_company_event("Company Founded", {
                {"name", company_name},
                {"capital", std::to_string(player_company->capital)}
            });
        }
    }

    void GameEngine::process_turn() {
        // Basic turn processing
        static int turn_counter_local = 0;
        turn_counter_local++;
        
        if (turn_counter_local % 100 == 0) { // Every 5 seconds at 50ms intervals
            turn_counter++;
            
            // Send turn notification
            if (phone_integration && turn_counter % 10 == 0) {
                phone_integration->notify_turn_update(turn_counter);
            }
            
            // Process random events
            if (turn_counter % 20 == 0) {
                process_random_events();
            }
            
            // Ghazarkhan activities
            if (turn_counter % 30 == 0) {
                process_ghazarkhan_actions();
            }
        }
    }

    void GameEngine::process_company_turn() {
        if (!player_company) return;
        
        static int company_turn_counter = 0;
        company_turn_counter++;
        
        // Generate revenue every few turns
        if (company_turn_counter % 50 == 0) {
            double revenue = player_company->capital * 0.01; // 1% growth
            player_company->capital += revenue;
            
            if (phone_integration && company_turn_counter % 200 == 0) {
                phone_integration->notify_company_event("Revenue Generated", {
                    {"amount", std::to_string(revenue)},
                    {"total", std::to_string(player_company->capital)}
                });
            }
        }
        
        // Regular turn processing
        process_turn();
    }

    void GameEngine::start_real_time_processing() {
        real_time_enabled.store(true);
        real_time_thread = std::thread([this]() {
            while (real_time_enabled.load()) {
                auto now = std::chrono::steady_clock::now();
                
                if (now - last_update >= update_interval) {
                    update_world_state();
                    last_update = now;
                }
                
                std::this_thread::sleep_for(std::chrono::milliseconds(100));
            }
        });
    }

    void GameEngine::update_world_state() {
        // Update character hunger and basic needs
        if (player_character && turn_counter % 1000 == 0) { // Every ~50 seconds
            player_character->modify_hunger(1);
            
            if (player_character->get_hunger() > 70) {
                player_character->modify_stat("happiness", -1);
                player_character->modify_stat("depression", 1);
            }
        }
        
        // Update company status
        if (player_company && turn_counter % 500 == 0) { // Every ~25 seconds
            // Random events can affect company
            if (random_int(1, 100) <= 5) { // 5% chance
                player_company->server_health = std::max(0, player_company->server_health - 5);
                player_company->corruption = std::min(100, player_company->corruption + 1);
            }
        }
        
        // AI updates
        if (ai_system && turn_counter % 200 == 0) { // Every ~10 seconds
            ai_system->update_all_agents(this);
        }
    }

    void GameEngine::process_random_events() {
        int event_type = random_int(1, 10);
        
        switch (event_type) {
            case 1: // Market fluctuation
                if (player_character) {
                    double change = random_double(-1000, 1000);
                    player_character->add_money(change);
                    
                    if (phone_integration && abs(change) > 500) {
                        phone_integration->notify_market_change("Cash", 
                            player_character->get_money() - change, 
                            player_character->get_money());
                    }
                }
                break;
                
            case 2: // Server issue
                if (player_company && player_company->server_health > 50) {
                    player_company->server_health -= random_int(5, 15);
                    
                    if (phone_integration) {
                        phone_integration->notify_server_status("main", player_company->server_health, "Degraded");
                    }
                }
                break;
                
            case 3: // Good fortune
                if (player_character) {
                    player_character->modify_stat("happiness", 5);
                    player_character->modify_stat("entertainment", 3);
                }
                break;
                
            default:
                // No event
                break;
        }
    }

    void GameEngine::process_ghazarkhan_actions() {
        // Initialize Ghazarkhan system if not discovered
        if (!ghazarkhan.discovered && turn_counter > 100) {
            ghazarkhan.discovered = true;
            ghazarkhan.threat_level = 1;
            
            if (phone_integration) {
                phone_integration->notify_ghazarkhan_activity("Shadow organization detected", 3);
            }
        }
        
        if (ghazarkhan.discovered) {
            // Increase threat over time
            if (turn_counter % 100 == 0) {
                ghazarkhan.threat_level = std::min(10, ghazarkhan.threat_level + 1);
                
                int action = random_int(1, 3);
                switch (action) {
                    case 1:
                        if (phone_integration) {
                            phone_integration->notify_hack_attempt("Unknown Source", ghazarkhan.threat_level);
                        }
                        break;
                    case 2:
                        if (player_company) {
                            player_company->corruption = std::min(100, player_company->corruption + 2);
                        }
                        break;
                    default:
                        break;
                }
            }
        }
    }

    void GameEngine::handle_investigations() {
        // Investigation mechanics
        if (player_company && player_company->corruption > 50) {
            // High corruption triggers investigations
            if (random_int(1, 100) <= 10) { // 10% chance per check
                if (phone_integration) {
                    phone_integration->notify_investigation_update("Authorities are investigating your company");
                }
                
                // Reset some corruption to show investigation "working"
                player_company->corruption = std::max(0, player_company->corruption - 10);
            }
        }
    }

    void GameEngine::check_win_conditions() {
        // Victory condition: Company success and global installation
        if (player_company && player_company->capital > 1000000) {
            // Simple win condition for demo
            current_state = GameState::VICTORY;
            
            if (phone_integration) {
                phone_integration->send_critical_alert("VICTORY!", 
                    "Your company has achieved global success! You've paved the way for a greater tomorrow!");
            }
            
            std::cout << "\n🎉 VICTORY! 🎉" << std::endl;
            std::cout << "Your company has achieved global domination!" << std::endl;
        }
        
        // Game over conditions
        if (player_character && !player_character->get_alive()) {
            current_state = GameState::GAME_OVER;
            std::cout << "\n💀 GAME OVER 💀" << std::endl;
        }
    }

    void GameEngine::queue_event(std::function<void()> event) {
        std::lock_guard<std::mutex> lock(event_mutex);
        event_queue.push(event);
    }

    void GameEngine::process_event_queue() {
        std::lock_guard<std::mutex> lock(event_mutex);
        
        while (!event_queue.empty()) {
            auto event = event_queue.front();
            event_queue.pop();
            
            try {
                event();
            } catch (const std::exception& e) {
                std::cerr << "Error processing event: " << e.what() << std::endl;
            }
        }
    }

    int GameEngine::random_int(int min, int max) {
        std::uniform_int_distribution<int> dist(min, max);
        return dist(rng);
    }

    double GameEngine::random_double(double min, double max) {
        std::uniform_real_distribution<double> dist(min, max);
        return dist(rng);
    }

    std::string GameEngine::generate_uuid() {
        std::ostringstream oss;
        oss << std::hex << std::time(nullptr) << "_" << random_int(1000, 9999);
        return oss.str();
    }

    bool GameEngine::save_game_state(const std::string& filename) {
        try {
            std::ofstream file(filename);
            if (!file.is_open()) return false;
            
            file << "turn_counter:" << turn_counter << std::endl;
            file << "game_state:" << game_state_to_string(current_state) << std::endl;
            
            if (player_character) {
                file << "character:" << player_character->serialize() << std::endl;
            }
            
            if (player_company) {
                file << "company:" << player_company->name << std::endl;
                file << "capital:" << player_company->capital << std::endl;
            }
            
            return true;
        } catch (...) {
            return false;
        }
    }

    bool GameEngine::load_game_state(const std::string& filename) {
        try {
            std::ifstream file(filename);
            if (!file.is_open()) return false;
            
            std::string line;
            while (std::getline(file, line)) {
                size_t pos = line.find(':');
                if (pos != std::string::npos) {
                    std::string key = line.substr(0, pos);
                    std::string value = line.substr(pos + 1);
                    
                    if (key == "turn_counter") {
                        turn_counter = std::stoi(value);
                    }
                    // Add more deserialization as needed
                }
            }
            
            return true;
        } catch (...) {
            return false;
        }
    }

    // Asset management
    void GameEngine::add_asset(AssetToken token) {
        if (player_character) {
            player_character->add_asset(token);
        }
    }

    void GameEngine::remove_asset(AssetToken token) {
        if (player_character) {
            player_character->remove_asset(token);
        }
    }

    bool GameEngine::has_asset(AssetToken token) const {
        return player_character ? player_character->has_asset(token) : false;
    }

} // namespace AstraTechnica