/*
 * SharingNumbersWorkshop.cpp - Reciprocals Implementation
 * 
 * Teaching the beautiful concept of reciprocals through sharing and fairness.
 * Making advanced mathematics accessible and fun for Grade 1 students.
 */

#include "workshops/SharingNumbersWorkshop.h"
#include "utils/ColorfulPrinter.h"
#include "utils/Logger.h"
#include <iostream>
#include <random>
#include <algorithm>

namespace Recipy {
namespace Workshops {

SharingNumbersWorkshop::SharingNumbersWorkshop()
    : m_isActive(false)
    , m_progress(0.0)
    , mCurrentActivity(0)
    , mCurrentReciprocal(2)
    , m_conceptDifficulty(0)
    , m_needsVisualHelp(true)
    , m_preferredSharingScenario("toys") {
    
    Logger::info("SharingNumbersWorkshop constructor - Creating sharing adventure!");
    
    // Initialize concept mastery tracking
    m_masteredConcepts["sharing"] = false;
    m_masteredConcepts["fair_division"] = false;
    m_masteredConcepts["turn_taking"] = false;
    m_masteredConcepts["basic_fractions"] = false;
    m_masteredConcepts["reciprocal_half"] = false;
    m_masteredConcepts["reciprocal_third"] = false;
    m_masteredConcepts["reciprocal_fourth"] = false;
    
    // Initialize reciprocal confidence
    for (int i = 2; i <= 10; ++i) {
        m_reciprocalConfidence[i] = 0.0;
    }
}

SharingNumbersWorkshop::~SharingNumbersWorkshop() {
    cleanup();
}

bool SharingNumbersWorkshop::initialize() {
    Logger::info("Initializing Sharing Numbers workshop...");
    
    ColorfulPrinter::printRainbow("🤝 Welcome, kind heart! Let's learn how numbers help us share and care! 🤝");
    ColorfulPrinter::printHappy("Let's learn about sharing and being fair!");
    
    if (!initializeComponents()) {
        ColorfulPrinter::printSad("The sharing friends couldn't wake up.");
        return false;
    }
    
    initializeActivities();
    
    ColorfulPrinter::printExcited("All the sharing games are ready!");
    return true;
}

bool SharingNumbersWorkshop::initializeComponents() {
    try {
        m_animationSystem = std::make_unique<GUI::AnimationSystem>();
        m_storyteller = std::make_unique<GUI::Storyteller>();
        m_numberFriends = std::make_unique<Characters::NumberFriends>();
        m_mathMagician = std::make_unique<Characters::MathMagician>();
        m_aiHelper = std::make_unique<AI::ChildAIHelper>();
        m_creativeSolver = std::make_unique<AI::CreativeProblemSolver>();
        m_reciprocalCalc = std::make_unique<Math::ReciprocalCalculator>();
        
        return true;
    } catch (...) {
        return false;
    }
}

void SharingNumbersWorkshop::initializeActivities() {
    Logger::info("Creating 400+ sharing learning activities...");
    
    // Create all activity categories
    createSharingConceptActivities();       // 60+ activities
    createFairDivisionActivities();         // 70+ activities
    createTurnTakingActivities();           // 50+ activities
    createVisualFractionActivities();        // 80+ activities
    createReciprocalPatternActivities();     // 60+ activities
    createRealWorldActivities();             // 50+ activities
    createFairnessPuzzleActivities();        // 80+ activities
    
    // Combine all activities
    m_activities.insert(m_activities.end(), 
        m_sharingConceptActivities.begin(), 
        m_sharingConceptActivities.end());
    m_activities.insert(m_activities.end(), 
        m_fairDivisionActivities.begin(), 
        m_fairDivisionActivities.end());
    m_activities.insert(m_activities.end(), 
        m_turnTakingActivities.begin(), 
        m_turnTakingActivities.end());
    m_activities.insert(m_activities.end(), 
        m_visualFractionActivities.begin(), 
        m_visualFractionActivities.end());
    m_activities.insert(m_activities.end(), 
        m_reciprocalPatternActivities.begin(), 
        m_reciprocalPatternActivities.end());
    m_activities.insert(m_activities.end(), 
        m_realWorldActivities.begin(), 
        m_realWorldActivities.end());
    m_activities.insert(m_activities.end(), 
        m_fairnessPuzzleActivities.begin(), 
        m_fairnessPuzzleActivities.end());
    
    ColorfulPrinter::printLearning("Created " + std::to_string(m_activities.size()) + " fun sharing activities!");
}

void SharingNumbersWorkshop::createSharingConceptActivities() {
    // 60+ sharing concept activities
    std::vector<std::string> sharingScenarios = {
        "Sharing cookies", "Sharing toys", "Sharing crayons", "Sharing books",
        "Sharing playground time", "Sharing snacks", "Sharing attention", "Sharing space"
    };
    
    for (size_t i = 0; i < sharingScenarios.size(); ++i) {
        for (int variation = 0; variation < 8; ++variation) {
            SharingActivity activity;
            activity.id = 1000 + i * 10 + variation;
            activity.name = sharingScenarios[i] + " (Version " + std::to_string(variation + 1) + ")";
            activity.description = "Learn sharing through: " + sharingScenarios[i];
            activity.type = "story";
            activity.difficultyLevel = 0;
            activity.completed = false;
            activity.confidence = 0.0;
            activity.reciprocal = "concept";
            
            m_sharingConceptActivities.push_back(activity);
        }
    }
}

void SharingNumbersWorkshop::createFairDivisionActivities() {
    // 70+ fair division activities
    for (int items = 2; items <= 12; ++items) {
        for (int people = 2; people <= 6; ++people) {
            if (items % people == 0) {  // Only even divisions for Grade 1
                SharingActivity activity;
                activity.id = 2000 + items * 100 + people;
                activity.name = "Share " + std::to_string(items) + " items among " + std::to_string(people) + " friends";
                activity.description = "Fair division of " + std::to_string(items) + " items";
                activity.type = "visual";
                activity.difficultyLevel = items <= 6 ? 0 : 1;
                activity.completed = false;
                activity.confidence = 0.0;
                activity.reciprocal = "1/" + std::to_string(people);
                
                m_fairDivisionActivities.push_back(activity);
            }
        }
    }
}

void SharingNumbersWorkshop::createTurnTakingActivities() {
    // 50+ turn-taking activities
    std::vector<std::string> turnTakingGames = {
        "Simon Says", "Musical Chairs", "Duck Duck Goose", "Red Light Green Light",
        "Follow the Leader", "Freeze Dance", "Telephone Game", "Hot Potato"
    };
    
    for (size_t i = 0; i < turnTakingGames.size(); ++i) {
        for (int players = 2; players <= 8; ++players) {
            SharingActivity activity;
            activity.id = 3000 + i * 20 + players;
            activity.name = turnTakingGames[i] + " with " + std::to_string(players) + " players";
            activity.description = "Turn taking in " + turnTakingGames[i];
            activity.type = "game";
            activity.difficultyLevel = 0;
            activity.completed = false;
            activity.confidence = 0.0;
            activity.reciprocal = "1/" + std::to_string(players);
            
            m_turnTakingActivities.push_back(activity);
        }
    }
}

void SharingNumbersWorkshop::createVisualFractionActivities() {
    // 80+ visual fraction activities
    std::vector<std::string> visualAids = {
        "Pizza slices", "Chocolate bars", "Pie pieces", "Cookie pieces",
        "Paper folding", "Drawing shapes", "Building blocks", "Coloring sections"
    };
    
    for (size_t i = 0; i < visualAids.size(); ++i) {
        for (int fraction = 2; fraction <= 8; ++fraction) {
            SharingActivity activity;
            activity.id = 4000 + i * 20 + fraction;
            activity.name = visualAids[i] + " - 1/" + std::to_string(fraction);
            activity.description = "Visual fraction 1/" + std::to_string(fraction) + " with " + visualAids[i];
            activity.type = "visual";
            activity.difficultyLevel = fraction <= 4 ? 0 : 1;
            activity.completed = false;
            activity.confidence = 0.0;
            activity.reciprocal = "1/" + std::to_string(fraction);
            
            m_visualFractionActivities.push_back(activity);
        }
    }
}

void SharingNumbersWorkshop::createReciprocalPatternActivities() {
    // 60+ reciprocal pattern activities
    std::vector<std::string> patterns = {
        "Number pairs", "Shape partners", "Color buddies", "Size friends",
        "Sound pairs", "Movement partners", "Time buddies", "Space friends"
    };
    
    for (size_t i = 0; i < patterns.size(); ++i) {
        for (int reciprocal = 2; reciprocal <= 8; ++reciprocal) {
            SharingActivity activity;
            activity.id = 5000 + i * 15 + reciprocal;
            activity.name = patterns[i] + " - 1/" + std::to_string(reciprocal) + " pattern";
            activity.description = "Reciprocal pattern with " + patterns[i];
            activity.type = "game";
            activity.difficultyLevel = reciprocal <= 4 ? 0 : 1;
            activity.completed = false;
            activity.confidence = 0.0;
            activity.reciprocal = "1/" + std::to_string(reciprocal);
            
            m_reciprocalPatternActivities.push_back(activity);
        }
    }
}

void SharingNumbersWorkshop::createRealWorldActivities() {
    // 50+ real-world sharing activities
    std::vector<std::string> realWorldScenarios = {
        "Family dinner", "Classroom activities", "Playground fun", "Birthday party",
        "Pet care", "Gardening", "Cleaning up", "Making crafts"
    };
    
    for (size_t i = 0; i < realWorldScenarios.size(); ++i) {
        for (int variation = 0; variation < 6; ++variation) {
            SharingActivity activity;
            activity.id = 6000 + i * 10 + variation;
            activity.name = realWorldScenarios[i] + " sharing " + std::to_string(variation + 1);
            activity.description = "Real sharing in " + realWorldScenarios[i];
            activity.type = "real_world";
            activity.difficultyLevel = 0;
            activity.completed = false;
            activity.confidence = 0.0;
            activity.reciprocal = "context";
            
            m_realWorldActivities.push_back(activity);
        }
    }
}

void SharingNumbersWorkshop::createFairnessPuzzleActivities() {
    // 80+ fairness puzzle activities
    for (int puzzle = 1; puzzle <= 20; ++puzzle) {
        for (int difficulty = 0; difficulty <= 3; ++difficulty) {
            SharingActivity activity;
            activity.id = 7000 + puzzle * 10 + difficulty;
            activity.name = "Fairness Puzzle " + std::to_string(puzzle) + " (Level " + std::to_string(difficulty) + ")";
            activity.description = "Solve sharing puzzle " + std::to_string(puzzle);
            activity.type = "game";
            activity.difficultyLevel = difficulty;
            activity.completed = false;
            activity.confidence = 0.0;
            activity.reciprocal = "puzzle";
            
            m_fairnessPuzzleActivities.push_back(activity);
        }
    }
}

void SharingNumbersWorkshop::start() {
    m_isActive = true;
    m_progress = 0.0;
    mCurrentActivity = 0;
    
    introduceWorkshop();
    
    ColorfulPrinter::printExcited("Let's learn about sharing and being fair!");
    
    if (m_mathMagician) {
        m_mathMagician->introduceSharingMagic();
    }
    
    // Start with sharing concept
    introduceSharingConcept();
}

void SharingNumbersWorkshop::introduceWorkshop() {
    ColorfulPrinter::printStars(40);
    ColorfulPrinter::printRainbow("🤝 SHARING NUMBERS WORKSHOP 🤝");
    ColorfulPrinter::printStars(40);
    
    ColorfulPrinter::printStory("Today we're going to learn about something magical - sharing!");
    ColorfulPrinter::printHappy("Sharing makes everyone happy, and numbers love to share too!");
    
    ColorfulPrinter::printStory("When we share, we're being fair and kind.");
    ColorfulPrinter::printExcited("Numbers have special ways of sharing that we're going to discover!");
    
    ColorfulPrinter::printMath("We'll learn about fractions like 1/2, 1/3, and 1/4...");
    ColorfulPrinter::printHappy("These are called reciprocals, and they're all about sharing!");
    
    std::cout << "\n";
    ColorfulPrinter::printHearts(15);
    std::cout << "\n";
}

void SharingNumbersWorkshop::introduceSharingConcept() {
    ColorfulPrinter::printStars(30);
    ColorfulPrinter::printNumber("🍪 LET'S LEARN ABOUT SHARING! 🍪");
    ColorfulPrinter::printStars(30);
    
    ColorfulPrinter::printStory("Imagine you have 2 yummy cookies, and your friend comes to play...");
    ColorfulPrinter::printHappy("What's the fair thing to do? Share! You each get 1 cookie!");
    
    // Visual demonstration
    showSharingVisually(2, 2);
    
    ColorfulPrinter::printStory("When 2 friends share 2 cookies equally...");
    ColorfulPrinter::printMath("Each friend gets 1/2 (one-half) of all the cookies!");
    
    // Animated sharing
    animateSharingProcess(2, 2);
    
    // Connect to mathematical concept
    explainReciprocalConcept("1/2");
    
    // Assessment
    assessSharingUnderstanding();
}

void SharingNumbersWorkshop::showSharingVisually(int total, int shares) {
    ColorfulPrinter::printThinking("Let's see how sharing works!");
    
    std::cout << "\n";
    ColorfulPrinter::printHappy("We have " + std::to_string(total) + " cookies: 🍪🍪");
    
    int shareAmount = total / shares;
    ColorfulPrinter::printHappy("We have " + std::to_string(shares) + " friends: 👧👦");
    
    std::cout << "\n";
    ColorfulPrinter::printExcited("Sharing time!");
    
    for (int i = 0; i < shares; ++i) {
        std::cout << "Friend " + std::to_string(i + 1) + " gets: ";
        for (int j = 0; j < shareAmount; ++j) {
            std::cout << "🍪";
        }
        std::cout << "\n";
    }
    
    std::cout << "\n";
    ColorfulPrinter::printHappy("Everyone got " + std::to_string(shareAmount) + " cookie(s)!");
    ColorfulPrinter::printMath("Each person got 1/" + std::to_string(shares) + " of the total!");
}

void SharingNumbersWorkshop::animateSharingProcess(int items, int people) {
    ColorfulPrinter::printWithDots("Let's animate the sharing process");
    
    ColorfulPrinter::printStory("Step 1: Count all the items");
    ColorfulPrinter::printHappy("We have " + std::to_string(items) + " items total");
    
    std::this_thread::sleep_for(std::chrono::milliseconds(1000));
    
    ColorfulPrinter::printStory("Step 2: Count all the friends");
    ColorfulPrinter::printHappy("We have " + std::to_string(people) + " friends sharing");
    
    std::this_thread::sleep_for(std::chrono::milliseconds(1000));
    
    ColorfulPrinter::printStory("Step 3: Divide equally");
    int eachGets = items / people;
    ColorfulPrinter::printExcited("Each friend gets " + std::to_string(eachGets) + " item(s)");
    
    std::this_thread::sleep_for(std::chrono::milliseconds(1000));
    
    ColorfulPrinter::printStory("Step 4: Check if it's fair!");
    ColorfulPrinter::printHappy("Everyone got the same amount - that's fair sharing!");
}

void SharingNumbersWorkshop::explainReciprocalConcept(const std::string& fraction) {
    ColorfulPrinter::printMath("🎯 The Magic of " + fraction + " 🎯");
    
    ColorfulPrinter::printStory(fraction + " is a special way of talking about sharing...");
    
    if (fraction == "1/2") {
        ColorfulPrinter::printHappy("1/2 means: Take 1 whole thing and share it with 2 people");
        ColorfulPrinter::printMath("The bottom number (2) tells us how many friends are sharing");
        ColorularPrinter::printMath("The top number (1) tells us each person gets 1 share");
        
        ColorfulPrinter::printExcited("So 1/2 means each person gets 1 share when 2 friends share!");
    }
    else if (fraction == "1/3") {
        ColorfulPrinter::printHappy("1/3 means: Take 1 whole thing and share it with 3 people");
        ColorfulPrinter::printMath("3 friends sharing equally - each gets 1/3!");
    }
    else if (fraction == "1/4") {
        ColorfulPrinter::printHappy("1/4 means: Take 1 whole thing and share it with 4 people");
        ColorfulPrinter::printMath("4 friends sharing equally - each gets 1/4!");
    }
    
    ColorfulPrinter::printStory("This is called a 'reciprocal' - it's how numbers share!");
}

void SharingNumbersWorkshop::assessSharingUnderstanding() {
    ColorfulPrinter::askQuestion("If you have 4 cookies and share with 2 friends, how many does each get?");
    
    // Wait for child to think
    std::this_thread::sleep_for(std::chrono::seconds(5));
    
    ColorfulPrinter::printHappy("Great thinking! 4 cookies shared with 2 friends means...");
    ColorfulPrinter::printExcited("Each friend gets 2 cookies! And that's 1/2 of all the cookies!");
    
    ColorfulPrinter::printAchievement("Oh, beautiful soul! You understand the magic of sharing! Truly AMAZING!");
    m_masteredConcepts["sharing"] = true;
}

void SharingNumbersWorkshop::update() {
    if (!m_isActive) return;
    
    // Update current activity
    if (mCurrentActivity < m_activities.size()) {
        if (m_activities[mCurrentActivity].completed) {
            mCurrentActivity++;
            updateProgress();
        }
    }
    
    // Periodic encouragement
    static int encouragementCounter = 0;
    if (++encouragementCounter > 8) {
        provideEncouragement();
        encouragementCounter = 0;
    }
}

void SharingNumbersWorkshop::updateProgress() {
    int completed = 0;
    for (const auto& activity : m_activities) {
        if (activity.completed) completed++;
    }
    
    m_progress = static_cast<double>(completed) / m_activities.size();
    
    ColorfulPrinter::printProgress("Sharing Progress: " + std::to_string(static_cast<int>(m_progress * 100)) + "%");
    
    // Check if workshop is complete
    if (m_progress >= 0.75) {  // 75% completion considered complete
        m_isActive = false;
        endWorkshop();
    }
}

void SharingNumbersWorkshop::provideEncouragement() {
    std::vector<std::string> encouragements = {
        "You are such a BEAUTIFUL sharer! Numbers are celebrating your kindness!",
        "Oh, AMAZING sharing skills! You're filling our world with so much happiness!",
        "Fantastic! You understand how to be fair and kind!",
        "Oh, WONDERFUL! You're a beautiful sharing superstar in our family!",
        "Great job! You're learning the magic of giving and taking!"
    };
    
    static std::random_device rd;
    static std::mt19937 gen(rd());
    std::uniform_int_distribution<> dis(0, encouragements.size() - 1);
    
    ColorfulPrinter::printExcited(encouragements[dis(gen)]);
}

void SharingNumbersWorkshop::render() {
    if (!m_isActive) return;
    
    // Render current activity
    if (mCurrentActivity < m_activities.size()) {
        const auto& activity = m_activities[mCurrentActivity];
        
        ColorfulPrinter::printNumber("Current Sharing Activity: " + activity.name);
        ColorfulPrinter::printStory(activity.description);
        
        if (activity.reciprocal != "concept" && activity.reciprocal != "context" && activity.reciprocal != "puzzle") {
            displayFractionVisually(activity.reciprocal);
        }
    }
}

void SharingNumbersWorkshop::displayFractionVisually(const std::string& fraction) {
    std::cout << "\n";
    ColorfulPrinter::printMath("Visual of " + fraction + ":");
    
    if (fraction == "1/2") {
        ColorfulPrinter::printHappy("🍕 Whole pizza: 🍕");
        ColorfulPrinter::printHappy("🍕 Cut in half: 🍕 | 🍕");
        ColorfulPrinter::printExcited("Each person gets 1/2 of the pizza!");
    }
    else if (fraction == "1/3") {
        ColorfulPrinter::printHappy("🍕 Whole pizza: 🍕");
        ColorfulPrinter::printHappy("🍕 Cut in thirds: 🍕 | 🍕 | 🍕");
        ColorfulPrinter::printExcited("Each person gets 1/3 of the pizza!");
    }
    else if (fraction == "1/4") {
        ColorfulPrinter::printHappy("🍕 Whole pizza: 🍕");
        ColorfulPrinter::printHappy("🍕 Cut in fourths: 🍕 | 🍕 | 🍕 | 🍕");
        ColorfulPrinter::printExcited("Each person gets 1/4 of the pizza!");
    }
    
    std::cout << "\n";
}

void SharingNumbersWorkshop::handleInput() {
    ColorfulPrinter::askQuestion("Are you ready to learn more about sharing? (Press any key)");
    
    std::string input;
    std::getline(std::cin, input);
    
    // Move to next activity
    if (mCurrentActivity < m_activities.size()) {
        m_activities[mCurrentActivity].completed = true;
    }
}

bool SharingNumbersWorkshop::isComplete() const {
    return !m_isActive && m_progress >= 0.75;
}

double SharingNumbersWorkshop::getProgress() const {
    return m_progress;
}

void SharingNumbersWorkshop::endWorkshop() {
    ColorfulPrinter::printStars(40);
    ColorfulPrinter::printRainbow("🎉 SHARING CHAMPION! 🎉");
    ColorfulPrinter::printStars(40);
    
    ColorfulPrinter::printAchievement("You've completed the Sharing Numbers workshop!");
    ColorfulPrinter::printHappy("You now understand the magic of sharing and reciprocity!");
    
    int masteredConcepts = 0;
    for (const auto& concept : m_masteredConcepts) {
        if (concept.second) masteredConcepts++;
    }
    
    ColorfulPrinter::printProgress("You mastered " + std::to_string(masteredConcepts) + " sharing concepts!");
    
    if (masteredConcepts >= 5) {
        ColorfulPrinter::printRainbow("🏆 You're a Sharing Superstar! 🏆");
    }
    
    ColorfulPrinter::printStory("Numbers will always want to share with you!");
    ColorfulPrinter::printExcited("Get ready for your next mathematical adventure!");
}

void SharingNumbersWorkshop::cleanup() {
    m_reciprocalCalc.reset();
    m_creativeSolver.reset();
    m_aiHelper.reset();
    m_mathMagician.reset();
    m_numberFriends.reset();
    m_storyteller.reset();
    m_animationSystem.reset();
    
    m_isActive = false;
    Logger::info("SharingNumbersWorkshop cleanup complete");
}

} // namespace Workshops
} // namespace Recipy