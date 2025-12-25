#include "character_system.hpp"
#include <iostream>
#include <sstream>
#include <algorithm>

namespace AstraTechnica {

    // Initialize static member
    std::map<CharacterType, CharacterData> CharacterFactory::character_templates;
    bool CharacterFactory::templates_initialized = false;

    // Character Factory Implementation
    void CharacterFactory::initialize_templates() {
        if (templates_initialized) return;
        
        // Col. Miles O'Brien [@Looper]
        CharacterData obrien;
        obrien.type = CharacterType::COL_MILES_OBRIEN;
        obrien.name = "Col. Miles O'Brien";
        obrien.handle = "@Looper";
        obrien.location = "Fort George G. Meade residential area";
        obrien.description = "NSA agent in charge of assisting with the Director of the agency in the Cyber Command.";
        obrien.ambition = "Excel in cyber operations and maintain his mining operation.";
        
        obrien.base_stats = {
            .intelligence = 85, .literacy = 75, .rationale = 80, .science = 70, .mathematics = 80,
            .obesity = 20, .wounds = 0, .happiness = 70, .entertainment = 60, .depression = 15,
            .stubbornness = 60,
            .legacy_hardware = 60, .modern_hardware = 75, .mobile_hardware = 65,
            .coding_protocols = 90, .network_configurations = 85, .server_management = 80,
            .virus_technology = 70, .laws_regulations = 85, .dark_web_knowledge = 60,
            .firewall_vpn_knowledge = 80, .hacker_techniques = 75
        };
        
        obrien.starting_assets = {
            AssetToken::VEHICLE, AssetToken::TV, AssetToken::COMPUTER, AssetToken::LAPTOP,
            AssetToken::AI_ASSISTANT, AssetToken::PRINTER, AssetToken::SMARTPHONE
        };
        
        obrien.starting_items = {"Car", "TV", "Computer", "Laptop", "AI Assistant", "Printer", "Smartphone"};
        obrien.starting_money = 50000.0;
        obrien.starting_hunger = 10; // Little hunger
        obrien.has_crew = true;
        
        CrewMember herbert;
        herbert.name = "Lt. Herbert Stimreck";
        herbert.handle = "Herbert";
        herbert.threat_rating = 3;
        herbert.spirit = 3;
        herbert.action = 4;
        herbert.health = 4;
        herbert.skill = 3;
        herbert.unity = 4;
        obrien.crew_members.push_back(herbert);
        
        // Yousef Feldtstein [@GrumpyDad76]
        CharacterData yousef;
        yousef.type = CharacterType::YOUSEF_FELDTSTEIN;
        yousef.name = "Yousef Feldtstein";
        yousef.handle = "@GrumpyDad76";
        yousef.location = "Long Island, New York City";
        yousef.description = "Jewish man working for Nexus Cybersecurity Agency, jack of all trades specializing in Project Management.";
        yousef.ambition = "Express his project management skills to the fullest.";
        
        yousef.base_stats = {
            .intelligence = 80, .literacy = 85, .rationale = 90, .science = 65, .mathematics = 75,
            .obesity = 35, .wounds = 0, .happiness = 80, .entertainment = 85, .depression = 10,
            .stubbornness = 40,
            .legacy_hardware = 70, .modern_hardware = 80, .mobile_hardware = 75,
            .coding_protocols = 75, .network_configurations = 80, .server_management = 70,
            .virus_technology = 50, .laws_regulations = 75, .dark_web_knowledge = 40,
            .firewall_vpn_knowledge = 75, .hacker_techniques = 55
        };
        
        yousef.starting_assets = {
            AssetToken::VEHICLE, AssetToken::TV, AssetToken::TV, AssetToken::TV,
            AssetToken::MOVIE_PLAYER, AssetToken::GAME_SYSTEM, AssetToken::GAME_SYSTEM,
            AssetToken::SECURITY_CAMERA, AssetToken::SECURITY_CAMERA, AssetToken::SECURITY_CAMERA,
            AssetToken::COMPUTER, AssetToken::COMPUTER, AssetToken::COMPUTER,
            AssetToken::LAPTOP, AssetToken::LAPTOP, AssetToken::SMARTPHONE, AssetToken::SMARTPHONE,
            AssetToken::SMARTPHONE, AssetToken::SERVER, AssetToken::PRINTER,
            AssetToken::SECURITY_CAMERA // Home Internet Security Device represented as additional camera
        };
        
        yousef.starting_items = {"Car", "3 TV's", "Movie Player", "2 Game Consoles", "6 Security Cameras",
                                  "3 Computers", "2 Laptops", "3 Smartphones", "Rolex Watch", "Server", "Printer", 
                                  "Home Internet Security Device"};
        yousef.starting_money = 75000.0;
        yousef.starting_hunger = 0; // Not hungry at all
        yousef.has_crew = true;
        
        CrewMember shiloh;
        shiloh.name = "Shiloh Feldtstein";
        shiloh.handle = "Shiloh";
        shiloh.threat_rating = 2;
        shiloh.spirit = 3;
        shiloh.action = 3;
        shiloh.health = 4;
        shiloh.skill = 3;
        shiloh.unity = 4;
        yousef.crew_members.push_back(shiloh);
        
        // Sherry Lorne [@FeliciaX]
        CharacterData sherry;
        sherry.type = CharacterType::SHERRY_LORNE;
        sherry.name = "Sherry Lorne";
        sherry.handle = "@FeliciaX";
        sherry.location = "Southeast LA";
        sherry.description = "Woman who works at a Grocery Store, skilled in Cybersecurity, offers white hat hacking services.";
        sherry.ambition = "Develop a real Cybersecurity firm.";
        
        sherry.base_stats = {
            .intelligence = 75, .literacy = 80, .rationale = 70, .science = 60, .mathematics = 65,
            .obesity = 25, .wounds = 0, .happiness = 65, .entertainment = 55, .depression = 25,
            .stubbornness = 50,
            .legacy_hardware = 65, .modern_hardware = 85, .mobile_hardware = 70,
            .coding_protocols = 80, .network_configurations = 85, .server_management = 90,
            .virus_technology = 85, .laws_regulations = 60, .dark_web_knowledge = 70,
            .firewall_vpn_knowledge = 90, .hacker_techniques = 85
        };
        
        sherry.starting_assets = {
            AssetToken::VEHICLE, AssetToken::TV, AssetToken::COMPUTER, AssetToken::COMPUTER,
            AssetToken::SERVER, AssetToken::SERVER, AssetToken::SERVER, AssetToken::MINING_RIG,
            AssetToken::LAPTOP, AssetToken::SMARTPHONE
        };
        
        sherry.starting_items = {"Car", "TV", "2 Computers", "3 Servers", "1 Mining Rig", "1 Laptop", "1 Smartphone"};
        sherry.starting_money = 35000.0;
        sherry.starting_hunger = 40; // Moderate hunger
        sherry.has_crew = false;
        
        // Deborah Casunaga [@RealDebCas]
        CharacterData deborah;
        deborah.type = CharacterType::DEBORAH_CASUNAGA;
        deborah.name = "Deborah Casunaga";
        deborah.handle = "@RealDebCas";
        deborah.location = "Atlanta, Georgia";
        deborah.description = "Famous owner of Beta Company which runs social media platform, visits government often.";
        deborah.ambition = "Global aspirations for a new company while managing current job.";
        
        deborah.base_stats = {
            .intelligence = 85, .literacy = 90, .rationale = 80, .science = 55, .mathematics = 60,
            .obesity = 30, .wounds = 0, .happiness = 55, .entertainment = 60, .depression = 35,
            .stubbornness = 55,
            .legacy_hardware = 60, .modern_hardware = 70, .mobile_hardware = 65,
            .coding_protocols = 65, .network_configurations = 70, .server_management = 60,
            .virus_technology = 45, .laws_regulations = 85, .dark_web_knowledge = 30,
            .firewall_vpn_knowledge = 70, .hacker_techniques = 50
        };
        
        deborah.starting_assets = {
            AssetToken::VEHICLE, AssetToken::TV, AssetToken::MOVIE_PLAYER, AssetToken::LAPTOP,
            AssetToken::COMPUTER, AssetToken::PRINTER, AssetToken::SECURITY_CAMERA, AssetToken::SMARTPHONE
        };
        
        deborah.starting_items = {"Car", "TV", "Movie Player", "Laptop", "Computer", "Printer", 
                                  "Security Camera", "Smartphone"};
        deborah.starting_money = 100000.0;
        deborah.starting_hunger = 20; // Not very hungry
        deborah.has_crew = false;
        
        // Johnathan Savworthy [@Diablo1]
        CharacterData johnathan;
        johnathan.type = CharacterType::JOHNATHAN_SAVWORTHY;
        johnathan.name = "Johnathan Savworthy";
        johnathan.handle = "@Diablo1";
        johnathan.location = "Stamford, Connecticut";
        johnathan.description = "Hacker extraordinaire, pirates personal information, locks out computers.";
        johnathan.ambition = "Maintain hacking operations and expand influence.";
        
        johnathan.base_stats = {
            .intelligence = 70, .literacy = 65, .rationale = 60, .science = 45, .mathematics = 55,
            .obesity = 40, .wounds = 0, .happiness = 60, .entertainment = 70, .depression = 20,
            .stubbornness = 75,
            .legacy_hardware = 80, .modern_hardware = 75, .mobile_hardware = 70,
            .coding_protocols = 85, .network_configurations = 90, .server_management = 85,
            .virus_technology = 95, .laws_regulations = 40, .dark_web_knowledge = 95,
            .firewall_vpn_knowledge = 80, .hacker_techniques = 95
        };
        
        johnathan.starting_assets = {
            AssetToken::BIKE, AssetToken::COMPUTER, AssetToken::COMPUTER, AssetToken::COMPUTER, AssetToken::COMPUTER,
            AssetToken::SERVER, AssetToken::SERVER, AssetToken::SERVER, AssetToken::SERVER, AssetToken::SERVER,
            AssetToken::SECURITY_CAMERA, AssetToken::SECURITY_CAMERA, AssetToken::PRINTER,
            AssetToken::LAPTOP, AssetToken::LAPTOP, AssetToken::SMARTPHONE, AssetToken::SMARTPHONE, AssetToken::SMARTPHONE
        };
        
        johnathan.starting_items = {"Bike", "4 Computers", "5 Servers", "Home Internet Security Device", 
                                    "2 Security Cameras", "Printer", "2 Laptops", "3 Smartphones"};
        johnathan.starting_money = 25000.0;
        johnathan.starting_hunger = 80; // Very hungry
        johnathan.has_crew = true;
        
        CrewMember candyman;
        candyman.name = "@Candyman";
        candyman.handle = "@Candyman";
        candyman.threat_rating = 4;
        candyman.spirit = 3;
        candyman.action = 4;
        candyman.health = 3;
        candyman.skill = 4;
        candyman.unity = 3;
        johnathan.crew_members.push_back(candyman);
        
        CrewMember crookshank;
        crookshank.name = "@Crookshank";
        crookshank.handle = "@Crookshank";
        crookshank.threat_rating = 3;
        crookshank.spirit = 4;
        crookshank.action = 3;
        crookshank.health = 4;
        crookshank.skill = 3;
        crookshank.unity = 3;
        johnathan.crew_members.push_back(crookshank);
        
        CrewMember misfit;
        misfit.name = "@Misfit334";
        misfit.handle = "@Misfit334";
        misfit.threat_rating = 3;
        misfit.spirit = 3;
        misfit.action = 4;
        misfit.health = 3;
        misfit.skill = 3;
        misfit.unity = 2;
        johnathan.crew_members.push_back(misfit);
        
        CrewMember kitten;
        kitten.name = "@KittenLauncherXD";
        kitten.handle = "@KittenLauncherXD";
        kitten.threat_rating = 2;
        kitten.spirit = 4;
        kitten.action = 3;
        kitten.health = 4;
        kitten.skill = 2;
        kitten.unity = 3;
        johnathan.crew_members.push_back(kitten);
        
        // Store templates
        character_templates[CharacterType::COL_MILES_OBRIEN] = obrien;
        character_templates[CharacterType::YOUSEF_FELDTSTEIN] = yousef;
        character_templates[CharacterType::SHERRY_LORNE] = sherry;
        character_templates[CharacterType::DEBORAH_CASUNAGA] = deborah;
        character_templates[CharacterType::JOHNATHAN_SAVWORTHY] = johnathan;
        
        templates_initialized = true;
    }
    
