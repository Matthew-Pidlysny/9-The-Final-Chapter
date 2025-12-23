/*
    * HadwigerNelsonWorkshop.h - Essential Hadwiger-Nelson Problem Workshop
    * 
    * Comprehensive 3D and 2D visualization of the Hadwiger-Nelson problem
    * with the breakthrough solution and interactive modeling capabilities.
    */

    #ifndef HADWIGER_NELSON_WORKSHOP_H
    #define HADWIGER_NELSON_WORKSHOP_H

    #include <memory>
    #include <vector>
    #include <string>

    class PlanePilotApp;

    namespace PlanePilot {
        namespace Graphics {
            class Renderer;
            class Shader;
            class Texture;
            class Camera3D;
            class Model3D;
        }
        namespace Math {
            struct Point2D;
            struct Point3D;
            class ChromaticGraph;
            class TrigonometricPolynomial;
        }
        namespace GUI {
            class FontManager;
            class UI;
        }
        namespace Workshops {

    /**
     * @brief Workshop for exploring the Hadwiger-Nelson problem
     * 
     * This workshop provides comprehensive tools for understanding and exploring
     * the Hadwiger-Nelson problem including:
     * - 3D visualization of point configurations
     * - Interactive chromatic graph analysis
     * - Real-time unit-distance edge detection
     * - Mathematical proof visualization
     * - Comparison of different approaches
     */
    class HadwigerNelsonWorkshop {
    public:
        /**
         * @brief Constructor
         * @param app Pointer to main application
         */
        explicit HadwigerNelsonWorkshop(PlanePilotApp* app);
        
        /**
         * @brief Destructor
         */
        ~HadwigerNelsonWorkshop();
        
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
         * @brief Set number of points for configuration
         * @param numPoints Number of points (3-182)
         */
        void setNumberOfPoints(int numPoints);
        
        /**
         * @brief Get current chromatic number
         * @return Current chromatic number
         */
        int getCurrentChromaticNumber() const;
        
        /**
         * @brief Export current configuration
         * @param filename Export filename
         */
        void exportConfiguration(const std::string& filename);

    private:
        PlanePilotApp* m_app;
        
        // Graphics components
        std::unique_ptr<PlanePilot::Graphics::Renderer> m_renderer;
        std::unique_ptr<PlanePilot::Graphics::Shader> m_basicShader;
        std::unique_ptr<PlanePilot::Graphics::Shader> m_chromaticShader;
        std::unique_ptr<PlanePilot::Graphics::Camera3D> m_camera;
        
        // Mathematical components
        std::unique_ptr<PlanePilot::Math::TrigonometricPolynomial> m_polyGenerator;
        std::unique_ptr<PlanePilot::Math::ChromaticGraph> m_chromaticGraph;
        
        // Point configurations
        std::vector<PlanePilot::Math::Point2D> m_points2D;
        std::vector<PlanePilot::Math::Point3D> m_points3D;
        
        // Visualization options
        struct VisualizationSettings {
            bool show3DView = true;
            bool show2DView = true;
            bool showUnitDistanceEdges = true;
            bool showChromaticColors = true;
            bool showMathematicalProof = true;
            bool animatePoints = false;
            float pointSize = 8.0f;
            float edgeWidth = 2.0f;
            float rotationSpeed = 0.5f;
            float zoomLevel = 1.0f;
        };
        
        VisualizationSettings m_settings;
        
        // State
        int m_currentNumPoints;
        int m_currentChromaticNumber;
        bool m_isAnimating;
        float m_animationTime;
        
        // UI components
        std::unique_ptr<PlanePilot::GUI::UI> m_ui;
        
        // Breakthrough data
        struct BreakthroughData {
            int maxChromatic;
            int bestConfiguration;
            std::vector<int> chromaticProgression;
            std::vector<std::string> keyInsights;
        };
        
        BreakthroughData m_breakthroughData;
        
        // Initialization methods
        bool initializeGraphics();
        bool initializeMathematics();
        bool initializeUI();
        bool loadBreakthroughData();
        
        // Update methods
        void updateAnimations();
        void updateCamera();
        void updateUI();
        void updateChromaticAnalysis();
        
        // Rendering methods
        void render3DView();
        void render2DView();
        void renderUI();
        void renderUnitDistanceEdges();
        void renderChromaticVisualization();
        void renderMathematicalProof();
        void renderComparisonView();
        
        // Mathematical methods
        void generatePointConfiguration(int numPoints);
        void calculateChromaticNumber();
        void detectUnitDistanceEdges();
        void optimizePointLayout();
        
        // Interaction methods
        void handleMouseInput();
        void handleKeyboardInput();
        void handle3DManipulation();
        void handle2DInteraction();
        
        // Visualization helpers
        void renderPoint(const PlanePilot::Math::Point3D& point, const float* color);
        void renderEdge(const PlanePilot::Math::Point3D& p1, const PlanePilot::Math::Point3D& p2, const float* color);
        void renderColorLegend();
        void renderStatistics();
        
        // Educational content
        void displayProblemStatement();
        void displaySolutionApproach();
        void displayMathematicalProof();
        void displayComparisonWithOtherMethods();
        
        // Animation methods
        void animatePointGeneration();
        void animateChromaticColoring();
        void animateUnitDistanceDetection();
        
        // Export/Import
        void exportToJSON(const std::string& filename);
        void exportToCSV(const std::string& filename);
        void exportToImage(const std::string& filename);
        void importConfiguration(const std::string& filename);
        
        // Comparison tools
        void compareWithTraditionalMethods();
        void compareWithKnownSolutions();
        void demonstrateBreakthrough();
        
        // 3D Modeling
        void create3DPointConfiguration();
        void create3DGraphStructure();
        void create3DChromaticVisualization();
        
        // Cleanup
        void cleanup();
    };

    } // namespace Workshops
    } // namespace PlanePilot

    #endif // HADWIGER_NELSON_WORKSHOP_H