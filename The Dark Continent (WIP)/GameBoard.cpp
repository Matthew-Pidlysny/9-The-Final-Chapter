#include "GameBoard.h"
#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <random>

// Static territory data for the world map
const struct TerritoryData {
    int id;
    std::string name;
    double x, y;
    TerritoryType type;
    ClimateType climate;
    int baseInfluence;
    int baseCurrency;
} WORLD_TERRITORIES[] = {
    // North America
    {1, "United States", 200, 150, TerritoryType::LAND, ClimateType::TEMPERATE, 25, 30},
    {2, "Canada", 200, 80, TerritoryType::LAND, ClimateType::ARCTIC, 15, 20},
    {3, "Mexico", 180, 220, TerritoryType::LAND, ClimateType::TROPICAL, 12, 18},
    {4, "Alaska", 120, 60, TerritoryType::LAND, ClimateType::ARCTIC, 8, 15},
    {5, "Greenland", 280, 50, TerritoryType::LAND, ClimateType::ARCTIC, 5, 10},
    
    // South America
    {6, "Brazil", 280, 320, TerritoryType::LAND, ClimateType::TROPICAL, 20, 25},
    {7, "Argentina", 260, 400, TerritoryType::LAND, ClimateType::TEMPERATE, 15, 20},
    {8, "Chile", 240, 410, TerritoryType::LAND, ClimateType::TEMPERATE, 10, 15},
    {9, "Peru", 240, 350, TerritoryType::LAND, ClimateType::TROPICAL, 12, 18},
    {10, "Colombia", 230, 290, TerritoryType::LAND, ClimateType::TROPICAL, 10, 15},
    
    // Europe
    {11, "United Kingdom", 380, 130, TerritoryType::LAND, ClimateType::TEMPERATE, 18, 22},
    {12, "France", 390, 150, TerritoryType::LAND, ClimateType::TEMPERATE, 20, 25},
    {13, "Germany", 400, 140, TerritoryType::LAND, ClimateType::TEMPERATE, 22, 28},
    {14, "Italy", 410, 170, TerritoryType::LAND, ClimateType::MEDITERRANEAN, 18, 23},
    {15, "Spain", 380, 160, TerritoryType::LAND, ClimateType::MEDITERRANEAN, 16, 20},
    {16, "Poland", 420, 130, TerritoryType::LAND, ClimateType::TEMPERATE, 15, 20},
    {17, "Scandinavia", 410, 90, TerritoryType::LAND, ClimateType::ARCTIC, 12, 18},
    {18, "Eastern Europe", 440, 140, TerritoryType::LAND, ClimateType::TEMPERATE, 14, 19},
    
    // Africa
    {19, "Egypt", 420, 220, TerritoryType::LAND, ClimateType::DESERT, 15, 20},
    {20, "Libya", 400, 210, TerritoryType::LAND, ClimateType::DESERT, 10, 15},
    {21, "Nigeria", 380, 260, TerritoryType::LAND, ClimateType::TROPICAL, 18, 22},
    {22, "South Africa", 410, 380, TerritoryType::LAND, ClimateType::TEMPERATE, 20, 25},
    {23, "Kenya", 430, 300, TerritoryType::LAND, ClimateType::TROPICAL, 12, 17},
    {24, "Morocco", 370, 190, TerritoryType::LAND, ClimateType::MEDITERRANEAN, 10, 14},
    
    // Middle East
    {25, "Saudi Arabia", 450, 250, TerritoryType::LAND, ClimateType::DESERT, 20, 30},
    {26, "Iran", 480, 230, TerritoryType::LAND, ClimateType::DESERT, 18, 25},
    {27, "Turkey", 460, 180, TerritoryType::LAND, ClimateType::TEMPERATE, 16, 22},
    {28, "Israel", 450, 210, TerritoryType::LAND, ClimateType::MEDITERRANEAN, 12, 18},
    {29, "Iraq", 470, 220, TerritoryType::LAND, ClimateType::DESERT, 14, 20},
    
    // Asia
    {30, "Russia", 550, 120, TerritoryType::LAND, ClimateType::ARCTIC, 30, 35},
    {31, "China", 580, 200, TerritoryType::LAND, ClimateType::TEMPERATE, 35, 40},
    {32, "India", 540, 250, TerritoryType::LAND, ClimateType::TROPICAL, 30, 35},
    {33, "Japan", 650, 180, TerritoryType::LAND, ClimateType::TEMPERATE, 25, 30},
    {34, "Southeast Asia", 600, 280, TerritoryType::LAND, ClimateType::TROPICAL, 20, 25},
    {35, "Korea", 620, 170, TerritoryType::LAND, ClimateType::TEMPERATE, 15, 20},
    
    // Oceania
    {36, "Australia", 620, 380, TerritoryType::LAND, ClimateType::DESERT, 22, 28},
    {37, "New Zealand", 660, 420, TerritoryType::LAND, ClimateType::TEMPERATE, 12, 16},
    {38, "Papua New Guinea", 640, 340, TerritoryType::LAND, ClimateType::TROPICAL, 10, 14},
    {39, "Indonesia", 610, 320, TerritoryType::LAND, ClimateType::TROPICAL, 18, 22},
    
    // Antarctica
    {40, "Antarctica", 400, 480, TerritoryType::LAND, ClimateType::ANTARCTIC, 5, 8},
    
    // Naval Regions
    {41, "North Atlantic", 300, 100, TerritoryType::NAVAL, ClimateType::TEMPERATE, 0, 0},
    {42, "South Atlantic", 320, 300, TerritoryType::NAVAL, ClimateType::TEMPERATE, 0, 0},
    {43, "North Pacific", 400, 120, TerritoryType::NAVAL, ClimateType::TEMPERATE, 0, 0},
    {44, "South Pacific", 500, 350, TerritoryType::NAVAL, ClimateType::TEMPERATE, 0, 0},
    {45, "Indian Ocean", 500, 300, TerritoryType::NAVAL, ClimateType::TROPICAL, 0, 0},
    {46, "Mediterranean Sea", 410, 180, TerritoryType::NAVAL, ClimateType::MEDITERRANEAN, 0, 0},
    {47, "Arctic Ocean", 350, 30, TerritoryType::NAVAL, ClimateType::ARCTIC, 0, 0},
    {48, "Southern Ocean", 450, 460, TerritoryType::NAVAL, ClimateType::ANTARCTIC, 0, 0}
};

