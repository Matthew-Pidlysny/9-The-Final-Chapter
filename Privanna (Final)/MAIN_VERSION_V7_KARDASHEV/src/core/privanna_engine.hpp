/*
 * Privanna Game Engine - Core System
 * Project Privanna - Massive Scale Implementation
 * 
 * Core engine coordinating all game systems
 * C++17 standard, enterprise-level architecture
 */

#ifndef PRIVANNA_ENGINE_HPP
#define PRIVANNA_ENGINE_HPP

#include <memory>
#include <vector>
#include <thread>
#include <atomic>
#include <chrono>
#include <mutex>
#include <condition_variable>

// Forward declarations for all major systems
namespace privanna {

class EventSystem;
class MemoryManager;
class ThreadingSystem;
class FactionManager;
class UnitManager;
class MagicSystem;
class AISystem;
class RenderSystem;
class AudioSystem;
class NetworkSystem;

// Core engine state enumeration
enum class EngineState {
    UNINITIALIZED,
    INITIALIZING,
    RUNNING,
    PAUSED,
    SHUTTING_DOWN,
    TERMINATED
};

// Engine configuration structure
struct EngineConfig {
    // Performance settings
    uint32_t target_fps = 60;
    uint32_t max_threads = 0;  // 0 = auto-detect
    size_t memory_pool_size = 1024 * 1024 * 1024;  // 1GB default
    
    // Graphics settings
    bool enable_vr = false;
    bool enable_4k = true;
    bool enable_ray_tracing = false;
    
    // AI settings
    bool enable_neural_networks = true;
    bool enable_learning_ai = true;
    std::string ai_model_path = "models/";
    
    // Network settings
    bool enable_multiplayer = true;
    uint16_t default_port = 7777;
    uint32_t max_players = 64;
    
    // Debug settings
    bool enable_debug_mode = false;
    bool enable_profiling = false;
    std::string log_level = "INFO";
};

// Main engine class - coordinates all subsystems
class PrivannaEngine {
private:
    // Core state
    std::atomic<EngineState> current_state_;
    EngineConfig config_;
    
    // System managers
    std::unique_ptr<EventSystem> event_system_;
    std::unique_ptr<MemoryManager> memory_manager_;
    std::unique_ptr<ThreadingSystem> threading_system_;
    
    // Game systems
    std::unique_ptr<FactionManager> faction_manager_;
    std::unique_ptr<UnitManager> unit_manager_;
    std::unique_ptr<MagicSystem> magic_system_;
    std::unique_ptr<AISystem> ai_system_;
    std::unique_ptr<RenderSystem> render_system_;
    std::unique_ptr<AudioSystem> audio_system_;
    std::unique_ptr<NetworkSystem> network_system_;
    
    // Timing
    std::chrono::high_resolution_clock::time_point last_frame_time_;
    std::chrono::duration<double> frame_time_accumulator_;
    double delta_time_ = 0.0;
    
    // Threading
    std::thread game_loop_thread_;
    std::thread render_thread_;
    std::thread ai_thread_;
    std::mutex engine_mutex_;
    std::condition_variable frame_condition_;
    std::atomic<bool> should_run_;
    
    // Performance monitoring
    uint32_t frame_count_ = 0;
    double fps_ = 0.0;
    std::chrono::duration<double> total_run_time_;
    
public:
    // Constructor/Destructor
    explicit PrivannaEngine(const EngineConfig& config = EngineConfig{});
    ~PrivannaEngine();
    
    // Engine lifecycle
    bool initialize();
    void start();
    void pause();
    void resume();
    void shutdown();
    void terminate();
    
    // State accessors
    EngineState get_state() const { return current_state_.load(); }
    bool is_running() const { return current_state_.load() == EngineState::RUNNING; }
    bool is_paused() const { return current_state_.load() == EngineState::PAUSED; }
    
    // System accessors
    EventSystem* get_event_system() const { return event_system_.get(); }
    MemoryManager* get_memory_manager() const { return memory_manager_.get(); }
    FactionManager* get_faction_manager() const { return faction_manager_.get(); }
    UnitManager* get_unit_manager() const { return unit_manager_.get(); }
    MagicSystem* get_magic_system() const { return magic_system_.get(); }
    AISystem* get_ai_system() const { return ai_system_.get(); }
    RenderSystem* get_render_system() const { return render_system_.get(); }
    AudioSystem* get_audio_system() const { return audio_system_.get(); }
    NetworkSystem* get_network_system() const { return network_system_.get(); }
    
    // Configuration
    const EngineConfig& get_config() const { return config_; }
    void update_config(const EngineConfig& new_config);
    
    // Performance monitoring
    double get_fps() const { return fps_; }
    uint32_t get_frame_count() const { return frame_count_; }
    double get_delta_time() const { return delta_time_; }
    std::chrono::duration<double> get_total_run_time() const { return total_run_time_; }
    
    // Divine data block access (faith-based system)
    void* access_divine_block();
    
private:
    // Core system initialization
    bool initialize_core_systems();
    bool initialize_game_systems();
    bool initialize_ai_systems();
    bool initialize_rendering();
    bool initialize_audio();
    bool initialize_networking();
    
    // Game loop
    void game_loop();
    void render_loop();
    void ai_loop();
    
    // Frame processing
    void update_frame_timing();
    void process_game_frame();
    void process_render_frame();
    void process_ai_frame();
    
    // System coordination
    void update_all_systems(double delta_time);
    void synchronize_systems();
    
    // Performance optimization
    void optimize_performance();
    void monitor_performance();
    void adjust_quality_settings();
    
    // Error handling
    void handle_critical_error(const std::string& error);
    void recover_from_error();
    
    // Memory management
    void cleanup_resources();
    void defragment_memory();
};

// Engine factory for different configurations
class EngineFactory {
public:
    static std::unique_ptr<PrivannaEngine> create_development_engine();
    static std::unique_ptr<PrivannaEngine> create_production_engine();
    static std::unique_ptr<PrivannaEngine> create_vr_engine();
    static std::unique_ptr<PrivannaEngine> create_server_engine();
    static std::unique_ptr<PrivannaEngine> create_ai_testing_engine();
};

// Global engine instance management
namespace engine {
    extern PrivannaEngine* g_engine;
    
    bool initialize(const EngineConfig& config = EngineConfig{});
    void shutdown();
    PrivannaEngine* get_instance();
    bool is_initialized();
}

} // namespace privanna

#endif // PRIVANNA_ENGINE_HPP