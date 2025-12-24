/*
 * HelloNumbersWorkshop.h - First Introduction to Numbers
 * 
 * A gentle, friendly introduction to numbers for Grade 1 students.
 * This workshop covers 400+ basic number concepts through play.
 */

#ifndef HELLONUMBERSWORKSHOP_H
#define HELLONUMBERSWORKSHOP_H

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
        class FriendlyGuide;
    }
    namespace AI {
        class ChildAIHelper;
    }

    /**
     * @brief Workshop 1: Hello Numbers!
     * 
     * The first step in mathematical adventure, introducing
     * Grade 1 students to the magical world of numbers.
     * 
     * Features 400+ learning activities:
     * - Number recognition (1-20)
     * - Counting with fingers and objects
     * - Number songs and rhymes
     * - Visual number patterns
     * - Simple number stories
     * - Interactive counting games
     */
    class HelloNumbersWorkshop {
    public:
        HelloNumbersWorkshop();
        ~HelloNumbersWorkshop();
        
        /**
         * @brief Initialize the workshop with all learning activities
         */
        bool initialize();
        
        /**
         * @brief Start the workshop adventure
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
        std::unique_ptr<Characters::FriendlyGuide> m_guide;
        std::unique_ptr<AI::ChildAIHelper> m_aiHelper;
        
        // Learning state
        bool m_isActive;
        double m_progress;
        int mCurrentActivity;
        int mCurrentNumber;
        std::vector<bool> m_masteredNumbers;
        std::map<int, int> m_numberConfidence;
        
        // Child psychology
        int m_attentionSpent;
        bool m_needsEncouragement;
        std::string m_preferredLearningStyle;
        
        // Learning activities (400+ total)
        struct LearningActivity {
            int id;
            std::string name;
            std::string description;
            std::string type;  // "visual", "auditory", "kinesthetic"
            int difficultyLevel;
            bool completed;
            double confidence;
        };
        
        std::vector<LearningActivity> m_activities;
        
        // Activity categories
        std::vector<LearningActivity> m_numberRecognitionActivities;
        std::vector<LearningActivity> m_countingActivities;
        std::vector<LearningActivity> m_numberSongActivities;
        std::vector<LearningActivity> m_visualPatternActivities;
        std::vector<LearningActivity> m_numberStoryActivities;
        std::vector<LearningActivity> m_countingGameActivities;
        
        // Initialize methods
        bool initializeComponents();
        void initializeActivities();
        void createNumberRecognitionActivities();    // 50+ activities
        void createCountingActivities();              // 60+ activities
        void createNumberSongActivities();            // 40+ activities
        void createVisualPatternActivities();         // 70+ activities
        void createNumberStoryActivities();           // 50+ activities
        void createCountingGameActivities();          // 80+ activities
        
        // Core learning methods
        void introduceNumberOne();
        void introduceNumberTwo();
        void introduceNumberThree();
        void introduceNumberFour();
        void introduceNumberFive();
        void introduceNumberSix();
        void introduceNumberSeven();
        void introduceNumberEight();
        void introduceNumberNine();
        void introduceNumberTen();
        void introduceTeens(int teen);
        
        // Activity execution
        void executeActivity(const LearningActivity& activity);
        void runNumberRecognitionActivity(int number);
        void runCountingActivity(int objects);
        void runNumberSongActivity(int song);
        void runVisualPatternActivity(int pattern);
        void runNumberStoryActivity(int story);
        void runCountingGameActivity(int game);
        
        // Interactive methods
        void askChildToCount(int count);
        void showNumberWithObjects(int number);
        void singNumberSong(int number);
        void tellNumberStory(int number);
        void playCountingGame(int gameType);
        
        // Visual learning
        void displayNumberVisually(int number);
        void showNumberAnimation(int number);
        void createNumberShape(int number);
        void showNumberInNature(int number);
        
        // Auditory learning
        void playNumberSound(int number);
        void singCountingSong(int count);
        void tellNumberRhyme(int number);
        void playNumberClapGame(int number);
        
        // Kinesthetic learning
        void countWithFingers(int number);
        void countWithBody(int number);
        void jumpCountActivity(int number);
        void createNumberWithBody(int number);
        
        // Assessment and progress
        void assessNumberKnowledge(int number);
        void updateProgress();
        void provideEncouragement();
        void celebrateMilestone(int number);
        
        // AI enhancement
        void adaptToChildResponse();
        void personalizeLearning();
        void generateCustomActivity();
        
        // Child psychology
        void maintainAttention();
        void providePositiveReinforcement();
        void adjustDifficulty();
        
        // Helper methods
        void introduceWorkshop();
        void explainActivity(const LearningActivity& activity);
        void celebrateSuccess();
        void suggestBreak();
        void endWorkshop();
        
        // Cleanup
        void cleanup();
    };
}

#endif // HELLONUMBERSWORKSHOP_H