GameBoard::GameBoard() 
    : mapWidth(800.0), mapHeight(500.0), zoomLevel(1.0), viewCenter(400.0, 250.0) {
}

GameBoard::~GameBoard() {
}

bool GameBoard::initialize() {
    try {
        std::cout << "Initializing game board..." << std::endl;
        
        // Initialize territories
        initializeTerritories();
        
        // Setup adjacency relationships
        setupAdjacency();
        
        // Initialize cities in territories
        initializeCities();
        
        // Create map outlines for rendering
        createMapOutlines();
        
        // Initialize population levels
        for (const auto& territory : territories) {
            for (const auto& city : territory.cities) {
                cityPopulationLevels[city.id] = 1; // Start at level 1
            }
        }
        
        std::cout << "Game board initialized with " << territories.size() << " territories" << std::endl;
        return true;
        
    } catch (const std::exception& e) {
        std::cerr << "Error initializing game board: " << e.what() << std::endl;
        return false;
    }
}

void GameBoard::initializeTerritories() {
    territories.clear();
    territoryMap.clear();
    controlledTerritories.clear();
    
    // Initialize controlled territories for all 5 players
    for (int i = 1; i <= 5; i++) {
        controlledTerritories[static_cast<PlayerID>(i)] = std::vector<int>();
    }
    
    // Create territories from static data
    int numTerritories = sizeof(WORLD_TERRITORIES) / sizeof(WORLD_TERRITORIES[0]);
    for (int i = 0; i < numTerritories; i++) {
        const auto& data = WORLD_TERRITORIES[i];
        
        Territory territory(data.id, data.name, Coordinates(data.x, data.y));
        territory.type = data.type;
        territory.climate = data.climate;
        territory.baseInfluence = data.baseInfluence;
        territory.baseCurrency = data.baseCurrency;
        
        territories.push_back(territory);
        territoryMap[data.id] = &territories.back();
    }
    
    std::cout << "Created " << territories.size() << " territories" << std::endl;
}

