#include "farha_game.hpp"
#include <algorithm>
#include <sstream>
#include <iomanip>

FarhaGame::FarhaGame() : rng(std::random_device{}()) {
    single_player_mode = true;
    game_completed = false;
    current_turn = 1;
    
    // Initialize educational content
    initialize_quranic_content();
    initialize_hadith_content();
    initialize_territories();
    initialize_historical_battles();
    
    std::cout << "\n🌟 Initializing Farha - Educational Caliphate Game 🌟\n";
}

void FarhaGame::initialize_quranic_content() {
    // Surah Al-Ikhlas (The Purity)
    quranic_verses.push_back({
        "Al-Ikhlas",
        "قُلْ هُوَ اللَّهُ أَحَدٌ",
        "Say: He is Allah, the One and Only",
        "Allah is unique, there is no one like Him. He is not born and does not give birth.",
        "Learn about the oneness of Allah (Tawhid)"
    });
    
    // Surah Al-Falaq (The Dawn)
    quranic_verses.push_back({
        "Al-Falaq",
        "قُلْ أَعُوذُ بِرَبِّ الْفَلَقِ",
        "Say: I seek refuge in the Lord of the dawn",
        "We ask Allah to protect us from all harm, especially from the darkness of night.",
        "Always seek Allah's protection from evil"
    });
    
    // Surah An-Nas (Mankind)
    quranic_verses.push_back({
        "An-Nas",
        "قُلْ أَعُوذُ بِرَبِّ النَّاسِ",
        "Say: I seek refuge in the Lord of mankind",
        "We ask Allah to protect us from the whisperings of Shaytan and evil suggestions.",
        "Seek refuge in Allah from bad influences"
    });
    
    // Surah Al-Kafirun (The Disbelievers)
    quranic_verses.push_back({
        "Al-Kafirun",
        "قُلْ يَا أَيُّهَا الْكَافِرُونَ",
        "Say: O you who disbelieve!",
        "This surah teaches us about religious tolerance and staying firm in our beliefs.",
        "Respect others while staying true to your faith"
    });
}

void FarhaGame::initialize_hadith_content() {
    hadith_collection.push_back({
        "The best among you are those who learn the Quran and teach it.",
        "Sahih Bukhari",
        "This hadith emphasizes the importance of Quranic education and sharing knowledge.",
        "Read Quran daily and share what you learn with friends and family."
    });
    
    hadith_collection.push_back({
        "None of you truly believes until he wishes for his brother what he wishes for himself.",
        "Sahih Bukhari",
        "This teaches us about empathy and treating others with kindness and fairness.",
        "Always think about others' feelings and treat everyone equally."
    });
    
    hadith_collection.push_back({
        "Seek knowledge from the cradle to the grave.",
        "Various sources",
        "Learning is a lifelong journey that should never stop.",
        "Be curious and always try to learn new things."
    });
}

void FarhaGame::initialize_territories() {
    territories.push_back({
        "Medina",
        "The city where Prophet Muhammad (PBUH) established the first Islamic state",
        "Medina became the center of the Islamic community and the capital of the Rashiddun Caliphate under the first four Caliphs.",
        1,
        false
    });
    
    territories.push_back({
        "Mecca",
        "The holiest city in Islam, home of the Kaaba",
        "Mecca was peacefully conquered during Prophet Muhammad's time and became the spiritual center of Islam.",
        1,
        false
    });
    
    territories.push_back({
        "Jerusalem",
        "City of Prophets, site of Al-Aqsa Mosque",
        "Jerusalem was conquered during Caliph Umar's reign and became an important Islamic city.",
        2,
        false
    });
    
    territories.push_back({
        "Damascus",
        "Capital of the Umayyad Caliphate",
        "Damascus was conquered during Caliph Umar's time and became a major center of Islamic civilization.",
        2,
        false
    });
    
    territories.push_back({
        "Cairo",
        "City of a thousand minarets",
        "Cairo became an important center of Islamic learning and culture during the Islamic expansion.",
        3,
        false
    });
}

