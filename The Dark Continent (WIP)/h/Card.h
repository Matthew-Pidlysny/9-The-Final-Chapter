#ifndef CARD_H
#define CARD_H

#include <string>
#include <vector>
#include <memory>
#include <map>
#include "GameEngine.h"

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

enum class CardRarity {
    COMMON,
    UNCOMMON,
    RARE,
    LEGENDARY
};

enum class CardEffect {
    // Economic effects
    CURRENCY_BONUS,
    CURRENCY_PENALTY,
    INFLUENCE_BONUS,
    INFLUENCE_PENALTY,
    RESOURCE_EXTRACTION,
    
    // Military effects
    UNIT_SPAWN,
    UNIT_UPGRADE,
    FORTIFICATION_BUILD,
    ATTACK_BONUS,
    DEFENSE_BONUS,
    NUKE_ENABLE,
    NUKE_DISABLE,
    
    // Political effects
    TERRITORY_CONTROL,
    INFLUENCE_SPREAD,
    ALLIANCE_FORM,
    TRUCE_FORM,
    FEDERATION_ACCEDE,
    
    // Special effects
    POPULATION_CHANGE,
    SHIMARRA_CHANGE,
    TECHNOLOGY_GAIN,
    ESPIONAGE,
    SABOTAGE,
    
    // Dark Continent specific
    FRAGMENT_SPAWN,
    DEVIL_UNIT_SPAWN,
    MISCHIEF_EFFECT,
    
    // Custom effects (card-specific)
    CUSTOM
};

struct CardCost {
    int currencyCost;
    int influenceCost;
    int shimarraCost;
    bool requiresNuclearProgram;
    bool requiresSuperweapon;
    std::map<std::string, bool> prerequisiteFlags;
    
    CardCost() : currencyCost(0), influenceCost(0), shimarraCost(0),
                 requiresNuclearProgram(false), requiresSuperweapon(false) {}
};

struct CardEffectData {
    CardEffect effectType;
    std::string effectValue;
    int magnitude;
    std::string targetPlayer; // "self", "enemy", "all", "selected"
    std::string targetTerritory; // "any", "adjacent", "controlled", etc.
    std::vector<std::string> parameters;
    
    CardEffectData() : effectType(CardEffect::CUSTOM), magnitude(0) {}
};

class Card {
private:
    int id;
    std::string name;
    std::string exactText; // Preserved exact wording from original cards
    CardType type;
    CardRarity rarity;
    CardCost cost;
    std::vector<CardEffectData> effects;
    std::string flavorText;
    std::string imageName;
    bool isUnique;
    bool isLimited;
    int copiesInDeck;
    
    // Card state
    bool isInPlay;
    bool isExhausted;
    int turnPlayed;
    PlayerID playedBy;
    std::map<std::string, std::string> customData;

public:
    Card(int id, const std::string& name, CardType type, const std::string& exactText);
    virtual ~Card() = default;
    
    // Basic card info
    int getID() const { return id; }
    const std::string& getName() const { return name; }
    const std::string& getExactText() const { return exactText; }
    CardType getType() const { return type; }
    CardRarity getRarity() const { return rarity; }
    
    void setRarity(CardRarity r) { rarity = r; }
    void setFlavorText(const std::string& text) { flavorText = text; }
    void setImageName(const std::string& name) { imageName = name; }
    void setUnique(bool unique) { isUnique = unique; }
    void setLimited(bool limited) { isLimited = limited; }
    void setCopiesInDeck(int copies) { copiesInDeck = copies; }
    
    // Cost management
    const CardCost& getCost() const { return cost; }
    void setCost(const CardCost& newCost) { cost = newCost; }
    void setCurrencyCost(int cost) { this->cost.currencyCost = cost; }
    void setInfluenceCost(int cost) { this->cost.influenceCost = cost; }
    void setShimarraCost(int cost) { this->cost.shimarraCost = cost; }
    
    // Effects management
    void addEffect(const CardEffectData& effect);
    void clearEffects();
    const std::vector<CardEffectData>& getEffects() const { return effects; }
    
