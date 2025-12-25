#include "GameEngine.h"
#include <iostream>
#include <random>
#include <sstream>
#include <fstream>
#include <iomanip>

class GameSimulator {
private:
    std::mt19937 rng;
    std::uniform_int_distribution<int> dice100;
    std::uniform_int_distribution<int> dice20;
    std::uniform_int_distribution<int> dice6;
    
    struct SimulationStats {
        int totalTurns;
        int totalYears;
        std::map<PlayerID, int> territoriesControlled;
        std::map<PlayerID, int> totalInfluence;
        std::map<PlayerID, int> totalCurrency;
        std::map<PlayerID, int> cardsPlayed;
        std::map<PlayerID, int> unitsBuilt;
        std::map<PlayerID, int> battlesWon;
        std::string winner;
        std::string victoryCondition;
        
        SimulationStats() : totalTurns(0), totalYears(0) {
            // Initialize all players
            territoriesControlled[PlayerID::UNITED_STATES] = 0;
            territoriesControlled[PlayerID::RUSSIA] = 0;
            territoriesControlled[PlayerID::EUROPEAN_UNION] = 0;
            territoriesControlled[PlayerID::SOUTHERN_ALLIANCE] = 0;
            territoriesControlled[PlayerID::DARK_CONTINENT] = 0;
            
            totalInfluence[PlayerID::UNITED_STATES] = 0;
            totalInfluence[PlayerID::RUSSIA] = 0;
            totalInfluence[PlayerID::EUROPEAN_UNION] = 0;
            totalInfluence[PlayerID::SOUTHERN_ALLIANCE] = 0;
            totalInfluence[PlayerID::DARK_CONTINENT] = 0;
            
            totalCurrency[PlayerID::UNITED_STATES] = 0;
            totalCurrency[PlayerID::RUSSIA] = 0;
            totalCurrency[PlayerID::EUROPEAN_UNION] = 0;
            totalCurrency[PlayerID::SOUTHERN_ALLIANCE] = 0;
            totalCurrency[PlayerID::DARK_CONTINENT] = 0;
        }
    };
    
    SimulationStats stats;

public:
    GameSimulator() : rng(std::random_device{}()), dice100(1, 100), dice20(1, 20), dice6(1, 6) {}
    
    void runFullSimulation() {
        std::cout << "=== DARK CONTINENT 5-PLAYER GAME SIMULATION ===" << std::endl;
        std::cout << "Running comprehensive game simulation..." << std::endl;
        
        // Initialize game
        if (!initializeSimulation()) {
            std::cerr << "Failed to initialize simulation!" << std::endl;
            return;
        }
        
        // Run simulation for 40 game years or until victory
        runGameLoop();
        
        // Generate report
        generateSimulationReport();
    }
    
private:
    bool initializeSimulation() {
        std::cout << "Initializing 5-player game simulation..." << std::endl;
        
        // Set up game configuration
        GameConfig config;
        config.maxPlayers = 5;
        config.asyncMode = false;
        config.turnTimeLimit = 30; // Fast simulation
        config.autoSave = false;
        
        // Initialize game engine
        GameEngine::initialize();
        if (!GameEngine::getInstance().initialize(config)) {
            return false;
        }
        
        // Setup initial game state
        setupInitialGameState();
        
        std::cout << "Simulation initialized successfully!" << std::endl;
        return true;
    }
    
