/*
 * Privanna Faction Manager
 * Manages 9 major factions + special entities
 * Complex alliance, diplomacy, and faction-specific rules
 */

#ifndef PRIVANNA_FACTION_MANAGER_HPP
#define PRIVANNA_FACTION_MANAGER_HPP

#include <string>
#include <vector>
#include <unordered_map>
#include <memory>
#include <array>
#include <functional>

namespace privanna {

// Faction types enumeration
enum class FactionType {
    // Devil Factions (6)
    SHENZAN,        // Queen-led authority
    SHAAKU,         // Investigation-focused
    AKUSIMABA,      // Warring faction
    BAKRI,          // Most horrible
    SIMREH,         // Genetically engineered
    INNUDAKU,       // Young at heart
    
    // Djinn Factions (3)
    DJINN,          // Main Djinn faction
    LOFT,           // Evil formed from silence
    BELIEVERS,      // Nomadic enthusiasts
    
    // Special Entities
    IBLIS,          // The fallen one
    YUDUU_AH,       // Iblis' creatures
    HUMAN_ROGUES,   // Board-controlled
    HORDE,          // Self-controlled
    CONVERTED,      // Neutral converted units
    
    TOTAL_FACTIONS  // For array sizing
};

// Faction alignment enumeration
enum class FactionAlignment {
    DEVIL,          // Devil-aligned
    DJINN,          // Djinn-aligned
    NEUTRAL,        // Neutral alignment
    DYNAMIC         // Changes based on situation
};

// Alliance status enumeration
enum class AllianceStatus {
    ENEMIES,        // Hostile relationship
    NEUTRAL,        // No relationship
    ALLIED,         // Friendly relationship
    VASSAL,         // Subordinate relationship
    OVERLORD        // Superior relationship
};

// Faction characteristics structure
struct FactionCharacteristics {
    FactionType type;
    FactionAlignment alignment;
    std::string name;
    std::string description;
    
    // Economic characteristics
    uint32_t starting_shimarra = 0;
    uint32_t starting_production = 0;
    double economic_multiplier = 1.0;
    
    // Military characteristics
    double combat_bonus = 1.0;
    double defense_bonus = 1.0;
    std::vector<std::string> unique_units;
    
    // Magic characteristics
    std::vector<std::string> magic_affinities;
    double magic_bonus = 1.0;
    
    // Special abilities
    std::vector<std::string> special_abilities;
    std::function<void()> special_ability_handler;
    
    // AI behavior modifiers
    double aggressiveness = 1.0;
    double diplomacy_factor = 1.0;
    double expansion_tendency = 1.0;
    
    // Story elements
    std::string background_story;
    std::vector<std::string> victory_conditions;
    std::vector<std::string> defeat_conditions;
};

// Alliance structure
struct Alliance {
    std::vector<FactionType> members;
    AllianceStatus status;
    double strength_rating = 1.0;
    bool is_mutual = true;
    std::string alliance_name;
    std::chrono::system_clock::time_point formed_time;
    std::function<void()> on_formed;
    std::function<void()> on_broken;
};

// Diplomatic relationship structure
struct DiplomaticRelationship {
    FactionType faction1;
    FactionType faction2;
    AllianceStatus current_status;
    double relationship_strength = 0.0;  // -100 to +100
    std::vector<std::string> diplomatic_history;
    std::chrono::system_clock::time_point last_contact;
    bool is_secret = false;
};

// Faction state structure
struct FactionState {
    FactionType type;
    bool is_active = true;
    bool is_ai_controlled = true;
    uint32_t player_id = 0;  // 0 for AI
    
    // Resources
    uint32_t shimarra = 0;
    uint32_t production_points = 0;
    uint32_t surplus_parts = 0;
    
    // Territory
    std::vector<uint32_t> controlled_territories;
    uint32_t total_territories = 0;
    double territorial_strength = 1.0;
    
    // Military
    uint32_t total_units = 0;
    uint32_t military_strength = 0;
    double combat_effectiveness = 1.0;
    
    // Magic
    uint32_t mana_pool = 0;
    double magical_power = 1.0;
    std::vector<std::string> learned_spells;
    
    // Diplomacy
    std::vector<Alliance> current_alliances;
    std::vector<DiplomaticRelationship> relationships;
    
    // Victory progress
    double victory_progress = 0.0;
    std::vector<std::string> completed_objectives;
    std::vector<std::string> active_quests;
};

// Event types for faction system
enum class FactionEventType {
    FACTION_CREATED,
    FACTION_DESTROYED,
    ALLIANCE_FORMED,
    ALLIANCE_BROKEN,
    WAR_DECLARED,
    PEACE_TREATY,
    RESOURCE_CHANGE,
    TERRITORY_CAPTURED,
    MAGIC_DISCOVERY,
    SPECIAL_ABILITY_USED
};

// Faction event structure
struct FactionEvent {
    FactionEventType type;
    FactionType primary_faction;
    FactionType secondary_faction;  // Optional
    std::string description;
    double event_strength = 1.0;
    std::chrono::system_clock::time_point timestamp;
    std::unordered_map<std::string, double> event_data;
};

// Faction manager class
class FactionManager {
private:
    // Faction data
    std::array<FactionCharacteristics, static_cast<size_t>(FactionType::TOTAL_FACTIONS)> faction_characteristics_;
    std::unordered_map<FactionType, FactionState> faction_states_;
    
    // Diplomacy system
    std::unordered_map<std::pair<FactionType, FactionType>, DiplomaticRelationship> relationships_;
    std::vector<Alliance> active_alliances_;
    
