#include "Player.h"
#include "Card.h"
#include "Unit.h"
#include "Fortification.h"
#include "GameBoard.h"
#include "CardSystem.h"
#include <iostream>
#include <algorithm>
#include <sstream>
#include <iomanip>

// Base Player class implementation
Player::Player(PlayerID id, const std::string& name) 
    : playerId(id), playerName(name), influence(0), currency(0), shimarra(0), 
      nuclearProgramLevel(0), actionsPerTurn(1), actionsRemaining(1), isActivePlayer(false),
      hasNuclearCapability(false), canBuildSuperweapon(false), isInTruce(false), 
      truceTurnsRemaining(0) {
    
    // Initialize player-specific counters
    specialCounters["turns_played"] = 0;
    specialCounters["cards_drawn_this_turn"] = 0;
    specialCounters["units_built_this_turn"] = 0;
    
    // Initialize ability flags
    abilityFlags["can_draw_cards"] = true;
    abilityFlags["can_build_units"] = true;
    abilityFlags["can_play_cards"] = true;
    abilityFlags["can_attack"] = true;
    
    setupCardAccess();
}

void Player::initializeCardAccess() {
    // Base card access - overridden by derived classes
    cardAccess[CardType::DIVINE_WILL] = true;
}

bool Player::hasCardAccess(CardType type) const {
    auto it = cardAccess.find(type);
    return it != cardAccess.end() && it->second;
}

void Player::setCardAccess(CardType type, bool hasAccess) {
    cardAccess[type] = hasAccess;
}

void Player::addCardToHand(std::shared_ptr<Card> card) {
    if (card) {
        hand.push_back(card);
        updateStats();
    }
}

void Player::removeCardFromHand(std::shared_ptr<Card> card) {
    auto it = std::find(hand.begin(), hand.end(), card);
    if (it != hand.end()) {
        hand.erase(it);
        updateStats();
    }
}

void Player::addCardToPlayed(std::shared_ptr<Card> card) {
    if (card) {
        playedCards.push_back(card);
        stats.cardsPlayed++;
    }
}

bool Player::spendInfluence(int amount) {
    if (influence >= amount) {
        influence -= amount;
        return true;
    }
    return false;
}

bool Player::spendCurrency(int amount) {
    if (currency >= amount) {
        currency -= amount;
        return true;
    }
    return false;
}

bool Player::spendShimarra(int amount) {
    if (shimarra >= amount) {
        shimarra -= amount;
        return true;
    }
    return false;
}

void Player::startTurn() {
    isActivePlayer = true;
    resetActions();
    specialCounters["cards_drawn_this_turn"] = 0;
    specialCounters["units_built_this_turn"] = 0;
    specialCounters["turns_played"]++;
    
    onTurnStart();
    updateStats();
}

void Player::endTurn() {
    onTurnEnd();
    isActivePlayer = false;
    updateStats();
}

void Player::useAction() {
    if (actionsRemaining > 0) {
        actionsRemaining--;
    }
}

void Player::resetActions() {
    actionsRemaining = actionsPerTurn;
}

void Player::setNuclearCapability(bool capable) {
    hasNuclearCapability = capable;
    if (capable) {
        nuclearProgramLevel = 20; // Full nuclear program
    }
}

void Player::enterTruce(int duration) {
    isInTruce = true;
    truceTurnsRemaining = duration;
}

void Player::updateTruceStatus() {
    if (isInTruce && truceTurnsRemaining > 0) {
        truceTurnsRemaining--;
        if (truceTurnsRemaining <= 0) {
            isInTruce = false;
        }
    }
}

int Player::getSpecialCounter(const std::string& key) const {
    auto it = specialCounters.find(key);
    return (it != specialCounters.end()) ? it->second : 0;
}

void Player::modifySpecialCounter(const std::string& key, int delta) {
    specialCounters[key] += delta;
}

bool Player::getAbilityFlag(const std::string& key) const {
    auto it = abilityFlags.find(key);
    return (it != abilityFlags.end()) ? it->second : false;
}

bool Player::checkInfluenceVictory() const {
    return influence >= 1000; // Maximum influence threshold
}

bool Player::checkShimarraVictory() const {
    return shimarra >= 100; // Maximum Shimarra threshold
}

bool Player::checkTerritoryVictory() const {
    // Check for domination (80% of territories)
    int totalTerritories = ENGINE.getBoard().getTotalTerritoryCount();
    int playerTerritories = ENGINE.getBoard().getTerritoryCount(playerId);
    return playerTerritories >= (totalTerritories * 0.8);
}

