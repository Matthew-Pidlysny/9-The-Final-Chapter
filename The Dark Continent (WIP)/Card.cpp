#include "Card.h"
#include "Player.h"
#include "GameBoard.h"
#include <iostream>
#include <algorithm>
#include <random>
#include <sstream>
#include <iomanip>

// Base Card class implementation
Card::Card(int id, const std::string& name, CardType type, const std::string& exactText)
    : id(id), name(name), type(type), exactText(exactText), rarity(CardRarity::COMMON),
      isUnique(false), isLimited(false), copiesInDeck(1), isInPlay(false), 
      isExhausted(false), turnPlayed(0), playedBy(PlayerID::UNITED_STATES) {
}

void Card::addEffect(const CardEffectData& effect) {
    effects.push_back(effect);
}

void Card::clearEffects() {
    effects.clear();
}

void Card::setInPlay(bool inPlay) {
    isInPlay = inPlay;
}

void Card::setExhausted(bool exhausted) {
    isExhausted = exhausted;
}

void Card::setTurnPlayed(int turn) {
    turnPlayed = turn;
}

void Card::setPlayedBy(PlayerID player) {
    playedBy = player;
}

void Card::setCustomData(const std::string& key, const std::string& value) {
    customData[key] = value;
}

std::string Card::getCustomData(const std::string& key) const {
    auto it = customData.find(key);
    return (it != customData.end()) ? it->second : "";
}

bool Card::canBePlayedBy(PlayerID player) const {
    // Check if player has access to this card type
    // This would require access to Player class
    return true; // Simplified for now
}

bool Card::canAfford(PlayerID player) const {
    // Check if player can afford the card costs
    // This would require access to Player class
    return true; // Simplified for now
}

bool Card::hasValidTargets(PlayerID player) const {
    // Check if there are valid targets for this card
    // Implementation depends on card effects
    return true; // Simplified for now
}

bool Card::play(PlayerID player, const std::map<std::string, std::string>& parameters) {
    if (!canBePlayedBy(player) || !canAfford(player) || !hasValidTargets(player)) {
        return false;
    }
    
    setPlayedBy(player);
    setTurnPlayed(ENGINE.getCurrentTurn());
    setInPlay(true);
    
    onPlay(player);
    
    // Execute all effects
    for (const auto& effect : effects) {
        if (!executeEffect(effect, player, parameters)) {
            std::cerr << "Failed to execute effect for card: " << name << std::endl;
            return false;
        }
        onEffectResolved(effect, player);
    }
    
    return true;
}

void Card::onPlay(PlayerID player) {
    // Default implementation - can be overridden by derived classes
    std::cout << "Card played: " << name << " by player " << static_cast<int>(player) << std::endl;
}

void Card::onEffectResolved(const CardEffectData& effect, PlayerID player) {
    // Default implementation - can be overridden
    std::cout << "Effect resolved: " << cardEffectToString(effect.effectType) 
              << " with magnitude " << effect.magnitude << std::endl;
}

void Card::onDiscard(PlayerID player) {
    // Default implementation
    setInPlay(false);
    setExhausted(false);
}

bool Card::executeEffect(const CardEffectData& effect, PlayerID player, 
                        const std::map<std::string, std::string>& parameters) {
    switch (effect.effectType) {
        case CardEffect::CURRENCY_BONUS:
            // Add currency to player
            return true;
            
        case CardEffect::CURRENCY_PENALTY:
            // Remove currency from player
            return true;
            
        case CardEffect::INFLUENCE_BONUS:
            // Add influence to player
            return true;
            
        case CardEffect::INFLUENCE_PENALTY:
            // Remove influence from player
            return true;
            
        case CardEffect::UNIT_SPAWN:
            // Spawn unit for player
            return true;
            
        case CardEffect::UNIT_UPGRADE:
            // Upgrade player's units
            return true;
            
        case CardEffect::FORTIFICATION_BUILD:
            // Build fortification for player
            return true;
            
        case CardEffect::TERRITORY_CONTROL:
            // Change territory control
            return true;
            
        case CardEffect::FEDERATION_ACCEDE:
            // Player accedes to federation
            return true;
            
        case CardEffect::POPULATION_CHANGE:
            // Change population in cities
            return true;
            
        case CardEffect::SHIMARRA_CHANGE:
            // Change Shimarra for player
            return true;
            
        case CardEffect::CUSTOM:
            // Handle custom effects
            return executeCustomEffect(effect, player, parameters);
            
        default:
            std::cerr << "Unknown effect type: " << static_cast<int>(effect.effectType) << std::endl;
            return false;
    }
}