void FarhaGame::initialize_historical_battles() {
    historical_battles.push_back({
        "Battle of Yarmouk",
        "636 CE",
        "A decisive battle that led to the conquest of Syria",
        "This battle demonstrated the importance of strategy and unity in achieving victory.",
        {"Who was the Caliph during this battle?", "What modern country includes this region?", "What was the outcome?"},
        false
    });
    
    historical_battles.push_back({
        "Battle of Qadisiyyah",
        "636 CE",
        "Led to the conquest of Persia",
        "This battle opened the way for Islamic civilization to spread into Persia.",
        {"Which empire was defeated?", "Who was the Persian commander?", "What was the significance?"},
        false
    });
    
    historical_battles.push_back({
        "Conquest of Jerusalem",
        "637 CE",
        "Peaceful surrender of Jerusalem to Muslims",
        "Caliph Umar's just treatment of the people of Jerusalem set an example for future generations.",
        {"Which Caliph received the keys?", "What famous document was signed?", "How were the people treated?"},
        false
    });
}

void FarhaGame::display_welcome() {
    display_ascii_art();
    std::cout << "\n🌟 WELCOME TO FARHA - THE EDUCATIONAL CALIPHATE GAME 🌟\n\n";
    std::cout << "📚 Learn about the Rashiddun Caliphate through fun and educational gameplay!\n";
    std::cout << "🎮 This is a child-friendly game where everyone learns and succeeds!\n";
    std::cout << "🕌 Discover the beauty of Islamic history and teachings.\n\n";
    
    std::cout << "🎯 Learning Objectives:\n";
    std::cout << "  • Understand the Rashiddun Caliphate establishment\n";
    std::cout << "  • Learn the 4 Qul (important Quranic chapters)\n";
    std::cout << "  • Gain knowledge of authentic Hadith\n";
    std::cout << "  • Develop historical understanding\n";
    std::cout << "  • Build moral and spiritual values\n\n";
    
    std::cout << "🎲 Special Feature: There's no losing in Farha!\n";
    std::cout << "   You only learn at different speeds - everyone succeeds! 🎉\n\n";
    
    animate_progress("Preparing your educational journey...");
}

void FarhaGame::display_ascii_art() {
    std::cout << R"(
    ╔═══════════════════════════════════════════════════════════════╗
    ║                                                               ║
    ║    F A R H A                                                 ║
    ║                                                         🕌    ║
    ║    Educational Caliphate Game                               ║
    ║                                                         📚    ║
    ║    Establish the Rashiddun Caliphate                        ║
    ║    Through Learning and Discovery                           ║
    ║                                                         🎮    ║
    ║                                                               ║
    ╚═══════════════════════════════════════════════════════════════╝
    )";
}

void FarhaGame::setup_players() {
    std::cout << "\n👥 PLAYER SETUP\n";
    std::cout << "═════════════════════════════════════════════\n\n";
    
    std::cout << "How many players? (1 or 2): ";
    int player_count;
    std::cin >> player_count;
    
    std::cin.ignore(); // Clear newline
    
    single_player_mode = (player_count == 1);
    
    // Setup Player 1
    std::cout << "\n👤 Player 1 Setup:\n";
    std::cout << "Enter your name: ";
    std::getline(std::cin, player1.name);
    player1.role = "Caliph";
    player1.knowledge_level = 1;
    player1.speed = 100; // Base speed
    player1.territories_conquered = 0;
    player1.is_active = true;
    
    if (single_player_mode) {
        player2.name = "AI Scholar";
        player2.role = "Scholar";
        player2.knowledge_level = 1;
        player2.speed = 100;
        player2.territories_conquered = 0;
        player2.is_active = false; // AI helper
    } else {
        std::cout << "\n👤 Player 2 Setup:\n";
        std::cout << "Enter your name: ";
        std::getline(std::cin, player2.name);
        player2.role = "Scholar";
        player2.knowledge_level = 1;
        player2.speed = 100;
        player2.territories_conquered = 0;
        player2.is_active = true;
    }
    
    std::cout << "\n✅ Players setup complete!\n";
    std::cout << player1.name << " - Role: " << player1.role << "\n";
    if (!single_player_mode) {
        std::cout << player2.name << " - Role: " << player2.role << "\n";
    } else {
        std::cout << "AI Scholar - Learning Assistant\n";
    }
}

void FarhaGame::start_game() {
    display_welcome();
    setup_players();
    
    if (single_player_mode) {
        play_single_player();
    } else {
        play_two_player();
    }
}