void GameBoard::setupAdjacency() {
    // Setup basic adjacency relationships for territories
    // This is a simplified version - in a full implementation, this would be
    // based on actual geographic boundaries
    
    // North America adjacency
    addTerritoryAdjacency(1, 2);  // US-Canada
    addTerritoryAdjacency(1, 3);  // US-Mexico
    addTerritoryAdjacency(2, 4);  // Canada-Alaska
    addTerritoryAdjacency(1, 41); // US-North Atlantic
    addTerritoryAdjacency(2, 41); // Canada-North Atlantic
    addTerritoryAdjacency(3, 42); // Mexico-South Atlantic
    
    // South America adjacency
    addTerritoryAdjacency(6, 9);  // Brazil-Peru
    addTerritoryAdjacency(6, 10); // Brazil-Colombia
    addTerritoryAdjacency(7, 8);  // Argentina-Chile
    addTerritoryAdjacency(8, 9);  // Chile-Peru
    addTerritoryAdjacency(9, 10); // Peru-Colombia
    
    // Europe adjacency
    addTerritoryAdjacency(11, 12); // UK-France
    addTerritoryAdjacency(12, 13); // France-Germany
    addTerritoryAdjacency(13, 14); // Germany-Italy
    addTerritoryAdjacency(12, 15); // France-Spain
    addTerritoryAdjacency(13, 16); // Germany-Poland
    addTerritoryAdjacency(16, 17); // Poland-Scandinavia
    addTerritoryAdjacency(13, 18); // Germany-Eastern Europe
    addTerritoryAdjacency(11, 41); // UK-North Atlantic
    addTerritoryAdjacency(14, 46); // Italy-Mediterranean
    
    // Africa adjacency
    addTerritoryAdjacency(19, 20); // Egypt-Libya
    addTerritoryAdjacency(20, 24); // Libya-Morocco
    addTerritoryAdjacency(21, 23); // Nigeria-Kenya
    addTerritoryAdjacency(22, 23); // South Africa-Kenya (simplified)
    addTerritoryAdjacency(19, 25); // Egypt-Saudi Arabia
    
    // Asia adjacency
    addTerritoryAdjacency(30, 31); // Russia-China
    addTerritoryAdjacency(31, 32); // China-India
    addTerritoryAdjacency(31, 35); // China-Korea
    addTerritoryAdjacency(32, 34); // India-Southeast Asia
    addTerritoryAdjacency(35, 33); // Korea-Japan
    
    // Oceania adjacency
    addTerritoryAdjacency(36, 37); // Australia-New Zealand
    addTerritoryAdjacency(36, 38); // Australia-Papua New Guinea
    addTerritoryAdjacency(38, 39); // Papua New Guinea-Indonesia
    
    // Naval adjacency (simplified)
    addTerritoryAdjacency(41, 42); // North Atlantic-South Atlantic
    addTerritoryAdjacency(43, 44); // North Pacific-South Pacific
    addTerritoryAdjacency(42, 45); // South Atlantic-Indian Ocean
    addTerritoryAdjacency(44, 45); // South Pacific-Indian Ocean
    addTerritoryAdjacency(46, 45); // Mediterranean-Indian Ocean
}

void GameBoard::addTerritoryAdjacency(int territory1, int territory2) {
    if (territoryMap.find(territory1) != territoryMap.end() &&
        territoryMap.find(territory2) != territoryMap.end()) {
        
        territoryMap[territory1]->addAdjacentTerritory(territory2);
        territoryMap[territory2]->addAdjacentTerritory(territory1);
    }
}

