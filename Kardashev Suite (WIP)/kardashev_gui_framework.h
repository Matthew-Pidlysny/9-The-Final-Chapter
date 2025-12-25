/*
 * Kardashev Suite - GUI Framework
 * Round 1: Foundation Implementation
 * 
 * Cross-platform GUI framework for Kardashev Suite applications
 * Built with modern C++ and designed for industrial-grade scalability
 */

#ifndef KARDASHEV_GUI_FRAMEWORK_H
#define KARDASHEV_GUI_FRAMEWORK_H

#include <string>
#include <vector>
#include <memory>
#include <functional>
#include <map>
#include <atomic>
#include <thread>
#include <mutex>

// Forward declarations for GUI libraries
#ifdef _WIN32
#include <windows.h>
#endif

#ifdef __APPLE__
#include <Cocoa/Cocoa.h>
#endif

#if defined(__linux__) || defined(__unix__)
#include <X11/Xlib.h>
#include <gtk/gtk.h>
#endif

namespace KardashevSuite {
namespace GUI {

/**
 * GUI Event Types
 */
enum class EventType {
    MOUSE_CLICK,
    MOUSE_MOVE,
    KEY_PRESS,
    KEY_RELEASE,
    WINDOW_RESIZE,
    WINDOW_CLOSE,
    CUSTOM_EVENT
};

/**
 * Input Event Structure
 */
struct InputEvent {
    EventType type;
    int x, y;
    int button;
    int key_code;
    std::string key_char;
    uint64_t timestamp;
    void* native_event;
    
    InputEvent() : type(EventType::CUSTOM_EVENT), x(0), y(0), button(0), 
                   key_code(0), timestamp(0), native_event(nullptr) {}
};

/**
 * Color Structure
 */
struct Color {
    float r, g, b, a;
    
    Color(float red = 0.0f, float green = 0.0f, float blue = 0.0f, float alpha = 1.0f)
        : r(red), g(green), b(blue), a(alpha) {}
    
    uint32_t to_rgba() const;
    uint32_t to_argb() const;
    static Color from_rgba(uint32_t rgba);
    static Color from_argb(uint32_t argb);
};

/**
 * Rectangle Structure
 */
struct Rect {
    int x, y;
    int width, height;
    
    Rect(int x_pos = 0, int y_pos = 0, int w = 0, int h = 0)
        : x(x_pos), y(y_pos), width(w), height(h) {}
    
    bool contains_point(int px, int py) const;
    bool intersects(const Rect& other) const;
};

/**
 * Widget Base Class
 */
class Widget {
public:
    virtual ~Widget() = default;
    
    // Core widget methods
    virtual void render() = 0;
    virtual bool handle_event(const InputEvent& event) = 0;
    virtual void update_bounds(const Rect& bounds) = 0;
    virtual Rect get_bounds() const = 0;
    
    // Hierarchy management
    virtual void add_child(std::shared_ptr<Widget> child) = 0;
    virtual void remove_child(std::shared_ptr<Widget> child) = 0;
    virtual std::vector<std::shared_ptr<Widget>> get_children() const = 0;
    virtual std::shared_ptr<Widget> get_parent() const = 0;
    
    // Properties
    virtual void set_visible(bool visible) = 0;
    virtual bool is_visible() const = 0;
    virtual void set_enabled(bool enabled) = 0;
    virtual bool is_enabled() const = 0;
    virtual void set_focusable(bool focusable) = 0;
    virtual bool is_focusable() const = 0;
    
    // Layout
    virtual void set_position(int x, int y) = 0;
    virtual void set_size(int width, int height) = 0;
    virtual void set_margins(int left, int top, int right, int bottom) = 0;
    virtual void set_padding(int left, int top, int right, int bottom) = 0;
    
    // Events
    virtual void set_on_click(std::function<void()> callback) = 0;
    virtual void set_on_change(std::function<void(const std::string&)> callback) = 0;
    virtual void set_on_hover(std::function<void(bool)> callback) = 0;
    
protected:
    Rect bounds_;
    bool visible_;
    bool enabled_;
    bool focusable_;
    std::weak_ptr<Widget> parent_;
    std::vector<std::shared_ptr<Widget>> children_;
    std::function<void()> on_click_callback_;
    std::function<void(const std::string&)> on_change_callback_;
    std::function<void(bool)> on_hover_callback_;
};

/**
 * Window Class
 */
class Window {
public:
    virtual ~Window() = default;
    
    // Window management
    virtual bool create(const std::string& title, int width, int height) = 0;
    virtual void destroy() = 0;
    virtual void show() = 0;
    virtual void hide() = 0;
    virtual void close() = 0;
    
    // Properties
    virtual void set_title(const std::string& title) = 0;
    virtual std::string get_title() const = 0;
    virtual void set_size(int width, int height) = 0;
    virtual void get_size(int& width, int& height) const = 0;
    virtual void set_position(int x, int y) = 0;
    virtual void get_position(int& x, int& y) const = 0;
    virtual void set_resizable(bool resizable) = 0;
    virtual bool is_resizable() const = 0;
    
