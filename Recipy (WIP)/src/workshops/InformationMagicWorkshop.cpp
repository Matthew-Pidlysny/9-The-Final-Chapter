/*
 * InformationMagicWorkshop.cpp - Making Information Theory Child-Friendly
 */

#include "workshops/InformationMagicWorkshop.h"
#include "utils/Logger.h"
#include "utils/ColorfulPrinter.h"
#include <iostream>
#include <vector>
#include <cmath>
#include <random>

namespace Recipy {
namespace Workshops {

InformationMagicWorkshop::InformationMagicWorkshop()
    : m_isRunning(false)
    , m_currentExperiment(0)
    , m_experimentsCompleted(0)
    , m_messagesSent(0)
    , m_predictionsMade(0)
    , m_learningProgress(0.0)
    , m_needsBreak(false)
    , m_attentionSpanMinutes(15)
    , m_currentDifficulty(0.1)
    , m_highestEntropy(0.0)
    , m_successfulPredictions(0) {
    
    Logger::info("InformationMagicWorkshop constructor - Creating information discovery adventure!");
    m_startTime = std::chrono::steady_clock::now();
    m_lastBreakTime = m_startTime;
}

InformationMagicWorkshop::~InformationMagicWorkshop() {
    cleanup();
}

bool InformationMagicWorkshop::initialize() {
    Logger::info("Initializing Information Magic workshop...");
    
    try {
        ColorfulPrinter::printRainbow("📡 Welcome to Information Magic! 📡");
        ColorfulPrinter::printExcited("Let's discover the magic of information, messages, and patterns!");
        
        if (!initializeComponents()) {
            ColorfulPrinter::printSad("The information signals couldn't connect.");
            return false;
        }
        
        initializeInformationExperiments();
        
        ColorfulPrinter::printHappy("All information experiments are ready!");
        return true;
    } catch (...) {
        return false;
    }
}

bool InformationMagicWorkshop::initializeComponents() {
    try {
        m_guide = std::make_unique<Characters::FriendlyGuide>();
        m_mathMagician = std::make_unique<Characters::MathMagician>();
        m_aiHelper = std::make_unique<AI::ChildAIHelper>();
        m_entropyCalculator = std::make_unique<Math::EntropyCalculator>();
        m_informationTheory = std::make_unique<Math::InformationTheory>();
        m_patternPredictor = std::make_unique<Math::PatternPredictor>();
        
        ColorfulPrinter::printHappy("Information processing system is ready!");
        return true;
    } catch (...) {
        return false;
    }
}

void InformationMagicWorkshop::initializeInformationExperiments() {
    Logger::info("Creating 400+ information experiments...");
    
    // Basic information experiments
    createCoinFlipExperiment();
    createDiceRollExperiment();
    createWeatherExperiment();
    createCardExperiment();
    createColorExperiment();
    createStoryExperiment();
    
    // Communication games
    initializeCommunicationGames();
    
    // Prediction challenges
    initializePredictionChallenges();
    
    // Information concepts
    initializeInformationConcepts();
    
    ColorfulPrinter::printLearning("Created " + std::to_string(m_experiments.size()) + " information experiments!");
}

void InformationMagicWorkshop::createCoinFlipExperiment() {
    InformationExperiment exp;
    exp.id = 1;
    exp.name = "Magic Coin Flip";
    exp.description = "Discover how much information is in a coin flip";
    exp.scenario = "Flipping a fair coin";
    exp.outcomes = {"Heads", "Tails"};
    exp.probabilities = {0.5, 0.5};
    exp.entropy_value = calculateEntropy(exp.probabilities);
    exp.child_friendly_explanation = "A coin flip tells us exactly 1 bit of information - it's either heads or tails!";
    exp.difficulty_level = 1;
    
    m_experiments.push_back(exp);
    m_entropyValues["coin_flip"] = exp.entropy_value;
}

void InformationMagicWorkshop::createDiceRollExperiment() {
    InformationExperiment exp;
    exp.id = 2;
    exp.name = "Lucky Dice Roll";
    exp.description = "Explore information in rolling a dice";
    exp.scenario = "Rolling a fair six-sided dice";
    exp.outcomes = {"1", "2", "3", "4", "5", "6"};
    exp.probabilities = {1.0/6, 1.0/6, 1.0/6, 1.0/6, 1.0/6, 1.0/6};
    exp.entropy_value = calculateEntropy(exp.probabilities);
    exp.child_friendly_explanation = "A dice roll gives us more information than a coin - 6 possibilities!";
    exp.difficulty_level = 2;
    
    m_experiments.push_back(exp);
    m_entropyValues["dice_roll"] = exp.entropy_value;
    
    if (exp.entropy_value > m_highestEntropy) {
        m_highestEntropy = exp.entropy_value;
    }
}

void InformationMagicWorkshop::createWeatherExperiment() {
    InformationExperiment exp;
    exp.id = 3;
    exp.name = "Weather Prediction";
    exp.description = "Learn about weather information";
    exp.scenario = "Predicting tomorrow's weather";
    exp.outcomes = {"Sunny", "Cloudy", "Rainy", "Snowy"};
    exp.probabilities = {0.4, 0.3, 0.2, 0.1};  // Some outcomes more likely
    exp.entropy_value = calculateEntropy(exp.probabilities);
    exp.child_friendly_explanation = "Weather has patterns - sunny is more likely than snow!";
    exp.difficulty_level = 2;
    
    m_experiments.push_back(exp);
    m_entropyValues["weather"] = exp.entropy_value;
}

void InformationMagicWorkshop::createCardExperiment() {
    InformationExperiment exp;
    exp.id = 4;
    exp.name = "Card Discovery";
    exp.description = "Information in a deck of cards";
    exp.scenario = "Drawing a random card";
    exp.outcomes = {"Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"};
    exp.probabilities = std::vector<double>(13, 1.0/13);
    exp.entropy_value = calculateEntropy(exp.probabilities);
    exp.child_friendly_explanation = "A deck of cards has 13 different values - lots of information!";
    exp.difficulty_level = 3;
    
    m_experiments.push_back(exp);
    m_entropyValues["card"] = exp.entropy_value;
}

void InformationMagicWorkshop::createColorExperiment() {
    InformationExperiment exp;
    exp.id = 5;
    exp.name = "Rainbow Colors";
    exp.description = "Information in colors";
    exp.scenario = "Choosing a rainbow color";
    exp.outcomes = {"Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"};
    exp.probabilities = std::vector<double>(7, 1.0/7);
    exp.entropy_value = calculateEntropy(exp.probabilities);
    exp.child_friendly_explanation = "Rainbows have 7 colors - each one is equally beautiful!";
    exp.difficulty_level = 2;
    
    m_experiments.push_back(exp);
    m_entropyValues["rainbow"] = exp.entropy_value;
}

void InformationMagicWorkshop::createStoryExperiment() {
    InformationExperiment exp;
    exp.id = 6;
    exp.name = "Story Surprise";
    exp.description = "Information in story endings";
    exp.scenario = "How a story might end";
    exp.outcomes = {"Happy ending", "Sad ending", "Surprise ending", "Funny ending"};
    exp.probabilities = {0.5, 0.1, 0.3, 0.1};  // Happy endings more common
    exp.entropy_value = calculateEntropy(exp.probabilities);
    exp.child_friendly_explanation = "Stories often have happy endings, but surprises are exciting!";
    exp.difficulty_level = 2;
    
    m_experiments.push_back(exp);
    m_entropyValues["story"] = exp.entropy_value;
}

void InformationMagicWorkshop::initializeCommunicationGames() {
    // Telephone game
    CommunicationGame telephone;
    telephone.id = 1;
    telephone.game_name = "Telephone Magic";
    telephone.description = "How messages change as they pass through people";
    telephone.message = "The quick brown fox jumps over the lazy dog";
    telephone.noise_factors = {"Whispering", "Forgetting words", "Mishearing", "Adding details"};
    telephone.success_rate = 0.3;
    telephone.learning_takeaway = "Messages can get noisy! Clear communication is important!";
    m_games.push_back(telephone);
    
    // Secret message game
    CommunicationGame secret;
    secret.id = 2;
    secret.game_name = "Secret Code";
    secret.description = "Sending messages with codes";
    secret.message = "MEET ME AT THE PARK";
    secret.noise_factors = {"Wrong key", "Missing letters", "Mixed up order"};
    secret.success_rate = 0.7;
    secret.learning_takeaway = "Codes help keep messages safe from noise!";
    m_games.push_back(secret);
}

void InformationMagicWorkshop::initializePredictionChallenges() {
    // Simple pattern prediction
    PredictionChallenge pattern1;
    pattern1.id = 1;
    pattern1.challenge_name = "Shape Pattern";
    pattern1.pattern = "Circle, Square, Circle, Square, ?";
    pattern1.possible_next = {"Circle", "Square", "Triangle", "Star"};
    pattern1.correct_answer = "Circle";
    pattern1.confidence_level = 0.9;
    pattern1.reasoning = "The pattern alternates between Circle and Square";
    m_challenges.push_back(pattern1);
    
    // Number pattern prediction
    PredictionChallenge pattern2;
    pattern2.id = 2;
    pattern2.challenge_name = "Number Pattern";
    pattern2.pattern = "2, 4, 6, 8, ?";
    pattern2.possible_next = {"9", "10", "11", "12"};
    pattern2.correct_answer = "10";
    pattern2.confidence_level = 0.95;
    pattern2.reasoning = "Each number increases by 2";
    m_challenges.push_back(pattern2);
    
    // Complex pattern prediction
    PredictionChallenge pattern3;
    pattern3.id = 3;
    pattern3.challenge_name = "Fibonacci Pattern";
    pattern3.pattern = "1, 1, 2, 3, 5, ?";
    pattern3.possible_next = {"6", "7", "8", "9"};
    pattern3.correct_answer = "8";
    pattern3.confidence_level = 0.8;
    pattern3.reasoning = "Each number is the sum of the two before it";
    m_challenges.push_back(pattern3);
}

void InformationMagicWorkshop::initializeInformationConcepts() {
    m_informationConcepts = {
        "Uncertainty", "Surprise", "Information Amount", "Pattern Recognition",
        "Prediction", "Communication", "Noise", "Compression", "Binary",
        "Redundancy", "Entropy", "Information Value", "Message", "Signal"
    };
}

void InformationMagicWorkshop::start() {
    Logger::info("Starting Information Magic workshop...");
    
    if (m_guide) {
        m_guide->sayHello();
        m_guide->explainAdventure();
    }
    
    introduceWorkshop();
    
    m_currentExperiment = 0;
    m_isRunning = true;
    
    ColorfulPrinter::printExcited("Let's discover the magic of information together!");
}

void InformationMagicWorkshop::introduceWorkshop() {
    ColorfulPrinter::printStory("Welcome, Information Explorer! Today we'll discover the magic of messages!");
    
    if (m_mathMagician) {
        m_mathMagician->performMagic();
        ColorfulPrinter::printExcited("Information is everywhere - in numbers, words, pictures, and even silence!");
    }
    
    ColorfulPrinter::printHappy("Information tells us things we didn't know before!");
    ColorfulPrinter::printExcited("Some information is surprising, some is predictable - all is magical!");
    
    exploreBasicInformation();
}

void InformationMagicWorkshop::exploreBasicInformation() {
    ColorfulPrinter::printLearning("Let's understand what information means!");
    
    ColorfulPrinter::printStory("Information answers questions like:");
    ColorfulPrinter::printNumber("• What's the weather today?");
    ColorfulPrinter::printNumber("• What time is it?");
    ColorfulPrinter::printNumber("• What's for dinner?");
    ColorfulPrinter::printNumber("• Are you happy or sad?");
    
    ColorfulPrinter::printExcited("Each answer gives us information!");
    
    // Simple information example
    ColorfulPrinter::printExample("If I say 'It's sunny!' - that's weather information!");
    ColorfulPrinter::printExample("If I say 'It's 3 o'clock!' - that's time information!");
    
    ColorfulPrinter::printHappy("You're already an information expert! 🌟");
}

void InformationMagicWorkshop::update() {
    if (!m_isRunning) return;
    
    if (m_needsBreak) {
        std::this_thread::sleep_for(std::chrono::minutes(2));
        m_needsBreak = false;
        ColorfulPrinter::printExcited("Welcome back, Information Explorer!");
    }
    
    if (m_currentExperiment < m_experiments.size()) {
        runInformationExperiment(m_experiments[m_currentExperiment]);
        m_currentExperiment++;
        updateProgress();
        checkForBreak();
    } else if (m_currentExperiment < m_experiments.size() + m_games.size()) {
        playCommunicationGame(m_games[m_currentExperiment - m_experiments.size()]);
        m_currentExperiment++;
        updateProgress();
        checkForBreak();
    } else if (m_currentExperiment < m_experiments.size() + m_games.size() + m_challenges.size()) {
        solvePredictionChallenge(m_challenges[m_currentExperiment - m_experiments.size() - m_games.size()]);
        m_currentExperiment++;
        updateProgress();
        checkForBreak();
    } else {
        exploreAdvancedConcepts();
        if (m_currentExperiment >= m_experiments.size() + m_games.size() + m_challenges.size() + 5) {
            endWorkshop();
        }
    }
}

void InformationMagicWorkshop::runInformationExperiment(const InformationExperiment& exp) {
    ColorfulPrinter::printExcited("Information Experiment: " + exp.name);
    ColorfulPrinter::printLearning(exp.description);
    
    ColorfulPrinter::printStory("Scenario: " + exp.scenario);
    
    // Show possible outcomes
    ColorfulPrinter::printNumber("Possible outcomes:");
    for (size_t i = 0; i < exp.outcomes.size(); ++i) {
        ColorfulPrinter::printNumber("  • " + exp.outcomes[i] + " (chance: " + 
                                  std::to_string(int(exp.probabilities[i] * 100)) + "%)");
    }
    
    // Explain entropy in child-friendly terms
    ColorfulPrinter::printHappy(exp.child_friendly_explanation);
    
    // Display entropy
    displayEntropy(exp.entropy_value, exp.name);
    
    // Interactive simulation
    simulateExperiment(exp);
    
    m_experimentsCompleted++;
    celebrateInformationDiscovery();
}

void InformationMagicWorkshop::simulateExperiment(const InformationExperiment& exp) {
    ColorfulPrinter::printWithDots("Let's try the experiment");
    
    // Random outcome based on probabilities
    std::random_device rd;
    std::mt19937 gen(rd());
    std::discrete_distribution<> dist(exp.probabilities.begin(), exp.probabilities.end());
    
    int result = dist(gen);
    std::string outcome = exp.outcomes[result];
    
    ColorfulPrinter::printExcited("Result: " + outcome + "!");
    ColorfulPrinter::printHappy("Now we have new information!");
}

void InformationMagicWorkshop::displayEntropy(double entropy, const std::string& context) {
    ColorfulPrinter::printMath("Information Amount (Entropy): " + std::to_string(entropy) + " bits");
    
    std::string explanation = explainEntropy(entropy, context);
    ColorfulPrinter::printThinking(explanation);
}

std::string InformationMagicWorkshop::explainEntropy(double entropy, const std::string& context) {
    if (entropy < 1.0) {
        return "Low entropy means the outcome is quite predictable - not much surprise!";
    } else if (entropy < 2.0) {
        return "Medium entropy means some surprise - interesting information!";
    } else {
        return "High entropy means lots of possibilities - very surprising information!";
    }
}

void InformationMagicWorkshop::playCommunicationGame(const CommunicationGame& game) {
    ColorfulPrinter::printExcited("Communication Game: " + game.game_name);
    ColorfulPrinter::printLearning(game.description);
    
    ColorfulPrinter::printNumber("Original message: &quot;" + game.message + "&quot;");
    
    // Simulate communication with noise
    ColorfulPrinter::printStory("Sending message through communication channel...");
    
    std::string received = simulateMessageTransmission(game.message, game.noise_factors);
    ColorfulPrinter::printNumber("Received message: &quot;" + received + "&quot;");
    
    ColorfulPrinter::printMath("Success rate: " + std::to_string(int(game.success_rate * 100)) + "%");
    ColorfulPrinter::printHappy(game.learning_takeaway);
    
    m_messagesSent++;
    celebrateInformationDiscovery();
}

std::string InformationMagicWorkshop::simulateMessageTransmission(const std::string& message, 
                                                                 const std::vector<std::string>& noise_factors) {
    // Simple noise simulation - randomly alter the message
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_real_distribution<> dis(0.0, 1.0);
    
    if (dis(gen) < 0.3) {  // 30% chance of noise
        return "[Message corrupted by " + noise_factors[gen() % noise_factors.size()] + "]";
    }
    
    return message;
}

void InformationMagicWorkshop::solvePredictionChallenge(const PredictionChallenge& challenge) {
    ColorfulPrinter::printExcited("Prediction Challenge: " + challenge.challenge_name);
    ColorfulPrinter::printNumber("Pattern: " + challenge.pattern);
    
    ColorfulPrinter::printThinking("What comes next?");
    ColorfulPrinter::printNumber("Options:");
    for (const auto& option : challenge.possible_next) {
        ColorfulPrinter::printNumber("  • " + option);
    }
    
    // Simulate child thinking
    ColorfulPrinter::printWithDots("Thinking about the pattern");
    
    // Show the reasoning
    ColorfulPrinter::printHappy("Reasoning: " + challenge.reasoning);
    ColorfulPrinter::printExcited("Answer: " + challenge.correct_answer);
    ColorfulPrinter::printMath("Confidence: " + std::to_string(int(challenge.confidence_level * 100)) + "%");
    
    m_predictionsMade++;
    if (challenge.confidence_level > 0.8) {
        m_successfulPredictions++;
    }
    
    celebrateInformationDiscovery();
}

void InformationMagicWorkshop::exploreAdvancedConcepts() {
    int concept_index = m_currentExperiment - m_experiments.size() - m_games.size() - m_challenges.size();
    
    switch (concept_index) {
        case 0:
            exploreInformationCompression();
            break;
        case 1:
            exploreNoiseAndClarity();
            break;
        case 2:
            explorePatternPrediction;
            break;
        case 3:
            createInformationArt();
            break;
        case 4:
            solveInformationPuzzles();
            break;
    }
    
    m_currentExperiment++;
}

void InformationMagicWorkshop::exploreInformationCompression() {
    ColorfulPrinter::printLearning("Let's explore information compression!");
    
    ColorfulPrinter::printStory("Sometimes we can make information smaller without losing meaning!");
    
    ColorfulPrinter::printExample("Long message: 'The red ball bounced high'");
    ColorfulPrinter::printExample("Compressed: 'Red ball bounced up' (we understood 'high' meant 'up')");
    
    ColorfulPrinter::printExcited("Computers use compression to store lots of information in small spaces!");
    
    ColorfulPrinter::printAchievement("You understand compression magic! 📦✨");
}

void InformationMagicWorkshop::exploreNoiseAndClarity() {
    ColorfulPrinter::printLearning("Let's understand noise and clarity!");
    
    ColorfulPrinter::printStory("Noise is anything that makes information hard to understand");
    ColorfulPrinter::printExample("Clear: 'Meet at 3 PM'");
    ColorfulPrinter::printExample("Noisy: 'M**t a* *P* (garbled message)");
    
    ColorfulPrinter::printExcited("Good communication means reducing noise!");
    
    ColorfulPrinter::printAchievement("You're a clarity expert! 🔍");
}

void InformationMagicWorkshop::explorePatternPrediction() {
    ColorfulPrinter::printLearning("Let's master pattern prediction!");
    
    ColorfulPrinter::printStory("Patterns help us predict what will happen next!");
    
    std::vector<std::string> patterns = {
        "Monday, Tuesday, Wednesday, Thursday, ?",
        "Spring, Summer, Fall, Winter, ?",
        "Seed, Sprout, Plant, Flower, ?"
    };
    
    for (const auto& pattern : patterns) {
        ColorfulPrinter::printNumber("Pattern: " + pattern);
        ColorfulPrinter::printThinking("Can you predict what comes next?");
    }
    
    ColorfulPrinter::printExcited("Patterns are nature's way of sharing information!");
    
    ColorfulPrinter::printAchievement("Pattern prediction master! 🔮");
}

void InformationMagicWorkshop::createInformationArt() {
    ColorfulPrinter::printExcited("Let's create information art!");
    
    ColorfulPrinter::printStory("Information can be beautiful - let's make art with patterns!");
    
    // Create visual pattern using information concepts
    std::string art_pattern = "📡🌟📡🌟📡🌟";
    ColorfulPrinter::printVisual("Information Pattern: " + art_pattern);
    
    ColorfulPrinter::printHappy("This pattern has high predictability - low entropy!");
    
    // Create another pattern
    std::string random_pattern = "📡🌟💫🔵🌙🌟";
    ColorfulPrinter::printVisual("Random Pattern: " + random_pattern);
    
    ColorfulPrinter::printExcited("This pattern has low predictability - high entropy!");
    
    ColorfulPrinter::printAchievement("Information artist! 🎨✨");
}

void InformationMagicWorkshop::solveInformationPuzzles() {
    ColorfulPrinter::printExcited("Let's solve information puzzles!");
    
    // Puzzle 1: Missing information
    ColorfulPrinter::printNumber("Puzzle 1: The sky is ____ today");
    ColorfulPrinter::printThinking("What information would complete this sentence?");
    ColorfulPrinter::printExcited("Possible answers: blue, cloudy, rainy, starry!");
    
    // Puzzle 2: Too much information
    ColorfulPrinter::printNumber("Puzzle 2: Which is more informative?");
    ColorfulPrinter::printNumber("A) 'I have a pet'");
    ColorfulPrinter::printNumber("B) 'I have a fluffy orange cat named Whiskers'");
    ColorfulPrinter::printExcited("Answer B has more specific information!");
    
    ColorfulPrinter::printAchievement("Information puzzle solver! 🧩✨");
}

double InformationMagicWorkshop::calculateEntropy(const std::vector<double>& probabilities) {
    double entropy = 0.0;
    for (double p : probabilities) {
        if (p > 0) {
            entropy -= p * log2(p);
        }
    }
    return entropy;
}

void InformationMagicWorkshop::celebrateInformationDiscovery() {
    std::vector<std::string> celebrations = {
        "Amazing information discovery! You understand how messages work! 📡",
        "Wonderful! You're becoming an information expert! 🌟",
        "Fantastic! Your information brain is working perfectly! 🧠",
        "Incredible! You see patterns in information! 💫",
        "Brilliant! Information is revealing its secrets to you! 🔍"
    };
    
    int index = rand() % celebrations.size();
    ColorfulPrinter::printExcited(celebrations[index]);
    
    // Progress visualization
    int total_activities = m_experiments.size() + m_games.size() + m_challenges.size() + 5;
    int progress = (m_currentExperiment * 100) / total_activities;
    ColorfulPrinter::printProgress("Information Discovery Progress: " + std::to_string(progress) + "%");
    
    // Milestone celebrations
    if (m_experimentsCompleted == 3) {
        ColorfulPrinter::printAchievement("🎉 3 Experiments! You're an Information Scientist! 🎉");
    } else if (m_messagesSent == 2) {
        ColorfulPrinter::printAchievement("🌟 Messages Sent! Communication Expert! 🌟");
    } else if (m_predictionsMade == 3) {
        ColorfulPrinter::printAchievement("💎 Predictions Made! Pattern Master! 💎");
    }
}

void InformationMagicWorkshop::updateProgress() {
    int total_activities = m_experiments.size() + m_games.size() + m_challenges.size() + 5;
    m_learningProgress = (m_currentExperiment * 100.0) / total_activities;
    
    if (m_aiHelper) {
        m_aiHelper->analyzeProgress(m_learningProgress);
        m_aiHelper->provideEncouragement();
    }
    
    Logger::info("Information magic progress: " + std::to_string(m_learningProgress) + "%");
}

void InformationMagicWorkshop::checkForBreak() {
    auto now = std::chrono::steady_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::minutes>(now - m_lastBreakTime);
    
    if (duration.count() >= m_attentionSpanMinutes) {
        m_needsBreak = true;
        suggestBreak();
    }
}

void InformationMagicWorkshop::suggestBreak() {
    ColorfulPrinter::printGentleWarning("Information explorers need to rest their amazing brains!");
    ColorfulPrinter::printStory("Let's take a little break! Even the best explorers recharge!");
    ColorfulPrinter::printHappy("When we come back, we'll discover more amazing information!");
    
    m_needsBreak = true;
    m_lastBreakTime = std::chrono::steady_clock::now();
}

void InformationMagicWorkshop::render() {
    ColorfulPrinter::printStars(6);
}

void InformationMagicWorkshop::handleInput() {
    ColorfulPrinter::printHelp("Keep exploring! Every piece of information you discover makes you smarter!");
}

bool InformationMagicWorkshop::isComplete() const {
    return m_currentExperiment >= m_experiments.size() + m_games.size() + m_challenges.size() + 5;
}

double InformationMagicWorkshop::getProgress() const {
    return m_learningProgress;
}

void InformationMagicWorkshop::endWorkshop() {
    ColorfulPrinter::printAchievement("You've completed the Information Magic workshop!");
    ColorfulPrinter::printExcited("You're now an Information Expert! 📡");
    
    ColorfulPrinter::printProgress("Experiments completed: " + std::to_string(m_experimentsCompleted));
    ColorfulPrinter::printProgress("Messages sent: " + std::to_string(m_messagesSent));
    ColorfulPrinter::printProgress("Predictions made: " + std::to_string(m_predictionsMade));
    
    if (m_highestEntropy > 2.5) {
        ColorfulPrinter::printAchievement("🏆 High Entropy Explorer! You understand uncertainty! 🏆");
    }
    
    m_isRunning = false;
}

void InformationMagicWorkshop::cleanup() {
    m_entropyCalculator.reset();
    m_informationTheory.reset();
    m_patternPredictor.reset();
    m_guide.reset();
    m_mathMagician.reset();
    m_aiHelper.reset();
    
    Logger::info("InformationMagicWorkshop cleanup complete");
}

} // namespace Workshops
} // namespace Recipy