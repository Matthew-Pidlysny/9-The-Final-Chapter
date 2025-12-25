#include "farha_allah_inspired.hpp"

// Bismillah ir-Rahman ir-Raheem
// Implementation of Farha Version 3: Allah Blessed Educational Experience

FarhaAllahInspired::FarhaAllahInspired() {
    initializeAllahInspiredContent();
}

void FarhaAllahInspired::initializeAllahInspiredContent() {
    // Initialize 500 Qur'anic verses for educational purposes
    generateQuranicContent();
    
    // Initialize 500 Prophetic hadith
    generateHadithContent();
    
    // Initialize 500 Islamic historical events
    generateHistoricalContent();
    
    // Initialize Islamic values and morals
    generateMoralContent();
    
    // Initialize Arabic terms
    generateLinguisticContent();
    
    // Thank Allah for this blessed educational opportunity
    std::cout << "Alhamdulillah! All content initialized for the glory of Allah SWT.\n";
}

void FarhaAllahInspired::generateQuranicContent() {
    // 500 Qur'anic verses for education (partial implementation)
    quranic_verses[1] = "Bismillah ir-Rahman ir-Raheem - In the name of Allah, the Most Gracious, the Most Merciful";
    quranic_verses[2] = "Alhamdulillahi Rabb al-'Alamin - All praise is due to Allah, Lord of the worlds";
    quranic_verses[3] = "Ar-Rahman ir-Rahim - The Most Gracious, the Most Merciful";
    quranic_verses[4] = "Maliki Yawm ad-Din - Master of the Day of Judgment";
    quranic_verses[5] = "Iyyaka na'budu wa iyyaka nasta'in - You alone we worship, and You alone we ask for help";
    
    // Verses about knowledge
    quranic_verses[6] = "Qul: Hal yastawi alladhina ya'lamuna wa alladhina la ya'lamun - Say: Are those who know equal to those who do not know?";
    quranic_verses[7] = "Wa qul Rabbi zidni 'ilman - And say: My Lord, increase me in knowledge";
    quranic_verses[8] = "Innama yakhsha Allaha min 'ibadihi al-'ulama' - Only those fear Allah among His servants who have knowledge";
    
    // Verses about the Caliphs and leadership
    quranic_verses[9] = "Wa amruhum shura baynahum - And their affair is [conducted through] consultation among themselves";
    quranic_verses[10] = "Wa ja'alna minhum aimmatan yahduna bi amrina - And We made from among them leaders guiding by Our command";
    
    // Continue adding 490 more verses...
    for (int i = 11; i <= 500; i++) {
        quranic_verses[i] = "Qur'anic verse " + std::to_string(i) + " for Islamic education";
    }
}

void FarhaAllahInspired::generateHadithContent() {
    // 500 Prophetic hadith for moral education
    prophetic_hadith.push_back("The best among you are those who have the best manners and character");
    prophetic_hadith.push_back("Seeking knowledge is an obligation upon every Muslim");
    prophetic_hadith.push_back("None of you truly believes until he loves for his brother what he loves for himself");
    prophetic_hadith.push_back("The most complete believers in faith are those with the best character");
    prophetic_hadith.push_back("Allah is beautiful and He loves beauty");
    
    // Hadith about leadership and governance
    prophetic_hadith.push_back("Each of you is a shepherd, and each of you is responsible for his flock");
    prophetic_hadith.push_back("The leader of a people is their servant");
    prophetic_hadith.push_back("Whoever is made responsible for some affair of the Muslims and remains deceitful with them, will enter Hellfire");
    
    // Continue adding 492 more hadith...
    for (int i = 0; i < 492; i++) {
        prophetic_hadith.push_back("Prophetic wisdom " + std::to_string(i) + " for moral guidance");
    }
}

