#ifndef PRIVANNA_MODERN_GUI_SYSTEM_HPP
#define PRIVANNA_MODERN_GUI_SYSTEM_HPP

#include <vector>
#include <memory>
#include <string>
#include <unordered_map>
#include <functional>
#include <chrono>
#include <glm/glm.hpp>
#include "src/core/event_system.hpp"

namespace privanna {
namespace gui {

// Forward declarations
class GUIRenderer;
class ThemeManager;
class AnimationSystem;
class LayoutManager;
class InputManager;
class FontRenderer;
class ParticleSystem;

// GUI Element Types
enum class GUIElementType {
    WINDOW,
    PANEL,
    BUTTON,
    LABEL,
    TEXT_FIELD,
    SLIDER,
    PROGRESS_BAR,
    CHECKBOX,
    RADIO_BUTTON,
    DROP_DOWN,
    LIST_BOX,
    TAB_CONTAINER,
    SCROLL_VIEW,
    MINIMAP,
    RESOURCE_DISPLAY,
    UNIT_PANEL,
    DIPLOMACY_PANEL,
    ACTION_BAR,
    CONTEXT_MENU,
    TOOLTIP,
    NOTIFICATION,
    CUSTOM
};

// Layout Types
enum class LayoutType {
    ABSOLUTE,
    VERTICAL_BOX,
    HORIZONTAL_BOX,
    GRID,
    FLEX,
    CONSTRAINT,
    RELATIVE
};

// Animation Types
enum class AnimationType {
    FADE_IN,
    FADE_OUT,
    SLIDE_IN_LEFT,
    SLIDE_IN_RIGHT,
    SLIDE_IN_TOP,
    SLIDE_IN_BOTTOM,
    SCALE_UP,
    SCALE_DOWN,
    ROTATE,
    BOUNCE,
    ELASTIC,
    CUSTOM
};

// Theme Colors
struct ThemeColors {
    glm::vec4 primary;
    glm::vec4 secondary;
    glm::vec4 accent;
    glm::vec4 background;
    glm::vec4 surface;
    glm::vec4 text_primary;
    glm::vec4 text_secondary;
    glm::vec4 border;
    glm::vec4 shadow;
    glm::vec4 highlight;
    glm::vec4 success;
    glm::vec4 warning;
    glm::vec4 error;
    glm::vec4 info;
};

// GUI Element Base Class
class GUIElement {
public:
    GUIElement(GUIElementType type, const std::string& name = "");
    virtual ~GUIElement() = default;
    
    // Core functionality
    virtual void render(GUIRenderer* renderer) = 0;
    virtual void update(double delta_time);
    virtual bool handleInput(const InputEvent& event);
    virtual void calculateLayout();
    
    // Properties
    const std::string& getName() const { return name_; }
    GUIElementType getType() const { return type_; }
    
    void setPosition(const glm::vec2& position) { position_ = position; needs_layout_ = true; }
    const glm::vec2& getPosition() const { return position_; }
    
    void setSize(const glm::vec2& size) { size_ = size; needs_layout_ = true; }
    const glm::vec2& getSize() const { return size_; }
    
    void setVisible(bool visible) { visible_ = visible; }
    bool isVisible() const { return visible_; }
    
    void setEnabled(bool enabled) { enabled_ = enabled; }
    bool isEnabled() const { return enabled_; }
    
    void setAlpha(float alpha) { alpha_ = std::clamp(alpha, 0.0f, 1.0f); }
    float getAlpha() const { return alpha_; }
    
    // Hierarchy
    void addChild(std::shared_ptr<GUIElement> child);
    void removeChild(std::shared_ptr<GUIElement> child);
    const std::vector<std::shared_ptr<GUIElement>>& getChildren() const { return children_; }
    GUIElement* getParent() const { return parent_; }
    
    // Layout
    void setLayoutType(LayoutType type) { layout_type_ = type; needs_layout_ = true; }
    LayoutType getLayoutType() const { return layout_type_; }
    