bool Card::executeCustomEffect(const CardEffectData& effect, PlayerID player, 
                              const std::map<std::string, std::string>& parameters) {
    // This would handle card-specific custom effects
    // Implementation depends on the specific card
    return true;
}

std::string Card::getCardDescription() const {
    std::ostringstream oss;
    oss << name << " (" << cardTypeToString(type) << ")\n";
    oss << "Cost: " << getCostDescription() << "\n";
    oss << "Text: " << exactText << "\n";
    if (!flavorText.empty()) {
        oss << "Flavor: " << flavorText << "\n";
    }
    oss << "Effects: " << getEffectsDescription();
    return oss.str();
}

std::string Card::getCostDescription() const {
    std::ostringstream oss;
    if (cost.currencyCost > 0) oss << cost.currencyCost << " Currency ";
    if (cost.influenceCost > 0) oss << cost.influenceCost << " Influence ";
    if (cost.shimarraCost > 0) oss << cost.shimarraCost << " Shimarra ";
    return oss.str();
}

std::string Card::getEffectsDescription() const {
    std::ostringstream oss;
    for (size_t i = 0; i < effects.size(); i++) {
        if (i > 0) oss << ", ";
        oss << cardEffectToString(effects[i].effectType);
        if (effects[i].magnitude != 0) {
            oss << " (" << effects[i].magnitude << ")";
        }
    }
    return oss.str();
}

std::string Card::serialize() const {
    std::ostringstream oss;
    oss << id << "|" << name << "|" << exactText << "|" << static_cast<int>(type) << "|"
        << static_cast<int>(rarity) << "|" << cost.currencyCost << "|" << cost.influenceCost << "|"
        << cost.shimarraCost << "|" << isUnique << "|" << isLimited << "|" << copiesInDeck << "|"
        << isInPlay << "|" << isExhausted << "|" << turnPlayed << "|" << static_cast<int>(playedBy);
    
    // Serialize effects
    for (const auto& effect : effects) {
        oss << "|" << static_cast<int>(effect.effectType) << ":" << effect.magnitude 
            << ":" << effect.targetPlayer << ":" << effect.targetTerritory;
    }
    
    return oss.str();
}

bool Card::deserialize(const std::string& data) {
    std::istringstream iss(data);
    std::string token;
    
    std::vector<std::string> tokens;
    while (std::getline(iss, token, '|')) {
        tokens.push_back(token);
    }
    
    if (tokens.size() < 14) {
        return false;
    }
    
    try {
        id = std::stoi(tokens[0]);
        name = tokens[1];
        exactText = tokens[2];
        type = static_cast<CardType>(std::stoi(tokens[3]));
        rarity = static_cast<CardRarity>(std::stoi(tokens[4]));
        cost.currencyCost = std::stoi(tokens[5]);
        cost.influenceCost = std::stoi(tokens[6]);
        cost.shimarraCost = std::stoi(tokens[7]);
        isUnique = (tokens[8] == "1");
        isLimited = (tokens[9] == "1");
        copiesInDeck = std::stoi(tokens[10]);
        isInPlay = (tokens[11] == "1");
        isExhausted = (tokens[12] == "1");
        turnPlayed = std::stoi(tokens[13]);
        playedBy = static_cast<PlayerID>(std::stoi(tokens[14]));
        
        // Parse effects
        effects.clear();
        for (size_t i = 15; i < tokens.size(); i++) {
            std::istringstream effectIss(tokens[i]);
            std::string effectToken;
            std::vector<std::string> effectTokens;
            while (std::getline(effectIss, effectToken, ':')) {
                effectTokens.push_back(effectToken);
            }
            
            if (effectTokens.size() >= 4) {
                CardEffectData effect;
                effect.effectType = static_cast<CardEffect>(std::stoi(effectTokens[0]));
                effect.magnitude = std::stoi(effectTokens[1]);
                effect.targetPlayer = effectTokens[2];
                effect.targetTerritory = effectTokens[3];
                effects.push_back(effect);
            }
        }
        
        return true;
    } catch (const std::exception&) {
        return false;
    }
}

