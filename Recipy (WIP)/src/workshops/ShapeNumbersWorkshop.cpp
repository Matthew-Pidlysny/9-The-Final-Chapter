/*
 * ShapeNumbersWorkshop.cpp - Making Geometry Child-Friendly
 */

#include "workshops/ShapeNumbersWorkshop.h"
#include "utils/Logger.h"
#include "utils/ColorfulPrinter.h"
#include <iostream>
#include <vector>
#include <cmath>
#include <random>

namespace Recipy {
namespace Workshops {

ShapeNumbersWorkshop::ShapeNumbersWorkshop()
    : m_isRunning(false)
    , m_currentShape(0)
    , m_shapesExplored(0)
    , m_puzzlesSolved(0)
    , m_patternsDiscovered(0)
    , m_learningProgress(0.0)
    , m_needsBreak(false)
    , m_attentionSpanMinutes(15)
    , m_currentDifficulty(0.1)
    , m_complexShapesUnderstood(0) {
    
    Logger::info("ShapeNumbersWorkshop constructor - Creating geometry adventure!");
    m_startTime = std::chrono::steady_clock::now();
    m_lastBreakTime = m_startTime;
}

ShapeNumbersWorkshop::~ShapeNumbersWorkshop() {
    cleanup();
}

bool ShapeNumbersWorkshop::initialize() {
    Logger::info("Initializing Shape Numbers workshop...");
    
    try {
        ColorfulPrinter::printRainbow("🔷 Welcome to Shape Numbers! 🔷");
        ColorfulPrinter::printExcited("Let's discover the magical world of shapes and spatial relationships!");
        
        if (!initializeComponents()) {
            ColorfulPrinter::printSad("The geometric shapes wouldn't appear.");
            return false;
        }
        
        initializeGeometricShapes();
        
        ColorfulPrinter::printHappy("All shapes are ready to be explored!");
        return true;
    } catch (...) {
        return false;
    }
}

bool ShapeNumbersWorkshop::initializeComponents() {
    try {
        m_guide = std::make_unique<Characters::FriendlyGuide>();
        m_mathMagician = std::make_unique<Characters::MathMagician>();
        m_aiHelper = std::make_unique<AI::ChildAIHelper>();
        m_geometryAnalyzer = std::make_unique<Math::GeometryAnalyzer>();
        m_spatialReasoning = std::make_unique<Math::SpatialReasoning>();
        m_shapeCalculator = std::make_unique<Math::ShapeCalculator>();
        
        ColorfulPrinter::printHappy("Shape analysis system is ready!");
        return true;
    } catch (...) {
        return false;
    }
}

void ShapeNumbersWorkshop::initializeGeometricShapes() {
    Logger::info("Creating geometric shapes and spatial puzzles...");
    
    // Create basic shapes
    createCircle();
    createTriangle();
    createSquare();
    createRectangle();
    createPentagon();
    createHexagon();
    createOctagon();
    
    // Initialize puzzles and patterns
    initializeSpatialPuzzles();
    initializeShapePatterns();
    initializeTransformations();
    initializeShapeKnowledge();
    
    ColorfulPrinter::printLearning("Created " + std::to_string(m_shapes.size()) + " geometric shapes!");
}

void ShapeNumbersWorkshop::createCircle() {
    GeometricShape circle;
    circle.id = 1;
    circle.name = "Circle";
    circle.description = "A perfectly round shape with no corners";
    circle.sides = 0;
    circle.corners = 0;
    circle.side_lengths = {};  // No sides
    circle.area = 3.14159;     // π * 1^2 (unit circle)
    circle.perimeter = 6.28318; // 2π * 1
    circle.child_friendly_properties = "Perfectly round, no corners, rolls beautifully";
    circle.visual_representation = "⭕";
    circle.difficulty_level = 1;
    
    m_shapes.push_back(circle);
}

void ShapeNumbersWorkshop::createTriangle() {
    GeometricShape triangle;
    triangle.id = 2;
    triangle.name = "Triangle";
    triangle.description = "A shape with three sides and three corners";
    triangle.sides = 3;
    triangle.corners = 3;
    triangle.side_lengths = {1.0, 1.0, 1.0};  // Equilateral
    triangle.area = 0.433;  // sqrt(3)/4 for unit equilateral
    triangle.perimeter = 3.0;
    triangle.child_friendly_properties = "Three sides, three corners, very stable";
    triangle.visual_representation = "🔺";
    triangle.difficulty_level = 1;
    
    m_shapes.push_back(triangle);
}

void ShapeNumbersWorkshop::createSquare() {
    GeometricShape square;
    square.id = 3;
    square.name = "Square";
    square.description = "A shape with four equal sides and four right angles";
    square.sides = 4;
    square.corners = 4;
    square.side_lengths = {1.0, 1.0, 1.0, 1.0};
    square.area = 1.0;  // 1×1
    square.perimeter = 4.0;
    square.child_friendly_properties = "Four equal sides, perfect corners, can stack";
    square.visual_representation = "⬜";
    square.difficulty_level = 1;
    
    m_shapes.push_back(square);
}

void ShapeNumbersWorkshop::createRectangle() {
    GeometricShape rectangle;
    rectangle.id = 4;
    rectangle.name = "Rectangle";
    rectangle.description = "A shape with four sides and four right angles, opposite sides equal";
    rectangle.sides = 4;
    rectangle.corners = 4;
    rectangle.side_lengths = {2.0, 1.0, 2.0, 1.0};
    rectangle.area = 2.0;  // 2×1
    rectangle.perimeter = 6.0;
    rectangle.child_friendly_properties = "Four sides, opposite sides equal, like a door";
    rectangle.visual_representation = "▭";
    rectangle.difficulty_level = 1;
    
    m_shapes.push_back(rectangle);
}

void ShapeNumbersWorkshop::createPentagon() {
    GeometricShape pentagon;
    pentagon.id = 5;
    pentagon.name = "Pentagon";
    pentagon.description = "A shape with five sides and five corners";
    pentagon.sides = 5;
    pentagon.corners = 5;
    pentagon.side_lengths = {1.0, 1.0, 1.0, 1.0, 1.0};  // Regular
    pentagon.area = 1.72;  // Approximate for regular pentagon
    pentagon.perimeter = 5.0;
    pentagon.child_friendly_properties = "Five sides, five corners, like a house shape";
    pentagon.visual_representation = "⬠";
    pentagon.difficulty_level = 2;
    
    m_shapes.push_back(pentagon);
}

void ShapeNumbersWorkshop::createHexagon() {
    GeometricShape hexagon;
    hexagon.id = 6;
    hexagon.name = "Hexagon";
    hexagon.description = "A shape with six sides and six corners";
    hexagon.sides = 6;
    hexagon.corners = 6;
    hexagon.side_lengths = {1.0, 1.0, 1.0, 1.0, 1.0, 1.0};  // Regular
    hexagon.area = 2.60;  // Approximate for regular hexagon
    hexagon.perimeter = 6.0;
    hexagon.child_friendly_properties = "Six sides, six corners, like honeycomb";
    hexagon.visual_representation = "⬡";
    hexagon.difficulty_level = 2;
    
    m_shapes.push_back(hexagon);
}

void ShapeNumbersWorkshop::createOctagon() {
    GeometricShape octagon;
    octagon.id = 7;
    octagon.name = "Octagon";
    octagon.description = "A shape with eight sides and eight corners";
    octagon.sides = 8;
    octagon.corners = 8;
    octagon.side_lengths = {1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0};  // Regular
    octagon.area = 4.83;  // Approximate for regular octagon
    octagon.perimeter = 8.0;
    octagon.child_friendly_properties = "Eight sides, eight corners, like stop sign";
    octagon.visual_representation = "⯃";
    octagon.difficulty_level = 2;
    
    m_shapes.push_back(octagon);
}

void ShapeNumbersWorkshop::initializeSpatialPuzzles() {
    // Puzzle 1: Shape stacking
    SpatialPuzzle puzzle1;
    puzzle1.id = 1;
    puzzle1.puzzle_name = "Shape Stacking Challenge";
    puzzle1.description = "Which shapes can stack on top of each other?";
    puzzle1.shapes_involved = {"Circle", "Square", "Triangle"};
    puzzle1.challenge_question = "If you stack shapes, which ones make a stable tower?";
    puzzle1.solution = "Squares and rectangles stack well, circles roll, triangles can be tricky";
    puzzle1.reasoning = "Flat, stable shapes stack better than round ones";
    puzzle1.spatial_concept = "Stability and Balance";
    m_puzzles.push_back(puzzle1);
    
    // Puzzle 2: Shape fitting
    SpatialPuzzle puzzle2;
    puzzle2.id = 2;
    puzzle2.puzzle_name = "Shape Fitting Mystery";
    puzzle2.description = "Which shapes fit together without gaps?";
    puzzle2.shapes_involved = {"Square", "Triangle", "Hexagon"};
    puzzle2.challenge_question = "Which shapes can tile a floor completely?";
    puzzle2.solution = "Squares, triangles, and hexagons can tile without gaps";
    puzzle2.reasoning = "These shapes have angles that divide evenly into 360 degrees";
    puzzle2.spatial_concept = "Tessellation";
    m_puzzles.push_back(puzzle2);
}

void ShapeNumbersWorkshop::initializeShapePatterns() {
    // Pattern 1: Shape sequence
    ShapePattern pattern1;
    pattern1.id = 1;
    pattern1.pattern_name = "Growing Shapes";
    pattern1.shape_sequence = {"Triangle", "Square", "Pentagon", "Hexagon"};
    pattern1.pattern_rule = "Each shape has one more side than the previous";
    pattern1.next_shape = "Heptagon (7 sides)";
    pattern1.mathematical_principle = "Arithmetic progression in polygon sides";
    m_patterns.push_back(pattern1);
    
    // Pattern 2: Alternating shapes
    ShapePattern pattern2;
    pattern2.id = 2;
    pattern2.pattern_name = "Circle and Square Dance";
    pattern2.shape_sequence = {"Circle", "Square", "Circle", "Square"};
    pattern2.pattern_rule = "Alternating between circle and square";
    pattern2.next_shape = "Circle";
    pattern2.mathematical_principle = "Alternating pattern";
    m_patterns.push_back(pattern2);
}

void ShapeNumbersWorkshop::initializeTransformations() {
    // Rotation transformation
    Transformation rotation;
    rotation.id = 1;
    rotation.transformation_name = "Shape Rotation";
    rotation.original_shape = "Triangle";
    rotation.transformed_shape = "Triangle (turned)";
    rotation.transformation_type = "Rotation";
    rotation.explanation = "Turning the shape around a central point";
    rotation.real_world_example = "A spinning top or rotating wheel";
    m_transformations.push_back(rotation);
    
    // Reflection transformation
    Transformation reflection;
    reflection.id = 2;
    reflection.transformation_name = "Shape Reflection";
    reflection.original_shape = "Square";
    reflection.transformed_shape = "Square (mirrored)";
    reflection.transformation_type = "Reflection";
    reflection.explanation = "Creating a mirror image of the shape";
    reflection.real_world_example = "Your reflection in a mirror";
    m_transformations.push_back(reflection);
    
    // Scaling transformation
    Transformation scaling;
    scaling.id = 3;
    scaling.transformation_name = "Shape Scaling";
    scaling.original_shape = "Circle";
    scaling.transformed_shape = "Circle (bigger or smaller)";
    scaling.transformation_type = "Scaling";
    scaling.explanation = "Making the shape bigger or smaller";
    scaling.real_world_example = "A growing balloon or shrinking shadow";
    m_transformations.push_back(scaling);
}

void ShapeNumbersWorkshop::initializeShapeKnowledge() {
    m_shapeKnowledge["circle"] = "Round shape with no corners, rolls perfectly";
    m_shapeKnowledge["triangle"] = "Three-sided shape, very stable like a pyramid";
    m_shapeKnowledge["square"] = "Four equal sides, perfect for stacking";
    m_shapeKnowledge["rectangle"] = "Four sides with pairs equal, like doors and windows";
    m_shapeKnowledge["pentagon"] = "Five sides, like the shape of a house";
    m_shapeKnowledge["hexagon"] = "Six sides, like honeycomb in beehives";
    m_shapeKnowledge["octagon"] = "Eight sides, like a stop sign";
}

void ShapeNumbersWorkshop::start() {
    Logger::info("Starting Shape Numbers workshop...");
    
    if (m_guide) {
        m_guide->sayHello();
        m_guide->explainAdventure();
    }
    
    introduceWorkshop();
    
    m_currentShape = 0;
    m_isRunning = true;
    
    ColorfulPrinter::printExcited("Let's explore the magical world of shapes together!");
}

void ShapeNumbersWorkshop::introduceWorkshop() {
    ColorfulPrinter::printStory("Welcome, Shape Explorer! Today we'll discover the world of geometric shapes!");
    
    if (m_mathMagician) {
        m_mathMagician->performMagic();
        ColorfulPrinter::printExcited("Shapes are everywhere - in nature, in buildings, in art, and even in numbers!");
    }
    
    ColorfulPrinter::printHappy("Every shape has special properties and mathematical secrets!");
    ColorfulPrinter::printExcited("We'll learn how shapes relate to each other and build amazing things!");
    
    exploreBasicShapes();
}

void ShapeNumbersWorkshop::exploreBasicShapes() {
    ColorfulPrinter::printLearning("Let's meet the basic shape family!");
    
    ColorfulPrinter::printNumber("Basic Shapes Around Us:");
    ColorfulPrinter::printNumber("• Circles: wheels, clocks, coins, the sun");
    ColorfulPrinter::printNumber("• Triangles: road signs, pizza slices, mountains");
    ColorfulPrinter::printNumber("• Squares: windows, tiles, chess boards");
    ColorfulPrinter::printNumber("• Rectangles: doors, books, screens");
    
    ColorfulPrinter::printExcited("Shapes help us understand and organize our world!");
    
    ColorfulPrinter::printAchievement("You're ready to be a Shape Explorer! 🔷✨");
}

void ShapeNumbersWorkshop::update() {
    if (!m_isRunning) return;
    
    if (m_needsBreak) {
        std::this_thread::sleep_for(std::chrono::minutes(2));
        m_needsBreak = false;
        ColorfulPrinter::printExcited("Welcome back, Shape Explorer!");
    }
    
    if (m_currentShape < m_shapes.size()) {
        exploreShape(m_shapes[m_currentShape]);
        m_currentShape++;
        updateProgress();
        checkForBreak();
    } else if (m_currentShape < m_shapes.size() + m_puzzles.size()) {
        solveSpatialPuzzle(m_puzzles[m_currentShape - m_shapes.size()]);
        m_currentShape++;
        updateProgress();
        checkForBreak();
    } else if (m_currentShape < m_shapes.size() + m_puzzles.size() + m_patterns.size()) {
        discoverShapePattern(m_patterns[m_currentShape - m_shapes.size() - m_puzzles.size()]);
        m_currentShape++;
        updateProgress();
        checkForBreak();
    } else {
        exploreAdvancedShapes();
        if (m_currentShape >= m_shapes.size() + m_puzzles.size() + m_patterns.size() + 5) {
            endWorkshop();
        }
    }
}

void ShapeNumbersWorkshop::exploreShape(const GeometricShape& shape) {
    ColorfulPrinter::printExcited("Shape Discovery: " + shape.name);
    ColorfulPrinter::printLearning(shape.description);
    
    // Display shape
    displayShape(shape);
    
    // Show properties
    ColorfulPrinter::printNumber("Sides: " + std::to_string(shape.sides));
    ColorfulPrinter::printNumber("Corners: " + std::to_string(shape.corners));
    ColorfulPrinter::printHappy("Special Properties: " + shape.child_friendly_properties);
    
    // Mathematical information
    ColorfulPrinter::printMath("Area: " + std::to_string(shape.area));
    ColorfulPrinter::printMath("Perimeter: " + std::to_string(shape.perimeter));
    
    // Interactive exploration
    exploreShapeProperties(shape);
    
    m_shapesExplored++;
    m_discoveredShapes.push_back(shape.name);
    celebrateShapeDiscovery();
}

void ShapeNumbersWorkshop::displayShape(const GeometricShape& shape) {
    ColorfulPrinter::printVisual("Shape Visual: " + shape.visual_representation);
    
    // Create ASCII art representation
    if (shape.name == "Circle") {
        ColorfulPrinter::printVisual("    ⭕    ");
        ColorfulPrinter::printVisual("  ⭕⭕⭕  ");
        ColorfulPrinter::printVisual(" ⭕⭕⭕⭕⭕ ");
        ColorfulPrinter::printVisual("  ⭕⭕⭕  ");
        ColorfulPrinter::printVisual("    ⭕    ");
    } else if (shape.name == "Triangle") {
        ColorfulPrinter::printVisual("    🔺    ");
        ColorfulPrinter::printVisual("   🔺🔺   ");
        ColorfulPrinter::printVisual("  🔺🔺🔺  ");
    } else if (shape.name == "Square") {
        ColorfulPrinter::printVisual(" ⬜⬜⬜ ");
        ColorfulPrinter::printVisual(" ⬜⬜⬜ ");
        ColorablePrinter::printVisual(" ⬜⬜⬜ ");
    }
}

void ShapeNumbersWorkshop::exploreShapeProperties(const GeometricShape& shape) {
    if (shape.name == "Circle") {
        exploreCircle();
    } else if (shape.name == "Triangle") {
        exploreTriangle();
    } else if (shape.name == "Square") {
        exploreSquare();
    } else if (shape.name == "Rectangle") {
        exploreRectangle();
    } else if (shape.name == "Pentagon") {
        explorePentagon();
    } else if (shape.name == "Hexagon") {
        exploreHexagon();
    } else if (shape.name == "Octagon") {
        exploreOctagon();
    }
    
    if (shape.difficulty_level > 1) {
        m_complexShapesUnderstood++;
    }
}

void ShapeNumbersWorkshop::exploreCircle() {
    ColorfulPrinter::printHappy("Circles are perfect and round!");
    ColorfulPrinter::printExample("Wheels roll because they're circles");
    ColorfulPrinter::printExample("Clocks have circular faces");
    ColorfulPrinter::printExample("Planets are approximately circular");
    
    ColorfulPrinter::printExcited("Circles can roll in any direction - that's why they're special!");
}

void ShapeNumbersWorkshop::exploreTriangle() {
    ColorfulPrinter::printHappy("Triangles are super strong and stable!");
    ColorfulPrinter::printExample("Pyramids are made of triangles - they last thousands of years!");
    ColorfulPrinter::printExample("Bridges use triangles for strength");
    ColorfulPrinter::printExample("Roofs are often triangular");
    
    ColorfulPrinter::printExcited("Triangles are the strongest shape in nature!");
}

void ShapeNumbersWorkshop::exploreSquare() {
    ColorablePrinter::printHappy("Squares are perfect for building and organizing!");
    ColorfulPrinter::printExample("Tiles are often square - they fit together perfectly");
    ColorfulPrinter::printExample("Computer screens are measured in square pixels");
    ColorfulPrinter::printExample("Chess boards have square spaces");
    
    ColorfulPrinter::printExcited("Squares can tile a floor without any gaps!");
}

void ShapeNumbersWorkshop::exploreRectangle() {
    ColorfulPrinter::printHappy("Rectangles are everywhere in our daily life!");
    ColorfulPrinter::printExample("Doors and windows are rectangles");
    ColorfulPrinter::printExample("Books and phones are rectangular");
    ColorfulPrinter::printExample("Rooms are usually rectangular");
    
    ColorfulPrinter::printExcited("Rectangles are perfect for organizing space!");
}

void ShapeNumbersWorkshop::explorePentagon() {
    ColorfulPrinter::printHappy("Pentagons have five sides - like a house shape!");
    ColorfulPrinter::printExample("Some houses have pentagonal shapes");
    ColorfulPrinter::printExample("The Pentagon building has five sides");
    ColorfulPrinter::printExample("Some flowers have five petals");
    
    ColorfulPrinter::printExcited("Pentagons appear in nature and architecture!");
}

void ShapeNumbersWorkshop::exploreHexagon() {
    ColorfulPrinter::printHappy("Hexagons are nature's favorite shape!");
    ColorfulPrinter::printExample("Honeycombs are made of hexagons - perfect storage!");
    ColorfulPrinter::printExample("Snowflakes have hexagonal patterns");
    ColorfulPrinter::printExample("Some crystals form hexagons");
    
    ColorfulPrinter::printExcited("Hexagons tile perfectly with minimal material!");
}

void ShapeNumbersWorkshop::exploreOctagon() {
    ColorfulPrinter::printHappy("Octagons help keep us safe!");
    ColorfulPrinter::printExample("Stop signs are octagons - easy to recognize!");
    ColorfulPrinter::printExample("Some tables have octagonal shapes");
    ColorfulPrinter::printExample("Some windows are octagonal");
    
    ColorfulPrinter::printExcited("Octagons are distinctive and attention-grabbing!");
}

void ShapeNumbersWorkshop::solveSpatialPuzzle(const SpatialPuzzle& puzzle) {
    ColorfulPrinter::printExcited("Spatial Puzzle: " + puzzle.puzzle_name);
    ColorfulPrinter::printLearning(puzzle.description);
    
    // Show shapes involved
    ColorfulPrinter::printNumber("Shapes Involved:");
    for (const auto& shape : puzzle.shapes_involved) {
        ColorfulPrinter::printNumber("• " + shape);
    }
    
    ColorfulPrinter::printThinking(puzzle.challenge_question);
    
    ColorfulPrinter::printWithDots("Solving the spatial puzzle");
    
    // Reveal solution
    ColorfulPrinter::printExcited("Solution: " + puzzle.solution);
    ColorfulPrinter::printHappy("Reasoning: " + puzzle.reasoning);
    ColorfulPrinter::printMath("Spatial Concept: " + puzzle.spatial_concept);
    
    m_puzzlesSolved++;
    celebrateShapeDiscovery();
}

void ShapeNumbersWorkshop::discoverShapePattern(const ShapePattern& pattern) {
    ColorfulPrinter::printExcited("Shape Pattern: " + pattern.pattern_name);
    
    // Show the pattern sequence
    std::string sequence = "";
    for (size_t i = 0; i < pattern.shape_sequence.size(); ++i) {
        sequence += pattern.shape_sequence[i];
        if (i < pattern.shape_sequence.size() - 1) sequence += " → ";
    }
    
    ColorfulPrinter::printNumber("Pattern: " + sequence + " → ?");
    
    ColorfulPrinter::printThinking("What's the pattern rule?");
    
    ColorfulPrinter::printWithDots("Discovering the pattern");
    
    // Reveal the pattern
    ColorfulPrinter::printExcited("Pattern Rule: " + pattern.pattern_rule);
    ColorablePrinter->printHappy("Next Shape: " + pattern.next_shape);
    ColorfulPrinter::printMath("Mathematical Principle: " + pattern.mathematical_principle);
    
    m_patternsDiscovered++;
    celebrateShapeDiscovery();
}

void ShapeNumbersWorkshop::exploreAdvancedShapes() {
    int shape_index = m_currentShape - m_shapes.size() - m_puzzles.size() - m_patterns.size();
    
    switch (shape_index) {
        case 0:
            exploreTransformations();
            break;
        case 1:
            exploreSpatialRelationships();
            break;
        case 2:
            exploreAreaAndPerimeter();
            break;
        case 3:
            createShapeArt();
            break;
        case 4:
            measureShapes();
            break;
    }
    
    m_currentShape++;
}

void ShapeNumbersWorkshop::exploreTransformations() {
    ColorfulPrinter::printLearning("Let's explore how shapes can change!");
    
    for (const auto& transformation : m_transformations) {
        animateTransformation(transformation);
    }
    
    ColorfulPrinter::printExcited("Shapes can move, turn, flip, and grow!");
    
    ColorablePrinter->printAchievement("Transformation expert! 🔄✨");
}

void ShapeNumbersWorkshop::animateTransformation(const Transformation& transformation) {
    ColorablePrinter->printNumber("Transformation: " + transformation.transformation_name);
    ColorablePrinter->printNumber("Original: " + transformation.original_shape);
    ColorablePrinter->printNumber("Transformed: " + transformation.transformed_shape);
    ColorablePrinter->printHappy("Type: " + transformation.transformation_type);
    ColorablePrinter->printExample("Real world: " + transformation.real_world_example);
}

void ShapeNumbersWorkshop::exploreSpatialRelationships() {
    ColorablePrinter->printLearning("Let's understand how shapes relate to each other in space!");
    
    ColorablePrinter->printNumber("Spatial Relationships:");
    ColorablePrinter->printNumber("• Above/Below: The triangle is above the square");
    ColorablePrinter->printNumber("• Inside/Outside: The circle is inside the square");
    ColorablePrinter->printNumber("• Next to: The rectangle is next to the circle");
    ColorablePrinter->printNumber("• Between: The triangle is between two squares");
    
    ColorablePrinter->printExcited("Understanding space helps us build and navigate!");
    
    ColorablePrinter->printAchievement("Spatial reasoning master! 🗺️✨");
}

void ShapeNumbersWorkshop::exploreAreaAndPerimeter() {
    ColorablePrinter->printLearning("Let's measure shapes!");
    
    ColorablePrinter->printNumber("Area = how much space inside the shape");
    ColorablePrinter->printNumber("Perimeter = distance around the shape");
    
    ColorablePrinter->printExample("Square with side 2:");
    ColorablePrinter->printMath("Area = 2 × 2 = 4 square units");
    ColorablePrinter->printMath("Perimeter = 2 + 2 + 2 + 2 = 8 units");
    
    ColorablePrinter->printExcited("Measuring helps us understand size and quantity!");
    
    ColorablePrinter->printAchievement("Measurement expert! 📏✨");
}

void ShapeNumbersWorkshop::createShapeArt() {
    ColorablePrinter->printExcited("Let's create art with shapes!");
    
    std::vector<std::string> art_shapes = {"Circle", "Triangle", "Square"};
    createShapeArt(art_shapes);
    
    ColorablePrinter->printHappy("You're a shape artist! Every shape adds beauty!");
    
    ColorablePrinter->printAchievement("Shape artist! 🎨✨");
}

void ShapeNumbersWorkshop::createShapeArt(const std::vector<std::string>& shapes) {
    ColorablePrinter->printVisual("Creating Shape Art:");
    
    for (const auto& shape : shapes) {
        ColorablePrinter->printVisual("Adding " + shape + " to our masterpiece");
    }
    
    ColorablePrinter->printExcited("Beautiful! Shapes make amazing art together!");
    
    m_createdPatterns.push_back("Shape Art " + std::to_string(m_createdPatterns.size() + 1));
}

void ShapeNumbersWorkshop::measureShapes() {
    ColorablePrinter->printLearning("Let's be shape measurers!");
    
    ColorablePrinter->printNumber("Measuring Activity:");
    ColorablePrinter->printNumber("• Find a square book");
    ColorablePrinter->printNumber("• Count the squares on a chess board");
    ColorablePrinter->printNumber("• Measure the perimeter of your table");
    ColorablePrinter->printNumber("• Find circular objects in your room");
    
    ColorablePrinter->printExcited("Measuring helps us understand our world mathematically!");
    
    ColorablePrinter->printAchievement("Shape measurer! 📐✨");
}

void ShapeNumbersWorkshop::celebrateShapeDiscovery() {
    std::vector<std::string> celebrations = {
        "Amazing shape discovery! You understand geometry! 🔷",
        "Wonderful! Shapes are revealing their secrets to you! 🌟",
        "Fantastic! Your spatial brain is working perfectly! 🧠",
        "Incredible! You see patterns in shapes and space! 💫",
        "Brilliant! Geometry is becoming your friend! ✨"
    };
    
    int index = rand() % celebrations.size();
    ColorablePrinter->printExcited(celebrations[index]);
    
    // Progress visualization
    int total_activities = m_shapes.size() + m_puzzles.size() + m_patterns.size() + 5;
    int progress = (m_currentShape * 100) / total_activities;
    ColorablePrinter->printProgress("Shape Discovery Progress: " + std::to_string(progress) + "%");
    
    // Milestone celebrations
    if (m_shapesExplored == 4) {
        ColorablePrinter->printAchievement("🎉 4 Shapes Explored! Shape Expert! 🎉");
    } else if (m_puzzlesSolved == 2) {
        ColorablePrinter->printAchievement("🌟 Puzzles Solved! Spatial Master! 🌟");
    } else if (m_patternsDiscovered == 2) {
        ColorablePrinter->printAchievement("💎 Patterns Found! Pattern Detective! 💎");
    }
}

void ShapeNumbersWorkshop::updateProgress() {
    int total_activities = m_shapes.size() + m_puzzles.size() + m_patterns.size() + 5;
    m_learningProgress = (m_currentShape * 100.0) / total_activities;
    
    if (m_aiHelper) {
        m_aiHelper->analyzeProgress(m_learningProgress);
        m_aiHelper->provideEncouragement();
    }
    
    Logger::info("Shape numbers progress: " + std::to_string(m_learningProgress) + "%");
}

void ShapeNumbersWorkshop::checkForBreak() {
    auto now = std::chrono::steady_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::minutes>(now - m_lastBreakTime);
    
    if (duration.count() >= m_attentionSpanMinutes) {
        m_needsBreak = true;
        suggestBreak();
    }
}

void ShapeNumbersWorkshop::suggestBreak() {
    ColorablePrinter->printGentleWarning("Shape explorers need to rest their amazing eyes and brains!");
    ColorablePrinter->printStory("Let's take a little break! Even the best explorers recharge!");
    ColorablePrinter->printHappy("When we come back, we'll discover more amazing shapes!");
    
    m_needsBreak = true;
    m_lastBreakTime = std::chrono::steady_clock::now();
}

void ShapeNumbersWorkshop::render() {
    ColorablePrinter->printStars(8);
}

void ShapeNumbersWorkshop::handleInput() {
    ColorablePrinter->printHelp("Keep exploring! Every shape you understand makes the world more beautiful!");
}

bool ShapeNumbersWorkshop::isComplete() const {
    return m_currentShape >= m_shapes.size() + m_puzzles.size() + m_patterns.size() + 5;
}

double ShapeNumbersWorkshop::getProgress() const {
    return m_learningProgress;
}

void ShapeNumbersWorkshop::endWorkshop() {
    ColorablePrinter->printAchievement("You've completed the Shape Numbers workshop!");
    ColorablePrinter->printExcited("You're now a Shape Expert! 🔷");
    
    ColorablePrinter->printProgress("Shapes explored: " + std::to_string(m_shapesExplored));
    ColorablePrinter->printProgress("Puzzles solved: " + std::to_string(m_puzzlesSolved));
    ColorablePrinter->printProgress("Patterns discovered: " + std::to_string(m_patternsDiscovered));
    
    if (m_complexShapesUnderstood >= 3) {
        ColorablePrinter->printAchievement("🏆 Geometry Master! You understand complex shapes! 🏆");
    }
    
    m_isRunning = false;
}

void ShapeNumbersWorkshop::cleanup() {
    m_geometryAnalyzer.reset();
    m_spatialReasoning.reset();
    m_shapeCalculator.reset();
    m_guide.reset();
    m_mathMagician.reset();
    m_aiHelper.reset();
    
    Logger::info("ShapeNumbersWorkshop cleanup complete");
}

} // namespace Workshops
} // namespace Recipy