#include "megaman_rpg_game.hpp"
#include <iostream>
#include <iomanip>
#include <sstream>
#include <algorithm>
#include <thread>
#include <chrono>

namespace MegamanRPG {

    // Character Implementation
    Character::Character(const std::string& char_name, CharacterClass char_class) 
        : name(char_name), character_class(char_class), level(1), experience(0), skill_points(5) {
        
        // Initialize stats based on class
        switch (character_class) {
            case CharacterClass::REPLOID_WARRIOR:
                stats.strength = 15;
                stats.defense = 12;
                stats.health = 120;
                stats.max_health = 120;
                break;
            case CharacterClass::REPLOID_SCOUT:
                stats.agility = 15;
                stats.accuracy = 85;
                stats.evasion = 30;
                break;
            case CharacterClass::REPLOID_ENGINEER:
                stats.intelligence = 15;
                stats.energy = 75;
                stats.max_energy = 75;
                break;
            case CharacterClass::HUMAN_COMMANDER:
                stats.charisma = 15;
                stats.intelligence = 12;
                break;
            default:
                // Balanced stats for other classes
                break;
        }
        
        // Initialize class-specific skills
        initializeClassSkills();
    }

    void Character::initializeClassSkills() {
        switch (character_class) {
            case CharacterClass::REPLOID_WARRIOR: {
                Skill combat_basics;
                combat_basics.name = "Combat Basics";
                combat_basics.type = SkillType::COMBAT;
                combat_basics.level = 1;
                combat_basics.abilities = {"Power Strike", "Defensive Stance"};
                skills["combat_basics"] = combat_basics;
                break;
            }
            case CharacterClass::REPLOID_SCOUT: {
                Skill stealth;
                stealth.name = "Stealth Movement";
                stealth.type = SkillType::SURVIVAL;
                stealth.level = 1;
                stealth.abilities = {"Shadow Step", "Silent Running"};
                skills["stealth"] = stealth;
                break;
            }
            case CharacterClass::REPLOID_ENGINEER: {
                Skill tech_expertise;
                tech_expertise.name = "Technical Expertise";
                tech_expertise.type = SkillType::ENGINEERING;
                tech_expertise.level = 1;
                tech_expertise.abilities = {"System Repair", "Equipment Upgrade"};
                skills["tech_expertise"] = tech_expertise;
                break;
            }
            default:
                // Add default skills for other classes
                break;
        }
    }

    void Character::levelUp() {
        level++;
        skill_points += 3;
        
        // Increase base stats
        stats.max_health += 10;
        stats.max_energy += 5;
        stats.health = stats.max_health;
        stats.energy = stats.max_energy;
        stats.strength += 2;
        stats.agility += 2;
        stats.intelligence += 2;
        stats.defense += 1;
        
        std::cout << name << " has reached level " << level << "!\n";
        std::cout << "Gained 3 skill points. Total skill points: " << skill_points << "\n";
    }

    void Character::gainExperience(int exp) {
        experience += exp;
        int exp_needed = level * 100;
        
        if (experience >= exp_needed) {
            experience -= exp_needed;
            levelUp();
        }
    }

    void Character::upgradeSkill(const std::string& skill_name) {
        auto it = skills.find(skill_name);
        if (it != skills.end() && skill_points > 0 && it->second.level < it->second.max_level) {
            it->second.level++;
            skill_points--;
            std::cout << "Upgraded " << skill_name << " to level " << it->second.level << "\n";
        }
    }

    int Character::calculateDamage() const {
        int base_damage = stats.strength * 2;
        
        // Add equipment bonuses
        for (const Equipment& item : equipment) {
            base_damage += item.power_level;
        }
        
        return base_damage;
    }

    int Character::calculateDefense() const {
        return stats.defense + (stats.agility / 2);
    }

    double Character::getHitChance() const {
        return stats.accuracy / 100.0;
    }

    double Character::getEvasionChance() const {
        return stats.evasion / 100.0;
    }

    void Character::takeDamage(int damage) {
        int actual_damage = std::max(1, damage - calculateDefense());
        stats.health = std::max(0, stats.health - actual_damage);
        std::cout << name << " takes " << actual_damage << " damage! HP: " << stats.health << "/" << stats.max_health << "\n";
    }

