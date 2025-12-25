#include "character_system.hpp"
#include <algorithm>
#include <fstream>
#include <sstream>
#include <random>

namespace Privanna {

// Character implementation
Character::Character(const std::string& name, CharacterClass cls) 
    : name(name), characterClass(cls) {
    
    // Initialize base attributes based on class
    switch (cls) {
        case CharacterClass::WARRIOR:
            attributes.setAttribute(Attribute::STRENGTH, 15);
            attributes.setAttribute(Attribute::CONSTITUTION, 14);
            attributes.setAttribute(Attribute::DEXTERITY, 12);
            attributes.setAttribute(Attribute::INTELLIGENCE, 8);
            break;
        case CharacterClass::MAGE:
            attributes.setAttribute(Attribute::INTELLIGENCE, 15);
            attributes.setAttribute(Attribute::WISDOM, 14);
            attributes.setAttribute(Attribute::WILLPOWER, 13);
            attributes.setAttribute(Attribute::STRENGTH, 8);
            break;
        case CharacterClass::DIPLOMAT:
            attributes.setAttribute(Attribute::CHARISMA, 15);
            attributes.setAttribute(Attribute::WISDOM, 14);
            attributes.setAttribute(Attribute::INTELLIGENCE, 12);
            attributes.setAttribute(Attribute::FAITH, 11);
            break;
        case CharacterClass::MERCHANT:
            attributes.setAttribute(Attribute::CHARISMA, 13);
            attributes.setAttribute(Attribute::INTELLIGENCE, 13);
            attributes.setAttribute(Attribute::LUCK, 12);
            attributes.setAttribute(Attribute::WISDOM, 11);
            break;
        case CharacterClass::EXPLORER:
            attributes.setAttribute(Attribute::PERCEPTION, 15);
            attributes.setAttribute(Attribute::AGILITY, 14);
            attributes.setAttribute(Attribute::ENDURANCE, 13);
            attributes.setAttribute(Attribute::LUCK, 12);
            break;
        case CharacterClass::CRAFTSMAN:
            attributes.setAttribute(Attribute::DEXTERITY, 14);
            attributes.setAttribute(Attribute::INTELLIGENCE, 13);
            attributes.setAttribute(Attribute::WISDOM, 12);
            attributes.setAttribute(Attribute::PERCEPTION, 11);
            break;
        case CharacterClass::LEADER:
            attributes.setAttribute(Attribute::CHARISMA, 15);
            attributes.setAttribute(Attribute::WISDOM, 14);
            attributes.setAttribute(Attribute::WILLPOWER, 13);
            attributes.setAttribute(Attribute::STRENGTH, 12);
            break;
        case CharacterClass::ROGUE:
            attributes.setAttribute(Attribute::AGILITY, 15);
            attributes.setAttribute(Attribute::DEXTERITY, 14);
            attributes.setAttribute(Attribute::LUCK, 13);
            attributes.setAttribute(Attribute::PERCEPTION, 12);
            break;
        case CharacterClass::CLERIC:
            attributes.setAttribute(Attribute::FAITH, 15);
            attributes.setAttribute(Attribute::WISDOM, 14);
            attributes.setAttribute(Attribute::WILLPOWER, 13);
            attributes.setAttribute(Attribute::CHARISMA, 12);
            break;
        case CharacterClass::SCHOLAR:
            attributes.setAttribute(Attribute::INTELLIGENCE, 15);
            attributes.setAttribute(Attribute::WISDOM, 14);
            attributes.setAttribute(Attribute::PERCEPTION, 13);
            attributes.setAttribute(Attribute::CHARISMA, 10);
            break;
    }
    
    // Set default values for all attributes
    std::vector<Attribute> allAttrs = {
        Attribute::STRENGTH, Attribute::DEXTERITY, Attribute::INTELLIGENCE,
        Attribute::WISDOM, Attribute::CHARISMA, Attribute::CONSTITUTION,
        Attribute::PERCEPTION, Attribute::LUCK, Attribute::FAITH,
        Attribute::WILLPOWER, Attribute::AGILITY, Attribute::ENDURANCE
    };
    
    for (auto attr : allAttrs) {
        if (!attributes.primary.count(attr)) {
            attributes.setAttribute(attr, 10);
        }
    }
}

void Character::addExperience(int exp, const std::string& source) {
    experience += exp;
    
    // Track experience by type
    if (source.find("combat") != std::string::npos) {
        experienceTracker.combatExperience[source] += exp;
    } else if (source.find("diplomatic") != std::string::npos) {
        experienceTracker.diplomaticExperience[source] += exp;
    } else if (source.find("economic") != std::string::npos) {
        experienceTracker.economicExperience[source] += exp;
    } else if (source.find("exploration") != std::string::npos) {
        experienceTracker.explorationExperience[source] += exp;
    } else if (source.find("crafting") != std::string::npos) {
        experienceTracker.craftingExperience[source] += exp;
    } else if (source.find("social") != std::string::npos) {
        experienceTracker.socialExperience[source] += exp;
    }
    
    // Check for level up
    while (canLevelUp()) {
        levelUp();
    }
}

bool Character::canLevelUp() const {
    return experience >= getExperienceForNextLevel();
}

int Character::getExperienceForNextLevel() const {
    return level * 1000 + (level * level * 100) + (prestigeLevel * 10000);
}

void Character::levelUp() {
    experience -= getExperienceForNextLevel();
    level++;
    availableAttributePoints += 2;
    skillPoints += 1;
    
    // Add talent points every 3 levels
    if (level % 3 == 0) {
        availableTalentPoints++;
    }
    
    // Improve base attributes based on class
    switch (characterClass) {
        case CharacterClass::WARRIOR:
            attributes.modifyAttribute(Attribute::STRENGTH, 2);
            attributes.modifyAttribute(Attribute::CONSTITUTION, 1);
            break;
        case CharacterClass::MAGE:
            attributes.modifyAttribute(Attribute::INTELLIGENCE, 2);
            attributes.modifyAttribute(Attribute::WISDOM, 1);
            break;
        case CharacterClass::DIPLOMAT:
            attributes.modifyAttribute(Attribute::CHARISMA, 2);
            attributes.modifyAttribute(Attribute::WISDOM, 1);
            break;
        case CharacterClass::MERCHANT:
            attributes.modifyAttribute(Attribute::CHARISMA, 1);
            attributes.modifyAttribute(Attribute::INTELLIGENCE, 1);
            attributes.modifyAttribute(Attribute::LUCK, 1);
            break;
        case CharacterClass::EXPLORER:
            attributes.modifyAttribute(Attribute::PERCEPTION, 1);
            attributes.modifyAttribute(Attribute::AGILITY, 1);
            attributes.modifyAttribute(Attribute::ENDURANCE, 1);
            break;
        case CharacterClass::CRAFTSMAN:
            attributes.modifyAttribute(Attribute::DEXTERITY, 2);
            attributes.modifyAttribute(Attribute::INTELLIGENCE, 1);
            break;
        case CharacterClass::LEADER:
            attributes.modifyAttribute(Attribute::CHARISMA, 2);
            attributes.modifyAttribute(Attribute::WILLPOWER, 1);
            break;
        case CharacterClass::ROGUE:
            attributes.modifyAttribute(Attribute::AGILITY, 2);
            attributes.modifyAttribute(Attribute::DEXTERITY, 1);
            break;
        case CharacterClass::CLERIC:
            attributes.modifyAttribute(Attribute::FAITH, 2);
            attributes.modifyAttribute(Attribute::WISDOM, 1);
            break;
        case CharacterClass::SCHOLAR:
            attributes.modifyAttribute(Attribute::INTELLIGENCE, 2);
            attributes.modifyAttribute(Attribute::WISDOM, 1);
            break;
    }
}

void Character::allocateAttributePoint(Attribute attr) {
    if (availableAttributePoints > 0) {
        attributes.setAttribute(attr, attributes.getAttribute(attr) + 1);
        availableAttributePoints--;
    }
}

void Character::learnSkill(const std::string& skillName) {
    if (skillPoints > 0 && availableSkills.count(skillName)) {
        skills[skillName] = availableSkills[skillName];
        skillPoints--;
    }
}

void Character::upgradeSkill(const std::string& skillName) {
    if (skills.count(skillName)) {
        auto skill = skills[skillName];
        if (skill->level < skill->maxLevel) {
            skillPoints--;
            skill->level++;
        }
    }
}

void Character::useSkill(const std::string& skillName) {
    if (skills.count(skillName)) {
        auto skill = skills[skillName];
        skill->addExperience(10); // Base experience for using skill
    }
}

int Character::getSkillLevel(const std::string& skillName) const {
    if (skills.count(skillName)) {
        return skills.at(skillName)->level;
    }
    return 0;
}

void Character::unlockTalent(const std::string& talentName) {
    if (availableTalentPoints > 0 && availableTalents.count(talentName)) {
        auto talent = availableTalents[talentName];
        if (!talent->isUnlocked) {
            talent->isUnlocked = true;
            availableTalentPoints -= talent->pointsRequired;
        }
    }
}

bool Character::isTalentUnlocked(const std::string& talentName) const {
    if (talents.count(talentName)) {
        return talents.at(talentName)->isUnlocked;
    }
    return false;
}

void Character::addSpecialization(const std::string& spec, int points) {
    specializations[spec] += points;
}

int Character::getSpecializationLevel(const std::string& spec) const {
    if (specializations.count(spec)) {
        return specializations.at(spec);
    }
    return 0;
}

bool Character::canEvolveClass() const {
    return level >= 20 && prestigeLevel == 0;
}

void Character::evolveClass(CharacterClass newClass) {
    if (canEvolveClass()) {
        characterClass = newClass;
        // Grant evolution bonuses
        availableAttributePoints += 5;
        availableTalentPoints += 3;
    }
}

bool Character::canPrestige() const {
    return level >= 50 && prestigeLevel < 10;
}

void Character::prestige() {
    if (canPrestige()) {
        prestigeLevel++;
        level = 1;
        experience = 0;
        
        // Reset some things but keep others
        availableAttributePoints = prestigeLevel * 2;
        availableTalentPoints = prestigeLevel;
        
        // Add prestige achievement
        achievements.push_back("Prestige Level " + std::to_string(prestigeLevel));
    }
}

void Character::addAchievement(const std::string& achievement) {
    if (std::find(achievements.begin(), achievements.end(), achievement) == achievements.end()) {
        achievements.push_back(achievement);
        // Award bonus experience for achievements
        addExperience(100, "achievement_" + achievement);
    }
}

bool Character::hasAchievement(const std::string& achievement) const {
    return std::find(achievements.begin(), achievements.end(), achievement) != achievements.end();
}

// CharacterSystem implementation
CharacterSystem::CharacterSystem(std::shared_ptr<EventSystem> eventSystem, std::shared_ptr<Logger> logger)
    : eventSystem(eventSystem), logger(logger) {
    
    initializeDefaultSkills();
    initializeDefaultTalents();
}

std::shared_ptr<Character> CharacterSystem::createCharacter(const std::string& name, CharacterClass cls) {
    auto character = std::make_shared<Character>(name, cls);
    characters[name] = character;
    
    logger->info("Created character: " + name + " with class: " + std::to_string(static_cast<int>(cls)));
    
    // Fire character creation event
    if (eventSystem) {
        eventSystem->fireEvent("character_created", name);
    }
    
    return character;
}

void CharacterSystem::removeCharacter(const std::string& name) {
    if (characters.count(name)) {
        characters.erase(name);
        logger->info("Removed character: " + name);
        
        if (eventSystem) {
            eventSystem->fireEvent("character_removed", name);
        }
    }
}

std::shared_ptr<Character> CharacterSystem::getCharacter(const std::string& name) {
    if (characters.count(name)) {
        return characters[name];
    }
    return nullptr;
}

const std::map<std::string, std::shared_ptr<Character>>& CharacterSystem::getAllCharacters() const {
    return characters;
}

void CharacterSystem::registerSkill(std::shared_ptr<Skill> skill) {
    availableSkills[skill->name] = skill;
    logger->info("Registered skill: " + skill->name);
}

void CharacterSystem::registerTalent(std::shared_ptr<Talent> talent) {
    availableTalents[talent->name] = talent;
    logger->info("Registered talent: " + talent->name);
}

void CharacterSystem::awardExperience(const std::string& characterName, int amount, const std::string& source) {
    if (characters.count(characterName)) {
        characters[characterName]->addExperience(amount, source);
        logger->info("Awarded " + std::to_string(amount) + " experience to " + characterName + " from " + source);
    }
}

void CharacterSystem::awardAchievement(const std::string& characterName, const std::string& achievement) {
    if (characters.count(characterName)) {
        characters[characterName]->addAchievement(achievement);
        logger->info("Awarded achievement '" + achievement + "' to " + characterName);
    }
}

void CharacterSystem::update(float deltaTime) {
    for (auto& pair : characters) {
        processCharacterProgression(pair.second, deltaTime);
    }
}

void CharacterSystem::saveCharacter(const std::string& name, const std::string& filename) {
    if (characters.count(name)) {
        // Implementation would serialize character data to file
        logger->info("Saved character " + name + " to " + filename);
    }
}

void CharacterSystem::loadCharacter(const std::string& name, const std::string& filename) {
    // Implementation would deserialize character data from file
    logger->info("Loaded character " + name + " from " + filename);
}

void CharacterSystem::initializeDefaultSkills() {
    // Combat skills
    auto swordMastery = std::make_shared<Skill>();
    swordMastery->name = "Sword Mastery";
    swordMastery->type = SkillType::COMBAT;
    swordMastery->description = "Improves effectiveness with sword weapons";
    availableSkills["Sword Mastery"] = swordMastery;
    
    auto magicMissile = std::make_shared<Skill>();
    magicMissile->name = "Magic Missile";
    magicMissile->type = SkillType::MAGIC;
    magicMissile->isActive = true;
    magicMissile->manaCost = 10;
    magicMissile->description = "Launches a magical projectile";
    availableSkills["Magic Missile"] = magicMissile;
    
    // Diplomatic skills
    auto negotiation = std::make_shared<Skill>();
    negotiation->name = "Negotiation";
    negotiation->type = SkillType::DIPLOMACY;
    negotiation->description = "Improves trade and diplomatic outcomes";
    availableSkills["Negotiation"] = negotiation;
    
    // Economic skills
    auto trading = std::make_shared<Skill>();
    trading->name = "Trading";
    trading->type = SkillType::ECONOMIC;
    trading->description = "Better prices and trade opportunities";
    availableSkills["Trading"] = trading;
}

void CharacterSystem::initializeDefaultTalents() {
    // Combat talents
    auto weaponFocus = std::make_shared<Talent>();
    weaponFocus->name = "Weapon Focus";
    weaponFocus->description = "+10% damage with all weapons";
    weaponFocus->tier = 1;
    weaponFocus->effects["damage_multiplier"] = 1.1f;
    availableTalents["Weapon Focus"] = weaponFocus;
    
    // Magic talents
    auto manaAffinity = std::make_shared<Talent>();
    manaAffinity->name = "Mana Affinity";
    manaAffinity->description = "+20% maximum mana";
    manaAffinity->tier = 1;
    manaAffinity->effects["mana_multiplier"] = 1.2f;
    availableTalents["Mana Affinity"] = manaAffinity;
    
    // Social talents
    auto charismatic = std::make_shared<Talent>();
    charismatic->name = "Charismatic";
    charismatic->description = "+15% better diplomatic outcomes";
    charismatic->tier = 1;
    charismatic->effects["diplomacy_bonus"] = 1.15f;
    availableTalents["Charismatic"] = charismatic;
}

void CharacterSystem::processCharacterProgression(std::shared_ptr<Character> character, float deltaTime) {
    // Process passive skill training, talent effects, etc.
    // This would handle skill degradation from disuse, temporary modifiers, etc.
}

} // namespace Privanna