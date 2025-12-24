/* 
 * ShapeNumbersWorkshop.h - Geometry and Spatial Mathematics for Grade 1
 * 
 * Teaching children about geometric shapes, spatial relationships, and
 * the mathematical properties of shapes based on the original analyzer.
 */

#pragma once

#include "../workshops/WorkshopBase.h"
#include "../characters/FriendlyGuide.h"
#include "../characters/MathMagician.h"
#include "../AI/ChildAIHelper.h"
#include "../math/GeometryAnalyzer.h"
#include "../math/SpatialReasoning.h"
#include "../math/ShapeCalculator.h"
#include "../psychology/LearningStyleAdapter.h"
#include <memory>
#include <vector>
#include <string>
#include <map>
#include <chrono>

namespace Recipy {
namespace Workshops {

struct GeometricShape {
    int id;
    std::string name;
    std::string description;
    int sides;
    int corners;
    std::vector<double> side_lengths;
    double area;
    double perimeter;
    std::string child_friendly_properties;
    std::string visual_representation;
    int difficulty_level;
};

struct SpatialPuzzle {
    int id;
    std::string puzzle_name;
    std::string description;
    std::vector<std::string> shapes_involved;
    std::string challenge_question;
    std::string solution;
    std::string reasoning;
    std::string spatial_concept;
};

struct ShapePattern {
    int id;
    std::string pattern_name;
    std::vector<std::string> shape_sequence;
    std::string pattern_rule;
    std::string next_shape;
    std::string mathematical_principle;
};

struct Transformation {
    int id;
    std::string transformation_name;
    std::string original_shape;
    std::string transformed_shape;
    std::string transformation_type;
    std::string explanation;
    std::string real_world_example;
};

class ShapeNumbersWorkshop : public WorkshopBase {
public:
    ShapeNumbersWorkshop();
    virtual ~ShapeNumbersWorkshop();
    
    // WorkshopBase overrides
    bool initialize() override;
    void start() override;
    void update() override;
    void render() override;
    void handleInput() override;
    bool isComplete() const override;
    double getProgress() const override;
    void endWorkshop() override;
    
    // Shape exploration methods
    void exploreBasicShapes();
    void exploreShapeProperties();
    void exploreSpatialRelationships();
    void solveSpatialPuzzles();
    void discoverShapePatterns();
    void exploreTransformations();
    void createShapeArt();
    void measureShapes();
    
private:
    // Core components
    std::unique_ptr<Characters::FriendlyGuide> m_guide;
    std::unique_ptr<Characters::MathMagician> m_aiHelper;
    std::unique_ptr<Math::GeometryAnalyzer> m_geometryAnalyzer;
    std::unique_ptr<Math::SpatialReasoning> m_spatialReasoning;
    std::unique_ptr<Math::ShapeCalculator> m_shapeCalculator;
    std::unique_ptr<Psychology::LearningStyleAdapter> m_learningAdapter;
    
    // Workshop state
    bool m_isRunning;
    int m_currentShape;
    int m_shapesExplored;
    int m_puzzlesSolved;
    int m_patternsDiscovered;
    double m_learningProgress;
    std::chrono::steady_clock::time_point m_startTime;
    std::chrono::steady_clock::time_point m_lastBreakTime;
    bool m_needsBreak;
    int m_attentionSpanMinutes;
    double m_currentDifficulty;
    
    // Collections
    std::vector<GeometricShape> m_shapes;
    std::vector<SpatialPuzzle> m_puzzles;
    std::vector<ShapePattern> m_patterns;
    std::vector<Transformation> m_transformations;
    std::map<std::string, std::string> m_shapeKnowledge;
    std::vector<std::string> m_discoveredShapes;
    
    // Mastery tracking
    std::map<std::string, bool> m_masteredShapes;
    int m_complexShapesUnderstood;
    std::string m_favoriteShape;
    std::vector<std::string> m_createdPatterns;
    
    // Initialization methods
    bool initializeComponents();
    void initializeGeometricShapes();
    void initializeSpatialPuzzles();
    void initializeShapePatterns();
    void initializeTransformations();
    void initializeShapeKnowledge();
    
    // Shape exploration methods
    void exploreCircle();
    void exploreTriangle();
    void exploreSquare();
    void exploreRectangle();
    void explorePentagon();
    void exploreHexagon();
    void exploreOctagon();
    void exploreComplexShapes();
    
    // Spatial reasoning methods
    void explorePosition();
    void exploreDirection();
    void exploreDistance();
    void exploreRotation();
    void exploreReflection();
    void exploreScaling();
    
    // Pattern methods
    void exploreShapeSequences();
    void exploreTessellations();
    void exploreSymmetry();
    void exploreFractals();
    
    // Advanced geometry concepts
    void exploreAreaAndPerimeter();
    void exploreVolume();
    void exploreCoordinates();
    void exploreAngles();
    
    // Interactive methods
    void buildWithShapes();
    void createShapeCombinations();
    void solveShapeMysteries();
    void playShapeGames();
    
    // Visualization and interaction
    void displayShape(const GeometricShape& shape);
    void showSpatialRelationship(const std::string& relationship);
    void animateTransformation(const Transformation& transformation);
    void createShapeArt(const std::vector<std::string>& shapes);
    
    // Assessment and celebration
    void assessShapeUnderstanding();
    void celebrateShapeDiscovery();
    void updateProgress();
    void checkForBreak();
    void suggestBreak();
    
    // Utility methods
    double calculateArea(const std::string& shape_name, const std::vector<double>& dimensions);
    double calculatePerimeter(const std::string& shape_name, const std::vector<double>& dimensions);
    bool canTessellate(const std::string& shape_name);
    std::string explainShapeProperty(const std::string& property, const std::string& shape_name);
    
    // Cleanup
    void cleanup();
};

} // namespace Workshops
} // namespace Recipy