    void setupInitialGameState() {
        std::cout << "Setting up initial game state..." << std::endl;
        
        // Initialize player starting positions
        auto& playerManager = GameEngine::getInstance().getPlayerManager();
        auto& gameBoard = GameEngine::getInstance().getBoard();
        
        // United States starts with North America territories
        std::vector<int> us_territories = {1, 2, 3, 4, 5};
        for (int territoryId : us_territories) {
            gameBoard.setTerritoryController(territoryId, PlayerID::UNITED_STATES);
            stats.territoriesControlled[PlayerID::UNITED_STATES]++;
        }
        
        // Russia starts with Eastern Europe and Russia
        std::vector<int> russia_territories = {16, 18, 30};
        for (int territoryId : russia_territories) {
            gameBoard.setTerritoryController(territoryId, PlayerID::RUSSIA);
            stats.territoriesControlled[PlayerID::RUSSIA]++;
        }
        
        // European Union starts with Western Europe
        std::vector<int> eu_territories = {11, 12, 13, 14, 15, 17};
        for (int territoryId : eu_territories) {
            gameBoard.setTerritoryController(territoryId, PlayerID::EUROPEAN_UNION);
            stats.territoriesControlled[PlayerID::EUROPEAN_UNION]++;
        }
        
        // Southern Alliance starts with South America, Africa, Oceania
        std::vector<int> southern_territories = {6, 7, 8, 9, 10, 19, 20, 21, 22, 23, 24, 36, 37, 38, 39, 40};
        for (int territoryId : southern_territories) {
            gameBoard.setTerritoryController(territoryId, PlayerID::SOUTHERN_ALLIANCE);
            stats.territoriesControlled[PlayerID::SOUTHERN_ALLIANCE]++;
        }
        
        // Dark Continent starts empty (will spawn later)
        
        // Set initial resources
        setupInitialResources();
        
        std::cout << "Initial setup complete!" << std::endl;
        std::cout << "US territories: " << stats.territoriesControlled[PlayerID::UNITED_STATES] << std::endl;
        std::cout << "Russia territories: " << stats.territoriesControlled[PlayerID::RUSSIA] << std::endl;
        std::cout << "EU territories: " << stats.territoriesControlled[PlayerID::EUROPEAN_UNION] << std::endl;
        std::cout << "Southern Alliance territories: " << stats.territoriesControlled[PlayerID::SOUTHERN_ALLIANCE] << std::endl;
    }
    
    void setupInitialResources() {
        std::cout << "Setting up initial player resources..." << std::endl;
        
        auto& playerManager = GameEngine::getInstance().getPlayerManager();
        
        // Set initial resources based on territories controlled
        for (int player = 1; player <= 4; player++) { // Skip Dark Continent initially
            PlayerID playerId = static_cast<PlayerID>(player);
            auto& playerObj = playerManager.getPlayer(playerId);
            
            // Base resources
            playerObj.setInfluence(50 + stats.territoriesControlled[playerId] * 10);
            playerObj.setCurrency(100 + stats.territoriesControlled[playerId] * 20);
            
            stats.totalInfluence[playerId] = playerObj.getInfluence();
            stats.totalCurrency[playerId] = playerObj.getCurrency();
        }
    }
    
    void runGameLoop() {
        std::cout << "Starting game simulation loop..." << std::endl;
        
        // Start the game
        GameEngine::getInstance().run();
        
        // Simulate up to 40 years or until victory
        while (GameEngine::getInstance().getCurrentYear() <= 42) {
            // Simulate one complete round of turns
            simulateTurnRound();
            
            // Check victory conditions
            if (checkVictoryConditions()) {
                break;
            }
            
            // Update statistics
            updateStatistics();
            
            // Progress time every 4 rounds
            if (GameEngine::getInstance().shouldIncrementYear()) {
                GameEngine::getInstance().incrementYear();
                stats.totalYears = GameEngine::getInstance().getCurrentYear();
                
                std::cout << "Year " << stats.totalYears << " completed." << std::endl;
                
                // Dark Continent spawn check
                checkDarkContinentSpawn();
            }
            
            // Prevent infinite loops
            if (stats.totalTurns > 1000) {
                std::cout << "Maximum turns reached, ending simulation." << std::endl;
                stats.winner = "Time Limit";
                stats.victoryCondition = "Maximum turns exceeded";
                break;
            }
        }
    }
    
