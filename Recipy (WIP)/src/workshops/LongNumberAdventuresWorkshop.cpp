/* 
 * LongNumberAdventuresWorkshop.cpp - Making 1200-decimal analysis child-friendly
 * 
 * Introducing children to the beauty of large numbers and patterns
 * through playful exploration and discovery.
 */

#include "workshops/LongNumberAdventuresWorkshop.h"
#include "utils/Logger.h"
#include "utils/ColorfulPrinter.h"
#include <iostream>
#include <iomanip>
#include <sstream>
#include <vector>
#include <cmath>
#include <random>

namespace Recipy {
namespace Workshops {

LongNumberAdventuresWorkshop::LongNumberAdventuresWorkshop()
    : m_currentActivity(0)
    , m_masteredConcepts{"patterns", "digits", "place_value", "sequences", "beauty"}
    , m_longestSequence(0)
    , m_currentDifficulty(0.1)
    , m_attentionSpanMinutes(15)
    , m_needsBreak(false)
    , m_lastBreakTime(std::chrono::steady_clock::now()) {
    
    Logger::info("LongNumberAdventuresWorkshop constructor - Creating number pattern adventure!");
}

LongNumberAdventuresWorkshop::~LongNumberAdventuresWorkshop() {
    cleanup();
}

bool LongNumberAdventuresWorkshop::initialize() {
    Logger::info("Initializing Long Number Adventures workshop...");
    
    try {
        ColorfulPrinter::printRainbow("🔢 Welcome to Long Number Adventures! 🔢");
        ColorfulPrinter::printExcited("Let's explore magical number patterns and discover amazing sequences!");
        
        if (!initializeComponents()) {
            ColorfulPrinter::printSad("The pattern friends couldn't wake up.");
            return false;
        }
        
        initializeActivities();
        
        ColorfulPrinter::printHappy("All the number pattern games are ready!");
        return true;
    } catch (...) {
        return false;
    }
}

bool LongNumberAdventuresWorkshop::initializeComponents() {
    Logger::info("Setting up pattern discovery components...");
    
    try {
        m_guide = std::make_unique<Characters::FriendlyGuide>();
        m_mathMagician = std::make_unique<Characters::MathMagician>();
        m_aiHelper = std::make_unique<AI::ChildAIHelper>();
        
        // Initialize pattern recognition system
        m_patternSystem = std::make_unique<Math::PatternRecognition>();
        
        // Initialize sequence generators
        m_fibonacciGenerator = std::make_unique<Math::SequenceGenerator>("fibonacci");
        m_primeGenerator = std::make_unique<Math::SequenceGenerator>("primes");
        m_decimalGenerator = std::make_unique<Math::DecimalAnalyzer>();
        
        ColorfulPrinter::printHappy("Pattern discovery tools are ready!");
        return true;
    } catch (...) {
        return false;
    }
}

void LongNumberAdventuresWorkshop::initializeActivities() {
    Logger::info("Creating 400+ long number learning activities...");
    
    // 60+ pattern recognition activities
    createPatternRecognitionActivities();
    
    // 50+ decimal exploration activities
    createDecimalExplorationActivities();
    
    // 50+ sequence discovery activities
    createSequenceDiscoveryActivities();
    
    // 50+ beauty in numbers activities
    createBeautyInNumbersActivities();
    
    // 50+ 1200-decimal analysis activities
    createDecimal1200Activities();
    
    // 40+ real-world patterns activities
    createRealWorldPatternsActivities();
    
    // 50+ pattern creation activities
    createPatternCreationActivities();
    
    // 50+ advanced pattern activities
    createAdvancedPatternActivities();
    
    ColorfulPrinter::printLearning("Created " + std::to_string(m_activities.size()) + " pattern discovery activities!");
}

void LongNumberAdventuresWorkshop::createPatternRecognitionActivities() {
    std::vector<std::string> patternTypes = {
        "repeating digits", "growing sequences", "alternating patterns",
        "symmetric patterns", "mirror patterns", "skip counting",
        "doubling patterns", "halving patterns", "circular patterns"
    };
    
    for (size_t i = 0; i < patternTypes.size(); ++i) {
        for (int variation = 0; variation < 7; ++variation) {
            Activity activity;
            activity.id = m_activities.size() + 1;
            activity.name = patternTypes[i] + " Discovery (Version " + std::to_string(variation + 1) + ")";
            activity.description = "Learn to recognize and understand " + patternTypes[i];
            activity.difficulty = m_currentDifficulty + (variation * 0.1);
            activity.duration = 8 + variation;
            activity.learningStyle = "visual";
            
            m_patternRecognitionActivities.push_back(activity);
            m_activities.push_back(activity);
        }
    }
}

void LongNumberAdventuresWorkshop::createDecimalExplorationActivities() {
    std::vector<std::string> decimalConcepts = {
        "decimal places", "repeating decimals", "terminating decimals",
        "decimal patterns", "decimal families", "decimal comparison",
        "decimal addition", "decimal beauty", "decimal sequences"
    };
    
    for (size_t i = 0; i < decimalConcepts.size(); ++i) {
        for (int variation = 0; variation < 6; ++variation) {
            Activity activity;
            activity.id = m_activities.size() + 1;
            activity.name = "Decimal " + decimalConcepts[i] + " (Version " + std::to_string(variation + 1) + ")";
            activity.description = "Explore the world of decimal " + decimalConcepts[i];
            activity.difficulty = m_currentDifficulty + 0.2 + (variation * 0.1);
            activity.duration = 10 + variation;
            activity.learningStyle = "kinesthetic";
            
            m_decimalExplorationActivities.push_back(activity);
            m_activities.push_back(activity);
        }
    }
}

void LongNumberAdventuresWorkshop::createSequenceDiscoveryActivities() {
    std::vector<std::string> sequenceTypes = {
        "Fibonacci", "prime numbers", "triangular numbers", "square numbers",
        "arithmetic sequences", "geometric sequences", "palindromic numbers",
        "perfect numbers", "friendly numbers"
    };
    
    for (size_t i = 0; i < sequenceTypes.size(); ++i) {
        for (int variation = 0; variation < 6; ++variation) {
            Activity activity;
            activity.id = m_activities.size() + 1;
            activity.name = sequenceTypes[i] + " Adventure (Version " + std::to_string(variation + 1) + ")";
            activity.description = "Discover the magic of " + sequenceTypes[i];
            activity.difficulty = m_currentDifficulty + 0.3 + (variation * 0.1);
            activity.duration = 12 + variation;
            activity.learningStyle = "auditory";
            
            m_sequenceDiscoveryActivities.push_back(activity);
            m_activities.push_back(activity);
        }
    }
}

void LongNumberAdventuresWorkshop::createBeautyInNumbersActivities() {
    std::vector<std::string> beautyConcepts = {
        "golden ratio", "pi patterns", "e patterns", "symmetric numbers",
        "beautiful fractions", "harmonic numbers", "sacred geometry",
        "fractal patterns", "natural patterns"
    };
    
    for (size_t i = 0; i < beautyConcepts.size(); ++i) {
        for (int variation = 0; variation < 6; ++variation) {
            Activity activity;
            activity.id = m_activities.size() + 1;
            activity.name = "Beauty of " + beautyConcepts[i] + " (Version " + std::to_string(variation + 1) + ")";
            activity.description = "Appreciate the beauty in " + beautyConcepts[i];
            activity.difficulty = m_currentDifficulty + 0.4 + (variation * 0.1);
            activity.duration = 15 + variation;
            activity.learningStyle = "visual";
            
            m_beautyInNumbersActivities.push_back(activity);
            m_activities.push_back(activity);
        }
    }
}

void LongNumberAdventuresWorkshop::createDecimal1200Activities() {
    // Special focus on 1200-decimal analysis from the original analyzer
    std::vector<std::string> decimal1200Concepts = {
        "1200-digit precision", "high-precision patterns", "decimal convergence",
        "accuracy in science", "space mathematics", "atomic precision",
        "quantum decimals", "astronomical calculations", "medical precision"
    };
    
    for (size_t i = 0; i < decimal1200Concepts.size(); ++i) {
        for (int variation = 0; variation < 6; ++variation) {
            Activity activity;
            activity.id = m_activities.size() + 1;
            activity.name = "1200-Decimal " + decimal1200Concepts[i] + " (Version " + std::to_string(variation + 1) + ")";
            activity.description = "Explore 1200-decimal analysis in " + decimal1200Concepts[i];
            activity.difficulty = m_currentDifficulty + 0.5 + (variation * 0.1);
            activity.duration = 15 + variation;
            activity.learningStyle = "multimodal";
            
            m_decimal1200Activities.push_back(activity);
            m_activities.push_back(activity);
        }
    }
}

void LongNumberAdventuresWorkshop::createRealWorldPatternsActivities() {
    std::vector<std::string> realWorldScenarios = {
        "nature patterns", "architecture patterns", "music patterns",
        "art patterns", "technology patterns", "weather patterns",
        "growth patterns", "wave patterns", "spiral patterns"
    };
    
    for (size_t i = 0; i < realWorldScenarios.size(); ++i) {
        for (int variation = 0; variation < 5; ++variation) {
            Activity activity;
            activity.id = m_activities.size() + 1;
            activity.name = realWorldScenarios[i] + " Pattern " + std::to_string(variation + 1);
            activity.description = "Discover patterns in " + realWorldScenarios[i];
            activity.difficulty = m_currentDifficulty + 0.3 + (variation * 0.15);
            activity.duration = 12 + (variation * 2);
            activity.learningStyle = "kinesthetic";
            
            m_activities.push_back(activity);
        }
    }
}

void LongNumberAdventuresWorkshop::createPatternCreationActivities() {
    for (int i = 1; i <= 50; ++i) {
        Activity activity;
        activity.id = m_activities.size() + 1;
        activity.name = "Create Your Pattern " + std::to_string(i);
        activity.description = "Design and share your own mathematical pattern";
        activity.difficulty = m_currentDifficulty + (i * 0.02);
        activity.duration = 8 + (i % 5);
        activity.learningStyle = "creative";
        
        m_activities.push_back(activity);
    }
}

void LongNumberAdventuresWorkshop::createAdvancedPatternActivities() {
    for (int i = 1; i <= 50; ++i) {
        Activity activity;
        activity.id = m_activities.size() + 1;
        activity.name = "Advanced Pattern Challenge " + std::to_string(i);
        activity.description = "Tackle complex pattern recognition challenges";
        activity.difficulty = 0.7 + (i * 0.006);
        activity.duration = 15 + (i % 10);
        activity.learningStyle = "analytical";
        
        m_activities.push_back(activity);
    }
}

void LongNumberAdventuresWorkshop::start() {
    Logger::info("Starting Long Number Adventures workshop...");
    
    if (m_guide) {
        m_guide->sayHello();
        m_guide->explainAdventure();
    }
    
    introduceWorkshop();
    
    m_currentActivity = 0;
    m_isRunning = true;
    
    ColorfulPrinter::printExcited("Let's discover amazing number patterns together!");
}

void LongNumberAdventuresWorkshop::introduceWorkshop() {
    ColorfulPrinter::printStory("Today we're going on an adventure with long, beautiful numbers!");
    
    if (m_mathMagician) {
        m_mathMagician->performMagic();
        ColorfulPrinter::printExcited("Numbers have incredible patterns that go on and on!");
    }
    
    ColorfulPrinter::printHappy("These are called long numbers, and they're full of surprises!");
    ColorfulPrinter::printExcited("We'll find patterns that repeat, sequences that grow, and beauty that never ends!");
    
    // Show example of interesting long number pattern
    showPatternExample("Fibonacci", "1, 1, 2, 3, 5, 8, 13, 21, 34...");
    
    ColorfulPrinter::printExcited("Each number is the sum of the two before it! Amazing pattern!");
}

void LongNumberAdventuresWorkshop::showPatternExample(const std::string& name, const std::string& pattern) {
    ColorfulPrinter::printMath(name + " Pattern: " + pattern);
    ColorfulPrinter::printThinking("Can you see the pattern? What comes next?");
    
    // Animated pattern reveal
    ColorfulPrinter::printWithDots("Let's discover the pattern magic");
    for (int i = 0; i < 3; ++i) {
        std::this_thread::sleep_for(std::chrono::milliseconds(500));
        ColorfulPrinter::printHappy("✨");
    }
}

void LongNumberAdventuresWorkshop::exploreFibonacciSequence() {
    ColorfulPrinter::printLearning("Let's explore the magical Fibonacci sequence!");
    
    std::vector<int> fibonacci = {1, 1};
    ColorfulPrinter::printNumber("We start with: 1, 1");
    
    for (int i = 2; i < 10; ++i) {
        int next = fibonacci[i-1] + fibonacci[i-2];
        fibonacci.push_back(next);
        
        ColorfulPrinter::printNumber(std::to_string(fibonacci[i-2]) + " + " + 
                                    std::to_string(fibonacci[i-1]) + " = " + 
                                    std::to_string(next));
    }
    
    ColorfulPrinter::printExcited("Look! We found the pattern: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55!");
    ColorfulPrinter::printHappy("This pattern appears in nature - in flowers, shells, and even galaxies!");
}

void LongNumberAdventuresWorkshop::exploreDecimalPatterns() {
    ColorfulPrinter::printLearning("Let's explore the magical world of decimal patterns!");
    
    // Show 1/7 = 0.142857142857... (repeating 6 digits)
    ColorfulPrinter::printMath("1/7 = 0.142857142857142857...");
    ColorfulPrinter::printExcited("The pattern 142857 repeats forever!");
    
    ColorfulPrinter::printMath("1/3 = 0.333333...");
    ColorfulPrinter::printHappy("The digit 3 repeats forever!");
    
    ColorfulPrinter::printMath("1/11 = 0.09090909...");
    ColorfulPrinter::printExcited("The pattern 09 repeats forever!");
    
    ColorfulPrinter::printStory("Some decimals go on forever with beautiful repeating patterns!");
}

void LongNumberAdventuresWorkshop::explore1200DecimalPrecision() {
    ColorfulPrinter::printLearning("Let's discover why 1200 decimal places are special!");
    
    ColorfulPrinter::printStory("In the original analyzer, we explore numbers with 1200 decimal places!");
    ColorfulPrinter::printExcited("That's like counting to a thousand and two hundred places after the dot!");
    
    // Show example with first few digits of pi to 1200 places
    ColorfulPrinter::printMath("π to 1200 places starts like this:");
    ColorfulPrinter::printMath("3.14159265358979323846264338327950288419716939937510...");
    ColorfulPrinter::printHappy("...and it continues for 1200 beautiful digits!");
    
    ColorfulPrinter::printExcited("Scientists use this for space travel, medical research, and quantum physics!");
    
    // Pattern finding in pi digits
    findPatternsInPi();
}

void LongNumberAdventuresWorkshop::findPatternsInPi() {
    ColorfulPrinter::printThinking("Let's hunt for patterns in the first 100 digits of pi!");
    
    std::string pi_100 = "31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679";
    
    // Look for repeating digits
    for (int i = 0; i < pi_100.length() - 2; ++i) {
        if (pi_100[i] == pi_100[i+1] && pi_100[i+1] == pi_100[i+2]) {
            ColorfulPrinter::printExcited("Found triple " + std::string(3, pi_100[i]) + " at position " + std::to_string(i));
        }
    }
    
    // Look for ascending sequences
    for (int i = 0; i < pi_100.length() - 3; ++i) {
        if (pi_100[i+1] == pi_100[i] + 1 && 
            pi_100[i+2] == pi_100[i] + 2 && 
            pi_100[i+3] == pi_100[i] + 3) {
            ColorfulPrinter::printHappy("Found ascending sequence " + pi_100.substr(i, 4));
        }
    }
}

void LongNumberAdventuresWorkshop::createPatternGame() {
    ColorfulPrinter::printExcited("Let's play the Pattern Detective Game!");
    
    std::random_device rd;
    std::mt19937 gen(rd());
    
    // Generate a pattern sequence
    std::vector<int> sequence;
    int pattern_type = gen() % 4;
    
    switch (pattern_type) {
        case 0: // Arithmetic progression
            {
                int start = gen() % 10 + 1;
                int step = gen() % 5 + 1;
                for (int i = 0; i < 5; ++i) {
                    sequence.push_back(start + i * step);
                }
                ColorfulPrinter::printNumber("Arithmetic pattern: " + std::to_string(start) + ", " + 
                                            std::to_string(start+step) + ", " + 
                                            std::to_string(start+2*step) + ", " + 
                                            std::to_string(start+3*step) + ", ?");
            }
            break;
        case 1: // Geometric progression
            {
                int start = gen() % 5 + 1;
                int factor = gen() % 3 + 2;
                for (int i = 0; i < 5; ++i) {
                    sequence.push_back(start * pow(factor, i));
                }
                ColorfulPrinter::printNumber("Multiplying pattern: " + std::to_string(start) + ", " + 
                                            std::to_string(start*factor) + ", " + 
                                            std::to_string(start*factor*factor) + ", " + 
                                            std::to_string(start*factor*factor*factor) + ", ?");
            }
            break;
        case 2: // Fibonacci-like
            {
                sequence = {gen() % 5 + 1, gen() % 5 + 1};
                for (int i = 2; i < 5; ++i) {
                    sequence.push_back(sequence[i-1] + sequence[i-2]);
                }
                ColorfulPrinter::printNumber("Fibonacci-style: " + std::to_string(sequence[0]) + ", " + 
                                            std::to_string(sequence[1]) + ", " + 
                                            std::to_string(sequence[2]) + ", " + 
                                            std::to_string(sequence[3]) + ", ?");
            }
            break;
        case 3: // Squares
            {
                for (int i = 1; i <= 5; ++i) {
                    sequence.push_back(i * i);
                }
                ColorfulPrinter::printNumber("Square numbers: 1, 4, 9, 16, ?");
            }
            break;
    }
    
    ColorfulPrinter::printThinking("What number comes next? Think about the pattern!");
    ColorfulPrinter::printHappy("The answer is " + std::to_string(sequence.back()) + "!");
    
    if (sequence.size() > m_longestSequence) {
        m_longestSequence = sequence.size();
        ColorfulPrinter::printAchievement("New record! You understood a sequence of " + std::to_string(m_longestSequence) + " numbers!");
    }
}

void LongNumberAdventuresWorkshop::runCurrentActivity() {
    if (m_currentActivity >= m_activities.size()) {
        endWorkshop();
        return;
    }
    
    Activity& activity = m_activities[m_currentActivity];
    
    ColorfulPrinter::printExcited("Activity " + std::to_string(m_currentActivity + 1) + ": " + activity.name);
    ColorfulPrinter::printLearning(activity.description);
    
    // Choose activity type based on what's available
    if (m_currentActivity % 8 == 0) {
        exploreFibonacciSequence();
    } else if (m_currentActivity % 8 == 1) {
        exploreDecimalPatterns();
    } else if (m_currentActivity % 8 == 2) {
        explore1200DecimalPrecision();
    } else if (m_currentActivity % 8 == 3) {
        createPatternGame();
    } else if (m_currentActivity % 8 == 4) {
        explorePrimePatterns();
    } else if (m_currentActivity % 8 == 5) {
        exploreSymmetricPatterns();
    } else if (m_currentActivity % 8 == 6) {
        exploreFractionPatterns();
    } else {
        exploreNaturalPatterns();
    }
    
    assessPatternUnderstanding(activity);
    celebrateProgress();
    
    m_currentActivity++;
    
    // Check if break is needed
    checkForBreak();
}

void LongNumberAdventuresWorkshop::explorePrimePatterns() {
    ColorfulPrinter::printLearning("Let's discover prime number patterns!");
    
    std::vector<int> primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29};
    ColorfulPrinter::printNumber("Prime numbers: " + std::to_string(primes[0]));
    
