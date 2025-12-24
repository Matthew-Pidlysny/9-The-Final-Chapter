/*
 * Recipy - Grade 1 Mathematical Adventure
 * Main Entry Point
 * 
 * A child-friendly introduction to advanced mathematical concepts
 * through playful workshops and AI-powered learning.
 */

#include <iostream>
#include <memory>
#include "RecipyApp.h"
#include "utils/ColorfulPrinter.h"

int main() {
    try {
        // Create colorful welcome message for children
        ColorfulPrinter::printRainbow("🌈 Welcome to Recipy! 🌈");
        ColorfulPrinter::printHappy("Your Mathematical Adventure Begins!");
        
        std::cout << "\n";
        ColorfulPrinter::printStory("Once upon a time, there was a magical place where numbers came to play...");
        std::cout << "\n";
        
        // Initialize the Recipy application
        auto app = std::make_unique<RecipyApp>();
        
        if (!app->initialize()) {
            ColorfulPrinter::printSad("Oh no! Recipy couldn't start properly.");
            ColorfulPrinter::printHelp("Let's ask a grown-up for help!");
            return 1;
        }
        
        // Start the main application loop
        ColorfulPrinter::printExcited("Let's go on a number adventure! 🚀");
        app->run();
        
    } catch (const std::exception& e) {
        ColorfulPrinter::printSad("Oops! Something unexpected happened.");
        ColorfulPrinter::printHelp("Don't worry, even mathematicians make mistakes!");
        return 1;
    }
    
    ColorfulPrinter::printRainbow("Thank you for playing with numbers today! 🌟");
    return 0;
}