    void simulateTurnRound() {
        // Simulate each player's turn in order
        std::vector<PlayerID> turnOrder = {
            PlayerID::UNITED_STATES,
            PlayerID::RUSSIA,
            PlayerID::EUROPEAN_UNION,
            PlayerID::SOUTHERN_ALLIANCE
        };
        
        // Add Dark Continent if spawned
        if (GameEngine::getInstance().isDarkContinentSpawned()) {
            turnOrder.push_back(PlayerID::DARK_CONTINENT);
        }
        
        for (PlayerID player : turnOrder) {
            simulatePlayerTurn(player);
            stats.totalTurns++;
        }
    }
    
    void simulatePlayerTurn(PlayerID player) {
        auto& playerManager = GameEngine::getInstance().getPlayerManager();
        auto& playerObj = playerManager.getPlayer(player);
        
        // Start player's turn
        playerObj.startTurn();
        
        // Simulate player actions based on their strategy
        int actionsTaken = 0;
        int maxActions = playerObj.getActionsPerTurn();
        
        while (actionsTaken < maxActions && playerObj.getActionsRemaining() > 0) {
            ActionType action = decidePlayerAction(player);
            executePlayerAction(player, action);
            actionsTaken++;
        }
        
        // End player's turn
        playerObj.endTurn();
    }
    
    ActionType decidePlayerAction(PlayerID player) {
        // Different strategies for different players
        int strategyRoll = dice100(rng);
        
        switch (player) {
            case PlayerID::UNITED_STATES:
                if (strategyRoll < 40) return ActionType::PLAY_CARD;
                if (strategyRoll < 70) return ActionType::BUILD_UNIT;
                if (strategyRoll < 85) return ActionType::ATTACK;
                return ActionType::BUILD_FORTIFICATION;
                
            case PlayerID::RUSSIA:
                if (strategyRoll < 35) return ActionType::BUILD_UNIT;
                if (strategyRoll < 65) return ActionType::PLAY_CARD;
                if (strategyRoll < 80) return ActionType::ATTACK;
                return ActionType::BUILD_FORTIFICATION;
                
            case PlayerID::EUROPEAN_UNION:
                if (strategyRoll < 50) return ActionType::PLAY_CARD; // Focus on influence
                if (strategyRoll < 75) return ActionType::BUILD_FORTIFICATION;
                if (strategyRoll < 90) return ActionType::DRAW_CARD;
                return ActionType::BUILD_UNIT;
                
            case PlayerID::SOUTHERN_ALLIANCE:
                if (strategyRoll < 45) return ActionType::BUILD_UNIT;
                if (strategyRoll < 70) return ActionType::PLAY_CARD;
                if (strategyRoll < 85) return ActionType::MOVE;
                return ActionType::BUILD_FORTIFICATION;
                
            case PlayerID::DARK_CONTINENT:
                if (strategyRoll < 60) return ActionType::PLAY_CARD; // Mischief cards
                if (strategyRoll < 85) return ActionType::ATTACK;
                return ActionType::NUKE;
                
            default:
                return ActionType::PLAY_CARD;
        }
    }
    
    void executePlayerAction(PlayerID player, ActionType action) {
        auto& playerManager = GameEngine::getInstance().getPlayerManager();
        auto& playerObj = playerManager.getPlayer(player);
        auto& gameBoard = GameEngine::getInstance().getBoard();
        
        switch (action) {
            case ActionType::PLAY_CARD:
                simulateCardPlay(player);
                stats.cardsPlayed[player]++;
                break;
                
            case ActionType::BUILD_UNIT:
                simulateUnitBuild(player);
                stats.unitsBuilt[player]++;
                break;
                
            case ActionType::BUILD_FORTIFICATION:
                simulateFortificationBuild(player);
                break;
                
            case ActionType::ATTACK:
                simulateAttack(player);
                break;
                
            case ActionType::MOVE:
                simulateMovement(player);
                break;
                
            case ActionType::DRAW_CARD:
                simulateCardDraw(player);
                break;
                
            case ActionType::NUKE:
                simulateNuke(player);
                break;
                
            default:
                break;
        }
        
        playerObj.useAction();
    }
    