    for (size_t i = 1; i < primes.size(); ++i) {
        ColorfulPrinter::printNumber(std::to_string(primes[i]));
    }
    
    ColorfulPrinter::printExcited("Prime numbers are like special treasures - they can only be divided by 1 and themselves!");
    ColorfulPrinter::printHappy("They appear in unpredictable but beautiful patterns!");
}

void LongNumberAdventuresWorkshop::exploreSymmetricPatterns() {
    ColorfulPrinter::printLearning("Let's explore symmetric number patterns!");
    
    std::vector<std::string> palindromes = {"121", "1331", "12321", "1221", "3443"};
    
    for (const auto& palindrome : palindromes) {
        ColorfulPrinter::printNumber("Palindrome: " + palindrome);
        ColorfulPrinter::printHappy("Read it backwards: " + std::string(palindrome.rbegin(), palindrome.rend()) + " - Same! ✨");
    }
    
    ColorfulPrinter::printExcited("Palindromes are symmetric - they're the same forwards and backwards!");
}

void LongNumberAdventuresWorkshop::exploreFractionPatterns() {
    ColorfulPrinter::printLearning("Let's discover beautiful fraction patterns!");
    
    ColorfulPrinter::printMath("1/2 = 0.5");
    ColorfulPrinter::printMath("1/4 = 0.25");
    ColorfulPrinter::printMath("1/8 = 0.125");
    
    ColorfulPrinter::printExcited("Do you see the pattern? Each time we double the denominator, the decimal gets longer!");
    
    ColorfulPrinter::printMath("1/3 = 0.333...");
    ColorfulPrinter::printMath("2/3 = 0.666...");
    ColorfulPrinter::printHappy("Beautiful repeating patterns!");
}

void LongNumberAdventuresWorkshop::exploreNaturalPatterns() {
    ColorfulPrinter::printLearning("Let's find patterns in nature!");
    
    ColorfulPrinter::printStory("Sunflower seeds grow in spiral patterns following Fibonacci numbers!");
    ColorfulPrinter::printStory("Nautilus shells grow in perfect logarithmic spirals!");
    ColorfulPrinter::printStory("Snowflakes have 6-fold symmetry - each one unique but follows the same pattern!");
    
    ColorfulPrinter::printExcited("Mathematics is the language of nature! 🌻🐚❄️");
}

void LongNumberAdventuresWorkshop::assessPatternUnderstanding(Activity& activity) {
    ColorfulPrinter::printThinking("Let's see what patterns you discovered!");
    
    // Simple assessment based on activity complexity
    if (activity.difficulty < 0.3) {
        ColorfulPrinter::printHappy("Wonderful pattern spotting! You're a natural pattern detective!");
    } else if (activity.difficulty < 0.6) {
        ColorfulPrinter::printExcited("Amazing! You understood a complex pattern! You're brilliant!");
    } else {
        ColorfulPrinter::printAchievement("Incredible! You mastered an advanced pattern concept!");
    }
}

void LongNumberAdventuresWorkshop::celebrateProgress() {
    std::vector<std::string> celebrations = {
        "Amazing pattern discovery! Numbers are celebrating with you!",
        "Wonderful! You're becoming a true pattern expert!",
        "Brilliant work! Your mathematical intuition is growing!",
        "Fantastic! You're seeing beauty in numbers!",
        "Incredible! You understand complex mathematical ideas!"
    };
    
    int index = rand() % celebrations.size();
    ColorfulPrinter::printExcited(celebrations[index]);
    
    // Progress visualization
    int progress = (m_currentActivity * 100) / m_activities.size();
    ColorfulPrinter::printProgress("Pattern Adventure Progress: " + std::to_string(progress) + "%");
    
    // Show pattern milestone
    if (m_currentActivity == 50) {
        ColorfulPrinter::printAchievement("🎉 50 Patterns Discovered! You're on fire! 🎉");
    } else if (m_currentActivity == 100) {
        ColorfulPrinter::printAchievement("🌟 100 Patterns! You're a Pattern Master! 🌟");
    } else if (m_currentActivity == 200) {
        ColorfulPrinter::printAchievement("💎 200 Patterns! Mathematical Genius Alert! 💎");
    }
}

void LongNumberAdventuresWorkshop::checkForBreak() {
    auto now = std::chrono::steady_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::minutes>(now - m_lastBreakTime);
    
    if (duration.count() >= m_attentionSpanMinutes) {
        m_needsBreak = true;
        suggestBreak();
    }
}

void LongNumberAdventuresWorkshop::suggestBreak() {
    ColorfulPrinter::printGentleWarning("Pattern detectives need rest too!");
    ColorfulPrinter::printStory("Let's take a little break! Even pattern explorers need to recharge!");
    ColorfulPrinter::printHappy("When we come back, we'll discover even more amazing patterns!");
    
    m_needsBreak = true;
    m_lastBreakTime = std::chrono::steady_clock::now();
}

void LongNumberAdventuresWorkshop::update() {
    if (!m_isRunning) return;
    
    if (m_needsBreak) {
        // Wait for child to take a break
        std::this_thread::sleep_for(std::chrono::minutes(2));
        
        m_needsBreak = false;
        ColorfulPrinter::printExcited("Welcome back! Let's continue our pattern adventure!");
    }
    
    runCurrentActivity();
    updateProgress();
}

void LongNumberAdventuresWorkshop::updateProgress() {
    m_learningProgress = (m_currentActivity * 100.0) / m_activities.size();
    
    if (m_aiHelper) {
        m_aiHelper->analyzeProgress(m_learningProgress);
        m_aiHelper->provideEncouragement();
    }
    
    Logger::info("Pattern learning progress: " + std::to_string(m_learningProgress) + "%");
}

void LongNumberAdventuresWorkshop::render() {
    // Visual pattern display would go here in GUI version
    ColorfulPrinter::printStars(3);
}

void LongNumberAdventuresWorkshop::handleInput() {
    // Handle child's input with patience and encouragement
    ColorfulPrinter::printHelp("Keep exploring! Every pattern you find is special!");
}

bool LongNumberAdventuresWorkshop::isComplete() const {
    return m_currentActivity >= m_activities.size();
}

double LongNumberAdventuresWorkshop::getProgress() const {
    return m_learningProgress;
}

void LongNumberAdventuresWorkshop::endWorkshop() {
    ColorfulPrinter::printAchievement("You've completed the Long Number Adventures workshop!");
    ColorfulPrinter::printExcited("You discovered amazing patterns in numbers!");
    
    int masteredConcepts = 0;
    for (const auto& concept : m_masteredConcepts) {
        if (concept.second) masteredConcepts++;
    }
    
    ColorfulPrinter::printProgress("You mastered " + std::to_string(masteredConcepts) + " pattern concepts!");
    
    if (m_longestSequence > 0) {
        ColorfulPrinter::printExcited("Longest sequence understood: " + std::to_string(m_longestSequence) + " numbers!");
    }
    
    m_isRunning = false;
}

void LongNumberAdventuresWorkshop::cleanup() {
    m_patternSystem.reset();
    m_fibonacciGenerator.reset();
    m_primeGenerator.reset();
    m_decimalGenerator.reset();
    m_guide.reset();
    m_mathMagician.reset();
    m_aiHelper.reset();
    
    Logger::info("LongNumberAdventuresWorkshop cleanup complete");
}

} // namespace Workshops
} // namespace Recipy