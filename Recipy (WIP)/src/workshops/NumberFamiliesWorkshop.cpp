/*
 * NumberFamiliesWorkshop.cpp - Making Number Theory Child-Friendly
 */

#include "workshops/NumberFamiliesWorkshop.h"
#include "utils/Logger.h"
#include "utils/ColorfulPrinter.h"
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

namespace Recipy {
namespace Workshops {

NumberFamiliesWorkshop::NumberFamiliesWorkshop()
    : m_isRunning(false)
    , m_currentFamily(0)
    , m_familiesDiscovered(0)
    , m_relationshipsFound(0)
    , m_learningProgress(0.0)
    , m_needsBreak(false)
    , m_attentionSpanMinutes(15)
    , m_currentDifficulty(0.1)
    , m_largestFamilyFound(0)
    , m_mostConnectedNumber(0) {
    
    Logger::info("NumberFamiliesWorkshop constructor - Creating number family adventure!");
    m_startTime = std::chrono::steady_clock::now();
    m_lastBreakTime = m_startTime;
}

NumberFamiliesWorkshop::~NumberFamiliesWorkshop() {
    cleanup();
}

bool NumberFamiliesWorkshop::initialize() {
    Logger::info("Initializing Number Families workshop...");
    
    try {
        ColorfulPrinter::printRainbow("👨‍👩‍👧‍👦 Welcome to Number Families! 👨‍👩‍👧‍👦");
        ColorfulPrinter::printExcited("Let's discover how numbers are related to each other like family members!");
        
        if (!initializeComponents()) {
            ColorfulPrinter::printSad("The number family members couldn't gather.");
            return false;
        }
        
        initializeNumberFamilies();
        
        ColorfulPrinter::printHappy("All number families are ready to meet you!");
        return true;
    } catch (...) {
        return false;
    }
}

bool NumberFamiliesWorkshop::initializeComponents() {
    try {
        m_guide = std::make_unique<Characters::FriendlyGuide>();
        m_mathMagician = std::make_unique<Characters::MathMagician>();
        m_aiHelper = std::make_unique<AI::ChildAIHelper>();
        m_numberTheory = std::make_unique<Math::NumberTheory>();
        m_divisibilityAnalyzer = std::make_unique<Math::DivisibilityAnalyzer>();
        m_gcdCalculator = std::make_unique<Math::GreatestCommonDivisor>();
        m_lcmCalculator = std::make_unique<Math::LeastCommonMultiple>();
        
        ColorfulPrinter::printHappy("Number family research center is ready!");
        return true;
    } catch (...) {
        return false;
    }
}

void NumberFamiliesWorkshop::initializeNumberFamilies() {
    Logger::info("Creating number family relationships...");
    
    // Even numbers family
    NumberFamily evenFamily;
    evenFamily.id = 1;
    evenFamily.name = "Even Numbers";
    evenFamily.description = "Numbers that can be divided exactly by 2";
    evenFamily.relationship_rule = "Number ÷ 2 = Whole number";
    evenFamily.visual_representation = "⚫⚪⚫⚪⚫⚪";
    evenFamily.difficulty_level = 1;
    
    for (int i = 2; i <= 100; i += 2) {
        evenFamily.members.push_back(i);
    }
    m_numberFamilies.push_back(evenFamily);
    
    // Odd numbers family
    NumberFamily oddFamily;
    oddFamily.id = 2;
    oddFamily.name = "Odd Numbers";
    oddFamily.description = "Numbers that leave 1 when divided by 2";
    oddFamily.relationship_rule = "Number ÷ 2 = Remainder 1";
    oddFamily.visual_representation = "⚫⚫⚪⚫⚫⚪";
    oddFamily.difficulty_level = 1;
    
    for (int i = 1; i <= 99; i += 2) {
        oddFamily.members.push_back(i);
    }
    m_numberFamilies.push_back(oddFamily);
    
    // Multiples of 3 family
    NumberFamily mult3Family;
    mult3Family.id = 3;
    mult3Family.name = "Multiples of 3";
    mult3Family.description = "Numbers that can be divided exactly by 3";
    mult3Family.relationship_rule = "Number ÷ 3 = Whole number";
    mult3Family.visual_representation = "🔵🔵🔵🔵🔵🔵";
    mult3Family.difficulty_level = 2;
    
    for (int i = 3; i <= 99; i += 3) {
        mult3Family.members.push_back(i);
    }
    m_numberFamilies.push_back(mult3Family);
    
    // Square numbers family
    NumberFamily squareFamily;
    squareFamily.id = 4;
    squareFamily.name = "Square Numbers";
    squareFamily.description = "Numbers made by multiplying a number by itself";
    squareFamily.relationship_rule = "n × n = Square number";
    squareFamily.visual_representation = "⬜⬛⬛⬛⬛⬛⬛⬛⬛";
    squareFamily.difficulty_level = 3;
    
    for (int i = 1; i <= 10; ++i) {
        squareFamily.members.push_back(i * i);
    }
    m_numberFamilies.push_back(squareFamily);
    
    // Prime numbers family
    NumberFamily primeFamily;
    primeFamily.id = 5;
    primeFamily.name = "Prime Numbers";
    primeFamily.description = "Numbers that can only be divided by 1 and themselves";
    primeFamily.relationship_rule = "Only divisible by 1 and itself";
    primeFamily.visual_representation = "💎💎💎💎💎💎💎💎💎";
    primeFamily.difficulty_level = 4;
    
    for (int i = 2; i <= 50; ++i) {
        if (isPrime(i)) {
            primeFamily.members.push_back(i);
        }
    }
    m_numberFamilies.push_back(primeFamily);
    
    // Triangular numbers family
    NumberFamily triangularFamily;
    triangularFamily.id = 6;
    triangularFamily.name = "Triangular Numbers";
    triangularFamily.description = "Numbers that can form triangles";
    triangularFamily.relationship_rule = "1 + 2 + 3 + ... + n = Triangular number";
    triangularFamily.visual_representation = "🔺🔺🔺🔺🔺🔺🔺🔺🔺";
    triangularFamily.difficulty_level = 3;
    
    int sum = 0;
    for (int i = 1; i <= 10; ++i) {
        sum += i;
        triangularFamily.members.push_back(sum);
    }
    m_numberFamilies.push_back(triangularFamily);
    
    // Perfect numbers family
    NumberFamily perfectFamily;
    perfectFamily.id = 7;
    perfectFamily.name = "Perfect Numbers";
    perfectFamily.description = "Numbers whose proper divisors add up to themselves";
    perfectFamily.relationship_rule = "Sum of proper divisors = Number itself";
    perfectFamily.visual_representation = "✨✨✨✨✨✨✨✨✨";
    perfectFamily.difficulty_level = 5;
    
    perfectFamily.members.push_back(6);  // 1 + 2 + 3 = 6
    perfectFamily.members.push_back(28); // 1 + 2 + 4 + 7 + 14 = 28
    m_numberFamilies.push_back(perfectFamily);
    
    // Initialize divisibility and multiple relationships
    initializeDivisibilityRelationships();
    initializeMultiplesRelationships();
    initializeFriendlyFamilies();
    
    ColorfulPrinter::printLearning("Created " + std::to_string(m_numberFamilies.size()) + " number families!");
}

void NumberFamiliesWorkshop::initializeDivisibilityRelationships() {
    for (int num = 1; num <= 50; ++num) {
        m_divisibilityMap[num] = getDivisors(num);
    }
}

void NumberFamiliesWorkshop::initializeMultiplesRelationships() {
    for (int num = 1; num <= 20; ++num) {
        m_multipleMap[num] = getMultiples(num, 10);
    }
}

void NumberFamiliesWorkshop::initializeFriendlyFamilies() {
    // Amicable numbers (friendly pairs)
    m_friendshipMap[220] = {284};  // 220's proper divisors sum to 284
    m_friendshipMap[284] = {220};  // 284's proper divisors sum to 220
    
    m_friendshipMap[1184] = {1210};
    m_friendshipMap[1210] = {1184};
}

void NumberFamiliesWorkshop::start() {
    Logger::info("Starting Number Families workshop...");
    
    if (m_guide) {
        m_guide->sayHello();
        m_guide->explainAdventure();
    }
    
    introduceWorkshop();
    
    m_currentFamily = 0;
    m_isRunning = true;
    
    ColorfulPrinter::printExcited("Let's discover how numbers are related in beautiful families!");
}

void NumberFamiliesWorkshop::introduceWorkshop() {
    ColorfulPrinter::printStory("Welcome to the Number Family Reunion! 🎉");
    
    if (m_mathMagician) {
        m_mathMagician->performMagic();
        ColorfulPrinter::printExcited("Numbers are like people - they have families, friends, and special relationships!");
    }
    
    ColorfulPrinter::printHappy("Just like you have family members, numbers have number families!");
    ColorfulPrinter::printExcited("Some numbers are siblings, some are cousins, some are best friends!");
    
    exploreBasicFamilies();
}

void NumberFamiliesWorkshop::exploreBasicFamilies() {
    ColorfulPrinter::printLearning("Let's meet the basic number families!");
    
    // Even numbers
    ColorfulPrinter::printNumber("Even Family: 2, 4, 6, 8, 10, 12...");
    ColorfulPrinter::printHappy("These numbers can be shared equally between 2 friends!");
    ColorfulPrinter::printExample("6 cookies ÷ 2 friends = 3 cookies each! Perfect sharing!");
    
    // Odd numbers
    ColorfulPrinter::printNumber("Odd Family: 1, 3, 5, 7, 9, 11...");
    ColorfulPrinter::printHappy("These numbers always leave 1 extra when shared between 2 friends!");
    ColorfulPrinter::printExample("7 cookies ÷ 2 friends = 3 each with 1 leftover!");
    
    ColorfulPrinter::printExcited("You're understanding number families so well! 🌟");
}

void NumberFamiliesWorkshop::update() {
    if (!m_isRunning) return;
    
    if (m_needsBreak) {
        std::this_thread::sleep_for(std::chrono::minutes(2));
        m_needsBreak = false;
        ColorfulPrinter::printExcited("Welcome back to the Number Family Reunion!");
    }
    
    if (m_currentFamily < m_numberFamilies.size()) {
        exploreFamily(m_numberFamilies[m_currentFamily]);
        m_currentFamily++;
        updateProgress();
        checkForBreak();
    } else {
        exploreAdvancedFamilies();
        if (m_currentFamily >= m_numberFamilies.size() + 5) {
            endWorkshop();
        }
    }
}

void NumberFamiliesWorkshop::exploreFamily(const NumberFamily& family) {
    ColorfulPrinter::printExcited("Meeting the " + family.name + " Family!");
    ColorfulPrinter::printLearning(family.description);
    
    // Show family members
    std::string members_str = "";
    for (size_t i = 0; i < std::min(family.members.size(), size_t(10)); ++i) {
        members_str += std::to_string(family.members[i]);
        if (i < std::min(family.members.size(), size_t(10)) - 1) members_str += ", ";
    }
    if (family.members.size() > 10) members_str += "...";
    
    ColorfulPrinter::printNumber("Family Members: " + members_str);
    ColorfulPrinter::printMath("Family Rule: " + family.relationship_rule);
    
    // Visual representation
    ColorfulPrinter::printVisual("Family Pattern: " + family.visual_representation);
    
    // Interactive exploration based on family type
    if (family.name == "Even Numbers") {
        exploreEvenFamily();
    } else if (family.name == "Odd Numbers") {
        exploreOddFamily();
    } else if (family.name == "Multiples of 3") {
        exploreDivisibleBy3Family();
    } else if (family.name == "Square Numbers") {
        exploreSquareFamily();
    } else if (family.name == "Prime Numbers") {
        explorePrimeFamilies();
    } else if (family.name == "Triangular Numbers") {
        exploreTriangularFamily();
    } else if (family.name == "Perfect Numbers") {
        explorePerfectFamilies();
    }
    
    m_familiesDiscovered++;
    celebrateFamilyDiscovery();
}

void NumberFamiliesWorkshop::exploreEvenFamily() {
    ColorfulPrinter::printExcited("Let's play with the Even Family!");
    
    ColorfulPrinter::printHappy("Even numbers are super fair - they can always be shared equally!");
    ColorfulPrinter::printExample("4 candies ÷ 2 friends = 2 candies each!");
    ColorfulPrinter::printExample("8 pencils ÷ 2 friends = 4 pencils each!");
    
    // Interactive check
    ColorfulPrinter::printThinking("Is 14 even? Let's check: 14 ÷ 2 = 7! Yes, no remainder!");
    ColorfulPrinter::printThinking("Is 15 even? Let's check: 15 ÷ 2 = 7 remainder 1! No, it's odd!");
    
    ColorfulPrinter::printAchievement("You understand the Even Family! They're the most sharing numbers! 🤝");
}

void NumberFamiliesWorkshop::exploreOddFamily() {
    ColorfulPrinter::printExcited("Let's meet the Odd Family!");
    
    ColorfulPrinter::printHappy("Odd numbers are unique - they always leave 1 when shared equally!");
    ColorfulPrinter::printExample("5 cookies ÷ 2 friends = 2 each with 1 leftover!");
    ColorfulPrinter::printExample("9 stickers ÷ 2 friends = 4 each with 1 leftover!");
    
    ColorfulPrinter::printExcited("That leftover makes odd numbers special! They have a unique personality!");
    
    ColorfulPrinter::printAchievement("You understand the Odd Family! They're the unique individualists! 🌟");
}

void NumberFamiliesWorkshop::exploreDivisibleBy3Family() {
    ColorfulPrinter::printExcited("Let's discover the Multiples of 3 Family!");
    
    ColorfulPrinter::printHappy("These numbers can be shared equally among 3 friends!");
    ColorfulPrinter::printExample("6 toys ÷ 3 friends = 2 toys each!");
    ColorfulPrinter::printExample("12 crayons ÷ 3 friends = 4 crayons each!");
    
    // Magic trick for divisibility by 3
    ColorfulPrinter::printExcited("Magic trick: Add the digits of any number!");
    ColorfulPrinter::printExample("For 24: 2 + 4 = 6. Since 6 is divisible by 3, so is 24!");
    ColorfulPrinter::printExample("For 17: 1 + 7 = 8. Since 8 isn't divisible by 3, neither is 17!");
    
    ColorfulPrinter::printAchievement("You know the divisibility by 3 magic! ✨");
}

void NumberFamiliesWorkshop::exploreSquareFamily() {
    ColorfulPrinter::printExcited("Let's explore the Square Numbers Family!");
    
    ColorfulPrinter::printHappy("Square numbers make perfect squares!");
    ColorfulPrinter::printVisual("1×1 = ⬜ (1 square)");
    ColorfulPrinter::printVisual("2×2 = ⬛⬛⬛⬛ (4 squares)");
    ColorfulPrinter::printVisual("3×3 = 9 squares in a big square!");
    
    for (int i = 1; i <= 5; ++i) {
        ColorfulPrinter::printMath(std::to_string(i) + " × " + std::to_string(i) + " = " + std::to_string(i * i));
    }
    
    ColorfulPrinter::printExcited("Square numbers are perfect and balanced! ⚖️");
}

void NumberFamiliesWorkshop::explorePrimeFamilies() {
    ColorfulPrinter::printExcited("Let's meet the special Prime Numbers Family!");
    
    ColorfulPrinter::printHappy("Prime numbers are like mathematical treasures!");
    ColorfulPrinter::printLearning("They can only be divided by 1 and themselves");
    
    std::vector<int> small_primes = {2, 3, 5, 7, 11, 13, 17, 19};
    ColorfulPrinter::printNumber("Small Primes: 2, 3, 5, 7, 11, 13, 17, 19...");
    
    ColorfulPrinter::printExample("7 can only be: 7×1 or 1×7");
    ColorfulPrinter::printExample("6 can be: 6×1, 3×2, 2×3, 1×6 (so 6 isn't prime)");
    
    ColorfulPrinter::printAchievement("Prime numbers are the building blocks of all other numbers! 💎");
}

void NumberFamiliesWorkshop::exploreTriangularFamily() {
    ColorfulPrinter::printExcited("Let's discover the Triangular Numbers Family!");
    
    ColorfulPrinter::printHappy("These numbers can form perfect triangles!");
    
    int sum = 0;
    for (int i = 1; i <= 6; ++i) {
        sum += i;
        ColorfulPrinter::printMath("1 + 2 + ... + " + std::to_string(i) + " = " + std::to_string(sum));
        
        // Visual triangle
        std::string triangle = "";
        for (int j = 1; j <= i; ++j) {
            triangle += "🔺 ";
        }
        ColorfulPrinter::printVisual(triangle);
    }
    
    ColorfulPrinter::printExcited("Triangular numbers build beautiful pyramids! 🔺");
}

void NumberFamiliesWorkshop::explorePerfectFamilies() {
    ColorfulPrinter::printExcited("Let's meet the rare Perfect Numbers Family!");
    
    ColorfulPrinter::printHappy("Perfect numbers are mathematically perfect!");
    ColorfulPrinter::printLearning("Their proper divisors add up to exactly themselves");
    
    // Show 6
    ColorfulPrinter::printNumber("Perfect Number: 6");
    ColorfulPrinter::printMath("Proper divisors of 6: 1, 2, 3");
    ColorfulPrinter::printMath("1 + 2 + 3 = 6! Perfect!");
    
    // Show 28
    ColorfulPrinter::printNumber("Perfect Number: 28");
    ColorfulPrinter::printMath("Proper divisors of 28: 1, 2, 4, 7, 14");
    ColorfulPrinter::printMath("1 + 2 + 4 + 7 + 14 = 28! Perfect!");
    
    ColorfulPrinter::printExcited("Perfect numbers are very rare and special! ✨");
}

void NumberFamiliesWorkshop::exploreAdvancedFamilies() {
    ColorfulPrinter::printLearning("Let's explore advanced number relationships!");
    
    switch (m_currentFamily - m_numberFamilies.size()) {
        case 0:
            exploreDivisibilityFamilies();
            break;
        case 1:
            exploreMultipleFamilies();
            break;
        case 2:
            exploreFriendlyFamilies();
            break;
        case 3:
            createFamilyTree();
            break;
        case 4:
            discoverHiddenRelationships();
            break;
    }
    
    m_currentFamily++;
}

void NumberFamiliesWorkshop::exploreDivisibilityFamilies() {
    ColorfulPrinter::printExcited("Let's explore Divisibility Families!");
    
    // Show divisibility relationships for a number
    int number = 12;
    ColorfulPrinter::printNumber("Divisibility Family for " + std::to_string(number) + ":");
    
    auto divisors = getDivisors(number);
    for (int divisor : divisors) {
        ColorfulPrinter::printMath(std::to_string(number) + " ÷ " + std::to_string(divisor) + " = " + 
                                std::to_string(number / divisor) + " (no remainder!)");
    }
    
    ColorfulPrinter::printAchievement("You understand how numbers divide into families! 👨‍👩‍👧‍👦");
}

void NumberFamiliesWorkshop::exploreMultipleFamilies() {
    ColorfulPrinter::printExcited("Let's explore Multiple Families!");
    
    int number = 4;
    ColorfulPrinter::printNumber("Multiple Family for " + std::to_string(number) + ":");
    
    auto multiples = getMultiples(number, 8);
    for (int multiple : multiples) {
        ColorfulPrinter::printMath(std::to_string(number) + " × " + 
                                std::to_string(multiple / number) + " = " + std::to_string(multiple));
    }
    
    ColorfulPrinter::printHappy("All these numbers are in the " + std::to_string(number) + " family!");
}

void NumberFamiliesWorkshop::exploreFriendlyFamilies() {
    ColorfulPrinter::printExcited("Let's discover Friendly Number Pairs!");
    
    ColorfulPrinter::printStory("Some numbers are best friends - they're called amicable numbers!");
    
    // Show 220 and 284
    ColorfulPrinter::printNumber("Best Friends: 220 and 284");
    ColorfulPrinter::printMath("Proper divisors of 220 add up to 284");
    ColorfulPrinter::printMath("Proper divisors of 284 add up to 220");
    
    ColorfulPrinter::printExcited("They give to each other equally! That's true friendship! 💕");
}

void NumberFamiliesWorkshop::createFamilyTree() {
    ColorfulPrinter::printExcited("Let's create a Number Family Tree!");
    
    int root = 12;
    FamilyTree tree;
    tree.root_number = root;
    tree.family_name = "The Dozens Family";
    
    // Find relationships
    tree.children = {24, 36, 48};  // Multiples
    tree.parents = {1, 2, 3, 4, 6};  // Divisors
    tree.siblings = {18, 24, 30};  // Same number of divisors
    
    displayFamilyTree(tree);
    
    ColorfulPrinter::printAchievement("You created a complete family tree! 🌳");
}

void NumberFamiliesWorkshop::displayFamilyTree(const FamilyTree& tree) {
    ColorfulPrinter::printNumber("Family Tree for " + std::to_string(tree.root_number) + " (" + tree.family_name + ")");
    
    ColorfulPrinter::printMath("Parents (Divisors): " + vectorToString(tree.parents));
    ColorfulPrinter::printMath("Children (Multiples): " + vectorToString(tree.children));
    ColorfulPrinter::printMath("Siblings (Similar): " + vectorToString(tree.siblings));
}

void NumberFamiliesWorkshop::discoverHiddenRelationships() {
    ColorfulPrinter::printExcited("Let's discover hidden number relationships!");
    
    ColorfulPrinter::printStory("Numbers have secret connections that mathematicians discover!");
    
    // Show GCD relationships
    ColorfulPrinter::printMath("GCD(12, 18) = 6 (Greatest Common Divisor)");
    ColorfulPrinter::printMath("LCM(12, 18) = 36 (Least Common Multiple)");
    
    ColorfulPrinter::printExcited("These relationships help us solve real-world problems!");
    
    ColorfulPrinter::printAchievement("You're becoming a number relationship expert! 🔍");
}

std::vector<int> NumberFamiliesWorkshop::getDivisors(int number) {
    std::vector<int> divisors;
    for (int i = 1; i <= number; ++i) {
        if (number % i == 0) {
            divisors.push_back(i);
        }
    }
    return divisors;
}

std::vector<int> NumberFamiliesWorkshop::getMultiples(int number, int count) {
    std::vector<int> multiples;
    for (int i = 1; i <= count; ++i) {
        multiples.push_back(number * i);
    }
    return multiples;
}

bool NumberFamiliesWorkshop::isPrime(int number) {
    if (number < 2) return false;
    for (int i = 2; i <= sqrt(number); ++i) {
        if (number % i == 0) return false;
    }
    return true;
}

std::string NumberFamiliesWorkshop::vectorToString(const std::vector<int>& vec) {
    std::string result = "";
    for (size_t i = 0; i < vec.size(); ++i) {
        result += std::to_string(vec[i]);
        if (i < vec.size() - 1) result += ", ";
    }
    return result;
}

void NumberFamiliesWorkshop::celebrateFamilyDiscovery() {
    m_relationshipsFound += 5; // Estimate relationships found per family
    
    std::vector<std::string> celebrations = {
        "Amazing family discovery! Numbers love showing you their relationships! 👨‍👩‍👧‍👦",
        "Wonderful! You understand how numbers are connected! 🌐",
        "Fantastic! You're becoming a number family expert! 📊",
        "Brilliant! Numbers are revealing their secrets to you! 🔍",
        "Incredible! You see the beautiful patterns in number families! ✨"
    };
    
    int index = rand() % celebrations.size();
    ColorfulPrinter::printExcited(celebrations[index]);
    
    // Progress visualization
    int progress = (m_currentFamily * 100) / (m_numberFamilies.size() + 5);
    ColorfulPrinter::printProgress("Family Discovery Progress: " + std::to_string(progress) + "%");
    
    // Milestone celebrations
    if (m_familiesDiscovered == 3) {
        ColorfulPrinter::printAchievement("🎉 3 Families Discovered! You're a Family Explorer! 🎉");
    } else if (m_familiesDiscovered == 5) {
        ColorfulPrinter::printAchievement("🌟 5 Families! You're a Relationship Expert! 🌟");
    } else if (m_familiesDiscovered == 7) {
        ColorfulPrinter::printAchievement("💎 All Basic Families! Number Theory Master! 💎");
    }
}

void NumberFamiliesWorkshop::updateProgress() {
    m_learningProgress = (m_currentFamily * 100.0) / (m_numberFamilies.size() + 5);
    
    if (m_aiHelper) {
        m_aiHelper->analyzeProgress(m_learningProgress);
        m_aiHelper->provideEncouragement();
    }
    
    Logger::info("Number families progress: " + std::to_string(m_learningProgress) + "%");
}

void NumberFamiliesWorkshop::checkForBreak() {
    auto now = std::chrono::steady_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::minutes>(now - m_lastBreakTime);
    
    if (duration.count() >= m_attentionSpanMinutes) {
        m_needsBreak = true;
        suggestBreak();
    }
}

void NumberFamiliesWorkshop::suggestBreak() {
    ColorfulPrinter::printGentleWarning("Number families need to rest too!");
    ColorfulPrinter::printStory("Let's take a little break! Even family explorers need to recharge!");
    ColorfulPrinter::printHappy("When we come back, we'll meet more amazing number families!");
    
    m_needsBreak = true;
    m_lastBreakTime = std::chrono::steady_clock::now();
}

void NumberFamiliesWorkshop::render() {
    ColorfulPrinter::printStars(4);
}

void NumberFamiliesWorkshop::handleInput() {
    ColorfulPrinter::printHelp("Keep exploring! Every number family you discover is special!");
}

bool NumberFamiliesWorkshop::isComplete() const {
    return m_currentFamily >= m_numberFamilies.size() + 5;
}

double NumberFamiliesWorkshop::getProgress() const {
    return m_learningProgress;
}

void NumberFamiliesWorkshop::endWorkshop() {
    ColorfulPrinter::printAchievement("You've completed the Number Families workshop!");
    ColorfulPrinter::printExcited("You're now a Number Family Expert! 👨‍👩‍👧‍👦");
    
    ColorfulPrinter::printProgress("Families discovered: " + std::to_string(m_familiesDiscovered));
    ColorfulPrinter::printProgress("Relationships found: " + std::to_string(m_relationshipsFound));
    
    if (m_familiesDiscovered >= 7) {
        ColorfulPrinter::printAchievement("🏆 Number Theory Master! You understand all basic families! 🏆");
    }
    
    m_isRunning = false;
}

void NumberFamiliesWorkshop::cleanup() {
    m_numberTheory.reset();
    m_divisibilityAnalyzer.reset();
    m_gcdCalculator.reset();
    m_lcmCalculator.reset();
    m_guide.reset();
    m_mathMagician.reset();
    m_aiHelper.reset();
    
    Logger::info("NumberFamiliesWorkshop cleanup complete");
}

} // namespace Workshops
} // namespace Recipy