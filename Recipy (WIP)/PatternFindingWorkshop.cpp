/*
 * PatternFindingWorkshop.cpp - Advanced Pattern Detection Made Child-Friendly
 */

#include "workshops/PatternFindingWorkshop.h"
#include "utils/Logger.h"
#include "utils/ColorfulPrinter.h"
#include <iostream>
#include <vector>
#include <random>

namespace Recipy {
namespace Workshops {

PatternFindingWorkshop::PatternFindingWorkshop()
    : m_isRunning(false)
    , m_currentChallenge(0)
    , m_patternsFound(0)
    , m_patternsCreated(0)
    , m_learningProgress(0.0)
    , m_needsBreak(false)
    , m_attentionSpanMinutes(15)
    , m_currentDifficulty(0.1)
    , m_streakCount(0)
    , m_bestStreak(0)
    , m_averageSolveTime(0.0) {
    
    Logger::info("PatternFindingWorkshop constructor - Creating pattern discovery adventure!");
    m_startTime = std::chrono::steady_clock::now();
    m_lastBreakTime = m_startTime;
}

PatternFindingWorkshop::~PatternFindingWorkshop() {
    cleanup();
}

bool PatternFindingWorkshop::initialize() {
    Logger::info("Initializing Pattern Finding workshop...");
    
    try {
        ColorfulPrinter::printRainbow("🔍 Welcome to Pattern Finding Adventures! 🔍");
        ColorfulPrinter::printExcited("Let's become pattern detectives and discover mathematical secrets!");
        
        if (!initializeComponents()) {
            ColorfulPrinter::printSad("The pattern tools couldn't wake up.");
            return false;
        }
        
        initializePatternChallenges();
        
        ColorfulPrinter::printHappy("All pattern detective tools are ready!");
        return true;
    } catch (...) {
        return false;
    }
}

bool PatternFindingWorkshop::initializeComponents() {
    try {
        m_guide = std::make_unique<Characters::FriendlyGuide>();
        m_mathMagician = std::make_unique<Characters::MathMagician>();
        m_aiHelper = std::make_unique<AI::ChildAIHelper>();
        m_patternMatcher = std::make_unique<Math::PatternMatcher>();
        m_sequenceAnalyzer = std::make_unique<Math::SequenceAnalyzer>();
        m_reciprocalDetector = std::make_unique<Math::ReciprocalPatternDetector>();
        
        ColorfulPrinter::printHappy("Pattern detection system is ready!");
        return true;
    } catch (...) {
        return false;
    }
}

void PatternFindingWorkshop::initializePatternChallenges() {
    Logger::info("Creating 400+ pattern detection challenges...");
    
    // Basic arithmetic patterns
    for (int i = 1; i <= 50; ++i) {
        PatternChallenge challenge;
        challenge.id = i;
        challenge.name = "Arithmetic Pattern " + std::to_string(i);
        challenge.description = "Find the next number in the arithmetic sequence";
        challenge.pattern_type = "arithmetic";
        challenge.sequence = generateArithmeticSequence(i);
        challenge.difficulty_level = 1 + (i % 5);
        challenge.solved = false;
        challenge.attempts = 0;
        challenge.time_taken = 0.0;
        m_patternChallenges.push_back(challenge);
    }
    
    // Geometric patterns
    for (int i = 1; i <= 50; ++i) {
        PatternChallenge challenge;
        challenge.id = 50 + i;
        challenge.name = "Geometric Pattern " + std::to_string(i);
        challenge.description = "Discover the multiplication pattern";
        challenge.pattern_type = "geometric";
        challenge.sequence = generateGeometricSequence(i);
        challenge.difficulty_level = 2 + (i % 4);
        challenge.solved = false;
        challenge.attempts = 0;
        challenge.time_taken = 0.0;
        m_patternChallenges.push_back(challenge);
    }
    
    // Fibonacci patterns
    for (int i = 1; i <= 40; ++i) {
        PatternChallenge challenge;
        challenge.id = 100 + i;
        challenge.name = "Fibonacci Pattern " + std::to_string(i);
        challenge.description = "Find the Fibonacci sequence pattern";
        challenge.pattern_type = "fibonacci";
        challenge.sequence = generateFibonacciSequence(i);
        challenge.difficulty_level = 3 + (i % 3);
        challenge.solved = false;
        challenge.attempts = 0;
        challenge.time_taken = 0.0;
        m_patternChallenges.push_back(challenge);
    }
    
    // Reciprocal patterns (from original analyzer)
    for (int i = 1; i <= 60; ++i) {
        PatternChallenge challenge;
        challenge.id = 140 + i;
        challenge.name = "Reciprocal Pattern " + std::to_string(i);
        challenge.description = "Discover beautiful reciprocal patterns";
        challenge.pattern_type = "reciprocal";
        challenge.sequence = generateReciprocalSequence(i);
        challenge.difficulty_level = 2 + (i % 6);
        challenge.solved = false;
        challenge.attempts = 0;
        challenge.time_taken = 0.0;
        m_patternChallenges.push_back(challenge);
    }
    
    // Complex mixed patterns
    for (int i = 1; i <= 200; ++i) {
        PatternChallenge challenge;
        challenge.id = 200 + i;
        challenge.name = "Complex Pattern " + std::to_string(i);
        challenge.description = "Solve advanced pattern mysteries";
        challenge.pattern_type = "complex";
        challenge.sequence = generateComplexPattern(i);
        challenge.difficulty_level = 3 + (i % 7);
        challenge.solved = false;
        challenge.attempts = 0;
        challenge.time_taken = 0.0;
        m_patternChallenges.push_back(challenge);
    }
    
    ColorfulPrinter::printLearning("Created " + std::to_string(m_patternChallenges.size()) + " pattern challenges!");
}

std::vector<int> PatternFindingWorkshop::generateArithmeticSequence(int seed) {
    std::vector<int> sequence;
    std::random_device rd;
    std::mt19937 gen(seed);
    
    int start = gen() % 10 + 1;
    int step = gen() % 5 + 1;
    
    for (int i = 0; i < 5; ++i) {
        sequence.push_back(start + i * step);
    }
    
    return sequence;
}

std::vector<int> PatternFindingWorkshop::generateGeometricSequence(int seed) {
    std::vector<int> sequence;
    std::random_device rd;
    std::mt19937 gen(seed);
    
    int start = gen() % 5 + 1;
    int factor = gen() % 3 + 2;
    
    for (int i = 0; i < 5; ++i) {
        sequence.push_back(start * pow(factor, i));
    }
    
    return sequence;
}

std::vector<int> PatternFindingWorkshop::generateFibonacciSequence(int seed) {
    std::vector<int> sequence;
    std::random_device rd;
    std::mt19937 gen(seed);
    
    int first = gen() % 5 + 1;
    int second = gen() % 5 + 1;
    
    sequence.push_back(first);
    sequence.push_back(second);
    
    for (int i = 2; i < 5; ++i) {
        sequence.push_back(sequence[i-1] + sequence[i-2]);
    }
    
    return sequence;
}

std::vector<int> PatternFindingWorkshop::generateReciprocalSequence(int seed) {
    // Based on the original analyzer's reciprocal patterns
    std::vector<int> sequence;
    std::random_device rd;
    std::mt19937 gen(seed);
    
    int denominator = gen() % 9 + 2;  // 2-10
    int numerator = gen() % denominator + 1;
    
    // Create pattern based on 1/n fractions
    for (int i = 1; i <= 5; ++i) {
        sequence.push_back((numerator * i) % denominator);
    }
    
    return sequence;
}

std::vector<int> PatternFindingWorkshop::generateComplexPattern(int seed) {
    std::vector<int> sequence;
    std::random_device rd;
    std::mt19937 gen(seed);
    
    int pattern_type = gen() % 4;
    
    switch (pattern_type) {
        case 0:  // Mixed arithmetic
            {
                int start = gen() % 10 + 1;
                for (int i = 0; i < 5; ++i) {
                    sequence.push_back(start + i * (gen() % 5 + 1));
                }
            }
            break;
        case 1:  // Alternating patterns
            {
                int base1 = gen() % 5 + 1;
                int base2 = gen() % 5 + 1;
                for (int i = 0; i < 5; ++i) {
                    sequence.push_back(i % 2 == 0 ? base1 : base2);
                }
            }
            break;
        case 2:  // Square patterns
            for (int i = 1; i <= 5; ++i) {
                sequence.push_back(i * i);
            }
            break;
        case 3:  // Prime patterns
            {
                std::vector<int> primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29};
                int start_idx = gen() % 5;
                for (int i = 0; i < 5; ++i) {
                    sequence.push_back(primes[start_idx + i]);
                }
            }
            break;
    }
    