    // Animation
    void startAnimation(AnimationType type, float duration);
    void stopAnimation();
    bool isAnimating() const { return is_animating_; }
    
    // Events
    void setOnClick(std::function<void()> callback) { on_click_ = callback; }
    void setOnHover(std::function<void(bool)> callback) { on_hover_ = callback; }
    void setOnFocus(std::function<void(bool)> callback) { on_focus_ = callback; }
    void setOnValueChanged(std::function<void(const std::string&)> callback) { on_value_changed_ = callback; }
    
protected:
    std::string name_;
    GUIElementType type_;
    glm::vec2 position_;
    glm::vec2 size_;
    float alpha_;
    bool visible_;
    bool enabled_;
    bool needs_layout_;
    bool is_animating_;
    
    GUIElement* parent_;
    std::vector<std::shared_ptr<GUIElement>> children_;
    LayoutType layout_type_;
    
    // Event callbacks
    std::function<void()> on_click_;
    std::function<void(bool)> on_hover_;
    std::function<void(bool)> on_focus_;
    std::function<void(const std::string&)> on_value_changed_;
    
    // Animation data
    AnimationType current_animation_;
    float animation_time_;
    float animation_duration_;
    
    // Internal helpers
    void triggerHover(bool is_hovering);
    void triggerClick();
    void triggerFocus(bool has_focus);
    void triggerValueChanged(const std::string& value);
};

// Window Class
class Window : public GUIElement {
public:
    Window(const std::string& title = "Window");
    
    void render(GUIRenderer* renderer) override;
    bool handleInput(const InputEvent& event) override;
    
    void setTitle(const std::string& title) { title_ = title; }
    const std::string& getTitle() const { return title_; }
    
    void setResizable(bool resizable) { resizable_ = resizable; }
    bool isResizable() const { return resizable_; }
    
    void setMovable(bool movable) { movable_ = movable; }
    bool isMovable() const { return movable_; }
    
    void setClosable(bool closable) { closable_ = closable; }
    bool isClosable() const { return closable_; }
    
private:
    std::string title_;
    bool resizable_;
    bool movable_;
    bool closable_;
    bool is_dragging_;
    glm::vec2 drag_offset_;
    glm::vec2 resize_start_;
    glm::vec2 original_size_;
};

// Button Class
class Button : public GUIElement {
public:
    Button(const std::string& text = "Button");
    
    void render(GUIRenderer* renderer) override;
    bool handleInput(const InputEvent& event) override;
    
    void setText(const std::string& text) { text_ = text; }
    const std::string& getText() const { return text_; }
    
    void setIcon(const std::string& icon_path) { icon_path_ = icon_path; }
    const std::string& getIconPath() const { return icon_path_; }
    
    enum class ButtonStyle {
        NORMAL,
        PRIMARY,
        SECONDARY,
        SUCCESS,
        WARNING,
        ERROR,
        GHOST,
        OUTLINE
    };
    
    void setStyle(ButtonStyle style) { style_ = style; }
    ButtonStyle getStyle() const { return style_; }
    
private:
    std::string text_;
    std::string icon_path_;
    ButtonStyle style_;
    bool is_hovered_;
    bool is_pressed_;
    glm::vec4 current_color_;
};

// Label Class
class Label : public GUIElement {
public:
    Label(const std::string& text = "Label");
    
    void render(GUIRenderer* renderer) override;
    
    void setText(const std::string& text) { text_ = text; needs_layout_ = true; }
    const std::string& getText() const { return text_; }
    
    enum class TextAlignment {
        LEFT,
        CENTER,
        RIGHT,
        JUSTIFIED
    };
    
    void setAlignment(TextAlignment alignment) { alignment_ = alignment; needs_layout_ = true; }
    TextAlignment getAlignment() const { return alignment_; }
    
    void setFontSize(float size) { font_size_ = size; needs_layout_ = true; }
    float getFontSize() const { return font_size_; }
    
