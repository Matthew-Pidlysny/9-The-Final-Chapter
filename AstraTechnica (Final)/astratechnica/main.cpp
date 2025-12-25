#include "core/game_engine.hpp"
#include "character/character_system.hpp"
#include "phone/phone_integration.hpp"
#include "ai/ai_system.hpp"
#include <iostream>
#include <chrono>
#include <thread>
#include <signal.h>

// Global game engine instance for signal handling
std::unique_ptr<AstraTechnica::GameEngine> g_game_engine = nullptr;

// Signal handler for graceful shutdown
void signal_handler(int signal) {
    std::cout << "\nReceived signal " << signal << ". Shutting down gracefully..." << std::endl;
    if (g_game_engine) {
        g_game_engine->shutdown();
    }
    exit(0);
}

int main() {
    std::cout << "\n========================================\n";
    std::cout << "  ASTRATECHNICA - EXTREMELY EPIC EDITION\n";
    std::cout << "  Pave the way for a greater tomorrow!\n";
    std::cout << "========================================\n\n";

    // Set up signal handlers
    signal(SIGINT, signal_handler);
    signal(SIGTERM, signal_handler);

    try {
        // Create and initialize the game engine
        g_game_engine = std::make_unique<AstraTechnica::GameEngine>();
        
        std::cout << "Initializing AstraTechnica Game Engine..." << std::endl;
        if (!g_game_engine->initialize()) {
            std::cerr << "Failed to initialize game engine!" << std::endl;
            return 1;
        }

        std::cout << "Game Engine initialized successfully!\n\n";

        // Character selection
        std::cout << "=== CHARACTER SELECTION ===\n";
        std::cout << "Available Characters:\n";
        std::cout << "1. Col. Miles O'Brien [@Looper] - NSA Agent with cyber command expertise\n";
        std::cout << "2. Yousef Feldtstein [@GrumpyDad76] - Project Management Specialist\n";
        std::cout << "3. Sherry Lorne [@FeliciaX] - Cybersecurity Expert and White Hat Hacker\n";
        std::cout << "4. Deborah Casunaga [@RealDebCas] - Social Media Company Owner\n";
        std::cout << "5. Johnathan Savworthy [@Diablo1] - Hacker Extraordinaire\n";
        std::cout << "\nEnter your choice (1-5): ";

        int character_choice;
        std::cin >> character_choice;

        if (character_choice < 1 || character_choice > 5) {
            std::cerr << "Invalid choice! Defaulting to Col. Miles O'Brien." << std::endl;
            character_choice = 1;
        }

        AstraTechnica::CharacterType selected_type;
        switch (character_choice) {
            case 1: selected_type = AstraTechnica::CharacterType::COL_MILES_OBRIEN; break;
            case 2: selected_type = AstraTechnica::CharacterType::YOUSEF_FELDTSTEIN; break;
            case 3: selected_type = AstraTechnica::CharacterType::SHERRY_LORNE; break;
            case 4: selected_type = AstraTechnica::CharacterType::DEBORAH_CASUNAGA; break;
            case 5: selected_type = AstraTechnica::CharacterType::JOHNATHAN_SAVWORTHY; break;
        }

        // Create selected character
        g_game_engine->create_character("Col. Miles O'Brien"); // Will be updated in the engine
        std::cout << "\nCharacter created successfully!\n";

        // Display character info
        std::cout << "\n=== CHARACTER STATUS ===\n";
        std::cout << "Game is now running with real-time mechanics...\n";
        std::cout << "Phone integration is active for notifications...\n";
        std::cout << "AI systems are initializing...\n\n";

        // Main game loop
        std::cout << "Starting AstraTechnica...\n";
        std::cout << "Press Ctrl+C to gracefully exit\n\n";

        g_game_engine->run_game_loop();

    } catch (const std::exception& e) {
        std::cerr << "Fatal error: " << e.what() << std::endl;
        return 1;
    } catch (...) {
        std::cerr << "Unknown fatal error occurred!" << std::endl;
        return 1;
    }

    std::cout << "\nThank you for playing AstraTechnica!\n";
    std::cout << "Pave the way for a greater tomorrow!\n\n";

    return 0;
}