// Factory methods
std::unique_ptr<Card> Card::createAmericaCard(int id, const std::string& name, 
                                             const std::string& exactText) {
    auto card = std::make_unique<AmericaCard>(id, name, exactText);
    return std::move(card);
}

std::unique_ptr<Card> Card::createCommunismCard(int id, const std::string& name, 
                                               const std::string& exactText) {
    auto card = std::make_unique<CommunismCard>(id, name, exactText);
    return std::move(card);
}

std::unique_ptr<Card> Card::createDivineWillCard(int id, const std::string& name, 
                                                const std::string& exactText) {
    auto card = std::make_unique<DivineWillCard>(id, name, exactText);
    return std::move(card);
}

std::unique_ptr<Card> Card::createTriviaCard(int id, const std::string& name, 
                                             const std::string& exactText) {
    // Trivia cards need question data, so this is a simplified factory
    auto card = std::make_unique<TriviaCard>(id, name, exactText, "", {}, 0);
    return std::move(card);
}

std::unique_ptr<Card> Card::createMischiefCard(int id, const std::string& name, 
                                               const std::string& exactText) {
    auto card = std::make_unique<MischiefCard>(id, name, exactText);
    return std::move(card);
}

std::unique_ptr<Card> Card::createEUInfluenceCard(int id, const std::string& name, 
                                                  const std::string& exactText) {
    auto card = std::make_unique<EUInfluenceCard>(id, name, exactText);
    return std::move(card);
}

std::unique_ptr<Card> Card::createAllianceCard(int id, const std::string& name, 
                                               const std::string& exactText) {
    auto card = std::make_unique<AllianceCard>(id, name, exactText);
    return std::move(card);
}

std::unique_ptr<Card> Card::createFederationCard(int id, const std::string& name, 
                                                const std::string& exactText) {
    auto card = std::make_unique<FederationCard>(id, name, exactText);
    return std::move(card);
}

// AmericaCard implementation
AmericaCard::AmericaCard(int id, const std::string& name, const std::string& exactText)
    : Card(id, name, CardType::AMERICA, exactText) {
    setupAmericaEffects();
}

void AmericaCard::setupAmericaEffects() {
    // Setup America-specific effects based on card name and text
    if (name.find("Gauss Rifle") != std::string::npos) {
        CardEffectData effect;
        effect.effectType = CardEffect::UNIT_UPGRADE;
        effect.effectValue = "Gauss Rifle";
        effect.magnitude = 5; // +5 attack power
        effect.targetPlayer = "self";
        addEffect(effect);
    }
    
    if (name.find("Titanium Weave") != std::string::npos) {
        CardEffectData effect;
        effect.effectType = CardEffect::UNIT_UPGRADE;
        effect.effectValue = "Titanium Weave";
        effect.magnitude = 4; // +4 defense
        effect.targetPlayer = "self";
        addEffect(effect);
    }
    
    if (name.find("Constitution") != std::string::npos) {
        CardEffectData effect;
        effect.effectType = CardEffect::CUSTOM;
        effect.effectValue = "ignore_mischief";
        effect.magnitude = 2; // Ignore up to 2 mischief cards
        effect.targetPlayer = "self";
        addEffect(effect);
    }
    
    if (name.find("Federation") != std::string::npos) {
        CardEffectData effect;
        effect.effectType = CardEffect::FEDERATION_ACCEDE;
        effect.targetPlayer = "self";
        addEffect(effect);
    }
}

