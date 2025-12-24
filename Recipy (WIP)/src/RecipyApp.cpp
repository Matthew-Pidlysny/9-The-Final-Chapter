/*
 * RecipyApp.cpp - Main Application Implementation
 * 
 * Bringing advanced mathematics to wonderful Grade 1 students through
 * loving, playful learning and beautiful child-centered psychological best practices.
 */

#include "RecipyApp.h"
#include "utils/Logger.h"
#include "utils/ColorfulPrinter.h"
#include <iostream>
#include <chrono>
#include <thread>

namespace Recipy {

RecipyApp::RecipyApp() 
    : m_isRunning(false)
    , m_needsBreak(false)
    , m_learningProgress(0.0)
    , m_currentWorkshop(0)
    , m_attentionSpanMinutes(15)  // Age-appropriate for Grade 1
    , m_difficultyLevel(0.1)      // Start very easy
    , m_preferredLearningStyle("visual")
    , m_useVisualLearning(true)
    , m_useAuditoryLearning(true)
    , m_useKinestheticLearning(true) {
    
    Logger::info("RecipyApp constructor - Creating magical math adventure!");
}

RecipyApp::~RecipyApp() {
    cleanup();
}

bool RecipyApp::initialize() {
    Logger::info("Initializing Recipy application for wonderful Grade 1 learners...");
    
    ColorfulPrinter::printStory("Oh, wonderful friend! Let's prepare the most magical learning adventure just for YOU!");
    
    // Initialize all components in beautiful child-friendly order
    if (!initializeGUI()) {
        ColorfulPrinter::printSad("The picture books couldn't be loaded.");
        return false;
    }
    
    if (!initializeWorkshops()) {
        ColorfulPrinter::printSad("The math playground couldn't be set up.");
        return false;
    }
    
    if (!initializeAI()) {
        ColorfulPrinter::printSad("Oh no, the caring learning helpers couldn't wake up.");
        return false;
    }
    
    if (!initializePsychology()) {
        ColorfulPrinter::printSad("The happiness machine couldn't start.");
        return false;
    }
    
    if (!initializeCharacters()) {
        ColorfulPrinter::printSad("Oh no, the magical number friends are feeling shy today.");
        return false;
    }
    
    m_isRunning = true;
    ColorfulPrinter::printRainbow("🎉 Oh, beautiful soul! Everything is ready for YOUR magical adventure! 🎉");
    return true;
}

bool RecipyApp::initializeGUI() {
    Logger::info("Setting up beautiful child-friendly interface...");
    
    try {
        m_mainWindow = std::make_unique<GUI::MainWindow>();
        m_childGUI = std::make_unique<GUI::ChildFriendlyGUI>();
        m_storyteller = std::make_unique<GUI::Storyteller>();
        m_progressTracker = std::make_unique<GUI::ProgressTracker>();
        m_animationSystem = std::make_unique<GUI::AnimationSystem>();
        
        ColorfulPrinter::printHappy("Oh, wonderful! Our colorful playground is ready for YOU!");
        return true;
    } catch (...) {
        return false;
    }
}

bool RecipyApp::initializeWorkshops() {
    Logger::info("Preparing 4000+ wonderful learning activities...");
    
    try {
        // Create all 10 workshops for comprehensive mathematical education
        m_helloNumbers = std::make_unique<Workshops::HelloNumbersWorkshop>();
        m_sharingNumbers = std::make_unique<Workshops::SharingNumbersWorkshop>();
        m_longNumbers = std::make_unique<Workshops::LongNumberAdventuresWorkshop>();
        m_patternFinding = std::make_unique<Workshops::PatternFindingWorkshop>();
        m_numberFamilies = std::make_unique<Workshops::NumberFamiliesWorkshop>();
        m_informationMagic = std::make_unique<Workshops::InformationMagicWorkshop>();
        m_numberSecrets = std::make_unique<Workshops::NumberSecretsWorkshop>();
        m_shapeNumbers = std::make_unique<Workshops::ShapeNumbersWorkshop>();
        m_numberGames = std::make_unique<Workshops::NumberGamesWorkshop>();
        m_bigIdeas = std::make_unique<Workshops::BigIdeasWorkshop>();
        
        m_workshopManager = std::make_unique<Workshops::WorkshopManager>();
        m_helloNumbers = std::make_unique<Workshops::HelloNumbersWorkshop>();
        m_sharingNumbers = std::make_unique<Workshops::SharingNumbersWorkshop>();
        m_longNumbers = std::make_unique<Workshops::LongNumberAdventuresWorkshop>();
        m_patternFinding = std::make_unique<Workshops::PatternFindingWorkshop>();
        m_numberFamilies = std::make_unique<Workshops::NumberFamiliesWorkshop>();
        m_informationMagic = std::make_unique<Workshops::InformationMagicWorkshop>();
        m_numberSecrets = std::make_unique<Workshops::NumberSecretsWorkshop>();
        m_shapeNumbers = std::make_unique<Workshops::ShapeNumbersWorkshop>();
        m_numberGames = std::make_unique<Workshops::NumberGamesWorkshop>();
        m_bigIdeas = std::make_unique<Workshops::BigIdeasWorkshop>();
        
        ColorfulPrinter::printExcited("Hooray! All our magical math playgrounds are ready for amazing friends like YOU!");
        return true;
    } catch (...) {
        return false;
    }
}

bool RecipyApp::initializeAI() {
    Logger::info("Waking up caring AI learning helpers...");
    
    try {
        m_aiHelper = std::make_unique<AI::ChildAIHelper>();
        m_adaptiveLearning = std::make_unique<AI::AdaptiveLearning>();
        m_creativeSolver = std::make_unique<AI::CreativeProblemSolver>();
        
        ColorfulPrinter::printHappy("Yippee! Our caring AI friends are ready to help YOU shine!");
        return true;
    } catch (...) {
        return false;
    }
}

bool RecipyApp::initializePsychology() {
    Logger::info("Starting happiness and motivation systems...");
    
    try {
        m_learningAdapter = std::make_unique<Psychology::LearningStyleAdapter>();
        m_motivationSystem = std::make_unique<Psychology::MotivationSystem>();
        m_attentionManager = std::make_unique<Psychology::AttentionSpanManager>();
        
        ColorfulPrinter::printHappy("Oh, wonderful! The magical fun machine is turned on just for YOU!");
        return true;
    } catch (...) {
        return false;
    }
}

bool RecipyApp::initializeCharacters() {
    Logger::info("Introducing magical number friends...");
    
    try {
        m_friendlyGuide = std::make_unique<Characters::FriendlyGuide>();
        m_numberFriends = std::make_unique<Characters::NumberFriends>();
        m_mathMagician = std::make_unique<Characters::MathMagician>();
        
        ColorfulPrinter::printExcited("Your magical number friends are here to play with YOU!");
        return true;
    } catch (...) {
        return false;
    }
}

void RecipyApp::run() {
    Logger::info("Starting main Recipy adventure loop...");
    
    // Introduce the adventure
    introduceGuide();
    
    auto startTime = std::chrono::steady_clock::now();
    auto lastCheck = startTime;
    
    while (m_isRunning) {
        // Check beautiful child's needs frequently
        auto currentTime = std::chrono::steady_clock::now();
        auto elapsed = std::chrono::duration_cast<std::chrono::minutes>(currentTime - lastCheck);
        
        if (elapsed.count() >= 5) {  // Check every 5 minutes
            checkChildNeeds();
            lastCheck = currentTime;
        }
        
        // Main update cycle
        update();
        render();
        handleInput();
        
        // Brief pause to prevent overwhelming
        std::this_thread::sleep_for(std::chrono::milliseconds(100));
        
        // Check if beautiful child needs a break
        if (needsBreak()) {
            suggestBreak();
        }
    }
}

void RecipyApp::update() {
    if (!m_isRunning) return;
    
    // Update all components
    if (m_progressTracker) m_progressTracker->update();
    if (m_animationSystem) m_animationSystem->update();
    if (m_workshopManager) m_workshopManager->update();
    if (m_adaptiveLearning) m_adaptiveLearning->update();
    if (m_attentionManager) m_attentionManager->update();
    
    // Update learning progress
    adaptToChildProgress();
}

void RecipyApp::render() {
    if (!m_isRunning) return;
    
    // Render all visual components
    if (m_mainWindow) m_mainWindow->render();
    if (m_childGUI) m_childGUI->render();
    if (m_progressTracker) m_progressTracker->render();
    if (m_animationSystem) m_animationSystem->render();
}

void RecipyApp::handleInput() {
    // Handle beautiful child's input in a very patient, encouraging way
    if (m_workshopManager) {
        m_workshopManager->handleChildInput();
    }
}

void RecipyApp::checkChildNeeds() {
    if (m_attentionManager) {
        m_needsBreak = m_attentionManager->needsBreak();
        
        if (m_needsBreak) {
            Logger::info("Child attention span reached, suggesting break");
        }
    }
}

bool RecipyApp::needsBreak() const {
    return m_needsBreak;
}

void RecipyApp::suggestBreak() {
    ColorfulPrinter::printStory("Let's take a little break! Even beautiful number explorers need rest!");
    ColorfulPrinter::printHappy("Stretch your arms, wiggle your fingers, and we'll play again soon!");
    
    // Wait for beautiful child to take a break
    std::this_thread::sleep_for(std::chrono::minutes(2));
    
    m_needsBreak = false;
    ColorfulPrinter::printExcited("Welcome back to our magical family! Oh, how we've missed you!");
}

void RecipyApp::introduceGuide() {
    if (m_friendlyGuide) {
        m_friendlyGuide->sayHello();
        m_friendlyGuide->explainAdventure();
    }
}

void RecipyApp::adaptToChildProgress() {
    if (m_adaptiveLearning) {
        m_adaptiveLearning->analyzeProgress(m_learningProgress);
        m_adaptiveLearning->adjustDifficulty(m_difficultyLevel);
    }
}

double RecipyApp::getLearningProgress() const {
    return m_learningProgress;
}

void RecipyApp::celebrateAchievement(const std::string& achievement) {
    m_achievements.push_back(achievement);
    
    ColorfulPrinter::printRainbow("🌟 AMAZING WORK! 🌟");
    ColorfulPrinter::printExcited("You achieved: " + achievement);
    
    if (m_motivationSystem) {
        m_motivationSystem->celebrate(achievement);
    }
    
    if (m_animationSystem) {
        m_animationSystem->showCelebration();
    }
}

void RecipyApp::shutdown() {
    Logger::info("Shutting down Recipy application...");
    
    ColorfulPrinter::printStory("Our magical number adventure is ending for now, beautiful friend...");
    ColorfulPrinter::printHappy("Thank you for exploring math with us today!");
    
    cleanup();
}

void RecipyApp::cleanup() {
    // Clean up all components in reverse order
    m_mathMagician.reset();
    m_numberFriends.reset();
    m_friendlyGuide.reset();
    
    m_attentionManager.reset();
    m_motivationSystem.reset();
    m_learningAdapter.reset();
    
    m_creativeSolver.reset();
    m_adaptiveLearning.reset();
    m_aiHelper.reset();
    
    m_bigIdeas.reset();
    m_numberGames.reset();
    m_shapeNumbers.reset();
    m_numberSecrets.reset();
    m_informationMagic.reset();
    m_numberFamilies.reset();
    m_patternFinding.reset();
    m_longNumbers.reset();
    m_sharingNumbers.reset();
    m_helloNumbers.reset();
    m_workshopManager.reset();
    
    m_animationSystem.reset();
    m_progressTracker.reset();
    m_storyteller.reset();
    m_childGUI.reset();
    m_mainWindow.reset();
    
    m_isRunning = false;
    Logger::info("Recipy application shutdown complete");
}

} // namespace Recipy