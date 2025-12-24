/*
 * RecipyApp.h - Main Application Class
 * 
 * Coordinates all the workshops, AI helpers, and child-friendly features
 * for the Grade 1 mathematical learning adventure.
 */

#ifndef RECIPIAPP_H
#define RECIPIAPP_H

#include <memory>
#include <string>
#include <vector>
#include <map>

namespace Recipy {
    namespace GUI {
        class MainWindow;
        class ChildFriendlyGUI;
        class Storyteller;
        class ProgressTracker;
        class AnimationSystem;
    }
    namespace Workshops {
        class WorkshopManager;
        class HelloNumbersWorkshop;
        class SharingNumbersWorkshop;
        class LongNumberAdventuresWorkshop;
        class PatternFindingWorkshop;
        class NumberFamiliesWorkshop;
        class InformationMagicWorkshop;
        class NumberSecretsWorkshop;
        class ShapeNumbersWorkshop;
        class NumberGamesWorkshop;
        class BigIdeasWorkshop;
    }
    namespace AI {
        class ChildAIHelper;
        class AdaptiveLearning;
        class CreativeProblemSolver;
    }
    namespace Psychology {
        class LearningStyleAdapter;
        class MotivationSystem;
        class AttentionSpanManager;
    }
    namespace Characters {
        class FriendlyGuide;
        class NumberFriends;
        class MathMagician;
    }

    /**
     * @brief Main application coordinator for Recipy
     * 
     * This class manages the entire educational experience, ensuring
     * that all content is age-appropriate and engaging for Grade 1 students
     * while introducing advanced mathematical concepts gradually.
     */
    class RecipyApp {
    public:
        RecipyApp();
        ~RecipyApp();
        
        /**
         * @brief Initialize all components and workshops
         * @return true if initialization successful
         */
        bool initialize();
        
        /**
         * @brief Run the main application loop
         */
        void run();
        
        /**
         * @brief Handle shutdown and cleanup
         */
        void shutdown();
        
        /**
         * @brief Get current child's learning progress
         */
        double getLearningProgress() const;
        
        /**
         * @brief Check if child needs a break
         */
        bool needsBreak() const;
        
        /**
         * @brief Celebrate child's achievements
         */
        void celebrateAchievement(const std::string& achievement);
        
    private:
        // GUI Components
        std::unique_ptr<GUI::MainWindow> m_mainWindow;
        std::unique_ptr<GUI::ChildFriendlyGUI> m_childGUI;
        std::unique_ptr<GUI::Storyteller> m_storyteller;
        std::unique_ptr<GUI::ProgressTracker> m_progressTracker;
        std::unique_ptr<GUI::AnimationSystem> m_animationSystem;
        
        // Workshop Components (4000+ features total)
        std::unique_ptr<Workshops::WorkshopManager> m_workshopManager;
        std::unique_ptr<Workshops::HelloNumbersWorkshop> m_helloNumbers;
        std::unique_ptr<Workshops::SharingNumbersWorkshop> m_sharingNumbers;
        std::unique_ptr<Workshops::LongNumberAdventuresWorkshop> m_longNumbers;
        std::unique_ptr<Workshops::PatternFindingWorkshop> m_patternFinding;
        std::unique_ptr<Workshops::NumberFamiliesWorkshop> m_numberFamilies;
        std::unique_ptr<Workshops::InformationMagicWorkshop> m_informationMagic;
        std::unique_ptr<Workshops::NumberSecretsWorkshop> m_numberSecrets;
        std::unique_ptr<Workshops::ShapeNumbersWorkshop> m_shapeNumbers;
        std::unique_ptr<Workshops::NumberGamesWorkshop> m_numberGames;
        std::unique_ptr<Workshops::BigIdeasWorkshop> m_bigIdeas;
        
        // AI Enhancement Components
        std::unique_ptr<AI::ChildAIHelper> m_aiHelper;
        std::unique_ptr<AI::AdaptiveLearning> m_adaptiveLearning;
        std::unique_ptr<AI::CreativeProblemSolver> m_creativeSolver;
        
        // Psychology Components
        std::unique_ptr<Psychology::LearningStyleAdapter> m_learningAdapter;
        std::unique_ptr<Psychology::MotivationSystem> m_motivationSystem;
        std::unique_ptr<Psychology::AttentionSpanManager> m_attentionManager;
        
        // Character Components
        std::unique_ptr<Characters::FriendlyGuide> m_friendlyGuide;
        std::unique_ptr<Characters::NumberFriends> m_numberFriends;
        std::unique_ptr<Characters::MathMagician> m_mathMagician;
        
        // State Management
        bool m_isRunning;
        bool m_needsBreak;
        double m_learningProgress;
        int m_currentWorkshop;
        std::vector<std::string> m_achievements;
        std::map<std::string, double> m_skillLevels;
        
        // Child Psychology Settings
        int m_attentionSpanMinutes;
        double m_difficultyLevel;
        std::string m_preferredLearningStyle;
        bool m_useVisualLearning;
        bool m_useAuditoryLearning;
        bool m_useKinestheticLearning;
        
        // Initialization Methods
        bool initializeGUI();
        bool initializeWorkshops();
        bool initializeAI();
        bool initializePsychology();
        bool initializeCharacters();
        
        // Main Loop Methods
        void update();
        void render();
        void handleInput();
        void checkChildNeeds();
        
        // Workshop Management
        void advanceToNextWorkshop();
        void repeatCurrentWorkshop();
        void selectWorkshop(int workshopId);
        
        // AI Helper Functions
        void adaptToChildProgress();
        void generatePersonalizedContent();
        void provideEncouragement();
        
        // Psychology Methods
        void maintainAttention();
        void providePositiveReinforcement();
        void adjustDifficulty();
        
        // Character Interaction
        void introduceGuide();
        void showNumberFriends();
        void callMathMagician();
        
        // Cleanup
        void cleanup();
    };
}

#endif // RECIPIAPP_H