#ifndef PRIVANNA_ECONOMIC_SYSTEM_HPP
#define PRIVANNA_ECONOMIC_SYSTEM_HPP

#include <string>
#include <vector>
#include <map>
#include <memory>
#include <cstdint>
#include "../systems/event_system.hpp"
#include "../utils/logger.hpp"
#include "../faction/faction_relationship_system.hpp"

namespace Privanna {

// Resource types
enum class ResourceType {
    GOLD,
    MANA_CRYSTALS,
    IRON,
    WOOD,
    FOOD,
    STONE,
    HERBS,
    RARE_GEMS,
    DRAGON_SCALES,
    DEMON_ESSENCE,
    DJINN_LAMP,
    SACRED_RELICS,
    SOUL_SHARDS,
    BLOOD_STONES,
    SHADOW_ORBS,
    LIGHT_ESSENCE,
    KNOWLEDGE,
    INFLUENCE,
    FAITH_POINTS,
    PRESTIGE
};

// Economic building types
enum class BuildingType {
    MINE,
    FARM,
    LUMBER_MILL,
    QUARRY,
    MARKET,
    BANK,
    TEMPLE,
    ACADEMY,
    FORGE,
    ALCHEMY_LAB,
    TRADE_POST,
    WAREHOUSE,
    WORKSHOP,
    TOWER,
    FORTRESS
};

// Trade route types
enum class TradeRouteType {
    LAND,
    SEA,
    AIR,
    MAGICAL,
    UNDERGROUND,
    DIMENSIONAL
};

// Economic policy types
enum class EconomicPolicy {
    FREE_TRADE,
    PROTECTIONISM,
    MERCANTILISM,
    SOCIALISM,
    AUTARKY,
    EXPORT_ORIENTED,
    IMPORT_SUBSTITUTION,
    MIXED_ECONOMY
};

// Resource
struct Resource {
    ResourceType type;
    std::string name;
    std::string description;
    int baseValue = 1;
    int rarity = 1; // 1-10, higher is rarer
    bool isTradeable = true;
    bool isConsumable = false;
    bool isRenewable = false;
    
    // Market dynamics
    int currentPrice = 1;
    int demand = 50;
    int supply = 50;
    float priceElasticity = 1.0f;
    
    // Production requirements
    std::map<ResourceType, int> requiredResources;
    std::vector<BuildingType> canBeProducedBy;
    
    int getMarketPrice() const {
        float supplyDemandRatio = static_cast<float>(supply) / demand;
        float priceModifier = 2.0f - supplyDemandRatio; // Higher price when supply < demand
        return static_cast<int>(baseValue * priceModifier * priceElasticity);
    }
    
    void updateMarket(int newDemand, int newSupply) {
        demand = newDemand;
        supply = newSupply;
        currentPrice = getMarketPrice();
    }
};

// Economic building
struct EconomicBuilding {
    std::string name;
    BuildingType type;
    int level = 1;
    int maxLevel = 10;
    
    // Production
    std::map<ResourceType, int> productionPerTurn;
    std::map<ResourceType, int> consumptionPerTurn;
    
    // Costs
    std::map<ResourceType, int> buildCost;
    std::map<ResourceType, int> upgradeCost;
    int maintenanceCost = 0;
    
    // Efficiency
    float efficiency = 1.0f;
    float happinessModifier = 0.0f;
    std::map<std::string, float> modifiers;
    
    // Location
    std::string location;
    SpecificFaction owner;
    
    // Status
    bool isOperational = true;
    int turnsToComplete = 0;
    
    void upgrade() {
        if (level < maxLevel) {
            level++;
            
            // Improve production
            for (auto& pair : productionPerTurn) {
                pair.second = static_cast<int>(pair.second * 1.2f);
            }
            
            // Increase maintenance
            maintenanceCost = static_cast<int>(maintenanceCost * 1.3f);
        }
    }
    
    int getActualProduction(ResourceType resource) const {
        if (productionPerTurn.count(resource)) {
            return static_cast<int>(productionPerTurn.at(resource) * efficiency);
        }
        return 0;
    }
    
