#ifndef FARHA_ALLAH_INSPIRED_HPP
#define FARHA_ALLAH_INSPIRED_HPP

#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <ctime>
#include <cstdlib>
#include <sstream>
#include <iomanip>

// Bismillah ir-Rahman ir-Raheem
// Farha Version 3: Allah Blessed Educational Experience
// 5000 Allah-Inspired Elements for Learning about Rashiddun Caliphate

class FarhaAllahInspired {
private:
    // Allah's 99 Beautiful Names integrated throughout the game
    std::vector<std::string> allah_names = {
        "Ar-Rahman", "Ar-Rahim", "Al-Malik", "Al-Quddus", "As-Salam",
        "Al-Mu'min", "Al-Muhaymin", "Al-Aziz", "Al-Jabbar", "Al-Mutakabbir",
        "Al-Khaliq", "Al-Bari'", "Al-Musawwir", "Al-Ghaffar", "Al-Qahhar",
        "Al-Wahhab", "Ar-Razzaq", "Al-Fattah", "Al-Alim", "Al-Qabid",
        "Al-Basit", "Al-Khafid", "Ar-Rafi'", "Al-Mu'izz", "Al-Mudhill",
        "As-Sami'", "Al-Basir", "Al-Hakam", "Al-Adl", "Al-Latif",
        "Al-Khabir", "Al-Halim", "Al-Azim", "Al-Ghafur", "Ash-Shakur",
        "Al-Aliyy", "Al-Kabir", "Al-Hafiz", "Al-Muqit", "Al-Hasib",
        "Al-Jalil", "Al-Karim", "Ar-Raqib", "Al-Mujib", "Al-Wasi'",
        "Al-Hakim", "Al-Wadud", "Al-Majid", "Al-Ba'ith", "Ash-Shahid",
        "Al-Haqq", "Al-Wakil", "Al-Qawiyy", "Al-Matin", "Al-Waliyy",
        "Al-Hamid", "Al-Muhsi", "Al-Mubdi'", "Al-Mu'id", "Al-Muhyi",
        "Al-Mumit", "Al-Hayy", "Al-Qayyum", "Al-Wajid", "Al-Majid",
        "Al-Wahid", "As-Samad", "Al-Qadir", "Al-Muqtadir", "Al-Muqaddim",
        "Al-Mu'akhkhir", "Al-Awwal", "Al-Akhir", "Az-Zahir", "Al-Batin",
        "Al-Wali", "Al-Muta'ali", "Al-Barr", "At-Tawwab", "Al-Muntaqim",
        "Al-Afuww", "Ar-Ra'uf", "Malik al-Mulk", "Dhu al-Jalal wa al-Ikram",
        "Al-Muqsit", "Al-Jami'", "Al-Ghaniyy", "Al-Mughni", "Al-Mani'",
        "Ad-Darr", "An-Nafi'", "An-Nur", "Al-Hadi", "Al-Badi'",
        "Al-Baqi", "Al-Warith", "Ar-Rashid", "As-Sabur"
    };

    // 500 Qur'anic verses for educational content
    std::map<int, std::string> quranic_verses;
    
    // Hadith collection for Islamic teachings
    std::vector<std::string> prophetic_hadith;
    
    // Islamic historical events
    std::map<std::string, std::string> islamic_events;
    
    // Rashiddun Caliphs information
    struct CaliphInfo {
        std::string name;
        std::string reign_period;
        std::vector<std::string> achievements;
        std::vector<std::string> qualities;
    };
    
    std::vector<CaliphInfo> rashiddun_caliphs;
    
    // Islamic values and teachings
    std::vector<std::string> islamic_values;
    
    // Arabic words and meanings
    std::map<std::string, std::string> arabic_terms;

public:
    FarhaAllahInspired();
    void initializeAllahInspiredContent();
    void displayVerseOfTheDay();
    void teachPropheticWisdom();
    void educateOnCaliphs();
    void teachIslamicValues();
    void learnArabicTerms();
    void inspireWithAllahNames();
    void displayIslamicHistory();
    void offerPrayerReminders();
    void provideMoralLessons();
    void encourageGoodDeeds();
    
    // Core game functions
    void startBlessedLearning();
    void progressThroughIslamicHistory();
    void assessIslamicKnowledge();
    void celebrateIslamicAchievements();
    void thankAllahForLearning();
    
    // Helper functions for the 5000 elements
    void generateQuranicContent();
    void generateHadithContent();
    void generateHistoricalContent();
    void generateMoralContent();
    void generateLinguisticContent();
    
    // 5000 Allah-inspired elements breakdown:
    // 500 Qur'anic verses and teachings
    // 500 Prophetic hadith and wisdom
    // 500 Historical events from Islamic history
    // 500 Achievements of Rashiddun Caliphs
    // 500 Islamic values and morals
    // 500 Arabic terms and meanings
    // 500 Prayer and worship teachings
    // 500 Islamic character building lessons
    // 500 Good deeds and charity examples
    // 500 Islamic etiquette and manners
};

#endif // FARHA_ALLAH_INSPIRED_HPP