    std::unique_ptr<Character> CharacterFactory::create_character(CharacterType type) {
        initialize_templates();
        
        auto it = character_templates.find(type);
        if (it != character_templates.end()) {
            return std::make_unique<Character>(it->second);
        }
        
        return nullptr;
    }
    
    std::unique_ptr<Character> CharacterFactory::create_character(const std::string& character_name) {
        initialize_templates();
        
        if (character_name == "Col. Miles O'Brien" || character_name == "Looper") {
            return create_character(CharacterType::COL_MILES_OBRIEN);
        } else if (character_name == "Yousef Feldtstein" || character_name == "GrumpyDad76") {
            return create_character(CharacterType::YOUSEF_FELDTSTEIN);
        } else if (character_name == "Sherry Lorne" || character_name == "FeliciaX") {
            return create_character(CharacterType::SHERRY_LORNE);
        } else if (character_name == "Deborah Casunaga" || character_name == "RealDebCas") {
            return create_character(CharacterType::DEBORAH_CASUNAGA);
        } else if (character_name == "Johnathan Savworthy" || character_name == "Diablo1") {
            return create_character(CharacterType::JOHNATHAN_SAVWORTHY);
        }
        
        return nullptr;
    }
    
    std::vector<CharacterType> CharacterFactory::get_available_characters() {
        initialize_templates();
        
        std::vector<CharacterType> types;
        for (const auto& pair : character_templates) {
            types.push_back(pair.first);
        }
        return types;
    }
    