    // Card state
    bool getIsInPlay() const { return isInPlay; }
    bool getIsExhausted() const { return isExhausted; }
    int getTurnPlayed() const { return turnPlayed; }
    PlayerID getPlayedBy() const { return playedBy; }
    
    void setInPlay(bool inPlay);
    void setExhausted(bool exhausted);
    void setTurnPlayed(int turn);
    void setPlayedBy(PlayerID player);
    
    // Custom data storage
    void setCustomData(const std::string& key, const std::string& value);
    std::string getCustomData(const std::string& key) const;
    
    // Card validation
    bool canBePlayedBy(PlayerID player) const;
    bool canAfford(PlayerID player) const;
    bool hasValidTargets(PlayerID player) const;
    
    // Card execution
    virtual bool play(PlayerID player, const std::map<std::string, std::string>& parameters = {});
    virtual void onPlay(PlayerID player);
    virtual void onEffectResolved(const CardEffectData& effect, PlayerID player);
    virtual void onDiscard(PlayerID player);
    
    // Effect execution helpers
    bool executeEffect(const CardEffectData& effect, PlayerID player, 
                      const std::map<std::string, std::string>& parameters = {});
    
    // Utility methods
    std::string getCardDescription() const;
    std::string getCostDescription() const;
    std::string getEffectsDescription() const;
    
    // Serialization
    virtual std::string serialize() const;
    virtual bool deserialize(const std::string& data);
    
    // Static factory methods for creating specific card types
    static std::unique_ptr<Card> createAmericaCard(int id, const std::string& name, 
                                                  const std::string& exactText);
    static std::unique_ptr<Card> createCommunismCard(int id, const std::string& name, 
                                                    const std::string& exactText);
    static std::unique_ptr<Card> createDivineWillCard(int id, const std::string& name, 
                                                     const std::string& exactText);
    static std::unique_ptr<Card> createTriviaCard(int id, const std::string& name, 
                                                 const std::string& exactText);
    static std::unique_ptr<Card> createMischiefCard(int id, const std::string& name, 
                                                   const std::string& exactText);
    static std::unique_ptr<Card> createEUInfluenceCard(int id, const std::string& name, 
                                                      const std::string& exactText);
    static std::unique_ptr<Card> createAllianceCard(int id, const std::string& name, 
                                                   const std::string& exactText);
    static std::unique_ptr<Card> createFederationCard(int id, const std::string& name, 
                                                     const std::string& exactText);
};

// Specialized card classes for exact wording preservation

class AmericaCard : public Card {
public:
    AmericaCard(int id, const std::string& name, const std::string& exactText);
    
    // America-specific card effects
    bool deployUnit(const std::string& unitType, int territoryId);
    bool upgradeTechnology(const std::string& techName);
    bool repairNuclearProgram();
    bool launchOrbitalStrike(int territoryId);
    
protected:
    void setupAmericaEffects();
};

class CommunismCard : public Card {
public:
    CommunismCard(int id, const std::string& name, const std::string& exactText);
    
    // Communism-specific card effects
    bool upgradeSuperweapon(const std::string& component);
    bool deploySpecialForces(const std::string& forceType, int territoryId);
    bool sabotageEnemyProgram(PlayerID targetPlayer);
    bool expandInfluence(int territoryId, int amount);
    
protected:
    void setupCommunismEffects();
};

class DivineWillCard : public Card {
public:
    DivineWillCard(int id, const std::string& name, const std::string& exactText);
    
    // Divine Will specific effects
    bool grantBlessing(PlayerID targetPlayer, const std::string& blessing);
    bool causeMiracle(const std::string& miracleType);
    bool divineIntervention(const std::string& intervention);
    
protected:
    void setupDivineWillEffects();
};

class TriviaCard : public Card {
private:
    std::string question;
    std::vector<std::string> options;
    int correctAnswer;
    
public:
    TriviaCard(int id, const std::string& name, const std::string& exactText, 
               const std::string& question, const std::vector<std::string>& options, 
               int correctAnswer);
    