void GameBoard::initializeCities() {
    // Initialize major cities for key territories
    // In a full implementation, this would include many more cities
    
    // North America
    addCityToTerritory(1, "Washington DC", 190, 140);
    addCityToTerritory(1, "New York", 210, 130);
    addCityToTerritory(2, "Ottawa", 200, 70);
    addCityToTerritory(3, "Mexico City", 175, 210);
    
    // South America
    addCityToTerritory(6, "Brasilia", 285, 315);
    addCityToTerritory(6, "Rio de Janeiro", 295, 330);
    addCityToTerritory(7, "Buenos Aires", 255, 405);
    addCityToTerritory(9, "Lima", 235, 345);
    
    // Europe
    addCityToTerritory(11, "London", 375, 125);
    addCityToTerritory(12, "Paris", 385, 145);
    addCityToTerritory(13, "Berlin", 395, 135);
    addCityToTerritory(14, "Rome", 415, 165);
    addCityToTerritory(15, "Madrid", 375, 155);
    addCityToTerritory(16, "Warsaw", 425, 125);
    addCityToTerritory(17, "Stockholm", 415, 85);
    
    // Africa
    addCityToTerritory(19, "Cairo", 415, 215);
    addCityToTerritory(21, "Lagos", 375, 255);
    addCityToTerritory(22, "Cape Town", 415, 385);
    addCityToTerritory(23, "Nairobi", 435, 295);
    addCityToTerritory(24, "Casablanca", 365, 185);
    
    // Middle East
    addCityToTerritory(25, "Riyadh", 455, 245);
    addCityToTerritory(27, "Istanbul", 465, 175);
    addCityToTerritory(28, "Jerusalem", 445, 205);
    
    // Asia
    addCityToTerritory(30, "Moscow", 550, 115);
    addCityToTerritory(31, "Beijing", 585, 195);
    addCityToTerritory(32, "New Delhi", 535, 245);
    addCityToTerritory(33, "Tokyo", 655, 175);
    addCityToTerritory(35, "Seoul", 625, 165);
    
    // Oceania
    addCityToTerritory(36, "Canberra", 625, 385);
    addCityToTerritory(36, "Sydney", 635, 375);
    addCityToTerritory(37, "Wellington", 665, 425);
    addCityToTerritory(39, "Jakarta", 605, 315);
}

void GameBoard::addCityToTerritory(int territoryId, const std::string& cityName, 
                                   double x, double y) {
    auto it = territoryMap.find(territoryId);
    if (it != territoryMap.end()) {
        static int nextCityId = 1;
        City city(nextCityId++, cityName, Coordinates(x, y));
        
        // Set city-specific values based on territory importance
        if (territoryId <= 5) { // North America
            city.baseCurrencyProduction = 15 + (nextCityId % 5);
            city.baseInfluenceProduction = 8 + (nextCityId % 3);
        } else if (territoryId <= 10) { // South America
            city.baseCurrencyProduction = 12 + (nextCityId % 4);
            city.baseInfluenceProduction = 6 + (nextCityId % 2);
        } else if (territoryId <= 18) { // Europe
            city.baseCurrencyProduction = 18 + (nextCityId % 6);
            city.baseInfluenceProduction = 10 + (nextCityId % 4);
        } else if (territoryId <= 29) { // Africa/Middle East
            city.baseCurrencyProduction = 10 + (nextCityId % 5);
            city.baseInfluenceProduction = 5 + (nextCityId % 3);
        } else if (territoryId <= 35) { // Asia
            city.baseCurrencyProduction = 20 + (nextCityId % 7);
            city.baseInfluenceProduction = 12 + (nextCityId % 5);
        } else { // Oceania/Antarctica
            city.baseCurrencyProduction = 8 + (nextCityId % 4);
            city.baseInfluenceProduction = 4 + (nextCityId % 2);
        }
        
        it->second->cities.push_back(city);
    }
}

