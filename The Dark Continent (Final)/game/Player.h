#ifndef PLAYER_H
#define PLAYER_H

#include <string>
#include <vector>
#include <map>
#include <memory>
#include "GameEngine.h"

// Forward declarations
class Card;
class Territory;
class Unit;
class Fortification;

enum class CardType {
    AMERICA,
    COMMUNISM,
    DIVINE_WILL,
    TRIVIA,
    MISCHIEF,
    EU_INFLUENCE,
    ALLIANCE,
    FEDERATION
};

enum class ActionType {
    ATTACK,
    PLAY_CARD,
    MOVE,
    NUKE,
    BUILD_UNIT,
    BUILD_FORTIFICATION,
    DRAW_CARD,
    FORM_TRUCE
};

struct PlayerStats {
    int territoriesControlled;
    int totalInfluence;
    int totalCurrency;
    int cardsInHand;
    int unitsBuilt;
    int unitsLost;
    int fortificationsBuilt;
    int cardsPlayed;
    int shimarra;
    int nuclearArsenal;
    int turnsPlayed;
    
    PlayerStats() : territoriesControlled(0), totalInfluence(0), totalCurrency(0), 
                   cardsInHand(0), unitsBuilt(0), unitsLost(0), fortificationsBuilt(0),
                   cardsPlayed(0), shimarra(0), nuclearArsenal(20), turnsPlayed(0) {}
};

class Player {
protected:
    PlayerID playerId;
    std::string playerName;
    PlayerStats stats;
    
    // Resources
    int influence;
    int currency;
    int shimarra;
    int nuclearProgramLevel;
    
    // Cards
    std::vector<std::shared_ptr<Card>> hand;
    std::vector<std::shared_ptr<Card>> playedCards;
    std::map<CardType, int> cardAccess; // Which card types this player can access
    
    // Turn management
    int actionsPerTurn;
    int actionsRemaining;
    bool isActivePlayer;
    
    // Special abilities and states
    bool hasNuclearCapability;
    bool canBuildSuperweapon;
    bool isInTruce;
    int truceTurnsRemaining;
    
    // Player-specific data
    std::map<std::string, int> specialCounters;
    std::map<std::string, bool> abilityFlags;

public:
    Player(PlayerID id, const std::string& name);
    virtual ~Player() = default;
    
    // Basic player info
    PlayerID getPlayerID() const { return playerId; }
    const std::string& getPlayerName() const { return playerName; }
    const PlayerStats& getStats() const { return stats; }
    
    // Resource management
    int getInfluence() const { return influence; }
    int getCurrency() const { return currency; }
    int getShimarra() const { return shimarra; }
    int getNuclearProgramLevel() const { return nuclearProgramLevel; }
    int getNuclearArsenal() const { return stats.nuclearArsenal; }
    
    void setInfluence(int amount) { influence = std::max(0, amount); }
    void setCurrency(int amount) { currency = std::max(0, amount); }
    void setShimarra(int amount) { shimarra = std::max(0, amount); }
    void setNuclearProgramLevel(int level) { nuclearProgramLevel = std::max(0, std::min(20, level)); }
    
    void addInfluence(int amount) { setInfluence(influence + amount); }
    void addCurrency(int amount) { setCurrency(currency + amount); }
    void addShimarra(int amount) { setShimarra(shimarra + amount); }
    
    bool spendInfluence(int amount);
    bool spendCurrency(int amount);
    bool spendShimarra(int amount);
    
    // Card management
    const std::vector<std::shared_ptr<Card>>& getHand() const { return hand; }
    const std::vector<std::shared_ptr<Card>>& getPlayedCards() const { return playedCards; }
    
    void addCardToHand(std::shared_ptr<Card> card);
    void removeCardFromHand(std::shared_ptr<Card> card);
    void addCardToPlayed(std::shared_ptr<Card> card);
    
    bool hasCardAccess(CardType type) const;
    void setCardAccess(CardType type, bool hasAccess);
    
    int getHandSize() const { return static_cast<int>(hand.size()); }
    int getPlayedCardsCount() const { return static_cast<int>(playedCards.size()); }
    
    // Turn management
    void startTurn();
    void endTurn();
    bool isActive() const { return isActivePlayer; }
    void setActive(bool active) { isActivePlayer = active; }
    
    int getActionsRemaining() const { return actionsRemaining; }
    bool hasActionsRemaining() const { return actionsRemaining > 0; }
    void useAction();
    void resetActions();
    
    // Special abilities
    bool hasNuclearCapability() const { return hasNuclearCapability; }
    void setNuclearCapability(bool capable);
    
    bool canBuildSuperweapon() const { return canBuildSuperweapon; }
    void setSuperweaponCapability(bool capable);
    
    // Truce management
    bool isInTruceState() const { return isInTruce; }
    int getTruceTurnsRemaining() const { return truceTurnsRemaining; }
    void enterTruce(int duration);
    void updateTruceStatus();
    