    int getActualConsumption(ResourceType resource) const {
        if (consumptionPerTurn.count(resource)) {
            return static_cast<int>(consumptionPerTurn.at(resource) * efficiency);
        }
        return 0;
    }
};

// Trade route
struct TradeRoute {
    std::string name;
    TradeRouteType type;
    std::string sourceLocation;
    std::string destinationLocation;
    
    // Route properties
    int capacity = 100;
    int currentUsage = 0;
    float efficiency = 1.0f;
    int distance = 10;
    
    // Trade details
    std::map<ResourceType, int> exportedResources;
    std::map<ResourceType, int> importedResources;
    
    // Security and risks
    int securityLevel = 5; // 1-10
    float riskFactor = 0.1f; // Chance of disruption
    int insuranceCost = 0;
    
    // Costs
    int maintenanceCost = 0;
    std::map<ResourceType, int> tollCost;
    
    // Relationships
    SpecificFaction owner;
    SpecificFaction partner;
    
    bool isActive = true;
    int turnsToEstablish = 0;
    
    float getProfitMargin() const {
        int exportValue = 0;
        int importValue = 0;
        
        for (const auto& pair : exportedResources) {
            exportValue += pair.second * getResourceBaseValue(pair.first);
        }
        
        for (const auto& pair : importedResources) {
            importValue += pair.second * getResourceBaseValue(pair.first);
        }
        
        return (exportValue - importValue - maintenanceCost) / static_cast<float>(exportValue);
    }
    
    bool canAddTrade(ResourceType resource, int amount) const {
        return currentUsage + amount <= capacity;
    }
    
    void addTrade(ResourceType resource, int amount) {
        if (canAddTrade(resource, amount)) {
            currentUsage += amount;
            exportedResources[resource] += amount;
        }
    }
    
private:
    int getResourceBaseValue(ResourceType type) const {
        switch (type) {
            case ResourceType::GOLD: return 10;
            case ResourceType::MANA_CRYSTALS: return 15;
            case ResourceType::IRON: return 5;
            case ResourceType::WOOD: return 2;
            case ResourceType::FOOD: return 1;
            case ResourceType::STONE: return 3;
            case ResourceType::HERBS: return 4;
            case ResourceType::RARE_GEMS: return 20;
            case ResourceType::DRAGON_SCALES: return 50;
            case ResourceType::DEMON_ESSENCE: return 30;
            case ResourceType::DJINN_LAMP: return 100;
            case ResourceType::SACRED_RELICS: return 80;
            case ResourceType::SOUL_SHARDS: return 25;
            case ResourceType::BLOOD_STONES: return 35;
            case ResourceType::SHADOW_ORBS: return 40;
            case ResourceType::LIGHT_ESSENCE: return 45;
            case ResourceType::KNOWLEDGE: return 12;
            case ResourceType::INFLUENCE: return 18;
            case ResourceType::FAITH_POINTS: return 22;
            case ResourceType::PRESTIGE: return 60;
            default: return 1;
        }
    }
};

// Market
struct Market {
    std::string name;
    std::string location;
    
    // Market resources and prices
    std::map<ResourceType, std::shared_ptr<Resource>> availableResources;
    std::map<ResourceType, int> currentPrices;
    
    // Market conditions
    float prosperityLevel = 1.0f;
    float stability = 1.0f;
    std::vector<std::string> activeEvents;
    
    // Trading rules
    std::map<ResourceType, float> taxes;
    std::map<ResourceType, int> tradeLimits;
    bool allowsForeignTrade = true;
    
    // Market relationships
    std::map<std::string, float> marketConnections; // Connected markets and efficiency
    
    void updatePrices() {
        for (auto& pair : availableResources) {
            auto resource = pair.second;
            resource->updateMarket(resource->demand, resource->supply);
            currentPrices[resource->type] = resource->getMarketPrice();
        }
    }
    
