/*
    * ThemeManager.cpp - Theme Management Implementation
    */

    #include "gui/ThemeManager.h"
    #include "utils/Logger.h"

    namespace PlanePilot {
    namespace GUI {

    ThemeManager::ThemeManager() : m_initialized(false), m_currentTheme("default") {}

    ThemeManager::~ThemeManager() {
        shutdown();
    }

    bool ThemeManager::initialize() {
        if (m_initialized) {
            return true;
        }
        
        Logger::info("Initializing Theme Manager...");
        
        // Create default theme
        ThemeColors defaultTheme = {
            {0.95f, 0.95f, 0.95f, 1.0f}, // background
            {0.1f, 0.1f, 0.1f, 1.0f},     // foreground
            {0.2f, 0.4f, 0.8f, 1.0f},     // accent
            {0.8f, 0.8f, 0.2f, 1.0f}      // highlight
        };
        
        m_themes["default"] = defaultTheme;
        m_currentTheme = "default";
        
        m_initialized = true;
        Logger::info("Theme Manager initialized successfully");
        return true;
    }

    void ThemeManager::shutdown() {
        if (!m_initialized) {
            return;
        }
        
        Logger::info("Shutting down Theme Manager...");
        
        m_themes.clear();
        m_initialized = false;
    }

    void ThemeManager::loadDefaultTheme() {
        Logger::info("Loading default theme");
        m_currentTheme = "default";
    }

    void ThemeManager::loadTheme(const std::string& name) {
        auto it = m_themes.find(name);
        if (it != m_themes.end()) {
            m_currentTheme = name;
            Logger::info("Theme loaded: " + name);
        } else {
            Logger::warning("Theme not found: " + name + ", using default");
            loadDefaultTheme();
        }
    }

    const ThemeColors& ThemeManager::getCurrentTheme() const {
        auto it = m_themes.find(m_currentTheme);
        if (it != m_themes.end()) {
            return it->second;
        }
        
        // Return default theme if current theme not found
        static ThemeColors defaultTheme = {
            {0.95f, 0.95f, 0.95f, 1.0f}, // background
            {0.1f, 0.1f, 0.1f, 1.0f},     // foreground
            {0.2f, 0.4f, 0.8f, 1.0f},     // accent
            {0.8f, 0.8f, 0.2f, 1.0f}      // highlight
        };
        return defaultTheme;
    }

    const float* ThemeManager::getBackgroundColor() const {
        return getCurrentTheme().background;
    }

    const float* ThemeManager::getForegroundColor() const {
        return getCurrentTheme().foreground;
    }

    const float* ThemeManager::getAccentColor() const {
        return getCurrentTheme().accent;
    }

    } // namespace GUI
    } // namespace PlanePilot