    // Trivia-specific effects
    bool askQuestion();
    bool checkAnswer(int answer);
    int getInfluenceReward() const;
    
protected:
    void setupTriviaEffects();
};

class MischiefCard : public Card {
public:
    MischiefCard(int id, const std::string& name, const std::string& exactText);
    
    // Mischief-specific effects
    bool causeChaos(const std::string& chaosType);
    bool spawnDevilUnits(int count, int fragmentId);
    bool corruptTerritory(int territoryId);
    bool stealShimarra(PlayerID targetPlayer, int amount);
    
protected:
    void setupMischiefEffects();
};

class EUInfluenceCard : public Card {
public:
    EUInfluenceCard(int id, const std::string& name, const std::string& exactText);
    
    // EU-specific effects
    bool applyDiplomaticPressure(int territoryId);
    bool formTradeAgreement(PlayerID partnerPlayer);
    bool expandUnion(int territoryId);
    bool implementSanctions(PlayerID targetPlayer);
    
protected:
    void setupEUInfluenceEffects();
};

class AllianceCard : public Card {
public:
    AllianceCard(int id, const std::string& name, const std::string& exactText);
    
    // Alliance-specific effects
    bool extractResources(int territoryId, int amount);
    bool developInfrastructure(int territoryId);
    bool adaptToClimate(int territoryId);
    bool establishBase(int territoryId);
    
protected:
    void setupAllianceEffects();
};

class FederationCard : public Card {
public:
    FederationCard(int id, const std::string& name, const std::string& exactText);
    
    // Federation-specific effects
    bool accedeToFederation();
    bool voteOnProposal(const std::string& proposal);
    bool establishCouncil();
    
protected:
    void setupFederationEffects();
};

// Card deck management
class CardDeck {
private:
    std::vector<std::shared_ptr<Card>> cards;
    std::vector<std::shared_ptr<Card>> discardPile;
    CardType deckType;
    std::string deckName;
    bool isShuffled;
    
public:
    CardDeck(CardType type, const std::string& name);
    
    // Deck management
    void addCard(std::shared_ptr<Card> card);
    void removeCard(std::shared_ptr<Card> card);
    void shuffle();
    std::shared_ptr<Card> drawCard();
    std::vector<std::shared_ptr<Card>> drawCards(int count);
    void discardCard(std::shared_ptr<Card> card);
    void discardCards(const std::vector<std::shared_ptr<Card>>& cards);
    
    // Deck info
    int getRemainingCards() const { return static_cast<int>(cards.size()); }
    int getDiscardPileSize() const { return static_cast<int>(discardPile.size()); }
    CardType getDeckType() const { return deckType; }
    const std::string& getDeckName() const { return deckName; }
    bool isEmpty() const { return cards.empty(); }
    
    // Deck operations
    void reshuffleDiscardPile();
    void resetDeck();
    std::shared_ptr<Card> searchCard(const std::string& cardName);
    std::vector<std::shared_ptr<Card>> searchCardsByType(CardType type);
    
    // Serialization
    std::string serialize() const;
    bool deserialize(const std::string& data);
    
    // Initialization helpers
    void initializeAmericaDeck();
    void initializeCommunismDeck();
    void initializeDivineWillDeck();
    void initializeTriviaDeck();
    void initializeMischiefDeck();
    void initializeEUInfluenceDeck();
    void initializeAllianceDeck();
    void initializeFederationDeck();
};

// Utility functions
std::string cardTypeToString(CardType type);
CardType stringToCardType(const std::string& typeStr);
std::string cardRarityToString(CardRarity rarity);
CardRarity stringToCardRarity(const std::string& rarityStr);
std::string cardEffectToString(CardEffect effect);
CardEffect stringToCardEffect(const std::string& effectStr);

// Card validation
bool isValidCardType(CardType type);
bool isValidCardEffect(CardEffect effect);
bool validateCardEffect(const CardEffectData& effect);

#endif // CARD_H