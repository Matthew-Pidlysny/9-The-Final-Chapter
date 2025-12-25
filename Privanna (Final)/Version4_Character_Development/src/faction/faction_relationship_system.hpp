#ifndef PRIVANNA_FACTION_RELATIONSHIP_SYSTEM_HPP
#define PRIVANNA_FACTION_RELATIONSHIP_SYSTEM_HPP

#include <string>
#include <vector>
<map>
#include <memory>
#include <cstdint>
#include "../systems/event_system.hpp"
#include "../utils/logger.hpp"

namespace Privanna {

// Faction types based on Privanna game
enum class FactionType {
    DEVIL_FACTION,
    DJINN_FACTION,
    SPECIAL_ENTITY,
    HUMAN_ROGUE,
    HORDE
};

// Specific factions from the game
enum class SpecificFaction {
    // Devil factions (6)
    LUCIFER_LEGION,
    MAMMON_MERCHANTS,
    ASMODEUS_COURT,
    BEELZEBUB_SWARM,
    LEVIATHAN_DEPTHS,
    SATAN_TEMPLE,
    
    // Djinn factions (3)
    MARID_ROYALTY,
    IFRIT_WARRIORS,
    SHAITAN_TRICKSTERS,
    
    // Special entities
    IBLIS_REDEEMED,
    YUDU_BUAH_GUARDIANS,
    
    // Others
    HUMAN_ROGUES,
    HORDE
};

// Relationship levels
enum class RelationshipLevel {
    HATED = -100,
    HOSTILE = -50,
    UNFRIENDLY = -25,
    NEUTRAL = 0,
    FRIENDLY = 25,
    ALLIED = 50,
    BOUND = 100
};

// Diplomatic status types
enum class DiplomaticStatus {
    WAR,
    HOSTILE,
    TENSION,
    NEUTRAL,
    PEACE,
    ALLIANCE,
    VASSAL,
    OVERLORD
};

// Faction relationship
struct FactionRelationship {
    SpecificFaction targetFaction;
    RelationshipLevel currentLevel = RelationshipLevel::NEUTRAL;
    DiplomaticStatus diplomaticStatus = DiplomaticStatus::NEUTRAL;
    int relationshipPoints = 0;
    std::vector<std::string> treaties;
    std::vector<std::string> conflicts;
    std::map<std::string, int> tradeRoutes;
    int lastInteraction = 0;
    bool isLocked = false; // Prevents automatic changes
    
    void modifyRelationship(int points) {
        if (!isLocked) {
            relationshipPoints += points;
            updateRelationshipLevel();
        }
    }
    
    void updateRelationshipLevel() {
        if (relationshipPoints <= -100) {
            currentLevel = RelationshipLevel::HATED;
            diplomaticStatus = DiplomaticStatus::WAR;
        } else if (relationshipPoints <= -50) {
            currentLevel = RelationshipLevel::HOSTILE;
            diplomaticStatus = DiplomaticStatus::HOSTILE;
        } else if (relationshipPoints <= -25) {
            currentLevel = RelationshipLevel::UNFRIENDLY;
            diplomaticStatus = DiplomaticStatus::TENSION;
        } else if (relationshipPoints <= 25) {
            currentLevel = RelationshipLevel::NEUTRAL;
            diplomaticStatus = DiplomaticStatus::NEUTRAL;
        } else if (relationshipPoints <= 50) {
            currentLevel = RelationshipLevel::FRIENDLY;
            diplomaticStatus = DiplomaticStatus::PEACE;
        } else if (relationshipPoints <= 100) {
            currentLevel = RelationshipLevel::ALLIED;
            diplomaticStatus = DiplomaticStatus::ALLIANCE;
        } else {
            currentLevel = RelationshipLevel::BOUND;
            diplomaticStatus = DiplomaticStatus::ALLIANCE;
        }
    }
    