void GameBoard::createMapOutlines() {
    // Create simplified continent outlines for rendering
    // In a full implementation, this would use actual geographic data
    
    continentOutlines.clear();
    
    // North America outline (simplified)
    std::vector<Coordinates> northAmerica = {
        {100, 50}, {300, 50}, {320, 100}, {280, 200}, 
        {250, 250}, {150, 220}, {100, 150}
    };
    continentOutlines.push_back(northAmerica);
    
    // South America outline
    std::vector<Coordinates> southAmerica = {
        {200, 280}, {280, 270}, {300, 350}, {280, 450}, 
        {220, 450}, {180, 380}, {190, 320}
    };
    continentOutlines.push_back(southAmerica);
    
    // Europe outline
    std::vector<Coordinates> europe = {
        {350, 100}, {450, 100}, {470, 130}, {450, 200}, 
        {400, 220}, {350, 180}, {340, 140}
    };
    continentOutlines.push_back(europe);
    
    // Africa outline
    std::vector<Coordinates> africa = {
        {340, 180}, {440, 180}, {480, 280}, {450, 420}, 
        {350, 440}, {320, 350}, {330, 250}
    };
    continentOutlines.push_back(africa);
    
    // Asia outline
    std::vector<Coordinates> asia = {
        {470, 80}, {680, 80}, {700, 200}, {650, 300}, 
        {520, 280}, {480, 180}
    };
    continentOutlines.push_back(asia);
    
    // Australia outline
    std::vector<Coordinates> australia = {
        {580, 360}, {680, 360}, {690, 420}, {620, 440}, 
        {570, 400}
    };
    continentOutlines.push_back(australia);
}

void GameBoard::assignStartingTerritories() {
    // Clear existing control
    for (auto& territory : territories) {
        territory.controller = PlayerID::UNITED_STATES; // Default to neutral
        territory.absenceTokens.clear();
        territory.isContested = false;
    }
    
    controlledTerritories.clear();
    for (int i = 1; i <= 5; i++) {
        controlledTerritories[static_cast<PlayerID>(i)] = std::vector<int>();
    }
    
    // Assign starting territories for each player based on game design
    
    // United States - North America
    setTerritoryController(1, PlayerID::UNITED_STATES);  // USA
    setTerritoryController(2, PlayerID::UNITED_STATES);  // Canada
    setTerritoryController(3, PlayerID::UNITED_STATES);  // Mexico
    setTerritoryController(4, PlayerID::UNITED_STATES);  // Alaska
    setTerritoryController(5, PlayerID::UNITED_STATES);  // Greenland
    
    // Russia - Russia and Eastern Europe
    setTerritoryController(30, PlayerID::RUSSIA);  // Russia
    setTerritoryController(16, PlayerID::RUSSIA);  // Poland
    setTerritoryController(18, PlayerID::RUSSIA);  // Eastern Europe
    
    // European Union - Western Europe
    setTerritoryController(11, PlayerID::EUROPEAN_UNION);  // UK
    setTerritoryController(12, PlayerID::EUROPEAN_UNION);  // France
    setTerritoryController(13, PlayerID::EUROPEAN_UNION);  // Germany
    setTerritoryController(14, PlayerID::EUROPEAN_UNION);  // Italy
    setTerritoryController(15, PlayerID::EUROPEAN_UNION);  // Spain
    setTerritoryController(17, PlayerID::EUROPEAN_UNION);  // Scandinavia
    
    // Southern Hemisphere Alliance - South America, Africa south, Oceania
    setTerritoryController(6, PlayerID::SOUTHERN_ALLIANCE);   // Brazil
    setTerritoryController(7, PlayerID::SOUTHERN_ALLIANCE);   // Argentina
    setTerritoryController(22, PlayerID::SOUTHERN_ALLIANCE);  // South Africa
    setTerritoryController(36, PlayerID::SOUTHERN_ALLIANCE);  // Australia
    setTerritoryController(37, PlayerID::SOUTHERN_ALLIANCE);  // New Zealand
    setTerritoryController(40, PlayerID::SOUTHERN_ALLIANCE);  // Antarctica (claims)
    
    // Dark Continent starts with no territories
    // Territories will be gained through fragment spawning and invasion
    
    std::cout << "Starting territories assigned to all 5 players" << std::endl;
}

// Territory management methods
Territory* GameBoard::getTerritory(int id) {
    auto it = territoryMap.find(id);
    return (it != territoryMap.end()) ? it->second : nullptr;
}

Territory* GameBoard::getTerritoryByName(const std::string& name) {
    for (auto& territory : territories) {
        if (territory.name == name) {
            return &territory;
        }
    }
    return nullptr;
}