    const CharacterData& CharacterFactory::get_character_template(CharacterType type) {
        initialize_templates();
        return character_templates.at(type);
    }
    
    // Character Implementation
    Character::Character(const CharacterData& initial_data) : data(initial_data) {
        current_stats = initial_data.base_stats;
        owned_assets = initial_data.starting_assets;
        money = initial_data.starting_money;
        hunger = initial_data.starting_hunger;
        current_location = initial_data.location;
    }
    
    void Character::initialize_from_type(CharacterType type) {
        CharacterFactory factory;
        auto template_data = factory.get_character_template(type);
        data = template_data;
        current_stats = template_data.base_stats;
        owned_assets = template_data.starting_assets;
        money = template_data.starting_money;
        hunger = template_data.starting_hunger;
        current_location = template_data.location;
    }
    
    void Character::modify_stat(const std::string& stat_name, int value) {
        if (stat_name == "intelligence") current_stats.intelligence += value;
        else if (stat_name == "literacy") current_stats.literacy += value;
        else if (stat_name == "rationale") current_stats.rationale += value;
        else if (stat_name == "science") current_stats.science += value;
        else if (stat_name == "mathematics") current_stats.mathematics += value;
        else if (stat_name == "obesity") current_stats.obesity += value;
        else if (stat_name == "wounds") current_stats.wounds += value;
        else if (stat_name == "happiness") current_stats.happiness += value;
        else if (stat_name == "entertainment") current_stats.entertainment += value;
        else if (stat_name == "depression") current_stats.depression += value;
        else if (stat_name == "stubbornness") current_stats.stubbornness += value;
        else if (stat_name == "legacy_hardware") current_stats.legacy_hardware += value;
        else if (stat_name == "modern_hardware") current_stats.modern_hardware += value;
        else if (stat_name == "mobile_hardware") current_stats.mobile_hardware += value;
        else if (stat_name == "coding_protocols") current_stats.coding_protocols += value;
        else if (stat_name == "network_configurations") current_stats.network_configurations += value;
        else if (stat_name == "server_management") current_stats.server_management += value;
        else if (stat_name == "virus_technology") current_stats.virus_technology += value;
        else if (stat_name == "laws_regulations") current_stats.laws_regulations += value;
        else if (stat_name == "dark_web_knowledge") current_stats.dark_web_knowledge += value;
        else if (stat_name == "firewall_vpn_knowledge") current_stats.firewall_vpn_knowledge += value;
        else if (stat_name == "hacker_techniques") current_stats.hacker_techniques += value;
        
        // Clamp values between 0 and 100
        current_stats.intelligence = std::clamp(current_stats.intelligence, 0, 100);
        current_stats.literacy = std::clamp(current_stats.literacy, 0, 100);
        current_stats.rationale = std::clamp(current_stats.rationale, 0, 100);
        current_stats.science = std::clamp(current_stats.science, 0, 100);
        current_stats.mathematics = std::clamp(current_stats.mathematics, 0, 100);
        current_stats.obesity = std::clamp(current_stats.obesity, 0, 100);
        current_stats.wounds = std::clamp(current_stats.wounds, 0, 100);
        current_stats.happiness = std::clamp(current_stats.happiness, 0, 100);
        current_stats.entertainment = std::clamp(current_stats.entertainment, 0, 100);
        current_stats.depression = std::clamp(current_stats.depression, 0, 100);
        current_stats.stubbornness = std::clamp(current_stats.stubbornness, 0, 100);
        current_stats.legacy_hardware = std::clamp(current_stats.legacy_hardware, 0, 100);
        current_stats.modern_hardware = std::clamp(current_stats.modern_hardware, 0, 100);
        current_stats.mobile_hardware = std::clamp(current_stats.mobile_hardware, 0, 100);
        current_stats.coding_protocols = std::clamp(current_stats.coding_protocols, 0, 100);
        current_stats.network_configurations = std::clamp(current_stats.network_configurations, 0, 100);
        current_stats.server_management = std::clamp(current_stats.server_management, 0, 100);
        current_stats.virus_technology = std::clamp(current_stats.virus_technology, 0, 100);
        current_stats.laws_regulations = std::clamp(current_stats.laws_regulations, 0, 100);
        current_stats.dark_web_knowledge = std::clamp(current_stats.dark_web_knowledge, 0, 100);
        current_stats.firewall_vpn_knowledge = std::clamp(current_stats.firewall_vpn_knowledge, 0, 100);
        current_stats.hacker_techniques = std::clamp(current_stats.hacker_techniques, 0, 100);
    }
    
