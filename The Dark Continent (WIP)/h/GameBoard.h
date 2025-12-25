#ifndef GAMEBOARD_H
#define GAMEBOARD_H

#include <vector>
#include <map>
#include <memory>
#include <string>
#include <unordered_set>
#include "GameEngine.h"

struct Coordinates {
    double x, y;
    Coordinates(double x = 0.0, double y = 0.0) : x(x), y(y) {}
    
    double distanceTo(const Coordinates& other) const {
        double dx = x - other.x;
        double dy = y - other.y;
        return std::sqrt(dx * dx + dy * dy);
    }
};

enum class TerritoryType {
    LAND,
    NAVAL,
    COASTAL
};

enum class ClimateType {
    TEMPERATE,
    TROPICAL,
    ARCTIC,
    ANTARCTIC,
    DESERT,
    MEDITERRANEAN
};

struct City {
    int id;
    std::string name;
    Coordinates position;
    int basePopulation;
    int currentPopulation;
    int maxPopulation;
    int baseCurrencyProduction;
    int baseInfluenceProduction;
    bool isDevastated;
    bool isOverpopulated;
    
    City(int id, const std::string& name, const Coordinates& pos) 
        : id(id), name(name), position(pos), basePopulation(1000), 
          currentPopulation(1000), maxPopulation(10000), baseCurrencyProduction(10),
          baseInfluenceProduction(5), isDevastated(false), isOverpopulated(false) {}
};

struct Territory {
    int id;
    std::string name;
    Coordinates centerPosition;
    std::vector<Coordinates> boundaries;
    TerritoryType type;
    ClimateType climate;
    PlayerID controller;
    int baseInfluence;
    int baseCurrency;
    std::vector<City> cities;
    std::unordered_set<int> adjacentTerritories;
    std::map<PlayerID, bool> absenceTokens;
    bool isContested;
    
    // Constructor
    Territory(int id, const std::string& name, const Coordinates& pos)
        : id(id), name(name), centerPosition(pos), type(TerritoryType::LAND),
          climate(ClimateType::TEMPERATE), controller(PlayerID::UNITED_STATES),
          baseInfluence(10), baseCurrency(15), isContested(false) {}
    
    // Methods
    bool hasAdjacentTerritory(int territoryId) const {
        return adjacentTerritories.find(territoryId) != adjacentTerritories.end();
    }
    
    void addAdjacentTerritory(int territoryId) {
        adjacentTerritories.insert(territoryId);
    }
    
    int getTotalInfluence() const {
        int total = baseInfluence;
        for (const auto& city : cities) {
            if (!city.isDevastated) {
                total += city.baseInfluenceProduction;
            }
        }
        return total;
    }
    
    int getTotalCurrency() const {
        int total = baseCurrency;
        for (const auto& city : cities) {
            if (!city.isDevastated) {
                total += city.baseCurrencyProduction;
            }
            if (city.isOverpopulated) {
                total -= 10; // Overpopulation penalty
            }
        }
        return total;
    }
};

struct DarkContinentFragment {
    int id;
    int cityId; // The city this fragment is over
    Coordinates position;
    bool isActive;
    int spawnYear;
    
    DarkContinentFragment(int id, int cityId, const Coordinates& pos, int year)
        : id(id), cityId(cityId), position(pos), isActive(true), spawnYear(year) {}
};

class GameBoard {
private:
    std::vector<Territory> territories;
    std::map<int, Territory*> territoryMap; // For quick lookup by ID
    std::vector<DarkContinentFragment> fragments;
    std::map<PlayerID, std::vector<int>> controlledTerritories;
    
    // Map properties
    double mapWidth;
    double mapHeight;
    double zoomLevel;
    Coordinates viewCenter;
    
    // Visual representation
    std::vector<std::vector<Coordinates>> continentOutlines;
    std::map<int, std::vector<Coordinates>> territoryBoundaries;
    
    // Population counter tracking
    std::map<int, int> cityPopulationLevels; // City ID -> population level (0-5)
    
    void initializeTerritories();
    void setupAdjacency();
    void initializeCities();
    void createMapOutlines();
    
public:
    GameBoard();
    ~GameBoard();
    
    // Initialization
    bool initialize();
    void assignStartingTerritories();
    
    // Territory management
    Territory* getTerritory(int id);
    Territory* getTerritoryByName(const std::string& name);
    const std::vector<Territory>& getTerritories() const { return territories; }
    int getTerritoryCount(PlayerID player) const;
    int getTotalTerritoryCount() const { return territories.size(); }
    
    // Territory control
    void setTerritoryController(int territoryId, PlayerID newController);
    bool changeTerritoryControl(int territoryId, PlayerID fromPlayer, PlayerID toPlayer);
    void placeAbsenceToken(int territoryId, PlayerID player);
    void removeAbsenceToken(int territoryId, PlayerID player);
    bool hasAbsenceToken(int territoryId, PlayerID player) const;
    
    // City management
    City* getCity(int cityId);
    City* getCityInTerritory(int territoryId, int cityIndex);
    void devastateCity(int cityId);
    void repairCity(int cityId);
    bool isCityDevastated(int cityId) const;
    
    // Population counter integration
    void updateCityPopulation(int cityId, int newLevel);
    int getCityPopulationLevel(int cityId) const;
    std::vector<int> getCitiesInTerritory(int territoryId) const;
    