    float getTradeBonus() const {
        switch (currentLevel) {
            case RelationshipLevel::HATED: return 0.5f;
            case RelationshipLevel::HOSTILE: return 0.7f;
            case RelationshipLevel::UNFRIENDLY: return 0.85f;
            case RelationshipLevel::NEUTRAL: return 1.0f;
            case RelationshipLevel::FRIENDLY: return 1.15f;
            case RelationshipLevel::ALLIED: return 1.3f;
            case RelationshipLevel::BOUND: return 1.5f;
            default: return 1.0f;
        }
    }
};

// Individual character within faction
struct FactionMember {
    std::string name;
    int rank = 1;
    int influence = 0;
    std::string title;
    std::vector<std::string> responsibilities;
    std::map<std::string, int> relationships; // Relationship with other members
    bool isLeader = false;
    bool canDiplomacy = false;
    bool canTrade = false;
    bool canCommand = false;
    
    void promote(int newRank) {
        rank = newRank;
        influence += rank * 10;
    }
    
    void addResponsibility(const std::string& responsibility) {
        responsibilities.push_back(responsibility);
    }
};

// Faction hierarchy and structure
struct FactionHierarchy {
    std::string leaderTitle;
    std::vector<std::string> rankTitles;
    std::map<int, std::vector<std::string>> rankResponsibilities;
    int maxRank = 10;
    
    std::string getRankTitle(int rank) const {
        if (rank > 0 && rank <= rankTitles.size()) {
            return rankTitles[rank - 1];
        }
        return "Member";
    }
    
    std::vector<std::string> getResponsibilities(int rank) const {
        if (rankResponsibilities.count(rank)) {
            return rankResponsibilities.at(rank);
        }
        return {};
    }
};

// Economic data for faction
struct FactionEconomy {
    std::map<std::string, int> resources;
    std::map<std::string, int> production;
    std::map<std::string, int> consumption;
    std::map<std::string, int> tradeSurplus;
    int totalWealth = 0;
    int incomeRate = 0;
    int expenseRate = 0;
    
    void addResource(const std::string& resource, int amount) {
        resources[resource] += amount;
        calculateTotalWealth();
    }
    
    void removeResource(const std::string& resource, int amount) {
        if (resources[resource] >= amount) {
            resources[resource] -= amount;
        } else {
            resources[resource] = 0;
        }
        calculateTotalWealth();
    }
    
    void calculateTotalWealth() {
        totalWealth = 0;
        for (const auto& pair : resources) {
            totalWealth += pair.second;
        }
    }
};

// Main faction class
class Faction {
private:
    SpecificFaction factionType;
    FactionType type;
    std::string name;
    std::string description;
    std::string ideology;
    
    FactionHierarchy hierarchy;
    FactionEconomy economy;
    
    std::map<SpecificFaction, std::shared_ptr<FactionRelationship>> relationships;
    std::vector<std::shared_ptr<FactionMember>> members;
    std::map<std::string, int> territories;
    
    std::vector<std::string> culturalTraits;
    std::vector<std::string> traditions;
    std::map<std::string, int> socialNorms;
    
    int power = 100;
    int prestige = 50;
    int stability = 75;
    
public:
    Faction(SpecificFaction type, const std::string& name, FactionType factionType);
    
    // Relationship management
    void establishRelationship(SpecificFaction target, RelationshipLevel level);
    void modifyRelationship(SpecificFaction target, int points);
    std::shared_ptr<FactionRelationship> getRelationship(SpecificFaction target);
    void setDiplomaticStatus(SpecificFaction target, DiplomaticStatus status);
    
    // Member management
    void addMember(std::shared_ptr<FactionMember> member);
    void removeMember(const std::string& name);
    void promoteMember(const std::string& name, int newRank);
    std::shared_ptr<FactionMember> getMember(const std::string& name);
    std::shared_ptr<FactionMember> getLeader();
    
    // Territory management
    void addTerritory(const std::string& territory, int value);
    void removeTerritory(const std::string& territory);
    int getTotalTerritoryValue() const;
    
    // Economic management
    void updateEconomy(float deltaTime);
    void processTrade(SpecificFaction partner, const std::string& resource, int amount);
    bool canAfford(const std::string& resource, int amount) const;
    
    // Cultural and social systems
    void addCulturalTrait(const std::string& trait);
    void addTradition(const std::string& tradition);
    void modifySocialNorm(const std::string& norm, int value);
    