    int Character::get_stat(const std::string& stat_name) const {
        if (stat_name == "intelligence") return current_stats.intelligence;
        else if (stat_name == "literacy") return current_stats.literacy;
        else if (stat_name == "rationale") return current_stats.rationale;
        else if (stat_name == "science") return current_stats.science;
        else if (stat_name == "mathematics") return current_stats.mathematics;
        else if (stat_name == "obesity") return current_stats.obesity;
        else if (stat_name == "wounds") return current_stats.wounds;
        else if (stat_name == "happiness") return current_stats.happiness;
        else if (stat_name == "entertainment") return current_stats.entertainment;
        else if (stat_name == "depression") return current_stats.depression;
        else if (stat_name == "stubbornness") return current_stats.stubbornness;
        else if (stat_name == "legacy_hardware") return current_stats.legacy_hardware;
        else if (stat_name == "modern_hardware") return current_stats.modern_hardware;
        else if (stat_name == "mobile_hardware") return current_stats.mobile_hardware;
        else if (stat_name == "coding_protocols") return current_stats.coding_protocols;
        else if (stat_name == "network_configurations") return current_stats.network_configurations;
        else if (stat_name == "server_management") return current_stats.server_management;
        else if (stat_name == "virus_technology") return current_stats.virus_technology;
        else if (stat_name == "laws_regulations") return current_stats.laws_regulations;
        else if (stat_name == "dark_web_knowledge") return current_stats.dark_web_knowledge;
        else if (stat_name == "firewall_vpn_knowledge") return current_stats.firewall_vpn_knowledge;
        else if (stat_name == "hacker_techniques") return current_stats.hacker_techniques;
        return 0;
    }
    
