/*
 * PlanePilotApp.h - Main Application Class
 * 
 * Central application controller for the Plane Pilot educational software.
 * Manages GUI, workshops, and overall application state.
 */

#ifndef PLANE_PILOT_APP_H
#define PLANE_PILOT_APP_H

#include <memory>
#include <string>
#include <vector>

// Forward declarations
class GLFWwindow;
class SplashScreen;
class MainWindow;
class WorkshopSelector;

namespace PlanePilot {
    namespace Graphics {
        class Renderer;
    }
    namespace Workshops {
        class HadwigerNelsonWorkshop;
        class ChromaticOlympics;
        class GeometrySequencing;
        class SphereOMatic;
    }
    namespace GUI {
        class FontManager;
        class ThemeManager;
    }
}

/**
 * @brief Main application class for Plane Pilot
 * 
 * This class manages the entire application lifecycle including:
 * - Window and OpenGL initialization
 * - GUI management
 * - Workshop coordination
 * - Resource management
 * - Application state
 */
class PlanePilotApp {
public:
    /**
     * @brief Constructor
     */
    PlanePilotApp();
    
    /**
     * @brief Destructor
     */
    ~PlanePilotApp();
    
    /**
     * @brief Initialize the application
     * @return true if initialization successful, false otherwise
     */
    bool initialize();
    
    /**
     * @brief Run the main application loop
     * @return Application exit code
     */
    int run();
    
    /**
     * @brief Get the GLFW window handle
     * @return Pointer to GLFW window
     */
    GLFWwindow* getWindow() const { return m_window; }
    
    /**
     * @brief Get application width
     * @return Window width in pixels
     */
    int getWidth() const { return m_width; }
    
    /**
     * @brief Get application height
     * @return Window height in pixels
     */
    int getHeight() const { return m_height; }
    
    /**
     * @brief Check if application should close
     * @return true if application should close
     */
    bool shouldClose() const;

private:
    // Window management
    GLFWwindow* m_window;
    int m_width;
    int m_height;
    std::string m_title;
    
    // GUI components
    std::unique_ptr<SplashScreen> m_splashScreen;
    std::unique_ptr<MainWindow> m_mainWindow;
    std::unique_ptr<WorkshopSelector> m_workshopSelector;
    
    // Workshop instances
    std::unique_ptr<PlanePilot::Workshops::HadwigerNelsonWorkshop> m_hadwigerWorkshop;
    std::unique_ptr<PlanePilot::Workshops::ChromaticOlympics> m_chromaticOlympics;
    std::unique_ptr<PlanePilot::Workshops::GeometrySequencing> m_geometrySequencing;
    std::unique_ptr<PlanePilot::Workshops::SphereOMatic> m_sphereOMatic;
    
    // Graphics
    std::unique_ptr<PlanePilot::Graphics::Renderer> m_renderer;
    
    // GUI managers
    std::unique_ptr<PlanePilot::GUI::FontManager> m_fontManager;
    std::unique_ptr<PlanePilot::GUI::ThemeManager> m_themeManager;
    
    // Application state
    enum class AppState {
        SPLASH_SCREEN,
        MAIN_MENU,
        WORKSHOP_SELECT,
        IN_WORKSHOP,
        EXITING
    };
    
    AppState m_currentState;
    AppState m_previousState;
    
    // Initialization methods
    bool initializeWindow();
    bool initializeOpenGL();
    bool initializeGUI();
    bool initializeWorkshops();
    bool initializeGraphics();
    
    // Main loop methods
    void update();
    void render();
    void handleInput();
    
    // State management
    void setState(AppState newState);
    void updateSplashScreen();
    void updateMainMenu();
    void updateWorkshopSelector();
    void updateWorkshop();
    
    // Rendering methods
    void renderSplashScreen();
    void renderMainMenu();
    void renderWorkshopSelector();
    void renderWorkshop();
    
    // Event callbacks
    static void windowCloseCallback(GLFWwindow* window);
    static void windowResizeCallback(GLFWwindow* window, int width, int height);
    static void keyCallback(GLFWwindow* window, int key, int scancode, int action, int mods);
    static void mouseCallback(GLFWwindow* window, int button, int action, int mods);
    static void cursorPosCallback(GLFWwindow* window, double xpos, double ypos);
    static void scrollCallback(GLFWwindow* window, double xoffset, double yoffset);
    
    // Cleanup
    void cleanup();
    
    // Static instance for callbacks
    static PlanePilotApp* s_instance;
};

#endif // PLANE_PILOT_APP_H