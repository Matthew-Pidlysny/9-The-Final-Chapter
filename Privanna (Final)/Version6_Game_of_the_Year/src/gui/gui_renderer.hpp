#ifndef PRIVANNA_GUI_RENDERER_HPP
#define PRIVANNA_GUI_RENDERER_HPP

#include <memory>
#include <vector>
#include <string>
#include <unordered_map>
#include <glm/glm.hpp>
#include <glm/gtc/matrix_transform.hpp>
#include "src/gui/modern_gui_system.hpp"
#include "src/render/renderer_core.hpp"

namespace privanna {
namespace gui {

// Vertex structure for GUI rendering
struct GUIVertex {
    glm::vec2 position;
    glm::vec2 tex_coord;
    glm::vec4 color;
    float texture_id;
    float effect_type;
    
    static std::vector<GUIVertex> createQuad(const glm::vec2& pos, const glm::vec2& size, 
                                           const glm::vec4& color, const glm::vec2& uv = glm::vec2(0, 0));
    static std::vector<GUIVertex> createRoundedRect(const glm::vec2& pos, const glm::vec2& size, 
                                                   float radius, const glm::vec4& color, int segments = 8);
    static std::vector<GUIVertex> createCircle(const glm::vec2& center, float radius, 
                                             const glm::vec4& color, int segments = 32);
};

// Render batch for efficient drawing
struct RenderBatch {
    std::vector<GUIVertex> vertices;
    std::vector<unsigned int> indices;
    unsigned int texture_id;
    std::string shader_name;
    bool is_transparent;
    int z_order;
    
    void clear();
    void addQuad(const glm::vec2& pos, const glm::vec2& size, const glm::vec4& color, 
                const glm::vec2& uv = glm::vec2(0, 0));
    void addTexturedQuad(const glm::vec2& pos, const glm::vec2& size, unsigned int texture_id,
                        const glm::vec4& color = glm::vec4(1.0f));
};

// Post-processing effects
enum class PostProcessEffect {
    NONE,
    BLUR,
    GLOW,
    SHADOW,
    OUTLINE,
    BLOOM,
    COLOR_CORRECTION,
    VIGNETTE,
    CHROMATIC_ABERRATION,
    MOTION_BLUR
};

// GUI Renderer Class
class GUIRenderer {
public:
    GUIRenderer(RendererCore* renderer_core);
    ~GUIRenderer();
    
    bool initialize();
    void shutdown();
    
    // Rendering control
    void beginFrame();
    void endFrame();
    void flush();
    
    // Basic drawing
    void drawQuad(const glm::vec2& position, const glm::vec2& size, const glm::vec4& color);
    void drawTexturedQuad(const glm::vec2& position, const glm::vec2& size, unsigned int texture_id,
                         const glm::vec4& color = glm::vec4(1.0f));
    void drawRoundedRect(const glm::vec2& position, const glm::vec2& size, float radius, 
                        const glm::vec4& color);
    void drawCircle(const glm::vec2& center, float radius, const glm::vec4& color);
    void drawLine(const glm::vec2& start, const glm::vec2& end, float thickness, const glm::vec4& color);
    void drawTriangle(const glm::vec2& p1, const glm::vec2& p2, const glm::vec2& p3, const glm::vec4& color);
    
    // Text rendering
    void drawText(const std::string& text, const glm::vec2& position, float size, 
                  const glm::vec4& color, TextAlignment alignment = TextAlignment::LEFT);
    
    // Advanced effects
    void drawShadowedQuad(const glm::vec2& position, const glm::vec2& size, const glm::vec4& color,
                         float shadow_offset = 2.0f, float shadow_blur = 4.0f);
    void drawGlowingQuad(const glm::vec2& position, const glm::vec2& size, const glm::vec4& color,
                        float glow_intensity = 1.0f);
    void drawOutlinedQuad(const glm::vec2& position, const glm::vec2& size, const glm::vec4& color,
                         const glm::vec4& outline_color, float outline_width = 1.0f);
    