    void simulateCardPlay(PlayerID player) {
        auto& cardSystem = GameEngine::getInstance().getCardSystem();
        auto& playerManager = GameEngine::getInstance().getPlayerManager();
        auto& playerObj = playerManager.getPlayer(player);
        
        // Check if player has cards to play
        if (playerObj.getHandSize() > 0) {
            // Simulate playing a random card from hand
            int cardIndex = dice6(rng) % playerObj.getHandSize();
            auto card = playerObj.getHand()[cardIndex];
            
            // Check if player can afford the card
            if (playerObj.getInfluence() >= card->getCost().influenceCost &&
                playerObj.getCurrency() >= card->getCost().currencyCost) {
                
                // Play the card
                std::map<std::string, std::string> parameters;
                if (card->play(player, parameters)) {
                    playerObj.removeCardFromHand(card);
                    playerObj.addCardToPlayed(card);
                    
                    // Apply costs
                    playerObj.spendInfluence(card->getCost().influenceCost);
                    playerObj.spendCurrency(card->getCost().currencyCost);
                }
            }
        } else {
            // Try to draw a card
            simulateCardDraw(player);
        }
    }
    
    void simulateCardDraw(PlayerID player) {
        auto& cardSystem = GameEngine::getInstance().getCardSystem();
        auto& playerManager = GameEngine::getInstance().getPlayerManager();
        auto& playerObj = playerManager.getPlayer(player);
        
        // Determine which deck to draw from based on player
        CardType deckType = getPlayerDeckType(player);
        auto card = cardSystem.drawCard(deckType);
        
        if (card) {
            playerObj.addCardToHand(card);
        }
    }
    
    void simulateUnitBuild(PlayerID player) {
        auto& playerManager = GameEngine::getInstance().getPlayerManager();
        auto& playerObj = playerManager.getPlayer(player);
        auto& gameBoard = GameEngine::getInstance().getBoard();
        
        // Find a controlled territory to build in
        auto controlledTerritories = gameBoard.getControlledTerritories(player);
        if (!controlledTerritories.empty()) {
            int territoryId = controlledTerritories[dice6(rng) % controlledTerritories.size()];
            
            // Build basic unit (cost: 10 currency)
            if (playerObj.getCurrency() >= 10) {
                playerObj.spendCurrency(10);
                gameBoard.addUnit(territoryId, player, "basic_unit");
            }
        }
    }
    
    void simulateFortificationBuild(PlayerID player) {
        auto& playerManager = GameEngine::getInstance().getPlayerManager();
        auto& playerObj = playerManager.getPlayer(player);
        auto& gameBoard = GameEngine::getInstance().getBoard();
        
        // Find a controlled territory to build in
        auto controlledTerritories = gameBoard.getControlledTerritories(player);
        if (!controlledTerritories.empty()) {
            int territoryId = controlledTerritories[dice6(rng) % controlledTerritories.size()];
            
            // Build basic fortification (cost: 15 currency)
            if (playerObj.getCurrency() >= 15) {
                playerObj.spendCurrency(15);
                gameBoard.addFortification(territoryId, player, "basic_fort");
            }
        }
    }
    
    void simulateAttack(PlayerID player) {
        auto& gameBoard = GameEngine::getInstance().getBoard();
        auto& combatSystem = GameEngine::getInstance().getCombatSystem();
        
        // Find a controlled territory with units
        auto controlledTerritories = gameBoard.getControlledTerritories(player);
        if (controlledTerritories.empty()) return;
        
        int attackerTerritory = controlledTerritories[dice6(rng) % controlledTerritories.size()];
        auto adjacentTerritories = gameBoard.getAdjacentTerritories(attackerTerritory);
        
        // Find an enemy adjacent territory
        for (int adjacentId : adjacentTerritories) {
            PlayerID defender = gameBoard.getTerritoryController(adjacentId);
            if (defender != player && defender != PlayerID::DARK_CONTINENT || player == PlayerID::DARK_CONTINENT) {
                // Simulate combat
                int attackRoll = dice20(rng);
                int defenseRoll = dice20(rng);
                
                if (attackRoll > defenseRoll) {
                    // Attacker wins
                    gameBoard.setTerritoryController(adjacentId, player);
                    stats.battlesWon[player]++;
                }
                break;
            }
        }
    }
    
