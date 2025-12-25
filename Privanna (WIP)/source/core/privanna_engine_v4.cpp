#include "privanna_engine.hpp"
#include "../character/character_system.hpp"
#include "../faction/faction_relationship_system.hpp"
#include "../combat/combat_system.hpp"
#include "../economy/economic_system.hpp"
#include <iostream>
#include <chrono>
#include <thread>

namespace Privanna {

class PrivannaEngineV4 : public PrivannaEngine {
private:
    // Version 4 specific systems
    std::shared_ptr<CharacterSystem> characterSystem;
    std::shared_ptr<FactionRelationshipSystem> factionSystem;
    std::shared_ptr<CombatSystem> combatSystem;
    std::shared_ptr<EconomicSystem> economicSystem;
    
    // Performance tracking
    float characterUpdateTime = 0.0f;
    float factionUpdateTime = 0.0f;
    float combatUpdateTime = 0.0f;
    float economicUpdateTime = 0.0f;
    
    // Demo data
    std::shared_ptr<Character> demoCharacter;
    std::shared_ptr<Combat> demoCombat;
    
public:
    PrivannaEngineV4() : PrivannaEngine() {
        version = "Version 4.0 - Character Development & Game Mechanics";
        std::cout << "Initializing Privanna Engine " << version << std::endl;
        
        // Initialize Version 4 systems
        initializeCharacterSystem();
        initializeFactionSystem();
        initializeCombatSystem();
        initializeEconomicSystem();
        
        // Setup demo content
        setupDemoContent();
        
        std::cout << "Version 4 systems initialized successfully!" << std::endl;
    }
    
    ~PrivannaEngineV4() {
        std::cout << "Shutting down Privanna Engine Version 4" << std::endl;
    }
    
protected:
    void initializeSystems() override {
        // Call parent initialization
        PrivannaEngine::initializeSystems();
        
        std::cout << "Version 4 systems initialization complete" << std::endl;
    }
    
    void updateSystems(float deltaTime) override {
        // Update parent systems
        PrivannaEngine::updateSystems(deltaTime);
        
        auto startChar = std::chrono::high_resolution_clock::now();
        if (characterSystem) {
            characterSystem->update(deltaTime);
        }
        auto endChar = std::chrono::high_resolution_clock::now();
        characterUpdateTime = std::chrono::duration<float, std::milli>(endChar - startChar).count();
        
        auto startFaction = std::chrono::high_resolution_clock::now();
        if (factionSystem) {
            factionSystem->update(deltaTime);
        }
        auto endFaction = std::chrono::high_resolution_clock::now();
        factionUpdateTime = std::chrono::duration<float, std::milli>(endFaction - startFaction).count();
        
        auto startCombat = std::chrono::high_resolution_clock::now();
        if (combatSystem) {
            combatSystem->update(deltaTime);
        }
        auto endCombat = std::chrono::high_resolution_clock::now();
        combatUpdateTime = std::chrono::duration<float, std::milli>(endCombat - startCombat).count();
        
        auto startEconomic = std::chrono::high_resolution_clock::now();
        if (economicSystem) {
            economicSystem->update(deltaTime);
        }
        auto endEconomic = std::chrono::high_resolution_clock::now();
        economicUpdateTime = std::chrono::duration<float, std::milli>(endEconomic - startEconomic).count();
    }
    
    void renderFrame() override {
        // Render parent systems
        PrivannaEngine::renderFrame();
        
        // Render Version 4 specific information
        renderVersion4Info();
    }
    
private:
    void initializeCharacterSystem() {
        characterSystem = std::make_shared<CharacterSystem>(eventSystem, logger);
        std::cout << "Character System initialized with 1000+ character development features" << std::endl;
        
        // Register some demo skills and talents
        auto swordMastery = std::make_shared<Skill>();
        swordMastery->name = "Sword Mastery";
        swordMastery->type = SkillType::COMBAT;
        swordMastery->description = "Master the art of sword combat";
        characterSystem->registerSkill(swordMastery);
        
        auto charismaTalent = std::make_shared<Talent>();
        charismaTalent->name = "Natural Leader";
        charismaTalent->description = "Born leadership abilities that inspire allies";
        charismaTalent->tier = 1;
        charismaTalent->effects["leadership_bonus"] = 1.5f;
        characterSystem->registerTalent(charismaTalent);
    }
    
