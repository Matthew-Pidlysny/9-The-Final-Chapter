#include "GameEngine.h"
#include "GameBoard.h"
#include "PlayerManager.h"
#include "ResourceManager.h"
#include "CardSystem.h"
#include "CombatSystem.h"
#include "PopulationCounter.h"
#include "EconomySystem.h"
#include "NetworkManager.h"
#include "SaveSystem.h"
#include "EventManager.h"
#include <iostream>
#include <algorithm>
#include <random>

std::unique_ptr<GameEngine> GameEngine::instance = nullptr;

GameEngine::GameEngine() 
    : currentState(GameState::MENU)
    , currentYear(2) // Game starts at year 2 since nukes were disabled
    , currentTurn(0)
    , currentPlayer(PlayerID::UNITED_STATES)
    , isGameRunning(false)
    , turnStartTime(std::chrono::steady_clock::now())
    , lastAutoSave(std::chrono::steady_clock::now()) {
}

GameEngine& GameEngine::getInstance() {
    if (!instance) {
        instance = std::make_unique<GameEngine>();
    }
    return *instance;
}

void GameEngine::initialize() {
    if (!instance) {
        instance = std::make_unique<GameEngine>();
    }
}

void GameEngine::shutdown() {
    if (instance) {
        instance->cleanup();
        instance.reset();
    }
}

bool GameEngine::initialize(const GameConfig& gameConfig) {
    config = gameConfig;
    
    try {
        // Initialize core systems
        gameBoard = std::make_unique<GameBoard>();
        playerManager = std::make_unique<PlayerManager>();
        resourceManager = std::make_unique<ResourceManager>();
        cardSystem = std::make_unique<CardSystem>();
        combatSystem = std::make_unique<CombatSystem>();
        populationCounter = std::make_unique<PopulationCounter>();
        economySystem = std::make_unique<EconomySystem>();
        saveSystem = std::make_unique<SaveSystem>();
        eventManager = std::make_unique<EventManager>();
        
        // Initialize network manager if async mode is enabled
        if (config.asyncMode) {
            networkManager = std::make_unique<NetworkManager>();
        }
        
        // Initialize subsystems
        if (!gameBoard->initialize() || 
            !playerManager->initialize() ||
            !resourceManager->initialize() ||
            !cardSystem->initialize() ||
            !combatSystem->initialize() ||
            !populationCounter->initialize() ||
            !economySystem->initialize() ||
            !saveSystem->initialize() ||
            !eventManager->initialize()) {
            
            std::cerr << "Failed to initialize game systems!" << std::endl;
            return false;
        }
        
        // Initialize network if enabled
        if (networkManager && !networkManager->initialize(config.serverUrl)) {
            std::cerr << "Failed to initialize network manager!" << std::endl;
            return false;
        }
        
        // Initialize players
        initializePlayers();
        
        // Register event callbacks
        registerEventCallback("turn_ended", [this]() {
            nextTurn();
        });
        
        registerEventCallback("game_over", [this]() {
            setState(GameState::GAME_OVER);
        });
        
        registerEventCallback("federation_triggered", [this]() {
            enterFederationMode();
        });
        
        std::cout << "GameEngine initialized successfully!" << std::endl;
        return true;
        
    } catch (const std::exception& e) {
        std::cerr << "Exception during GameEngine initialization: " << e.what() << std::endl;
        return false;
    }
}

void GameEngine::run() {
    isGameRunning = true;
    setState(GameState::PLAYING);
    
    std::cout << "Starting Dark Continent 5-Player Game..." << std::endl;
    std::cout << "Current Year: " << currentYear << " (Since nukes were disabled)" << std::endl;
    
    startNewTurn();
    
    // Main game loop would be handled by the main application
    // This is just the game logic initialization
}

void GameEngine::update(float deltaTime) {
    if (!isGameRunning) return;
    
    updateTimers();
    
    switch (currentState) {
        case GameState::PLAYING:
            processPendingActions();
            validateGameState();
            
            // Check victory conditions
            if (checkVictoryConditions()) {
                triggerEvent("game_over");
            }
            
            // Check auto-save
            if (config.autoSave && autoSaveCheck()) {
                saveGame("autosave");
            }
            break;
            
        case GameState::FEDERATION:
            // Handle federation mode updates
            break;
            
        case GameState::PAUSED:
            // No updates when paused
            break;
            
        default:
            break;
    }
}

