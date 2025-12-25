#ifndef PRIVANNA_CHARACTER_SYSTEM_HPP
#define PRIVANNA_CHARACTER_SYSTEM_HPP

#include <string>
#include <vector>
#include <map>
#include <memory>
#include <cstdint>
#include "../systems/event_system.hpp"
#include "../utils/logger.hpp"

namespace Privanna {

// Character attributes
enum class Attribute {
    STRENGTH,
    DEXTERITY,
    INTELLIGENCE,
    WISDOM,
    CHARISMA,
    CONSTITUTION,
    PERCEPTION,
    LUCK,
    FAITH,
    WILLPOWER,
    AGILITY,
    ENDURANCE
};

// Skill types
enum class SkillType {
    COMBAT,
    DIPLOMACY,
    ECONOMIC,
    EXPLORATION,
    CRAFTING,
    MAGIC,
    SURVIVAL,
    SOCIAL,
    LEADERSHIP,
    STEALTH
};

// Character class progression
enum class CharacterClass {
    WARRIOR,
    MAGE,
    DIPLOMAT,
    MERCHANT,
    EXPLORER,
    CRAFTSMAN,
    LEADER,
    ROGUE,
    CLERIC,
    SCHOLAR
};

// Individual skill
struct Skill {
    std::string name;
    SkillType type;
    int level = 1;
    int experience = 0;
    int maxLevel = 100;
    std::vector<std::string> prerequisites;
    std::map<std::string, int> modifiers;
    bool isActive = false;
    int cooldown = 0;
    int manaCost = 0;
    
    void addExperience(int exp) {
        experience += exp;
        while (experience >= getExperienceForNextLevel() && level < maxLevel) {
            experience -= getExperienceForNextLevel();
            level++;
        }
    }
    
    int getExperienceForNextLevel() const {
        return level * 100 + (level * level * 10);
    }
    
    float getEffectiveness() const {
        return 1.0f + (level - 1) * 0.1f;
    }
};

// Character attributes with detailed tracking
struct CharacterAttributes {
    std::map<Attribute, int> primary;
    std::map<Attribute, int> secondary;
    std::map<Attribute, int> hidden;
    std::map<Attribute, int> modifiers;
    std::map<Attribute, int> temporary;
    
    int getAttribute(Attribute attr) const {
        int base = primary.count(attr) ? primary.at(attr) : 10;
        int sec = secondary.count(attr) ? secondary.at(attr) : 0;
        int mod = modifiers.count(attr) ? modifiers.at(attr) : 0;
        int temp = temporary.count(attr) ? temporary.at(attr) : 0;
        return base + sec + mod + temp;
    }
    
    void setAttribute(Attribute attr, int value) {
        primary[attr] = value;
    }
    
    void modifyAttribute(Attribute attr, int modifier) {
        modifiers[attr] += modifier;
    }
};

// Experience tracking for different activities
struct ExperienceTracker {
    std::map<std::string, int> combatExperience;
    std::map<std::string, int> diplomaticExperience;
    std::map<std::string, int> economicExperience;
    std::map<std::string, int> explorationExperience;
    std::map<std::string, int> craftingExperience;
    std::map<std::string, int> socialExperience;
    
    int getTotalExperience() const {
        int total = 0;
        for (const auto& pair : combatExperience) total += pair.second;
        for (const auto& pair : diplomaticExperience) total += pair.second;
        for (const auto& pair : economicExperience) total += pair.second;
        for (const auto& pair : explorationExperience) total += pair.second;
        for (const auto& pair : craftingExperience) total += pair.second;
        for (const auto& pair : socialExperience) total += pair.second;
        return total;
    }
};

// Talent system
struct Talent {
    std::string name;
    std::string description;
    int tier = 1;
    bool isPassive = true;
    std::vector<std::string> prerequisites;
    std::map<std::string, float> effects;
    bool isUnlocked = false;
    int pointsRequired = 1;
};

// Character class with full progression
class Character {
private:
    std::string name;
    int level = 1;
    int experience = 0;
    int prestigeLevel = 0;
    CharacterClass characterClass;
    