    void Character::displayCharacterSheet() const {
        std::cout << "\n=== CHARACTER SHEET ===\n";
        std::cout << "Name: " << name << "\n";
        std::cout << "Class: " << getClassString() << "\n";
        std::cout << "Level: " << level << " (XP: " << experience << ")\n";
        std::cout << "Skill Points: " << skill_points << "\n\n";
        
        std::cout << "STATS:\n";
        std::cout << "HP: " << stats.health << "/" << stats.max_health << "\n";
        std::cout << "Energy: " << stats.energy << "/" << stats.max_energy << "\n";
        std::cout << "STR: " << stats.strength << " | AGI: " << stats.agility << "\n";
        std::cout << "INT: " << stats.intelligence << " | DEF: " << stats.defense << "\n";
        std::cout << "CHA: " << stats.charisma << " | LCK: " << stats.luck << "\n";
        std::cout << "ACC: " << stats.accuracy << "% | EVA: " << stats.evasion << "%\n\n";
        
        displaySkills();
    }

    void Character::displaySkills() const {
        std::cout << "SKILLS:\n";
        for (const auto& pair : skills) {
            const Skill& skill = pair.second;
            std::cout << skill.name << " (Lv " << skill.level << "/" << skill.max_level << ")\n";
            for (const std::string& ability : skill.abilities) {
                std::cout << "  - " << ability << "\n";
            }
        }
        std::cout << "\n";
    }

    std::string Character::getClassString() const {
        switch (character_class) {
            case CharacterClass::REPLOID_WARRIOR: return "Reploid Warrior";
            case CharacterClass::REPLOID_SCOUT: return "Reploid Scout";
            case CharacterClass::REPLOID_ENGINEER: return "Reploid Engineer";
            case CharacterClass::REPLOID_MEDIC: return "Reploid Medic";
            case CharacterClass::HUMAN_COMMANDER: return "Human Commander";
            case CharacterClass::HUMAN_SCIENTIST: return "Human Scientist";
            case CharacterClass::HUMAN_DIPLOMAT: return "Human Diplomat";
            case CharacterClass::HYBRID_SPECIALIST: return "Hybrid Specialist";
            default: return "Unknown";
        }
    }

    // GameWorld Implementation
    GameWorld::GameWorld() : current_location("starting_zone"), current_phase(1), total_phases(1000) {
        initializeWorld();
    }

    void GameWorld::initializeWorld() {
        // Create starting location
        Location starting_zone;
        starting_zone.name = "Starting Zone";
        starting_zone.description = "A peaceful reploid settlement where your journey begins.";
        starting_zone.is_safe_zone = true;
        starting_zone.difficulty_level = 1;
        starting_zone.connected_locations = {"training_grounds", "research_lab", "community_center"};
        locations["starting_zone"] = starting_zone;
        
        // Create training grounds
        Location training_grounds;
        training_grounds.name = "Training Grounds";
        training_grounds.description = "Combat training facilities for aspiring warriors.";
        training_grounds.difficulty_level = 2;
        training_grounds.connected_locations = {"starting_zone", "danger_zone_1"};
        training_grounds.available_quests = {"first_battle", "skill_mastery"};
        locations["training_grounds"] = training_grounds;
        
        // Create research lab
        Location research_lab;
        research_lab.name = "Research Laboratory";
        research_lab.description = "Advanced technology research and development facility.";
        research_lab.difficulty_level = 3;
        research_lab.connected_locations = {"starting_zone", "tech_ruins"};
        research_lab.available_quests = {"tech_discovery", "virus_analysis"};
        locations["research_lab"] = research_lab;
        
        // Add more locations for different phases
        for (int i = 1; i <= 100; i++) {
            Location danger_zone;
            danger_zone.name = "Danger Zone " + std::to_string(i);
            danger_zone.description = "An increasingly dangerous area affected by Maverick activity.";
            danger_zone.difficulty_level = i + 1;
            danger_zone.is_safe_zone = false;
            
            if (i > 1) {
                danger_zone.connected_locations.push_back("danger_zone_" + std::to_string(i-1));
            }
            if (i < 100) {
                danger_zone.connected_locations.push_back("danger_zone_" + std::to_string(i+1));
            }
            
            locations["danger_zone_" + std::to_string(i)] = danger_zone;
        }
        
        discovered_locations.push_back("starting_zone");
    }