void FarhaGame::play_two_player() {
    std::cout << "\n🎮 STARTING TWO PLAYER MODE\n";
    std::cout << "═════════════════════════════════════════════\n";
    
    while (!game_completed) {
        // Player 1's turn
        std::cout << "\n📅 TURN " << current_turn << " - " << player1.name << "'s Learning Journey\n";
        std::cout << "═════════════════════════════════════════════\n";
        
        display_game_board();
        process_turn(player1);
        
        // Player 2's turn
        if (!game_completed) {
            std::cout << "\n📅 TURN " << current_turn << " - " << player2.name << "'s Learning Journey\n";
            std::cout << "═════════════════════════════════════════════\n";
            
            display_game_board();
            process_turn(player2);
        }
        
        display_progress();
        current_turn++;
        
        // Check win conditions for both players
        int total_territories = player1.territories_conquered + player2.territories_conquered;
        int total_surahs = player1.learned_surahs.size() + player2.learned_surahs.size();
        
        if (total_territories >= static_cast<int>(territories.size()) && total_surahs >= 4) {
            complete_game();
            break;
        }
        
        // Prevent infinite loop
        if (current_turn > 20) {
            std::cout << "\n🎉 Maximum learning turns reached! Time to complete your journey!\n";
            complete_game();
            break;
        }
        
        std::cout << "\nPress Enter to continue your learning journey...";
        std::cin.ignore();
        std::cin.get();
    }
}

void FarhaGame::play_single_player() {
    std::cout << "\n🎮 STARTING SINGLE PLAYER MODE\n";
    std::cout << "═════════════════════════════════════════════\n";
    
    while (!game_completed) {
        std::cout << "\n📅 TURN " << current_turn << " - " << player1.name << "'s Learning Journey\n";
        std::cout << "═════════════════════════════════════════════\n";
        
        display_game_board();
        process_turn(player1);
        display_progress();
        
        current_turn++;
        
        // Check win conditions
        if (player1.territories_conquered >= territories.size() && 
            player1.learned_surahs.size() >= 4) {
            complete_game();
            break;
        }
        
        // Prevent infinite loop
        if (current_turn > 20) {
            std::cout << "\n🎉 Maximum learning turns reached! Time to complete your journey!\n";
            complete_game();
            break;
        }
        
        std::cout << "\nPress Enter to continue your learning journey...";
        std::cin.ignore();
        std::cin.get();
    }
}

void FarhaGame::display_game_board() {
    std::cout << "\n🗺️ CALIPHATE EXPANSION BOARD\n";
    std::cout << "═════════════════════════════════════════════\n\n";
    
    std::cout << "👤 " << player1.name << " (Caliph)\n";
    std::cout << "📚 Knowledge Level: " << player1.knowledge_level << "\n";
    std::cout << "⚡ Speed: " << player1.speed << "\n";
    std::cout << "🏰 Territories Conquered: " << player1.territories_conquered << "/" << territories.size() << "\n";
    std::cout << "📖 Surahs Learned: " << player1.learned_surahs.size() << "/4\n";
    std::cout << "📜 Hadith Learned: " << player1.learned_hadith.size() << "\n\n";
    
    std::cout << "🏛️ AVAILABLE TERRITORIES:\n";
    for (size_t i = 0; i < territories.size(); ++i) {
        std::string status = territories[i].conquered ? "✅" : "🔓";
        std::cout << "  " << (i+1) << ". " << territories[i].name << " " << status << "\n";
    }
    
    std::cout << "\n⚔️ HISTORICAL BATTLES TO LEARN:\n";
    for (size_t i = 0; i < historical_battles.size(); ++i) {
        std::string status = historical_battles[i].completed ? "✅" : "📚";
        std::cout << "  " << (i+1) << ". " << historical_battles[i].name << " (" << historical_battles[i].year << ") " << status << "\n";
    }
}

void FarhaGame::process_turn(Player& player) {
    std::cout << "\n🎯 What would you like to learn about today?\n";
    std::cout << "1. 🕌 Learn about a Territory\n";
    std::cout << "2. ⚔️ Study a Historical Battle\n";
    std::cout << "3. 📖 Learn a Surah from the 4 Qul\n";
    std::cout << "4. 📜 Study Hadith\n";
    std::cout << "5. 🎲 Educational Quiz Challenge\n";
    std::cout << "Choose your learning path (1-5): ";
    
    int choice;
    std::cin >> choice;
    
    switch (choice) {
        case 1:
            process_territory_expansion(player);
            break;
        case 2:
            process_historical_battle(player);
            break;
        case 3:
            teach_4_qul(player);
            break;
        case 4:
            teach_hadith(player);
            break;
        case 5:
            quiz_player(player);
            break;
        default:
            std::cout << "Invalid choice. Let's learn about territories instead!\n";
            process_territory_expansion(player);
    }
    
    update_player_speed(player);
}