    void simulateMovement(PlayerID player) {
        auto& gameBoard = GameEngine::getInstance().getBoard();
        
        // Simple movement simulation
        auto controlledTerritories = gameBoard.getControlledTerritories(player);
        if (controlledTerritories.empty()) return;
        
        int fromTerritory = controlledTerritories[dice6(rng) % controlledTerritories.size()];
        auto adjacentTerritories = gameBoard.getAdjacentTerritories(fromTerritory);
        
        if (!adjacentTerritories.empty()) {
            int toTerritory = adjacentTerritories[dice6(rng) % adjacentTerritories.size()];
            // Move units (simplified)
            gameBoard.moveUnits(fromTerritory, toTerritory, 1);
        }
    }
    
    void simulateNuke(PlayerID player) {
        auto& playerManager = GameEngine::getInstance().getPlayerManager();
        auto& playerObj = playerManager.getPlayer(player);
        
        // Check if player has nuclear capability
        if (playerObj.getNuclearArsenal() > 0 && playerObj.getNuclearProgramLevel() >= 20) {
            // Simulate nuclear strike (rare)
            int nukeRoll = dice100(rng);
            if (nukeRoll < 5) { // 5% chance
                playerObj.modifySpecialCounter("nukes_used", 1);
                std::cout << "Player " << static_cast<int>(player) << " used a nuclear weapon!" << std::endl;
            }
        }
    }
    
    CardType getPlayerDeckType(PlayerID player) {
        switch (player) {
            case PlayerID::UNITED_STATES: return CardType::AMERICA;
            case PlayerID::RUSSIA: return CardType::COMMUNISM;
            case PlayerID::EUROPEAN_UNION: return CardType::EU_INFLUENCE;
            case PlayerID::SOUTHERN_ALLIANCE: return CardType::ALLIANCE;
            case PlayerID::DARK_CONTINENT: return CardType::MISCHIEF;
            default: return CardType::DIVINE_WILL;
        }
    }
    
    void checkDarkContinentSpawn() {
        auto& gameEngine = GameEngine::getInstance();
        
        if (!gameEngine.isDarkContinentSpawned()) {
            // Roll Dark Continent dice (2d20)
            int dice1 = dice20(rng);
            int dice2 = dice20(rng);
            int spawnYear = dice1 + dice2;
            
            if (spawnYear <= gameEngine.getCurrentYear()) {
                // Spawn Dark Continent
                gameEngine.spawnDarkContinent();
                std::cout << "DARK CONTINENT SPAWNED in year " << gameEngine.getCurrentYear() << "!" << std::endl;
                
                // Place fragments in random cities
                auto& gameBoard = gameEngine.getBoard();
                auto cities = gameBoard.getAllCities();
                
                for (int i = 0; i < 10 && i < cities.size(); i++) {
                    int cityIndex = dice20(rng) % cities.size();
                    gameBoard.spawnDarkFragment(cities[cityIndex].id, gameEngine.getCurrentYear());
                }
            }
        }
    }
    
