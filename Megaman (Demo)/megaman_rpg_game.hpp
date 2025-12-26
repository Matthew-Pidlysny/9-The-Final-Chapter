#ifndef MEGAMAN_RPG_GAME_HPP
#define MEGAMAN_RPG_GAME_HPP

#include <string>
#include <vector>
#include <map>
#include <memory>
#include <random>
#include <functional>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <chrono>
#include <thread>

namespace MegamanRPG {

    // Forward Declarations
    class Character;
    class GameWorld;
    class CombatSystem;
    class StoryManager;
    class SigmaBoss;

    // Character Classes and Types
    enum class CharacterClass {
        REPLOID_WARRIOR,
        REPLOID_SCOUT,
        REPLOID_ENGINEER,
        REPLOID_MEDIC,
        HUMAN_COMMANDER,
        HUMAN_SCIENTIST,
        HUMAN_DIPLOMAT,
        HYBRID_SPECIALIST
    };

    enum class SkillType {
        COMBAT,
        TECHNICAL,
        SOCIAL,
        SURVIVAL,
        LEADERSHIP,
        MEDICAL,
        ENGINEERING,
        DIPLOMATIC
    };

    // Skill Structure
    struct Skill {
        std::string name;
        SkillType type;
        int level;
        int experience;
        int max_level;
        std::vector<std::string> abilities;
        std::function<void(Character&)> on_level_up;
        
        Skill() : level(1), experience(0), max_level(10) {}
    };

    // Equipment Structure
    struct Equipment {
        std::string name;
        std::string type;
        int power_level;
        std::vector<std::string> bonuses;
        std::vector<std::string> requirements;
        int durability;
        int max_durability;
        bool is_legendary;
        
        Equipment() : power_level(1), durability(100), max_durability(100), is_legendary(false) {}
    };

    // Character Stats
    struct CharacterStats {
        int health;
        int max_health;
        int energy;
        int max_energy;
        int strength;
        int agility;
        int intelligence;
        int defense;
        int charisma;
        int luck;
        int accuracy;
        int evasion;
        
        CharacterStats() : 
            health(100), max_health(100), energy(50), max_energy(50),
            strength(10), agility(10), intelligence(10), defense(10),
            charisma(10), luck(10), accuracy(75), evasion(20) {}
    };

    // Main Character Class
    class Character {
    private:
        std::string name;
        CharacterClass character_class;
        CharacterStats stats;
        std::map<std::string, Skill> skills;
        std::vector<Equipment> equipment;
        int level;
        int experience;
        int skill_points;
        std::string background_story;
        std::vector<std::string> relationships;
        std::map<std::string, int> reputation;
        
    public:
        Character(const std::string& char_name, CharacterClass char_class);
        
        // Core Character Functions
        void levelUp();
        void gainExperience(int exp);
        void addSkillPoint();
        void upgradeSkill(const std::string& skill_name);
        void equipItem(const Equipment& item);
        void unequipItem(int slot);
        void takeDamage(int damage);
        void heal(int amount);
        void restoreEnergy(int amount);
        
        // Getters and Setters
        std::string getName() const { return name; }
        CharacterClass getClass() const { return character_class; }
        CharacterStats getStats() const { return stats; }
        int getLevel() const { return level; }
        int getExperience() const { return experience; }
        std::map<std::string, Skill> getSkills() const { return skills; }
        std::vector<Equipment> getEquipment() const { return equipment; }
        
        // Combat Functions
        int calculateDamage() const;
        int calculateDefense() const;
        double getHitChance() const;
        double getEvasionChance() const;
        bool useSkill(const std::string& skill_name);
        bool useAbility(const std::string& ability_name);
        
        // Social Functions
        void buildRelationship(const std::string& character_name, int strength);
        int getRelationshipStrength(const std::string& character_name);
        void changeReputation(const std::string& faction, int amount);
        int getReputation(const std::string& faction);
        
        // Story Functions
        void setBackgroundStory(const std::string& story);
        std::string getBackgroundStory() const;
        void addToStory(const std::string& event);
        
        // Display Functions
        void displayCharacterSheet() const;
        void displaySkills() const;
        void displayEquipment() const;
        void displayRelationships() const;
    };

