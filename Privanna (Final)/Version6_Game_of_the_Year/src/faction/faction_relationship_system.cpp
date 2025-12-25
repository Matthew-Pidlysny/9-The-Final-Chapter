#include "faction_relationship_system.hpp"
#include <algorithm>
#include <fstream>
#include <sstream>
#include <random>

namespace Privanna {

// Faction implementation
Faction::Faction(SpecificFaction type, const std::string& name, FactionType factionType)
    : factionType(type), name(name), type(factionType) {
    
    // Initialize faction-specific data
    switch (type) {
        case SpecificFaction::LUCIFER_LEGION:
            description = "The mighty legions of Lucifer, masters of strategy and warfare";
            ideology = "Order through strength, honor through conquest";
            culturalTraits = {"Militaristic", "Hierarchical", "Disciplined"};
            power = 150;
            prestige = 80;
            break;
            
        case SpecificFaction::MAMMON_MERCHANTS:
            description = "Wealthy merchants and traders specializing in rare resources";
            ideology = "Wealth is power, trade is freedom";
            culturalTraits = {"Commercial", "Opportunistic", "Influential"};
            power = 120;
            prestige = 90;
            break;
            
        case SpecificFaction::ASMODEUS_COURT:
            description = "Sophisticated nobles focused on diplomacy and intrigue";
            ideology = "Knowledge and manipulation are the ultimate weapons";
            culturalTraits = {"Scholarly", "Intriguing", "Refined"};
            power = 100;
            prestige = 85;
            break;
            
        case SpecificFaction::BEELZEBUB_SWARM:
            description = "Overwhelming forces that dominate through numbers";
            ideology = "Strength in numbers, unity in purpose";
            culturalTraits = {"Collective", "Adaptive", "Persistent"};
            power = 180;
            prestige = 60;
            break;
            
        case SpecificFaction::LEVIATHAN_DEPTHS:
            description = "Mysterious entities from the depths, masters of the unknown";
            ideology = "The depths hold all secrets, all power";
            culturalTraits = {"Mysterious", "Ancient", "Unpredictable"};
            power = 130;
            prestige = 70;
            break;
            
        case SpecificFaction::SATAN_TEMPLE:
            description = "Religious fanatics devoted to their dark faith";
            ideology = "Faith is the path to ultimate power";
            culturalTraits = {"Zealous", "Devotional", "Mystical"};
            power = 110;
            prestige = 75;
            break;
            
        case SpecificFaction::MARID_ROYALTY:
            description = "Noble djinn with magical prowess and ancient wisdom";
            ideology = "Magic is life, wisdom is power";
            culturalTraits = {"Magical", "Noble", "Wise"};
            power = 140;
            prestige = 95;
            break;
            
        case SpecificFaction::IFRIT_WARRIORS:
            description = "Powerful djinn warriors who live for battle";
            ideology = "Honor in combat, glory in victory";
            culturalTraits = {"Warlike", "Honorable", "Passionate"};
            power = 160;
            prestige = 65;
            break;
            
        case SpecificFaction::SHAITAN_TRICKSTERS:
            description = "Cunning djinn who excel at deception and manipulation";
            ideology = "Cunning is the greatest weapon";
            culturalTraits = {"Deceptive", "Cunning", "Adaptive"};
            power = 90;
            prestige = 55;
            break;
            
        case SpecificFaction::IBLIS_REDEEMED:
            description = "The redeemed Iblis, now seeking mercy and redemption";
            ideology = "Through mercy comes redemption, through redemption comes peace";
            culturalTraits = {"Merciful", "Redeemed", "Peaceful"};
            power = 85;
            prestige = 100;
            break;
            
        case SpecificFaction::YUDU_BUAH_GUARDIANS:
            description = "Ancient guardians protecting sacred knowledge";
            ideology = "Knowledge must be protected at all costs";
            culturalTraits = {"Protective", "Ancient", "Guardians"};
            power = 95;
            prestige = 88;
            break;
            
        case SpecificFaction::HUMAN_ROGUES:
            description = "Independent humans who defy all factions";
            ideology = "Freedom is worth any price";
            culturalTraits = {"Independent", "Adaptable", "Survivors"};
            power = 70;
            prestige = 45;
            break;
            
        case SpecificFaction::HORDE:
            description = "Unorganized masses driven by basic instincts";
            ideology = "Survival of the fittest";
            culturalTraits = {"Chaotic", "Primal", "Unpredictable"};
            power = 200;
            prestige = 30;
            break;
    }
    
    // Initialize hierarchy based on faction type
    switch (type) {
        case SpecificFaction::LUCIFER_LEGION:
            hierarchy.leaderTitle = "Supreme Commander";
            hierarchy.rankTitles = {"Recruit", "Soldier", "Sergeant", "Lieutenant", "Captain", "Major", "Colonel", "General", "High General", "Supreme Commander"};
            break;
            
        case SpecificFaction::MARID_ROYALTY:
            hierarchy.leaderTitle = "Sultan";
            hierarchy.rankTitles = {"Citizen", "Scholar", "Advisor", "Vizier", "Prince", "Royal Prince", "Duke", "Grand Duke", "Crown Prince", "Sultan"};
            break;
            
        case SpecificFaction::IBLIS_REDEEMED:
            hierarchy.leaderTitle = "Redeemed One";
            hierarchy.rankTitles = {"Seeker", "Follower", "Disciple", "Acolyte", "Priest", "High Priest", "Bishop", "Archbishop", "Patriarch", "Redeemed One"};
            break;
            
        default:
            hierarchy.leaderTitle = "Leader";
            hierarchy.rankTitles = {"Member", "Veteran", "Elite", "Captain", "Commander", "Warlord", "General", "High Commander", "Supreme", "Leader"};
            break;
    }
}

void Faction::establishRelationship(SpecificFaction target, RelationshipLevel level) {
    if (!relationships.count(target)) {
        relationships[target] = std::make_shared<FactionRelationship>();
        relationships[target]->targetFaction = target;
    }
    
    relationships[target]->currentLevel = level;
    relationships[target]->relationshipPoints = static_cast<int>(level);
    relationships[target]->updateRelationshipLevel();
}

void Faction::modifyRelationship(SpecificFaction target, int points) {
    if (!relationships.count(target)) {
        establishRelationship(target, RelationshipLevel::NEUTRAL);
    }
    relationships[target]->modifyRelationship(points);
}

std::shared_ptr<FactionRelationship> Faction::getRelationship(SpecificFaction target) {
    if (relationships.count(target)) {
        return relationships[target];
    }
    return nullptr;
}

void Faction::setDiplomaticStatus(SpecificFaction target, DiplomaticStatus status) {
    if (!relationships.count(target)) {
        establishRelationship(target, RelationshipLevel::NEUTRAL);
    }
    relationships[target]->diplomaticStatus = status;
}

void Faction::addMember(std::shared_ptr<FactionMember> member) {
    members.push_back(member);
    
    // Assign rank and responsibilities based on member capabilities
    if (member->isLeader) {
        member->rank = hierarchy.maxRank;
        member->title = hierarchy.leaderTitle;
    } else {
        member->rank = 1;
        member->title = hierarchy.getRankTitle(1);
    }
}

void Faction::removeMember(const std::string& name) {
    members.erase(
        std::remove_if(members.begin(), members.end(),
            [&name](const std::shared_ptr<FactionMember>& member) {
                return member->name == name;
            }),
        members.end()
    );
}

void Faction::promoteMember(const std::string& name, int newRank) {
    for (auto& member : members) {
        if (member->name == name) {
            member->promote(newRank);
            member->title = hierarchy.getRankTitle(newRank);
            
            // Assign responsibilities for new rank
            auto responsibilities = hierarchy.getResponsibilities(newRank);
            for (const auto& resp : responsibilities) {
                member->addResponsibility(resp);
            }
            break;
        }
    }
}

std::shared_ptr<FactionMember> Faction::getMember(const std::string& name) {
    for (auto& member : members) {
        if (member->name == name) {
            return member;
        }
    }
    return nullptr;
}

std::shared_ptr<FactionMember> Faction::getLeader() {
    for (auto& member : members) {
        if (member->isLeader) {
            return member;
        }
    }
    return nullptr;
}

void Faction::addTerritory(const std::string& territory, int value) {
    territories[territory] += value;
    power += value / 10; // Territory contributes to power
}

void Faction::removeTerritory(const std::string& territory) {
    if (territories.count(territory)) {
        power -= territories[territory] / 10;
        territories.erase(territory);
    }
}

int Faction::getTotalTerritoryValue() const {
    int total = 0;
    for (const auto& pair : territories) {
        total += pair.second;
    }
    return total;
}

void Faction::updateEconomy(float deltaTime) {
    // Process production
    for (const auto& pair : production) {
        economy.addResource(pair.first, static_cast<int>(pair.second * deltaTime));
    }
    
    // Process consumption
    for (const auto& pair : consumption) {
        economy.removeResource(pair.first, static_cast<int>(pair.second * deltaTime));
    }
    
    // Calculate income and expenses
    economy.incomeRate = 0;
    economy.expenseRate = 0;
    
    for (const auto& pair : production) {
        economy.incomeRate += pair.second;
    }
    
    for (const auto& pair : consumption) {
        economy.expenseRate += pair.second;
    }
}

void Faction::processTrade(SpecificFaction partner, const std::string& resource, int amount) {
    auto relationship = getRelationship(partner);
    if (relationship) {
        float bonus = relationship->getTradeBonus();
        int adjustedAmount = static_cast<int>(amount * bonus);
        
        if (economy.resources[resource] >= amount) {
            economy.removeResource(resource, amount);
            economy.addResource("wealth", adjustedAmount);
            
            relationship->lastInteraction++;
        }
    }
}

bool Faction::canAfford(const std::string& resource, int amount) const {
    return economy.resources.count(resource) && economy.resources.at(resource) >= amount;
}

void Faction::addCulturalTrait(const std::string& trait) {
    if (std::find(culturalTraits.begin(), culturalTraits.end(), trait) == culturalTraits.end()) {
        culturalTraits.push_back(trait);
    }
}

void Faction::addTradition(const std::string& tradition) {
    traditions.push_back(tradition);
}

void Faction::modifySocialNorm(const std::string& norm, int value) {
    socialNorms[norm] += value;
}

void Faction::calculatePower() {
    power = 100;
    power += getTotalTerritoryValue() / 10;
    power += members.size() * 5;
    power += economy.totalWealth / 50;
    power += prestige / 2;
    power += stability / 3;
}

void Faction::calculatePrestige() {
    prestige = 50;
    prestige += culturalTraits.size() * 5;
    prestige += traditions.size() * 3;
    prestige += (relationships.size() * 2);
    
    // Bonus for positive relationships
    for (const auto& pair : relationships) {
        if (pair.second->currentLevel >= RelationshipLevel::FRIENDLY) {
            prestige += 5;
        }
    }
}

void Faction::modifyStability(int amount) {
    stability += amount;
    if (stability > 100) stability = 100;
    if (stability < 0) stability = 0;
}

void Faction::handleDiplomaticEvent(const std::string& eventType, SpecificFaction otherFaction) {
    if (eventType == "trade_success") {
        modifyRelationship(otherFaction, 5);
        modifyStability(2);
    } else if (eventType == "border_conflict") {
        modifyRelationship(otherFaction, -10);
        modifyStability(-5);
    } else if (eventType == "cultural_exchange") {
        modifyRelationship(otherFaction, 8);
        prestige += 3;
    } else if (eventType == "betrayal") {
        modifyRelationship(otherFaction, -25);
        modifyStability(-15);
    }
}

void Faction::makeDecision(const std::string& decisionType) {
    if (decisionType == "military_expansion") {
        power += 20;
        stability -= 5;
        prestige -= 3;
    } else if (decisionType == "diplomatic_peace") {
        stability += 10;
        prestige += 8;
        power -= 5;
    } else if (decisionType == "economic_growth") {
        economy.totalWealth += 100;
        prestige += 5;
        stability += 3;
    }
}

// FactionRelationshipSystem implementation
FactionRelationshipSystem::FactionRelationshipSystem(std::shared_ptr<EventSystem> eventSystem, std::shared_ptr<Logger> logger)
    : eventSystem(eventSystem), logger(logger) {
    
    initializeDefaultFactions();
    setupDefaultHierarchies();
    establishAllRelationships();
}

std::shared_ptr<Faction> FactionRelationshipSystem::createFaction(SpecificFaction type, const std::string& name, FactionType factionType) {
    auto faction = std::make_shared<Faction>(type, name, factionType);
    factions[type] = faction;
    
    logger->info("Created faction: " + name);
    
    if (eventSystem) {
        eventSystem->fireEvent("faction_created", name);
    }
    
    return faction;
}

void FactionRelationshipSystem::removeFaction(SpecificFaction type) {
    if (factions.count(type)) {
        std::string name = factions[type]->getName();
        factions.erase(type);
        logger->info("Removed faction: " + name);
    }
}

std::shared_ptr<Faction> FactionRelationshipSystem::getFaction(SpecificFaction type) {
    if (factions.count(type)) {
        return factions[type];
    }
    return nullptr;
}

const std::map<SpecificFaction, std::shared_ptr<Faction>>& FactionRelationshipSystem::getAllFactions() const {
    return factions;
}

void FactionRelationshipSystem::establishAllRelationships() {
    // Set up initial relationships between all factions
    for (auto& pair1 : factions) {
        for (auto& pair2 : factions) {
            if (pair1.first != pair2.first) {
                SpecificFaction faction1 = pair1.first;
                SpecificFaction faction2 = pair2.first;
                
                // Default neutral relationships
                factions[faction1]->establishRelationship(faction2, RelationshipLevel::NEUTRAL);
                
                // Set up special relationships based on faction types
                if ((faction1 == SpecificFaction::LUCIFER_LEGION && faction2 == SpecificFaction::IFRIT_WARRIORS) ||
                    (faction1 == SpecificFaction::IFRIT_WARRIORS && faction2 == SpecificFaction::LUCIFER_LEGION)) {
                    factions[faction1]->establishRelationship(faction2, RelationshipLevel::FRIENDLY);
                }
                
                if ((faction1 == SpecificFaction::IBLIS_REDEEMED && faction2 == SpecificFaction::MARID_ROYALTY) ||
                    (faction1 == SpecificFaction::MARID_ROYALTY && faction2 == SpecificFaction::IBLIS_REDEEMED)) {
                    factions[faction1]->establishRelationship(faction2, RelationshipLevel::FRIENDLY);
                }
                
                if (faction1 == SpecificFaction::HORDE || faction2 == SpecificFaction::HORDE) {
                    factions[faction1]->establishRelationship(faction2, RelationshipLevel::HOSTILE);
                }
            }
        }
    }
}

void FactionRelationshipSystem::modifyAllRelationships(SpecificFaction faction, int modifier) {
    if (factions.count(faction)) {
        auto factionObj = factions[faction];
        for (auto& pair : factionObj->getRelationships()) {
            factionObj->modifyRelationship(pair.first, modifier);
        }
    }
}

bool FactionRelationshipSystem::proposeTreaty(SpecificFaction faction1, SpecificFaction faction2, const std::string& treatyType) {
    if (!factions.count(faction1) || !factions.count(faction2)) {
        return false;
    }
    
    auto relationship1 = factions[faction1]->getRelationship(faction2);
    auto relationship2 = factions[faction2]->getRelationship(faction1);
    
    if (relationship1 && relationship2) {
        // Both factions must be at least friendly to form treaties
        if (relationship1->currentLevel >= RelationshipLevel::FRIENDLY && 
            relationship2->currentLevel >= RelationshipLevel::FRIENDLY) {
            
            relationship1->treaties.push_back(treatyType);
            relationship2->treaties.push_back(treatyType);
            
            factions[faction1]->modifyRelationship(faction2, 10);
            factions[faction2]->modifyRelationship(faction1, 10);
            
            logger->info("Treaty established: " + getFactionName(faction1) + " - " + getFactionName(faction2) + " (" + treatyType + ")");
            return true;
        }
    }
    
    return false;
}

bool FactionRelationshipSystem::declareWar(SpecificFaction faction1, SpecificFaction faction2) {
    if (!factions.count(faction1) || !factions.count(faction2)) {
        return false;
    }
    
    factions[faction1]->setDiplomaticStatus(faction2, DiplomaticStatus::WAR);
    factions[faction2]->setDiplomaticStatus(faction1, DiplomaticStatus::WAR);
    
    factions[faction1]->modifyRelationship(faction2, -50);
    factions[faction2]->modifyRelationship(faction1, -50);
    
    logger->info("War declared: " + getFactionName(faction1) + " vs " + getFactionName(faction2));
    return true;
}

bool FactionRelationshipSystem::formAlliance(SpecificFaction faction1, SpecificFaction faction2) {
    if (!factions.count(faction1) || !factions.count(faction2)) {
        return false;
    }
    
    factions[faction1]->setDiplomaticStatus(faction2, DiplomaticStatus::ALLIANCE);
    factions[faction2]->setDiplomaticStatus(faction1, DiplomaticStatus::ALLIANCE);
    
    factions[faction1]->modifyRelationship(faction2, 30);
    factions[faction2]->modifyRelationship(faction1, 30);
    
    logger->info("Alliance formed: " + getFactionName(faction1) + " + " + getFactionName(faction2));
    return true;
}

void FactionRelationshipSystem::negotiatePeace(SpecificFaction faction1, SpecificFaction faction2) {
    if (!factions.count(faction1) || !factions.count(faction2)) {
        return;
    }
    
    factions[faction1]->setDiplomaticStatus(faction2, DiplomaticStatus::PEACE);
    factions[faction2]->setDiplomaticStatus(faction1, DiplomaticStatus::PEACE);
    
    factions[faction1]->modifyRelationship(faction2, 20);
    factions[faction2]->modifyRelationship(faction1, 20);
    
    logger->info("Peace negotiated: " + getFactionName(faction1) + " + " + getFactionName(faction2));
}

void FactionRelationshipSystem::update(float deltaTime) {
    // Update all faction economies
    for (auto& pair : factions) {
        pair.second->updateEconomy(deltaTime);
    }
    
    // Process all trade routes
    processAllTrade(deltaTime);
    
    // Process relationship decay and changes
    processRelationshipDecay();
    
    // Check for potential conflicts and alliances
    checkForConflicts();
    checkForAllianceFormation();
    
    // Process global events
    processGlobalEvents();
}

void FactionRelationshipSystem::processAllTrade(float deltaTime) {
    for (auto& pair1 : factions) {
        for (auto& pair2 : pair1.second->getRelationships()) {
            if (pair2.second->diplomaticStatus == DiplomaticStatus::PEACE || 
                pair2.second->diplomaticStatus == DiplomaticStatus::ALLIANCE) {
                
                // Process trade between peaceful factions
                for (auto& trade : pair2.second->tradeRoutes) {
                    pair1.second->processTrade(pair2.first, trade.first, trade.second);
                }
            }
        }
    }
}

void FactionRelationshipSystem::processRelationshipDecay() {
    for (auto& pair : factions) {
        for (auto& rel : pair.second->getRelationships()) {
            // Slowly decay relationships over time if not maintained
            if (rel.second->lastInteraction > 100) {
                if (rel.second->currentLevel > RelationshipLevel::NEUTRAL) {
                    rel.second->modifyRelationship(-1);
                } else if (rel.second->currentLevel < RelationshipLevel::NEUTRAL) {
                    rel.second->modifyRelationship(1);
                }
            }
            rel.second->lastInteraction = std::max(0, rel.second->lastInteraction - 1);
        }
    }
}

void FactionRelationshipSystem::checkForConflicts() {
    auto conflicts = getConflictingFactions();
    for (auto& conflict : conflicts) {
        if (factions[conflict.first]->getRelationship(conflict.second)->currentLevel <= RelationshipLevel::HOSTILE) {
            // Chance of war declaration
            if (rand() % 100 < 5) { // 5% chance per update
                declareWar(conflict.first, conflict.second);
            }
        }
    }
}

void FactionRelationshipSystem::checkForAllianceFormation() {
    for (auto& pair1 : factions) {
        for (auto& pair2 : pair1.second->getRelationships()) {
            if (pair2.second->currentLevel >= RelationshipLevel::ALLIED &&
                pair2.second->diplomaticStatus == DiplomaticStatus::PEACE) {
                // Chance of alliance formation
                if (rand() % 100 < 3) { // 3% chance per update
                    formAlliance(pair1.first, pair2.first);
                }
            }
        }
    }
}

void FactionRelationshipSystem::initializeDefaultFactions() {
    // Create all the factions from the game
    createFaction(SpecificFaction::LUCIFER_LEGION, "Lucifer Legion", FactionType::DEVIL_FACTION);
    createFaction(SpecificFaction::MAMMON_MERCHANTS, "Mammon Merchants", FactionType::DEVIL_FACTION);
    createFaction(SpecificFaction::ASMODEUS_COURT, "Asmodeus Court", FactionType::DEVIL_FACTION);
    createFaction(SpecificFaction::BEELZEBUB_SWARM, "Beelzebub Swarm", FactionType::DEVIL_FACTION);
    createFaction(SpecificFaction::LEVIATHAN_DEPTHS, "Leviathan Depths", FactionType::DEVIL_FACTION);
    createFaction(SpecificFaction::SATAN_TEMPLE, "Satan Temple", FactionType::DEVIL_FACTION);
    
    createFaction(SpecificFaction::MARID_ROYALTY, "Marid Royalty", FactionType::DJINN_FACTION);
    createFaction(SpecificFaction::IFRIT_WARRIORS, "Ifrit Warriors", FactionType::DJINN_FACTION);
    createFaction(SpecificFaction::SHAITAN_TRICKSTERS, "Shaitan Tricksters", FactionType::DJINN_FACTION);
    
    createFaction(SpecificFaction::IBLIS_REDEEMED, "Iblis Redeemed", FactionType::SPECIAL_ENTITY);
    createFaction(SpecificFaction::YUDU_BUAH_GUARDIANS, "Yudu'buah Guardians", FactionType::SPECIAL_ENTITY);
    
    createFaction(SpecificFaction::HUMAN_ROGUES, "Human Rogues", FactionType::HUMAN_ROGUE);
    createFaction(SpecificFaction::HORDE, "Horde", FactionType::HORDE);
}

void FactionRelationshipSystem::setupDefaultHierarchies() {
    // This would set up detailed hierarchies for each faction
    // For now, using basic setup in Faction constructor
}

std::string FactionRelationshipSystem::getFactionName(SpecificFaction faction) {
    if (factions.count(faction)) {
        return factions[faction]->getName();
    }
    return "Unknown Faction";
}

std::map<SpecificFaction, int> FactionRelationshipSystem::calculatePowerBalance() {
    std::map<SpecificFaction, int> powerBalance;
    for (const auto& pair : factions) {
        powerBalance[pair.first] = pair.second->getPower();
    }
    return powerBalance;
}

std::vector<std::pair<SpecificFaction, SpecificFaction>> FactionRelationshipSystem::getConflictingFactions() {
    std::vector<std::pair<SpecificFaction, SpecificFaction>> conflicts;
    
    for (const auto& pair1 : factions) {
        for (const auto& rel : pair1.second->getRelationships()) {
            if (rel.second->currentLevel <= RelationshipLevel::HOSTILE) {
                conflicts.push_back({pair1.first, rel.first});
            }
        }
    }
    
    return conflicts;
}

std::vector<std::pair<SpecificFaction, SpecificFaction>> FactionRelationshipSystem::getAlliedFactions() {
    std::vector<std::pair<SpecificFaction, SpecificFaction>> alliances;
    
    for (const auto& pair1 : factions) {
        for (const auto& rel : pair1.second->getRelationships()) {
            if (rel.second->diplomaticStatus == DiplomaticStatus::ALLIANCE) {
                alliances.push_back({pair1.first, rel.first});
            }
        }
    }
    
    return alliances;
}

} // namespace Privanna