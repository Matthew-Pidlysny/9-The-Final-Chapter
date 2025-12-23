/*
    * FontManager.cpp - Font Management Implementation
    */

    #include "gui/FontManager.h"
    #include "utils/Logger.h"
    #include <iostream>

    namespace PlanePilot {
    namespace GUI {

    FontManager::FontManager() : m_initialized(false) {}

    FontManager::~FontManager() {
        shutdown();
    }

    bool FontManager::initialize() {
        if (m_initialized) {
            return true;
        }
        
        Logger::info("Initializing Font Manager...");
        
        // Load default fonts
        loadFont("default", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf");
        loadFont("title", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf");
        
        m_initialized = true;
        Logger::info("Font Manager initialized successfully");
        return true;
    }

    void FontManager::shutdown() {
        if (!m_initialized) {
            return;
        }
        
        Logger::info("Shutting down Font Manager...");
        
        // Clean up all loaded fonts
        for (auto& font : m_fonts) {
            // In a real implementation, we would clean up font resources here
            delete static_cast<char*>(font.second);
        }
        m_fonts.clear();
        
        m_initialized = false;
    }

    void FontManager::loadFont(const std::string& name, const std::string& path) {
        Logger::info("Loading font: " + name + " from " + path);
        
        // In a real implementation, we would load the actual font file
        // For now, we'll just simulate loading
        void* fontData = new char[100]; // Simulated font data
        m_fonts[name] = fontData;
        
        Logger::info("Font loaded successfully: " + name);
    }

    void* FontManager::getFont(const std::string& name) const {
        auto it = m_fonts.find(name);
        if (it != m_fonts.end()) {
            return it->second;
        }
        
        // Return default font if requested font not found
        auto defaultIt = m_fonts.find("default");
        return (defaultIt != m_fonts.end()) ? defaultIt->second : nullptr;
    }

    } // namespace GUI
    } // namespace PlanePilot