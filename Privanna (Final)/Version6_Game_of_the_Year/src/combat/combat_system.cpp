#include "combat_system.hpp"
#include <algorithm>
#include <random>
#include <sstream>
#include <iomanip>

namespace Privanna {

// Combat implementation
Combat::Combat(const std::string& name, CombatType type, const CombatEnvironment& env)
    : name(name), type(type), environment(env) {
    
    // Initialize combat based on type
    switch (type) {
        case CombatType::MELEE:
            // Close-quarters combat setup
            break;
        case CombatType::RANGED:
            // Ranged combat setup with larger range
            break;
        case CombatType::MAGIC:
            // Magical combat with mana focus
            break;
        case CombatType::SIEGE:
            // Siege warfare with fortifications
            break;
        case CombatType::NAVAL:
            // Naval combat on water
            break;
        case CombatType::AERIAL:
            // Aerial combat with flying units
            break;
        case CombatType::PSYCHIC:
            // Psychic combat with mental effects
            break;
        case CombatType::DIVINE:
            // Divine combat with holy/unholy powers
            break;
    }
}

void Combat::addPlayerUnit(std::shared_ptr<CombatUnit> unit) {
    playerUnits.push_back(unit);
    allUnits.push_back(unit);
    
    // Set initial position
    unit->position = {1, environment.height / 2};
    
    addToCombatLog(unit->name + " joined the combat (Player)");
}

void Combat::addEnemyUnit(std::shared_ptr<CombatUnit> unit) {
    enemyUnits.push_back(unit);
    allUnits.push_back(unit);
    
    // Set initial position
    unit->position = {environment.width - 2, environment.height / 2};
    
    addToCombatLog(unit->name + " joined the combat (Enemy)");
}

void Combat::removeUnit(const std::string& unitName) {
    auto removeFromVector = [&](std::vector<std::shared_ptr<CombatUnit>>& units) {
        units.erase(
            std::remove_if(units.begin(), units.end(),
                [&unitName](const std::shared_ptr<CombatUnit>& unit) {
                    return unit->name == unitName;
                }),
            units.end()
        );
    };
    
    removeFromVector(playerUnits);
    removeFromVector(enemyUnits);
    removeFromVector(allUnits);
    
    addToCombatLog(unitName + " was removed from combat");
}

std::shared_ptr<CombatUnit> Combat::getUnit(const std::string& name) {
    for (auto& unit : allUnits) {
        if (unit->name == name) {
            return unit;
        }
    }
    return nullptr;
}

void Combat::startCombat() {
    isCombatActive = true;
    currentTurn = 0;
    isPlayerTurn = true;
    
    addToCombatLog("Combat started: " + name);
    
    // Apply initial formation bonuses
    updateFormationPositions();
    
    // Sort units by speed for turn order
    std::sort(allUnits.begin(), allUnits.end(), 
        [](const std::shared_ptr<CombatUnit>& a, const std::shared_ptr<CombatUnit>& b) {
            return a->speed > b->speed;
        });
}

void Combat::endCombat() {
    isCombatActive = false;
    addToCombatLog("Combat ended");
}

void Combat::nextTurn() {
    currentTurn++;
    isPlayerTurn = !isPlayerTurn;
    
    // Update cooldowns
    for (auto& unit : allUnits) {
        for (auto& cooldown : unit->cooldowns) {
            if (cooldown.second > 0) {
                cooldown.second--;
            }
        }
    }
    
    // Update status effects
    updateStatusEffects();
    
    addToCombatLog("Turn " + std::to_string(currentTurn) + " - " + (isPlayerTurn ? "Player" : "Enemy") + " phase");
    
    // Check if combat is over
    if (isCombatOver()) {
        endCombat();
    }
}

bool Combat::attack(const std::string& attackerName, const std::string& targetName) {
    auto attacker = getUnit(attackerName);
    auto target = getUnit(targetName);
    
    if (!attacker || !target || !attacker->isAlive() || !target->isAlive()) {
        return false;
    }
    
    if (!isTargetInRange(attacker, target, nullptr)) {
        addToCombatLog(attackerName + " is too far from " + targetName);
        return false;
    }
    
    float hitChance = calculateHitChance(attacker, target);
    bool hits = (rand() % 100) < (hitChance * 100);
    
    if (hits) {
        int damage = calculateDamage(attacker, target);
        target->takeDamage(damage, DamageType::PHYSICAL);
        
        addToCombatLog(attackerName + " hits " + targetName + " for " + std::to_string(damage) + " damage");
        
        if (!target->isAlive()) {
            addToCombatLog(targetName + " has been defeated!");
        }
    } else {
        addToCombatLog(attackerName + " misses " + targetName);
    }
    
    return true;
}

bool Combat::useAbility(const std::string& unitName, const std::string& abilityName, const std::string& targetName) {
    auto unit = getUnit(unitName);
    if (!unit || !availableAbilities.count(abilityName)) {
        return false;
    }
    
    auto ability = availableAbilities[abilityName];
    
    if (!unit->canUseAbility(abilityName)) {
        return false;
    }
    
    if (unit->mana < ability->manaCost) {
        addToCombatLog(unitName + " doesn't have enough mana for " + abilityName);
        return false;
    }
    
    std::shared_ptr<CombatUnit> target = nullptr;
    if (ability->requiresTarget && !targetName.empty()) {
        target = getUnit(targetName);
        if (!target) {
            return false;
        }
    }
    
    // Consume mana
    unit->mana -= ability->manaCost;
    
    // Set cooldown
    unit->cooldowns[abilityName] = ability->cooldown;
    
    // Apply ability effects
    if (target) {
        int damage = ability->calculateDamage(unit);
        target->takeDamage(damage, ability->damageType);
        
        // Apply status effects
        for (const auto& effectName : ability->statusEffects) {
            if (allStatusEffects.count(effectName)) {
                applyStatusEffect(targetName, allStatusEffects[effectName]);
            }
        }
        
        addToCombatLog(unitName + " uses " + abilityName + " on " + targetName + " for " + std::to_string(damage) + " damage");
    } else {
        addToCombatLog(unitName + " uses " + abilityName);
    }
    
    return true;
}

bool Combat::moveUnit(const std::string& unitName, int x, int y) {
    auto unit = getUnit(unitName);
    if (!unit) {
        return false;
    }
    
    // Check if position is valid
    if (x < 0 || x >= environment.width || y < 0 || y >= environment.height) {
        return false;
    }
    
    // Check if position is occupied
    for (auto& other : allUnits) {
        if (other != unit && other->position.first == x && other->position.second == y) {
            return false;
        }
    }
    
    unit->position = {x, y};
    addToCombatLog(unitName + " moved to position (" + std::to_string(x) + ", " + std::to_string(y) + ")");
    
    return true;
}

void Combat::changeStance(const std::string& unitName, CombatStance newStance) {
    auto unit = getUnit(unitName);
    if (!unit) {
        return;
    }
    
    unit->currentStance = newStance;
    
    // Apply stance modifiers
    switch (newStance) {
        case CombatStance::AGGRESSIVE:
            unit->attack = static_cast<int>(unit->attack * 1.2f);
            unit->defense = static_cast<int>(unit->defense * 0.8f);
            break;
        case CombatStance::DEFENSIVE:
            unit->attack = static_cast<int>(unit->attack * 0.8f);
            unit->defense = static_cast<int>(unit->defense * 1.3f);
            break;
        case CombatStance::BERSERK:
            unit->attack = static_cast<int>(unit->attack * 1.5f);
            unit->defense = static_cast<int>(unit->defense * 0.5f);
            break;
        case CombatStance::TACTICAL:
            unit->speed = static_cast<int>(unit->speed * 1.2f);
            break;
        default:
            break;
    }
    
    addToCombatLog(unitName + " changed stance to " + std::to_string(static_cast<int>(newStance)));
}

void Combat::applyStatusEffect(const std::string& unitName, std::shared_ptr<StatusEffect> effect) {
    auto unit = getUnit(unitName);
    if (!unit || !effect) {
        return;
    }
    
    // Check if effect already exists
    auto existing = std::find(unit->statusEffects.begin(), unit->statusEffects.end(), effect->name);
    if (existing != unit->statusEffects.end()) {
        // Stack effect if possible
        auto effectData = activeStatusEffects[effect->name];
        if (effectData && effectData->stackCount < effectData->maxStacks) {
            effectData->stackCount++;
        }
    } else {
        unit->statusEffects.push_back(effect->name);
        activeStatusEffects[effect->name] = effect;
        effect->apply(unit.get());
    }
    
    addToCombatLog(effect->name + " applied to " + unitName);
}

void Combat::updateStatusEffects() {
    std::vector<std::string> effectsToRemove;
    
    for (auto& pair : activeStatusEffects) {
        auto effect = pair.second;
        auto unitName = pair.first;
        auto unit = getUnit(unitName);
        
        if (unit) {
            effect->tick(unit.get());
            
            if (effect->duration <= 0) {
                effectsToRemove.push_back(pair.first);
            }
        }
    }
    
    for (const auto& effectName : effectsToRemove) {
        activeStatusEffects.erase(effectName);
    }
}

void Combat::executeAITurn() {
    for (auto& unit : enemyUnits) {
        if (unit->isAlive()) {
            executeUnitAI(unit);
        }
    }
}

void Combat::executeUnitAI(std::shared_ptr<CombatUnit> unit) {
    if (!unit->isAlive()) return;
    
    // Find nearest enemy
    std::shared_ptr<CombatUnit> nearestEnemy = nullptr;
    int minDistance = INT_MAX;
    
    for (auto& enemy : playerUnits) {
        if (enemy->isAlive()) {
            int distance = abs(unit->position.first - enemy->position.first) + 
                          abs(unit->position.second - enemy->position.second);
            if (distance < minDistance) {
                minDistance = distance;
                nearestEnemy = enemy;
            }
        }
    }
    
    if (!nearestEnemy) return;
    
    // AI decision making
    if (minDistance <= unit->range) {
        // Attack if in range
        attack(unit->name, nearestEnemy->name);
        
        // Try to use abilities
        for (const auto& ability : unit->abilities) {
            if (unit->canUseAbility(ability)) {
                useAbility(unit->name, ability, nearestEnemy->name);
                break; // Use one ability per turn
            }
        }
    } else {
        // Move towards enemy
        int dx = (nearestEnemy->position.first > unit->position.first) ? 1 : -1;
        int dy = (nearestEnemy->position.second > unit->position.second) ? 1 : -1;
        
        int newX = unit->position.first + dx;
        int newY = unit->position.second + dy;
        
        moveUnit(unit->name, newX, newY);
    }
}

int Combat::calculateDamage(const CombatUnit* attacker, const CombatUnit* target, const CombatAbility* ability) {
    int baseDamage = ability ? ability->calculateDamage(attacker) : attacker->attack;
    
    // Apply stance modifiers
    switch (attacker->currentStance) {
        case CombatStance::AGGRESSIVE:
            baseDamage = static_cast<int>(baseDamage * 1.2f);
            break;
        case CombatStance::BERSERK:
            baseDamage = static_cast<int>(baseDamage * 1.5f);
            break;
        default:
            break;
    }
    
    // Apply target defense
    int defense = target->defense;
    switch (target->currentStance) {
        case CombatStance::DEFENSIVE:
            defense = static_cast<int>(defense * 1.3f);
            break;
        default:
            break;
    }
    
    int finalDamage = baseDamage - defense / 2;
    if (finalDamage < 1) finalDamage = 1;
    
    return finalDamage;
}

float Combat::calculateHitChance(const CombatUnit* attacker, const CombatUnit* target) {
    float baseChance = 0.8f; // 80% base hit chance
    
    // Speed difference affects hit chance
    int speedDiff = attacker->speed - target->speed;
    float speedModifier = speedDiff * 0.02f; // 2% per speed point
    
    // Stance modifiers
    switch (attacker->currentStance) {
        case CombatStance::TACTICAL:
            speedModifier += 0.1f; // +10% hit chance
            break;
        case CombatStance::BERSERK:
            speedModifier -= 0.1f; // -10% hit chance
            break;
        default:
            break;
    }
    
    float finalChance = baseChance + speedModifier;
    if (finalChance > 0.95f) finalChance = 0.95f;
    if (finalChance < 0.1f) finalChance = 0.1f;
    
    return finalChance;
}

bool Combat::isTargetInRange(const CombatUnit* attacker, const CombatUnit* target, const CombatAbility* ability) {
    if (!attacker || !target) return false;
    
    int range = ability ? ability->range : attacker->range;
    int distance = abs(attacker->position.first - target->position.first) + 
                  abs(attacker->position.second - target->position.second);
    
    return distance <= range;
}

bool Combat::isCombatOver() const {
    bool playerAlive = false;
    bool enemyAlive = false;
    
    for (const auto& unit : playerUnits) {
        if (unit->isAlive()) {
            playerAlive = true;
            break;
        }
    }
    
    for (const auto& unit : enemyUnits) {
        if (unit->isAlive()) {
            enemyAlive = true;
            break;
        }
    }
    
    return !playerAlive || !enemyAlive;
}

bool Combat::isPlayerVictory() const {
    for (const auto& unit : enemyUnits) {
        if (unit->isAlive()) {
            return false;
        }
    }
    return true;
}

std::vector<std::shared_ptr<CombatUnit>> Combat::getAliveUnits(bool playerUnits) const {
    std::vector<std::shared_ptr<CombatUnit>> aliveUnits;
    
    const auto& units = playerUnits ? this->playerUnits : this->enemyUnits;
    for (const auto& unit : units) {
        if (unit->isAlive()) {
            aliveUnits.push_back(unit);
        }
    }
    
    return aliveUnits;
}

void Combat::addToCombatLog(const std::string& message) {
    combatLog.push_back(message);
    if (combatLog.size() > 100) {
        combatLog.erase(combatLog.begin());
    }
}

void Combat::updateFormationPositions() {
    // Update unit positions based on current formation
    // This would implement formation-specific positioning logic
}

void Combat::setFormation(const std::string& formationName) {
    // Apply formation bonuses and positioning
    // This would look up the formation and apply its effects
}

// CombatSystem implementation
CombatSystem::CombatSystem(std::shared_ptr<EventSystem> eventSystem, std::shared_ptr<Logger> logger)
    : eventSystem(eventSystem), logger(logger) {
    
    initializeDefaultAbilities();
    initializeDefaultStatusEffects();
    initializeDefaultFormations();
    initializeDefaultEnvironments();
}

std::shared_ptr<Combat> CombatSystem::createCombat(const std::string& name, CombatType type, const std::string& environmentName) {
    if (!allEnvironments.count(environmentName)) {
        logger->error("Environment not found: " + environmentName);
        return nullptr;
    }
    
    auto combat = std::make_shared<Combat>(name, type, *allEnvironments[environmentName]);
    activeCombats[name] = combat;
    
    logger->info("Created combat: " + name + " of type " + std::to_string(static_cast<int>(type)));
    
    return combat;
}

std::shared_ptr<CombatUnit> CombatSystem::createUnit(const std::string& name, UnitType type, SpecificFaction faction, int level) {
    auto unit = std::make_shared<CombatUnit>();
    unit->name = name;
    unit->type = type;
    unit->faction = faction;
    unit->level = level;
    
    // Set base stats based on unit type
    switch (type) {
        case UnitType::YOUNGLING:
            unit->health = unit->maxHealth = 50;
            unit->attack = 5;
            unit->defense = 3;
            unit->speed = 8;
            break;
        case UnitType::WARRIOR:
            unit->health = unit->maxHealth = 120;
            unit->attack = 15;
            unit->defense = 12;
            unit->speed = 6;
            break;
        case UnitType::ARCHER:
            unit->health = unit->maxHealth = 80;
            unit->attack = 12;
            unit->defense = 6;
            unit->speed = 10;
            unit->range = 5;
            break;
        case UnitType::MAGE:
            unit->health = unit->maxHealth = 70;
            unit->mana = unit->maxMana = 100;
            unit->attack = 8;
            unit->defense = 4;
            unit->speed = 7;
            unit->range = 4;
            break;
        case UnitType::BESERKER:
            unit->health = unit->maxHealth = 140;
            unit->attack = 20;
            unit->defense = 8;
            unit->speed = 9;
            break;
        case UnitType::ASSASSIN:
            unit->health = unit->maxHealth = 90;
            unit->attack = 14;
            unit->defense = 5;
            unit->speed = 15;
            break;
        case UnitType::HEALER:
            unit->health = unit->maxHealth = 85;
            unit->mana = unit->maxMana = 80;
            unit->attack = 6;
            unit->defense = 8;
            unit->speed = 7;
            break;
        case UnitType::DEMON:
            unit->health = unit->maxHealth = 150;
            unit->attack = 18;
            unit->defense = 15;
            unit->speed = 8;
            break;
        case UnitType::DJINN:
            unit->health = unit->maxHealth = 110;
            unit->mana = unit->maxMana = 120;
            unit->attack = 14;
            unit->defense = 10;
            unit->speed = 12;
            break;
        case UnitType::HORDE:
            unit->health = unit->maxHealth = 60;
            unit->attack = 10;
            unit->defense = 4;
            unit->speed = 11;
            break;
    }
    
    // Scale stats by level
    float levelMultiplier = 1.0f + (level - 1) * 0.15f;
    unit->maxHealth = static_cast<int>(unit->maxHealth * levelMultiplier);
    unit->health = unit->maxHealth;
    unit->maxMana = static_cast<int>(unit->maxMana * levelMultiplier);
    unit->mana = unit->maxMana;
    unit->attack = static_cast<int>(unit->attack * levelMultiplier);
    unit->defense = static_cast<int>(unit->defense * levelMultiplier);
    
    // Add default abilities based on type
    switch (type) {
        case UnitType::WARRIOR:
            unit->abilities = {"Power Strike", "Shield Bash"};
            unit->equippedWeapon = WeaponType::SWORD;
            break;
        case UnitType::ARCHER:
            unit->abilities = {"Precise Shot", "Multi Shot"};
            unit->equippedWeapon = WeaponType::BOW;
            break;
        case UnitType::MAGE:
            unit->abilities = {"Fireball", "Magic Missile", "Lightning Bolt"};
            unit->equippedWeapon = WeaponType::STAFF;
            break;
        case UnitType::HEALER:
            unit->abilities = {"Heal", "Restore Mana", "Cleanse"};
            unit->equippedWeapon = WeaponType::WAND;
            break;
        case UnitType::ASSASSIN:
            unit->abilities = {"Backstab", "Stealth", "Poison Blade"};
            unit->equippedWeapon = WeaponType::DAGGER;
            break;
        case UnitType::DEMON:
            unit->abilities = {"Hellfire", "Intimidate", "Demonic Rage"};
            unit->equippedWeapon = WeaponType::DEMONIC_WEAPON;
            break;
        case UnitType::DJINN:
            unit->abilities = {"Wish", "Teleport", "Elemental Blast"};
            unit->equippedWeapon = WeaponType::MAGICAL_FOCUS;
            break;
        default:
            unit->abilities = {"Basic Attack"};
            break;
    }
    
    logger->info("Created unit: " + name + " of type " + std::to_string(static_cast<int>(type)));
    
    return unit;
}

void CombatSystem::update(float deltaTime) {
    processAllCombats(deltaTime);
}

void CombatSystem::processAllCombats(float deltaTime) {
    std::vector<std::string> finishedCombats;
    
    for (auto& pair : activeCombats) {
        auto combat = pair.second;
        
        if (combat->isActive()) {
            if (!combat->isPlayerTurnActive()) {
                executeAITurn(combat);
                combat->nextTurn();
            }
            
            if (!combat->isActive()) {
                finishedCombats.push_back(pair.first);
                handleCombatEnd(combat);
            }
        }
    }
    
    // Remove finished combats
    for (const auto& name : finishedCombats) {
        activeCombats.erase(name);
    }
}

void CombatSystem::executeAITurn(std::shared_ptr<Combat> combat) {
    combat->executeAITurn();
}

void CombatSystem::handleCombatEnd(std::shared_ptr<Combat> combat) {
    if (combat->isPlayerVictory()) {
        logger->info("Player victory in combat: " + combat->getName());
        
        if (eventSystem) {
            eventSystem->fireEvent("combat_victory", combat->getName());
        }
    } else {
        logger->info("Enemy victory in combat: " + combat->getName());
        
        if (eventSystem) {
            eventSystem->fireEvent("combat_defeat", combat->getName());
        }
    }
}

void CombatSystem::initializeDefaultAbilities() {
    // Combat abilities
    auto powerStrike = std::make_shared<CombatAbility>();
    powerStrike->name = "Power Strike";
    powerStrike->description = "A powerful melee attack";
    powerStrike->damageType = DamageType::PHYSICAL;
    powerStrike->baseDamage = 20;
    powerStrike->cooldown = 2;
    allAbilities["Power Strike"] = powerStrike;
    
    auto fireball = std::make_shared<CombatAbility>();
    fireball->name = "Fireball";
    fireball->description = "Launches a fireball at the target";
    fireball->damageType = DamageType::FIRE;
    fireball->baseDamage = 25;
    fireball->manaCost = 15;
    fireball->range = 5;
    fireball->cooldown = 1;
    allAbilities["Fireball"] = fireball;
    
    auto heal = std::make_shared<CombatAbility>();
    heal->name = "Heal";
    heal->description = "Restores health to an ally";
    heal->damageType = DamageType::HOLY;
    heal->baseDamage = -30; // Negative for healing
    heal->manaCost = 10;
    heal->range = 3;
    heal->cooldown = 1;
    heal->canTargetAllies = true;
    heal->canTargetEnemies = false;
    allAbilities["Heal"] = heal;
}

void CombatSystem::initializeDefaultStatusEffects() {
    auto poison = std::make_shared<StatusEffect>();
    poison->name = "Poison";
    poison->description = "Takes damage over time";
    poison->duration = 5;
    poison->damagePerTurn = 5;
    poison->damageType = DamageType::POISON;
    allStatusEffects["Poison"] = poison;
    
    auto regeneration = std::make_shared<StatusEffect>();
    regeneration->name = "Regeneration";
    regeneration->description = "Heals over time";
    regeneration->duration = 5;
    regeneration->damagePerTurn = -8; // Negative for healing
    regeneration->damageType = DamageType::PHYSICAL;
    regeneration->isPositive = true;
    allStatusEffects["Regeneration"] = regeneration;
}

void CombatSystem::initializeDefaultFormations() {
    auto lineFormation = std::make_shared<CombatFormation>();
    lineFormation->name = "Line";
    lineFormation->formationBonuses["defense"] = 1.2f;
    lineFormation->formationBonuses["attack"] = 1.1f;
    allFormations["Line"] = lineFormation;
    
    auto wedgeFormation = std::make_shared<CombatFormation>();
    wedgeFormation->name = "Wedge";
    wedgeFormation->formationBonuses["attack"] = 1.3f;
    wedgeFormation->formationBonuses["speed"] = 1.2f;
    allFormations["Wedge"] = wedgeFormation;
}

void CombatSystem::initializeDefaultEnvironments() {
    auto plains = std::make_shared<CombatEnvironment>();
    plains->name = "Plains";
    plains->description = "Open grassland with no cover";
    plains->width = 25;
    plains->height = 20;
    plains->elementalModifiers[DamageType::LIGHTNING] = 1.1f;
    allEnvironments["Plains"] = plains;
    
    auto dungeon = std::make_shared<CombatEnvironment>();
    dungeon->name = "Dungeon";
    dungeon->description = "Dark corridors with limited visibility";
    dungeon->width = 15;
    dungeon->height = 15;
    dungeon->elementalModifiers[DamageType::SHADOW] = 1.3f;
    dungeon->elementalModifiers[DamageType::HOLY] = 0.8f;
    dungeon->terrainModifiers["movement"] = 0.8f;
    allEnvironments["Dungeon"] = dungeon;
    
    auto battlefield = std::make_shared<CombatEnvironment>();
    battlefield->name = "Battlefield";
    battlefield->description = "War-torn landscape with fortifications";
    battlefield->width = 30;
    battlefield->height = 25;
    battlefield->terrainModifiers["defense_bonus"] = 1.2f;
    allEnvironments["Battlefield"] = battlefield;
}

} // namespace Privanna