    // Virtual methods for player-specific behavior
    virtual void initializeStartingResources() = 0;
    virtual void initializeStartingCards() = 0;
    virtual void initializeStartingTerritories() = 0;
    virtual bool canPerformAction(ActionType action) const = 0;
    virtual void onTurnStart() = 0;
    virtual void onTurnEnd() = 0;
    virtual void onTerritoryGained(int territoryId) = 0;
    virtual void onTerritoryLost(int territoryId) = 0;
    virtual void onCardPlayed(std::shared_ptr<Card> card) = 0;
    virtual void onUnitBuilt(std::shared_ptr<Unit> unit) = 0;
    virtual void onUnitLost(std::shared_ptr<Unit> unit) = 0;
    
    // Special counters and abilities
    void setSpecialCounter(const std::string& key, int value) { specialCounters[key] = value; }
    int getSpecialCounter(const std::string& key) const;
    void modifySpecialCounter(const std::string& key, int delta);
    
    void setAbilityFlag(const std::string& key, bool value) { abilityFlags[key] = value; }
    bool getAbilityFlag(const std::string& key) const;
    
    // Victory condition checks
    virtual bool hasAchievedVictory() const = 0;
    virtual int calculateVictoryPoints() const = 0;
    
    // Player-specific victory conditions
    virtual bool checkInfluenceVictory() const;
    virtual bool checkShimarraVictory() const;
    virtual bool checkTerritoryVictory() const;
    
    // Nuclear capabilities
    bool canLaunchNuke() const;
    bool launchNuke(int targetCityId);
    bool repairNuclearProgram();
    bool sabotageNuclearProgram(PlayerID targetPlayer);
    
    // Statistics tracking
    void updateStats();
    void resetStats();
    
    // Serialization
    virtual std::string serialize() const;
    virtual bool deserialize(const std::string& data);
    
    // AI and decision making (for computer-controlled players)
    virtual bool isHumanControlled() const { return true; }
    virtual void makeAIDecision() {}
    
    // Utility methods
    virtual std::string getPlayerDescription() const;
    virtual void logPlayerAction(const std::string& action) const;

protected:
    // Helper methods for derived classes
    void setActionsPerTurn(int actions) { actionsPerTurn = actions; }
    void initializeCardAccess();
    
    // Resource calculation helpers
    virtual int calculateBaseInfluence() const = 0;
    virtual int calculateBaseCurrency() const = 0;
    
    // Card access setup for different player types
    virtual void setupCardAccess() = 0;
};

// Specialized player classes

class UnitedStatesPlayer : public Player {
private:
    int technologySlots;
    std::map<std::string, bool> technologies;
    
public:
    UnitedStatesPlayer();
    
    // Override base class methods
    void initializeStartingResources() override;
    void initializeStartingCards() override;
    void initializeStartingTerritories() override;
    bool canPerformAction(ActionType action) const override;
    void onTurnStart() override;
    void onTurnEnd() override;
    void onTerritoryGained(int territoryId) override;
    void onTerritoryLost(int territoryId) override;
    void onCardPlayed(std::shared_ptr<Card> card) override;
    void onUnitBuilt(std::shared_ptr<Unit> unit) override;
    void onUnitLost(std::shared_ptr<Unit> unit) override;
    
    // US-specific methods
    bool hasTechnology(const std::string& techName) const;
    void acquireTechnology(const std::string& techName);
    int getTechnologyLevel(const std::string& techName) const;
    
    bool hasAchievedVictory() const override;
    int calculateVictoryPoints() const override;
    
    std::string getPlayerDescription() const override;
    
protected:
    void setupCardAccess() override;
    int calculateBaseInfluence() const override;
    int calculateBaseCurrency() const override;
};

class RussiaPlayer : public Player {
private:
    int superweaponUpgrades;
    std::vector<std::string> superweaponComponents;
    bool hasNauka;
    
public:
    RussiaPlayer();
    
    // Override base class methods
    void initializeStartingResources() override;
    void initializeStartingCards() override;
    void initializeStartingTerritories() override;
    bool canPerformAction(ActionType action) const override;
    void onTurnStart() override;
    void onTurnEnd() override;
    void onTerritoryGained(int territoryId) override;
    void onTerritoryLost(int territoryId) override;
    void onCardPlayed(std::shared_ptr<Card> card) override;
    void onUnitBuilt(std::shared_ptr<Unit> unit) override;
    void onUnitLost(std::shared_ptr<Unit> unit) override;
    
    // Russia-specific methods
    bool hasSuperweaponComponent(const std::string& component) const;
    void addSuperweaponComponent(const std::string& component);
    bool canBuildSuperweapon() const override;
    bool buildSuperweapon();
    
    bool hasAchievedVictory() const override;
    int calculateVictoryPoints() const override;
    
    std::string getPlayerDescription() const override;
    
protected:
    void setupCardAccess() override;
    int calculateBaseInfluence() const override;
    int calculateBaseCurrency() const override;
};

class EuropeanUnionPlayer : public Player {
private:
    int politicalInfluence;
    std::map<std::string, int> diplomaticRelations;
    std::vector<std::string> formedAlliances;
    
public:
    EuropeanUnionPlayer();
    
