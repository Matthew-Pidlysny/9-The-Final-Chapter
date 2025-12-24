/*
 * SharingNumbersWorkshop.h - Introduction to Reciprocals
 * 
 * A gentle introduction to the concept of reciprocals for Grade 1 students.
 * This workshop covers 400+ reciprocal concepts through sharing and fairness.
 */

#ifndef SHARINGNUMBERSWORKSHOP_H
#define SHARINGNUMBERSWORKSHOP_H

#include <memory>
#include <vector>
#include <string>
#include <map>

namespace Recipy {
    namespace GUI {
        class AnimationSystem;
        class Storyteller;
    }
    namespace Characters {
        class NumberFriends;
        class MathMagician;
    }
    namespace AI {
        class ChildAIHelper;
        class CreativeProblemSolver;
    }
    namespace Math {
        class ReciprocalCalculator;
    }

    /**
     * @brief Workshop 2: Sharing Numbers (Reciprocals)
     * 
     * Introduces the concept of reciprocals through the idea of sharing
     * and fairness, making advanced mathematics accessible to Grade 1 students.
     * 
     * Features 400+ learning activities:
     * - Sharing concept introduction
     * - Fair division games
     * - Turn-taking activities
     * - Visual fraction foundations
     * - Simple reciprocal patterns (1/2, 1/3, 1/4)
     * - Real-world sharing scenarios
     * - Interactive fairness puzzles
     */
    class SharingNumbersWorkshop {
    public:
        SharingNumbersWorkshop();
        ~SharingNumbersWorkshop();
        
        /**
         * @brief Initialize the sharing workshop
         */
        bool initialize();
        
        /**
         * @brief Start the sharing adventure
         */
        void start();
        
        /**
         * @brief Update workshop state
         */
        void update();
        
        /**
         * @brief Render workshop visuals
         */
        void render();
        
        /**
         * @brief Handle child's input
         */
        void handleInput();
        
        /**
         * @brief Check if workshop is complete
         */
        bool isComplete() const;
        
        /**
         * @brief Get current progress (0.0 to 1.0)
         */
        double getProgress() const;
        
    private:
        // Core components
        std::unique_ptr<GUI::AnimationSystem> m_animationSystem;
        std::unique_ptr<GUI::Storyteller> m_storyteller;
        std::unique_ptr<Characters::NumberFriends> m_numberFriends;
        std::unique_ptr<Characters::MathMagician> m_mathMagician;
        std::unique_ptr<AI::ChildAIHelper> m_aiHelper;
        std::unique_ptr<AI::CreativeProblemSolver> m_creativeSolver;
        std::unique_ptr<Math::ReciprocalCalculator> m_reciprocalCalc;
        
        // Learning state
        bool m_isActive;
        double m_progress;
        int mCurrentActivity;
        int mCurrentReciprocal;
        std::map<std::string, bool> m_masteredConcepts;
        std::map<int, double> m_reciprocalConfidence;
        
        // Child psychology
        int m_conceptDifficulty;
        bool m_needsVisualHelp;
        std::string m_preferredSharingScenario;
        
        // Learning activities (400+ total)
        struct SharingActivity {
            int id;
            std::string name;
            std::string description;
            std::string type;  // "visual", "story", "game", "real_world"
            int difficultyLevel;
            bool completed;
            double confidence;
            std::string reciprocal;  // "1/2", "1/3", "1/4", etc.
        };
        
        std::vector<SharingActivity> m_activities;
        
        // Activity categories
        std::vector<SharingActivity> m_sharingConceptActivities;    // 60+ activities
        std::vector<SharingActivity> m_fairDivisionActivities;      // 70+ activities
        std::vector<SharingActivity> m_turnTakingActivities;        // 50+ activities
        std::vector<SharingActivity> m_visualFractionActivities;   // 80+ activities
        std::vector<SharingActivity> m_reciprocalPatternActivities; // 60+ activities
        std::vector<SharingActivity> m_realWorldActivities;        // 50+ activities
        std::vector<SharingActivity> m_fairnessPuzzleActivities;   // 80+ activities
        
        // Initialize methods
        bool initializeComponents();
        void initializeActivities();
        void createSharingConceptActivities();       // 60+ activities
        void createFairDivisionActivities();         // 70+ activities
        void createTurnTakingActivities();           // 50+ activities
        void createVisualFractionActivities();        // 80+ activities
        void createReciprocalPatternActivities();     // 60+ activities
        void createRealWorldActivities();             // 50+ activities
        void createFairnessPuzzleActivities();        // 80+ activities
        
        // Core learning methods
        void introduceSharingConcept();
        void explainFairDivision();
        void teachTurnTaking();
        void showVisualFractions();
        void demonstrateReciprocalPatterns();
        void exploreRealWorldSharing();
        void solveFairnessPuzzles();
        
        // Specific reciprocal teachings
        void teachReciprocalHalf();
        void teachReciprocalThird();
        void teachReciprocalFourth();
        void teachReciprocalFifth();
        void teachReciprocalSixth();
        void teachReciprocalEighth();
        void teachReciprocalTenth();
        
        // Activity execution
        void executeActivity(const SharingActivity& activity);
        void runSharingActivity(int activity);
        void runFairDivisionGame(int game);
        void runTurnTakingExercise(int exercise);
        void runVisualFractionDemo(int demo);
        void runReciprocalPattern(int pattern);
        void runRealWorldScenario(int scenario);
        void runFairnessPuzzle(int puzzle);
        
        // Visual learning
        void showSharingVisually(int total, int shares);
        void displayFractionVisually(const std::string& fraction);
        void animateSharingProcess(int items, int people);
        void createFractionArt(const std::string& fraction);
        void showReciprocalRelationship(int numerator, int denominator);
        
        // Story-based learning
        void tellSharingStory(const std::string& story);
        void explainFairnessWithStory();
        void narrateSharingAdventure(int scenario);
        void createSharingCharacters();
        
        // Game-based learning
        void playSharingGame(int gameType);
        void conductFairDivisionExercise(int exercise);
        practiceTurnTakingActivity(int activity);
        void solveSharingPuzzle(int puzzle);
        
        // Real-world connections
        void connectToFoodSharing();
        void connectToToySharing();
        void connectToTimeSharing();
        void connectToSpaceSharing();
        
        // Mathematical foundations
        void introduceBasicFractions();
        void explainReciprocalConcept(const std::string& fraction);
        void demonstrateReciprocalProperty(int a, int b);
        void showReciprocalPatterns();
        
        // AI enhancement
        void adaptToChildResponse();
        void personalizeScenarios();
        void generateCreativeSharingStories();
        
        // Assessment and progress
        void assessSharingUnderstanding();
        void testReciprocalKnowledge(const std::string& reciprocal);
        void updateProgress();
        void provideEncouragement();
        void celebrateMilestone(const std::string& concept);
        
        // Child psychology
        void maintainFairnessFocus();
        void providePositiveReinforcement();
        void adjustSharingComplexity();
        
        // Helper methods
        void introduceWorkshop();
        void explainActivity(const SharingActivity& activity);
        void celebrateSuccess();
        void suggestBreak();
        void endWorkshop();
        
        // Cleanup
        void cleanup();
    };
}

#endif // SHARINGNUMBERSWORKSHOP_H