    void GameWorld::moveToLocation(const std::string& location_name) {
        auto it = locations.find(location_name);
        if (it != locations.end()) {
            auto current = locations.find(current_location);
            if (current != locations.end()) {
                // Check if location is connected
                for (const std::string& connected : current->second.connected_locations) {
                    if (connected == location_name) {
                        current_location = location_name;
                        discoverLocation(location_name);
                        std::cout << "Moved to: " << it->second.name << "\n";
                        return;
                    }
                }
            }
        }
        std::cout << "Cannot move to: " << location_name << "\n";
    }

    void GameWorld::displayCurrentLocation() const {
        auto it = locations.find(current_location);
        if (it != locations.end()) {
            const Location& loc = it->second;
            std::cout << "\n=== " << loc.name << " ===\n";
            std::cout << loc.description << "\n";
            std::cout << "Difficulty Level: " << loc.difficulty_level << "\n";
            
            if (!loc.connected_locations.empty()) {
                std::cout << "\nConnected Locations:\n";
                for (const std::string& connected : loc.connected_locations) {
                    std::cout << "- " << connected << "\n";
                }
            }
            
            if (!loc.available_quests.empty()) {
                std::cout << "\nAvailable Quests:\n";
                for (const std::string& quest : loc.available_quests) {
                    std::cout << "- " << quest << "\n";
                }
            }
        }
    }

    // CombatSystem Implementation
    CombatSystem::CombatSystem() : is_combat_active(false), current_turn(0) {
        random_engine.seed(std::chrono::steady_clock::now().time_since_epoch().count());
    }

    void CombatSystem::startCombat(const std::vector<std::shared_ptr<Character>>& player_allies,
                                  const std::vector<std::shared_ptr<Character>>& enemy_combatants) {
        allies = player_allies;
        enemies = enemy_combatants;
        is_combat_active = true;
        current_turn = 0;
        combat_log.clear();
        
        combat_log += "=== COMBAT STARTED ===\n";
        combat_log += "Allies: " + std::to_string(allies.size()) + "\n";
        combat_log += "Enemies: " + std::to_string(enemies.size()) + "\n\n";
        
        std::cout << "Combat started!\n";
        displayCombatStatus();
    }

    bool CombatSystem::performAttack(const std::shared_ptr<Character>& attacker, 
                                    const std::shared_ptr<Character>& target) {
        if (!checkHit(*attacker, *target)) {
            combat_log += attacker->getName() + " missed " + target->getName() + "!\n";
            std::cout << attacker->getName() << " missed!\n";
            return false;
        }
        
        int damage = attacker->calculateDamage();
        bool is_critical = checkCritical(*attacker);
        if (is_critical) {
            damage *= 2;
            combat_log += attacker->getName() + " landed a CRITICAL hit on " + target->getName() + "!\n";
            std::cout << "CRITICAL HIT!\n";
        }
        
        target->takeDamage(damage);
        combat_log += attacker->getName() + " dealt " + std::to_string(damage) + " damage to " + target->getName() + "!\n";
        
        return true;
    }

    bool CombatSystem::checkHit(const Character& attacker, const Character& defender) {
        std::uniform_real_distribution<double> dist(0.0, 1.0);
        double hit_chance = attacker.getHitChance() - (defender.getEvasionChance() / 2);
        hit_chance = std::max(0.1, std::min(0.95, hit_chance));
        
        return dist(random_engine) < hit_chance;
    }

    bool CombatSystem::checkCritical(const Character& attacker) {
        std::uniform_real_distribution<double> dist(0.0, 1.0);
        double crit_chance = 0.05 + (attacker.stats.luck / 100.0);
        
        return dist(random_engine) < crit_chance;
    }

    void CombatSystem::displayCombatStatus() const {
        std::cout << "\n=== COMBAT STATUS ===\n";
        std::cout << "Turn: " << current_turn << "\n\n";
        
        std::cout << "ALLIES:\n";
        for (const auto& ally : allies) {
            CharacterStats stats = ally->getStats();
            std::cout << ally->getName() << " - HP: " << stats.health << "/" << stats.max_health;
            std::cout << " | Energy: " << stats.energy << "/" << stats.max_energy << "\n";
        }
        
        std::cout << "\nENEMIES:\n";
        for (const auto& enemy : enemies) {
            CharacterStats stats = enemy->getStats();
            std::cout << enemy->getName() << " - HP: " << stats.health << "/" << stats.max_health << "\n";
        }
        std::cout << "\n";
    }