    // Override base class methods
    void initializeStartingResources() override;
    void initializeStartingCards() override;
    void initializeStartingTerritories() override;
    bool canPerformAction(ActionType action) const override;
    void onTurnStart() override;
    void onTurnEnd() override;
    void onTerritoryGained(int territoryId) override;
    void onTerritoryLost(int territoryId) override;
    void onCardPlayed(std::shared_ptr<Card> card) override;
    void onUnitBuilt(std::shared_ptr<Unit> unit) override;
    void onUnitLost(std::shared_ptr<Unit> unit) override;
    
    // EU-specific methods
    int getPoliticalInfluence() const { return politicalInfluence; }
    void addPoliticalInfluence(int amount) { politicalInfluence += amount; }
    
    int getDiplomaticRelation(PlayerID player) const;
    void setDiplomaticRelation(PlayerID player, int level);
    
    bool hasAlliance(const std::string& allianceName) const;
    void formAlliance(const std::string& allianceName);
    
    bool canInfluenceTerritory(int territoryId) const;
    bool applyPoliticalInfluence(int territoryId, int amount);
    
    bool hasAchievedVictory() const override;
    int calculateVictoryPoints() const override;
    
    std::string getPlayerDescription() const override;
    
protected:
    void setupCardAccess() override;
    int calculateBaseInfluence() const override;
    int calculateBaseCurrency() const override;
};

class SouthernAlliancePlayer : public Player {
private:
    std::map<int, int> resourceExtraction; // Territory ID -> extraction level
    std::vector<int> developedTerritories;
    int climateAdaptationLevel;
    
public:
    SouthernAlliancePlayer();
    
    // Override base class methods
    void initializeStartingResources() override;
    void initializeStartingCards() override;
    void initializeStartingTerritories() override;
    bool canPerformAction(ActionType action) const override;
    void onTurnStart() override;
    void onTurnEnd() override;
    void onTerritoryGained(int territoryId) override;
    void onTerritoryLost(int territoryId) override;
    void onCardPlayed(std::shared_ptr<Card> card) override;
    void onUnitBuilt(std::shared_ptr<Unit> unit) override;
    void onUnitLost(std::shared_ptr<Unit> unit) override;
    
    // Alliance-specific methods
    int getResourceExtraction(int territoryId) const;
    void setResourceExtraction(int territoryId, int level);
    
    bool isTerritoryDeveloped(int territoryId) const;
    void developTerritory(int territoryId);
    
    int getClimateAdaptationLevel() const { return climateAdaptationLevel; }
    void upgradeClimateAdaptation();
    
    bool hasClimateAdvantage(int territoryId) const;
    int calculateResourceBonus(int territoryId) const;
    
    bool hasAchievedVictory() const override;
    int calculateVictoryPoints() const override;
    
    std::string getPlayerDescription() const override;
    
protected:
    void setupCardAccess() override;
    int calculateBaseInfluence() const override;
    int calculateBaseCurrency() const override;
};

class DarkContinentPlayer : public Player {
private:
    std::vector<int> fragmentLocations;
    int maxShimarra;
    bool isSpawned;
    int spawnYear;
    bool hasFragmented;
    
public:
    DarkContinentPlayer();
    
    // Override base class methods
    void initializeStartingResources() override;
    void initializeStartingCards() override;
    void initializeStartingTerritories() override;
    bool canPerformAction(ActionType action) const override;
    void onTurnStart() override;
    void onTurnEnd() override;
    void onTerritoryGained(int territoryId) override;
    void onTerritoryLost(int territoryId) override;
    void onCardPlayed(std::shared_ptr<Card> card) override;
    void onUnitBuilt(std::shared_ptr<Unit> unit) override;
    void onUnitLost(std::shared_ptr<Unit> unit) override;
    
    // Dark Continent-specific methods
    void setSpawned(bool spawned, int year);
    bool getIsSpawned() const { return isSpawned; }
    int getSpawnYear() const { return spawnYear; }
    
    void setFragmented(bool fragmented);
    bool getIsFragmented() const { return hasFragmented; }
    
    void addFragmentLocation(int cityId);
    const std::vector<int>& getFragmentLocations() const { return fragmentLocations; }
    
    int getMaxShimarra() const { return maxShimarra; }
    void setMaxShimarra(int max) { maxShimarra = max; }
    
    bool canSpawnFromFragment(int fragmentId) const;
    bool spawnUnitFromFragment(int fragmentId, const std::string& unitType);
    
    bool hasAchievedVictory() const override;
    int calculateVictoryPoints() const override;
    
    std::string getPlayerDescription() const override;
    
protected:
    void setupCardAccess() override;
    int calculateBaseInfluence() const override;
    int calculateBaseCurrency() const override;
};

// Utility functions
std::unique_ptr<Player> createPlayer(PlayerID playerId, const std::string& playerName);
std::string playerIDToString(PlayerID playerId);
PlayerID stringToPlayerID(const std::string& playerStr);

#endif // PLAYER_H