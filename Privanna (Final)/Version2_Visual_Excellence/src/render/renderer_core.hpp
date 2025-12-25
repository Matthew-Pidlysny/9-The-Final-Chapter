/*
 * Renderer Core - Advanced Visual Pipeline
 * HDR rendering, deferred shading, post-processing
 */

#ifndef RENDERER_CORE_HPP
#define RENDERER_CORE_HPP

#include <memory>
#include <vector>
#include <cstdint>
#include <atomic>
#include <mutex>

namespace privanna::render {

// Render pipeline stages
enum class RenderStage {
    GEOMETRY_PASS,
    LIGHTING_PASS,
    POST_PROCESS_PASS,
    UI_PASS,
    PRESENT_PASS
};

// Graphics API abstraction
enum class GraphicsAPI {
    OPENGL,
    VULKAN,
    DIRECTX12,
    METAL
};

// Render quality settings
enum class RenderQuality {
    LOW,
    MEDIUM,
    HIGH,
    ULTRA,
    CUSTOM
};

// Framebuffer configuration
struct FramebufferConfig {
    uint32_t width = 1920;
    uint32_t height = 1080;
    uint32_t color_attachments = 4;  // Albedo, Normal, Roughness, Motion
    bool has_depth = true;
    bool has_stencil = false;
    bool hdr_enabled = true;
    uint32_t msaa_samples = 4;
};

// Lighting configuration
struct LightingConfig {
    bool enable_deferred_shading = true;
    bool enable_global_illumination = true;
    bool enable_volumetric_lighting = true;
    uint32_t max_lights = 1024;
    uint32_t shadow_map_size = 2048;
    float shadow_distance = 100.0f;
    bool enable_cascaded_shadows = true;
    uint32_t cascade_count = 4;
};

// Post-processing configuration
struct PostProcessConfig {
    bool enable_bloom = true;
    bool enable_tone_mapping = true;
    bool enable_anti_aliasing = true;
    bool enable_motion_blur = true;
    bool enable_depth_of_field = true;
    bool enable_screen_space_reflections = true;
    bool enable_ambient_occlusion = true;
    float bloom_threshold = 1.0f;
    float bloom_intensity = 0.5f;
};

// Render statistics
struct RenderStats {
    std::atomic<uint64_t> frame_count{0};
    std::atomic<uint32_t> draw_calls{0};
    std::atomic<uint32_t> triangles_rendered{0};
    std::atomic<uint32_t> vertices_processed{0};
    std::atomic<float> gpu_time_ms{0.0f};
    std::atomic<float> cpu_time_ms{0.0f};
    std::atomic<float> frame_time_ms{0.0f};
    std::atomic<float> fps{0.0f};
};

// Camera representation
struct Camera {
    alignas(16) float position[4] = {0.0f, 0.0f, 5.0f, 1.0f};
    alignas(16) float direction[4] = {0.0f, 0.0f, -1.0f, 0.0f};
    alignas(16) float up[4] = {0.0f, 1.0f, 0.0f, 0.0f};
    alignas(16) float view_matrix[16];
    alignas(16) float projection_matrix[16];
    alignas(16) float view_projection_matrix[16];
    
    float fov = 45.0f;
    float near_plane = 0.1f;
    float far_plane = 1000.0f;
    float aspect_ratio = 16.0f / 9.0f;
};

// Light representation
struct Light {
    enum class Type {
        DIRECTIONAL,
        POINT,
        SPOT
    };
    
    Type type;
    alignas(16) float position[4];
    alignas(16) float direction[4];
    alignas(16) float color[4];
    float intensity;
    float range;
    float spot_angle;
    bool enabled;
    bool casts_shadows;
    uint32_t shadow_map_id;
};

// Material representation
struct Material {
    alignas(16) float albedo[4] = {1.0f, 1.0f, 1.0f, 1.0f};
    alignas(16) float normal[4] = {0.5f, 0.5f, 1.0f, 0.0f};
    alignas(16) float roughness_metallic[4] = {0.5f, 0.0f, 0.0f, 0.0f};
    alignas(16) float emissive[4] = {0.0f, 0.0f, 0.0f, 0.0f};
    
    uint32_t albedo_texture;
    uint32_t normal_texture;
    uint32_t roughness_texture;
    uint32_t metallic_texture;
    uint32_t emissive_texture;
    
    bool is_transparent = false;
    bool is_double_sided = false;
    float alpha_cutoff = 0.5f;
};

// Main renderer class
class Renderer {
private:
    GraphicsAPI api_;
    RenderQuality quality_;
    bool initialized_;
    
    // Framebuffers
    uint32_t gbuffer_fbo_;
    uint32_t lighting_fbo_;
    uint32_t post_process_fbo_;
    uint32_t ui_fbo_;
    
    // Render targets
    std::vector<uint32_t> color_textures_;
    uint32_t depth_texture_;
    uint32_t stencil_texture_;
    
    // Shaders
    uint32_t geometry_shader_;
    uint32_t lighting_shader_;
    uint32_t post_process_shader_;
    uint32_t ui_shader_;
    
    // Lighting
    std::vector<Light> lights_;
    std::vector<uint32_t> shadow_maps_;
    
    // Camera
    Camera camera_;
    
    // Performance tracking
    RenderStats stats_;
    std::chrono::high_resolution_clock::time_point last_frame_time_;
    
    // Thread safety
    mutable std::mutex render_mutex_;
    
public:
    Renderer();
    ~Renderer();
    
    bool initialize(GraphicsAPI api = GraphicsAPI::OPENGL);
    void shutdown();
    
    // Configuration
    void set_render_quality(RenderQuality quality);
    void set_framebuffer_config(const FramebufferConfig& config);
    void set_lighting_config(const LightingConfig& config);
    void set_post_process_config(const PostProcessConfig& config);
    
    // Rendering
    void begin_frame();
    void end_frame();
    void render_frame();
    
    // Camera control
    void set_camera(const Camera& camera);
    const Camera& get_camera() const;
    
    // Lighting
    uint32_t add_light(const Light& light);
    void remove_light(uint32_t light_id);
    void update_light(uint32_t light_id, const Light& light);
    const std::vector<Light>& get_lights() const;
    
    // Materials
    uint32_t create_material(const Material& material);
    void update_material(uint32_t material_id, const Material& material);
    
    // Performance
    const RenderStats& get_stats() const;
    void reset_stats();
    
    // Advanced features
    void enable_hdr(bool enable);
    void enable_msaa(uint32_t samples);
    void enable_ray_tracing(bool enable);
    void enable_global_illumination(bool enable);
    
    // Debug utilities
    void save_screenshot(const char* filename);
    void toggle_wireframe();
    void toggle_debug_view();
    
private:
    bool initialize_framebuffers();
    bool initialize_shaders();
    bool initialize_lighting();
    
    void geometry_pass();
    void lighting_pass();
    void post_process_pass();
    void ui_pass();
    
    void update_stats();
    void calculate_fps();
    
    uint32_t compile_shader(const char* vertex_source, const char* fragment_source);
    uint32_t create_texture(uint32_t width, uint32_t height, uint32_t format, bool hdr = false);
    
    void set_render_state();
    void bind_framebuffer(uint32_t fbo);
    void clear_framebuffer();
    
    void draw_quad();
    void draw_fullscreen_quad();
};

} // namespace privanna::render

#endif // RENDERER_CORE_HPP