void FarhaGame::process_territory_expansion(Player& player) {
    std::cout << "\n🏰 TERRITORY EXPANSION LEARNING\n";
    std::cout << "═════════════════════════════════════════════\n";
    
    // Find unconquered territories
    std::vector<int> available_territories;
    for (size_t i = 0; i < territories.size(); ++i) {
        if (!territories[i].conquered) {
            available_territories.push_back(i);
        }
    }
    
    if (available_territories.empty()) {
        std::cout << "🎉 All territories have been learned about!\n";
        return;
    }
    
    std::cout << "Available territories to learn about:\n";
    for (size_t i = 0; i < available_territories.size(); ++i) {
        int idx = available_territories[i];
        std::cout << (i+1) << ". " << territories[idx].name 
                  << " (Difficulty: " << territories[idx].difficulty_level << ")\n";
    }
    
    std::cout << "Choose a territory to learn about: ";
    int choice;
    std::cin >> choice;
    
    if (choice >= 1 && choice <= static_cast<int>(available_territories.size())) {
        int territory_idx = available_territories[choice-1];
        Territory& territory = territories[territory_idx];
        
        std::cout << "\n📚 Learning about " << territory.name << ":\n";
        std::cout << territory.historical_significance << "\n\n";
        std::cout << "🎓 Educational Content:\n";
        std::cout << territory.educational_content << "\n\n";
        
        // Simple learning confirmation
        std::cout << "Did you learn something new? (1=Yes, 2=Not really): ";
        int learned;
        std::cin >> learned;
        
        if (learned == 1) {
            territory.conquered = true;
            player.territories_conquered++;
            player.knowledge_level++;
            std::cout << "🎉 Great job! " << territory.name << " is now part of your knowledge!\n";
            std::cout << generate_encouragement() << "\n";
        } else {
            std::cout << "📚 That's okay! Learning takes time. Your speed will adjust accordingly.\n";
            player.speed = std::max(50, player.speed - 20); // Slow down to learn more
        }
    }
}

void FarhaGame::teach_4_qul(Player& player) {
    std::cout << "\n📖 LEARNING THE 4 QUL\n";
    std::cout << "═════════════════════════════════════════════\n";
    
    // Find unlearned surahs
    std::vector<int> unlearned_surahs;
    for (size_t i = 0; i < quranic_verses.size(); ++i) {
        bool learned = false;
        for (const auto& learned_name : player.learned_surahs) {
            if (learned_name == quranic_verses[i].surah_name) {
                learned = true;
                break;
            }
        }
        if (!learned) {
            unlearned_surahs.push_back(i);
        }
    }
    
    if (unlearned_surahs.empty()) {
        std::cout << "🎉 You have learned all 4 Qul! Masha'Allah!\n";
        return;
    }
    
    // Teach next unlearned surah
    int surah_idx = unlearned_surahs[0];
    const QuranicContent& surah = quranic_verses[surah_idx];
    
    std::cout << "🕌 Today we're learning: " << surah.surah_name << "\n\n";
    
    std::cout << "📜 Arabic Text:\n";
    std::cout << surah.arabic_text << "\n\n";
    
    std::cout << "🌍 English Translation:\n";
    std::cout << surah.english_translation << "\n\n";
    
    std::cout << "👶 Child-Friendly Explanation:\n";
    std::cout << surah.child_explanation << "\n\n";
    
    std::cout << "💡 Moral Lesson:\n";
    std::cout << surah.moral_lesson << "\n\n";
    
    animate_progress("Absorbing the beautiful words of the Quran...");
    
    player.learned_surahs.push_back(surah.surah_name);
    player.knowledge_level += 2;
    player.speed = std::min(150, player.speed + 10); // Speed up for learning Quran
    
    std::cout << "🎉 Excellent! You've learned " << surah.surah_name << "!\n";
    std::cout << generate_encouragement() << "\n";
}

