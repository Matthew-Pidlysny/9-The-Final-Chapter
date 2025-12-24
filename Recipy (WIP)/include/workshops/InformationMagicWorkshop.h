/* 
 * InformationMagicWorkshop.h - Information Theory for Grade 1
 * 
 * Teaching children about information, patterns, and uncertainty
 * based on Shannon entropy concepts from the original analyzer.
 */

#pragma once

#include "../workshops/WorkshopBase.h"
#include "../characters/FriendlyGuide.h"
#include "../characters/MathMagician.h"
#include "../AI/ChildAIHelper.h"
#include "../math/EntropyCalculator.h"
#include "../math/InformationTheory.h"
#include "../math/PatternPredictor.h"
#include "../psychology/LearningStyleAdapter.h"
#include <memory>
#include <vector>
#include <string>
#include <map>
#include <chrono>

namespace Recipy {
namespace Workshops {

struct InformationExperiment {
    int id;
    std::string name;
    std::string description;
    std::string scenario;
    std::vector<std::string> outcomes;
    std::vector<double> probabilities;
    double entropy_value;
    std::string child_friendly_explanation;
    int difficulty_level;
};

struct CommunicationGame {
    int id;
    std::string game_name;
    std::string description;
    std::string message;
    std::vector<std::string> noise_factors;
    double success_rate;
    std::string learning_takeaway;
};

struct PredictionChallenge {
    int id;
    std::string challenge_name;
    std::string pattern;
    std::vector<std::string> possible_next;
    std::string correct_answer;
    double confidence_level;
    std::string reasoning;
};

class InformationMagicWorkshop : public WorkshopBase {
public:
    InformationMagicWorkshop();
    virtual ~InformationMagicWorkshop();
    
    // WorkshopBase overrides
    bool initialize() override;
    void start() override;
    void update() override;
    void render() override;
    void handleInput() override;
    bool isComplete() const override;
    double getProgress() const override;
    void endWorkshop() override;
    
    // Information exploration methods
    void exploreBasicInformation();
    void exploreCertaintyAndUncertainty();
    void exploreMessageSending();
    void explorePatternPrediction;
    void exploreInformationCompression();
    void exploreNoiseAndClarity();
    void createInformationArt();
    void solveInformationPuzzles();
    
private:
    // Core components
    std::unique_ptr<Characters::FriendlyGuide> m_guide;
    std::unique_ptr<Characters::MathMagician> m_aiHelper;
    std::unique_ptr<Math::EntropyCalculator> m_entropyCalculator;
    std::unique_ptr<Math::InformationTheory> m_informationTheory;
    std::unique_ptr<Math::PatternPredictor> m_patternPredictor;
    std::unique_ptr<Psychology::LearningStyleAdapter> m_learningAdapter;
    
    // Workshop state
    bool m_isRunning;
    int m_currentExperiment;
    int m_experimentsCompleted;
    int m_messagesSent;
    int m_predictionsMade;
    double m_learningProgress;
    std::chrono::steady_clock::time_point m_startTime;
    std::chrono::steady_clock::time_point m_lastBreakTime;
    bool m_needsBreak;
    int m_attentionSpanMinutes;
    double m_currentDifficulty;
    
    // Information collections
    std::vector<InformationExperiment> m_experiments;
    std::vector<CommunicationGame> m_games;
    std::vector<PredictionChallenge> m_challenges;
    std::map<std::string, double> m_entropyValues;
    std::vector<std::string> m_informationConcepts;
    
    // Mastery tracking
    std::map<std::string, bool> m_masteredConcepts;
    double m_highestEntropy;
    std::string m_mostInterestingPattern;
    int m_successfulPredictions;
    std::vector<std::string> m_discoveredConcepts;
    
    // Initialization methods
    bool initializeComponents();
    void initializeInformationExperiments();
    void initializeCommunicationGames();
    void initializePredictionChallenges();
    void initializeInformationConcepts();
    
    // Experiment methods
    void createCoinFlipExperiment();
    void createDiceRollExperiment();
    void createWeatherExperiment();
    void createCardExperiment();
    void createColorExperiment();
    void createStoryExperiment();
    
    // Communication methods
    void playTelephoneGame();
    void sendSecretMessage();
    void overcomeNoise();
    void measureInformation();
    
    // Prediction methods
    void predictNextInSequence();
    void guessThePattern();
    void calculateUncertainty;
    void findHiddenInformation();
    
    // Advanced information concepts
    void exploreInformationCompression();
    void exploreRedundancy();
    void exploreBinaryInformation();
    void exploreInformationValue();
    
    // Visualization and interaction
    void displayEntropy(double entropy, const std::string& context);
    void showInformationAmount(const std::string& message);
    void visualizeUncertainty(const std::vector<std::string>& outcomes);
    void createInformationArt(const std::string& pattern);
    
    // Assessment and celebration
    void assessInformationUnderstanding();
    void celebrateInformationDiscovery();
    void updateProgress();
    void checkForBreak();
    void suggestBreak();
    
    // Utility methods
    double calculateEntropy(const std::vector<double>& probabilities);
    std::string explainEntropy(double entropy, const std::string& context);
    std::string simplifyInformationConcept(const std::string& concept);
    bool predictNextItem(const std::string& pattern, std::string& prediction);
    
    // Cleanup
    void cleanup();
};

} // namespace Workshops
} // namespace Recipy