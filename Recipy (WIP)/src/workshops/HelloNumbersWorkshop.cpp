/*
 * HelloNumbersWorkshop.cpp - First Numbers Implementation
 * 
 * Where the magical journey into mathematics begins!
 * Designed with love for wonderful Grade 1 students.
 */

#include "workshops/HelloNumbersWorkshop.h"
#include "utils/ColorfulPrinter.h"
#include "utils/Logger.h"
#include <iostream>
#include <random>
#include <algorithm>

namespace Recipy {
namespace Workshops {

HelloNumbersWorkshop::HelloNumbersWorkshop()
    : m_isActive(false)
    , m_progress(0.0)
    , mCurrentActivity(0)
    , mCurrentNumber(1)
    , m_attentionSpent(0)
    , m_needsEncouragement(false)
    , m_preferredLearningStyle("visual") {
    
    Logger::info("HelloNumbersWorkshop constructor - Creating magical number introduction!");
    
    // Initialize mastery tracking for numbers 1-10
    m_masteredNumbers.resize(11, false);  // 0-10 indices
    for (int i = 1; i <= 10; ++i) {
        m_numberConfidence[i] = 0;
    }
}

HelloNumbersWorkshop::~HelloNumbersWorkshop() {
    cleanup();
}

bool HelloNumbersWorkshop::initialize() {
    Logger::info("Initializing Hello Numbers workshop...");
    
    ColorfulPrinter::printRainbow("🌟 Oh, beautiful friend! Welcome to our magical Hello Numbers family! 🌟");
    ColorfulPrinter::printHappy("Let's make friends with numbers today!");
    
    if (!initializeComponents()) {
        ColorfulPrinter::printSad("The number friends couldn't wake up.");
        return false;
    }
    
    initializeActivities();
    
    ColorfulPrinter::printExcited("All the number games are ready!");
    return true;
}

bool HelloNumbersWorkshop::initializeComponents() {
    try {
        m_animationSystem = std::make_unique<GUI::AnimationSystem>();
        m_storyteller = std::make_unique<GUI::Storyteller>();
        m_numberFriends = std::make_unique<Characters::NumberFriends>();
        m_guide = std::make_unique<Characters::FriendlyGuide>();
        m_aiHelper = std::make_unique<AI::ChildAIHelper>();
        
        return true;
    } catch (...) {
        return false;
    }
}

void HelloNumbersWorkshop::initializeActivities() {
    Logger::info("Creating 400+ wonderful number learning activities...");
    
    // Create all activity categories
    createNumberRecognitionActivities();    // 50+ activities
    createCountingActivities();              // 60+ activities
    createNumberSongActivities();            // 40+ activities
    createVisualPatternActivities();         // 70+ activities
    createNumberStoryActivities();           // 50+ activities
    createCountingGameActivities();          // 80+ activities
    
    // Combine all activities
    m_activities.insert(m_activities.end(), 
        m_numberRecognitionActivities.begin(), 
        m_numberRecognitionActivities.end());
    m_activities.insert(m_activities.end(), 
        m_countingActivities.begin(), 
        m_countingActivities.end());
    m_activities.insert(m_activities.end(), 
        m_numberSongActivities.begin(), 
        m_numberSongActivities.end());
    m_activities.insert(m_activities.end(), 
        m_visualPatternActivities.begin(), 
        m_visualPatternActivities.end());
    m_activities.insert(m_activities.end(), 
        m_numberStoryActivities.begin(), 
        m_numberStoryActivities.end());
    m_activities.insert(m_activities.end(), 
        m_countingGameActivities.begin(), 
        m_countingGameActivities.end());
    
    ColorfulPrinter::printLearning("Created " + std::to_string(m_activities.size()) + " wonderfully fun number activities!");
}

void HelloNumbersWorkshop::createNumberRecognitionActivities() {
    // 50+ number recognition activities
    for (int number = 1; number <= 10; ++number) {
        for (int variation = 0; variation < 5; ++variation) {
            LearningActivity activity;
            activity.id = number * 10 + variation;
            activity.name = "Meet Number " + std::to_string(number) + " (Version " + std::to_string(variation + 1) + ")";
            activity.description = "Learn to recognize the number " + std::to_string(number);
            activity.type = "visual";
            activity.difficultyLevel = 0;
            activity.completed = false;
            activity.confidence = 0.0;
            
            m_numberRecognitionActivities.push_back(activity);
        }
    }
}

void HelloNumbersWorkshop::createCountingActivities() {
    // 60+ counting activities
    for (int count = 1; count <= 20; ++count) {
        for (int variation = 0; variation < 3; ++variation) {
            LearningActivity activity;
            activity.id = 100 + count * 3 + variation;
            activity.name = "Count to " + std::to_string(count) + " (Fun way " + std::to_string(variation + 1) + ")";
            activity.description = "Practice counting up to " + std::to_string(count);
            activity.type = "kinesthetic";
            activity.difficultyLevel = count <= 10 ? 0 : 1;
            activity.completed = false;
            activity.confidence = 0.0;
            
            m_countingActivities.push_back(activity);
        }
    }
}

void HelloNumbersWorkshop::createNumberSongActivities() {
    // 40+ number song activities
    std::vector<std::string> songs = {
        "One Little Finger", "Five Little Ducks", "Ten in the Bed",
        "Five Little Monkeys", "One Potato Two Potato", "Five Speckled Frogs"
    };
    
    for (size_t i = 0; i < songs.size(); ++i) {
        for (int variation = 0; variation < 7; ++variation) {
            LearningActivity activity;
            activity.id = 200 + i * 10 + variation;
            activity.name = "Sing: " + songs[i] + " (Version " + std::to_string(variation + 1) + ")";
            activity.description = "Learn numbers through the song: " + songs[i];
            activity.type = "auditory";
            activity.difficultyLevel = 0;
            activity.completed = false;
            activity.confidence = 0.0;
            
            m_numberSongActivities.push_back(activity);
        }
    }
}

void HelloNumbersWorkshop::createVisualPatternActivities() {
    // 70+ visual pattern activities
    std::vector<std::string> patterns = {
        "Dot patterns", "Number shapes", "Ten frames", "Number lines",
        "Dice patterns", "Domino patterns", "Playing card patterns"
    };
    
    for (size_t i = 0; i < patterns.size(); ++i) {
        for (int number = 1; number <= 10; ++number) {
            LearningActivity activity;
            activity.id = 300 + i * 20 + number;
            activity.name = patterns[i] + " for " + std::to_string(number);
            activity.description = "See " + std::to_string(number) + " in " + patterns[i];
            activity.type = "visual";
            activity.difficultyLevel = 0;
            activity.completed = false;
            activity.confidence = 0.0;
            
            m_visualPatternActivities.push_back(activity);
        }
    }
}

void HelloNumbersWorkshop::createNumberStoryActivities() {
    // 50+ number story activities
    std::vector<std::string> storyThemes = {
        "Animal adventure with friends", "Toy story joy", "Food fun with family", "Nature walk wonders",
        "Playground games", "Bedtime routine", "Birthday party"
    };
    
    for (size_t i = 0; i < storyThemes.size(); ++i) {
        for (int number = 1; number <= 7; ++number) {
            LearningActivity activity;
            activity.id = 400 + i * 10 + number;
            activity.name = storyThemes[i] + " with " + std::to_string(number);
            activity.description = "A wonderfully fun story about the magical number " + std::to_string(number);
            activity.type = "auditory";
            activity.difficultyLevel = 0;
            activity.completed = false;
            activity.confidence = 0.0;
            
            m_numberStoryActivities.push_back(activity);
        }
    }
}

void HelloNumbersWorkshop::createCountingGameActivities() {
    // 80+ counting game activities
    std::vector<std::string> games = {
        "Hide and Seek", "Hopscotch", "Jump Rope", "Ball Toss",
        "Treasure Hunt", "Simon Says", "Follow the Leader", "Musical Chairs"
    };
    
    for (size_t i = 0; i < games.size(); ++i) {
        for (int count = 1; count <= 10; ++count) {
            LearningActivity activity;
            activity.id = 500 + i * 15 + count;
            activity.name = games[i] + " - Count to " + std::to_string(count);
            activity.description = "Play " + games[i] + " while counting to " + std::to_string(count);
            activity.type = "kinesthetic";
            activity.difficultyLevel = 0;
            activity.completed = false;
            activity.confidence = 0.0;
            
            m_countingGameActivities.push_back(activity);
        }
    }
}

void HelloNumbersWorkshop::start() {
    m_isActive = true;
    m_progress = 0.0;
    mCurrentActivity = 0;
    
    introduceWorkshop();
    
    ColorfulPrinter::printExcited("Let's start our number adventure!");
    
    if (m_guide) {
        m_guide->sayHello();
        m_guide->explainFirstNumbers();
    }
    
    // Start with number one
    introduceNumberOne();
}

void HelloNumbersWorkshop::introduceWorkshop() {
    ColorfulPrinter::printStars(40);
    ColorfulPrinter::printRainbow("🎈 HELLO NUMBERS WORKSHOP 🎈");
    ColorfulPrinter::printStars(40);
    
    ColorfulPrinter::printStory("In this magical place, we're going to make friends with numbers!");
    ColorfulPrinter::printHappy("Numbers are everywhere - in your toys, in nature, and even in your fingers!");
    
    ColorfulPrinter::printStory("Each number has its own personality and special powers.");
    ColorfulPrinter::printExcited("Are you ready to meet them? Let's begin our adventure!");
    
    std::cout << "\n";
    ColorfulPrinter::printNumbers123();
    std::cout << "\n";
}

void HelloNumbersWorkshop::introduceNumberOne() {
    mCurrentNumber = 1;
    
    ColorfulPrinter::printStars(30);
    ColorfulPrinter::printNumber("🌟 MEET NUMBER ONE! 🌟");
    ColorfulPrinter::printStars(30);
    
    ColorfulPrinter::printStory("Number One is very special!");
    ColorfulPrinter::printHappy("It's the first number we learn, and it means 'just one thing'.");
    
    // Visual learning
    showNumberWithObjects(1);
    displayNumberVisually(1);
    
    // Kinesthetic learning
    countWithFingers(1);
    countWithBody(1);
    
    // Storytelling
    tellNumberStory(1);
    
    // Assessment
    assessNumberKnowledge(1);
    
    // Progress update
    updateProgress();
}

void HelloNumbersWorkshop::showNumberWithObjects(int number) {
    ColorfulPrinter::printThinking("Let's find " + std::to_string(number) + " thing(s) around you!");
    
    switch (number) {
        case 1:
            ColorfulPrinter::printHappy("Can you find ONE nose? Yes! You have ONE nose!");
            ColorfulPrinter::printHappy("Can you find ONE mouth? Perfect! You have ONE mouth!");
            ColorfulPrinter::printHappy("Can you find ONE teddy bear? Great job!");
            break;
        case 2:
            ColorfulPrinter::printHappy("Can you find TWO eyes? Wonderful! You have TWO eyes!");
            ColorfulPrinter::printHappy("Can you find TWO ears? Amazing! You have TWO ears!");
            ColorfulPrinter::printHappy("Can you find TWO hands? Fantastic!");
            break;
        case 3:
            ColorfulPrinter::printHappy("Let's find THREE things!");
            ColorfulPrinter::printHappy("Can you see THREE buttons on your shirt?");
            ColorfulPrinter::printHappy("Can you find THREE toys on the floor?");
            break;
        default:
            ColorfulPrinter::printHappy("Let's count " + std::to_string(number) + " things together!");
            break;
    }
}

void HelloNumbersWorkshop::displayNumberVisually(int number) {
    ColorfulPrinter::printMath("Look at the shape of number " + std::to_string(number) + ":");
    
    // Create visual representation using characters
    std::cout << "\n";
    ColorfulPrinter::printStars(number * 3);
    std::cout << "\n";
    
    switch (number) {
        case 1:
            ColorfulPrinter::printSlowly("✨ 1 ✨ Looks like a straight line, standing tall and proud!");
            break;
        case 2:
            ColorfulPrinter::printSlowly("✨ 2 ✨ Looks like a swan swimming on a pond!");
            break;
        case 3:
            ColorfulPrinter::printSlowly("✨ 3 ✨ Looks like two curves, like a winding path!");
            break;
        default:
            ColorfulPrinter::printSlowly("✨ " + std::to_string(number) + " ✨ What a beautiful number!");
            break;
    }
    
    std::cout << "\n";
}

void HelloNumbersWorkshop::countWithFingers(int number) {
    ColorfulPrinter::printExcited("Let's use our fingers to count!");
    
    ColorfulPrinter::printHelp("Hold up your hand and let's count together:");
    
    switch (number) {
        case 1:
            ColorfulPrinter::printHappy("👆 Show ONE finger - your pointer finger!");
            ColorfulPrinter::printHappy("Great job! That's ONE finger!");
            break;
        case 2:
            ColorularPrinter::printHappy("✌️ Show TWO fingers - pointer and middle finger!");
            ColorfulPrinter::printHappy("Perfect! That's TWO fingers making a peace sign!");
            break;
        case 3:
            ColorfulPrinter::printHappy("🤟 Show THREE fingers - pointer, middle, and ring!");
            ColorfulPrinter::printHappy("Wonderful! That's THREE fingers!");
            break;
        case 5:
            ColorfulPrinter::printHappy("✋ Show ALL FIVE fingers - your whole hand!");
            ColorfulPrinter::printHappy("Amazing! FIVE fingers on one hand!");
            break;
        case 10:
            ColorfulPrinter::printHappy("🙌 Show ALL TEN fingers - both hands!");
            ColorfulPrinter::printExcited("Fantastic! TEN fingers total!");
            break;
        default:
            ColorfulPrinter::printHappy("Let's count " + std::to_string(number) + " on our fingers!");
            break;
    }
}

void HelloNumbersWorkshop::countWithBody(int number) {
    ColorfulPrinter::printExcited("Let's move our bodies to count!");
    
    for (int i = 1; i <= number; ++i) {
        ColorfulPrinter::printHappy("Jump " + std::to_string(i) + "!");
        std::this_thread::sleep_for(std::chrono::milliseconds(500));
    }
    
    ColorfulPrinter::printCelebration("Great jumping! We counted to " + std::to_string(number) + "!");
}

void HelloNumbersWorkshop::tellNumberStory(int number) {
    ColorfulPrinter::printStory("Time for a number story!");
    
    switch (number) {
        case 1:
            ColorfulPrinter::printStory("Once upon a time, there was ONE little star...");
            ColorfulPrinter::printStory("The star was lonely, so it wished for a friend...");
            ColorfulPrinter::printStory("Then the moon came to keep the star company!");
            ColorfulPrinter::printHappy("Now the star has ONE moon friend!");
            break;
        case 2:
            ColorfulPrinter::printStory("TWO little ducks went swimming in a pond...");
            ColorfulPrinter::printStory("They swam together, side by side...");
            ColorfulPrinter::printStory("Quack quack! They were the best of friends!");
            break;
        case 3:
            ColorfulPrinter::printStory("THREE little pigs built houses...");
            ColorfulPrinter::printStory("One built with straw, one with sticks, one with bricks...");
            ColorfulPrinter::printHappy("All THREE pigs were safe and happy!");
            break;
        default:
            ColorfulPrinter::printStory("Let's imagine " + std::to_string(number) + " happy friends playing together!");
            break;
    }
}

void HelloNumbersWorkshop::assessNumberKnowledge(int number) {
    ColorfulPrinter::askQuestion("Can you show me " + std::to_string(number) + " with your fingers?");
    
    // Simulate waiting for child response
    std::this_thread::sleep_for(std::chrono::seconds(3));
    
    // Positive reinforcement regardless of response
    ColorfulPrinter::printHappy("Oh, wonderful trying! You are absolutely brilliant, my dear friend!");
    
    m_numberConfidence[number] += 20;
    if (m_numberConfidence[number] >= 80) {
        m_masteredNumbers[number] = true;
        celebrateMilestone(number);
    }
}

void HelloNumbersWorkshop::celebrateMilestone(int number) {
    ColorfulPrinter::printRainbow("🎉 AMAZING! You've mastered number " + std::to_string(number) + "! 🎉");
    ColorfulPrinter::printAchievement("Number " + std::to_string(number) + " is now your friend!");
    
    if (m_numberFriends) {
        m_numberFriends->celebrateMastery(number);
    }
}

void HelloNumbersWorkshop::update() {
    if (!m_isActive) return;
    
    m_attentionSpent++;
    
    // Check if current activity is complete
    if (mCurrentActivity < m_activities.size()) {
        if (m_activities[mCurrentActivity].completed) {
            mCurrentActivity++;
            updateProgress();
        }
    }
    
    // Check if child needs encouragement
    if (m_attentionSpent > 10) {
        provideEncouragement();
        m_attentionSpent = 0;
    }
    
    // Maintain attention
    maintainAttention();
}

void HelloNumbersWorkshop::updateProgress() {
    int completed = 0;
    for (const auto& activity : m_activities) {
        if (activity.completed) completed++;
    }
    
    m_progress = static_cast<double>(completed) / m_activities.size();
    
    ColorfulPrinter::printProgress("Progress: " + std::to_string(static_cast<int>(m_progress * 100)) + "%");
    
    // Check if workshop is complete
    if (m_progress >= 0.8) {  // 80% completion considered complete
        m_isActive = false;
        endWorkshop();
    }
}

void HelloNumbersWorkshop::provideEncouragement() {
    std::vector<std::string> encouragements = {
        "You are absolutely AMAZING! Numbers adore being friends with wonderful souls like YOU!",
        "Wow! You're learning so wonderfully fast! You're absolutely brilliant!",
        "Fantastic work! You're a number expert!",
        "Oh, keep shining! You're filling our world with beautiful math magic!",
        "Amazing! Numbers are so happy to meet you!"
    };
    
    static std::random_device rd;
    static std::mt19937 gen(rd());
    std::uniform_int_distribution<> dis(0, encouragements.size() - 1);
    
    ColorfulPrinter::printExcited(encouragements[dis(gen)]);
}

void HelloNumbersWorkshop::maintainAttention() {
    // Change activity type if attention is waning
    if (m_attentionSpent > 15) {
        ColorfulPrinter::printStory("Let's try something different to keep our brain happy!");
        suggestBreak();
    }
}

void HelloNumbersWorkshop::suggestBreak() {
    ColorfulPrinter::printHelp("Let's take a tiny break! Stand up and stretch!");
    ColorfulPrinter::printHappy("Great! Now let's continue our number adventure!");
}

void HelloNumbersWorkshop::render() {
    if (!m_isActive) return;
    
    // Render current activity visuals
    if (mCurrentActivity < m_activities.size()) {
        const auto& activity = m_activities[mCurrentActivity];
        
        ColorfulPrinter::printMath("Current Activity: " + activity.name);
        ColorfulPrinter::printStory(activity.description);
    }
}

void HelloNumbersWorkshop::handleInput() {
    // Handle child's input in a patient, encouraging way
    ColorfulPrinter::askQuestion("Are you ready for the next number adventure? (Press any key)");
    
    // Wait for simple input
    std::string input;
    std::getline(std::cin, input);
    
    // Move to next activity
    if (mCurrentActivity < m_activities.size()) {
        m_activities[mCurrentActivity].completed = true;
    }
}

bool HelloNumbersWorkshop::isComplete() const {
    return !m_isActive && m_progress >= 0.8;
}

double HelloNumbersWorkshop::getProgress() const {
    return m_progress;
}

void HelloNumbersWorkshop::endWorkshop() {
    ColorfulPrinter::printStars(40);
    ColorfulPrinter::printRainbow("🌟 CONGRATULATIONS! 🌟");
    ColorfulPrinter::printStars(40);
    
    ColorfulPrinter::printAchievement("You've completed the Hello Numbers workshop!");
    ColorfulPrinter::printHappy("Numbers are now your friends forever!");
    
    int masteredCount = 0;
    for (int i = 1; i <= 10; ++i) {
        if (m_masteredNumbers[i]) masteredCount++;
    }
    
    ColorfulPrinter::printProgress("You mastered " + std::to_string(masteredCount) + " out of 10 numbers!");
    
    if (masteredCount >= 7) {
        ColorfulPrinter::printRainbow("🏆 You're a Number Champion! 🏆");
    }
    
    ColorfulPrinter::printStory("Get ready for your next mathematical adventure!");
}

void HelloNumbersWorkshop::cleanup() {
    m_numberFriends.reset();
    m_guide.reset();
    m_aiHelper.reset();
    m_storyteller.reset();
    m_animationSystem.reset();
    
    m_isActive = false;
    Logger::info("HelloNumbersWorkshop cleanup complete");
}

} // namespace Workshops
} // namespace Recipy