void FarhaGame::teach_hadith(Player& player) {
    std::cout << "\n📜 LEARNING HADITH\n";
    std::cout << "═════════════════════════════════════════════\n";
    
    if (player.learned_hadith.size() >= hadith_collection.size()) {
        std::cout << "🎉 You have learned all available Hadith! Subhan'Allah!\n";
        return;
    }
    
    const HadithContent& hadith = hadith_collection[player.learned_hadith.size()];
    
    std::cout << "📚 Today's Hadith:\n";
    std::cout << "&quot;" << hadith.text << "&quot;\n\n";
    
    std::cout << "📖 Source: " << hadith.source << "\n\n";
    
    std::cout << "💭 Explanation:\n";
    std::cout << hadith.explanation << "\n\n";
    
    std::cout << "🎯 How to Apply This:\n";
    std::cout << hadith.practical_application << "\n\n";
    
    animate_progress("Reflecting on the wisdom of Prophet Muhammad (PBUH)...");
    
    player.learned_hadith.push_back(hadith.text);
    player.knowledge_level++;
    player.speed = std::min(140, player.speed + 5);
    
    std::cout << "🎉 Beautiful! You've learned a new Hadith!\n";
    std::cout << generate_encouragement() << "\n";
}

void FarhaGame::quiz_player(Player& player) {
    std::cout << "\n🎲 EDUCATIONAL QUIZ CHALLENGE\n";
    std::cout << "═════════════════════════════════════════════\n";
    
    std::vector<std::string> questions = {
        "Who was the first Caliph of Islam?",
        "What does the word 'Caliph' mean?",
        "Name one of the 4 Qul surahs",
        "Which city was the first capital of the Islamic Caliphate?",
        "What does 'Rashiddun' mean?"
    };
    
    std::vector<std::string> answers = {
        "Abu Bakr",
        "Successor or deputy",
        "Al-Ikhlas or Al-Falaq or An-Nas or Al-Kafirun",
        "Medina",
        "Rightly Guided"
    };
    
    int question_idx = rng() % questions.size();
    
    std::cout << "❓ Question: " << questions[question_idx] << "\n";
    std::cout << "Your answer: ";
    std::cin.ignore();
    std::string user_answer;
    std::getline(std::cin, user_answer);
    
    std::cout << "\n💡 The correct answer is: " << answers[question_idx] << "\n";
    
    if (user_answer.find("Abu Bakr") != std::string::npos && question_idx == 0) {
        std::cout << "🎉 Correct! Excellent knowledge!\n";
        player.knowledge_level += 2;
        player.speed = std::min(160, player.speed + 15);
    } else if (user_answer.find("Successor") != std::string::npos && question_idx == 1) {
        std::cout << "🎉 Correct! Great understanding!\n";
        player.knowledge_level += 2;
        player.speed = std::min(160, player.speed + 15);
    } else {
        std::cout << "📚 Good try! Learning is a journey. Let's remember this for next time!\n";
        player.knowledge_level++;
        player.speed = std::max(60, player.speed - 10);
    }
    
    std::cout << generate_encouragement() << "\n";
}

void FarhaGame::process_historical_battle(Player& player) {
    std::cout << "\n⚔️ HISTORICAL BATTLE STUDY\n";
    std::cout << "═════════════════════════════════════════════\n";
    
    // Find uncompleted battles
    std::vector<int> available_battles;
    for (size_t i = 0; i < historical_battles.size(); ++i) {
        if (!historical_battles[i].completed) {
            available_battles.push_back(i);
        }
    }
    
    if (available_battles.empty()) {
        std::cout << "🎉 You have studied all historical battles!\n";
        return;
    }
    
    int battle_idx = available_battles[0];
    const Battle& battle = historical_battles[battle_idx];
    
    std::cout << "📚 Today we're studying: " << battle.name << " (" << battle.year << ")\n\n";
    
    std::cout << "📖 Description:\n";
    std::cout << battle.description << "\n\n";
    
    std::cout << "🎓 Educational Outcome:\n";
    std::cout << battle.educational_outcome << "\n\n";
    
    std::cout << "❓ Quick Question: " << battle.questions[0] << "\n";
    std::cout << "Your answer: ";
    std::cin.ignore();
    std::string answer;
    std::getline(std::cin, answer);
    
    animate_progress("Processing historical learning...");
    
    historical_battles[battle_idx].completed = true;
    player.knowledge_level += 2;
    player.speed = std::min(145, player.speed + 8);
    
    std::cout << "\n🎉 Excellent historical analysis! You've completed " << battle.name << "!\n";
    std::cout << generate_encouragement() << "\n";
}

void FarhaGame::update_player_speed(Player& player) {
    // Adjust speed based on knowledge level
    int base_speed = 100;
    int speed_bonus = player.knowledge_level * 5;
    player.speed = base_speed + speed_bonus;
    player.speed = std::max(50, std::min(200, player.speed));
    
    std::cout << "\n⚡ Your new speed: " << player.speed << " (Faster means you're learning well!)\n";
}