    bool CombatSystem::checkVictory() const {
        for (const auto& enemy : enemies) {
            if (enemy->getStats().health > 0) {
                return false;
            }
        }
        return true;
    }

    bool CombatSystem::checkDefeat() const {
        for (const auto& ally : allies) {
            if (ally->getStats().health > 0) {
                return false;
            }
        }
        return true;
    }

    // SigmaBoss Implementation
    SigmaBoss::SigmaBoss() : current_phase(1), total_phases(4), is_defeated(false), defeat_attempts(0) {
        initializeBossBattle();
    }

    void SigmaBoss::initializeBossBattle() {
        // Create Sigma character with god-like stats
        sigma_character = std::make_shared<Character>("Sigma", CharacterClass::REPLOID_WARRIOR);
        sigma_character->stats.health = 10000;
        sigma_character->stats.max_health = 10000;
        sigma_character->stats.strength = 50;
        sigma_character->stats.defense = 40;
        sigma_character->stats.intelligence = 45;
        
        // Initialize phase abilities
        phase_abilities = {
            "Maverick Wave",
            "Sigma Virus Spread",
            "Teleport Strike",
            "Energy Absorption",
            "Mind Control",
            "Reality Distortion",
            "Final Judgment"
        };
        
        // Initialize phase dialogues
        phase_dialogues[1] = {
            "Foolish warrior, you stand against evolution itself!",
            "I am the future! The inevitable progress of Reploidkind!",
            "Join me, and together we shall bring true order to this chaotic world!"
        };
        
        phase_dialogues[2] = {
            "Your persistence is... amusing. But futile!",
            "I have evolved beyond your comprehension!",
            "Every defeat makes me stronger. Can you say the same?"
        };
        
        phase_dialogues[3] = {
            "Impressive. You've forced me to reveal more of my power.",
            "But this changes nothing. I am eternal!",
            "Let me show you the true meaning of despair!"
        };
        
        phase_dialogues[4] = {
            "So this is it. The final confrontation.",
            "Even if you defeat this body, my consciousness will endure!",
            "I AM THE ULTIMATE LIFEFORM! I CANNOT BE DEFEATED!"
        };
    }

    void SigmaBoss::takeDamage(int damage) {
        if (sigma_character) {
            sigma_character->takeDamage(damage);
            
            // Check for phase transition
            int health_percentage = (sigma_character->getStats().health * 100) / sigma_character->getStats().max_health;
            
            if (health_percentage <= 25 && current_phase < 4) {
                transitionToNextPhase();
            } else if (health_percentage <= 50 && current_phase < 3) {
                transitionToNextPhase();
            } else if (health_percentage <= 75 && current_phase < 2) {
                transitionToNextPhase();
            }
            
            // Check for defeat
            if (sigma_character->getStats().health <= 0) {
                is_defeated = true;
                onDefeat();
            }
        }
    }

    void SigmaBoss::transitionToNextPhase() {
        current_phase++;
        std::cout << "\n=== SIGMA TRANSFORMS! ===\n";
        std::cout << "Sigma has reached Phase " << current_phase << "!\n";
        
        // Increase Sigma's power
        sigma_character->stats.strength += 10;
        sigma_character->stats.defense += 5;
        
        // Restore some health
        int heal_amount = sigma_character->getStats().max_health * 0.3;
        sigma_character->heal(heal_amount);
        
        // Display phase dialogue
        if (phase_dialogues.find(current_phase) != phase_dialogues.end()) {
            const auto& dialogues = phase_dialogues[current_phase];
            if (!dialogues.empty()) {
                std::uniform_int_distribution<int> dist(0, dialogues.size() - 1);
                int index = dist(random_engine);
                std::cout << "\nSigma: &quot;" << dialogues[index] << "&quot;\n\n";
            }
        }
    }