    void setTextColor(const glm::vec4& color) { text_color_ = color; }
    const glm::vec4& getTextColor() const { return text_color_; }
    
    void setWordWrap(bool wrap) { word_wrap_ = wrap; needs_layout_ = true; }
    bool isWordWrapped() const { return word_wrap_; }
    
private:
    std::string text_;
    TextAlignment alignment_;
    float font_size_;
    glm::vec4 text_color_;
    bool word_wrap_;
};

// Resource Display Panel
class ResourceDisplay : public GUIElement {
public:
    ResourceDisplay();
    
    void render(GUIRenderer* renderer) override;
    void update(double delta_time) override;
    
    void addResource(const std::string& name, int current, int max, const glm::vec4& color);
    void updateResource(const std::string& name, int current, int max);
    void removeResource(const std::string& name);
    
    void setShowAnimations(bool show) { show_animations_ = show; }
    void setShowIcons(bool show) { show_icons_ = show; }
    
private:
    struct ResourceInfo {
        std::string name;
        int current;
        int max;
        int previous;
        glm::vec4 color;
        float animation_time;
        bool is_increasing;
    };
    
    std::unordered_map<std::string, ResourceInfo> resources_;
    bool show_animations_;
    bool show_icons_;
};

// Minimap
class Minimap : public GUIElement {
public:
    Minimap();
    
    void render(GUIRenderer* renderer) override;
    bool handleInput(const InputEvent& event) override;
    
    void setWorldSize(const glm::vec2& size) { world_size_ = size; }
    void setViewport(const glm::vec2& center, const glm::vec2& size);
    
    void addUnit(int unit_id, const glm::vec2& position, const glm::vec4& color, bool is_friendly);
    void removeUnit(int unit_id);
    void updateUnit(int unit_id, const glm::vec2& position);
    
    void setTerritoryData(const std::vector<glm::vec4>& territory_colors);
    void setShowGrid(bool show) { show_grid_ = show; }
    void setShowUnits(bool show) { show_units_ = show; }
    void setShowTerritories(bool show) { show_territories_ = show; }
    
private:
    struct MinimapUnit {
        int id;
        glm::vec2 position;
        glm::vec4 color;
        bool is_friendly;
    };
    
    glm::vec2 world_size_;
    glm::vec2 viewport_center_;
    glm::vec2 viewport_size_;
    std::vector<MinimapUnit> units_;
    std::vector<glm::vec4> territory_colors_;
    
    bool show_grid_;
    bool show_units_;
    bool show_territories_;
    bool is_dragging_;
    glm::vec2 drag_start_;
};

// Action Bar
class ActionBar : public GUIElement {
public:
    ActionBar();
    
    void render(GUIRenderer* renderer) override;
    bool handleInput(const InputEvent& event) override;
    
    struct ActionSlot {
        int id;
        std::string name;
        std::string icon_path;
        std::string description;
        bool is_available;
        float cooldown;
        float current_cooldown;
        int hotkey;
    };
    
    void addAction(const ActionSlot& action);
    void removeAction(int id);
    void updateAction(int id, const ActionSlot& action);
    
    void setSlotCount(int count);
    void setShowHotkeys(bool show) { show_hotkeys_ = show; }
    void setShowCooldowns(bool show) { show_cooldowns_ = show; }
    
    const ActionSlot* getSelectedAction() const { return selected_action_; }
    
private:
    std::vector<ActionSlot> actions_;
    int slot_count_;
    bool show_hotkeys_;
    bool show_cooldowns_;
    ActionSlot* selected_action_;
    glm::vec2 hover_position_;
};

// Notification System
class NotificationSystem : public GUIElement {
public:
    NotificationSystem();
    
    void render(GUIRenderer* renderer) override;
    void update(double delta_time) override;
    
    enum class NotificationType {
        INFO,
        SUCCESS,
        WARNING,
        ERROR,
        ACHIEVEMENT,
        QUEST,
        DIPLOMATIC,
        COMBAT
    };
    
