/*
 * NumberGamesWorkshop.cpp - Making Mathematics Fun Through Games
 */

#include "workshops/NumberGamesWorkshop.h"
#include "utils/Logger.h"
#include "utils/ColorfulPrinter.h"
#include <iostream>
#include <vector>
#include <random>
#include <algorithm>

namespace Recipy {
namespace Workshops {

NumberGamesWorkshop::NumberGamesWorkshop()
    : m_isRunning(false)
    , m_currentGame(0)
    , m_gamesPlayed(0)
    , m_challengesCompleted(0)
    , m_achievementsUnlocked(0)
    , m_learningProgress(0.0)
    , m_needsBreak(false)
    , m_attentionSpanMinutes(15)
    , m_currentDifficulty(0.1)
    , m_highestScore(0)
    , m_averageAccuracy(0.0) {
    
    Logger::info("NumberGamesWorkshop constructor - Creating mathematical games adventure!");
    m_startTime = std::chrono::steady_clock::now();
    m_lastBreakTime = m_startTime;
}

NumberGamesWorkshop::~NumberGamesWorkshop() {
    cleanup();
}

bool NumberGamesWorkshop::initialize() {
    Logger::info("Initializing Number Games workshop...");
    
    try {
        ColorfulPrinter::printRainbow("🎮 Welcome to Number Games! 🎮");
        ColorfulPrinter::printExcited("Let's learn mathematics through fun and engaging games!");
        
        if (!initializeComponents()) {
            ColorfulPrinter::printSad("The game boards wouldn't set up.");
            return false;
        }
        
        initializeMathGames();
        
        ColorfulPrinter::printHappy("All mathematical games are ready to play!");
        return true;
    } catch (...) {
        return false;
    }
}

bool NumberGamesWorkshop::initializeComponents() {
    try {
        m_guide = std::make_unique<Characters::FriendlyGuide>();
        m_mathMagician = std::make_unique<Characters::MathMagician>();
        m_aiHelper = std::make_unique<AI::ChildAIHelper>();
        m_gameEngine = std::make_unique<Math::GameEngine>();
        m_mathPuzzles = std::make_unique<Math::MathPuzzles>();
        m_numberGames = std::make_unique<Math::NumberGames>();
        
        ColorfulPrinter::printHappy("Game engine is ready!");
        return true;
    } catch (...) {
        return false;
    }
}

void NumberGamesWorkshop::initializeMathGames() {
    Logger::info("Creating mathematical games and challenges...");
    
    // Create different types of games
    createCountingGames();
    createPatternGames();
    createStrategyGames();
    createProbabilityGames();
    createGeometryGames();
    createSpeedGames();
    createMemoryGames();
    createAdvancedGames();
    
    // Initialize challenges and achievements
    initializeGameChallenges();
    initializeAchievements();
    
    ColorfulPrinter::printLearning("Created " + std::to_string(m_games.size()) + " mathematical games!");
}

void NumberGamesWorkshop::createCountingGames() {
    // Number Bingo
    MathGame bingo;
    bingo.id = 1;
    bingo.game_name = "Number Bingo";
    bingo.description = "Mark numbers as they're called to make patterns";
    bingo.learning_objective = "Number recognition and listening skills";
    bingo.materials_needed = {"Bingo cards", "Number caller", "Markers"};
    bingo.difficulty_level = 1;
    bingo.players_count = 2;
    bingo.game_type = "Recognition";
    bingo.competitive = false;
    m_games.push_back(bingo);
    
    // Counting Race
    MathGame countingRace;
    countingRace.id = 2;
    countingRace.game_name = "Counting Race";
    countingRace.description = "Race to count objects correctly";
    countingRace.learning_objective = "Counting accuracy and speed";
    countingRace.materials_needed = {"Objects to count", "Timer", "Score sheet"};
    countingRace.difficulty_level = 1;
    countingRace.players_count = 4;
    countingRace.game_type = "Speed";
    countingRace.competitive = true;
    m_games.push_back(countingRace);
    
    // Skip Counting Jump
    MathGame skipCounting;
    skipCounting.id = 3;
    skipCounting.game_name = "Skip Counting Jump";
    skipCounting.description = "Jump while counting by 2s, 5s, or 10s";
    skipCounting.learning_objective = "Skip counting and motor skills";
    skipCounting.materials_needed = {"Open space", "Music", "Number cards"};
    skipCounting.difficulty_level = 2;
    skipCounting.players_count = 6;
    skipCounting.game_type = "Physical";
    skipCounting.competitive = false;
    m_games.push_back(skipCounting);
}

void NumberGamesWorkshop::createPatternGames() {
    // Pattern Master
    MathGame patternMaster;
    patternMaster.id = 4;
    patternMaster.game_name = "Pattern Master";
    patternMaster.description = "Complete and create number patterns";
    patternMaster.learning_objective = "Pattern recognition and creation";
    patternMaster.materials_needed = {"Pattern cards", "Blank cards", "Markers"};
    patternMaster.difficulty_level = 2;
    patternMaster.players_count = 3;
    patternMaster.game_type = "Logic";
    patternMaster.competitive = false;
    m_games.push_back(patternMaster);
    
    // Sequence Builder
    MathGame sequenceBuilder;
    sequenceBuilder.id = 5;
    sequenceBuilder.game_name = "Sequence Builder";
    sequenceBuilder.description = "Build mathematical sequences correctly";
    sequenceBuilder.learning_objective = "Understanding mathematical sequences";
    sequenceBuilder.materials_needed = {"Number tiles", "Sequence templates", "Timer"};
    sequenceBuilder.difficulty_level = 3;
    sequenceBuilder.players_count = 2;
    sequenceBuilder.game_type = "Construction";
    sequenceBuilder.competitive = true;
    m_games.push_back(sequenceBuilder);
}

void NumberGamesWorkshop::createStrategyGames() {
    // Math War
    MathGame mathWar;
    mathWar.id = 6;
    mathWar.game_name = "Math War";
    mathWar.description = "Battle with math facts to win cards";
    mathWar.learning_objective = "Math fact fluency and quick thinking";
    mathWar.materials_needed = {"Playing cards with numbers", "Math operation cards"};
    mathWar.difficulty_level = 2;
    mathWar.players_count = 2;
    mathWar.game_type = "Strategy";
    mathWar.competitive = true;
    m_games.push_back(mathWar);
    
    // Number Tic-Tac-Toe
    MathGame numberTicTacToe;
    numberTicTacToe.id = 7;
    numberTicTacToe.game_name = "Number Tic-Tac-Toe";
    numberTicTacToe.description = "Get three in a row using number operations";
    numberTicTacToe.learning_objective = "Strategic thinking with numbers";
    numberTicTacToe.materials_needed = {"Grid board", "Number tokens", "Operation cards"};
    numberTicTacToe.difficulty_level = 3;
    numberTicTacToe.players_count = 2;
    numberTicTacToe.game_type = "Strategy";
    numberTicTacToe.competitive = true;
    m_games.push_back(numberTicTacToe);
}

void NumberGamesWorkshop::createProbabilityGames() {
    // Probability Wheel
    MathGame probabilityWheel;
    probabilityWheel.id = 8;
    probabilityWheel.game_name = "Probability Wheel";
    probabilityWheel.description = "Spin the wheel and predict outcomes";
    probabilityWheel.learning_objective = "Understanding probability and chance";
    probabilityWheel.materials_needed = {"Spinning wheel", "Prediction cards", "Score tokens"};
    probabilityWheel.difficulty_level = 3;
    probabilityWheel.players_count = 4;
    probabilityWheel.game_type = "Probability";
    probabilityWheel.competitive = true;
    m_games.push_back(probabilityWheel);
    
    // Dice Probability
    MathGame diceProbability;
    diceProbability.id = 9;
    diceProbability.game_name = "Dice Probability";
    diceProbability.description = "Predict and test dice roll outcomes";
    diceProbability.learning_objective = "Experimental probability";
    diceProbability.materials_needed = {"Dice", "Prediction sheets", "Recording charts"};
    diceProbability.difficulty_level = 2;
    diceProbability.players_count = 3;
    diceProbability.game_type = "Probability";
    diceProbability.competitive = false;
    m_games.push_back(diceProbability);
}

void NumberGamesWorkshop::createGeometryGames() {
    // Shape Sorter
    MathGame shapeSorter;
    shapeSorter.id = 10;
    shapeSorter.game_name = "Shape Sorter Race";
    shapeSorter.description = "Sort shapes quickly and accurately";
    shapeSorter.learning_objective = "Shape recognition and classification";
    shapeSorter.materials_needed = {"Various shapes", "Sorting containers", "Timer"};
    shapeSorter.difficulty_level = 1;
    shapeSorter.players_count = 4;
    shapeSorter.game_type = "Geometry";
    shapeSorter.competitive = true;
    m_games.push_back(shapeSorter);
    
    // Geometry Tangram
    MathGame tangram;
    tangram.id = 11;
    tangram.game_name = "Geometry Tangram";
    tangram.description = "Create shapes using geometric pieces";
    tangram.learning_objective = "Spatial reasoning and geometry";
    tangram.materials_needed = {"Tangram pieces", "Shape templates", "Timer"};
    tangram.difficulty_level = 3;
    tangram.players_count = 2;
    tangram.game_type = "Spatial";
    tangram.competitive = false;
    m_games.push_back(tangram);
}

void NumberGamesWorkshop::createSpeedGames() {
    // Quick Calc
    MathGame quickCalc;
    quickCalc.id = 12;
    quickCalc.game_name = "Quick Calculation";
    quickCalc.description = "Solve math problems as fast as possible";
    quickCalc.learning_objective = "Mental math speed and accuracy";
    quickCalc.materials_needed = {"Problem cards", "Timer", "Answer sheets"};
    quickCalc.difficulty_level = 2;
    quickCalc.players_count = 4;
    quickCalc.game_type = "Speed";
    quickCalc.competitive = true;
    m_games.push_back(quickCalc);
    
    // Number Dash
    MathGame numberDash;
    numberDash.id = 13;
    numberDash.game_name = "Number Dash";
    numberDash.description = "Run to the correct number when called";
    numberDash.learning_objective = "Number recognition and physical activity";
    numberDash.materials_needed = {"Number cards spread out", "Open space", "Caller"};
    numberDash.difficulty_level = 1;
    numberDash.players_count = 8;
    numberDash.game_type = "Physical";
    numberDash.competitive = true;
    m_games.push_back(numberDash);
}

void NumberGamesWorkshop::createMemoryGames() {
    // Math Memory
    MathGame mathMemory;
    mathMemory.id = 14;
    mathMemory.game_name = "Math Memory";
    mathMemory.description = "Match math problems with answers";
    mathMemory.learning_objective = "Memory and math fact recall";
    mathMemory.materials_needed = {"Memory cards with problems and answers"};
    mathMemory.difficulty_level = 1;
    mathMemory.players_count = 2;
    mathMemory.game_type = "Memory";
    mathMemory.competitive = true;
    m_games.push_back(mathMemory);
    
    // Number Sequence Memory
    MathGame sequenceMemory;
    sequenceMemory.id = 15;
    sequenceMemory.game_name = "Number Sequence Memory";
    sequenceMemory.description = "Remember and repeat number sequences";
    sequenceMemory.learning_objective = "Working memory and pattern recognition";
    sequenceMemory.materials_needed = {"Number cards", "Sequence display", "Timer"};
    sequenceMemory.difficulty_level = 2;
    sequenceMemory.players_count = 3;
    sequenceMemory.game_type = "Memory";
    sequenceMemory.competitive = false;
    m_games.push_back(sequenceMemory);
}

void NumberGamesWorkshop::createAdvancedGames() {
    // Fraction Pizza
    MathGame fractionPizza;
    fractionPizza.id = 16;
    fractionPizza.game_name = "Fraction Pizza Party";
    fractionPizza.description = "Create and compare fraction pizzas";
    fractionPizza.learning_objective = "Understanding fractions and comparison";
    fractionPizza.materials_needed = {"Pizza cutouts", "Fraction cards", "Comparison tools"};
    fractionPizza.difficulty_level = 3;
    fractionPizza.players_count = 4;
    fractionPizza.game_type = "Fractions";
    fractionPizza.competitive = false;
    m_games.push_back(fractionPizza);
    
    // Math Scavenger Hunt
    MathGame scavengerHunt;
    scavengerHunt.id = 17;
    scavengerHunt.game_name = "Math Scavenger Hunt";
    scavengerHunt.description = "Find and solve math problems around the room";
    scavengerHunt.learning_objective = "Problem-solving and exploration";
    scavengerHunt.materials_needed = {"Problem stations", "Answer sheets", "Clue cards"};
    scavengerHunt.difficulty_level = 2;
    scavengerHunt.players_count = 6;
    scavengerHunt.game_type = "Exploration";
    scavengerHunt.competitive = true;
    m_games.push_back(scavengerHunt);
}

void NumberGamesWorkshop::initializeGameChallenges() {
    // Speed Challenge
    GameChallenge speedChallenge;
    speedChallenge.id = 1;
    speedChallenge.challenge_name = "Lightning Calculator";
    speedChallenge.game_reference = "Quick Calculation";
    speedChallenge.challenge_description = "Solve 20 problems in under 2 minutes";
    speedChallenge.success_criteria = "90% accuracy within time limit";
    speedChallenge.time_limit_seconds = 120;
    speedChallenge.hints = {"Practice mental math", "Start with easier problems"};
    speedChallenge.solution_approach = "Build speed through repeated practice";
    m_challenges.push_back(speedChallenge);
    
    // Accuracy Challenge
    GameChallenge accuracyChallenge;
    accuracyChallenge.id = 2;
    accuracyChallenge.challenge_name = "Perfect Score";
    accuracyChallenge.game_reference = "Math Memory";
    accuracyChallenge.challenge_description = "Complete a game with 100% accuracy";
    accuracyChallenge.success_criteria = "No mistakes throughout the game";
    accuracyChallenge.time_limit_seconds = 300;
    accuracyChallenge.hints = {"Take your time", "Double-check before answering"};
    accuracyChallenge.solution_approach = "Focus on accuracy over speed";
    m_challenges.push_back(accuracyChallenge);
    
    // Strategy Challenge
    GameChallenge strategyChallenge;
    strategyChallenge.id = 3;
    strategyChallenge.challenge_name = "Strategic Master";
    strategyChallenge.game_reference = "Math War";
    strategyChallenge.challenge_description = "Win 5 games in a row using different strategies";
    strategyChallenge.success_criteria = "5 consecutive wins with varied approaches";
    strategyChallenge.time_limit_seconds = 600;
    strategyChallenge.hints = {"Plan ahead", "Adapt to opponent's strategy"};
    strategyChallenge.solution_approach = "Think multiple moves ahead";
    m_challenges.push_back(strategyChallenge);
}

void NumberGamesWorkshop::initializeAchievements() {
    // First Game Achievement
    Achievement firstGame;
    firstGame.id = 1;
    firstGame.achievement_name = "Game Starter";
    firstGame.description = "Play your first mathematical game";
    firstGame.unlock_condition = "Complete first game";
    firstGame.unlocked = false;
    firstGame.icon = "🎮";
    m_achievements.push_back(firstGame);
    
    // Speed Achievement
    Achievement speedMaster;
    speedMaster.id = 2;
    speedMaster.achievement_name = "Speed Demon";
    speedMaster.description = "Complete a speed game in record time";
    speedMaster.unlock_condition = "Beat time limit in speed game";
    speedMaster.unlocked = false;
    speedMaster.icon = "⚡";
    m_achievements.push_back(speedMaster);
    
    // Accuracy Achievement
    Achievement accuracyMaster;
    accuracyMaster.id = 3;
    accuracyMaster.achievement_name = "Perfect Accuracy";
    accuracyMaster.description = "Complete any game with 100% accuracy";
    accuracyMaster.unlock_condition = "Achieve perfect score";
    accuracyMaster.unlocked = false;
    accuracyMaster.icon = "🎯";
    m_achievements.push_back(accuracyMaster);
    
    // Variety Achievement
    Achievement varietyMaster;
    varietyMaster.id = 4;
    varietyMaster.achievement_name = "Game Explorer";
    varietyMaster.description = "Play 5 different types of games";
    varietyMaster.unlock_condition = "Complete 5 different game types";
    varietyMaster.unlocked = false;
    varietyMaster.icon = "🗺️";
    m_achievements.push_back(varietyMaster);
    
    // Mastery Achievement
    Achievement masteryMaster;
    masteryMaster.id = 5;
    masteryMaster.achievement_name = "Game Master";
    masteryMaster.description = "Master 10 different games";
    masteryMaster.unlock_condition = "Achieve high scores in 10 games";
    masteryMaster.unlocked = false;
    masteryMaster.icon = "👑";
    m_achievements.push_back(masteryMaster);
}

void NumberGamesWorkshop::start() {
    Logger::info("Starting Number Games workshop...");
    
    if (m_guide) {
        m_guide->sayHello();
        m_guide->explainAdventure();
    }
    
    introduceWorkshop();
    
    m_currentGame = 0;
    m_isRunning = true;
    
    ColorfulPrinter::printExcited("Let's play and learn mathematics together!");
}

void NumberGamesWorkshop::introduceWorkshop() {
    ColorfulPrinter::printStory("Welcome, Game Player! Today we'll learn math through fun games!");
    
    if (m_mathMagician) {
        m_mathMagician->performMagic();
        ColorfulPrinter::printExcited("Games make learning mathematics exciting and memorable!");
    }
    
    ColorfulPrinter->printHappy("Every game teaches us something new about numbers!");
    ColorfulPrinter->printExcited("We'll play counting games, pattern games, strategy games, and more!");
    
    playCountingGames();
}

void NumberGamesWorkshop::playCountingGames() {
    ColorfulPrinter->printLearning("Let's start with fun counting games!");
    
    ColorfulPrinter->printNumber("Counting Games We'll Play:");
    ColorablePrinter->printNumber("• Number Bingo - Listen for numbers and mark them");
    ColorablePrinter->printNumber("• Counting Race - Count objects quickly");
    ColorablePrinter->printNumber("• Skip Counting Jump - Count by 2s, 5s, 10s while jumping");
    
    ColorablePrinter->printExcited("Counting games help us recognize numbers instantly!");
    
    // Quick demo of Number Bingo
    playNumberBingo();
    
    ColorablePrinter->printAchievement("You're ready to be a Mathematical Game Player! 🎮✨");
}

void NumberGamesWorkshop::playNumberBingo() {
    ColorablePrinter->printExcited("Let's play Number Bingo!");
    
    ColorablePrinter->printNumber("Game Setup:");
    ColorablePrinter->printNumber("• Each player gets a bingo card with numbers");
    ColorablePrinter->printNumber("• Caller announces random numbers");
    ColorablePrinter->printNumber("• Mark the numbers on your card");
    ColorablePrinter->printNumber("• First to complete a pattern wins!");
    
    // Simulate a few rounds
    ColorablePrinter->printWithDots("Calling numbers");
    std::vector<std::string> calledNumbers = {"7", "15", "23", "8", "12"};
    
    for (const auto& number : calledNumbers) {
        ColorablePrinter->printExcited("Number " + number + "!");
        ColorablePrinter->printHappy("Mark it if you have it!");
    }
    
    ColorablePrinter->printAchievement("Great job listening and marking! 🎯");
}

void NumberGamesWorkshop::update() {
    if (!m_isRunning) return;
    
    if (m_needsBreak) {
        std::this_thread::sleep_for(std::chrono::minutes(2));
        m_needsBreak = false;
        ColorablePrinter->printExcited("Welcome back, Game Player!");
    }
    
    if (m_currentGame < m_games.size()) {
        playGame(m_games[m_currentGame]);
        m_currentGame++;
        updateProgress();
        checkForBreak();
    } else if (m_currentGame < m_games.size() + m_challenges.size()) {
        completeChallenge(m_challenges[m_currentGame - m_games.size()]);
        m_currentGame++;
        updateProgress();
        checkForBreak();
    } else {
        exploreAdvancedGaming();
        if (m_currentGame >= m_games.size() + m_challenges.size() + 5) {
            endWorkshop();
        }
    }
}

void NumberGamesWorkshop::playGame(const MathGame& game) {
    ColorablePrinter->printExcited("Game Time: " + game.game_name);
    ColorablePrinter->printLearning(game.description);
    ColorablePrinter->printNumber("Learning: " + game.learning_objective);
    
    // Show game setup
    ColorablePrinter->printNumber("Materials Needed:");
    for (const auto& material : game.materials_needed) {
        ColorablePrinter->printNumber("• " + material);
    }
    
    ColorablePrinter->printNumber("Players: " + std::to_string(game.players_count));
    ColorablePrinter->printNumber("Type: " + game.game_type);
    ColorablePrinter->printNumber("Difficulty: " + std::string(game.difficulty_level, '⭐'));
    
    // Play the specific game
    if (game.game_name == "Number Bingo") {
        playNumberBingo();
    } else if (game.game_name == "Math Memory") {
        playMathMemory();
    } else if (game.game_name == "Pattern Master") {
        playPatternMaster();
    } else if (game.game_name == "Quick Calculation") {
        playQuickCalc();
    } else if (game.game_name == "Shape Sorter Race") {
        playShapeSorter();
    } else if (game.game_name == "Probability Wheel") {
        playProbabilityWheel();
    } else if (game.game_name == "Sequence Builder") {
        playSequenceBuilder();
    } else if (game.game_name == "Math Scavenger Hunt") {
        playMathScavengerHunt();
    } else if (game.game_name == "Math War") {
        playMultiplicationWar();
    } else if (game.game_name == "Fraction Pizza Party") {
        playFractionPizza();
    } else if (game.game_name == "Geometry Tangram") {
        playGeometryTangram();
    } else {
        simulateGameplay(game);
    }
    
    m_gamesPlayed++;
    
    // Track high score and progress
    int score = simulateGameScore(game);
    double accuracy = simulateGameAccuracy(game);
    trackGameProgress(game.game_name, score, accuracy);
    
    checkAchievements();
    celebrateGamingSuccess();
}

void NumberGamesWorkshop::playMathMemory() {
    ColorablePrinter->printExcited("Let's play Math Memory!");
    
    ColorablePrinter->printNumber("Game Rules:");
    ColorablePrinter->printNumber("• Cards face down in a grid");
    ColorablePrinter->printNumber("• Each card has either a problem or answer");
    ColorablePrinter->printNumber("• Flip two cards per turn");
    ColorablePrinter->printNumber("• Match problems with correct answers");
    ColorablePrinter->printNumber("• Player with most pairs wins!");
    
    // Simulate game
    ColorablePrinter->printWithDots("Flipping cards");
    std::vector<std::string> matches = {"2+3 = 5", "4×2 = 8", "10-3 = 7"};
    
    for (const auto& match : matches) {
        ColorablePrinter->printExcited("Match found: " + match);
        ColorablePrinter->printHappy("Great memory!");
    }
    
    ColorablePrinter->printAchievement("Memory master! 🧠✨");
}

void NumberGamesWorkshop::playPatternMaster() {
    ColorablePrinter->printExcited("Let's play Pattern Master!");
    
    ColorablePrinter->printNumber("Pattern Challenge 1:");
    ColorablePrinter->printNumber("2, 4, 6, 8, ?");
    ColorablePrinter->printThinking("What comes next?");
    ColorablePrinter->printExcited("10! You added 2 each time!");
    
    ColorablePrinter->printNumber("Pattern Challenge 2:");
    ColorablePrinter->printNumber("1, 1, 2, 3, 5, ?");
    ColorablePrinter->printThinking("This is trickier!");
    ColorablePrinter->printExcited("8! Fibonacci sequence!");
    
    ColorablePrinter->printAchievement("Pattern detective! 🔍✨");
}

void NumberGamesWorkshop::playQuickCalc() {
    ColorablePrinter->printExcited("Let's play Quick Calculation!");
    
    std::vector<std::string> problems = {
        "5 + 3 = ?",
        "12 - 4 = ?",
        "6 × 2 = ?",
        "15 ÷ 3 = ?"
    };
    
    ColorablePrinter->printWithDots("Solving problems quickly");
    
    for (const auto& problem : problems) {
        ColorablePrinter->printNumber(problem);
        ColorablePrinter->printThinking("Quick calculation!");
        ColorablePrinter->printHappy("Correct! Speed + accuracy!");
    }
    
    ColorablePrinter->printAchievement("Mental math champion! ⚡✨");
}

void NumberGamesWorkshop::playShapeSorter() {
    ColorablePrinter->printExcited("Let's play Shape Sorter Race!");
    
    ColorablePrinter->printNumber("Shapes to sort:");
    ColorablePrinter->printNumber("• Circles - Put in the round basket");
    ColorablePrinter->printNumber("• Squares - Put in the square basket");
    ColorablePrinter->printNumber("• Triangles - Put in the triangle basket");
    
    ColorablePrinter->printWithDots("Sorting shapes quickly");
    
    ColorablePrinter->printNumber("Circle → Round basket ✓");
    ColorablePrinter->printNumber("Square → Square basket ✓");
    ColorablePrinter->printNumber("Triangle → Triangle basket ✓");
    
    ColorablePrinter->printAchievement("Shape sorting expert! 🔷✨");
}

void NumberGamesWorkshop::playProbabilityWheel() {
    ColorablePrinter->printExcited("Let's play Probability Wheel!");
    
    ColorablePrinter->printNumber("Wheel sections:");
    ColorablePrinter->printNumber("• Red (1/4 chance)");
    ColorablePrinter->printNumber("• Blue (1/4 chance)");
    ColorablePrinter->printNumber("• Green (1/4 chance)");
    ColorablePrinter->printNumber("• Yellow (1/4 chance)");
    
    ColorablePrinter->printWithDots("Spinning the wheel");
    
    ColorablePrinter->printNumber("Which color will it land on?");
    ColorablePrinter->printExcited("It landed on Green!");
    ColorablePrinter->printHappy("Sometimes we guess right, sometimes not - that's probability!");
    
    ColorablePrinter->printAchievement("Probability predictor! 🎯✨");
}

void NumberGamesWorkshop::playSequenceBuilder() {
    ColorablePrinter->printExcited("Let's play Sequence Builder!");
    
    ColorablePrinter->printNumber("Build the Fibonacci sequence:");
    ColorablePrinter->printNumber("1, 1, 2, 3, 5, 8, ?");
    ColorablePrinter->printThinking("What's the next number?");
    ColorablePrinter->printExcited("13! 5 + 8 = 13!");
    
    ColorablePrinter->printNumber("Build square numbers:");
    ColorablePrinter->printNumber("1, 4, 9, 16, ?");
    ColorablePrinter->printThinking("What's the pattern?");
    ColorablePrinter->printExcited("25! 5 × 5 = 25!");
    
    ColorablePrinter->printAchievement("Sequence builder! 🔢✨");
}

void NumberGamesWorkshop::playMathScavengerHunt() {
    ColorablePrinter->printExcited("Let's play Math Scavenger Hunt!");
    
    ColorablePrinter->printNumber("Find and solve:");
    ColorablePrinter->printNumber("• Station 1: Count the windows");
    ColorablePrinter->printNumber("• Station 2: Measure the table");
    ColorablePrinter->printNumber("• Station 3: Find shapes in the room");
    
    ColorablePrinter->printWithDots("Hunting for math problems");
    
    ColorablePrinter->printNumber("Found 6 windows!");
    ColorablePrinter->printNumber("Table is 120 cm long!");
    ColorablePrinter->printNumber("Found circles, squares, and rectangles!");
    
    ColorablePrinter->printAchievement("Math explorer! 🔍✨");
}

void NumberGamesWorkshop::playMultiplicationWar() {
    ColorablePrinter->printExcited("Let's play Math War!");
    
    ColorablePrinter->printNumber("Battle Round:");
    ColorablePrinter->printNumber("Player 1: 7 × 6 = ?");
    ColorablePrinter->printNumber("Player 2: 8 × 5 = ?");
    
    ColorablePrinter->printWithDots("Quick calculations");
    
    ColorablePrinter->printNumber("Player 1: 7 × 6 = 42");
    ColorablePrinter->printNumber("Player 2: 8 × 5 = 40");
    ColorablePrinter->printExcited("Player 1 wins this round!");
    
    ColorablePrinter->printAchievement("Math warrior! ⚔️✨");
}

void NumberGamesWorkshop::playFractionPizza() {
    ColorablePrinter->printExcited("Let's play Fraction Pizza Party!");
    
    ColorablePrinter->printNumber("Pizza fractions:");
    ColorablePrinter->printNumber("• Cut pizza into 8 slices = 8/8 = 1 whole pizza");
    ColorablePrinter->printNumber("• Eat 2 slices = 6/8 = 3/4 pizza left");
    ColorablePrinter->printNumber("• Share 1 slice = 5/8 pizza left");
    
    ColorablePrinter->printWithDots("Making fraction comparisons");
    
    ColorablePrinter->printNumber("3/4 > 1/2");
    ColorablePrinter->printNumber("5/8 < 3/4");
    ColorablePrinter->printExcited("Fractions help us share fairly!");
    
    ColorablePrinter->printAchievement("Fraction chef! 🍕✨");
}

void NumberGamesWorkshop::playGeometryTangram() {
    ColorablePrinter->printExcited("Let's play Geometry Tangram!");
    
    ColorablePrinter->printNumber("Tangram pieces:");
    ColorablePrinter->printNumber("• 2 large triangles");
    ColorablePrinter->printNumber("• 1 medium triangle");
    ColorablePrinter->printNumber("• 2 small triangles");
    ColorablePrinter->printNumber("• 1 square");
    ColorablePrinter->printNumber("• 1 parallelogram");
    
    ColorablePrinter->printWithDots("Creating shapes with pieces");
    
    ColorablePrinter->printNumber("Made a house using 5 pieces!");
    ColorablePrinter->printNumber("Made a cat using 6 pieces!");
    ColorablePrinter->printNumber("Made a boat using all 7 pieces!");
    
    ColorablePrinter->printAchievement("Tangram artist! 🎨✨");
}

void NumberGamesWorkshop::simulateGameplay(const MathGame& game) {
    ColorablePrinter->printNumber("Playing " + game.game_name + "...");
    ColorablePrinter->printWithDots("Game in progress");
    
    ColorablePrinter->printHappy("Great job playing " + game.game_name + "!");
    ColorablePrinter->printExcited("You learned: " + game.learning_objective);
}

int NumberGamesWorkshop::simulateGameScore(const MathGame& game) {
    // Simulate a score based on game type and difficulty
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> dis(50, 100);
    
    int base_score = dis(gen);
    int difficulty_bonus = game.difficulty_level * 10;
    
    return std::min(base_score + difficulty_bonus, 100);
}

double NumberGamesWorkshop::simulateGameAccuracy(const MathGame& game) {
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_real_distribution<> dis(0.7, 1.0);
    
    return dis(gen);
}

void NumberGamesWorkshop::trackGameProgress(const std::string& game_name, int score, double accuracy) {
    m_highScores[game_name] = score;
    
    if (score > m_highestScore) {
        m_highestScore = score;
        m_bestGame = game_name;
    }
    
    // Update average accuracy
    if (m_gamesPlayed == 1) {
        m_averageAccuracy = accuracy;
    } else {
        m_averageAccuracy = (m_averageAccuracy * (m_gamesPlayed - 1) + accuracy) / m_gamesPlayed;
    }
}

void NumberGamesWorkshop::completeChallenge(const GameChallenge& challenge) {
    ColorablePrinter->printExcited("Challenge: " + challenge.challenge_name);
    ColorablePrinter->printNumber("From Game: " + challenge.game_reference);
    ColorablePrinter->printNumber(challenge.challenge_description);
    ColorablePrinter->printNumber("Success Criteria: " + challenge.success_criteria);
    ColorablePrinter->printNumber("Time Limit: " + std::to_string(challenge.time_limit_seconds) + " seconds");
    
    ColorablePrinter->printWithDots("Attempting challenge");
    
    ColorablePrinter->printExcited("Challenge completed!");
    ColorablePrinter->printHappy("Approach: " + challenge.solution_approach);
    
    m_challengesCompleted++;
    celebrateGamingSuccess();
}

void NumberGamesWorkshop::exploreAdvancedGaming() {
    int game_index = m_currentGame - m_games.size() - m_challenges.size();
    
    switch (game_index) {
        case 0:
            exploreGameTheory();
            break;
        case 1:
            exploreProbabilityInGames();
            break;
        case 2:
            exploreStrategyAndLogic();
            break;
        case 3:
            playCooperativeGames();
            break;
        case 4:
            createOwnGame();
            break;
    }
    
    m_currentGame++;
}

void NumberGamesWorkshop::exploreGameTheory() {
    ColorablePrinter->printLearning("Let's explore game theory - why games work!");
    
    ColorablePrinter->printNumber("Game Theory Concepts:");
    ColorablePrinter->printNumber("• Strategy affects outcomes");
    ColorablePrinter->printNumber("• Some games have guaranteed wins");
    ColorablePrinter->printNumber("• Others involve probability");
    ColorablePrinter->printNumber("• Cooperation vs competition");
    
    ColorablePrinter->printExcited("Understanding games helps us make better decisions!");
    
    ColorablePrinter->printAchievement("Game theory expert! 🧠✨");
}

void NumberGamesWorkshop::exploreProbabilityInGames() {
    ColorablePrinter->printLearning("Let's understand probability in games!");
    
    ColorablePrinter->printNumber("Probability in Games:");
    ColorablePrinter->printNumber("• Dice rolls: Each number has 1/6 chance");
    ColorablePrinter->printNumber("• Card draws: Depends on remaining cards");
    ColorablePrinter->printNumber("• Coin flips: 50/50 chance each way");
    ColorablePrinter->printNumber("• Spinner games: Depends on spinner sections");
    
    ColorablePrinter->printExcited("Probability helps us predict and understand chance!");
    
    ColorablePrinter->printAchievement("Probability master! 🎯✨");
}

void NumberGamesWorkshop::exploreStrategyAndLogic() {
    ColorablePrinter->printLearning("Let's master strategy and logic in games!");
    
    ColorablePrinter->printNumber("Strategic Thinking:");
    ColorablePrinter->printNumber("• Plan ahead multiple moves");
    ColorablePrinter->printNumber("• Consider opponent's possible moves");
    ColorablePrinter->printNumber("• Look for winning patterns");
    ColorablePrinter->printNumber("• Adapt your strategy as needed");
    
    ColorablePrinter->printExcited("Strategic thinking helps in games and life!");
    
    ColorablePrinter->printAchievement("Strategic master! ♟️✨");
}

void NumberGamesWorkshop::playCooperativeGames() {
    ColorablePrinter->printLearning("Let's play cooperative games where everyone wins!");
    
    ColorablePrinter->printNumber("Cooperative Math Games:");
    ColorablePrinter->printNumber("• Team counting challenges");
    ColorablePrinter->printNumber("• Group pattern building");
    ColorablePrinter->printNumber("• Collaborative problem solving");
    ColorablePrinter->printNumber("• Shared success celebrations");
    
    ColorablePrinter->printExcited("Cooperation makes learning fun for everyone!");
    
    ColorablePrinter->printAchievement("Team player! 🤝✨");
}

void NumberGamesWorkshop::createOwnGame() {
    ColorablePrinter->printExcited("Let's create your own mathematical game!");
    
    ColorablePrinter->printNumber("Game Design Steps:");
    ColorablePrinter->printNumber("1. Choose what math skill to teach");
    ColorablePrinter->printNumber("2. Decide how players will play");
    ColorablePrinter->printNumber("3. Make rules clear and fun");
    ColorablePrinter->printNumber("4. Test your game with friends");
    ColorablePrinter->printNumber("5. Make improvements based on feedback");
    
    std::string gameName = "My Math Game " + std::to_string(m_createdGames.size() + 1);
    m_createdGames.push_back(gameName);
    
    ColorablePrinter->printAchievement("Game designer! 🎮✨");
}

void NumberGamesWorkshop::checkAchievements() {
    // Check for first game
    if (m_gamesPlayed == 1 && !m_achievements[0].unlocked) {
        unlockAchievement("Game Starter");
    }
    
    // Check for speed achievement
    if (m_highestScore >= 90 && !m_achievements[1].unlocked) {
        unlockAchievement("Speed Demon");
    }
    
    // Check for accuracy achievement
    if (m_averageAccuracy >= 0.95 && !m_achievements[2].unlocked) {
        unlockAchievement("Perfect Accuracy");
    }
    
    // Check for variety achievement
    if (m_gamesPlayed >= 5 && !m_achievements[3].unlocked) {
        unlockAchievement("Game Explorer");
    }
    
    // Check for mastery achievement
    if (m_gamesPlayed >= 10 && m_highestScore >= 85 && !m_achievements[4].unlocked) {
        unlockAchievement("Game Master");
    }
}

void NumberGamesWorkshop::unlockAchievement(const std::string& achievement_name) {
    for (auto& achievement : m_achievements) {
        if (achievement.achievement_name == achievement_name && !achievement.unlocked) {
            achievement.unlocked = true;
            m_achievementsUnlocked++;
            celebrateAchievement(achievement);
            break;
        }
    }
}

void NumberGamesWorkshop::celebrateAchievement(const Achievement& achievement) {
    ColorablePrinter->printExcited("🎉 ACHIEVEMENT UNLOCKED! 🎉");
    ColorablePrinter->printNumber(achievement.icon + " " + achievement.achievement_name);
    ColorablePrinter->printHappy(achievement.description);
    ColorablePrinter->printAchievement("Total Achievements: " + std::to_string(m_achievementsUnlocked) + "/" + std::to_string(m_achievements.size()));
}

void NumberGamesWorkshop::celebrateGamingSuccess() {
    std::vector<std::string> celebrations = {
        "Amazing game! You're learning while having fun! 🎮",
        "Wonderful! Mathematics is exciting through games! 🌟",
        "Fantastic! Your gaming skills are improving! 🏆",
        "Incredible! You're mastering mathematical concepts! 🎯",
        "Brilliant! Games make learning unforgettable! ✨"
    };
    
    int index = rand() % celebrations.size();
    ColorablePrinter->printExcited(celebrations[index]);
    
    // Progress visualization
    int total_activities = m_games.size() + m_challenges.size() + 5;
    int progress = (m_currentGame * 100) / total_activities;
    ColorablePrinter->printProgress("Game Learning Progress: " + std::to_string(progress) + "%");
    
    // Score and achievement display
    ColorablePrinter->printProgress("Games Played: " + std::to_string(m_gamesPlayed));
    ColorablePrinter->printProgress("Challenges Completed: " + std::to_string(m_challengesCompleted));
    ColorablePrinter->printProgress("Achievements Unlocked: " + std::to_string(m_achievementsUnlocked));
    ColorablePrinter->printProgress("Highest Score: " + std::to_string(m_highestScore));
    
    // Milestone celebrations
    if (m_gamesPlayed == 5) {
        ColorablePrinter->printAchievement("🎉 5 Games Played! Game Explorer! 🎉");
    } else if (m_gamesPlayed == 10) {
        ColorablePrinter->printAchievement("🌟 10 Games! Game Enthusiast! 🌟");
    } else if (m_achievementsUnlocked == 3) {
        ColorablePrinter->printAchievement("💎 3 Achievements! Achievement Hunter! 💎");
    }
}

void NumberGamesWorkshop::updateProgress() {
    int total_activities = m_games.size() + m_challenges.size() + 5;
    m_learningProgress = (m_currentGame * 100.0) / total_activities;
    
    if (m_aiHelper) {
        m_aiHelper->analyzeProgress(m_learningProgress);
        m_aiHelper->provideEncouragement();
    }
    
    Logger::info("Number games progress: " + std::to_string(m_learningProgress) + "%");
}

void NumberGamesWorkshop::checkForBreak() {
    auto now = std::chrono::steady_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::minutes>(now - m_lastBreakTime);
    
    if (duration.count() >= m_attentionSpanMinutes) {
        m_needsBreak = true;
        suggestBreak();
    }
}

void NumberGamesWorkshop::suggestBreak() {
    ColorablePrinter->printGentleWarning("Game players need to rest their amazing brains!");
    ColorablePrinter->printStory("Let's take a little break! Even the best players recharge!");
    ColorablePrinter->printHappy("When we come back, we'll play more amazing games!");
    
    m_needsBreak = true;
    m_lastBreakTime = std::chrono::steady_clock::now();
}

void NumberGamesWorkshop::render() {
    ColorablePrinter->printStars(9);
}

void NumberGamesWorkshop::handleInput() {
    ColorablePrinter->printHelp("Keep playing! Every game teaches you something new about mathematics!");
}

bool NumberGamesWorkshop::isComplete() const {
    return m_currentGame >= m_games.size() + m_challenges.size() + 5;
}

double NumberGamesWorkshop::getProgress() const {
    return m_learningProgress;
}

void NumberGamesWorkshop::endWorkshop() {
    ColorablePrinter->printAchievement("You've completed the Number Games workshop!");
    ColorablePrinter->printExcited("You're now a Mathematical Game Master! 🎮");
    
    ColorablePrinter->printProgress("Games Played: " + std::to_string(m_gamesPlayed));
    ColorablePrinter->printProgress("Challenges Completed: " + std::to_string(m_challengesCompleted));
    ColorablePrinter->printProgress("Achievements Unlocked: " + std::to_string(m_achievementsUnlocked));
    ColorablePrinter->printProgress("Highest Score: " + std::to_string(m_highestScore));
    ColorablePrinter->printProgress("Best Game: " + m_bestGame);
    
    if (m_achievementsUnlocked >= 4) {
        ColorablePrinter->printAchievement("🏆 Achievement Master! You've unlocked most achievements! 🏆");
    }
    
    m_isRunning = false;
}

void NumberGamesWorkshop::cleanup() {
    m_gameEngine.reset();
    m_mathPuzzles.reset();
    m_numberGames.reset();
    m_guide.reset();
    m_mathMagician.reset();
    m_aiHelper.reset();
    
    Logger::info("NumberGamesWorkshop cleanup complete");
}

} // namespace Workshops
} // namespace Recipy