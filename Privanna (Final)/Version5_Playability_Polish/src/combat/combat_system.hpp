#ifndef PRIVANNA_COMBAT_SYSTEM_HPP
#define PRIVANNA_COMBAT_SYSTEM_HPP

#include <string>
#include <vector>
#include <map>
#include <memory>
#include <cstdint>
#include "../systems/event_system.hpp"
#include "../utils/logger.hpp"
#include "../character/character_system.hpp"
#include "../faction/faction_relationship_system.hpp"

namespace Privanna {

// Combat types
enum class CombatType {
    MELEE,
    RANGED,
    MAGIC,
    SIEGE,
    NAVAL,
    AERIAL,
    PSYCHIC,
    DIVINE
};

// Unit types from Privanna game
enum class UnitType {
    YOUNGLING,
    WARRIOR,
    ARCHER,
    MAGE,
    CAVALRY,
    BESERKER,
    ASSASSIN,
    HEALER,
    SUMMONER,
    DEMON,
    DJINN,
    ANGEL,
    HORDE
};

// Weapon types
enum class WeaponType {
    SWORD,
    AXE,
    SPEAR,
    BOW,
    CROSSBOW,
    STAFF,
    WAND,
    DAGGER,
    HAMMER,
    POLEARM,
    MAGICAL_FOCUS,
    DIVINE_WEAPON
};

// Combat stance
enum class CombatStance {
    AGGRESSIVE,
    BALANCED,
    DEFENSIVE,
    TACTICAL,
    BERSERK,
    STEALTH,
    RANGED,
    MAGICAL
};

// Damage types
enum class DamageType {
    PHYSICAL,
    FIRE,
    ICE,
    LIGHTNING,
    POISON,
    HOLY,
    SHADOW,
    PSYCHIC,
    PURE
};

// Combat unit
struct CombatUnit {
    std::string name;
    UnitType type;
    int level = 1;
    int health = 100;
    int maxHealth = 100;
    int mana = 50;
    int maxMana = 50;
    int attack = 10;
    int defense = 5;
    int speed = 10;
    int range = 1;
    
    std::map<DamageType, float> resistances;
    std::map<DamageType, float> vulnerabilities;
    
    CombatStance currentStance = CombatStance::BALANCED;
    WeaponType equippedWeapon = WeaponType::SWORD;
    
    std::vector<std::string> abilities;
    std::vector<std::string> statusEffects;
    std::map<std::string, int> cooldowns;
    
    std::shared_ptr<Character> character; // If linked to character
    SpecificFaction faction;
    
    bool isAlive() const { return health > 0; }
    
    void takeDamage(int amount, DamageType type) {
        float multiplier = 1.0f;
        if (resistances.count(type)) multiplier -= resistances[type];
        if (vulnerabilities.count(type)) multiplier += vulnerabilities[type];
        
        int finalDamage = static_cast<int>(amount * multiplier);
        health -= finalDamage;
        if (health < 0) health = 0;
    }
    
    void heal(int amount) {
        health += amount;
        if (health > maxHealth) health = maxHealth;
    }
    
    void restoreMana(int amount) {
        mana += amount;
        if (mana > maxMana) mana = maxMana;
    }
    
    bool canUseAbility(const std::string& ability) const {
        return std::find(abilities.begin(), abilities.end(), ability) != abilities.end() &&
               (!cooldowns.count(ability) || cooldowns.at(ability) == 0);
    }
};

// Combat ability
struct CombatAbility {
    std::string name;
    std::string description;
    DamageType damageType;
    int baseDamage = 0;
    int manaCost = 0;
    int range = 1;
    int cooldown = 0;
    int areaOfEffect = 0; // 0 for single target
    
    std::vector<std::string> statusEffects;
    std::map<std::string, float> modifiers;
    
    bool requiresTarget = true;
    bool canTargetSelf = false;
    bool canTargetAllies = false;
    bool canTargetEnemies = true;
    
    int calculateDamage(const CombatUnit* user) const {
        int damage = baseDamage;
        if (user) {
            damage += user->attack;
            if (user->equippedWeapon == WeaponType::STAFF && damageType == DamageType::FIRE) {
                damage = static_cast<int>(damage * 1.2f); // Staff bonus for fire magic
            }
        }
        return damage;
    }
};

// Status effect
struct StatusEffect {
    std::string name;
    std::string description;
    int duration = 0;
    int stackCount = 1;
    int maxStacks = 1;
    