    // Dark Continent mechanics
    void placeDarkContinentFragments();
    void fragmentDarkContinent();
    bool hasDarkContinentFragments() const { return !fragments.empty(); }
    const std::vector<DarkContinentFragment>& getFragments() const { return fragments; }
    DarkContinentFragment* getFragmentAtCity(int cityId);
    std::vector<int> getTerritoriesWithFragments() const;
    
    // Adjacency and movement
    bool areTerritoriesAdjacent(int territory1, int territory2) const;
    std::vector<int> getAdjacentTerritories(int territoryId) const;
    std::vector<int> getConnectedTerritories(int territoryId, PlayerID player) const;
    bool isValidMovement(int fromTerritory, int toTerritory, PlayerID player) const;
    
    // Map rendering and UI
    void setZoom(double zoom);
    double getZoom() const { return zoomLevel; }
    void setViewCenter(const Coordinates& center);
    Coordinates getViewCenter() const { return viewCenter; }
    void panView(double deltaX, double deltaY);
    void zoomView(double factor);
    
    // Coordinate conversion
    Coordinates worldToScreen(const Coordinates& worldPos) const;
    Coordinates screenToWorld(const Coordinates& screenPos) const;
    
    // Territory selection and highlighting
    std::vector<int> getTerritoriesInArea(const Coordinates& topLeft, const Coordinates& bottomRight) const;
    int getTerritoryAtPosition(const Coordinates& position) const;
    bool isPositionInTerritory(const Coordinates& position, int territoryId) const;
    
    // Territory statistics
    int getTerritoryInfluence(int territoryId, PlayerID player) const;
    int getTerritoryCurrency(int territoryId, PlayerID player) const;
    int getTotalPlayerInfluence(PlayerID player) const;
    int getTotalPlayerCurrency(PlayerID player) const;
    
    // Naval regions
    std::vector<int> getNavalRegions() const;
    bool isNavalRegion(int territoryId) const;
    bool canEnterNavalRegion(int territoryId, PlayerID player) const;
    
    // Climate and special mechanics
    ClimateType getTerritoryClimate(int territoryId) const;
    bool hasClimateAdvantage(int territoryId, PlayerID player) const;
    std::vector<int> getTerritoriesByClimate(ClimateType climate) const;
    
    // Resource zones (for Southern Alliance)
    std::vector<int> getResourceZones() const;
    bool isResourceZone(int territoryId) const;
    int getResourceBonus(int territoryId, PlayerID player) const;
    
    // Map data serialization
    std::string serializeTerritoryData() const;
    bool deserializeTerritoryData(const std::string& data);
    std::string serializeFragmentData() const;
    bool deserializeFragmentData(const std::string& data);
    
    // Validation and debugging
    bool validateTerritoryControl() const;
    bool validateAdjacency() const;
    void printTerritoryInfo(int territoryId) const;
    void printPlayerTerritories(PlayerID player) const;
    
    // Utility methods
    void reset();
    void update(double deltaTime);
    std::string getTerritoryDescription(int territoryId) const;
    
    // Map generation (for custom maps)
    void generateRandomMap(int numTerritories);
    void loadMapFromFile(const std::string& filename);
    void saveMapToFile(const std::string& filename) const;
    
    // Visual helpers for piece stacking
    std::vector<Coordinates> getUnitPositionsInTerritory(int territoryId) const;
    Coordinates getFortificationPosition(int territoryId) const;
    std::vector<Coordinates> getStackedPiecePositions(int territoryId, int pieceCount) const;
    
    // Zoom levels and LOD
    enum class ZoomLevel {
        OVERVIEW = 0,    // Show territory names and basic info
        REGIONAL = 1,    // Show city names and piece counts
        DETAILED = 2,    // Show individual pieces and details
        CLOSEUP = 3      // Maximum detail for selected territory
    };
    
    ZoomLevel getCurrentZoomLevel() const;
    void setZoomLevel(ZoomLevel level);
    
    // Piece stacking visualization
    struct PieceStack {
        PlayerID player;
        std::string unitType;
        int count;
        Coordinates position;
        bool isExpanded;
        
        PieceStack(PlayerID p, const std::string& type, int c, const Coordinates& pos)
            : player(p), unitType(type), count(c), position(pos), isExpanded(false) {}
    };
    
    std::vector<PieceStack> getPieceStacksInTerritory(int territoryId) const;
    void expandPieceStack(int territoryId, PlayerID player, const std::string& unitType);
    void collapsePieceStack(int territoryId, PlayerID player, const std::string& unitType);
    
    // Territory search and filtering
    std::vector<int> findTerritoriesByController(PlayerID player) const;
    std::vector<int> findTerritoriesByType(TerritoryType type) const;
    std::vector<int> findContestedTerritories() const;
    std::vector<int> findTerritoriesWithCities() const;
    std::vector<int> findTerritoriesInRange(int centerTerritory, int range) const;
    
    // Pathfinding
    std::vector<int> findPath(int startTerritory, int endTerritory, PlayerID player) const;
    int getDistanceBetweenTerritories(int territory1, int territory2) const;
    bool canReachTerritory(int startTerritory, int endTerritory, PlayerID player) const;
};

#endif // GAMEBOARD_H