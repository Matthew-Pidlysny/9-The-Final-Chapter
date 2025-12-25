#ifndef GAMEENGINE_H
#define GAMEENGINE_H

#include <memory>
#include <vector>
#include <map>
#include <string>
#include <functional>
#include <chrono>

// Forward declarations
class GameBoard;
class PlayerManager;
class ResourceManager;
class CardSystem;
class CombatSystem;
class PopulationCounter;
class EconomySystem;
class NetworkManager;
class SaveSystem;
class EventManager;

enum class GameState {
    MENU,
    SETUP,
    PLAYING,
    PAUSED,
    FEDERATION,
    GAME_OVER
};

enum class PlayerID {
    UNITED_STATES = 1,
    RUSSIA = 2,
    EUROPEAN_UNION = 3,
    SOUTHERN_ALLIANCE = 4,
    DARK_CONTINENT = 5
};

struct GameConfig {
    int maxPlayers = 5;
    bool asyncMode = false;
    std::string serverUrl = "";
    int turnTimeLimit = 300; // seconds
    bool autoSave = true;
    int autoSaveInterval = 60; // seconds
    std::map<std::string, bool> enabledFeatures;
};

class GameEngine {
private:
    static std::unique_ptr<GameEngine> instance;
    GameState currentState;
    GameConfig config;
    int currentYear;
    int currentTurn;
    PlayerID currentPlayer;
    bool isGameRunning;
    
    // Core systems
    std::unique_ptr<GameBoard> gameBoard;
    std::unique_ptr<PlayerManager> playerManager;
    std::unique_ptr<ResourceManager> resourceManager;
    std::unique_ptr<CardSystem> cardSystem;
    std::unique_ptr<CombatSystem> combatSystem;
    std::unique_ptr<PopulationCounter> populationCounter;
    std::unique_ptr<EconomySystem> economySystem;
    std::unique_ptr<NetworkManager> networkManager;
    std::unique_ptr<SaveSystem> saveSystem;
    std::unique_ptr<EventManager> eventManager;
    
    // Timing
    std::chrono::steady_clock::time_point turnStartTime;
    std::chrono::steady_clock::time_point lastAutoSave;
    
    // Event callbacks
    std::map<std::string, std::function<void()>> eventCallbacks;
    
    GameEngine();
    
public:
    // Singleton pattern
    static GameEngine& getInstance();
    static void initialize();
    static void shutdown();
    
    // Core game loop
    bool initialize(const GameConfig& config);
    void run();
    void update(float deltaTime);
    void render();
    void shutdown();
    
    // Game state management
    void setState(GameState newState);
    GameState getState() const { return currentState; }
    bool isRunning() const { return isGameRunning; }
    
    // Turn management
    void startNewTurn();
    void nextTurn();
    void endTurn();
    PlayerID getCurrentPlayer() const { return currentPlayer; }
    int getCurrentYear() const { return currentYear; }
    int getCurrentTurn() const { return currentTurn; }
    
    // Year progression (Dark Continent rules: 4 turns = 1 year)
    void incrementYear();
    bool shouldIncrementYear() const;
    
    // Player management
    void initializePlayers();
    bool isValidPlayer(PlayerID player) const;
    
    // System accessors
    GameBoard& getBoard() { return *gameBoard; }
    PlayerManager& getPlayerManager() { return *playerManager; }
    ResourceManager& getResourceManager() { return *resourceManager; }
    CardSystem& getCardSystem() { return *cardSystem; }
    CombatSystem& getCombatSystem() { return *combatSystem; }
    PopulationCounter& getPopulationCounter() { return *populationCounter; }
    EconomySystem& getEconomySystem() { return *economySystem; }
    NetworkManager& getNetworkManager() { return *networkManager; }
    SaveSystem& getSaveSystem() { return *saveSystem; }
    EventManager& getEventManager() { return *eventManager; }
    
    // Configuration
    const GameConfig& getConfig() const { return config; }
    void updateConfig(const GameConfig& newConfig);
    
    // Event system
    void registerEventCallback(const std::string& eventName, std::function<void()> callback);
    void triggerEvent(const std::string& eventName);
    
    // Victory conditions
    bool checkVictoryConditions();
    bool checkFederationConditions();
    bool checkDominationConditions();
    bool checkInfluenceConditions();
    bool checkShimarraConditions();
    
    // Dark Continent specific
    bool isDarkContinentSpawned() const;
    void spawnDarkContinent();
    int getDarkContinentYear() const;
    void handleDarkContinentFragmentation();
    
    // Federation mode
    void enterFederationMode();
    void handleFederationCard(const std::string& cardData);
    void exitFederationMode();
    
    // Save/Load
    bool saveGame(const std::string& saveName);
    bool loadGame(const std::string& saveName);
    bool autoSaveCheck();
    
    // Utility
    std::string getGameStateString() const;
    void logGameAction(const std::string& action, PlayerID player = PlayerID::UNITED_STATES);
    
    // Statistics and debugging
    struct GameStats {
        int totalTurns;
        int totalYears;
        std::map<PlayerID, int> territoriesControlled;
        std::map<PlayerID, int> totalInfluence;
        std::map<PlayerID, int> totalCurrency;
        std::map<PlayerID, int> cardsPlayed;
        std::map<PlayerID, int> unitsLost;
        std::map<PlayerID, int> unitsBuilt;
    };
    
    GameStats getGameStats() const;
    void resetStats();
    
private:
    void updateTimers();
    void handleTurnTimeout();
    void processPendingActions();
    void validateGameState();
    void cleanup();
    
    // Victory calculation helpers
    int calculateVictoryPoints(PlayerID player);
    bool hasPlayerDominance(PlayerID player);
    bool hasMaximumInfluence(PlayerID player);
    bool hasMaximumShimarra(PlayerID player);
    
    // Dark Continent dice mechanics
    int rollDarkContinentDice();
    void rollTimeDice();
};

// Global access macro
#define ENGINE GameEngine::getInstance()

#endif // GAMEENGINE_H