    // Game World Structure
    struct Location {
        std::string name;
        std::string description;
        std::vector<std::string> connected_locations;
        std::vector<std::string> available_quests;
        std::vector<std::string> npcs_present;
        std::vector<std::string> resources;
        bool is_safe_zone;
        int difficulty_level;
        
        Location() : is_safe_zone(false), difficulty_level(1) {}
    };

    // Quest Structure
    struct Quest {
        std::string id;
        std::string title;
        std::string description;
        std::vector<std::string> objectives;
        std::vector<std::string> rewards;
        std::map<std::string, int> reputation_rewards;
        int experience_reward;
        bool is_main_quest;
        bool is_completed;
        int current_phase;
        int total_phases;
        
        Quest() : experience_reward(0), is_main_quest(false), is_completed(false), 
                  current_phase(0), total_phases(1) {}
    };

    // Game World Class
    class GameWorld {
    private:
        std::map<std::string, Location> locations;
        std::map<std::string, Quest> quests;
        std::string current_location;
        std::vector<std::string> discovered_locations;
        std::map<std::string, bool> world_state;
        int current_phase;
        int total_phases;
        
    public:
        GameWorld();
        
        // World Management
        void initializeWorld();
        void moveToLocation(const std::string& location_name);
        Location getCurrentLocation() const;
        void discoverLocation(const std::string& location_name);
        std::vector<std::string> getAvailableLocations() const;
        
        // Quest Management
        void addQuest(const Quest& quest);
        Quest getQuest(const std::string& quest_id);
        std::vector<Quest> getAvailableQuests() const;
        void completeQuest(const std::string& quest_id);
        void updateQuestProgress(const std::string& quest_id, const std::string& objective);
        
        // World State
        void setWorldState(const std::string& key, bool value);
        bool getWorldState(const std::string& key) const;
        void advancePhase();
        int getCurrentPhase() const;
        int getTotalPhases() const;
        
        // Environmental Effects
        void applyEnvironmentalEffects(Character& character);
        std::string getCurrentWeather() const;
        std::string getTimeOfDay() const;
        
        // Display Functions
        void displayCurrentLocation() const;
        void displayAvailableQuests() const;
        void displayWorldStatus() const;
    };

    // Combat System Class
    class CombatSystem {
    private:
        std::vector<std::shared_ptr<Character>> allies;
        std::vector<std::shared_ptr<Character>> enemies;
        bool is_combat_active;
        int current_turn;
        std::string combat_log;
        
        std::mt19937 random_engine;
        
        // Combat Calculations
        int calculateDamage(const Character& attacker, const Character& defender);
        bool checkHit(const Character& attacker, const Character& defender);
        bool checkCritical(const Character& attacker);
        std::string generateCombatLogEntry(const std::string& action, const std::string& target, int damage);
        
    public:
        CombatSystem();
        
        // Combat Management
        void startCombat(const std::vector<std::shared_ptr<Character>>& player_allies,
                        const std::vector<std::shared_ptr<Character>>& enemies);
        void endCombat();
        bool isCombatActive() const;
        
        // Turn Management
        void nextTurn();
        int getCurrentTurn() const;
        std::shared_ptr<Character> getCurrentActor();
        
        // Combat Actions
        bool performAttack(const std::shared_ptr<Character>& attacker, 
                          const std::shared_ptr<Character>& target);
        bool useSkill(const std::shared_ptr<Character>& user, 
                     const std::string& skill_name,
                     const std::vector<std::shared_ptr<Character>>& targets);
        bool useItem(const std::shared_ptr<Character>& user, const std::string& item_name);
        bool defend(const std::shared_ptr<Character>& character);
        bool retreat(const std::shared_ptr<Character>& character);
        
        // Combat Status
        std::vector<std::shared_ptr<Character>> getAllies() const;
        std::vector<std::shared_ptr<Character>> getEnemies() const;
        std::vector<std::shared_ptr<Character>> getCombatants() const;
        bool checkVictory() const;
        bool checkDefeat() const;
        
        // Combat Display
        void displayCombatStatus() const;
        void displayCombatLog() const;
        std::string getCombatLog() const;
        void clearCombatLog();
    };

    // Story Manager Class
    class StoryManager {
    private:
        std::map<int, std::vector<std::string>> phase_stories;
        std::map<std::string, std::vector<std::string>> character_dialogues;
        std::map<std::string, bool> story_flags;
        int current_story_phase;
        std::vector<std::string> completed_story_elements;
        
