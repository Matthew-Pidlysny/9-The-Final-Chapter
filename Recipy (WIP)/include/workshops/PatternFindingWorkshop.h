/* 
 * PatternFindingWorkshop.h - Advanced Pattern Recognition for Grade 1
 * 
 * Teaching children to recognize and create mathematical patterns
 * based on the advanced pattern detection from the original analyzer.
 */

#pragma once

#include "../workshops/WorkshopBase.h"
#include "../characters/FriendlyGuide.h"
#include "../characters/MathMagician.h"
#include "../AI/ChildAIHelper.h"
#include "../AI/AdaptiveLearning.h"
#include "../math/PatternMatcher.h"
#include "../math/SequenceAnalyzer.h"
#include "../math/ReciprocalPatternDetector.h"
#include "../psychology/LearningStyleAdapter.h"
#include "../psychology/AttentionManager.h"
#include <memory>
#include <vector>
#include <string>
#include <chrono>

namespace Recipy {
namespace Workshops {

struct PatternChallenge {
    int id;
    std::string name;
    std::string description;
    std::string pattern_type;
    std::vector<int> sequence;
    int difficulty_level;
    std::string hint;
    bool solved;
    int attempts;
    double time_taken;
};

struct PatternCreation {
    int id;
    std::string creator_name;
    std::string pattern_name;
    std::vector<int> pattern;
    std::string rule_description;
    int complexity_level;
    std::string learning_style;
};

class PatternFindingWorkshop : public WorkshopBase {
public:
    PatternFindingWorkshop();
    virtual ~PatternFindingWorkshop();
    
    // WorkshopBase overrides
    bool initialize() override;
    void start() override;
    void update() override;
    void render() override;
    void handleInput() override;
    bool isComplete() const override;
    double getProgress() const override;
    void endWorkshop() override;
    
    // Pattern-specific methods
    void exploreBasicPatterns();
    void exploreAdvancedPatterns();
    void exploreReciprocalPatterns();
    void createOwnPattern();
    void solvePatternChallenge();
    void analyzeRealWorldPatterns();
    void discoverPatternFamilies();
    
private:
    // Core components
    std::unique_ptr<Characters::FriendlyGuide> m_guide;
    std::unique_ptr<Characters::MathMagician> m_mathMagician;
    std::unique_ptr<AI::ChildAIHelper> m_aiHelper;
    std::unique_ptr<AI::AdaptiveLearning> m_adaptiveLearning;
    std::unique_ptr<Math::PatternMatcher> m_patternMatcher;
    std::unique_ptr<Math::SequenceAnalyzer> m_sequenceAnalyzer;
    std::unique_ptr<Math::ReciprocalPatternDetector> m_reciprocalDetector;
    std::unique_ptr<Psychology::LearningStyleAdapter> m_learningAdapter;
    std::unique_ptr<Psychology::AttentionManager> m_attentionManager;
    
    // Workshop state
    bool m_isRunning;
    int m_currentChallenge;
    int m_patternsFound;
    int m_patternsCreated;
    double m_learningProgress;
    std::chrono::steady_clock::time_point m_startTime;
    std::chrono::steady_clock::time_point m_lastBreakTime;
    bool m_needsBreak;
    int m_attentionSpanMinutes;
    double m_currentDifficulty;
    
    // Pattern collections
    std::vector<PatternChallenge> m_patternChallenges;
    std::vector<PatternCreation> m_patternCreations;
    std::vector<std::string> m_patternTypes;
    std::vector<std::string> m_patternFamilies;
    
    // Mastery tracking
    std::map<std::string, bool> m_masteredPatterns;
    int m_streakCount;
    int m_bestStreak;
    double m_averageSolveTime;
    
    // Initialization methods
    bool initializeComponents();
    void initializePatternChallenges();
    void initializePatternTypes();
    void initializePatternFamilies();
    
    // Pattern exploration methods
    void exploreArithmeticPatterns();
    void exploreGeometricPatterns();
    void exploreFibonacciPatterns();
    void explorePrimePatterns();
    void exploreSymmetricPatterns();
    void exploreRecursivePatterns();
    void exploreFractalPatterns();
    void exploreReciprocalSequences();
    
    // Pattern creation methods
    void createArithmeticSequence();
    void createGeometricSequence();
    void createCustomPattern();
    void validatePattern(const std::vector<int>& pattern, const std::string& rule);
    
    // Assessment and celebration
    void assessPatternUnderstanding();
    void celebratePatternDiscovery();
    void updateProgress();
    void checkForBreak();
    void suggestBreak();
    
    // Cleanup
    void cleanup();
};

} // namespace Workshops
} // namespace Recipy