    bool checkVictoryConditions() {
        auto& playerManager = GameEngine::getInstance().getPlayerManager();
        auto& gameEngine = GameEngine::getInstance();
        
        // Check for domination victory
        for (int player = 1; player <= 5; player++) {
            PlayerID playerId = static_cast<PlayerID>(player);
            auto& playerObj = playerManager.getPlayer(playerId);
            
            auto controlledTerritories = gameEngine.getBoard().getControlledTerritories(playerId);
            if (controlledTerritories.size() >= 35) { // Control majority of map
                stats.winner = playerIDToString(playerId);
                stats.victoryCondition = "Domination";
                return true;
            }
            
            // Check influence victory
            if (playerObj.getInfluence() >= 1000) {
                stats.winner = playerIDToString(playerId);
                stats.victoryCondition = "Influence";
                return true;
            }
            
            // Check Shimarra victory
            if (playerObj.getShimarra() >= 100) {
                stats.winner = playerIDToString(playerId);
                stats.victoryCondition = "Shimarra";
                return true;
            }
        }
        
        // Check time limit victory
        if (gameEngine.getCurrentYear() >= 42) {
            stats.winner = calculateTimeVictoryWinner();
            stats.victoryCondition = "Time Limit";
            return true;
        }
        
        return false;
    }
    
    std::string calculateTimeVictoryWinner() {
        // Calculate scores based on territories * influence / cards
        std::map<PlayerID, double> scores;
        auto& playerManager = GameEngine::getInstance().getPlayerManager();
        
        for (int player = 1; player <= 5; player++) {
            PlayerID playerId = static_cast<PlayerID>(player);
            auto& playerObj = playerManager.getPlayer(playerId);
            
            double territories = stats.territoriesControlled[playerId];
            double influence = playerObj.getInfluence();
            double currency = playerObj.getCurrency();
            int cards = playerObj.getHandSize();
            
            if (cards > 0) {
                scores[playerId] = (territories * influence * currency) / cards;
            } else {
                scores[playerId] = territories * influence * currency;
            }
        }
        
        // Find player with highest score
        PlayerID winner = PlayerID::UNITED_STATES;
        double maxScore = 0;
        
        for (const auto& pair : scores) {
            if (pair.second > maxScore) {
                maxScore = pair.second;
                winner = pair.first;
            }
        }
        
        return playerIDToString(winner);
    }
    
    void updateStatistics() {
        auto& playerManager = GameEngine::getInstance().getPlayerManager();
        auto& gameBoard = GameEngine::getInstance().getBoard();
        
        for (int player = 1; player <= 5; player++) {
            PlayerID playerId = static_cast<PlayerID>(player);
            auto& playerObj = playerManager.getPlayer(playerId);
            
            // Update territory count
            auto controlledTerritories = gameBoard.getControlledTerritories(playerId);
            stats.territoriesControlled[playerId] = static_cast<int>(controlledTerritories.size());
            
            // Update resources
            stats.totalInfluence[playerId] = playerObj.getInfluence();
            stats.totalCurrency[playerId] = playerObj.getCurrency();
        }
    }
    
    std::string playerIDToString(PlayerID player) {
        switch (player) {
            case PlayerID::UNITED_STATES: return "United States";
            case PlayerID::RUSSIA: return "Russia";
            case PlayerID::EUROPEAN_UNION: return "European Union";
            case PlayerID::SOUTHERN_ALLIANCE: return "Southern Alliance";
            case PlayerID::DARK_CONTINENT: return "Dark Continent";
            default: return "Unknown";
        }
    }
    
    void generateSimulationReport() {
        std::cout << "\n=== SIMULATION COMPLETE ===" << std::endl;
        std::cout << "Total Turns: " << stats.totalTurns << std::endl;
        std::cout << "Total Years: " << stats.totalYears << std::endl;
        std::cout << "Winner: " << stats.winner << std::endl;
        std::cout << "Victory Condition: " << stats.victoryCondition << std::endl;
        
        std::cout << "\n=== FINAL STATISTICS ===" << std::endl;
        std::cout << std::left << std::setw(18) << "Player" 
                  << std::setw(12) << "Territories" 
                  << std::setw(10) << "Influence" 
                  << std::setw(10) << "Currency"
                  << std::setw(8) << "Cards"
                  << std::setw(8) << "Units"
                  << std::setw(10) << "Battles Won" << std::endl;
        std::cout << std::string(84, '-') << std::endl;
        
        for (int player = 1; player <= 5; player++) {
            PlayerID playerId = static_cast<PlayerID>(player);
            std::cout << std::left << std::setw(18) << playerIDToString(playerId)
                      << std::setw(12) << stats.territoriesControlled[playerId]
                      << std::setw(10) << stats.totalInfluence[playerId]
                      << std::setw(10) << stats.totalCurrency[playerId]
                      << std::setw(8) << stats.cardsPlayed[playerId]
                      << std::setw(8) << stats.unitsBuilt[playerId]
                      << std::setw(10) << stats.battlesWon[playerId] << std::endl;
        }
        
        // Save detailed report to file
        saveDetailedReport();
        
        // Analyze game balance
        analyzeGameBalance();
    }
    
