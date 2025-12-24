/* 
 * NumberGamesWorkshop.h - Mathematical Games and Play for Grade 1
 * 
 * Teaching mathematical concepts through engaging games and activities
 * that reinforce learning from the original analyzer components.
 */

#pragma once

#include "../workshops/WorkshopBase.h"
#include "../characters/FriendlyGuide.h"
#include "../characters/MathMagician.h"
#include "../AI/ChildAIHelper.h"
#include "../math/GameEngine.h"
#include "../math/MathPuzzles.h"
#include "../math/NumberGames.h"
#include "../psychology/LearningStyleAdapter.h"
#include <memory>
#include <vector>
#include <string>
#include <map>
#include <chrono>

namespace Recipy {
namespace Workshops {

struct MathGame {
    int id;
    std::string game_name;
    std::string description;
    std::string learning_objective;
    std::vector<std::string> materials_needed;
    int difficulty_level;
    int players_count;
    std::string game_type;
    bool competitive;
};

struct GameChallenge {
    int id;
    std::string challenge_name;
    std::string game_reference;
    std::string challenge_description;
    std::string success_criteria;
    int time_limit_seconds;
    std::vector<std::string> hints;
    std::string solution_approach;
};

struct Achievement {
    int id;
    std::string achievement_name;
    std::string description;
    std::string unlock_condition;
    bool unlocked;
    std::string icon;
};

class NumberGamesWorkshop : public WorkshopBase {
public:
    NumberGamesWorkshop();
    virtual ~NumberGamesWorkshop();
    
    // WorkshopBase overrides
    bool initialize() override;
    void start() override;
    void update() override;
    void render() override;
    void handleInput() override;
    bool isComplete() const override;
    double getProgress() const override;
    void endWorkshop() override;
    
    // Game exploration methods
    void playCountingGames();
    void playPatternGames();
    void playStrategyGames();
    void playProbabilityGames();
    void playGeometryGames();
    void playSpeedGames();
    void playMemoryGames();
    void createOwnGame();
    
private:
    // Core components
    std::unique_ptr<Characters::FriendlyGuide> m_guide;
    std::unique_ptr<Characters::MathMagician> m_aiHelper;
    std::unique_ptr<Math::GameEngine> m_gameEngine;
    std::unique_ptr<Math::MathPuzzles> m_mathPuzzles;
    std::unique_ptr<Math::NumberGames> m_numberGames;
    std::unique_ptr<Psychology::LearningStyleAdapter> m_learningAdapter;
    
    // Workshop state
    bool m_isRunning;
    int m_currentGame;
    int m_gamesPlayed;
    int m_challengesCompleted;
    int m_achievementsUnlocked;
    double m_learningProgress;
    std::chrono::steady_clock::time_point m_startTime;
    std::chrono::steady_clock::time_point m_lastBreakTime;
    bool m_needsBreak;
    int m_attentionSpanMinutes;
    double m_currentDifficulty;
    
    // Collections
    std::vector<MathGame> m_games;
    std::vector<GameChallenge> m_challenges;
    std::vector<Achievement> m_achievements;
    std::map<std::string, int> m_highScores;
    std::vector<std::string> m_favoriteGames;
    
    // Mastery tracking
    std::map<std::string, bool> m_masteredGames;
    int m_highestScore;
    std::string m_bestGame;
    std::vector<std::string> m_createdGames;
    double m_averageAccuracy;
    
    // Initialization methods
    bool initializeComponents();
    void initializeMathGames();
    void initializeGameChallenges();
    void initializeAchievements();
    
    // Game creation methods
    void createCountingGames();
    void createPatternGames();
    void createStrategyGames();
    void createProbabilityGames();
    void createGeometryGames();
    void createSpeedGames();
    void createMemoryGames();
    void createAdvancedGames();
    
    // Specific game implementations
    void playNumberBingo();
    void playMathMemory();
    void playPatternMaster();
    void playQuickCalc();
    void playShapeSorter();
    void playProbabilityWheel();
    void playSequenceBuilder();
    void playMathScavengerHunt();
    void playMultiplicationWar();
    void playFractionPizza();
    void playGeometryTangram();
    
    // Challenge methods
    void solveSpeedChallenge();
    void solveAccuracyChallenge();
    void solveStrategyChallenge();
    void solveCreativeChallenge();
    
    // Achievement system
    void unlockAchievement(const std::string& achievement_name);
    void checkAchievements();
    void displayAchievements();
    void celebrateAchievement(const Achievement& achievement);
    
    // Game mechanics
    void simulateGameplay(const MathGame& game);
    void trackGameProgress(const std::string& game_name, int score, double accuracy);
    void adaptDifficulty(double performance);
    void provideGameFeedback(int score, double accuracy);
    
    // Advanced gaming concepts
    void exploreGameTheory();
    void exploreProbabilityInGames();
    void exploreStrategyAndLogic();
    void exploreGameDesign();
    
    // Social and cooperative games
    void playCooperativeGames();
    void playTeamChallenges();
    void playTeachingGames();
    void playLeadershipGames();
    
    // Visualization and interaction
    void displayGameBoard(const std::string& game_name);
    void showScoreProgress(const std::string& game_name);
    void animateGameAction(const std::string& action);
    void createGameCelebration(const std::string& game_name, int score);
    
    // Assessment and celebration
    void assessGameUnderstanding();
    void celebrateGamingSuccess();
    void updateProgress();
    void checkForBreak();
    void suggestBreak();
    
    // Utility methods
    int calculateGameScore(const std::string& game_name, const std::vector<int>& results);
    double calculateAccuracy(const std::vector<int>& attempts, const std::vector<int>& correct);
    std::string recommendNextGame(double current_performance);
    bool isGameMastered(const std::string& game_name);
    
    // Cleanup
    void cleanup();
};

} // namespace Workshops
} // namespace Recipy