bool AmericaCard::deployUnit(const std::string& unitType, int territoryId) {
    // Deploy unit logic would go here
    std::cout << "Deploying " << unitType << " to territory " << territoryId << std::endl;
    return true;
}

bool AmericaCard::upgradeTechnology(const std::string& techName) {
    // Technology upgrade logic would go here
    std::cout << "Upgrading technology: " << techName << std::endl;
    return true;
}

bool AmericaCard::repairNuclearProgram() {
    // Nuclear program repair logic would go here
    std::cout << "Repairing nuclear program" << std::endl;
    return true;
}

bool AmericaCard::launchOrbitalStrike(int territoryId) {
    // Orbital strike logic would go here
    std::cout << "Launching orbital strike on territory " << territoryId << std::endl;
    return true;
}

// CommunismCard implementation
CommunismCard::CommunismCard(int id, const std::string& name, const std::string& exactText)
    : Card(id, name, CardType::COMMUNISM, exactText) {
    setupCommunismEffects();
}

void CommunismCard::setupCommunismEffects() {
    if (name.find("Neobkhodimyy") != std::string::npos) {
        CardEffectData effect;
        effect.effectType = CardEffect::TERRITORY_CONTROL;
        effect.effectValue = "auto_take_adjacent";
        effect.magnitude = 1;
        effect.targetPlayer = "self";
        addEffect(effect);
    }
    
    if (name.find("Vosstanovit") != std::string::npos) {
        CardEffectData effect;
        effect.effectType = CardEffect::NUKE_ENABLE;
        effect.targetPlayer = "self";
        addEffect(effect);
    }
    
    if (name.find("Zagovor") != std::string::npos) {
        CardEffectData effect;
        effect.effectType = CardEffect::NUKE_DISABLE;
        effect.targetPlayer = "enemy";
        addEffect(effect);
    }
}

bool CommunismCard::upgradeSuperweapon(const std::string& component) {
    std::cout << "Upgrading superweapon with component: " << component << std::endl;
    return true;
}

bool CommunismCard::deploySpecialForces(const std::string& forceType, int territoryId) {
    std::cout << "Deploying special forces: " << forceType << " to territory " << territoryId << std::endl;
    return true;
}

bool CommunismCard::sabotageEnemyProgram(PlayerID targetPlayer) {
    std::cout << "Sabotaging program of player " << static_cast<int>(targetPlayer) << std::endl;
    return true;
}

bool CommunismCard::expandInfluence(int territoryId, int amount) {
    std::cout << "Expanding influence in territory " << territoryId << " by " << amount << std::endl;
    return true;
}

// TriviaCard implementation
TriviaCard::TriviaCard(int id, const std::string& name, const std::string& exactText,
                       const std::string& question, const std::vector<std::string>& options, 
                       int correctAnswer)
    : Card(id, name, CardType::TRIVIA, exactText), question(question), 
      options(options), correctAnswer(correctAnswer) {
    setupTriviaEffects();
}

void TriviaCard::setupTriviaEffects() {
    CardEffectData effect;
    effect.effectType = CardEffect::INFLUENCE_BONUS;
    effect.magnitude = 10; // Default influence reward
    effect.targetPlayer = "self";
    addEffect(effect);
}

bool TriviaCard::askQuestion() {
    std::cout << "Trivia Question: " << question << std::endl;
    for (size_t i = 0; i < options.size(); i++) {
        std::cout << (i + 1) << ". " << options[i] << std::endl;
    }
    return true;
}

bool TriviaCard::checkAnswer(int answer) {
    return answer == correctAnswer;
}