int GameBoard::getTerritoryCount(PlayerID player) const {
    auto it = controlledTerritories.find(player);
    return (it != controlledTerritories.end()) ? static_cast<int>(it->second.size()) : 0;
}

void GameBoard::setTerritoryController(int territoryId, PlayerID newController) {
    Territory* territory = getTerritory(territoryId);
    if (territory) {
        PlayerID oldController = territory->controller;
        
        // Remove from old controller's list
        if (oldController != PlayerID::UNITED_STATES) { // Not neutral
            auto it = controlledTerritories.find(oldController);
            if (it != controlledTerritories.end()) {
                auto& territories = it->second;
                territories.erase(std::remove(territories.begin(), territories.end(), territoryId), 
                                 territories.end());
            }
        }
        
        // Set new controller
        territory->controller = newController;
        
        // Add to new controller's list
        if (newController != PlayerID::UNITED_STATES) { // Not neutral
            controlledTerritories[newController].push_back(territoryId);
        }
        
        std::cout << "Territory " << territory->name << " control changed to player " 
                  << static_cast<int>(newController) << std::endl;
    }
}

bool GameBoard::changeTerritoryControl(int territoryId, PlayerID fromPlayer, PlayerID toPlayer) {
    Territory* territory = getTerritory(territoryId);
    if (territory && territory->controller == fromPlayer) {
        setTerritoryController(territoryId, toPlayer);
        return true;
    }
    return false;
}

void GameBoard::placeAbsenceToken(int territoryId, PlayerID player) {
    Territory* territory = getTerritory(territoryId);
    if (territory) {
        territory->absenceTokens[player] = true;
    }
}

void GameBoard::removeAbsenceToken(int territoryId, PlayerID player) {
    Territory* territory = getTerritory(territoryId);
    if (territory) {
        territory->absenceTokens.erase(player);
    }
}

bool GameBoard::hasAbsenceToken(int territoryId, PlayerID player) const {
    const Territory* territory = const_cast<GameBoard*>(this)->getTerritory(territoryId);
    if (territory) {
        auto it = territory->absenceTokens.find(player);
        return it != territory->absenceTokens.end() && it->second;
    }
    return false;
}

// City management methods
City* GameBoard::getCity(int cityId) {
    for (auto& territory : territories) {
        for (auto& city : territory.cities) {
            if (city.id == cityId) {
                return &city;
            }
        }
    }
    return nullptr;
}

City* GameBoard::getCityInTerritory(int territoryId, int cityIndex) {
    Territory* territory = getTerritory(territoryId);
    if (territory && cityIndex >= 0 && cityIndex < static_cast<int>(territory->cities.size())) {
        return &territory->cities[cityIndex];
    }
    return nullptr;
}

void GameBoard::devastateCity(int cityId) {
    City* city = getCity(cityId);
    if (city) {
        city->isDevastated = true;
        std::cout << "City " << city->name << " has been devastated" << std::endl;
    }
}

void GameBoard::repairCity(int cityId) {
    City* city = getCity(cityId);
    if (city) {
        city->isDevastated = false;
        std::cout << "City " << city->name << " has been repaired" << std::endl;
    }
}

bool GameBoard::isCityDevastated(int cityId) const {
    const City* city = const_cast<GameBoard*>(this)->getCity(cityId);
    return city ? city->isDevastated : false;
}

// Population counter integration
void GameBoard::updateCityPopulation(int cityId, int newLevel) {
    cityPopulationLevels[cityId] = std::max(0, std::min(5, newLevel));
    
    City* city = getCity(cityId);
    if (city) {
        // Update city properties based on population level
        switch (newLevel) {
            case 0: // Underpopulated
                city->currentPopulation = city->basePopulation * 0.5;
                city->isOverpopulated = false;
                break;
            case 1: // Normal
                city->currentPopulation = city->basePopulation;
                city->isOverpopulated = false;
                break;
            case 2: // Growing
                city->currentPopulation = city->basePopulation * 1.5;
                city->isOverpopulated = false;
                break;
            case 3: // Optimal
                city->currentPopulation = city->basePopulation * 2.0;
                city->isOverpopulated = false;
                break;
            case 4: // Dense
                city->currentPopulation = city->basePopulation * 3.0;
                city->isOverpopulated = false;
                break;
            case 5: // Overpopulated
                city->currentPopulation = city->basePopulation * 4.0;
                city->isOverpopulated = true;
                break;
        }
        
        std::cout << "City " << city->name << " population updated to level " << newLevel 
                  << " (" << city->currentPopulation << " people)" << std::endl;
    }
}

