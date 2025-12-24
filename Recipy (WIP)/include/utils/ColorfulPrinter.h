/*
 * ColorfulPrinter.h - Child-Friendly Output System
 * 
 * Makes console output fun and engaging for Grade 1 students
 * with colors, emojis, and encouraging messages.
 */

#ifndef COLORFULPRINTER_H
#define COLORFULPRINTER_H

#include <string>
#include <iostream>

namespace Recipy {
namespace Utils {

/**
 * @brief Child-friendly colorful output system
 * 
 * Uses ANSI color codes and emojis to create engaging
 * text output that appeals to Grade 1 students.
 */
class ColorfulPrinter {
public:
    /**
     * @brief Print text in rainbow colors
     */
    static void printRainbow(const std::string& message);
    
    /**
     * @brief Print happy/excited messages
     */
    static void printHappy(const std::string& message);
    static void printExcited(const std::string& message);
    
    /**
     * @brief Print gentle/encouraging messages
     */
    static void printStory(const std::string& message);
    static void printHelp(const std::string& message);
    
    /**
     * @brief Print gentle warning/sad messages
     */
    static void printSad(const std::string& message);
    static void printGentleWarning(const std::string& message);
    
    /**
     * @brief Print thinking/learning messages
     */
    static void printThinking(const std::string& message);
    static void printLearning(const std::string& message);
    
    /**
     * @brief Print number-related messages
     */
    static void printNumber(const std::string& message);
    static void printMath(const std::string& message);
    
    /**
     * @brief Print achievement messages
     */
    static void printAchievement(const std::string& message);
    static void printProgress(const std::string& message);
    
    /**
     * @brief Print interactive prompts
     */
    static void askQuestion(const std::string& question);
    static void giveInstructions(const std::string& instruction);
    
    /**
     * @brief Create fun separators and borders
     */
    static void printStars(int count = 50);
    static void printHearts(int count = 20);
    static void printNumbers123();
    
    /**
     * @brief Print with fun animations (simple)
     */
    static void printWithDots(const std::string& message);
    static void printSlowly(const std::string& message, int delayMs = 100);
    
private:
    // ANSI color codes
    static const std::string RED;
    static const std::string GREEN;
    static const std::string YELLOW;
    static const std::string BLUE;
    static const std::string MAGENTA;
    static const std::string CYAN;
    static const std::string WHITE;
    static const std::string RESET;
    static const std::string BOLD;
    
    // Helper methods
    static void printColored(const std::string& message, const std::string& color);
    static void printWithEmoji(const std::string& message, const std::string& emoji);
    static void printColorCycling(const std::string& message);
};

} // namespace Utils
} // namespace Recipy

#endif // COLORFULPRINTER_H