bool Player::canLaunchNuke() const {
    return hasNuclearCapability && stats.nuclearArsenal > 0;
}

bool Player::launchNuke(int targetCityId) {
    if (!canLaunchNuke()) {
        return false;
    }
    
    // Spend nuke
    stats.nuclearArsenal--;
    
    // Devastate target city
    ENGINE.getBoard().devastateCity(targetCityId);
    
    logPlayerAction("Launched nuclear weapon at city ID " + std::to_string(targetCityId));
    return true;
}

bool Player::repairNuclearProgram() {
    if (currency >= 50) { // Cost to repair
        spendCurrency(50);
        nuclearProgramLevel = std::min(20, nuclearProgramLevel + 5);
        if (nuclearProgramLevel >= 20) {
            setNuclearCapability(true);
        }
        return true;
    }
    return false;
}

bool Player::sabotageNuclearProgram(PlayerID targetPlayer) {
    // This would be implemented with player manager interaction
    // For now, return true as a placeholder
    logPlayerAction("Attempted to sabotage nuclear program of player " + 
                   std::to_string(static_cast<int>(targetPlayer)));
    return true;
}

void Player::updateStats() {
    stats.territoriesControlled = ENGINE.getBoard().getTerritoryCount(playerId);
    stats.totalInfluence = influence;
    stats.totalCurrency = currency;
    stats.cardsInHand = static_cast<int>(hand.size());
    stats.shimarra = shimarra;
    stats.turnsPlayed = getSpecialCounter("turns_played");
}

void Player::resetStats() {
    stats = PlayerStats();
    specialCounters.clear();
    abilityFlags.clear();
}

std::string Player::serialize() const {
    std::ostringstream oss;
    oss << playerId << "|" << playerName << "|" << influence << "|" << currency << "|" 
        << shimarra << "|" << nuclearProgramLevel << "|" << hasNuclearCapability << "|"
        << canBuildSuperweapon << "|" << isInTruce << "|" << truceTurnsRemaining << "|"
        << actionsPerTurn << "|" << stats.nuclearArsenal;
    
    // Add special counters
    for (const auto& counter : specialCounters) {
        oss << "|" << counter.first << ":" << counter.second;
    }
    
    return oss.str();
}

bool Player::deserialize(const std::string& data) {
    std::istringstream iss(data);
    std::string token;
    
    std::vector<std::string> tokens;
    while (std::getline(iss, token, '|')) {
        tokens.push_back(token);
    }
    
    if (tokens.size() < 13) {
        return false;
    }
    
    try {
        playerId = static_cast<PlayerID>(std::stoi(tokens[0]));
        playerName = tokens[1];
        influence = std::stoi(tokens[2]);
        currency = std::stoi(tokens[3]);
        shimarra = std::stoi(tokens[4]);
        nuclearProgramLevel = std::stoi(tokens[5]);
        hasNuclearCapability = (tokens[6] == "1");
        canBuildSuperweapon = (tokens[7] == "1");
        isInTruce = (tokens[8] == "1");
        truceTurnsRemaining = std::stoi(tokens[9]);
        actionsPerTurn = std::stoi(tokens[10]);
        stats.nuclearArsenal = std::stoi(tokens[11]);
        
        // Parse special counters
        for (size_t i = 12; i < tokens.size(); i++) {
            size_t colonPos = tokens[i].find(':');
            if (colonPos != std::string::npos) {
                std::string key = tokens[i].substr(0, colonPos);
                int value = std::stoi(tokens[i].substr(colonPos + 1));
                specialCounters[key] = value;
            }
        }
        
        return true;
    } catch (const std::exception&) {
        return false;
    }
}

std::string Player::getPlayerDescription() const {
    std::ostringstream oss;
    oss << "Player: " << playerName << " (ID: " << static_cast<int>(playerId) << ")\n";
    oss << "Resources:\n";
    oss << "  Influence: " << influence << "\n";
    oss << "  Currency: " << currency << "\n";
    oss << "  Shimarra: " << shimarra << "\n";
    oss << "  Nuclear Arsenal: " << stats.nuclearArsenal << "\n";
    oss << "Stats:\n";
    oss << "  Territories: " << stats.territoriesControlled << "\n";
    oss << "  Cards in hand: " << stats.cardsInHand << "\n";
    oss << "  Units built: " << stats.unitsBuilt << "\n";
    oss << "  Cards played: " << stats.cardsPlayed << "\n";
    
    return oss.str();
}

