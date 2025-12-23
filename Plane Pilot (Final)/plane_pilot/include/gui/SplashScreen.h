/*
 * SplashScreen.h - Splash Screen GUI Component
 * 
 * Displays the application splash screen with the breakthrough discovery
 * and mathematical proof information.
 */

#ifndef SPLASH_SCREEN_H
#define SPLASH_SCREEN_H

#include <memory>
#include <chrono>
#include <string>
#include <vector>

class PlanePilotApp;

namespace PlanePilot {
    namespace Graphics {
        class Texture;
        class Renderer;
    }
    namespace GUI {
        class FontManager;
    }
}

/**
 * @brief Splash screen component with breakthrough display
 * 
 * This splash screen boldly declares the Hadwiger-Nelson breakthrough
 * and shows why other methods cannot work through visual demonstration.
 */
class SplashScreen {
public:
    /**
     * @brief Constructor
     * @param app Pointer to the main application
     */
    explicit SplashScreen(PlanePilotApp* app);
    
    /**
     * @brief Destructor
     */
    ~SplashScreen();
    
    /**
     * @brief Initialize the splash screen
     * @return true if initialization successful
     */
    bool initialize();
    
    /**
     * @brief Update splash screen state
     */
    void update();
    
    /**
     * @brief Render the splash screen
     */
    void render();
    
    /**
     * @brief Check if splash screen is complete
     * @return true if splash screen should transition
     */
    bool isComplete() const { return m_isComplete; }
    
    /**
     * @brief Force completion (for user input)
     */
    void complete() { m_isComplete = true; }

private:
    PlanePilotApp* m_app;
    
    // Timing
    std::chrono::steady_clock::time_point m_startTime;
    float m_displayDuration;
    bool m_isComplete;
    
    // Visual elements
    std::unique_ptr<PlanePilot::Graphics::Texture> m_logoTexture;
    std::unique_ptr<PlanePilot::Graphics::Texture> m_breakthroughTexture;
    
    // Colors and styling
    struct Color {
        float r, g, b, a;
        Color(float r = 1.0f, float g = 1.0f, float b = 1.0f, float a = 1.0f)
            : r(r), g(g), b(b), a(a) {}
    };
    
    Color m_backgroundColor;
    Color m_titleColor;
    Color m_subtitleColor;
    Color m_textColor;
    Color m_highlightColor;
    
    // Content
    std::string m_title;
    std::string m_subtitle;
    std::string m_breakthroughText;
    std::vector<std::string> m_keyPoints;
    
    // Animation
    float m_fadeIn;
    float m_pulseEffect;
    
    // Rendering methods
    void renderBackground();
    void renderTitle();
    void renderBreakthroughDisplay();
    void renderKeyPoints();
    void renderMathematicalProof();
    void renderProgressBar();
    
    // Layout helpers
    void calculateLayout();
    void loadContent();
    
    // Animation methods
    void updateAnimations();
    
    // Breakthrough visualization
    void renderChromaticVisualization();
    void renderHadwigerNelsonGraph();
    void renderThreePineconesDiagram();
};

#endif // SPLASH_SCREEN_H