    void initializeFactionSystem() {
        factionSystem = std::make_shared<FactionRelationshipSystem>(eventSystem, logger);
        std::cout << "Faction Relationship System initialized with complex diplomacy" << std::endl;
        
        // Demo faction interactions
        auto luciferFaction = factionSystem->getFaction(SpecificFaction::LUCIFER_LEGION);
        auto maridFaction = factionSystem->getFaction(SpecificFaction::MARID_ROYALTY);
        
        if (luciferFaction && maridFaction) {
            factionSystem->formAlliance(SpecificFaction::LUCIFER_LEGION, SpecificFaction::MARID_ROYALTY);
        }
    }
    
    void initializeCombatSystem() {
        combatSystem = std::make_shared<CombatSystem>(eventSystem, logger);
        std::cout << "Combat System initialized with tactical warfare mechanics" << std::endl;
        
        // Create demo combat
        demoCombat = combatSystem->createCombat("Demo Battle", CombatType::MELEE, "Battlefield");
        if (demoCombat) {
            // Add some demo units
            auto playerUnit = combatSystem->createUnit("Hero Warrior", UnitType::WARRIOR, SpecificFaction::LUCIFER_LEGION, 5);
            auto enemyUnit = combatSystem->createUnit("Orc Berserker", UnitType::BESERKER, SpecificFaction::HORDE, 4);
            
            if (playerUnit && enemyUnit) {
                demoCombat->addPlayerUnit(playerUnit);
                demoCombat->addEnemyUnit(enemyUnit);
                demoCombat->startCombat();
            }
        }
    }
    
    void initializeEconomicSystem() {
        economicSystem = std::make_shared<EconomicSystem>(eventSystem, logger);
        std::cout << "Economic System initialized with resource management" << std::endl;
        
        // Create demo economies
        auto luciferEconomy = economicSystem->createEconomy("Lucifer Legion Treasury", SpecificFaction::LUCIFER_LEGION);
        auto maridEconomy = economicSystem->createEconomy("Marid Royal Treasury", SpecificFaction::MARID_ROYALTY);
        
        if (luciferEconomy) {
            luciferEconomy->addResource(ResourceType::GOLD, 10000);
            luciferEconomy->addResource(ResourceType::IRON, 5000);
            luciferEconomy->addResource(ResourceType::DEMON_ESSENCE, 1000);
        }
        
        if (maridEconomy) {
            maridEconomy->addResource(ResourceType::GOLD, 15000);
            maridEconomy->addResource(ResourceType::MANA_CRYSTALS, 8000);
            maridEconomy->addResource(ResourceType::DJINN_LAMP, 500);
        }
    }
    
    void setupDemoContent() {
        // Create demo character
        if (characterSystem) {
            demoCharacter = characterSystem->createCharacter("Iblis Redeemed", CharacterClass::CLERIC);
            if (demoCharacter) {
                // Add some experience and progress
                characterSystem->awardExperience("Iblis Redeemed", 500, "character_creation");
                characterSystem->awardAchievement("Iblis Redeemed", "Redemption Path");
                
                // Learn some skills
                demoCharacter->learnSkill("Sword Mastery");
                demoCharacter->upgradeSkill("Sword Mastery");
                
                // Unlock talent
                demoCharacter->unlockTalent("Natural Leader");
            }
        }
        
        std::cout << "Demo content setup complete" << std::endl;
    }
    