    void saveDetailedReport() {
        std::ofstream report("simulation_report.txt");
        if (report.is_open()) {
            report << "Dark Continent 5-Player Game Simulation Report\n";
            report << "==============================================\n\n";
            
            report << "Game Summary:\n";
            report << "Total Turns: " << stats.totalTurns << "\n";
            report << "Total Years: " << stats.totalYears << "\n";
            report << "Winner: " << stats.winner << "\n";
            report << "Victory Condition: " << stats.victoryCondition << "\n\n";
            
            report << "Final Player Statistics:\n";
            for (int player = 1; player <= 5; player++) {
                PlayerID playerId = static_cast<PlayerID>(player);
                report << playerIDToString(playerId) << ":\n";
                report << "  Territories: " << stats.territoriesControlled[playerId] << "\n";
                report << "  Influence: " << stats.totalInfluence[playerId] << "\n";
                report << "  Currency: " << stats.totalCurrency[playerId] << "\n";
                report << "  Cards Played: " << stats.cardsPlayed[playerId] << "\n";
                report << "  Units Built: " << stats.unitsBuilt[playerId] << "\n";
                report << "  Battles Won: " << stats.battlesWon[playerId] << "\n\n";
            }
            
            report.close();
            std::cout << "\nDetailed report saved to simulation_report.txt" << std::endl;
        }
    }
    
    void analyzeGameBalance() {
        std::cout << "\n=== GAME BALANCE ANALYSIS ===" << std::endl;
        
        // Calculate average territories per player
        double totalTerritories = 0;
        int activePlayers = 0;
        for (int player = 1; player <= 5; player++) {
            PlayerID playerId = static_cast<PlayerID>(player);
            if (stats.territoriesControlled[playerId] > 0) {
                totalTerritories += stats.territoriesControlled[playerId];
                activePlayers++;
            }
        }
        
        double avgTerritories = totalTerritories / activePlayers;
        std::cout << "Average territories per active player: " << avgTerritories << std::endl;
        
        // Check for balance issues
        for (int player = 1; player <= 5; player++) {
            PlayerID playerId = static_cast<PlayerID>(player);
            double territories = stats.territoriesControlled[playerId];
            
            if (territories > 0) {
                double ratio = territories / avgTerritories;
                if (ratio > 1.5) {
                    std::cout << "WARNING: " << playerIDToString(playerId) 
                              << " appears overpowered (" << ratio << "x average)" << std::endl;
                } else if (ratio < 0.5) {
                    std::cout << "WARNING: " << playerIDToString(playerId) 
                              << " appears underpowered (" << ratio << "x average)" << std::endl;
                }
            }
        }
        
        std::cout << "\n=== RECOMMENDATIONS ===" << std::endl;
        std::cout << "1. Consider adjusting starting resources for balance" << std::endl;
        std::cout << "2. Review card distributions for each faction" << std::endl;
        std::cout << "3. Consider territory value adjustments" << std::endl;
        std::cout << "4. Test different strategy AI patterns" << std::endl;
        std::cout << "5. Consider additional balance tweaks based on gameplay" << std::endl;
    }
};

// Main simulation function
void runGameSimulation() {
    GameSimulator simulator;
    simulator.runFullSimulation();
}