    // Power and prestige
    void calculatePower();
    void calculatePrestige();
    void modifyStability(int amount);
    
    // Events and decisions
    void handleDiplomaticEvent(const std::string& eventType, SpecificFaction otherFaction);
    void makeDecision(const std::string& decisionType);
    
    // Getters
    SpecificFaction getFactionType() const { return factionType; }
    const std::string& getName() const { return name; }
    const std::string& getDescription() const { return description; }
    FactionType getType() const { return type; }
    int getPower() const { return power; }
    int getPrestige() const { return prestige; }
    int getStability() const { return stability; }
    
    const FactionEconomy& getEconomy() const { return economy; }
    const std::map<SpecificFaction, std::shared_ptr<FactionRelationship>>& getRelationships() const { return relationships; }
    const std::vector<std::shared_ptr<FactionMember>>& getMembers() const { return members; }
};

// Faction relationship system manager
class FactionRelationshipSystem {
private:
    std::map<SpecificFaction, std::shared_ptr<Faction>> factions;
    std::map<std::string, std::shared_ptr<FactionMember>> allMembers;
    
    std::shared_ptr<EventSystem> eventSystem;
    std::shared_ptr<Logger> logger;
    
    std::vector<std::string> globalEvents;
    std::map<std::string, int> globalTensions;
    
public:
    FactionRelationshipSystem(std::shared_ptr<EventSystem> eventSystem, std::shared_ptr<Logger> logger);
    
    // Faction management
    std::shared_ptr<Faction> createFaction(SpecificFaction type, const std::string& name, FactionType factionType);
    void removeFaction(SpecificFaction type);
    std::shared_ptr<Faction> getFaction(SpecificFaction type);
    const std::map<SpecificFaction, std::shared_ptr<Faction>>& getAllFactions() const;
    
    // Relationship management
    void establishAllRelationships();
    void modifyAllRelationships(SpecificFaction faction, int modifier);
    void checkForConflicts();
    void resolveConflict(SpecificFaction faction1, SpecificFaction faction2);
    
    // Diplomatic actions
    bool proposeTreaty(SpecificFaction faction1, SpecificFaction faction2, const std::string& treatyType);
    bool declareWar(SpecificFaction faction1, SpecificFaction faction2);
    bool formAlliance(SpecificFaction faction1, SpecificFaction faction2);
    void negotiatePeace(SpecificFaction faction1, SpecificFaction faction2);
    
    // Trade system
    bool establishTradeRoute(SpecificFaction faction1, SpecificFaction faction2, const std::string& resource);
    void processAllTrade(float deltaTime);
    void breakTradeRoute(SpecificFaction faction1, SpecificFaction faction2, const std::string& resource);
    
    // Member interactions
    void transferMember(const std::string& memberName, SpecificFaction newFaction);
    void promoteDiplomat(const std::string& memberName);
    void assignResponsibility(const std::string& memberName, const std::string& responsibility);
    
    // Cultural exchange
    void facilitateCulturalExchange(SpecificFaction faction1, SpecificFaction faction2);
    void spreadInfluence(SpecificFaction faction, int amount);
    
    // Global events
    void addGlobalEvent(const std::string& event);
    void processGlobalEvents();
    void modifyGlobalTension(const std::string& region, int amount);
    
    // System updates
    void update(float deltaTime);
    void saveFactionData(const std::string& filename);
    void loadFactionData(const std::string& filename);
    
    // Analytics
    std::map<SpecificFaction, int> calculatePowerBalance();
    std::vector<std::pair<SpecificFaction, SpecificFaction>> getConflictingFactions();
    std::vector<std::pair<SpecificFaction, SpecificFaction>> getAlliedFactions();
    
private:
    void initializeDefaultFactions();
    void setupDefaultHierarchies();
    void processRelationshipDecay();
    void checkForAllianceFormation();
    void checkForWarDeclaration();
    std::string getFactionName(SpecificFaction faction);
};

} // namespace Privanna

#endif // PRIVANNA_FACTION_RELATIONSHIP_SYSTEM_HPP