void Player::logPlayerAction(const std::string& action) const {
    std::cout << "[" << playerName << "] " << action << std::endl;
}

// UnitedStatesPlayer implementation
UnitedStatesPlayer::UnitedStatesPlayer() : Player(PlayerID::UNITED_STATES, "United States") {
    technologySlots = 5;
    setActionsPerTurn(2); // US gets 2 actions per turn
}

void UnitedStatesPlayer::initializeStartingResources() {
    setInfluence(50);
    setCurrency(100);
    setNuclearCapability(false); // Nukes disabled at start
    nuclearProgramLevel = 0;
    stats.nuclearArsenal = 0;
    
    // Technologies start empty
    technologies["Gauss Rifle"] = false;
    technologies["Titanium Weave"] = false;
    technologies["Mobile Barricade"] = false;
    technologies["Advanced Sonar"] = false;
    technologies["Hypersonic Engine"] = false;
}

void UnitedStatesPlayer::initializeStartingCards() {
    // Deal starting America cards
    // This would interact with the CardSystem
    for (int i = 0; i < 4; i++) {
        // Add America cards to hand
    }
}

void UnitedStatesPlayer::initializeStartingTerritories() {
    // Starting territories assigned by GameBoard
}

bool UnitedStatesPlayer::canPerformAction(ActionType action) const {
    switch (action) {
        case ActionType::ATTACK:
            return getAbilityFlag("can_attack") && !isInTruceState();
        case ActionType::PLAY_CARD:
            return getAbilityFlag("can_play_cards") && hasActionsRemaining();
        case ActionType::MOVE:
            return hasActionsRemaining();
        case ActionType::NUKE:
            return canLaunchNuke() && hasActionsRemaining();
        case ActionType::BUILD_UNIT:
            return getAbilityFlag("can_build_units") && hasActionsRemaining();
        case ActionType::BUILD_FORTIFICATION:
            return hasActionsRemaining();
        case ActionType::DRAW_CARD:
            return getAbilityFlag("can_draw_cards") && hasActionsRemaining();
        case ActionType::FORM_TRUCE:
            return !isInTruceState() && hasActionsRemaining();
        default:
            return false;
    }
}

void UnitedStatesPlayer::onTurnStart() {
    Player::onTurnStart();
    // US-specific turn start logic
}

void UnitedStatesPlayer::onTurnEnd() {
    Player::onTurnEnd();
    updateStats();
}

void UnitedStatesPlayer::onTerritoryGained(int territoryId) {
    logPlayerAction("Gained territory ID " + std::to_string(territoryId));
}

void UnitedStatesPlayer::onTerritoryLost(int territoryId) {
    logPlayerAction("Lost territory ID " + std::to_string(territoryId));
}

void UnitedStatesPlayer::onCardPlayed(std::shared_ptr<Card> card) {
    addCardToPlayed(card);
    removeCardFromHand(card);
    logPlayerAction("Played card: " + card->getName());
}

void UnitedStatesPlayer::onUnitBuilt(std::shared_ptr<Unit> unit) {
    stats.unitsBuilt++;
    specialCounters["units_built_this_turn"]++;
    logPlayerAction("Built unit: " + unit->getType());
}

void UnitedStatesPlayer::onUnitLost(std::shared_ptr<Unit> unit) {
    stats.unitsLost++;
    logPlayerAction("Lost unit: " + unit->getType());
}

bool UnitedStatesPlayer::hasTechnology(const std::string& techName) const {
    auto it = technologies.find(techName);
    return it != technologies.end() && it->second;
}

void UnitedStatesPlayer::acquireTechnology(const std::string& techName) {
    technologies[techName] = true;
    logPlayerAction("Acquired technology: " + techName);
}

int UnitedStatesPlayer::getTechnologyLevel(const std::string& techName) const {
    return hasTechnology(techName) ? 1 : 0;
}

bool UnitedStatesPlayer::hasAchievedVictory() const {
    return checkInfluenceVictory() || checkShimarraVictory() || checkTerritoryVictory();
}

int UnitedStatesPlayer::calculateVictoryPoints() const {
    return (getTotalInfluence() * getTotalCurrency()) / std::max(1, getHandSize());
}