int GameBoard::getCityPopulationLevel(int cityId) const {
    auto it = cityPopulationLevels.find(cityId);
    return (it != cityPopulationLevels.end()) ? it->second : 1;
}

std::vector<int> GameBoard::getCitiesInTerritory(int territoryId) const {
    std::vector<int> cityIds;
    const Territory* territory = const_cast<GameBoard*>(this)->getTerritory(territoryId);
    if (territory) {
        for (const auto& city : territory->cities) {
            cityIds.push_back(city.id);
        }
    }
    return cityIds;
}

// Dark Continent mechanics
void GameBoard::placeDarkContinentFragments() {
    fragments.clear();
    
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> cityDis(2, 60); // Cities numbered 2-60 as per rules
    
    // Place 10 fragments (increased from original for 5-player game)
    for (int i = 0; i < 12; i++) {
        int cityId = cityDis(gen);
        City* city = getCity(cityId);
        
        if (city) {
            fragments.emplace_back(i + 1, cityId, city->position, ENGINE.getCurrentYear());
            std::cout << "Dark Continent Fragment " << (i + 1) << " placed over city " 
                      << city->name << " (ID: " << cityId << ")" << std::endl;
        }
    }
    
    std::cout << "Placed " << fragments.size() << " Dark Continent fragments" << std::endl;
}

void GameBoard::fragmentDarkContinent() {
    std::cout << "Dark Continent fragments spreading across the globe!" << std::endl;
    
    // Mark all fragments as active for spawning units
    for (auto& fragment : fragments) {
        fragment.isActive = true;
    }
}

DarkContinentFragment* GameBoard::getFragmentAtCity(int cityId) {
    for (auto& fragment : fragments) {
        if (fragment.cityId == cityId) {
            return &fragment;
        }
    }
    return nullptr;
}

std::vector<int> GameBoard::getTerritoriesWithFragments() const {
    std::vector<int> territoryIds;
    
    for (const auto& fragment : fragments) {
        // Find which territory contains this city
        for (const auto& territory : territories) {
            for (const auto& city : territory.cities) {
                if (city.id == fragment.cityId) {
                    territoryIds.push_back(territory.id);
                    break;
                }
            }
        }
    }
    
    // Remove duplicates
    std::sort(territoryIds.begin(), territoryIds.end());
    territoryIds.erase(std::unique(territoryIds.begin(), territoryIds.end()), territoryIds.end());
    
    return territoryIds;
}

// Adjacency and movement methods
bool GameBoard::areTerritoriesAdjacent(int territory1, int territory2) const {
    const Territory* terr1 = const_cast<GameBoard*>(this)->getTerritory(territory1);
    if (terr1) {
        return terr1->hasAdjacentTerritory(territory2);
    }
    return false;
}

std::vector<int> GameBoard::getAdjacentTerritories(int territoryId) const {
    std::vector<int> adjacent;
    const Territory* territory = const_cast<GameBoard*>(this)->getTerritory(territoryId);
    
    if (territory) {
        for (int adjId : territory->adjacentTerritories) {
            adjacent.push_back(adjId);
        }
    }
    
    return adjacent;
}

bool GameBoard::isValidMovement(int fromTerritory, int toTerritory, PlayerID player) const {
    // Check if territories are adjacent
    if (!areTerritoriesAdjacent(fromTerritory, toTerritory)) {
        return false;
    }
    
    // Check if player controls fromTerritory or has absence token there
    const Territory* fromTerr = const_cast<GameBoard*>(this)->getTerritory(fromTerritory);
    if (!fromTerr) {
        return false;
    }
    
    if (fromTerr->controller != player && !hasAbsenceToken(fromTerritory, player)) {
        return false;
    }
    
    // Check movement rules for different territory types
    const Territory* toTerr = const_cast<GameBoard*>(this)->getTerritory(toTerritory);
    if (!toTerr) {
        return false;
    }
    
    // Can move to own territories, contested territories, or uncontrolled territories
    if (toTerr->controller == player || toTerr->controller == PlayerID::UNITED_STATES || toTerr->isContested) {
        return true;
    }
    
    // Can move to enemy territories (for attack)
    return true;
}

