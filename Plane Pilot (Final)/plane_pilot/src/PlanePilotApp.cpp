/*
 * PlanePilotApp.cpp - Main Application Implementation
 */

#include "PlanePilotApp.h"
#include "utils/Logger.h"

// GLFW and OpenGL includes
#include <GLFW/glfw3.h>
#include <GL/gl.h>

// GUI components
#include "gui/SplashScreen.h"
#include "gui/MainWindow.h"
#include "gui/WorkshopSelector.h"

// Workshops
#include "workshops/HadwigerNelsonWorkshop.h"
#include "workshops/ChromaticOlympics.h"
#include "workshops/GeometrySequencing.h"
#include "workshops/SphereOMatic.h"

// Graphics
#include "graphics/Renderer.h"

// GUI managers
#include "gui/FontManager.h"
#include "gui/ThemeManager.h"

// Static instance for callbacks
PlanePilotApp* PlanePilotApp::s_instance = nullptr;

PlanePilotApp::PlanePilotApp()
    : m_window(nullptr)
    , m_width(1200)
    , m_height(800)
    , m_title("Plane Pilot - Educational Geometry Software")
    , m_currentState(AppState::SPLASH_SCREEN)
    , m_previousState(AppState::SPLASH_SCREEN)
{
    s_instance = this;
    Logger::info("PlanePilotApp constructor called");
}

PlanePilotApp::~PlanePilotApp() {
    cleanup();
    s_instance = nullptr;
    Logger::info("PlanePilotApp destructor completed");
}

bool PlanePilotApp::initialize() {
    Logger::info("Initializing Plane Pilot application...");
    
    // Initialize window
    if (!initializeWindow()) {
        Logger::error("Failed to initialize window");
        return false;
    }
    
    // Initialize OpenGL
    if (!initializeOpenGL()) {
        Logger::error("Failed to initialize OpenGL");
        return false;
    }
    
    // Initialize graphics
    if (!initializeGraphics()) {
        Logger::error("Failed to initialize graphics");
        return false;
    }
    
    // Initialize GUI managers
    if (!initializeGUI()) {
        Logger::error("Failed to initialize GUI");
        return false;
    }
    
    // Initialize workshops
    if (!initializeWorkshops()) {
        Logger::error("Failed to initialize workshops");
        return false;
    }
    
    Logger::info("Plane Pilot application initialized successfully");
    return true;
}

bool PlanePilotApp::initializeWindow() {
    Logger::info("Initializing GLFW window...");
    
    // Initialize GLFW
    if (!glfwInit()) {
        Logger::error("Failed to initialize GLFW");
        return false;
    }
    
    // Configure GLFW
    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);
    glfwWindowHint(GLFW_RESIZABLE, GL_TRUE);
    
    // Create window
    m_window = glfwCreateWindow(m_width, m_height, m_title.c_str(), nullptr, nullptr);
    if (!m_window) {
        Logger::error("Failed to create GLFW window");
        glfwTerminate();
        return false;
    }
    
    // Set context and callbacks
    glfwMakeContextCurrent(m_window);
    glfwSetWindowUserPointer(m_window, this);
    
    glfwSetWindowCloseCallback(m_window, windowCloseCallback);
    glfwSetWindowSizeCallback(m_window, windowResizeCallback);
    glfwSetKeyCallback(m_window, keyCallback);
    glfwSetMouseButtonCallback(m_window, mouseCallback);
    glfwSetCursorPosCallback(m_window, cursorPosCallback);
    glfwSetScrollCallback(m_window, scrollCallback);
    
    Logger::info("GLFW window initialized successfully");
    return true;
}

bool PlanePilotApp::initializeOpenGL() {
    Logger::info("Initializing OpenGL...");
    
    // Set viewport
    glViewport(0, 0, m_width, m_height);
    
    // Enable blending for transparency
    glEnable(GL_BLEND);
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
    
    // Set clear color
    glClearColor(0.1f, 0.1f, 0.2f, 1.0f);
    
    Logger::info("OpenGL initialized successfully");
    return true;
}

bool PlanePilotApp::initializeGraphics() {
    Logger::info("Initializing graphics renderer...");
    
    m_renderer = std::make_unique<PlanePilot::Graphics::Renderer>();
    if (!m_renderer->initialize(m_width, m_height)) {
        Logger::error("Failed to initialize graphics renderer");
        return false;
    }
    
    Logger::info("Graphics renderer initialized successfully");
    return true;
}

bool PlanePilotApp::initializeGUI() {
    Logger::info("Initializing GUI components...");
    
    // Initialize font manager
    m_fontManager = std::make_unique<PlanePilot::GUI::FontManager>();
    if (!m_fontManager->initialize()) {
        Logger::error("Failed to initialize font manager");
        return false;
    }
    
    // Initialize theme manager
    m_themeManager = std::make_unique<PlanePilot::GUI::ThemeManager>();
    m_themeManager->loadDefaultTheme();
    
    // Initialize GUI components
    m_splashScreen = std::make_unique<SplashScreen>(this);
    m_mainWindow = std::make_unique<MainWindow>(this);
    m_workshopSelector = std::make_unique<WorkshopSelector>(this);
    
    Logger::info("GUI components initialized successfully");
    return true;
}

bool PlanePilotApp::initializeWorkshops() {
    Logger::info("Initializing workshops...");
    
    // Initialize all workshop instances
    m_hadwigerWorkshop = std::make_unique<PlanePilot::Workshops::HadwigerNelsonWorkshop>(this);
    m_chromaticOlympics = std::make_unique<PlanePilot::Workshops::ChromaticOlympics>(this);
    m_geometrySequencing = std::make_unique<PlanePilot::Workshops::GeometrySequencing>(this);
    m_sphereOMatic = std::make_unique<PlanePilot::Workshops::SphereOMatic>(this);
    
    Logger::info("Workshops initialized successfully");
    return true;
}