    std::map<std::string, float> statModifiers;
    std::vector<std::string> damageOverTime;
    int damagePerTurn = 0;
    DamageType damageType = DamageType::PHYSICAL;
    
    bool isPositive = false;
    bool isDispellable = true;
    
    void apply(CombatUnit* target) {
        if (!target) return;
        
        for (const auto& modifier : statModifiers) {
            // Apply stat modifications
            if (modifier.first == "health") {
                target->health = static_cast<int>(target->health * modifier.second);
            } else if (modifier.first == "attack") {
                target->attack = static_cast<int>(target->attack * modifier.second);
            } else if (modifier.first == "defense") {
                target->defense = static_cast<int>(target->defense * modifier.second);
            } else if (modifier.first == "speed") {
                target->speed = static_cast<int>(target->speed * modifier.second);
            }
        }
    }
    
    void tick(CombatUnit* target) {
        if (!target) return;
        
        if (damagePerTurn > 0) {
            target->takeDamage(damagePerTurn, damageType);
        }
        
        duration--;
        if (duration <= 0) {
            remove(target);
        }
    }
    
    void remove(CombatUnit* target) {
        if (!target) return;
        
        // Remove status effect from target
        auto it = std::find(target->statusEffects.begin(), target->statusEffects.end(), name);
        if (it != target->statusEffects.end()) {
            target->statusEffects.erase(it);
        }
    }
};

// Combat formation
struct CombatFormation {
    std::string name;
    std::vector<std::vector<int>> unitPositions; // Grid positions
    std::map<std::string, float> formationBonuses;
    std::vector<std::string> requiredUnits;
    
    float getBonus(const std::string& bonusType) const {
        if (formationBonuses.count(bonusType)) {
            return formationBonuses.at(bonusType);
        }
        return 1.0f;
    }
};

// Combat environment
struct CombatEnvironment {
    std::string name;
    std::string description;
    int width = 20;
    int height = 20;
    
    std::map<DamageType, float> elementalModifiers;
    std::map<std::string, float> terrainModifiers;
    std::vector<std::string> environmentalHazards;
    
    float getDamageModifier(DamageType type) const {
        if (elementalModifiers.count(type)) {
            return elementalModifiers.at(type);
        }
        return 1.0f;
    }
};

// Combat encounter
class Combat {
private:
    std::string name;
    CombatType type;
    CombatEnvironment environment;
    
    std::vector<std::shared_ptr<CombatUnit>> playerUnits;
    std::vector<std::shared_ptr<CombatUnit>> enemyUnits;
    std::vector<std::shared_ptr<CombatUnit>> allUnits;
    
    std::map<std::string, std::shared_ptr<CombatAbility>> availableAbilities;
    std::map<std::string, std::shared_ptr<StatusEffect>> activeStatusEffects;
    
    std::vector<std::shared_ptr<CombatFormation>> formations;
    
    int currentTurn = 0;
    bool isPlayerTurn = true;
    bool isCombatActive = false;
    
    std::vector<std::string> combatLog;
    
public:
    Combat(const std::string& name, CombatType type, const CombatEnvironment& env);
    
    // Unit management
    void addPlayerUnit(std::shared_ptr<CombatUnit> unit);
    void addEnemyUnit(std::shared_ptr<CombatUnit> unit);
    void removeUnit(const std::string& unitName);
    std::shared_ptr<CombatUnit> getUnit(const std::string& name);
    
    // Formation management
    void setFormation(const std::string& formationName);
    void updateFormationPositions();
    
    // Combat mechanics
    void startCombat();
    void endCombat();
    void nextTurn();
    
    // Actions
    bool attack(const std::string& attackerName, const std::string& targetName);
    bool useAbility(const std::string& unitName, const std::string& abilityName, const std::string& targetName = "");
    bool moveUnit(const std::string& unitName, int x, int y);
    void changeStance(const std::string& unitName, CombatStance newStance);
    
    // Status effects
    void applyStatusEffect(const std::string& unitName, std::shared_ptr<StatusEffect> effect);
    void updateStatusEffects();
    
    // AI actions
    void executeAITurn();
    void executeUnitAI(std::shared_ptr<CombatUnit> unit);
    