    void Character::add_asset(AssetToken token) {
        owned_assets.push_back(token);
    }
    
    void Character::remove_asset(AssetToken token) {
        auto it = std::find(owned_assets.begin(), owned_assets.end(), token);
        if (it != owned_assets.end()) {
            owned_assets.erase(it);
        }
    }
    
    bool Character::has_asset(AssetToken token) const {
        return std::find(owned_assets.begin(), owned_assets.end(), token) != owned_assets.end();
    }
    
    void Character::add_money(double amount) {
        money += amount;
        if (amount > 0) {
            modify_stat("happiness", std::min(5, static_cast<int>(amount / 1000)));
        }
    }
    
    bool Character::spend_money(double amount) {
        if (money >= amount) {
            money -= amount;
            return true;
        }
        return false;
    }
    
    void Character::modify_hunger(int amount) {
        hunger += amount;
        hunger = std::clamp(hunger, 0, 100);
    }
    
    void Character::add_crew_member(const CrewMember& member) {
        data.crew_members.push_back(member);
    }
    
    void Character::remove_crew_member(const std::string& handle) {
        auto it = std::remove_if(data.crew_members.begin(), data.crew_members.end(),
                                [&handle](const CrewMember& member) {
                                    return member.handle == handle;
                                });
        data.crew_members.erase(it, data.crew_members.end());
    }
    