    struct Notification {
        int id;
        std::string title;
        std::string message;
        NotificationType type;
        float duration;
        float elapsed_time;
        glm::vec4 color;
        bool is_persistent;
    };
    
    void addNotification(const Notification& notification);
    void removeNotification(int id);
    void clearNotifications();
    
    void setMaxVisibleNotifications(int max) { max_visible_ = max; }
    void setAnimationDuration(float duration) { animation_duration_ = duration; }
    
private:
    std::vector<Notification> notifications_;
    int next_notification_id_;
    int max_visible_;
    float animation_duration_;
    
    glm::vec4 getTypeColor(NotificationType type);
};

// Main GUI System
class ModernGUISystem {
public:
    ModernGUISystem();
    ~ModernGUISystem();
    
    bool initialize();
    void shutdown();
    
    void update(double delta_time);
    void render();
    
    // Element management
    std::shared_ptr<GUIElement> createElement(GUIElementType type, const std::string& name = "");
    void addElement(std::shared_ptr<GUIElement> element);
    void removeElement(std::shared_ptr<GUIElement> element);
    
    // Root elements
    void addRootWindow(std::shared_ptr<Window> window);
    void removeRootWindow(std::shared_ptr<Window> window);
    
    // Theme management
    void loadTheme(const std::string& theme_name);
    void saveTheme(const std::string& theme_name);
    void setThemeColors(const ThemeColors& colors);
    const ThemeColors& getCurrentTheme() const { return current_theme_; }
    
    // Input handling
    bool handleInput(const InputEvent& event);
    
    // Layout management
    void recalculateLayouts();
    void setScreenSize(int width, int height);
    
    // Performance monitoring
    void enablePerformanceOverlay(bool enable);
    float getGpuTime() const { return gpu_time_; }
    float getCpuTime() const { return cpu_time_; }
    int getElementCount() const { return element_count_; }
    
    // Debug features
    void enableDebugMode(bool enable);
    void showLayoutBounds(bool show);
    void showZOrder(bool show);
    
    // Resource display
    void updateGameResources(const std::unordered_map<std::string, std::pair<int, int>>& resources);
    void updateMinimapData(const glm::vec2& viewport, const std::vector<glm::vec2>& units);
    
    // Notifications
    void showNotification(const std::string& title, const std::string& message, 
                         NotificationSystem::NotificationType type = NotificationSystem::NotificationType::INFO);
    
private:
    std::unique_ptr<GUIRenderer> renderer_;
    std::unique_ptr<ThemeManager> theme_manager_;
    std::unique_ptr<AnimationSystem> animation_system_;
    std::unique_ptr<LayoutManager> layout_manager_;
    std::unique_ptr<InputManager> input_manager_;
    std::unique_ptr<FontRenderer> font_renderer_;
    std::unique_ptr<ParticleSystem> particle_system_;
    
    std::vector<std::shared_ptr<GUIElement>> elements_;
    std::vector<std::shared_ptr<Window>> root_windows_;
    
    ThemeColors current_theme_;
    glm::vec2 screen_size_;
    
    // Performance metrics
    float gpu_time_;
    float cpu_time_;
    int element_count_;
    bool performance_overlay_enabled_;
    
    // Debug state
    bool debug_mode_enabled_;
    bool show_layout_bounds_;
    bool show_z_order_;
    
    // Built-in UI elements
    std::shared_ptr<ResourceDisplay> resource_display_;
    std::shared_ptr<Minimap> minimap_;
    std::shared_ptr<ActionBar> action_bar_;
    std::shared_ptr<NotificationSystem> notification_system_;
    
    // Internal methods
    void initializeDefaultTheme();
    void createDefaultUI();
    void renderPerformanceOverlay();
    void renderDebugOverlay();
    void updatePerformanceMetrics(double delta_time);
};

} // namespace gui
} // namespace privanna

#endif // PRIVANNA_MODERN_GUI_SYSTEM_HPP