    CharacterAttributes attributes;
    std::map<std::string, std::shared_ptr<Skill>> skills;
    std::map<std::string, std::shared_ptr<Talent>> talents;
    
    ExperienceTracker experienceTracker;
    std::vector<std::string> achievements;
    std::map<std::string, int> specializations;
    
    int availableAttributePoints = 0;
    int availableTalentPoints = 0;
    int skillPoints = 0;
    
public:
    Character(const std::string& name, CharacterClass cls);
    
    // Core progression
    void addExperience(int exp, const std::string& source);
    void levelUp();
    bool canLevelUp() const;
    int getExperienceForNextLevel() const;
    
    // Attribute management
    void allocateAttributePoint(Attribute attr);
    int getAvailableAttributePoints() const { return availableAttributePoints; }
    
    // Skill management
    void learnSkill(const std::string& skillName);
    void upgradeSkill(const std::string& skillName);
    void useSkill(const std::string& skillName);
    int getSkillLevel(const std::string& skillName) const;
    
    // Talent management
    void unlockTalent(const std::string& talentName);
    bool isTalentUnlocked(const std::string& talentName) const;
    
    // Specialization
    void addSpecialization(const std::string& spec, int points);
    int getSpecializationLevel(const std::string& spec) const;
    
    // Class evolution
    bool canEvolveClass() const;
    void evolveClass(CharacterClass newClass);
    
    // Prestige system
    bool canPrestige() const;
    void prestige();
    
    // Achievement system
    void addAchievement(const std::string& achievement);
    bool hasAchievement(const std::string& achievement) const;
    
    // Getters
    const std::string& getName() const { return name; }
    int getLevel() const { return level; }
    int getExperience() const { return experience; }
    int getPrestigeLevel() const { return prestigeLevel; }
    CharacterClass getCharacterClass() const { return characterClass; }
    
    const CharacterAttributes& getAttributes() const { return attributes; }
    const std::map<std::string, std::shared_ptr<Skill>>& getSkills() const { return skills; }
    const std::map<std::string, std::shared_ptr<Talent>>& getTalents() const { return talents; }
    const ExperienceTracker& getExperienceTracker() const { return experienceTracker; }
    const std::vector<std::string>& getAchievements() const { return achievements; }
};

// Character system manager
class CharacterSystem {
private:
    std::map<std::string, std::shared_ptr<Character>> characters;
    std::map<std::string, std::shared_ptr<Skill>> availableSkills;
    std::map<std::string, std::shared_ptr<Talent>> availableTalents;
    
    std::shared_ptr<EventSystem> eventSystem;
    std::shared_ptr<Logger> logger;
    
public:
    CharacterSystem(std::shared_ptr<EventSystem> eventSystem, std::shared_ptr<Logger> logger);
    
    // Character management
    std::shared_ptr<Character> createCharacter(const std::string& name, CharacterClass cls);
    void removeCharacter(const std::string& name);
    std::shared_ptr<Character> getCharacter(const std::string& name);
    const std::map<std::string, std::shared_ptr<Character>>& getAllCharacters() const;
    
    // Skill and talent registration
    void registerSkill(std::shared_ptr<Skill> skill);
    void registerTalent(std::shared_ptr<Talent> talent);
    
    // Character progression
    void awardExperience(const std::string& characterName, int amount, const std::string& source);
    void awardAchievement(const std::string& characterName, const std::string& achievement);
    
    // System updates
    void update(float deltaTime);
    void saveCharacter(const std::string& name, const std::string& filename);
    void loadCharacter(const std::string& name, const std::string& filename);
    
private:
    void initializeDefaultSkills();
    void initializeDefaultTalents();
    void processCharacterProgression(std::shared_ptr<Character> character, float deltaTime);
};

} // namespace Privanna

#endif // PRIVANNA_CHARACTER_SYSTEM_HPP