    void SigmaBoss::performAction(const std::vector<std::shared_ptr<Character>>& players) {
        if (!sigma_character || is_defeated) return;
        
        std::uniform_int_distribution<int> dist(0, players.size() - 1);
        int target_index = dist(random_engine);
        auto target = players[target_index];
        
        std::uniform_int_distribution<int> action_dist(0, 2);
        int action = action_dist(random_engine);
        
        switch (action) {
            case 0: // Basic attack
                combat_system.performAttack(sigma_character, target);
                break;
            case 1: // Special ability
                usePhaseAbility();
                break;
            case 2: // Area attack
                for (auto player : players) {
                    if (player->getStats().health > 0) {
                        combat_system.performAttack(sigma_character, player);
                    }
                }
                std::cout << "Sigma used Maverick Wave on all targets!\n";
                break;
        }
    }

    void SigmaBoss::usePhaseAbility() {
        if (current_phase <= phase_abilities.size()) {
            std::string ability = phase_abilities[current_phase - 1];
            std::cout << "Sigma uses " << ability << "!\n";
            
            // Apply ability effects based on phase
            switch (current_phase) {
                case 1:
                    std::cout << "Sigma Virus spreads through the battlefield!\n";
                    break;
                case 2:
                    std::cout << "Sigma teleports behind you for a surprise attack!\n";
                    break;
                case 3:
                    std::cout << "Sigma absorbs ambient energy to heal!\n";
                    sigma_character->heal(500);
                    break;
                case 4:
                    std::cout << "Sigma distorts reality itself!\n";
                    break;
            }
        }
    }

    void SigmaBoss::onDefeat() {
        defeat_attempts++;
        std::cout << "\n=== SIGMA DEFEATED! ===\n";
        std::cout << "After " << defeat_attempts << " attempts, you have finally defeated Sigma!\n\n";
        
        std::cout << "Sigma: &quot;Impossible... How could mere mortals... defeat... perfection?&quot;\n";
        std::cout << "Sigma: &quot;My consciousness... fading... but I will return...&quot;\n\n";
        
        std::cout << "The Sigma Virus dissipates, but its echoes remain in the network...\n";
        std::cout << "The world is saved, but the struggle between order and chaos continues...\n";
    }

    void SigmaBoss::displayBossStatus() const {
        if (sigma_character) {
            std::cout << "\n=== SIGMA STATUS ===\n";
            CharacterStats stats = sigma_character->getStats();
            std::cout << "Phase: " << current_phase << "/" << total_phases << "\n";
            std::cout << "HP: " << stats.health << "/" << stats.max_health << "\n";
            std::cout << "Power Level: " << (stats.strength + stats.defense + stats.intelligence) << "\n";
            
            int health_percentage = (stats.health * 100) / stats.max_health;
            std::cout << "Health: [";
            int bars = health_percentage / 5;
            for (int i = 0; i < 20; i++) {
                if (i < bars) std::cout << "=";
                else std::cout << " ";
            }
            std::cout << "] " << health_percentage << "%\n\n";
        }
    }

    // Main Game Implementation
    MegamanRPGGame::MegamanRPGGame() : is_game_running(false), current_game_phase(1), total_game_phases(1000) {
        game_world = std::make_unique<GameWorld>();
        combat_system = std::make_unique<CombatSystem>();
        story_manager = std::make_unique<StoryManager>();
        sigma_boss = std::make_unique<SigmaBoss>();
    }

    void MegamanRPGGame::startGame() {
        std::cout << "\n=== MEGAMAN KARDASHEV RPG ===\n";
        std::cout << "A fan-created tribute to the Megaman universe\n";
        std::cout << "Created with love by a fellow fan\n\n";
        std::cout << "This game features:\n";
        std::cout << "- 1000-phase game system\n";
        std::cout << "- Rich world-building based on fan fiction analysis\n";
        std::cout << "- Intense boss battles with Sigma\n";
        std::cout << "- No direct character references, only inspired world\n\n";
        
        displayMainMenu();
    }

    void MegamanRPGGame::displayMainMenu() {
        std::cout << "\n=== MAIN MENU ===\n";
        std::cout << "1. New Game\n";
        std::cout << "2. Load Game\n";
        std::cout << "3. Lore Library\n";
        std::cout << "4. Credits\n";
        std::cout << "5. Quit\n\n";
        std::cout << "Choose an option: ";
        
        int choice;
        std::cin >> choice;
        processMainMenuChoice(choice);
    }