void GameEngine::render() {
    // Rendering would be handled by the Renderer system
    // This is a placeholder for game state rendering
}

void GameEngine::setState(GameState newState) {
    if (currentState != newState) {
        GameState oldState = currentState;
        currentState = newState;
        
        std::cout << "Game state changed: " << getGameStateString() << std::endl;
        
        // Trigger state change event
        eventManager->triggerEvent("state_changed", {
            {"old_state", static_cast<int>(oldState)},
            {"new_state", static_cast<int>(newState)}
        });
    }
}

void GameEngine::startNewTurn() {
    currentTurn++;
    turnStartTime = std::chrono::steady_clock::now();
    
    std::cout << "Turn " << currentTurn << " started - Player: " << static_cast<int>(currentPlayer) << std::endl;
    
    // Trigger turn start event
    triggerEvent("turn_started");
    
    // Handle player-specific turn start logic
    playerManager->onTurnStart(currentPlayer);
    
    // Handle year progression (every 4 turns = 1 year)
    if (shouldIncrementYear()) {
        incrementYear();
    }
}

void GameEngine::nextTurn() {
    // Handle turn end logic
    playerManager->onTurnEnd(currentPlayer);
    
    // Move to next player
    switch (currentPlayer) {
        case PlayerID::UNITED_STATES:
            currentPlayer = PlayerID::RUSSIA;
            break;
        case PlayerID::RUSSIA:
            currentPlayer = PlayerID::EUROPEAN_UNION;
            break;
        case PlayerID::EUROPEAN_UNION:
            currentPlayer = PlayerID::SOUTHERN_ALLIANCE;
            break;
        case PlayerID::SOUTHERN_ALLIANCE:
            currentPlayer = PlayerID::DARK_CONTINENT;
            break;
        case PlayerID::DARK_CONTINENT:
            currentPlayer = PlayerID::UNITED_STATES;
            break;
    }
    
    // Skip Dark Continent if not spawned yet
    if (currentPlayer == PlayerID::DARK_CONTINENT && !isDarkContinentSpawned()) {
        currentPlayer = PlayerID::UNITED_STATES;
    }
    
    triggerEvent("turn_ended");
}

void GameEngine::endTurn() {
    // Handle immediate turn end (timeout or player action)
    handleTurnTimeout();
}

void GameEngine::incrementYear() {
    currentYear++;
    std::cout << "Year " << currentYear << " begins!" << std::endl;
    
    // Update population counter for all cities
    populationCounter->incrementYear();
    
    // Handle Dark Continent spawn check
    if (!isDarkContinentSpawned() && currentYear >= getDarkContinentYear()) {
        spawnDarkContinent();
    }
    
    // Trigger year progression event
    triggerEvent("year_incremented");
}

bool GameEngine::shouldIncrementYear() const {
    return (currentTurn % 4) == 0;
}

void GameEngine::initializePlayers() {
    // Initialize all 5 players with starting positions and resources
    playerManager->createPlayer(PlayerID::UNITED_STATES, "United States");
    playerManager->createPlayer(PlayerID::RUSSIA, "Russia");
    playerManager->createPlayer(PlayerID::EUROPEAN_UNION, "European Union");
    playerManager->createPlayer(PlayerID::SOUTHERN_ALLIANCE, "Southern Hemisphere Alliance");
    playerManager->createPlayer(PlayerID::DARK_CONTINENT, "The Dark Continent");
    
    // Set starting territories based on game design
    gameBoard->assignStartingTerritories();
    
    // Distribute starting cards
    cardSystem->distributeStartingCards();
    
    std::cout << "All 5 players initialized successfully!" << std::endl;
}

bool GameEngine::isValidPlayer(PlayerID player) const {
    return player >= PlayerID::UNITED_STATES && player <= PlayerID::DARK_CONTINENT;
}