int PlanePilotApp::run() {
    Logger::info("Starting main application loop...");
    
    // Main loop
    while (!shouldClose()) {
        // Poll events
        glfwPollEvents();
        
        // Update application state
        update();
        
        // Render frame
        render();
        
        // Swap buffers
        glfwSwapBuffers(m_window);
    }
    
    Logger::info("Main application loop ended");
    return 0;
}

bool PlanePilotApp::shouldClose() const {
    return m_window ? glfwWindowShouldClose(m_window) : true;
}

void PlanePilotApp::update() {
    switch (m_currentState) {
        case AppState::SPLASH_SCREEN:
            updateSplashScreen();
            break;
        case AppState::MAIN_MENU:
            updateMainMenu();
            break;
        case AppState::WORKSHOP_SELECT:
            updateWorkshopSelector();
            break;
        case AppState::IN_WORKSHOP:
            updateWorkshop();
            break;
        case AppState::EXITING:
            // Will exit on next loop iteration
            break;
    }
}

void PlanePilotApp::render() {
    // Clear screen
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    
    // Render based on current state
    switch (m_currentState) {
        case AppState::SPLASH_SCREEN:
            renderSplashScreen();
            break;
        case AppState::MAIN_MENU:
            renderMainMenu();
            break;
        case AppState::WORKSHOP_SELECT:
            renderWorkshopSelector();
            break;
        case AppState::IN_WORKSHOP:
            renderWorkshop();
            break;
        case AppState::EXITING:
            break;
    }
}

void PlanePilotApp::updateSplashScreen() {
    if (m_splashScreen) {
        m_splashScreen->update();
        
        // Check if splash screen should transition
        if (m_splashScreen->isComplete()) {
            setState(AppState::MAIN_MENU);
        }
    }
}

void PlanePilotApp::updateMainMenu() {
    if (m_mainWindow) {
        m_mainWindow->update();
        
        // Check for state transitions
        if (m_mainWindow->shouldExit()) {
            setState(AppState::EXITING);
        } else if (m_mainWindow->shouldGoToWorkshops()) {
            setState(AppState::WORKSHOP_SELECT);
        }
    }
}

void PlanePilotApp::updateWorkshopSelector() {
    if (m_workshopSelector) {
        m_workshopSelector->update();
        
        // Check for workshop selection
        if (m_workshopSelector->hasSelectedWorkshop()) {
            setState(AppState::IN_WORKSHOP);
        } else if (m_workshopSelector->shouldGoBack()) {
            setState(AppState::MAIN_MENU);
        }
    }
}

void PlanePilotApp::updateWorkshop() {
    // Update the currently selected workshop
    // This would be expanded based on which workshop is active
    // For now, we'll just go back to the workshop selector
    if (glfwGetKey(m_window, GLFW_KEY_ESCAPE) == GLFW_PRESS) {
        setState(AppState::WORKSHOP_SELECT);
    }
}

void PlanePilotApp::renderSplashScreen() {
    if (m_splashScreen) {
        m_splashScreen->render();
    }
}

void PlanePilotApp::renderMainMenu() {
    if (m_mainWindow) {
        m_mainWindow->render();
    }
}

void PlanePilotApp::renderWorkshopSelector() {
    if (m_workshopSelector) {
        m_workshopSelector->render();
    }
}

void PlanePilotApp::renderWorkshop() {
    // Render the currently selected workshop
    // This would be expanded based on which workshop is active
}

void PlanePilotApp::setState(AppState newState) {
    if (m_currentState != newState) {
        m_previousState = m_currentState;
        m_currentState = newState;
        Logger::info("Application state changed: " + std::to_string(static_cast<int>(m_previousState)) + 
                    " -> " + std::to_string(static_cast<int>(m_currentState)));
    }
}

void PlanePilotApp::cleanup() {
    Logger::info("Cleaning up Plane Pilot application...");
    
    // Destroy workshops
    m_sphereOMatic.reset();
    m_geometrySequencing.reset();
    m_chromaticOlympics.reset();
    m_hadwigerWorkshop.reset();
    
    // Destroy GUI components
    m_workshopSelector.reset();
    m_mainWindow.reset();
    m_splashScreen.reset();
    
    // Destroy managers
    m_themeManager.reset();
    m_fontManager.reset();
    
    // Destroy renderer
    m_renderer.reset();
    
    // Destroy window
    if (m_window) {
        glfwDestroyWindow(m_window);
        m_window = nullptr;
    }
    
    // Terminate GLFW
    glfwTerminate();
    
    Logger::info("Plane Pilot application cleanup completed");
}

// GLFW callback implementations
void PlanePilotApp::windowCloseCallback(GLFWwindow* window) {
    if (s_instance) {
        s_instance->setState(AppState::EXITING);
    }
}

void PlanePilotApp::windowResizeCallback(GLFWwindow* window, int width, int height) {
    if (s_instance) {
        s_instance->m_width = width;
        s_instance->m_height = height;
        glViewport(0, 0, width, height);
        
        if (s_instance->m_renderer) {
            s_instance->m_renderer->resize(width, height);
        }
    }
}

void PlanePilotApp::keyCallback(GLFWwindow* window, int key, int scancode, int action, int mods) {
    // Handle key input
}

void PlanePilotApp::mouseCallback(GLFWwindow* window, int button, int action, int mods) {
    // Handle mouse button input
}

void PlanePilotApp::cursorPosCallback(GLFWwindow* window, double xpos, double ypos) {
    // Handle mouse movement
}

void PlanePilotApp::scrollCallback(GLFWwindow* window, double xoffset, double yoffset) {
    // Handle scroll input
}