    // Animation and transitions
    void drawFadingQuad(const glm::vec2& position, const glm::vec2& size, const glm::vec4& color, 
                       float alpha);
    void drawScalingQuad(const glm::vec2& position, const glm::vec2& size, const glm::vec4& color, 
                        float scale);
    void drawRotatingQuad(const glm::vec2& position, const glm::vec2& size, const glm::vec4& color, 
                         float angle);
    
    // Clipping and masking
    void setClipRect(const glm::vec4& clip_rect); // x, y, width, height
    void resetClipRect();
    void pushClipRect(const glm::vec4& clip_rect);
    void popClipRect();
    
    // Transformation
    void pushTransform(const glm::mat4& transform);
    void popTransform();
    void setTransform(const glm::mat4& transform);
    const glm::mat4& getTransform() const { return current_transform_; }
    
    // Shaders and effects
    void setShader(const std::string& shader_name);
    void setPostProcessEffect(PostProcessEffect effect);
    void setUniform(const std::string& name, const glm::vec4& value);
    void setUniform(const std::string& name, float value);
    void setUniform(const std::string& name, int value);
    
    // Texture management
    unsigned int loadTexture(const std::string& file_path);
    unsigned int createTexture(int width, int height, void* data);
    void updateTexture(unsigned int texture_id, int width, int height, void* data);
    void bindTexture(unsigned int texture_id, int slot = 0);
    void unbindTexture(int slot = 0);
    
    // Performance
    void enableBatching(bool enable);
    void setMaxBatchSize(int size);
    void flushBatches();
    
    // Metrics
    float getGpuTime() const { return gpu_time_; }
    int getDrawCalls() const { return draw_calls_; }
    int getTrianglesDrawn() const { return triangles_drawn_; }
    void resetMetrics();
    
private:
    RendererCore* renderer_core_;
    
    // Rendering state
    glm::mat4 current_transform_;
    glm::mat4 projection_matrix_;
    std::vector<glm::mat4> transform_stack_;
    std::vector<glm::vec4> clip_rect_stack_;
    glm::vec4 current_clip_rect_;
    
    // Batching
    bool batching_enabled_;
    int max_batch_size_;
    std::vector<RenderBatch> render_batches_;
    RenderBatch* current_batch_;
    
    // Shaders
    std::unordered_map<std::string, unsigned int> shaders_;
    std::string current_shader_;
    
    // Textures
    std::unordered_map<std::string, unsigned int> texture_cache_;
    unsigned int white_texture_;
    unsigned int font_texture_;
    
    // Buffers
    unsigned int vao_;
    unsigned int vbo_;
    unsigned int ebo_;
    std::vector<GUIVertex> vertex_buffer_;
    std::vector<unsigned int> index_buffer_;
    
    // Post-processing
    unsigned int framebuffer_;
    unsigned int color_buffer_;
    unsigned int depth_buffer_;
    PostProcessEffect current_post_effect_;
    
    // Font rendering
    struct Character {
        unsigned int texture_id;
        glm::ivec2 size;
        glm::ivec2 bearing;
        unsigned int advance;
    };
    std::unordered_map<char, Character> characters_;
    float font_scale_;
    
    // Performance metrics
    float gpu_time_;
    int draw_calls_;
    int triangles_drawn_;
    
    // Internal methods
    bool initializeShaders();
    bool initializeBuffers();
    bool initializeTextures();
    bool initializeFonts();
    bool initializePostProcessing();
    
    void createDefaultShaders();
    void createWhiteTexture();
    
    void ensureBatchCapacity(int vertices);
    void submitBatch();
    void renderBatch(const RenderBatch& batch);
    
    void setupShader(const std::string& shader_name);
    void applyPostProcessing();
    
    // Shader creation helpers
    unsigned int createShader(const std::string& vertex_source, const std::string& fragment_source);
    unsigned int createBasicShader();
    unsigned int createTexturedShader();
    unsigned int createRoundedRectShader();
    unsigned int createGlowShader();
    unsigned int createShadowShader();
    unsigned int createPostProcessShader();
    
    // Text rendering helpers
    bool loadFont(const std::string& font_path, int font_size);
    void renderTextCharacter(char c, const glm::vec2& position, float scale, const glm::vec4& color);
    float calculateTextWidth(const std::string& text, float size);
    