void GameEngine::updateConfig(const GameConfig& newConfig) {
    config = newConfig;
    
    // Reinitialize network if async mode changed
    if (config.asyncMode && !networkManager) {
        networkManager = std::make_unique<NetworkManager>();
        networkManager->initialize(config.serverUrl);
    } else if (!config.asyncMode && networkManager) {
        networkManager.reset();
    }
}

void GameEngine::registerEventCallback(const std::string& eventName, std::function<void()> callback) {
    eventCallbacks[eventName] = callback;
}

void GameEngine::triggerEvent(const std::string& eventName) {
    auto it = eventCallbacks.find(eventName);
    if (it != eventCallbacks.end()) {
        it->second();
    }
    
    // Also trigger in event manager
    eventManager->triggerEvent(eventName);
}

bool GameEngine::checkVictoryConditions() {
    return checkFederationConditions() ||
           checkDominationConditions() ||
           checkInfluenceConditions() ||
           checkShimarraConditions() ||
           (currentYear >= 40); // Time limit reached
}

bool GameEngine::checkFederationConditions() {
    return cardSystem->allPlayersAccededToFederation();
}

bool GameEngine::checkDominationConditions() {
    // Check if any player controls all other player territories
    for (int i = 1; i <= 5; i++) {
        PlayerID player = static_cast<PlayerID>(i);
        if (hasPlayerDominance(player)) {
            return true;
        }
    }
    return false;
}

bool GameEngine::checkInfluenceConditions() {
    // Check if any player reached maximum influence
    for (int i = 1; i <= 5; i++) {
        PlayerID player = static_cast<PlayerID>(i);
        if (hasMaximumInfluence(player)) {
            return true;
        }
    }
    return false;
}

bool GameEngine::checkShimarraConditions() {
    // Check if any player reached maximum Shimarra
    for (int i = 1; i <= 5; i++) {
        PlayerID player = static_cast<PlayerID>(i);
        if (hasMaximumShimarra(player)) {
            return true;
        }
    }
    return false;
}

bool GameEngine::isDarkContinentSpawned() const {
    return gameBoard->hasDarkContinentFragments();
}

void GameEngine::spawnDarkContinent() {
    std::cout << "The Dark Continent spawns in year " << currentYear << "!" << std::endl;
    gameBoard->placeDarkContinentFragments();
    triggerEvent("dark_continent_spawned");
}

int GameEngine::getDarkContinentYear() const {
    // This would be determined by Dark Continent dice at game start
    // For now, return a default value
    return 15;
}

void GameEngine::handleDarkContinentFragmentation() {
    if (isDarkContinentSpawned() && currentYear == getDarkContinentYear() + 1) {
        gameBoard->fragmentDarkContinent();
        triggerEvent("dark_continent_fragmented");
    }
}

void GameEngine::enterFederationMode() {
    setState(GameState::FEDERATION);
    std::cout << "Entering Federation mode!" << std::endl;
    
    // Deal federation cards to all players
    cardSystem->dealFederationCards();
}

void GameEngine::handleFederationCard(const std::string& cardData) {
    // Handle federation card play
    cardSystem->processFederationCard(cardData);
    
    // Check if federation is complete
    if (cardSystem->isFederationComplete()) {
        exitFederationMode();
    }
}

void GameEngine::exitFederationMode() {
    setState(GameState::PLAYING);
    std::cout << "Federation mode ended!" << std::endl;
    
    // Calculate final scores
    triggerEvent("federation_ended");
}

bool GameEngine::saveGame(const std::string& saveName) {
    return saveSystem->save(saveName, *this);
}

bool GameEngine::loadGame(const std::string& saveName) {
    return saveSystem->load(saveName, *this);
}

bool GameEngine::autoSaveCheck() {
    auto now = std::chrono::steady_clock::now();
    auto elapsed = std::chrono::duration_cast<std::chrono::seconds>(now - lastAutoSave);
    return elapsed.count() >= config.autoSaveInterval;
}

std::string GameEngine::getGameStateString() const {
    switch (currentState) {
        case GameState::MENU: return "MENU";
        case GameState::SETUP: return "SETUP";
        case GameState::PLAYING: return "PLAYING";
        case GameState::PAUSED: return "PAUSED";
        case GameState::FEDERATION: return "FEDERATION";
        case GameState::GAME_OVER: return "GAME_OVER";
        default: return "UNKNOWN";
    }
}