    void renderVersion4Info() {
        // Display Version 4 system information
        std::cout << "\n=== PRIVANNA ENGINE VERSION 4 - CHARACTER DEVELOPMENT & GAME MECHANICS ===" << std::endl;
        std::cout << "Frame Time: " << getFrameTime() << "ms | FPS: " << getFPS() << std::endl;
        std::cout << "Character System: " << characterUpdateTime << "ms" << std::endl;
        std::cout << "Faction System: " << factionUpdateTime << "ms" << std::endl;
        std::cout << "Combat System: " << combatUpdateTime << "ms" << std::endl;
        std::cout << "Economic System: " << economicUpdateTime << "ms" << std::endl;
        
        // Display character information
        if (demoCharacter) {
            std::cout << "\n--- DEMO CHARACTER: " << demoCharacter->getName() << " ---" << std::endl;
            std::cout << "Class: " << static_cast<int>(demoCharacter->getCharacterClass()) << std::endl;
            std::cout << "Level: " << demoCharacter->getLevel() << std::endl;
            std::cout << "Experience: " << demoCharacter->getExperience() << std::endl;
            std::cout << "Skills: " << demoCharacter->getSkills().size() << std::endl;
            std::cout << "Talents: " << demoCharacter->getTalents().size() << std::endl;
            std::cout << "Achievements: " << demoCharacter->getAchievements().size() << std::endl;
            
            // Display attributes
            const auto& attrs = demoCharacter->getAttributes();
            std::cout << "Attributes - STR:" << attrs.getAttribute(Attribute::STRENGTH)
                      << " INT:" << attrs.getAttribute(Attribute::INTELLIGENCE)
                      << " CHA:" << attrs.getAttribute(Attribute::CHARISMA)
                      << " FAITH:" << attrs.getAttribute(Attribute::FAITH) << std::endl;
        }
        
        // Display faction information
        if (factionSystem) {
            std::cout << "\n--- FACTION DIPLOMACY ---" << std::endl;
            auto powerBalance = factionSystem->calculatePowerBalance();
            std::cout << "Active Factions: " << powerBalance.size() << std::endl;
            
            auto alliances = factionSystem->getAlliedFactions();
            auto conflicts = factionSystem->getConflictingFactions();
            std::cout << "Alliances: " << alliances.size() << " | Conflicts: " << conflicts.size() << std::endl;
        }
        
        // Display combat information
        if (demoCombat && demoCombat->isActive()) {
            std::cout << "\n--- ACTIVE COMBAT: " << demoCombat->getName() << " ---" << std::endl;
            std::cout << "Turn: " << demoCombat->getCurrentTurn() 
                      << " | Phase: " << (demoCombat->isPlayerTurnActive() ? "Player" : "Enemy") << std::endl;
            
            auto playerUnits = demoCombat->getAliveUnits(true);
            auto enemyUnits = demoCombat->getAliveUnits(false);
            std::cout << "Player Units: " << playerUnits.size() 
                      << " | Enemy Units: " << enemyUnits.size() << std::endl;
            
            // Show recent combat log
            const auto& log = demoCombat->getCombatLog();
            if (!log.empty()) {
                std::cout << "Latest: " << log.back() << std::endl;
            }
        }
        
        // Display economic information
        if (economicSystem) {
            std::cout << "\n--- ECONOMIC OVERVIEW ---" << std::endl;
            auto wealthRanks = economicSystem->getWealthRankings();
            std::cout << "Economies: " << wealthRanks.size() << std::endl;
            
            // Show top economies
            int count = 0;
            for (const auto& pair : wealthRanks) {
                if (count >= 3) break;
                std::cout << "Faction " << static_cast<int>(pair.first) 
                          << ": " << pair.second << " gold" << std::endl;
                count++;
            }
        }
        
        std::cout << "\n=== 1000+ CHARACTER DEVELOPMENT & GAME MECHANICS FEATURES ACTIVE ===" << std::endl;
        std::cout << "Including: Character Progression, Faction Relationships, Combat Systems, Economic Management" << std::endl;
        std::cout << "=========================================================================" << std::endl;
    }
};

} // namespace Privanna

// Main function for Version 4 demo
int main() {
    std::cout << "Starting Privanna Engine Version 4 Demo..." << std::endl;
    std::cout << "Character Development & Game Mechanics Implementation" << std::endl;
    std::cout << "=========================================================" << std::endl;
    
    try {
        // Create and run the Version 4 engine
        auto engine = std::make_unique<Privanna::PrivannaEngineV4>();
        
        std::cout << "\nEngine created successfully. Running demo..." << std::endl;
        std::cout << "Press Ctrl+C to stop the demo." << std::endl;
        
        // Run the engine loop
        engine->run();
        
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }
    
    return 0;
}