    int getPrice(ResourceType type) const {
        if (currentPrices.count(type)) {
            return currentPrices.at(type);
        }
        return 1;
    }
    
    bool canTrade(ResourceType type, int amount) const {
        if (tradeLimits.count(type)) {
            return amount <= tradeLimits.at(type);
        }
        return true;
    }
    
    void addMarketEvent(const std::string& event) {
        activeEvents.push_back(event);
        // Apply event effects
        if (event == "boom") {
            prosperityLevel += 0.2f;
        } else if (event == "recession") {
            prosperityLevel -= 0.2f;
        } else if (event == "shortage") {
            stability -= 0.1f;
        }
    }
};

// Economy
class Economy {
private:
    std::string name;
    SpecificFaction owner;
    
    // Resources
    std::map<ResourceType, int> resources;
    std::map<ResourceType, int> resourceProduction;
    std::map<ResourceType, int> resourceConsumption;
    
    // Buildings
    std::vector<std::shared_ptr<EconomicBuilding>> buildings;
    std::map<BuildingType, int> buildingCounts;
    
    // Trade routes
    std::vector<std::shared_ptr<TradeRoute>> tradeRoutes;
    std::map<std::string, std::shared_ptr<TradeRoute>> tradeRoutesByName;
    
    // Market access
    std::vector<std::shared_ptr<Market>> accessibleMarkets;
    
    // Economic indicators
    int totalWealth = 0;
    int incomePerTurn = 0;
    int expensesPerTurn = 0;
    float gdpGrowthRate = 0.05f; // 5% base growth
    
    // Policies
    EconomicPolicy currentPolicy = EconomicPolicy::FREE_TRADE;
    std::map<std::string, float> policyModifiers;
    
    // Property ownership
    std::map<std::string, int> propertyOwnership; // Location -> ownership percentage
    
public:
    Economy(const std::string& name, SpecificFaction owner);
    
    // Resource management
    void addResource(ResourceType type, int amount);
    bool removeResource(ResourceType type, int amount);
    int getResource(ResourceType type) const;
    int getResourceProduction(ResourceType type) const;
    int getResourceConsumption(ResourceType type) const;
    
    // Building management
    std::shared_ptr<EconomicBuilding> build(BuildingType type, const std::string& location);
    void demolish(const std::string& buildingName);
    std::shared_ptr<EconomicBuilding> getBuilding(const std::string& name);
    void upgradeBuilding(const std::string& name);
    
    // Trade route management
    std::shared_ptr<TradeRoute> createTradeRoute(const std::string& name, TradeRouteType type, 
                                                  const std::string& source, const std::string& destination,
                                                  SpecificFaction partner);
    void closeTradeRoute(const std::string& name);
    std::shared_ptr<TradeRoute> getTradeRoute(const std::string& name);
    
    // Market operations
    bool buyResource(ResourceType type, int amount, std::shared_ptr<Market> market);
    bool sellResource(ResourceType type, int amount, std::shared_ptr<Market> market);
    void addMarketAccess(std::shared_ptr<Market> market);
    
    // Economic policies
    void setPolicy(EconomicPolicy policy);
    void updatePolicyEffects();
    
    // Property ownership
    void acquireProperty(const std::string& location, int percentage);
    void sellProperty(const std::string& location, int percentage);
    int getPropertyOwnership(const std::string& location) const;
    
    // Economic calculations
    void calculateEconomicIndicators();
    void processEconomicTurn();
    float calculateEfficiency() const;
    int calculateTaxRevenue() const;
    
    // Trading with other factions
    bool tradeWithFaction(SpecificFaction faction, const std::map<ResourceType, int>& offered, 
                          const std::map<ResourceType, int>& requested);
    void establishTradeEmbargo(SpecificFaction faction);
    void liftTradeEmbargo(SpecificFaction faction);
    