int TriviaCard::getInfluenceReward() const {
    return 10; // Default reward
}

// MischiefCard implementation
MischiefCard::MischiefCard(int id, const std::string& name, const std::string& exactText)
    : Card(id, name, CardType::MISCHIEF, exactText) {
    setupMischiefEffects();
}

void MischiefCard::setupMischiefEffects() {
    // Most mischief cards give Shimarra
    CardEffectData shimarraEffect;
    shimarraEffect.effectType = CardEffect::SHIMARRA_CHANGE;
    shimarraEffect.magnitude = 1;
    shimarraEffect.targetPlayer = "self";
    addEffect(shimarraEffect);
}

bool MischiefCard::causeChaos(const std::string& chaosType) {
    std::cout << "Causing chaos: " << chaosType << std::endl;
    return true;
}

bool MischiefCard::spawnDevilUnits(int count, int fragmentId) {
    std::cout << "Spawning " << count << " devil units from fragment " << fragmentId << std::endl;
    return true;
}

bool MischiefCard::corruptTerritory(int territoryId) {
    std::cout << "Corrupting territory " << territoryId << std::endl;
    return true;
}

bool MischiefCard::stealShimarra(PlayerID targetPlayer, int amount) {
    std::cout << "Stealing " << amount << " shimarra from player " << static_cast<int>(targetPlayer) << std::endl;
    return true;
}

// EUInfluenceCard implementation
EUInfluenceCard::EUInfluenceCard(int id, const std::string& name, const std::string& exactText)
    : Card(id, name, CardType::EU_INFLUENCE, exactText) {
    setupEUInfluenceEffects();
}

void EUInfluenceCard::setupEUInfluenceEffects() {
    CardEffectData effect;
    effect.effectType = CardEffect::INFLUENCE_SPREAD;
    effect.magnitude = 15;
    effect.targetPlayer = "self";
    addEffect(effect);
}

bool EUInfluenceCard::applyDiplomaticPressure(int territoryId) {
    std::cout << "Applying diplomatic pressure to territory " << territoryId << std::endl;
    return true;
}

bool EUInfluenceCard::formTradeAgreement(PlayerID partnerPlayer) {
    std::cout << "Forming trade agreement with player " << static_cast<int>(partnerPlayer) << std::endl;
    return true;
}

bool EUInfluenceCard::expandUnion(int territoryId) {
    std::cout << "Expanding union to territory " << territoryId << std::endl;
    return true;
}

bool EUInfluenceCard::implementSanctions(PlayerID targetPlayer) {
    std::cout << "Implementing sanctions against player " << static_cast<int>(targetPlayer) << std::endl;
    return true;
}

// AllianceCard implementation
AllianceCard::AllianceCard(int id, const std::string& name, const std::string& exactText)
    : Card(id, name, CardType::ALLIANCE, exactText) {
    setupAllianceEffects();
}

void AllianceCard::setupAllianceEffects() {
    CardEffectData effect;
    effect.effectType = CardEffect::RESOURCE_EXTRACTION;
    effect.magnitude = 20;
    effect.targetPlayer = "self";
    addEffect(effect);
}

bool AllianceCard::extractResources(int territoryId, int amount) {
    std::cout << "Extracting " << amount << " resources from territory " << territoryId << std::endl;
    return true;
}

bool AllianceCard::developInfrastructure(int territoryId) {
    std::cout << "Developing infrastructure in territory " << territoryId << std::endl;
    return true;
}

bool AllianceCard::adaptToClimate(int territoryId) {
    std::cout << "Adapting to climate in territory " << territoryId << std::endl;
    return true;
}

bool AllianceCard::establishBase(int territoryId) {
    std::cout << "Establishing base in territory " << territoryId << std::endl;
    return true;
}

// FederationCard implementation
FederationCard::FederationCard(int id, const std::string& name, const std::string& exactText)
    : Card(id, name, CardType::FEDERATION, exactText) {
    setupFederationEffects();
}

