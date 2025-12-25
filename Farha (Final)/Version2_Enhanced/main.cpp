#include "farha_enhanced.hpp"
#include <iostream>

int main() {
    std::cout << "\n🌟 FARHA ENHANCED - AUTHENTIC ISLAMIC EDUCATION 🌟\n";
    std::cout << "=================================================\n\n";
    
    try {
        FarhaEnhanced enhanced_game;
        enhanced_game.start_enhanced_game();
        
        if (enhanced_game.is_enhanced_game_completed()) {
            std::cout << "\n🎉 Enhanced game completed successfully! 🎉\n";
        }
        
    } catch (const std::exception& e) {
        std::cerr << "\n❌ An error occurred: " << e.what() << std::endl;
        return 1;
    }
    
    return 0;
}