void FarhaGame::display_progress() {
    std::cout << "\n📊 YOUR LEARNING PROGRESS\n";
    std::cout << "═════════════════════════════════════════════\n";
    std::cout << "📚 Knowledge Level: " << player1.knowledge_level << "\n";
    std::cout << "⚡ Learning Speed: " << player1.speed << "\n";
    std::cout << "🏰 Territories Learned: " << player1.territories_conquered << "/" << territories.size() << "\n";
    std::cout << "📖 4 Qul Learned: " << player1.learned_surahs.size() << "/4\n";
    std::cout << "📜 Hadith Learned: " << player1.learned_hadith.size() << "\n";
    
    int total_progress = (player1.territories_conquered * 20) + 
                        (player1.learned_surahs.size() * 20) + 
                        (player1.knowledge_level * 2);
    total_progress = std::min(100, total_progress);
    
    std::cout << "\n🎯 Overall Progress: " << total_progress << "%\n";
    
    // Progress bar
    std::cout << "[";
    for (int i = 0; i < 50; ++i) {
        if (i < total_progress/2) std::cout << "█";
        else std::cout << "░";
    }
    std::cout << "]\n";
}

std::string FarhaGame::generate_encouragement() {
    std::vector<std::string> encouragements = {
        "🌟 Masha'Allah! You're doing amazing!",
        "🎉 Subhan'Allah! Keep up the excellent work!",
        "📚 Alhamdulillah! Your knowledge is growing!",
        "🕌 Beautiful! You're making the Prophet (PBUH) proud!",
        "🎯 Excellent! You're on the path of success!",
        "📖 Wonderful! Keep seeking knowledge!",
        "🌅 Amazing! Every step forward is progress!",
        "💫 Fantastic! You're becoming a true scholar!"
    };
    
    return encouragements[rng() % encouragements.size()];
}

void FarhaGame::animate_progress(const std::string& message) {
    std::cout << message;
    for (int i = 0; i < 3; ++i) {
        std::cout << ".";
        std::cout.flush();
        std::this_thread::sleep_for(std::chrono::milliseconds(500));
    }
    std::cout << " ✅\n\n";
}

void FarhaGame::complete_game() {
    game_completed = true;
    
    std::cout << "\n\n🎉🎉🎉 CONGRATULATIONS! 🎉🎉🎉\n";
    std::cout << "═════════════════════════════════════════════\n\n";
    
    display_ascii_art();
    
    std::cout << "\n🌟 " << player1.name << ", you have successfully completed your Farha journey!\n\n";
    
    std::cout << "🏆 YOUR ACHIEVEMENTS:\n";
    std::cout << "📚 Final Knowledge Level: " << player1.knowledge_level << "\n";
    std::cout << "🏰 Territories Learned: " << player1.territories_conquered << "/" << territories.size() << "\n";
    std::cout << "📖 4 Qul Mastered: " << player1.learned_surahs.size() << "/4\n";
    std::cout << "📜 Hadith Collected: " << player1.learned_hadith.size() << "\n";
    std::cout << "🎓 Learning Turns: " << current_turn << "\n\n";
    
    std::cout << "🕌 You have helped establish the Rashiddun Caliphate through knowledge!\n";
    std::cout << "📚 You've learned about Islamic history and teachings!\n";
    std::cout << "🌟 You've become a true scholar of Islam!\n\n";
    
    std::cout << "💝 FINAL MESSAGE:\n";
    std::cout << "Remember what the Prophet Muhammad (PBUH) said:\n";
    std::cout << "&quot;Seek knowledge from the cradle to the grave.&quot;\n\n";
    
    std::cout << "🎊 Your journey with Farha may be complete,\n";
    std::cout << "but your journey of learning has just begun!\n\n";
    
    std::cout << "🌟 May Allah bless you with continued knowledge and wisdom! 🌟\n";
    std::cout << "═════════════════════════════════════════════\n\n";
}

bool FarhaGame::is_game_completed() const {
    return game_completed;
}

FarhaGame::~FarhaGame() {
    std::cout << "\n🤝 Thank you for playing Farha - Educational Caliphate Game!\n";
    std::cout << "📚 Keep learning and growing in knowledge and faith!\n";
    std::cout << "🕌 Assalamu Alaikum Warahmatullahi Wabarakatuh!\n";
}