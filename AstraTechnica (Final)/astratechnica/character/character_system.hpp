#ifndef ASTRATECHNICA_CHARACTER_SYSTEM_HPP
#define ASTRATECHNICA_CHARACTER_SYSTEM_HPP

// Forward declaration to avoid circular dependency
namespace AstraTechnica {
    class GameEngine;
}
#include <vector>
#include <map>
#include <memory>

namespace AstraTechnica {

    // Character definitions from document
    enum class CharacterType {
        COL_MILES_OBRIEN,
        YOUSEF_FELDTSTEIN,
        SHERRY_LORNE,
        DEBORAH_CASUNAGA,
        JOHNATHAN_SAVWORTHY
    };
    
    // Character data structure
    struct CharacterData {
        CharacterType type;
        std::string name;
        std::string handle;
        std::string location;
        std::string description;
        std::string ambition;
        
        std::map<std::string, int> base_stats;
        std::vector<std::string> starting_assets;
        std::vector<std::string> starting_items;
        
        double starting_money = 0.0;
        int starting_hunger = 0;
        bool has_crew = false;
        std::vector<std::map<std::string, std::string>> crew_members;
        
        std::map<std::string, int> relationships;
    };
    
    // Character class
    class Character {
    private:
        CharacterData data;
        CharacterStats current_stats;
        std::string current_location;
        std::vector<AssetToken> owned_assets;
        double money = 0.0;
        int hunger = 0;
        bool is_alive = true;
        
        // Position on map board
        int map_x = 0;
        int map_y = 0;
        std::string current_map_board = "domicile";
        
    public:
        Character(const CharacterData& initial_data);
        ~Character() = default;
        
        // Character management
        void initialize_from_type(CharacterType type);
        void update_location(const std::string& new_location, int x, int y);
        void move_unit(int dx, int dy);
        
        // Stats management
        void modify_stat(const std::string& stat_name, int value);
        int get_stat(const std::string& stat_name) const;
        std::map<std::string, int> get_all_stats() const { return current_stats; }
        
        // Asset management
        void add_asset(const std::string& token);
        void remove_asset(const std::string& token);
        bool has_asset(const std::string& token) const;
        const std::vector<std::string>& get_assets() const { return owned_assets; }
        
        // Money and hunger
        void add_money(double amount);
        bool spend_money(double amount);
        double get_money() const { return money; }
        void modify_hunger(int amount);
        int get_hunger() const { return hunger; }
        
        // Crew management
        void add_crew_member(const CrewMember& member);
        void remove_crew_member(const std::string& handle);
        const std::vector<CrewMember>& get_crew() const { return data.crew_members; }
        
        // Life status
        void set_alive(bool status) { is_alive = status; }
        bool get_alive() const { return is_alive; }
        
        // Accessors
        const CharacterData& get_data() const { return data; }
        const std::string& get_name() const { return data.name; }
        const std::string& get_handle() const { return data.handle; }
        CharacterType get_type() const { return data.type; }
        int get_map_x() const { return map_x; }
        int get_map_y() const { return map_y; }
        const std::string& get_current_map_board() const { return current_map_board; }
        
        // Actions
        bool can_perform_action(const std::string& action) const;
        void perform_action(const std::string& action);
        
        // Character-specific abilities
        void use_special_ability();
        bool can_hack() const;
        bool can_invest() const;
        bool can_start_company() const;
        
        // Serialization
        std::string serialize() const;
        bool deserialize(const std::string& data);
    };
    
    // Character factory
    class CharacterFactory {
    private:
        static std::map<CharacterType, CharacterData> character_templates;
        static bool templates_initialized;
        
    public:
        static void initialize_templates();
        static std::unique_ptr<Character> create_character(CharacterType type);
        static std::unique_ptr<Character> create_character(const std::string& character_name);
        static std::vector<CharacterType> get_available_characters();
        static const CharacterData& get_character_template(CharacterType type);
    };
    
    // Character progression system
    class CharacterProgression {
    private:
        Character* character;
        std::vector<std::string> learned_skills;
        int experience_points = 0;
        int level = 1;
        
    public:
        explicit CharacterProgression(Character* char_ptr);
        
        void gain_experience(int points);
        void level_up();
        void learn_skill(const std::string& skill);
        bool has_skill(const std::string& skill) const;
        
        int get_experience() const { return experience_points; }
        int get_level() const { return level; }
        const std::vector<std::string>& get_skills() const { return learned_skills; }
        
        void apply_level_bonuses();
        void check_skill_prerequisites(const std::string& action);
    };
    
} // namespace AstraTechnica

#endif // ASTRATECHNICA_CHARACTER_SYSTEM_HPP