std::string UnitedStatesPlayer::getPlayerDescription() const {
    std::string desc = Player::getPlayerDescription();
    desc += "\nUS-Specific:\n";
    desc += "  Technology Slots: " + std::to_string(technologySlots) + "\n";
    desc += "  Technologies: ";
    for (const auto& tech : technologies) {
        if (tech.second) {
            desc += tech.first + " ";
        }
    }
    desc += "\n";
    return desc;
}

void UnitedStatesPlayer::setupCardAccess() {
    Player::setupCardAccess();
    cardAccess[CardType::AMERICA] = true;
}

int UnitedStatesPlayer::calculateBaseInfluence() const {
    return 25 + (stats.territoriesControlled * 10);
}

int UnitedStatesPlayer::calculateBaseCurrency() const {
    return 30 + (stats.territoriesControlled * 15);
}

// Similar implementations for other player classes would follow...
// Due to length constraints, I'll show the key differences

RussiaPlayer::RussiaPlayer() : Player(PlayerID::RUSSIA, "Russia") {
    superweaponUpgrades = 0;
    hasNauka = false;
    setActionsPerTurn(2);
}

void RussiaPlayer::setupCardAccess() {
    Player::setupCardAccess();
    cardAccess[CardType::COMMUNISM] = true;
}

bool RussiaPlayer::canBuildSuperweapon() const {
    return superweaponUpgrades >= 5 && hasNauka;
}

EuropeanUnionPlayer::EuropeanUnionPlayer() : Player(PlayerID::EUROPEAN_UNION, "European Union") {
    politicalInfluence = 30;
    setActionsPerTurn(2);
}

void EuropeanUnionPlayer::setupCardAccess() {
    Player::setupCardAccess();
    cardAccess[CardType::EU_INFLUENCE] = true;
    cardAccess[CardType::TRIVIA] = false; // EU doesn't use trivia cards
}

SouthernAlliancePlayer::SouthernAlliancePlayer() : Player(PlayerID::SOUTHERN_ALLIANCE, "Southern Hemisphere Alliance") {
    climateAdaptationLevel = 1;
    setActionsPerTurn(2);
}

void SouthernAlliancePlayer::setupCardAccess() {
    Player::setupCardAccess();
    cardAccess[CardType::ALLIANCE] = true;
}

DarkContinentPlayer::DarkContinentPlayer() : Player(PlayerID::DARK_CONTINENT, "The Dark Continent") {
    maxShimarra = 150; // Higher maximum for Devils
    isSpawned = false;
    spawnYear = 0;
    hasFragmented = false;
    setActionsPerTurn(3); // Devils get more actions
}

void DarkContinentPlayer::setupCardAccess() {
    Player::setupCardAccess();
    cardAccess[CardType::MISCHIEF] = true;
    cardAccess[CardType::DIVINE_WILL] = true;
    cardAccess[CardType::FEDERATION] = true;
}

// Utility functions
std::unique_ptr<Player> createPlayer(PlayerID playerId, const std::string& playerName) {
    switch (playerId) {
        case PlayerID::UNITED_STATES:
            return std::make_unique<UnitedStatesPlayer>();
        case PlayerID::RUSSIA:
            return std::make_unique<RussiaPlayer>();
        case PlayerID::EUROPEAN_UNION:
            return std::make_unique<EuropeanUnionPlayer>();
        case PlayerID::SOUTHERN_ALLIANCE:
            return std::make_unique<SouthernAlliancePlayer>();
        case PlayerID::DARK_CONTINENT:
            return std::make_unique<DarkContinentPlayer>();
        default:
            return nullptr;
    }
}

std::string playerIDToString(PlayerID playerId) {
    switch (playerId) {
        case PlayerID::UNITED_STATES: return "United States";
        case PlayerID::RUSSIA: return "Russia";
        case PlayerID::EUROPEAN_UNION: return "European Union";
        case PlayerID::SOUTHERN_ALLIANCE: return "Southern Alliance";
        case PlayerID::DARK_CONTINENT: return "Dark Continent";
        default: return "Unknown";
    }
}

PlayerID stringToPlayerID(const std::string& playerStr) {
    if (playerStr == "United States") return PlayerID::UNITED_STATES;
    if (playerStr == "Russia") return PlayerID::RUSSIA;
    if (playerStr == "European Union") return PlayerID::EUROPEAN_UNION;
    if (playerStr == "Southern Alliance") return PlayerID::SOUTHERN_ALLIANCE;
    if (playerStr == "Dark Continent") return PlayerID::DARK_CONTINENT;
    return PlayerID::UNITED_STATES; // Default
}