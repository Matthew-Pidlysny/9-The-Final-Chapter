#include "farha_game.hpp"
#include <iostream>

int main() {
    std::cout << "\n🌟 FARHA - EDUCATIONAL CALIPHATE GAME 🌟\n";
    std::cout << "========================================\n\n";
    
    try {
        FarhaGame game;
        game.start_game();
        
        if (game.is_game_completed()) {
            std::cout << "\n🎉 Game completed successfully! 🎉\n";
        }
        
    } catch (const std::exception& e) {
        std::cerr << "\n❌ An error occurred: " << e.what() << std::endl;
        return 1;
    }
    
    return 0;
}