    return sequence;
}

void PatternFindingWorkshop::start() {
    Logger::info("Starting Pattern Finding workshop...");
    
    if (m_guide) {
        m_guide->sayHello();
        m_guide->explainAdventure();
    }
    
    introduceWorkshop();
    
    m_currentChallenge = 0;
    m_isRunning = true;
    
    ColorfulPrinter::printExcited("Let's become amazing pattern detectives together!");
}

void PatternFindingWorkshop::introduceWorkshop() {
    ColorfulPrinter::printStory("Welcome, Pattern Detective! Today we'll solve mathematical mysteries!");
    
    if (m_mathMagician) {
        m_mathMagician->performMagic();
        ColorfulPrinter::printExcited("Patterns are hidden everywhere in numbers, waiting for us to find them!");
    }
    
    ColorfulPrinter::printHappy("Just like detectives find clues, we'll find number patterns!");
    ColorfulPrinter::printExcited("Some patterns repeat, some grow, some dance - all are beautiful!");
    
    exploreBasicPatterns();
}

void PatternFindingWorkshop::exploreBasicPatterns() {
    ColorfulPrinter::printLearning("Let's start with simple, beautiful patterns!");
    
    // Arithmetic pattern example
    ColorfulPrinter::printNumber("Pattern: 2, 4, 6, 8, ?");
    ColorfulPrinter::printThinking("What comes next? Each number grows by 2!");
    ColorfulPrinter::printExcited("Yes! 10! You found the pattern!");
    
    // Geometric pattern example  
    ColorfulPrinter::printNumber("Pattern: 1, 2, 4, 8, ?");
    ColorfulPrinter::printThinking("What's happening? Each number doubles!");
    ColorfulPrinter::printExcited("Correct! 16! Amazing pattern detection!");
    
    ColorfulPrinter::printHappy("You're a natural pattern detective! 🕵️‍♀️");
}

void PatternFindingWorkshop::update() {
    if (!m_isRunning) return;
    
    if (m_needsBreak) {
        std::this_thread::sleep_for(std::chrono::minutes(2));
        m_needsBreak = false;
        ColorfulPrinter::printExcited("Welcome back, Pattern Detective!");
    }
    
    if (m_currentChallenge < m_patternChallenges.size()) {
        solvePatternChallenge();
        m_currentChallenge++;
        updateProgress();
        checkForBreak();
    } else {
        endWorkshop();
    }
}

void PatternFindingWorkshop::solvePatternChallenge() {
    PatternChallenge& challenge = m_patternChallenges[m_currentChallenge];
    
    ColorfulPrinter::printExcited("Pattern Challenge " + std::to_string(challenge.id) + ": " + challenge.name);
    ColorfulPrinter::printLearning(challenge.description);
    
    // Display the pattern
    std::string pattern_str = "";
    for (size_t i = 0; i < challenge.sequence.size(); ++i) {
        pattern_str += std::to_string(challenge.sequence[i]);
        if (i < challenge.sequence.size() - 1) pattern_str += ", ";
    }
    pattern_str += ", ?";
    
    ColorfulPrinter::printNumber(pattern_str);
    
    // Provide hints based on difficulty
    if (challenge.difficulty_level <= 2) {
        ColorfulPrinter::printHelp("Hint: Look how the numbers change from one to the next!");
    } else if (challenge.difficulty_level <= 4) {
        ColorfulPrinter::printHelp("Hint: Try adding, subtracting, or multiplying!");
    } else {
        ColorfulPrinter::printHelp("Hint: This pattern might have a special rule!");
    }
    
    // Simulate child solving the pattern
    bool solved = simulatePatternSolve(challenge);
    challenge.attempts++;
    
    if (solved) {
        challenge.solved = true;
        m_patternsFound++;
        celebratePatternDiscovery();
        
        if (m_streakCount > m_bestStreak) {
            m_bestStreak = m_streakCount;
            ColorfulPrinter::printAchievement("New record! " + std::to_string(m_bestStreak) + " patterns in a row!");
        }
    } else {
        m_streakCount = 0;
        ColorfulPrinter::printGentleWarning("That's okay! Pattern detectives sometimes need to think more!");
        ColorfulPrinter::printHappy("The important thing is that you're trying!");
    }
}

bool PatternFindingWorkshop::simulatePatternSolve(PatternChallenge& challenge) {
    // Simulate solving based on difficulty and child's progress
    double solve_probability = 0.8 - (challenge.difficulty_level * 0.1) + (m_learningProgress * 0.2);
    
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_real_distribution<> dis(0.0, 1.0);
    
    return dis(gen) < solve_probability;
}

void PatternFindingWorkshop::celebratePatternDiscovery() {
    m_streakCount++;
    
    std::vector<std::string> celebrations = {
        "Amazing pattern discovery! You're a brilliant detective! 🕵️‍♀️",
        "Wonderful! You saw what others couldn't see! ✨",
        "Fantastic! Your pattern brain is working perfectly! 🧠",
        "Incredible! You're becoming a pattern master! 🌟",
        "Brilliant! Numbers love showing you their secrets! 💫"
    };
    
    int index = rand() % celebrations.size();
    ColorfulPrinter::printExcited(celebrations[index]);
    
    // Progress visualization
    int progress = (m_currentChallenge * 100) / m_patternChallenges.size();
    ColorfulPrinter::printProgress("Pattern Detective Progress: " + std::to_string(progress) + "%");
    
    // Milestone celebrations
    if (m_patternsFound == 10) {
        ColorfulPrinter::printAchievement("🎉 10 Patterns Found! You're officially a Pattern Detective! 🎉");
    } else if (m_patternsFound == 50) {
        ColorfulPrinter::printAchievement("🌟 50 Patterns! You're a Pattern Expert! 🌟");
    } else if (m_patternsFound == 100) {
        ColorfulPrinter::printAchievement("💎 100 Patterns! Pattern Genius Alert! 💎");
    }
}

void PatternFindingWorkshop::exploreAdvancedPatterns() {
    ColorfulPrinter::printLearning("Let's explore advanced patterns from the original analyzer!");
    
    // Reciprocal patterns
    ColorfulPrinter::printExcited("Reciprocal patterns are like sharing patterns!");
    ColorfulPrinter::printMath("1/2 = 0.5, 1/4 = 0.25, 1/8 = 0.125");
    ColorfulPrinter::printHappy("Each time we share more, the decimal gets smaller!");
    
    // Complex sequences
    ColorfulPrinter::printMath("1, 1, 2, 3, 5, 8, 13... Fibonacci!");
    ColorfulPrinter::printExcited("Each number is the sum of the two before it!");
    
    // Prime patterns
    ColorfulPrinter::printMath("2, 3, 5, 7, 11, 13... Prime numbers!");
    ColorfulPrinter::printHappy("These special numbers can only be divided by 1 and themselves!");
}

void PatternFindingWorkshop::exploreReciprocalPatterns() {
    ColorfulPrinter::printLearning("Let's discover the magic of reciprocal patterns!");
    
    ColorfulPrinter::printStory("In the original analyzer, we study how numbers behave when flipped!");
    ColorfulPrinter::printMath("1/7 = 0.142857142857...");
    ColorfulPrinter::printExcited("The pattern 142857 repeats forever - it's a beautiful dance!");
    
    ColorfulPrinter::printMath("1/3 = 0.333333...");
    ColorfulPrinter::printHappy("The number 3 repeats forever - never ending!");
    
    ColorfulPrinter::printMath("1/11 = 0.09090909...");
    ColorfulPrinter::printExcited("The pattern 09 repeats - it's winking at us!");
    
    ColorfulPrinter::printStory("These patterns help us understand how numbers share and divide!");
}

void PatternFindingWorkshop::createOwnPattern() {
    ColorfulPrinter::printExcited("Now it's your turn to be a Pattern Creator!");
    
    ColorfulPrinter::printHappy("Create your own pattern for other detectives to solve!");
    
    PatternCreation creation;
    creation.id = m_patternCreations.size() + 1;
    creation.creator_name = "Amazing Detective";
    creation.pattern_name = "My Special Pattern";
    creation.pattern = generateArithmeticSequence(rand() % 100 + 1);
    creation.rule_description = "Add 3 each time!";
    creation.complexity_level = 2;
    creation.learning_style = "visual";
    
    m_patternCreations.push_back(creation);
    m_patternsCreated++;
    
    ColorfulPrinter::printAchievement("Pattern Created! You're not just a detective, you're a creator!");
    ColorfulPrinter::printExcited("Your pattern: " + std::to_string(creation.pattern[0]) + ", " + 
                                std::to_string(creation.pattern[1]) + ", " + 
                                std::to_string(creation.pattern[2]) + ", " + 
                                std::to_string(creation.pattern[3]) + ", " + 
                                std::to_string(creation.pattern[4]));
}

void PatternFindingWorkshop::analyzeRealWorldPatterns() {
    ColorfulPrinter::printLearning("Let's find patterns in our world!");
    
    ColorfulPrinter::printStory("Look around! Patterns are everywhere!");
    ColorfulPrinter::printExcited("Days of the week: Monday, Tuesday, Wednesday... (repeating pattern!)");
    ColorfulPrinter::printHappy("Seasons: Spring, Summer, Fall, Winter... (cycle pattern!)");
    ColorfulPrinter::printExcited("Music: Do-Re-Mi-Fa-So-La-Ti-Do... (ascending pattern!)");
    
    ColorfulPrinter::printStory("Mathematics helps us understand the patterns that make our world beautiful!");
}

void PatternFindingWorkshop::discoverPatternFamilies() {
    ColorfulPrinter::printLearning("Patterns have families, just like people!");
    
    ColorfulPrinter::printExcited("Arithmetic Family: All patterns that add or subtract the same amount");
    ColorfulPrinter::printExcited("Geometric Family: All patterns that multiply or divide");
    ColorfulPrinter::printExcited("Fibonacci Family: All patterns where each number is the sum of the two before");
    ColorfulPrinter::printExcited("Reciprocal Family: All patterns about sharing and dividing");
    
    ColorfulPrinter::printHappy("Knowing pattern families helps us recognize them faster!");
}

void PatternFindingWorkshop::updateProgress() {
    m_learningProgress = (m_currentChallenge * 100.0) / m_patternChallenges.size();
    
    if (m_aiHelper) {
        m_aiHelper->analyzeProgress(m_learningProgress);
        m_aiHelper->provideEncouragement();
    }
    
    Logger::info("Pattern finding progress: " + std::to_string(m_learningProgress) + "%");
}

void PatternFindingWorkshop::checkForBreak() {
    auto now = std::chrono::steady_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::minutes>(now - m_lastBreakTime);
    
    if (duration.count() >= m_attentionSpanMinutes) {
        m_needsBreak = true;
        suggestBreak();
    }
}

void PatternFindingWorkshop::suggestBreak() {
    ColorfulPrinter::printGentleWarning("Pattern detectives need to rest their amazing brains!");
    ColorfulPrinter::printStory("Let's take a little break! Even the best detectives recharge!");
    ColorfulPrinter::printHappy("When we come back, we'll solve even more amazing patterns!");
    
    m_needsBreak = true;
    m_lastBreakTime = std::chrono::steady_clock::now();
}

void PatternFindingWorkshop::render() {
    // Visual pattern display would go here in GUI version
    ColorfulPrinter::printStars(5);
}

void PatternFindingWorkshop::handleInput() {
    ColorfulPrinter::printHelp("Keep investigating! Every pattern you find makes you smarter!");
}

bool PatternFindingWorkshop::isComplete() const {
    return m_currentChallenge >= m_patternChallenges.size();
}

double PatternFindingWorkshop::getProgress() const {
    return m_learningProgress;
}

void PatternFindingWorkshop::endWorkshop() {
    ColorfulPrinter::printAchievement("You've completed the Pattern Finding workshop!");
    ColorfulPrinter::printExcited("You're now a certified Pattern Detective! 🕵️‍♀️");
    
    ColorfulPrinter::printProgress("Patterns found: " + std::to_string(m_patternsFound));
    ColorfulPrinter::printProgress("Patterns created: " + std::to_string(m_patternsCreated));
    ColorfulPrinter::printProgress("Best streak: " + std::to_string(m_bestStreak));
    
    if (m_patternsFound >= 300) {
        ColorfulPrinter::printAchievement("🏆 Pattern Master! You've found over 300 patterns! 🏆");
    }
    
    m_isRunning = false;
}

void PatternFindingWorkshop::cleanup() {
    m_patternMatcher.reset();
    m_sequenceAnalyzer.reset();
    m_reciprocalDetector.reset();
    m_guide.reset();
    m_mathMagician.reset();
    m_aiHelper.reset();
    
    Logger::info("PatternFindingWorkshop cleanup complete");
}

} // namespace Workshops
} // namespace Recipy