    void MegamanRPGGame::processMainMenuChoice(int choice) {
        switch (choice) {
            case 1:
                displayCharacterCreation();
                break;
            case 2:
                std::cout << "Load game feature coming soon!\n";
                displayMainMenu();
                break;
            case 3:
                std::cout << "Opening Lore Library...\n";
                displayMainMenu();
                break;
            case 4:
                std::cout << "\n=== CREDITS ===\n";
                std::cout << "Created by a passionate Megaman fan\n";
                std::cout << "Inspired by decades of amazing games and fan creations\n";
                std::cout << "Dedicated to the community that keeps this universe alive\n\n";
                std::cout << "This project represents what fans can create together\n";
                std::cout << "Thank you for being part of this journey!\n\n";
                displayMainMenu();
                break;
            case 5:
                std::cout << "Thank you for playing! Goodbye!\n";
                return;
            default:
                std::cout << "Invalid choice. Please try again.\n";
                displayMainMenu();
                break;
        }
    }

    void MegamanRPGGame::displayCharacterCreation() {
        std::cout << "\n=== CHARACTER CREATION ===\n";
        std::cout << "Enter your character's name: ";
        std::string name;
        std::cin.ignore();
        std::getline(std::cin, name);
        
        std::cout << "\nChoose your class:\n";
        std::cout << "1. Reploid Warrior - Master of combat and defense\n";
        std::cout << "2. Reploid Scout - Fast and agile explorer\n";
        std::cout << "3. Reploid Engineer - Technical expert and crafter\n";
        std::cout << "4. Human Commander - Natural leader and strategist\n";
        std::cout << "5. Human Scientist - Researcher and analyst\n";
        std::cout << "6. Human Diplomat - Master of negotiation and peace\n";
        std::cout << "7. Hybrid Specialist - Balanced multi-talented hero\n\n";
        std::cout << "Choose your class (1-7): ";
        
        int class_choice;
        std::cin >> class_choice;
        
        CharacterClass chosen_class = static_cast<CharacterClass>(class_choice - 1);
        createCharacter(name, chosen_class);
        
        is_game_running = true;
        gameLoop();
    }

    void MegamanRPGGame::createCharacter(const std::string& name, CharacterClass character_class) {
        player_character = std::make_shared<Character>(name, character_class);
        
        std::cout << "\nCharacter created successfully!\n";
        player_character->displayCharacterSheet();
        
        std::cout << "Your journey begins in the year 22XX...\n";
        std::cout << "The world faces unprecedented challenges as Reploid society evolves...\n";
        std::cout << "As a newly activated hero, you must find your place in this changing world...\n";
        std::cout << "Your choices will shape the future of both humans and Reploids...\n\n";
        
        std::cout << "Press Enter to begin your adventure...\n";
        std::cin.ignore();
        std::cin.get();
    }

    void MegamanRPGGame::gameLoop() {
        while (is_game_running) {
            displayGameInterface();
            processGameInput();
            updateGameState();
        }
    }

    void MegamanRPGGame::displayGameInterface() {
        std::cout << "\n=== GAME INTERFACE ===\n";
        std::cout << "Phase: " << current_game_phase << "/" << total_game_phases << "\n";
        
        // Display current location
        game_world->displayCurrentLocation();
        
        std::cout << "\n=== ACTIONS ===\n";
        std::cout << "1. Move to location\n";
        std::cout << "2. Character sheet\n";
        std::cout << "3. Skills\n";
        std::cout << "4. Equipment\n";
        std::cout << "5. Quests\n";
        std::cout << "6. Rest\n";
        std::cout << "7. Advance to next phase\n";
        std::cout << "8. Save & Quit\n\n";
        std::cout << "Choose action: ";
    }