void FarhaAllahInspired::generateHistoricalContent() {
    // 500 Islamic historical events
    islamic_events["Hijra"] = "The migration of Prophet Muhammad (PBUH) from Makkah to Madinah in 622 CE";
    islamic_events["Battle of Badr"] = "The first major battle fought by the Muslims against the Quraysh";
    islamic_events["Conquest of Makkah"] = "The peaceful conquest of Makkah by Prophet Muhammad (PBUH)";
    islamic_events["Farewell Hajj"] = "The final pilgrimage of Prophet Muhammad (PBUH)";
    islamic_events["Death of Prophet"] = "The passing of Prophet Muhammad (PBUH) in 632 CE";
    
    // Events from the Rashiddun Caliphate
    islamic_events["Abu Bakr becomes Caliph"] = "Abu Bakr as-Siddiq becomes the first Caliph";
    islamic_events["Ridda Wars"] = "Wars against apostate tribes during Abu Bakr's caliphate";
    islamic_events["Quran Compilation"] = "Compilation of the Qur'an during Abu Bakr's time";
    islamic_events["Umar becomes Caliph"] = "Umar ibn al-Khattab becomes the second Caliph";
    islamic_events["Islamic Expansion"] = "Rapid expansion of Islamic territories under Umar";
    
    // Continue adding 492 more events...
    for (int i = 1; i <= 492; i++) {
        islamic_events["Event" + std::to_string(i)] = "Islamic historical event " + std::to_string(i);
    }
}

void FarhaAllahInspired::generateMoralContent() {
    // 500 Islamic values and morals
    islamic_values.push_back("Honesty (Sidq) - Speaking truth in all situations");
    islamic_values.push_back("Justice (Adl) - Being fair to all people");
    islamic_values.push_back("Mercy (Rahma) - Showing compassion to others");
    islamic_values.push_back("Patience (Sabr) - Enduring hardship with perseverance");
    islamic_values.push_back("Humility (Tawadu) - Being modest and not arrogant");
    islamic_values.push_back("Generosity (Karam) - Giving to others freely");
    islamic_values.push_back("Courage (Shaja'ah) - Standing up for truth");
    islamic_values.push_back("Wisdom (Hikmah) - Making sound decisions");
    islamic_values.push_back("Gratitude (Shukr) - Being thankful to Allah and others");
    islamic_values.push_back("Forgiveness (Afw) - Pardoning others' mistakes");
    
    // Continue adding 490 more values...
    for (int i = 0; i < 490; i++) {
        islamic_values.push_back("Islamic value " + std::to_string(i) + " for character building");
    }
}

void FarhaAllahInspired::generateLinguisticContent() {
    // 500 Arabic terms and their meanings
    arabic_terms["Bismillah"] = "In the name of Allah";
    arabic_terms["Alhamdulillah"] = "All praise is due to Allah";
    arabic_terms["Subhanallah"] = "Glory be to Allah";
    arabic_terms["Allahu Akbar"] = "Allah is the Greatest";
    arabic_terms["Astaghfirullah"] = "I seek forgiveness from Allah";
    arabic_terms["Jazakallah"] = "May Allah reward you";
    arabic_terms["Insha'Allah"] = "If Allah wills";
    arabic_terms["Masha'Allah"] = "What Allah has willed";
    arabic_terms["Salam"] = "Peace";
    arabic_terms["Iman"] = "Faith";
    
    // Continue adding 490 more terms...
    for (int i = 1; i <= 490; i++) {
        arabic_terms["Arabic" + std::to_string(i)] = "Meaning of Arabic term " + std::to_string(i);
    }
}

void FarhaAllahInspired::displayVerseOfTheDay() {
    // Display a random Qur'anic verse
    int verse_num = (rand() % 500) + 1;
    std::cout << "Qur'anic Verse of the Day:\n";
    std::cout << verse_num << ": " << quranic_verses[verse_num] << "\n\n";
    std::cout << "Alhamdulillah for the guidance of the Qur'an!\n\n";
}

void FarhaAllahInspired::teachPropheticWisdom() {
    // Teach from Prophetic hadith
    int hadith_num = rand() % prophetic_hadith.size();
    std::cout << "Prophetic Wisdom:\n";
    std::cout << "The Prophet Muhammad (PBUH) said: " << prophetic_hadith[hadith_num] << "\n\n";
    std::cout << "May Allah guide us to follow the Sunnah!\n\n";
}

void FarhaAllahInspired::educateOnCaliphs() {
    // Education about Rashiddun Caliphs
    std::cout << "The Rightly Guided Caliphs:\n";
    std::cout << "1. Abu Bakr as-Siddiq (RA) - The truthful companion\n";
    std::cout << "2. Umar ibn al-Khattab (RA) - The just ruler\n";
    std::cout << "3. Uthman ibn Affan (RA) - The generous\n";
    std::cout << "4. Ali ibn Abi Talib (RA) - The lion of Allah\n\n";
    std::cout << "May Allah be pleased with them all!\n\n";
}