    void Character::update_location(const std::string& new_location, int x, int y) {
        current_location = new_location;
        map_x = x;
        map_y = y;
    }
    
    void Character::move_unit(int dx, int dy) {
        map_x += dx;
        map_y += dy;
    }
    
    bool Character::can_perform_action(const std::string& action) const {
        if (action == "hack") return current_stats.hacker_techniques >= 50;
        if (action == "code") return current_stats.coding_protocols >= 60;
        if (action == "manage_servers") return current_stats.server_management >= 40;
        if (action == "investigate") return current_stats.intelligence >= 70;
        return true;
    }
    
    void Character::perform_action(const std::string& action) {
        if (!can_perform_action(action)) {
            modify_stat("depression", 5);
            return;
        }
        
        modify_stat("happiness", 10);
        modify_stat("entertainment", 5);
    }
    
    void Character::use_special_ability() {
        switch (data.type) {
            case CharacterType::COL_MILES_OBRIEN:
                // NSA agent abilities
                modify_stat("laws_regulations", 10);
                break;
            case CharacterType::YOUSEF_FELDTSTEIN:
                // Project management bonus
                modify_stat("rationale", 15);
                break;
            case CharacterType::SHERRY_LORNE:
                // Cybersecurity expert
                modify_stat("firewall_vpn_knowledge", 15);
                break;
            case CharacterType::DEBORAH_CASUNAGA:
                // Business acumen
                add_money(10000);
                break;
            case CharacterType::JOHNATHAN_SAVWORTHY:
                // Hacker abilities
                modify_stat("dark_web_knowledge", 20);
                break;
        }
    }
    
    bool Character::can_hack() const {
        return current_stats.hacker_techniques >= 60;
    }
    
    bool Character::can_invest() const {
        return money >= 10000 && current_stats.intelligence >= 70;
    }
    
    bool Character::can_start_company() const {
        return money >= 25000 && current_stats.rationale >= 50;
    }
    
    std::string Character::serialize() const {
        std::ostringstream oss;
        oss << data.name << "|" << data.handle << "|" << current_location << "|"
            << money << "|" << hunger << "|" << is_alive << "|" << map_x << "|" << map_y << "|"
            << current_map_board;
        return oss.str();
    }
    
    bool Character::deserialize(const std::string& data) {
        std::istringstream iss(data);
        std::string token;
        
        try {
            std::getline(iss, token, '|');
            // Parse and restore character data...
            return true;
        } catch (...) {
            return false;
        }
    }
    
    // CharacterProgression Implementation
    CharacterProgression::CharacterProgression(Character* char_ptr) : character(char_ptr) {
        
    }
    
    void CharacterProgression::gain_experience(int points) {
        experience_points += points;
        while (experience_points >= level * 100) {
            level_up();
        }
    }
    
    void CharacterProgression::level_up() {
        experience_points -= level * 100;
        level++;
        apply_level_bonuses();
    }
    
    void CharacterProgression::apply_level_bonuses() {
        if (character) {
            character->modify_stat("intelligence", 2);
            character->modify_stat("happiness", 5);
            character->add_money(1000 * level);
        }
    }
    
    void CharacterProgression::learn_skill(const std::string& skill) {
        if (std::find(learned_skills.begin(), learned_skills.end(), skill) == learned_skills.end()) {
            learned_skills.push_back(skill);
            
            // Apply skill bonuses
            if (skill == "advanced_hacking") {
                character->modify_stat("hacker_techniques", 15);
            } else if (skill == "project_management") {
                character->modify_stat("rationale", 10);
            } else if (skill == "cybersecurity") {
                character->modify_stat("firewall_vpn_knowledge", 15);
            }
        }
    }
    
    bool CharacterProgression::has_skill(const std::string& skill) const {
        return std::find(learned_skills.begin(), learned_skills.end(), skill) != learned_skills.end();
    }
    
    void CharacterProgression::check_skill_prerequisites(const std::string& action) {
        // Implementation for checking if character has required skills
    }
    
} // namespace AstraTechnica