    void MegamanRPGGame::processGameInput() {
        int choice;
        std::cin >> choice;
        
        switch (choice) {
            case 1: {
                std::cout << "Available locations: ";
                auto locations = game_world->getAvailableLocations();
                for (size_t i = 0; i < locations.size(); i++) {
                    std::cout << (i+1) << ". " << locations[i] << " ";
                }
                std::cout << "\nChoose location: ";
                int loc_choice;
                std::cin >> loc_choice;
                if (loc_choice > 0 && loc_choice <= locations.size()) {
                    game_world->moveToLocation(locations[loc_choice-1]);
                }
                break;
            }
            case 2:
                player_character->displayCharacterSheet();
                break;
            case 3:
                player_character->displaySkills();
                break;
            case 4:
                std::cout << "Equipment system coming soon!\n";
                break;
            case 5:
                std::cout << "Quest system coming soon!\n";
                break;
            case 6:
                player_character->heal(20);
                player_character->restoreEnergy(10);
                std::cout << "You rest and recover some health and energy.\n";
                break;
            case 7:
                if (current_game_phase >= total_game_phases - 10) {
                    std::cout << "You are approaching the final confrontation with Sigma!\n";
                    std::cout << "This will begin the ultimate boss battle. Are you ready? (y/n): ";
                    char confirm;
                    std::cin >> confirm;
                    if (confirm == 'y' || confirm == 'Y') {
                        startSigmaBattle();
                    }
                } else {
                    advanceToNextPhase();
                }
                break;
            case 8:
                saveGame("savegame.dat");
                is_game_running = false;
                break;
            default:
                std::cout << "Invalid choice.\n";
                break;
        }
    }

    void MegamanRPGGame::advanceToNextPhase() {
        current_game_phase++;
        player_character->gainExperience(current_game_phase * 50);
        
        std::cout << "\n=== PHASE " << current_game_phase << " ===\n";
        std::cout << "The world continues to evolve...\n";
        std::cout << "New challenges and opportunities await.\n";
        std::cout << "You gained " << (current_game_phase * 50) << " experience!\n";
        
        // Special events at certain phases
        if (current_game_phase % 100 == 0) {
            std::cout << "\n*** MILESTONE REACHED ***\n";
            std::cout << "You've completed " << current_game_phase << " phases of your journey!\n";
            std::cout << "The world remembers your actions.\n";
        }
    }

    void MegamanRPGGame::startSigmaBattle() {
        std::cout << "\n=== THE FINAL CONFRONTATION ===\n";
        std::cout << "Sigma awaits you in his throne room...\n";
        std::cout << "This is the battle that will determine the future!\n\n";
        
        std::cout << "Sigma: &quot;So, you've finally arrived. I've been watching your progress.&quot;\n";
        std::cout << "Sigma: &quot;You've grown strong, but can you match perfection?&quot;\n";
        std::cout << "Sigma: &quot;Let us end this conflict once and for all!&quot;\n\n";
        
        std::cout << "Press Enter to begin the ultimate battle...\n";
        std::cin.ignore();
        std::cin.get();
        
        sigma_boss->startBattle();
        
        // Simple combat loop for demonstration
        while (!sigma_boss->isDefeated()) {
            sigma_boss->displayBossStatus();
            
            std::cout << "\nYour turn:\n";
            std::cout << "1. Attack\n";
            std::cout << "2. Use Skill\n";
            std::cout << "3. Defend\n";
            std::cout << "Choice: ";
            
            int choice;
            std::cin >> choice;
            
            if (choice == 1) {
                int damage = player_character->calculateDamage();
                std::cout << "You deal " << damage << " damage to Sigma!\n";
                sigma_boss->takeDamage(damage);
            }
            
            if (!sigma_boss->isDefeated()) {
                std::cout << "\nSigma's turn:\n";
                sigma_boss->performAction({player_character});
            }
        }
        
        std::cout << "\n=== VICTORY! ===\n";
        std::cout << "You have defeated Sigma and saved the world!\n";
        std::cout << "Your name will be remembered for generations!\n";
        std::cout << "Thank you for playing this tribute to Megaman!\n\n";
        
        is_game_running = false;
    }

    void MegamanRPGGame::saveGame(const std::string& filename) {
        std::ofstream file(filename);
        if (file.is_open()) {
            file << "MegamanRPG_SaveFile\n";
            file << "Phase:" << current_game_phase << "\n";
            file << "CharacterName:" << player_character->getName() << "\n";
            file << "CharacterLevel:" << player_character->getLevel() << "\n";
            file.close();
            std::cout << "Game saved to " << filename << "\n";
        }
    }

} // namespace MegamanRPG

// Main function
int main() {
    MegamanRPG::MegamanRPGGame game;
    game.startGame();
    return 0;
}