    // Widget management
    virtual void set_root_widget(std::shared_ptr<Widget> widget) = 0;
    virtual std::shared_ptr<Widget> get_root_widget() const = 0;
    
    // Event handling
    virtual void set_on_close(std::function<void()> callback) = 0;
    virtual void set_on_resize(std::function<void(int, int)> callback) = 0;
    virtual void set_on_move(std::function<void(int, int)> callback) = 0;
    
    // Rendering
    virtual void invalidate() = 0;
    virtual void invalidate_rect(const Rect& rect) = 0;
    virtual bool begin_frame() = 0;
    virtual void end_frame() = 0;
    
protected:
    std::string title_;
    int width_, height_;
    int x_, y_;
    bool visible_;
    bool resizable_;
    std::shared_ptr<Widget> root_widget_;
    std::function<void()> on_close_callback_;
    std::function<void(int, int)> on_resize_callback_;
    std::function<void(int, int)> on_move_callback_;
};

/**
 * Application Class
 */
class Application {
public:
    virtual ~Application() = default;
    
    // Application lifecycle
    virtual bool initialize() = 0;
    virtual void run() = 0;
    virtual void quit() = 0;
    virtual void cleanup() = 0;
    
    // Window management
    virtual std::shared_ptr<Window> create_window() = 0;
    virtual void destroy_window(std::shared_ptr<Window> window) = 0;
    virtual std::vector<std::shared_ptr<Window>> get_windows() const = 0;
    
    // Event loop
    virtual void process_events() = 0;
    virtual bool is_running() const = 0;
    
    // Threading
    virtual void run_on_ui_thread(std::function<void()> task) = 0;
    virtual void run_on_background_thread(std::function<void()> task) = 0;
    
protected:
    std::vector<std::shared_ptr<Window>> windows_;
    std::atomic<bool> running_;
    std::mutex windows_mutex_;
    std::unique_ptr<std::thread> ui_thread_;
};

/**
 * Widget Factory
 */
class WidgetFactory {
public:
    // Basic widgets
    static std::shared_ptr<Widget> create_button();
    static std::shared_ptr<Widget> create_label(const std::string& text = "");
    static std::shared_ptr<Widget> create_textbox();
    static std::shared_ptr<Widget> create_checkbox(const std::string& label = "");
    static std::shared_ptr<Widget> create_radio_button(const std::string& label = "");
    static std::shared_ptr<Widget> create_slider();
    static std::shared_ptr<Widget> create_progress_bar();
    
    // Container widgets
    static std::shared_ptr<Widget> create_panel();
    static std::shared_ptr<Widget> create_scroll_panel();
    static std::shared_ptr<Widget> create_split_panel(bool horizontal = true);
    static std::shared_ptr<Widget> create_tab_panel();
    
    // Menu widgets
    static std::shared_ptr<Widget> create_menu_bar();
    static std::shared_ptr<Widget> create_menu();
    static std::shared_ptr<Widget> create_menu_item(const std::string& text = "");
    
    // Advanced widgets
    static std::shared_ptr<Widget> create_tree_view();
    static std::shared_ptr<Widget> create_list_view();
    static std::shared_ptr<Widget> create_table_view();
    static std::shared_ptr<Widget> create_chart();
    static std::shared_ptr<Widget> create_web_view();
};

/**
 * Layout System
 */
class LayoutManager {
public:
    enum class LayoutType {
        ABSOLUTE,
        VERTICAL_BOX,
        HORIZONTAL_BOX,
        GRID,
        FLEX,
        RELATIVE
    };
    
    virtual ~LayoutManager() = default;
    virtual void layout_widgets(std::shared_ptr<Widget> container) = 0;
    virtual void add_widget(std::shared_ptr<Widget> widget, const std::map<std::string, int>& properties) = 0;
    virtual void remove_widget(std::shared_ptr<Widget> widget) = 0;
    virtual void set_spacing(int spacing) = 0;
    virtual void set_margins(int margins) = 0;
    
    static std::unique_ptr<LayoutManager> create_layout_manager(LayoutType type);
};

/**
 * Theme System
 */
class Theme {
public:
    struct ThemeColors {
        Color background;
        Color foreground;
        Color accent;
        Color highlight;
        Color border;
        Color shadow;
        Color text_primary;
        Color text_secondary;
        Color success;
        Color warning;
        Color error;
        Color info;
    };
    
    struct ThemeFonts {
        std::string primary_font;
        std::string secondary_font;
        std::string monospace_font;
        int primary_size;
        int secondary_size;
        int monospace_size;
    };
    
    ThemeColors colors;
    ThemeFonts fonts;
    
    void load_from_file(const std::string& theme_path);
    void save_to_file(const std::string& theme_path) const;
    static Theme create_default_theme();
    static Theme create_dark_theme();
    static Theme create_light_theme();
};

/**
 * Application Factory
 */
class ApplicationFactory {
public:
    static std::unique_ptr<Application> create_application();
    static void set_platform_backend(const std::string& backend_name);
};

} // namespace GUI
} // namespace KardashevSuite

#endif // KARDASHEV_GUI_FRAMEWORK_H