    // Clipping helpers
    bool isPointClipped(const glm::vec2& point) const;
    glm::vec4 applyClipTransform(const glm::vec4& rect) const;
    
    // Utility methods
    glm::mat4 createOrthoMatrix(float left, float right, float bottom, float top);
    glm::vec4 hexToRgba(const std::string& hex);
};

// Advanced GUI Effects Manager
class GUIEffectManager {
public:
    GUIEffectManager(GUIRenderer* renderer);
    ~GUIEffectManager();
    
    bool initialize();
    
    // Particle effects
    void emitParticles(const glm::vec2& position, const glm::vec4& color, int count);
    void updateParticles(float delta_time);
    void renderParticles();
    
    // Transition effects
    void startTransition(PostProcessEffect effect, float duration);
    void updateTransition(float delta_time);
    bool isTransitionActive() const { return transition_active_; }
    
    // Screen effects
    void setScreenShake(float intensity, float duration);
    void setScreenFlash(const glm::vec4& color, float duration);
    void setFade(float alpha, float duration);
    
    // Atmospheric effects
    void enableVignette(bool enable, float strength = 0.5f);
    void enableChromaticAberration(bool enable, float strength = 0.5f);
    void enableBloom(bool enable, float threshold = 1.0f, float intensity = 0.5f);
    
private:
    GUIRenderer* renderer_;
    
    // Particles
    struct Particle {
        glm::vec2 position;
        glm::vec2 velocity;
        glm::vec4 color;
        float life;
        float max_life;
        float size;
    };
    
    std::vector<Particle> particles_;
    unsigned int particle_shader_;
    unsigned int particle_vao_;
    unsigned int particle_vbo_;
    
    // Transitions
    bool transition_active_;
    PostProcessEffect current_transition_;
    float transition_time_;
    float transition_duration_;
    
    // Screen effects
    float screen_shake_intensity_;
    float screen_shake_time_;
    float screen_shake_duration_;
    glm::vec4 screen_flash_color_;
    float screen_flash_time_;
    float screen_flash_duration_;
    float fade_alpha_;
    float fade_target_;
    float fade_duration_;
    
    // Atmospheric effects
    bool vignette_enabled_;
    float vignette_strength_;
    bool chromatic_enabled_;
    float chromatic_strength_;
    bool bloom_enabled_;
    float bloom_threshold_;
    float bloom_intensity_;
    
    // Internal methods
    void initializeParticles();
    void updateScreenEffects(float delta_time);
    void renderScreenEffects();
};

// Performance Monitor for GUI
class GUIPerformanceMonitor {
public:
    GUIPerformanceMonitor();
    
    void beginFrame();
    void endFrame();
    
    void addDrawCall() { draw_calls_++; }
    void addTriangles(int count) { triangles_drawn_ += count; }
    void recordGpuTime(float time) { gpu_time_ += time; }
    
    // Metrics
    float getAverageFps() const { return average_fps_; }
    float getCurrentFps() const { return current_fps_; }
    float getGpuTime() const { return gpu_time_; }
    int getDrawCalls() const { return draw_calls_; }
    int getTrianglesDrawn() const { return triangles_drawn_; }
    
    // Frame analysis
    float getFrameTime() const { return frame_time_; }
    float getMinFrameTime() const { return min_frame_time_; }
    float getMaxFrameTime() const { return max_frame_time_; }
    
    void reset();
    void enable(bool enable) { enabled_ = enable; }
    
private:
    bool enabled_;
    std::chrono::high_resolution_clock::time_point frame_start_time_;
    std::chrono::high_resolution_clock::time_point last_frame_time_;
    
    // Current frame metrics
    float frame_time_;
    float current_fps_;
    
    // Averaged metrics
    float average_fps_;
    float gpu_time_;
    int draw_calls_;
    int triangles_drawn_;
    
    // Frame time analysis
    float min_frame_time_;
    float max_frame_time_;
    std::vector<float> frame_history_;
    static constexpr size_t FRAME_HISTORY_SIZE = 60;
    
    void updateMetrics();
};

} // namespace gui
} // namespace privanna

#endif // PRIVANNA_GUI_RENDERER_HPP