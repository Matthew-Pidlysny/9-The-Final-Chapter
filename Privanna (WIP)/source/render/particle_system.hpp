/*
 * Particle System - GPU-Accelerated Visual Effects
 * Millions of particles with physics simulation
 */

#ifndef PARTICLE_SYSTEM_HPP
#define PARTICLE_SYSTEM_HPP

#include <memory>
#include <vector>
#include <cstdint>
#include <atomic>
#include <mutex>
#include "../utils/math_utils.hpp"

namespace privanna::render {

// Particle properties
struct alignas(32) Particle {
    // Position and velocity
    alignas(16) math::Vector3 position;
    float size;
    
    alignas(16) math::Vector3 velocity;
    float mass;
    
    // Appearance
    alignas(16) math::Vector3 color;
    float alpha;
    
    alignas(16) math::Vector3 acceleration;
    float lifetime;
    
    // Physics properties
    float damping;
    float restitution;
    uint32_t flags;
    uint32_t padding;
};

// Particle emitter configuration
struct ParticleEmitter {
    enum class Type {
        POINT,
        SPHERE,
        BOX,
        CYLINDER,
        CONE,
        MESH
    };
    
    enum class Shape {
        SPHERE,
        CUBE,
        DISC,
        RING,
        LINE
    };
    
    Type type = Type::POINT;
    Shape shape = Shape::SPHERE;
    
    // Emission properties
    math::Vector3 position{0.0f};
    math::Vector3 direction{0.0f, 1.0f, 0.0f};
    math::Vector3 size{1.0f};
    
    // Emission rates
    float emit_rate = 100.0f;  // particles per second
    float burst_count = 0.0f;  // particles per burst
    float burst_frequency = 1.0f;  // bursts per second
    
    // Particle properties
    float lifetime_min = 1.0f;
    float lifetime_max = 3.0f;
    float size_min = 0.1f;
    float size_max = 0.5f;
    float speed_min = 1.0f;
    float speed_max = 5.0f;
    
    // Color variation
    math::Vector3 color_start{1.0f, 1.0f, 1.0f};
    math::Vector3 color_end{1.0f, 1.0f, 1.0f};
    float alpha_start = 1.0f;
    float alpha_end = 0.0f;
    
    // Physics
    float gravity = -9.81f;
    float damping = 0.99f;
    float turbulence = 0.0f;
    
    // Flags
    bool enabled = true;
    bool loop = true;
    bool collide_with_world = false;
    bool fade_out = true;
    bool scale_over_lifetime = false;
    
    // Texture and material
    uint32_t texture_id = 0;
    uint32_t material_id = 0;
    bool billboard = true;
    bool soft_particles = false;
    
    // Simulation
    float time_accumulator = 0.0f;
    uint32_t particles_emitted = 0;
    std::atomic<uint32_t> active_particles{0};
};

// Particle forces
struct ParticleForce {
    enum class Type {
        GRAVITY,
        WIND,
        TURBULENCE,
        VORTEX,
        MAGNETIC,
        DRAG,
        POINT_ATTRACTION,
        PLANE_REPULSION
    };
    
    Type type;
    math::Vector3 position{0.0f};
    math::Vector3 direction{0.0f, 1.0f, 0.0f};
    float strength = 1.0f;
    float range = 10.0f;
    bool enabled = true;
};

// Particle collision with world
struct ParticleCollision {
    math::Vector3 normal{0.0f, 1.0f, 0.0f};
    float distance = 0.0f;
    float restitution = 0.5f;
    float friction = 0.3f;
};

// Particle system configuration
struct ParticleSystemConfig {
    uint32_t max_particles = 1000000;
    uint32_t max_emitters = 1000;
    uint32_t max_forces = 100;
    
    bool gpu_simulation = true;
    bool gpu_rendering = true;
    bool enable_collisions = false;
    bool enable_sorting = true;
    
    float update_frequency = 60.0f;
    float culling_distance = 100.0f;
    float lod_distance = 50.0f;
    
    // Performance
    uint32_t simulation_threads = 4;
    uint32_t render_threads = 2;
    bool use_compute_shaders = true;
    bool async_update = true;
};

// Particle performance statistics
struct ParticleStats {
    std::atomic<uint32_t> total_particles{0};
    std::atomic<uint32_t> active_particles{0};
    std::atomic<uint32_t> emitters_active{0};
    std::atomic<uint32_t> forces_active{0};
    std::atomic<float> simulation_time_ms{0.0f};
    std::atomic<float> render_time_ms{0.0f};
    std::atomic<uint32_t> gpu_memory_usage_mb{0};
};

// Main particle system class
class ParticleSystem {
private:
    ParticleSystemConfig config_;
    bool initialized_;
    
