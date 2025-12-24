/*
 * Recipy - Grade 1 Mathematical Adventure
 * Main Entry Point
 * 
 * A loving, child-friendly introduction to advanced mathematical concepts
 * through loving, playful workshops and caring AI-powered learning adventures.
 */

#include <iostream>
#include <memory>
#include "RecipyApp.h"
#include "utils/ColorfulPrinter.h"

int main() {
    try {
        // Create colorful welcome message for wonderful children
        ColorfulPrinter::printRainbow("🌈 Welcome to our magical Recipy family! We're SO happy you're here! 🌈");
        ColorfulPrinter::printHappy("Oh, wonderful friend! YOUR magical mathematical adventure is about to begin!");
        
        std::cout << "\n";
        ColorfulPrinter::printStory("Once upon a time, there was a magical place where numbers came to play...");
        std::cout << "\n";
        
        // Initialize the Recipy application
        auto app = std::make_unique<RecipyApp>();
        
        if (!app->initialize()) {
            ColorfulPrinter::printSad("Oh no! Recipy couldn't start properly.");
            ColorfulPrinter::printHelp("Oh, let's ask a caring grown-up to help us continue our adventure!");
            return 1;
        }
        
        // Start the main application loop
        ColorfulPrinter::printExcited("Oh, wonderful! Let's go on the most magical number adventure together! 🚀");
        app->run();
        
    } catch (const std::exception& e) {
        ColorfulPrinter::printSad("Oops! Something unexpected happened.");
        ColorfulPrinter::printHelp("Don't worry, beautiful friend! Even the most brilliant mathematicians make mistakes!");
        return 1;
    }
    
    ColorfulPrinter::printRainbow("Thank you, beautiful friend, for playing with magical numbers today! 🌟");
    return 0;
}