    public:
        StoryManager();
        
        // Story Progression
        void initializeStory();
        void advanceStoryPhase();
        int getCurrentStoryPhase() const;
        void triggerStoryEvent(const std::string& event_name);
        
        // Story Content
        std::string getStoryText(int phase, int index);
        std::string getCharacterDialogue(const std::string& character_id, int index);
        void setStoryFlag(const std::string& flag_name, bool value);
        bool getStoryFlag(const std::string& flag_name) const;
        
        // Story Choices
        struct StoryChoice {
            std::string text;
            std::string consequence_flag;
            int reputation_change;
            std::string follow_up_story;
        };
        
        std::vector<StoryChoice> getCurrentChoices();
        bool makeStoryChoice(int choice_index);
        
        // Display Functions
        void displayCurrentStory() const;
        void displayChoices() const;
        void displayStoryProgress() const;
    };

    // Sigma Boss Battle Class
    class SigmaBoss {
    private:
        std::shared_ptr<Character> sigma_character;
        int current_phase;
        int total_phases;
        std::vector<std::string> phase_abilities;
        std::map<int, std::vector<std::string>> phase_dialogues;
        bool is_defeated;
        int defeat_attempts;
        
        // Boss Mechanics
        void transitionToNextPhase();
        void adaptToPlayerStrategy(const std::vector<std::shared_ptr<Character>>& players);
        void usePhaseAbility();
        std::string getCurrentPhaseDialogue();
        
    public:
        SigmaBoss();
        
        // Boss Battle Management
        void initializeBossBattle();
        void startBattle();
        void takeDamage(int damage);
        bool isDefeated() const;
        int getCurrentPhase() const;
        
        // Boss Actions
        void performAction(const std::vector<std::shared_ptr<Character>>& players);
        std::vector<std::shared_ptr<Character>> generateMinions();
        void environmentalAttack(std::vector<std::shared_ptr<Character>>& players);
        void psychologicalAttack(std::vector<std::shared_ptr<Character>>& players);
        
        // Boss Phases
        void phaseOneMechanics();
        void phaseTwoMechanics();
        void phaseThreeMechanics();
        void finalPhaseMechanics();
        
        // Defeat and Resolution
        void onDefeat();
        std::string getDefeatDialogue();
        std::vector<std::string> getPostBattleConsequences();
        
        // Display Functions
        void displayBossStatus() const;
        void displayPhaseStatus() const;
        void displayBossDialogue() const;
    };

    // Main Game Engine
    class MegamanRPGGame {
    private:
        std::shared_ptr<Character> player_character;
        std::unique_ptr<GameWorld> game_world;
        std::unique_ptr<CombatSystem> combat_system;
        std::unique_ptr<StoryManager> story_manager;
        std::unique_ptr<SigmaBoss> sigma_boss;
        
        bool is_game_running;
        int current_game_phase;
        int total_game_phases;
        
        // Game Systems
        void initializeGame();
        void gameLoop();
        void processInput(const std::string& input);
        void updateGameState();
        void renderGameState();
        
        // Save/Load System
        void saveGame(const std::string& filename);
        void loadGame(const std::string& filename);
        bool hasSaveFile(const std::string& filename);
        
        // Achievement System
        std::map<std::string, bool> achievements;
        void unlockAchievement(const std::string& achievement_id);
        void checkAchievements();
        
    public:
        MegamanRPGGame();
        ~MegamanRPGGame();
        
        // Game Control
        void startGame();
        void pauseGame();
        void resumeGame();
        void quitGame();
        
        // Character Management
        void createCharacter(const std::string& name, CharacterClass character_class);
        std::shared_ptr<Character> getPlayerCharacter() const;
        
        // Phase Management
        void advanceToNextPhase();
        int getCurrentGamePhase() const;
        int getTotalGamePhases() const;
        
        // Game State
        bool isGameRunning() const;
        void displayGameStatus() const;
        
        // Main Game Functions
        void displayMainMenu();
        void displayCharacterCreation();
        void displayGameInterface();
        void processMainMenuChoice(int choice);
        void processGameInput(const std::string& input);
    };

} // namespace MegamanRPG

#endif // MEGAMAN_RPG_GAME_HPP