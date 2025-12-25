/*
 * Privanna Game Engine - Core Implementation
 * Implementation of the main engine coordination system
 */

#include "privanna_engine.hpp"
#include "../systems/event_system.hpp"
#include "../systems/memory_manager.hpp"
#include "../systems/threading_system.hpp"
#include "../game/faction_manager.hpp"
#include "../game/unit_manager.hpp"
#include "../game/magic_system.hpp"
#include "../ai/ai_system.hpp"
#include "../render/render_system.hpp"
#include "../audio/audio_system.hpp"
#include "../network/network_system.hpp"
#include "../utils/logger.hpp"
#include "divine_data_block.h"

#include <algorithm>
#include <iostream>

namespace privanna {

// Global engine instance
PrivannaEngine* engine::g_engine = nullptr;

// Constructor
PrivannaEngine::PrivannaEngine(const EngineConfig& config)
    : current_state_(EngineState::UNINITIALIZED)
    , config_(config)
    , should_run_(false)
    , frame_time_accumulator_(0)
    , total_run_time_(0) {
    
    // Auto-detect thread count if not specified
    if (config_.max_threads == 0) {
        config_.max_threads = std::thread::hardware_concurrency();
    }
    
    logger::info("Privanna Engine constructor called with configuration:");
    logger::info("  Target FPS: {}", config_.target_fps);
    logger::info("  Max Threads: {}", config_.max_threads);
    logger::info("  Memory Pool: {} MB", config_.memory_pool_size / (1024 * 1024));
    logger::info("  AI Enabled: {}", config_.enable_neural_networks);
    logger::info("  Multiplayer Enabled: {}", config_.enable_multiplayer);
}

// Destructor
PrivannaEngine::~PrivannaEngine() {
    if (is_running() || is_paused()) {
        shutdown();
    }
    terminate();
}

// Initialize all engine systems
bool PrivannaEngine::initialize() {
    logger::info("Initializing Privanna Engine...");
    
    current_state_.store(EngineState::INITIALIZING);
    
    try {
        // Initialize core systems first
        if (!initialize_core_systems()) {
            logger::error("Failed to initialize core systems");
            return false;
        }
        
        // Initialize game systems
        if (!initialize_game_systems()) {
            logger::error("Failed to initialize game systems");
            return false;
        }
        
        // Initialize AI systems
        if (!initialize_ai_systems()) {
            logger::error("Failed to initialize AI systems");
            return false;
        }
        
        // Initialize rendering
        if (!initialize_rendering()) {
            logger::error("Failed to initialize rendering");
            return false;
        }
        
        // Initialize audio
        if (!initialize_audio()) {
            logger::error("Failed to initialize audio");
            return false;
        }
        
        // Initialize networking
        if (config_.enable_multiplayer && !initialize_networking()) {
            logger::error("Failed to initialize networking");
            return false;
        }
        
        // Initialize divine data block
        access_divine_block();
        
        current_state_.store(EngineState::RUNNING);
        logger::info("Privanna Engine initialized successfully!");
        
        return true;
        
    } catch (const std::exception& e) {
        logger::error("Engine initialization failed: {}", e.what());
        handle_critical_error(e.what());
        return false;
    }
}

// Initialize core systems
bool PrivannaEngine::initialize_core_systems() {
    logger::info("Initializing core systems...");
    
    try {
        // Event system first - everything depends on it
        event_system_ = std::make_unique<EventSystem>();
        if (!event_system_->initialize()) {
            return false;
        }
        
        // Memory manager for optimal resource usage
        memory_manager_ = std::make_unique<MemoryManager>(config_.memory_pool_size);
        if (!memory_manager_->initialize()) {
            return false;
        }
        
        // Threading system for parallel processing
        threading_system_ = std::make_unique<ThreadingSystem>(config_.max_threads);
        if (!threading_system_->initialize()) {
            return false;
        }
        
        logger::info("Core systems initialized successfully");
        return true;
        
    } catch (const std::exception& e) {
        logger::error("Core system initialization failed: {}", e.what());
        return false;
    }
}

// Initialize game systems
bool PrivannaEngine::initialize_game_systems() {
    logger::info("Initializing game systems...");
    
    try {
        // Faction manager for 9 major factions
        faction_manager_ = std::make_unique<FactionManager>();
        if (!faction_manager_->initialize()) {
            return false;
        }
        
        // Unit manager for 15+ unit types
        unit_manager_ = std::make_unique<UnitManager>();
        if (!unit_manager_->initialize()) {
            return false;
        }
        
        // Magic system for 20+ magic dice types
        magic_system_ = std::make_unique<MagicSystem>();
        if (!magic_system_->initialize()) {
            return false;
        }
        
        logger::info("Game systems initialized successfully");
        return true;
        
    } catch (const std::exception& e) {
        logger::error("Game system initialization failed: {}", e.what());
        return false;
    }
}

// Initialize AI systems
bool PrivannaEngine::initialize_ai_systems() {
    logger::info("Initializing AI systems...");
    
    try {
        // AI system with PyTorch integration
        ai_system_ = std::make_unique<AISystem>(config_);
        if (!ai_system_->initialize()) {
            return false;
        }
        
        logger::info("AI systems initialized successfully");
        return true;
        
    } catch (const std::exception& e) {
        logger::error("AI system initialization failed: {}", e.what());
        return false;
    }
}

// Initialize rendering system
bool PrivannaEngine::initialize_rendering() {
    logger::info("Initializing rendering system...");
    
    try {
        render_system_ = std::make_unique<RenderSystem>(config_);
        if (!render_system_->initialize()) {
            return false;
        }
        
        logger::info("Rendering system initialized successfully");
        return true;
        
    } catch (const std::exception& e) {
        logger::error("Rendering system initialization failed: {}", e.what());
        return false;
    }
}

// Initialize audio system
bool PrivannaEngine::initialize_audio() {
    logger::info("Initializing audio system...");
    
    try {
        audio_system_ = std::make_unique<AudioSystem>();
        if (!audio_system_->initialize()) {
            return false;
        }
        
        logger::info("Audio system initialized successfully");
        return true;
        
    } catch (const std::exception& e) {
        logger::error("Audio system initialization failed: {}", e.what());
        return false;
    }
}

// Initialize networking system
bool PrivannaEngine::initialize_networking() {
    logger::info("Initializing networking system...");
    
    try {
        network_system_ = std::make_unique<NetworkSystem>(config_);
        if (!network_system_->initialize()) {
            return false;
        }
        
        logger::info("Networking system initialized successfully");
        return true;
        
    } catch (const std::exception& e) {
        logger::error("Networking system initialization failed: {}", e.what());
        return false;
    }
}

// Start the engine
void PrivannaEngine::start() {
    if (current_state_.load() != EngineState::RUNNING) {
        logger::error("Engine must be initialized before starting");
        return;
    }
    
    logger::info("Starting Privanna Engine...");
    should_run_ = true;
    last_frame_time_ = std::chrono::high_resolution_clock::now();
    
    // Start worker threads
    game_loop_thread_ = std::thread(&PrivannaEngine::game_loop, this);
    render_thread_ = std::thread(&PrivannaEngine::render_loop, this);
    
    if (config_.enable_neural_networks) {
        ai_thread_ = std::thread(&PrivannaEngine::ai_loop, this);
    }
    
    logger::info("Privanna Engine started successfully");
}

// Main game loop
void PrivannaEngine::game_loop() {
    logger::info("Game loop started");
    
    while (should_run_) {
        if (current_state_.load() == EngineState::RUNNING) {
            update_frame_timing();
            process_game_frame();
        }
        
        // Frame rate limiting
        std::chrono::duration<double> frame_duration(1.0 / config_.target_fps);
        std::this_thread::sleep_for(frame_duration - delta_time_);
    }
    
    logger::info("Game loop ended");
}

// Render loop
void PrivannaEngine::render_loop() {
    logger::info("Render loop started");
    
    while (should_run_) {
        if (current_state_.load() == EngineState::RUNNING) {
            process_render_frame();
        }
        
        // Render at target FPS
        std::chrono::duration<double> frame_duration(1.0 / config_.target_fps);
        std::this_thread::sleep_for(frame_duration);
    }
    
    logger::info("Render loop ended");
}

// AI processing loop
void PrivannaEngine::ai_loop() {
    logger::info("AI loop started");
    
    while (should_run_) {
        if (current_state_.load() == EngineState::RUNNING) {
            process_ai_frame();
        }
        
        // AI processing at lower frequency (30 FPS)
        std::chrono::duration<double> ai_frame_duration(1.0 / 30.0);
        std::this_thread::sleep_for(ai_frame_duration);
    }
    
    logger::info("AI loop ended");
}

// Update frame timing
void PrivannaEngine::update_frame_timing() {
    auto current_time = std::chrono::high_resolution_clock::now();
    delta_time_ = std::chrono::duration<double>(current_time - last_frame_time_).count();
    last_frame_time_ = current_time;
    
    frame_time_accumulator_ += delta_time_;
    total_run_time_ += delta_time_;
    frame_count_++;
    
    // Update FPS every second
    if (frame_time_accumulator_ >= 1.0) {
        fps_ = frame_count_ / frame_time_accumulator_.count();
        frame_count_ = 0;
        frame_time_accumulator_ = std::chrono::duration<double>(0);
        
        // Performance monitoring
        if (config_.enable_profiling) {
            monitor_performance();
        }
    }
}

// Process game frame
void PrivannaEngine::process_game_frame() {
    try {
        update_all_systems(delta_time_);
        synchronize_systems();
        
    } catch (const std::exception& e) {
        logger::error("Game frame processing error: {}", e.what());
        handle_critical_error(e.what());
    }
}

// Process render frame
void PrivannaEngine::process_render_frame() {
    try {
        if (render_system_) {
            render_system_->render_frame(delta_time_);
        }
        
    } catch (const std::exception& e) {
        logger::error("Render frame processing error: {}", e.what());
    }
}

// Process AI frame
void PrivannaEngine::process_ai_frame() {
    try {
        if (ai_system_) {
            ai_system_->process_ai_frame(delta_time_);
        }
        
    } catch (const std::exception& e) {
        logger::error("AI frame processing error: {}", e.what());
    }
}

// Update all systems
void PrivannaEngine::update_all_systems(double delta_time) {
    // Update game systems
    if (faction_manager_) faction_manager_->update(delta_time);
    if (unit_manager_) unit_manager_->update(delta_time);
    if (magic_system_) magic_system_->update(delta_time);
    
    // Process network events
    if (network_system_) network_system_->process_events();
    
    // Update audio
    if (audio_system_) audio_system_->update(delta_time);
}

// Synchronize systems
void PrivannaEngine::synchronize_systems() {
    // Process any pending events
    if (event_system_) {
        event_system_->process_events();
    }
}

// Access divine data block (faith-based system)
void* PrivannaEngine::access_divine_block() {
    logger::info("Accessing divine data block through prayer...");
    
    // Allocate and initialize the divine block
    static DivineDataBlock* divine_block = nullptr;
    if (!divine_block) {
        divine_block = new DivineDataBlock();
        
        // Initialize with sacred bounds
        memset(divine_block, 0, sizeof(DivineDataBlock));
        
        logger::info("Divine data block initialized and ready for revelation");
    }
    
    return divine_block;
}

// Performance monitoring
void PrivannaEngine::monitor_performance() {
    if (fps_ < config_.target_fps * 0.9) {
        logger::warn("Performance warning: FPS = {:.1f} (target: {})", fps_, config_.target_fps);
        optimize_performance();
    }
}

// Performance optimization
void PrivannaEngine::optimize_performance() {
    // Memory defragmentation
    if (frame_count_ % 600 == 0) {  // Every 10 seconds at 60 FPS
        defragment_memory();
    }
    
    // Adjust quality settings
    if (fps_ < config_.target_fps * 0.8) {
        adjust_quality_settings();
    }
}

// Memory defragmentation
void PrivannaEngine::defragment_memory() {
    if (memory_manager_) {
        memory_manager_->defragment();
        logger::debug("Memory defragmentation completed");
    }
}

// Adjust quality settings
void PrivannaEngine::adjust_quality_settings() {
    // Implementation for dynamic quality adjustment
    logger::info("Adjusting quality settings for better performance");
}

// Handle critical errors
void PrivannaEngine::handle_critical_error(const std::string& error) {
    logger::error("CRITICAL ERROR: {}", error);
    
    // Attempt recovery
    recover_from_error();
}

// Error recovery
void PrivannaEngine::recover_from_error() {
    logger::info("Attempting error recovery...");
    
    // Implementation for error recovery
    // This would typically involve resetting systems to a safe state
}

// Pause the engine
void PrivannaEngine::pause() {
    if (current_state_.load() == EngineState::RUNNING) {
        current_state_.store(EngineState::PAUSED);
        logger::info("Engine paused");
    }
}

// Resume the engine
void PrivannaEngine::resume() {
    if (current_state_.load() == EngineState::PAUSED) {
        current_state_.store(EngineState::RUNNING);
        logger::info("Engine resumed");
    }
}

// Shutdown the engine
void PrivannaEngine::shutdown() {
    if (current_state_.load() == EngineState::TERMINATED) {
        return;
    }
    
    logger::info("Shutting down Privanna Engine...");
    current_state_.store(EngineState::SHUTTING_DOWN);
    should_run_ = false;
    
    // Wait for threads to finish
    if (game_loop_thread_.joinable()) {
        game_loop_thread_.join();
    }
    if (render_thread_.joinable()) {
        render_thread_.join();
    }
    if (ai_thread_.joinable()) {
        ai_thread_.join();
    }
    
    cleanup_resources();
    
    current_state_.store(EngineState::TERMINATED);
    logger::info("Privanna Engine shutdown complete");
}

// Terminate the engine
void PrivannaEngine::terminate() {
    cleanup_resources();
    current_state_.store(EngineState::TERMINATED);
}

// Clean up resources
void PrivannaEngine::cleanup_resources() {
    logger::info("Cleaning up engine resources...");
    
    // Shutdown in reverse order of initialization
    network_system_.reset();
    audio_system_.reset();
    render_system_.reset();
    ai_system_.reset();
    magic_system_.reset();
    unit_manager_.reset();
    faction_manager_.reset();
    threading_system_.reset();
    memory_manager_.reset();
    event_system_.reset();
    
    logger::info("Resource cleanup completed");
}

// Update configuration
void PrivannaEngine::update_config(const EngineConfig& new_config) {
    config_ = new_config;
    logger::info("Engine configuration updated");
}

// Engine factory implementations
std::unique_ptr<PrivannaEngine> EngineFactory::create_development_engine() {
    EngineConfig config;
    config.enable_debug_mode = true;
    config.enable_profiling = true;
    config.log_level = "DEBUG";
    return std::make_unique<PrivannaEngine>(config);
}

std::unique_ptr<PrivannaEngine> EngineFactory::create_production_engine() {
    EngineConfig config;
    config.enable_debug_mode = false;
    config.enable_profiling = false;
    config.log_level = "INFO";
    config.enable_vr = false;
    return std::make_unique<PrivannaEngine>(config);
}

std::unique_ptr<PrivannaEngine> EngineFactory::create_vr_engine() {
    EngineConfig config;
    config.enable_vr = true;
    config.target_fps = 90;  // VR requires higher FPS
    config.enable_4k = false;
    return std::make_unique<PrivannaEngine>(config);
}

std::unique_ptr<PrivannaEngine> EngineFactory::create_server_engine() {
    EngineConfig config;
    config.enable_multiplayer = true;
    config.max_players = 1000;
    config.enable_neural_networks = false;  // Servers don't need AI
    return std::make_unique<PrivannaEngine>(config);
}

std::unique_ptr<PrivannaEngine> EngineFactory::create_ai_testing_engine() {
    EngineConfig config;
    config.enable_neural_networks = true;
    config.enable_learning_ai = true;
    config.enable_debug_mode = true;
    config.enable_profiling = true;
    return std::make_unique<PrivannaEngine>(config);
}

// Global engine instance management
namespace engine {
    bool initialize(const EngineConfig& config) {
        if (g_engine) {
            logger::warn("Engine already initialized");
            return true;
        }
        
        g_engine = new PrivannaEngine(config);
        return g_engine->initialize();
    }
    
    void shutdown() {
        if (g_engine) {
            g_engine->shutdown();
            delete g_engine;
            g_engine = nullptr;
        }
    }
    
    PrivannaEngine* get_instance() {
        return g_engine;
    }
    
    bool is_initialized() {
        return g_engine != nullptr && g_engine->get_state() != EngineState::UNINITIALIZED;
    }
}

} // namespace privanna