    // Getters
    const std::string& getName() const { return name; }
    SpecificFaction getOwner() const { return owner; }
    int getTotalWealth() const { return totalWealth; }
    int getIncomePerTurn() const { return incomePerTurn; }
    int getExpensesPerTurn() const { return expensesPerTurn; }
    float getGDPGrowthRate() const { return gdpGrowthRate; }
    EconomicPolicy getCurrentPolicy() const { return currentPolicy; }
    
    const std::map<ResourceType, int>& getResources() const { return resources; }
    const std::vector<std::shared_ptr<EconomicBuilding>>& getBuildings() const { return buildings; }
    const std::vector<std::shared_ptr<TradeRoute>>& getTradeRoutes() const { return tradeRoutes; }
};

// Economic system manager
class EconomicSystem {
private:
    std::map<SpecificFaction, std::shared_ptr<Economy>> economies;
    std::map<std::string, std::shared_ptr<Market>> markets;
    std::map<ResourceType, std::shared_ptr<Resource>> allResources;
    
    std::shared_ptr<EventSystem> eventSystem;
    std::shared_ptr<Logger> logger;
    
    // Global economic factors
    float globalProsperity = 1.0f;
    float globalInflation = 1.0f;
    std::vector<std::string> globalEconomicEvents;
    
    // Trade relationships
    std::map<std::pair<SpecificFaction, SpecificFaction>, std::vector<std::shared_ptr<TradeRoute>>> interFactionTrade;
    
    // Economic statistics
    std::map<SpecificFaction, int> wealthRankings;
    std::map<ResourceType, int> globalResourceProduction;
    std::map<ResourceType, int> globalResourceConsumption;
    
public:
    EconomicSystem(std::shared_ptr<EventSystem> eventSystem, std::shared_ptr<Logger> logger);
    
    // Economy management
    std::shared_ptr<Economy> createEconomy(const std::string& name, SpecificFaction owner);
    void removeEconomy(SpecificFaction owner);
    std::shared_ptr<Economy> getEconomy(SpecificFaction owner);
    
    // Market management
    std::shared_ptr<Market> createMarket(const std::string& name, const std::string& location);
    void removeMarket(const std::string& name);
    std::shared_ptr<Market> getMarket(const std::string& name);
    
    // Resource registration
    void registerResource(std::shared_ptr<Resource> resource);
    
    // Inter-faction trade
    bool facilitateTrade(SpecificFaction faction1, SpecificFaction faction2, 
                        const std::map<ResourceType, int>& trade1, 
                        const std::map<ResourceType, int>& trade2);
    void establishTradeEmbargo(SpecificFaction faction1, SpecificFaction faction2);
    
    // Global economic management
    void updateGlobalEconomy(float deltaTime);
    void processAllEconomicTurns();
    void updateMarketPrices();
    void processTradeRoutes();
    
    // Economic events
    void triggerEconomicEvent(const std::string& eventName);
    void triggerMarketEvent(const std::string& marketName, const std::string& eventName);
    void handleNaturalDisaster(const std::string& location, DisasterType type);
    
    // Currency and inflation
    void updateGlobalInflation();
    float getExchangeRate(SpecificFaction faction1, SpecificFaction faction2) const;
    
    // Property and ownership
    void transferProperty(const std::string& property, SpecificFaction from, SpecificFaction to, int percentage);
    void processRentPayments();
    
    // Analytics and reporting
    std::map<SpecificFaction, int> getWealthRankings();
    std::vector<std::pair<ResourceType, int>> getMostValuableResources();
    std::vector<std::string> getActiveTradeRoutes();
    std::map<SpecificFaction, float> getEconomicGrowthRates();
    
    // System updates
    void update(float deltaTime);
    void saveEconomicData(const std::string& filename);
    void loadEconomicData(const std::string& filename);
    
private:
    void initializeDefaultResources();
    void initializeDefaultMarkets();
    void processSupplyAndDemand();
    void updateTradeEfficiency();
    void calculateGlobalStatistics();
    DisasterType getRandomDisasterType();
    void applyEconomicPolicyEffects();
};

} // namespace Privanna

#endif // PRIVANNA_ECONOMIC_SYSTEM_HPP