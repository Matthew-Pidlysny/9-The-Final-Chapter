/*
 * ColorfulPrinter.cpp - Child-Friendly Output Implementation
 * 
 * Making learning fun with colorful, engaging text output
 * designed specifically for Grade 1 students.
 */

#include "utils/ColorfulPrinter.h"
#include <iostream>
#include <thread>
#include <chrono>

namespace Recipy {
namespace Utils {

// ANSI color codes
const std::string ColorfulPrinter::RED = "\033[31m";
const std::string ColorfulPrinter::GREEN = "\033[32m";
const std::string ColorfulPrinter::YELLOW = "\033[33m";
const std::string ColorfulPrinter::BLUE = "\033[34m";
const std::string ColorfulPrinter::MAGENTA = "\033[35m";
const std::string ColorfulPrinter::CYAN = "\033[36m";
const std::string ColorfulPrinter::WHITE = "\033[37m";
const std::string ColorfulPrinter::RESET = "\033[0m";
const std::string ColorfulPrinter::BOLD = "\033[1m";

void ColorfulPrinter::printRainbow(const std::string& message) {
    printColorCycling(message);
}

void ColorfulPrinter::printHappy(const std::string& message) {
    printWithEmoji(message, "😊");
}

void ColorfulPrinter::printExcited(const std::string& message) {
    printWithEmoji(message, "🎉");
}

void ColorfulPrinter::printStory(const std::string& message) {
    printColored(message, YELLOW);
    std::cout << " 📖" << std::endl;
}

void ColorfulPrinter::printHelp(const std::string& message) {
    printColored(message, CYAN);
    std::cout << " 💡" << std::endl;
}

void ColorfulPrinter::printSad(const std::string& message) {
    printColored(message, BLUE);
    std::cout << " 😔" << std::endl;
}

void ColorfulPrinter::printGentleWarning(const std::string& message) {
    printColored(message, YELLOW);
    std::cout << " ⚠️" << std::endl;
}

void ColorfulPrinter::printThinking(const std::string& message) {
    printColored(message, MAGENTA);
    std::cout << " 🤔" << std::endl;
}

void ColorfulPrinter::printLearning(const std::string& message) {
    printColored(message, GREEN);
    std::cout << " 🎓" << std::endl;
}

void ColorfulPrinter::printNumber(const std::string& message) {
    printColored(message, CYAN);
    std::cout << " 🔢" << std::endl;
}

void ColorfulPrinter::printMath(const std::string& message) {
    printColored(message, MAGENTA);
    std::cout << " ➕" << std::endl;
}

void ColorfulPrinter::printAchievement(const std::string& message) {
    printColored(message, YELLOW);
    std::cout << " 🏆" << std::endl;
}

void ColorfulPrinter::printProgress(const std::string& message) {
    printColored(message, GREEN);
    std::cout << " 📈" << std::endl;
}

void ColorfulPrinter::askQuestion(const std::string& question) {
    printColored(question, BLUE);
    std::cout << " ❓" << std::endl;
}

void ColorfulPrinter::giveInstructions(const std::string& instruction) {
    printColored(instruction, GREEN);
    std::cout << " 👉" << std::endl;
}

void ColorfulPrinter::printStars(int count) {
    std::cout << YELLOW;
    for (int i = 0; i < count; ++i) {
        std::cout << "⭐";
    }
    std::cout << RESET << std::endl;
}

void ColorfulPrinter::printHearts(int count) {
    std::cout << RED;
    for (int i = 0; i < count; ++i) {
        std::cout << "❤️";
    }
    std::cout << RESET << std::endl;
}

void ColorfulPrinter::printNumbers123() {
    std::cout << BLUE << "1️⃣ 2️⃣ 3️⃣ 4️⃣ 5️⃣ 6️⃣ 7️⃣ 8️⃣ 9️⃣ 🔟" << RESET << std::endl;
}

void ColorfulPrinter::printWithDots(const std::string& message) {
    printColored(message, YELLOW);
    std::cout << " ";
    for (int i = 0; i < 3; ++i) {
        std::cout << ".";
        std::cout.flush();
        std::this_thread::sleep_for(std::chrono::milliseconds(500));
    }
    std::cout << RESET << std::endl;
}

void ColorfulPrinter::printSlowly(const std::string& message, int delayMs) {
    for (char c : message) {
        std::cout << c;
        std::cout.flush();
        std::this_thread::sleep_for(std::chrono::milliseconds(delayMs));
    }
    std::cout << RESET << std::endl;
}

void ColorfulPrinter::printColored(const std::string& message, const std::string& color) {
    std::cout << color << message << RESET;
}

void ColorfulPrinter::printWithEmoji(const std::string& message, const std::string& emoji) {
    std::cout << GREEN << message << " " << emoji << RESET << std::endl;
}

void ColorfulPrinter::printColorCycling(const std::string& message) {
    const std::vector<std::string> colors = {RED, YELLOW, GREEN, CYAN, BLUE, MAGENTA};
    
    for (size_t i = 0; i < message.length(); ++i) {
        std::cout << colors[i % colors.size()] << message[i];
    }
    std::cout << RESET << std::endl;
}

} // namespace Utils
} // namespace Recipy