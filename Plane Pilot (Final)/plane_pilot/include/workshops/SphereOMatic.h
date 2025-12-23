/*
 * SphereOMatic.h - 3D Sphere Modeling and AI-Generated Geometry Workshop
 * 
 * Uses the 5 sphere models from je-suis-ballin.py and AI to create novel
 * geometric sphere configurations with collision testing and extremal analysis.
 */

#ifndef SPHERE_O_MATIC_H
#define SPHERE_O_MATIC_H

#include <memory>
#include <vector>
#include <string>

class PlanePilotApp;

namespace PlanePilot {
    namespace Graphics {
        class Renderer;
        class Shader;
        class Camera3D;
        class Model3D;
        class Texture;
    }
    namespace Math {
        struct Point3D;
        struct Sphere;
        class CollisionDetector;
        class GeometryAI;
    }
    namespace AI {
        class GeometryGenerator;
        class AIConnector;
    }
    namespace GUI {
        class UI;
    }
    namespace Workshops {

/**
 * @brief Workshop for 3D sphere modeling and AI-generated geometry
 * 
 * This workshop provides:
 * - 3D visualization of sphere models from je-suis-ballin.py
 * - Collision detection at extremal configurations
 * - AI-powered novel geometry generation
 * - Real-time physics simulation
 * - Interactive 3D manipulation
 */

   class SphereOMatic {
public:
    /**
     * @brief Constructor
     * @param app Pointer to main application
     */
    explicit SphereOMatic(PlanePilotApp* app);
    
    /**
     * @brief Destructor
     */
    ~SphereOMatic();
    
    /**
     * @brief Initialize the workshop
     * @return true if initialization successful
     */
    bool initialize();
    
    /**
     * @brief Update workshop state
     */
    void update();
    
    /**
     * @brief Render the workshop
     */
    void render();
    
    /**
     * @brief Handle input events
     */
    void handleInput();
    
    /**
     * @brief Reset workshop to initial state
     */
    void reset();
    
    /**
     * @brief Generate AI sphere
     * @param prompt AI prompt for sphere generation
     */
    void generateAISphere(const std::string& prompt);
    
    /**
     * @brief Test collisions
     */
    void testCollisions();
    
    /**
     * @brief Export sphere configuration
     * @param filename Export filename
     */
    void exportConfiguration(const std::string& filename);

private:
    PlanePilotApp* m_app;
    
    // Graphics components
    std::unique_ptr<PlanePilot::Graphics::Renderer> m_renderer;
    std::unique_ptr<PlanePilot::Graphics::Shader> m_phongShader;
    std::unique_ptr<PlanePilot::Graphics::Shader> m_wireframeShader;
    std::unique_ptr<PlanePilot::Graphics::Camera3D> m_camera;
    std::unique_ptr<PlanePilot::Graphics::Model3D> m_sphereModel;
    
    // Mathematical components
    std::unique_ptr<PlanePilot::Math::CollisionDetector> m_collisionDetector;
    
    // AI components
    std::unique_ptr<PlanePilot::AI::GeometryGenerator> m_geometryGenerator;
    std::unique_ptr<PlanePilot::AI::AIConnector> m_aiConnector;
    
    // Sphere models from je-suis-ballin.py
    std::vector<PlanePilot::Math::Sphere> m_originalSpheres;
    std::vector<PlanePilot::Math::Sphere> m_currentSpheres;
    std::vector<PlanePilot::Math::Sphere> m_aiGeneratedSpheres;
    
    // Visualization settings
    struct VisualizationSettings {
        bool showWireframe = false;
        bool showSolid = true;
        bool showCollisions = true;
        bool showExtremes = true;
        bool showAIGenerated = true;
        bool simulatePhysics = false;
        float rotationSpeed = 0.5f;
        float zoomLevel = 1.0f;
        int quality = 32;  // Sphere subdivision quality
    };
    
    VisualizationSettings m_settings;
    
    // State
    bool m_isSimulating;
    bool m_isTestingCollisions;
    float m_simulationTime;
    float m_collisionTestProgress;
    
    // UI components
    std::unique_ptr<PlanePilot::GUI::UI> m_ui;
    
    // AI integration
    struct AIConfig {
        std::string apiEndpoint = "https://api.openai.com/v1/chat/completions";
        std::string apiKey = "";  // Would be configured
        std::string model = "gpt-3.5-turbo";
        float temperature = 0.7f;
        int maxTokens = 1000;
    };
    
    AIConfig m_aiConfig;
    
    // Initialization methods
    bool initializeGraphics();
    bool initializeMathematics();
    bool initializeAI();
    bool initializeUI();
    bool loadOriginalSpheres();
    
    // Update methods
    void updateSimulation();
    void updateCollisions();
    void updateAI();
    void updateCamera();
    void updateUI();
    
    // Rendering methods
    void render3DScene();
    void renderSpheres();
    void renderWireframeSpheres();
    void renderCollisions();
    void renderExtremes();
    void renderAISpheres();
    void renderUI();
    void renderStatistics();
    
    // Sphere management
    void loadOriginalSphereModels();
    void createSphereGeometry();
    void updateSpherePhysics();
    void optimizeSphereLayout();
    
    // Collision testing
    void detectCollisions();
    void testExtremalConfigurations();
    void analyzeCollisionPatterns();
    void generateCollisionReport();
    
    // AI geometry generation
    void connectToAI();
    void generateNovelGeometry();
    void analyzeAIGeometry();
    void validateAIGeometry();
    void integrateAIGeometry();
    
    // Interaction methods
    void handleMouseInput();
    void handleKeyboardInput();
    void handle3DManipulation();
    void handleSphereSelection();
    
    // Export methods
    void exportToJSON(const std::string& filename);
    void exportToOBJ(const std::string& filename);
    void exportToSTL(const std::string& filename);
    void exportCollisionReport(const std::string& filename);
    
    // Analysis methods
    void analyzeGeometryProperties();
    void compareSphereModels();
    void generateStatisticalReport();
    
    // Cleanup
    void cleanup();
};

} // namespace Workshops
} // namespace PlanePilot

#endif // SPHERE_O_MATIC_H