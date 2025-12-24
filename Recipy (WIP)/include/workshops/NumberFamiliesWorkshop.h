/* 
 * NumberFamiliesWorkshop.h - Number Relationships and Families for Grade 1
 * 
 * Teaching children about number families, relationships, and connections
 * based on advanced number theory from the original analyzer.
 */

#pragma once

#include "../workshops/WorkshopBase.h"
#include "../characters/FriendlyGuide.h"
#include "../characters/MathMagician.h"
#include "../AI/ChildAIHelper.h"
#include "../math/NumberTheory.h"
#include "../math/DivisibilityAnalyzer.h"
#include "../math/GreatestCommonDivisor.h"
#include "../math/LeastCommonMultiple.h"
#include "../psychology/LearningStyleAdapter.h"
#include <memory>
#include <vector>
#include <string>
#include <map>
#include <chrono>

namespace Recipy {
namespace Workshops {

struct NumberFamily {
    int id;
    std::string name;
    std::string description;
    std::vector<int> members;
    std::string relationship_rule;
    std::string visual_representation;
    int difficulty_level;
};

struct NumberRelationship {
    int number1;
    int number2;
    std::string relationship_type;
    std::string explanation;
    bool mutual;
    int strength;
};

struct FamilyTree {
    int root_number;
    std::vector<int> children;
    std::vector<int> parents;
    std::vector<int> siblings;
    std::string family_name;
};

class NumberFamiliesWorkshop : public WorkshopBase {
public:
    NumberFamiliesWorkshop();
    virtual ~NumberFamiliesWorkshop();
    
    // WorkshopBase overrides
    bool initialize() override;
    void start() override;
    void update() override;
    void render() override;
    void handleInput() override;
    bool isComplete() const override;
    double getProgress() const override;
    void endWorkshop() override;
    
    // Number family exploration methods
    void exploreBasicFamilies();
    void exploreDivisibilityFamilies();
    void exploreMultipleFamilies();
    void explorePrimeFamilies();
    void explorePerfectFamilies();
    void exploreFriendlyFamilies();
    void createFamilyTree();
    void discoverHiddenRelationships();
    
private:
    // Core components
    std::unique_ptr<Characters::FriendlyGuide> m_guide;
    std::unique_ptr<Characters::MathMagician> m_aiHelper;
    std::unique_ptr<Math::NumberTheory> m_numberTheory;
    std::unique_ptr<Math::DivisibilityAnalyzer> m_divisibilityAnalyzer;
    std::unique_ptr<Math::GreatestCommonDivisor> m_gcdCalculator;
    std::unique_ptr<Math::LeastCommonMultiple> m_lcmCalculator;
    std::unique_ptr<Psychology::LearningStyleAdapter> m_learningAdapter;
    
    // Workshop state
    bool m_isRunning;
    int m_currentFamily;
    int m_familiesDiscovered;
    int m_relationshipsFound;
    double m_learningProgress;
    std::chrono::steady_clock::time_point m_startTime;
    std::chrono::steady_clock::time_point m_lastBreakTime;
    bool m_needsBreak;
    int m_attentionSpanMinutes;
    double m_currentDifficulty;
    
    // Number family collections
    std::vector<NumberFamily> m_numberFamilies;
    std::vector<NumberRelationship> m_relationships;
    std::vector<FamilyTree> m_familyTrees;
    std::map<int, std::vector<int>> m_divisibilityMap;
    std::map<int, std::vector<int>> m_multipleMap;
    std::map<int, std::vector<int>> m_friendshipMap;
    
    // Mastery tracking
    std::map<std::string, bool> m_masteredFamilies;
    int m_largestFamilyFound;
    int m_mostConnectedNumber;
    std::vector<int> m_discoveredNumbers;
    
    // Initialization methods
    bool initializeComponents();
    void initializeNumberFamilies();
    void initializeDivisibilityRelationships();
    void initializeMultiplesRelationships();
    void initializePrimeFamilies();
    void initializePerfectFamilies();
    void initializeFriendlyFamilies();
    
    // Family exploration methods
    void exploreEvenFamily();
    void exploreOddFamily();
    void exploreDivisibleBy3Family();
    void exploreDivisibleBy5Family();
    void exploreSquareFamily();
    void exploreCubeFamily();
    void exploreTriangularFamily();
    void exploreFibonacciFamily();
    
    // Advanced relationship methods
    void findGCDRelationships();
    void findLCMRelationships();
    void findFactorRelationships();
    void findAmicableNumbers();
    void findSociableNumbers();
    
    // Visualization and interaction methods
    void displayFamilyTree(const FamilyTree& tree);
    void displayNumberRelationship(const NumberRelationship& rel);
    void createFamilyVisualization(int number);
    void showFamilyConnections(int number);
    
    // Assessment methods
    void assessFamilyUnderstanding();
    void celebrateFamilyDiscovery();
    void updateProgress();
    void checkForBreak();
    void suggestBreak();
    
    // Utility methods
    std::vector<int> getDivisors(int number);
    std::vector<int> getMultiples(int number, int count);
    bool isPrime(int number);
    bool isPerfect(int number);
    int sumOfProperDivisors(int number);
    std::string getFamilyDescription(const std::string& family_name);
    
    // Cleanup
    void cleanup();
};

} // namespace Workshops
} // namespace Recipy