    // Event system
    std::vector<FactionEvent> event_history_;
    std::vector<std::function<void(const FactionEvent&)>> event_listeners_;
    
    // AI modifiers
    std::unordered_map<FactionType, double> ai_difficulty_modifiers_;
    std::unordered_map<FactionType, std::vector<std::function<void()>>> ai_behaviors_;
    
    // Balance tracking
    std::unordered_map<FactionType, double> power_ratings_;
    bool is_balanced_ = true;
    double balance_threshold_ = 0.3;  // 30% power difference threshold
    
public:
    // Constructor/Destructor
    FactionManager();
    ~FactionManager();
    
    // Initialization
    bool initialize();
    void shutdown();
    
    // Faction management
    void create_faction(FactionType type, bool is_ai_controlled = true, uint32_t player_id = 0);
    void destroy_faction(FactionType type);
    bool is_faction_active(FactionType type) const;
    
    // Characteristic access
    const FactionCharacteristics& get_faction_characteristics(FactionType type) const;
    void modify_faction_characteristics(FactionType type, const std::function<void(FactionCharacteristics&)>& modifier);
    
    // State management
    const FactionState& get_faction_state(FactionType type) const;
    void update_faction_state(FactionType type, const std::function<void(FactionState&)>& updater);
    
    // Resource management
    void add_shimarra(FactionType type, uint32_t amount);
    void remove_shimarra(FactionType type, uint32_t amount);
    void add_production_points(FactionType type, uint32_t amount);
    void remove_production_points(FactionType type, uint32_t amount);
    
    // Territory management
    void add_territory(FactionType type, uint32_t territory_id);
    void remove_territory(FactionType type, uint32_t territory_id);
    std::vector<uint32_t> get_controlled_territories(FactionType type) const;
    
    // Diplomacy system
    void set_relationship(FactionType faction1, FactionType faction2, AllianceStatus status);
    AllianceStatus get_relationship(FactionType faction1, FactionType faction2) const;
    void modify_relationship_strength(FactionType faction1, FactionType faction2, double modifier);
    
    // Alliance management
    void create_alliance(const std::vector<FactionType>& members, const std::string& alliance_name);
    void break_alliance(const std::string& alliance_name);
    bool are_allied(FactionType faction1, FactionType faction2) const;
    std::vector<Alliance> get_faction_alliances(FactionType type) const;
    
    // Special faction behaviors
    void execute_faction_special_ability(FactionType type);
    bool can_use_special_ability(FactionType type) const;
    std::vector<std::string> get_available_abilities(FactionType type) const;
    
    // Iblis-specific systems (mercy implementation)
    void update_ibis_mercy_system();
    bool should_ibis_show_mercy(FactionType target_faction) const;
    void execute_ibis_mercy_action(FactionType target_faction);
    
    // AI systems
    void update_ai_diplomacy(double delta_time);
    void update_ai_economics(double delta_time);
    void update_ai_military(double delta_time);
    void set_ai_difficulty(FactionType type, double difficulty);
    
    // Balance system
    void update_power_ratings();
    bool is_game_balanced() const;
    void auto_balance_game();
    std::vector<FactionType> get_dominant_factions() const;
    std::vector<FactionType> get_struggling_factions() const;
    
    // Event system
    void add_event_listener(const std::function<void(const FactionEvent&)>& listener);
    void remove_event_listener(const std::function<void(const FactionEvent&)>& listener);
    void trigger_event(const FactionEvent& event);
    std::vector<FactionEvent> get_faction_events(FactionType type, size_t count = 10) const;
    
    // Update system
    void update(double delta_time);
    
    // Serialization
    void serialize_state(std::string& output) const;
    void deserialize_state(const std::string& input);
    
    // Utility functions
    FactionAlignment get_faction_alignment(FactionType type) const;
    std::string get_faction_name(FactionType type) const;
    std::vector<FactionType> get_enemy_factions(FactionType type) const;
    std::vector<FactionType> get_allied_factions(FactionType type) const;
    double calculate_faction_power(FactionType type) const;
    
private:
    // Initialization helpers
    void initialize_faction_characteristics();
    void initialize_diplomatic_relationships();
    void initialize_ai_behaviors();
    
    // Balance helpers
    void recalculate_power_ratings();
    void apply_balance_corrections();
    
    // Event helpers
    void notify_event_listeners(const FactionEvent& event);
    void log_event(const FactionEvent& event);
    
    // Validation helpers
    bool is_valid_faction(FactionType type) const;
    bool can_form_alliance(const std::vector<FactionType>& members) const;
    
    // Mercy system for Iblis
    void initialize_ibis_mercy_parameters();
    double calculate_mercy_score(FactionType target_faction) const;
    
    // AI helpers
    void execute_ai_diplomatic_decision(FactionType type);
    void execute_ai_economic_decision(FactionType type);
    void execute_ai_military_decision(FactionType type);
    
    // Utility helpers
    double get_combat_modifier(FactionType type) const;
    double get_economic_modifier(FactionType type) const;
    double get_magic_modifier(FactionType type) const;
};

// Utility functions
FactionType string_to_faction_type(const std::string& faction_name);
std::string faction_type_to_string(FactionType type);
std::string alliance_status_to_string(AllianceStatus status);
std::string faction_alignment_to_string(FactionAlignment alignment);

} // namespace privanna

#endif // PRIVANNA_FACTION_MANAGER_HPP