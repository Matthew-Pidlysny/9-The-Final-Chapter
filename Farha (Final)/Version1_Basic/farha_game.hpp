#ifndef FARHA_GAME_HPP
#define FARHA_GAME_HPP

#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <chrono>
#include <thread>
#include <random>

class FarhaGame {
private:
    struct Player {
        std::string name;
        std::string role; // "Caliph" or "Scholar"
        int knowledge_level;
        int speed;
        size_t territories_conquered;
        std::vector<std::string> learned_surahs;
        std::vector<std::string> learned_hadith;
        bool is_active;
    };
    
    struct Territory {
        std::string name;
        std::string historical_significance;
        std::string educational_content;
        int difficulty_level;
        bool conquered;
    };
    
    struct Battle {
        std::string name;
        std::string year;
        std::string description;
        std::string educational_outcome;
        std::vector<std::string> questions;
        bool completed;
    };
    
    struct QuranicContent {
        std::string surah_name;
        std::string arabic_text;
        std::string english_translation;
        std::string child_explanation;
        std::string moral_lesson;
    };
    
    struct HadithContent {
        std::string text;
        std::string source;
        std::string explanation;
        std::string practical_application;
    };
    
    Player player1, player2;
    std::vector<Territory> territories;
    std::vector<Battle> historical_battles;
    std::vector<QuranicContent> quranic_verses;
    std::vector<HadithContent> hadith_collection;
    
    bool single_player_mode;
    bool game_completed;
    int current_turn;
    std::mt19937 rng;
    
    // Educational Content Database
    void initialize_quranic_content();
    void initialize_hadith_content();
    void initialize_territories();
    void initialize_historical_battles();
    
    // Game Mechanics
    void display_welcome();
    void setup_players();
    void display_game_board();
    void process_turn(Player& player);
    bool present_educational_challenge(Player& player);
    void process_territory_expansion(Player& player);
    void process_historical_battle(Player& player);
    void update_player_speed(Player& player);
    void display_progress();
    
    // Educational Functions
    void teach_4_qul(Player& player);
    void teach_hadith(Player& player);
    void teach_history(const std::string& topic);
    std::string generate_encouragement();
    
    // Visual Functions
    void display_ascii_art();
    void display_caliphate_map();
    void animate_progress(const std::string& message);
    
public:
    FarhaGame();
    void start_game();
    void play_single_player();
    void play_two_player();
    void complete_game();
    bool is_game_completed() const;
    
    // Educational Tools
    void quiz_player(Player& player);
    void provide_learning_bonuses(Player& player);
    
    ~FarhaGame();
};

#endif // FARHA_GAME_HPP