// Map rendering and UI methods
void GameBoard::setZoom(double zoom) {
    zoomLevel = std::max(0.1, std::min(10.0, zoom));
}

void GameBoard::setViewCenter(const Coordinates& center) {
    viewCenter.x = std::max(0, std::min(mapWidth, center.x));
    viewCenter.y = std::max(0, std::min(mapHeight, center.y));
}

void GameBoard::panView(double deltaX, double deltaY) {
    viewCenter.x += deltaX / zoomLevel;
    viewCenter.y += deltaY / zoomLevel;
    setViewCenter(viewCenter);
}

void GameBoard::zoomView(double factor) {
    double newZoom = zoomLevel * factor;
    setZoom(newZoom);
}

Coordinates GameBoard::worldToScreen(const Coordinates& worldPos) const {
    double screenX = (worldPos.x - viewCenter.x) * zoomLevel + (mapWidth / 2.0);
    double screenY = (worldPos.y - viewCenter.y) * zoomLevel + (mapHeight / 2.0);
    return Coordinates(screenX, screenY);
}

Coordinates GameBoard::screenToWorld(const Coordinates& screenPos) const {
    double worldX = (screenPos.x - (mapWidth / 2.0)) / zoomLevel + viewCenter.x;
    double worldY = (screenPos.y - (mapHeight / 2.0)) / zoomLevel + viewCenter.y;
    return Coordinates(worldX, worldY);
}

int GameBoard::getTerritoryAtPosition(const Coordinates& position) const {
    for (const auto& territory : territories) {
        if (isPositionInTerritory(position, territory.id)) {
            return territory.id;
        }
    }
    return -1;
}

bool GameBoard::isPositionInTerritory(const Coordinates& position, int territoryId) const {
    const Territory* territory = const_cast<GameBoard*>(this)->getTerritory(territoryId);
    if (!territory) {
        return false;
    }
    
    // Simple distance-based check (simplified)
    // In a full implementation, this would use proper polygon point-in-polygon test
    double distance = position.distanceTo(territory->centerPosition);
    return distance < 30.0 / zoomLevel; // Approximate territory radius
}

// Utility methods
void GameBoard::reset() {
    territories.clear();
    territoryMap.clear();
    fragments.clear();
    controlledTerritories.clear();
    cityPopulationLevels.clear();
    
    zoomLevel = 1.0;
    viewCenter = Coordinates(400.0, 250.0);
}

void GameBoard::update(double deltaTime) {
    // Update board animations, effects, etc.
    // This would handle visual updates in the rendering system
}

std::string GameBoard::getTerritoryDescription(int territoryId) const {
    const Territory* territory = const_cast<GameBoard*>(this)->getTerritory(territoryId);
    if (!territory) {
        return "Unknown Territory";
    }
    
    std::ostringstream description;
    description << territory->name << " (ID: " << territory->id << ")\n";
    description << "Controller: Player " << static_cast<int>(territory->controller) << "\n";
    description << "Type: " << static_cast<int>(territory->type) << "\n";
    description << "Climate: " << static_cast<int>(territory->climate) << "\n";
    description << "Base Influence: " << territory->baseInfluence << "\n";
    description << "Base Currency: " << territory->baseCurrency << "\n";
    description << "Cities: " << territory->cities.size() << "\n";
    
    if (!territory->cities.empty()) {
        description << "City Details:\n";
        for (const auto& city : territory->cities) {
            description << "  - " << city.name << " (Pop: " << city.currentPopulation;
            if (city.isDevastated) description << ", DEVASTATED";
            if (city.isOverpopulated) description << ", OVERPOPULATED";
            description << ")\n";
        }
    }
    
    return description.str();
}

// Additional methods would be implemented here...
// Due to length constraints, I'm showing the core implementation