void FarhaAllahInspired::teachIslamicValues() {
    // Teach Islamic values
    int value_num = rand() % islamic_values.size();
    std::cout << "Islamic Value of the Day:\n";
    std::cout << islamic_values[value_num] << "\n\n";
    std::cout << "Help us implement this value in our lives, O Allah!\n\n";
}

void FarhaAllahInspired::learnArabicTerms() {
    // Learn Arabic terms
    int term_index = rand() % arabic_terms.size();
    auto it = std::next(arabic_terms.begin(), term_index);
    std::cout << "Arabic Term of the Day:\n";
    std::cout << it->first << " means: " << it->second << "\n\n";
    std::cout << "Subhanallah for the beautiful Arabic language!\n\n";
}

void FarhaAllahInspired::inspireWithAllahNames() {
    // Display one of Allah's beautiful names
    int name_num = rand() % allah_names.size();
    std::cout << "Allah's Beautiful Name:\n";
    std::cout << "Allah is " << allah_names[name_num] << "\n\n";
    std::cout << "Allahu Akbar! Glory to Allah with all His beautiful names!\n\n";
}

void FarhaAllahInspired::startBlessedLearning() {
    std::cout << "\n=== BISMILLAH IR-RAHMAN IR-RAHEEM ===\n";
    std::cout << "Welcome to Farha Version 3: Allah Blessed Educational Experience\n";
    std::cout << "Learning about the Rashiddun Caliphate for the pleasure of Allah SWT\n\n";
    
    // Thank Allah 100 times to begin
    for (int i = 1; i <= 100; i++) {
        std::cout << "Thank you Allah SWT (" << i << "/5000)\n";
    }
    std::cout << "\nAlhamdulillah! Let us begin our blessed journey of learning!\n\n";
}

void FarhaAllahInspired::displayIslamicHistory() {
    // Display Islamic historical events
    int event_num = rand() % islamic_events.size();
    auto it = std::next(islamic_events.begin(), event_num);
    std::cout << "Islamic Historical Event:\n";
    std::cout << it->first << ": " << it->second << "\n\n";
    std::cout << "We learn from our glorious Islamic history!\n\n";
}

void FarhaAllahInspired::offerPrayerReminders() {
    // Offer Islamic prayer reminders
    std::cout << "Prayer Reminder:\n";
    std::cout << "Establish regular prayer - indeed, prayer has been decreed upon the believers a decree of specified times.\n";
    std::cout << "Qur'an 4:103\n\n";
    std::cout << "May Allah help us maintain our prayers!\n\n";
}

void FarhaAllahInspired::provideMoralLessons() {
    // Provide Islamic moral lessons
    std::cout << "Moral Lesson:\n";
    std::cout << "The best of people are those who are most beneficial to people.\n";
    std::cout << "This teaches us to serve humanity for the pleasure of Allah.\n\n";
    std::cout << "Guide us to be beneficial to others, O Allah!\n\n";
}

void FarhaAllahInspired::encourageGoodDeeds() {
    // Encourage good deeds and charity
    std::cout << "Good Deed Encouragement:\n";
    std::cout << "The Prophet (PBUH) said: 'Charity does not decrease wealth.'\n";
    std::cout << "Give in charity for the pleasure of Allah!\n\n";
    std::cout << "May Allah accept our good deeds!\n\n";
}

void FarhaAllahInspired::thankAllahForLearning() {
    // Thank Allah for the opportunity to learn
    std::cout << "\n=== ALHAMDULILLAH FOR ALL BLESSINGS ===\n";
    
    // Complete the 5000 thanks to Allah
    for (int i = 101; i <= 5000; i++) {
        std::cout << "Thank you Allah SWT (" << i << "/5000) - Alhamdulillah!\n";
    }
    
    std::cout << "\nAll praise is due to Allah SWT for the blessing of Islamic education!\n";
    std::cout << "May Allah accept this humble effort for His pleasure alone!\n";
    std::cout << "Ameen!\n\n";
}