void FederationCard::setupFederationEffects() {
    CardEffectData effect;
    effect.effectType = CardEffect::CUSTOM;
    effect.effectValue = "federation_vote";
    effect.targetPlayer = "all";
    addEffect(effect);
}

bool FederationCard::accedeToFederation() {
    std::cout << "Acceding to federation" << std::endl;
    return true;
}

bool FederationCard::voteOnProposal(const std::string& proposal) {
    std::cout << "Voting on proposal: " << proposal << std::endl;
    return true;
}

bool FederationCard::establishCouncil() {
    std::cout << "Establishing federation council" << std::endl;
    return true;
}

// CardDeck implementation
CardDeck::CardDeck(CardType type, const std::string& name) 
    : deckType(type), deckName(name), isShuffled(false) {
}

void CardDeck::addCard(std::shared_ptr<Card> card) {
    cards.push_back(card);
}

void CardDeck::removeCard(std::shared_ptr<Card> card) {
    auto it = std::find(cards.begin(), cards.end(), card);
    if (it != cards.end()) {
        cards.erase(it);
    }
}

void CardDeck::shuffle() {
    std::random_device rd;
    std::mt19937 g(rd());
    std::shuffle(cards.begin(), cards.end(), g);
    isShuffled = true;
}

std::shared_ptr<Card> CardDeck::drawCard() {
    if (cards.empty()) {
        reshuffleDiscardPile();
    }
    
    if (!cards.empty()) {
        auto card = cards.back();
        cards.pop_back();
        return card;
    }
    
    return nullptr;
}

std::vector<std::shared_ptr<Card>> CardDeck::drawCards(int count) {
    std::vector<std::shared_ptr<Card>> drawnCards;
    for (int i = 0; i < count; i++) {
        auto card = drawCard();
        if (card) {
            drawnCards.push_back(card);
        } else {
            break;
        }
    }
    return drawnCards;
}

void CardDeck::discardCard(std::shared_ptr<Card> card) {
    if (card) {
        discardPile.push_back(card);
    }
}

void CardDeck::discardCards(const std::vector<std::shared_ptr<Card>>& cards) {
    for (const auto& card : cards) {
        discardCard(card);
    }
}

void CardDeck::reshuffleDiscardPile() {
    if (!discardPile.empty()) {
        cards.insert(cards.end(), discardPile.begin(), discardPile.end());
        discardPile.clear();
        shuffle();
    }
}

std::string cardTypeToString(CardType type) {
    switch (type) {
        case CardType::AMERICA: return "America";
        case CardType::COMMUNISM: return "Communism";
        case CardType::DIVINE_WILL: return "Divine Will";
        case CardType::TRIVIA: return "Trivia";
        case CardType::MISCHIEF: return "Mischief";
        case CardType::EU_INFLUENCE: return "EU Influence";
        case CardType::ALLIANCE: return "Alliance";
        case CardType::FEDERATION: return "Federation";
        default: return "Unknown";
    }
}

std::string cardEffectToString(CardEffect effect) {
    switch (effect) {
        case CardEffect::CURRENCY_BONUS: return "Currency Bonus";
        case CardEffect::CURRENCY_PENALTY: return "Currency Penalty";
        case CardEffect::INFLUENCE_BONUS: return "Influence Bonus";
        case CardEffect::INFLUENCE_PENALTY: return "Influence Penalty";
        case CardEffect::UNIT_SPAWN: return "Spawn Unit";
        case CardEffect::UNIT_UPGRADE: return "Upgrade Unit";
        case CardEffect::FORTIFICATION_BUILD: return "Build Fortification";
        case CardEffect::TERRITORY_CONTROL: return "Territory Control";
        case CardEffect::FEDERATION_ACCEDE: return "Accede to Federation";
        case CardEffect::SHIMARRA_CHANGE: return "Shimarra Change";
        case CardEffect::CUSTOM: return "Custom Effect";
        default: return "Unknown Effect";
    }
}