    // Particle storage
    std::vector<Particle> particles_;
    std::vector<uint32_t> free_particles_;
    std::vector<uint32_t> active_particles_;
    
    // Emitters and forces
    std::vector<ParticleEmitter> emitters_;
    std::vector<ParticleForce> forces_;
    
    // GPU resources
    uint32_t particle_buffer_;
    uint32_t particle_vao_;
    uint32_t particle_shader_;
    uint32_t compute_shader_;
    
    // Collision
    std::vector<ParticleCollision> collisions_;
    
    // Performance
    ParticleStats stats_;
    std::chrono::high_resolution_clock::time_point last_update_;
    
    // Thread safety
    mutable std::mutex particle_mutex_;
    
    // Random number generator
    math::FastRandom rng_;
    
public:
    explicit ParticleSystem(const ParticleSystemConfig& config = ParticleSystemConfig{});
    ~ParticleSystem();
    
    bool initialize();
    void shutdown();
    
    // Update and render
    void update(float dt);
    void render();
    
    // Emitter management
    uint32_t create_emitter(const ParticleEmitter& emitter);
    void update_emitter(uint32_t emitter_id, const ParticleEmitter& emitter);
    void remove_emitter(uint32_t emitter_id);
    void enable_emitter(uint32_t emitter_id, bool enabled);
    
    // Force management
    uint32_t add_force(const ParticleForce& force);
    void update_force(uint32_t force_id, const ParticleForce& force);
    void remove_force(uint32_t force_id);
    
    // Particle manipulation
    uint32_t emit_particle(const Particle& particle);
    void emit_burst(uint32_t emitter_id, uint32_t count);
    void clear_all_particles();
    
    // Collision
    void add_collision_surface(const ParticleCollision& collision);
    void remove_collision_surface(uint32_t collision_id);
    void enable_collisions(bool enable);
    
    // Performance
    const ParticleStats& get_stats() const;
    void set_config(const ParticleSystemConfig& config);
    
    // Presets
    void create_fire_effect(uint32_t emitter_id, const math::Vector3& position);
    void create_smoke_effect(uint32_t emitter_id, const math::Vector3& position);
    void create_explosion_effect(uint32_t emitter_id, const math::Vector3& position);
    void create_magic_effect(uint32_t emitter_id, const math::Vector3& position, 
                           const math::Vector3& color);
    void create_rain_effect(uint32_t emitter_id, const math::Vector3& area);
    void create_snow_effect(uint32_t emitter_id, const math::Vector3& area);
    
    // Debug utilities
    void set_debug_mode(bool enabled);
    void save_particle_positions(const char* filename);
    
private:
    // Particle management
    uint32_t allocate_particle();
    void deallocate_particle(uint32_t particle_id);
    void update_particle_physics(Particle& particle, float dt);
    void apply_forces(Particle& particle, float dt);
    bool check_collision(const Particle& particle, math::Vector3& collision_normal);
    
    // Emitter updates
    void update_emitters(float dt);
    void emit_from_emitter(ParticleEmitter& emitter, float dt);
    
    // GPU operations
    bool initialize_gpu_resources();
    void update_gpu_buffer();
    void render_gpu_particles();
    
    // CPU fallback
    void update_cpu_particles(float dt);
    void render_cpu_particles();
    
    // Utility functions
    math::Vector3 calculate_emission_position(const ParticleEmitter& emitter);
    math::Vector3 calculate_emission_velocity(const ParticleEmitter& emitter);
    math::Vector3 interpolate_color(const math::Vector3& start, const math::Vector3& end, 
                                   float t);
    float calculate_particle_size(const ParticleEmitter& emitter, float lifetime_ratio);
    float calculate_particle_alpha(const ParticleEmitter& emitter, float lifetime_ratio);
    
    // Performance optimization
    void cull_distant_particles();
    void sort_particles_by_depth();
    void update_lod();
    
    // Statistics
    void update_stats();
    void reset_stats();
};

} // namespace privanna::render

#endif // PARTICLE_SYSTEM_HPP