void GameEngine::logGameAction(const std::string& action, PlayerID player) {
    std::cout << "[Year " << currentYear << ", Turn " << currentTurn << "] ";
    std::cout << "Player " << static_cast<int>(player) << ": " << action << std::endl;
}

GameEngine::GameStats GameEngine::getGameStats() const {
    // Return comprehensive game statistics
    GameStats stats;
    stats.totalTurns = currentTurn;
    stats.totalYears = currentYear;
    
    // Gather player-specific stats
    for (int i = 1; i <= 5; i++) {
        PlayerID player = static_cast<PlayerID>(i);
        stats.territoriesControlled[player] = gameBoard->getTerritoryCount(player);
        stats.totalInfluence[player] = playerManager->getInfluence(player);
        stats.totalCurrency[player] = playerManager->getCurrency(player);
        stats.cardsPlayed[player] = playerManager->getCardsPlayed(player);
        stats.unitsLost[player] = combatSystem->getUnitsLost(player);
        stats.unitsBuilt[player] = playerManager->getUnitsBuilt(player);
    }
    
    return stats;
}

void GameEngine::resetStats() {
    // Reset all game statistics
    currentTurn = 0;
    currentYear = 2;
    currentPlayer = PlayerID::UNITED_STATES;
}

// Private helper methods
void GameEngine::updateTimers() {
    // Handle turn timer
    if (config.turnTimeLimit > 0) {
        auto now = std::chrono::steady_clock::now();
        auto elapsed = std::chrono::duration_cast<std::chrono::seconds>(now - turnStartTime);
        
        if (elapsed.count() >= config.turnTimeLimit) {
            handleTurnTimeout();
        }
    }
}

void GameEngine::handleTurnTimeout() {
    std::cout << "Turn timeout for player " << static_cast<int>(currentPlayer) << std::endl;
    triggerEvent("turn_ended");
}

void GameEngine::processPendingActions() {
    if (networkManager) {
        networkManager->processPendingActions();
    }
}

void GameEngine::validateGameState() {
    // Ensure game state is consistent
    if (currentState == GameState::PLAYING && !isValidPlayer(currentPlayer)) {
        currentPlayer = PlayerID::UNITED_STATES;
    }
}

void GameEngine::cleanup() {
    gameBoard.reset();
    playerManager.reset();
    resourceManager.reset();
    cardSystem.reset();
    combatSystem.reset();
    populationCounter.reset();
    economySystem.reset();
    networkManager.reset();
    saveSystem.reset();
    eventManager.reset();
    
    eventCallbacks.clear();
    isGameRunning = false;
}

// Additional helper methods
int GameEngine::calculateVictoryPoints(PlayerID player) {
    // Calculate victory points based on game rules
    int influence = playerManager->getInfluence(player);
    int currency = playerManager->getCurrency(player);
    int cardsInHand = playerManager->getCardsInHand(player);
    
    if (cardsInHand > 0) {
        return (influence * currency) / cardsInHand;
    }
    return 0;
}

bool GameEngine::hasPlayerDominance(PlayerID player) {
    // Check if player controls all other player territories
    int totalTerritories = gameBoard->getTotalTerritoryCount();
    int playerTerritories = gameBoard->getTerritoryCount(player);
    
    return playerTerritories >= (totalTerritories * 0.8); // 80% domination
}

bool GameEngine::hasMaximumInfluence(PlayerID player) {
    return playerManager->getInfluence(player) >= 1000; // Maximum influence threshold
}

bool GameEngine::hasMaximumShimarra(PlayerID player) {
    return playerManager->getShimarra(player) >= 100; // Maximum Shimarra threshold
}

int GameEngine::rollDarkContinentDice() {
    static std::random_device rd;
    static std::mt19937 gen(rd());
    static std::uniform_int_distribution<> dis(1, 20);
    
    // Roll two 20-sided dice and combine
    int roll1 = dis(gen);
    int roll2 = dis(gen);
    
    return (roll1 * 100) + roll2; // Combine for unique year calculation
}

void GameEngine::rollTimeDice() {
    // Time dice start at 2 and increment by 1 each year
    // No rolling needed, just increment
}