    // Combat calculations
    int calculateDamage(const CombatUnit* attacker, const CombatUnit* target, const CombatAbility* ability = nullptr);
    float calculateHitChance(const CombatUnit* attacker, const CombatUnit* target);
    bool isTargetInRange(const CombatUnit* attacker, const CombatUnit* target, const CombatAbility* ability = nullptr);
    
    // Combat state
    bool isCombatOver() const;
    bool isPlayerVictory() const;
    std::vector<std::shared_ptr<CombatUnit>> getAliveUnits(bool playerUnits = true) const;
    
    // Combat log
    void addToCombatLog(const std::string& message);
    const std::vector<std::string>& getCombatLog() const { return combatLog; }
    
    // Getters
    const std::string& getName() const { return name; }
    CombatType getType() const { return type; }
    int getCurrentTurn() const { return currentTurn; }
    bool isPlayerTurnActive() const { return isPlayerTurn; }
    bool isActive() const { return isCombatActive; }
    const std::vector<std::shared_ptr<CombatUnit>>& getPlayerUnits() const { return playerUnits; }
    const std::vector<std::shared_ptr<CombatUnit>>& getEnemyUnits() const { return enemyUnits; }
};

// Combat system manager
class CombatSystem {
private:
    std::map<std::string, std::shared_ptr<Combat>> activeCombats;
    std::map<std::string, std::shared_ptr<CombatAbility>> allAbilities;
    std::map<std::string, std::shared_ptr<StatusEffect>> allStatusEffects;
    std::map<std::string, std::shared_ptr<CombatFormation>> allFormations;
    std::map<std::string, std::shared_ptr<CombatEnvironment>> allEnvironments;
    
    std::shared_ptr<EventSystem> eventSystem;
    std::shared_ptr<Logger> logger;
    
public:
    CombatSystem(std::shared_ptr<EventSystem> eventSystem, std::shared_ptr<Logger> logger);
    
    // Combat creation
    std::shared_ptr<Combat> createCombat(const std::string& name, CombatType type, const std::string& environmentName);
    void removeCombat(const std::string& name);
    std::shared_ptr<Combat> getCombat(const std::string& name);
    
    // Unit creation
    std::shared_ptr<CombatUnit> createUnit(const std::string& name, UnitType type, SpecificFaction faction, int level = 1);
    std::shared_ptr<CombatUnit> createUnitFromCharacter(std::shared_ptr<Character> character);
    
    // Ability and effect registration
    void registerAbility(std::shared_ptr<CombatAbility> ability);
    void registerStatusEffect(std::shared_ptr<StatusEffect> effect);
    void registerFormation(std::shared_ptr<CombatFormation> formation);
    void registerEnvironment(std::shared_ptr<CombatEnvironment> environment);
    
    // Combat execution
    void startCombat(const std::string& combatName);
    void processCombatTurn(const std::string& combatName);
    void endCombat(const std::string& combatName);
    
    // Warfare mechanics
    void processLargeScaleBattle(SpecificFaction faction1, SpecificFaction faction2, const std::string& location);
    void processSiege(const std::string& location, SpecificFaction attackers, SpecificFaction defenders);
    void processNavalBattle(const std::string& navalZone, SpecificFaction faction1, SpecificFaction faction2);
    
    // Military command
    void issueCommand(SpecificFaction faction, const std::string& command, const std::vector<std::string>& targets);
    void executeBattleStrategy(SpecificFaction faction, const std::map<std::string, int>& unitDeployments);
    void processTacticalRetreat(SpecificFaction faction, const std::string& location);
    
    // System updates
    void update(float deltaTime);
    void processAllCombats(float deltaTime);
    
    // Analytics and statistics
    std::map<SpecificFaction, int> calculateMilitaryStrength();
    std::map<std::string, int> getCombatStatistics();
    std::vector<std::string> getActiveCombatLocations();
    
private:
    void initializeDefaultAbilities();
    void initializeDefaultStatusEffects();
    void initializeDefaultFormations();
    void initializeDefaultEnvironments();
    void processCombatAI(std::shared_ptr<Combat> combat);
    void handleCombatEnd(std::shared_ptr<Combat> combat);
    void updateMilitaryRelationships(SpecificFaction victor, SpecificFaction defeated);
};

} // namespace Privanna

#endif // PRIVANNA_COMBAT_SYSTEM_HPP