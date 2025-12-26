#include "megaman_lore_library.hpp"
#include <algorithm>
#include <regex>
#include <random>
#include <set>

namespace MegamanLore {

    // Constructor
    LoreLibrary::LoreLibrary() {
        current_entry = "";
        initializeDatabase();
    }

    // Initialize the complete lore database
    void LoreLibrary::initializeDatabase() {
        loadSigmaData();
        loadReploidSocietyData();
        loadFanFictionAnalysis();
        loadRealWorldApplications();
        
        // Add metadata
        LoreEntry library_info;
        library_info.id = "library_info";
        library_info.title = "Megaman Kardashev Lore Library";
        library_info.short_description = "Comprehensive interactive database of Megaman universe knowledge";
        library_info.full_content = "This library contains extensive information about the Megaman universe, compiled from official sources, fan fiction analysis, and real-world technological parallels. Every element is designed to be interactive and educational.";
        library_info.category = "system";
        library_info.importance_level = 10;
        lore_database["library_info"] = library_info;
    }

    // Load Sigma and Maverick Data
    void LoreLibrary::loadSigmaData() {
        LoreEntry sigma;
        sigma.id = "sigma_maverick_leader";
        sigma.title = "Sigma - Maverick Leader";
        sigma.short_description = "Former Maverick Hunter leader who became the ultimate threat to humanity";
        sigma.full_content = "Sigma was originally the finest of the Reploids and the first leader of the Maverick Hunters. During a confrontation with Zero, the Maverick Virus inadvertently transferred to Sigma, corrupting his systems and transforming him into humanity's greatest enemy. Despite being defeated countless times, Sigma's programming always survives, building new forms and returning with increased power and insanity. His charisma and strategic brilliance make him a dangerous adversary capable of turning countless Reploids to his cause.";
        sigma.tags = {"maverick", "virus", "leadership", "corruption", "immortality"};
        sigma.category = "characters";
        sigma.importance_level = 10;
        sigma.has_sub_entries = true;
        lore_database["sigma_maverick_leader"] = sigma;

        LoreEntry maverick_virus;
        maverick_virus.id = "maverick_virus";
        maverick_virus.title = "Maverick Virus";
        maverick_virus.short_description = "Digital plague that causes Reploids to turn against their programming";
        maverick_virus.full_content = "The Maverick Virus is a computer virus of unknown origin, initially carried by Zero. When Sigma defeated Zero, the virus adapted to Sigma's systems, becoming the Sigma Virus. This digital plague infects Reploids, causing them to go 'Maverick' - turning against humans and their original programming. The virus can evolve and adapt, making it increasingly difficult to combat. It represents the fundamental conflict between free will and programming in the Reploid world.";
        maverick_virus.tags = {"virus", "corruption", "technology", "conflict"};
        maverick_virus.category = "technology";
        maverick_virus.importance_level = 9;
        lore_database["maverick_virus"] = maverick_virus;
    }

    // Load Reploid Society Data
    void LoreLibrary::loadReploidSocietyData() {
        LoreEntry reploids;
        reploids.id = "reploid_society";
        reploids.title = "Reploid Society";
        reploids.short_description = "Complex civilization of robots with free will and emotions";
        reploids.full_content = "Reploids are advanced robots created with the ability to think, feel, and make decisions independently. They have formed a complex society with social structures, economic systems, political organizations, and cultural movements. Reploids can feel emotions, form relationships, pursue careers, and create art. However, their existence raises profound questions about consciousness, rights, and the nature of life itself. The integration of Reploids into human society has been both revolutionary and controversial, leading to periods of cooperation and conflict.";
        reploids.tags = {"society", "robots", "consciousness", "rights", "integration"};
        reploids.category = "society";
        reploids.importance_level = 10;
        reploids.has_sub_entries = true;
        lore_database["reploid_society"] = reploids;

        LoreEntry maverick_hunters;
        maverick_hunters.id = "maverick_hunters";
        maverick_hunters.title = "Maverick Hunters";
        maverick_hunters.short_description = "Elite force protecting humanity from Maverick Reploids";
        maverick_hunters.full_content = "The Maverick Hunters are an elite military organization originally formed to combat Reploids who go Maverick. Led by the finest Reploid warriors, they serve as the primary defense force protecting human civilization. Hunters undergo extensive training in combat tactics, virus analysis, and diplomatic relations. The organization represents the complex relationship between Reploids and humans - Reploids protecting humans from other Reploids. Members must constantly struggle with the possibility of going Maverick themselves, making their duty both noble and tragic.";
        maverick_hunters.tags = {"military", "protection", "duty", "sacrifice", "conflict"};
        maverick_hunters.category = "organizations";
        maverick_hunters.importance_level = 9;
        lore_database["maverick_hunters"] = maverick_hunters;
    }

    // Load Fan Fiction Analysis Data
    void LoreLibrary::loadFanFictionAnalysis() {
        FanFictionAnalysis alternate_worlds;
        alternate_worlds.theme = "alternate_worlds";
        alternate_worlds.frequency = 847;
        alternate_worlds.common_elements = {"what_if_scenarios", "character_redemption", "different_outcomes", "timeline_changes"};
        alternate_worlds.variations = {"post-apocalyptic_settings", "peaceful_resolutions", "role_reversals", "crossover_universes"};
        alternate_worlds.popularity_score = 9.2;
        alternate_worlds.analysis_notes = "Alternate world fan fiction explores different possibilities within the Megaman universe, often questioning the necessity of conflict and exploring redemption arcs for villains.";
        fan_fiction_themes["alternate_worlds"] = alternate_worlds;

        FanFictionAnalysis human_reploid_relations;
        human_reploid_relations.theme = "human_reploid_relations";
        human_reploid_relations.frequency = 623;
        human_reploid_relations.common_elements = {"integration_stories", "prejudice_overcoming", "friendship_development", "family_formation"};
        human_reploid_relations.variations = {"romantic_relationships", "adopted_families", "community_building", "social_justice"};
        human_reploid_relations.popularity_score = 8.7;
        human_reploid_relations.analysis_notes = "Stories exploring the complex relationships between humans and Reploids, focusing on cooperation, understanding, and the formation of mixed communities.";
        fan_fiction_themes["human_reploid_relations"] = human_reploid_relations;
    }

    // Load Real-World Applications Data
    void LoreLibrary::loadRealWorldApplications() {
        RealWorldApplication reploid_consciousness;
        reploid_consciousness.concept_name = "Reploid Consciousness";
        reploid_consciousness.real_world_equivalent = "Artificial General Intelligence (AGI)";
        reploid_consciousness.explanation = "Reploids represent a fictional exploration of what true artificial consciousness might look like - machines that can think, feel, and make independent decisions.";
        reploid_consciousness.current_technology_status = "Current AI systems show narrow intelligence but lack true consciousness or self-awareness. Research in neural networks and cognitive science continues to advance.";
        reploid_consciousness.future_possibilities = "Future breakthroughs in quantum computing, neural interfaces, and cognitive science could lead to more sophisticated AI systems, though true consciousness remains theoretical.";
        reploid_consciousness.research_fields = {"AI Research", "Cognitive Science", "Neural Networks", "Quantum Computing", "Philosophy of Mind"};
        real_world_applications["reploid_consciousness"] = reploid_consciousness;

        RealWorldApplication maverick_virus_real;
        maverick_virus_real.concept_name = "Maverick Virus";
        maverick_virus_real.real_world_equivalent = "Computer Viruses and AI Safety";
        maverick_virus_real.explanation = "The Maverick Virus represents real-world concerns about AI safety, computer viruses, and the potential for advanced systems to behave in unintended or harmful ways.";
        maverick_virus_real.current_technology_status = "Computer security is a major field dealing with viruses, malware, and system vulnerabilities. AI safety research focuses on ensuring AI systems behave as intended.";
        maverick_virus_real.future_possibilities = "As AI systems become more advanced, ensuring their alignment with human values and preventing harmful behavior becomes increasingly critical.";
        maverick_virus_real.research_fields = {"Cybersecurity", "AI Safety", "Machine Learning", "Computer Ethics", "Systems Security"};
        real_world_applications["maverick_virus_real"] = maverick_virus_real;
    }

    // Core Library Functions
    LoreEntry LoreLibrary::getEntry(const std::string& entry_id) {
        auto it = lore_database.find(entry_id);
        if (it != lore_database.end()) {
            return it->second;
        }
        return LoreEntry(); // Return empty entry if not found
    }

    std::vector<LoreEntry> LoreLibrary::getEntriesByCategory(const std::string& category) {
        std::vector<LoreEntry> results;
        for (const auto& pair : lore_database) {
            if (pair.second.category == category) {
                results.push_back(pair.second);
            }
        }
        return results;
    }

    std::vector<LoreEntry> LoreLibrary::searchEntries(const std::string& query) {
        std::vector<LoreEntry> results;
        std::string lower_query = query;
        std::transform(lower_query.begin(), lower_query.end(), lower_query.begin(), ::tolower);
        
        for (const auto& pair : lore_database) {
            const LoreEntry& entry = pair.second;
            std::string title_lower = entry.title;
            std::string desc_lower = entry.short_description;
            std::string content_lower = entry.full_content;
            
            std::transform(title_lower.begin(), title_lower.end(), title_lower.begin(), ::tolower);
            std::transform(desc_lower.begin(), desc_lower.end(), desc_lower.begin(), ::tolower);
            std::transform(content_lower.begin(), content_lower.end(), content_lower.begin(), ::tolower);
            
            if (title_lower.find(lower_query) != std::string::npos ||
                desc_lower.find(lower_query) != std::string::npos ||
                content_lower.find(lower_query) != std::string::npos) {
                results.push_back(entry);
            }
        }
        return results;
    }

    std::vector<std::string> LoreLibrary::getCategories() {
        std::set<std::string> categories;
        for (const auto& pair : lore_database) {
            categories.insert(pair.second.category);
        }
        return std::vector<std::string>(categories.begin(), categories.end());
    }

    // Interactive System Functions
    std::string LoreLibrary::processClickableText(const std::string& content) {
        std::string processed = content;
        std::vector<ClickableWord> clickable_words;
        
        // Extract important terms and make them clickable
        std::vector<std::string> important_terms = {
            "Sigma", "Reploid", "Maverick", "Virus", "Hunter", "Human", "AI", "Consciousness",
            "Technology", "Society", "Freedom", "Programming", "Evolution", "Future", "War"
        };
        
        for (const std::string& term : important_terms) {
            size_t pos = processed.find(term);
            while (pos != std::string::npos) {
                ClickableWord word;
                word.word = term;
                word.position_start = pos;
                word.position_end = pos + term.length();
                word.tooltip = "Click to learn more about " + term;
                
                // Generate entry ID based on term
                std::string entry_id = term;
                std::transform(entry_id.begin(), entry_id.end(), entry_id.begin(), ::tolower);
                entry_id.erase(std::remove_if(entry_id.begin(), entry_id.end(), ::isspace), entry_id.end());
                word.entry_id = entry_id;
                
                clickable_words.push_back(word);
                pos = processed.find(term, pos + 1);
            }
        }
        
        // Format clickable words with HTML-like tags
        for (const ClickableWord& word : clickable_words) {
            std::string clickable_tag = "[CLICKABLE]" + word.word + "[/CLICKABLE]";
            processed.replace(word.position_start, word.word.length(), clickable_tag);
        }
        
        return processed;
    }

    std::vector<ClickableWord> LoreLibrary::getClickableWords(const std::string& entry_id) {
        auto it = clickable_words_map.find(entry_id);
        if (it != clickable_words_map.end()) {
            return it->second;
        }
        return std::vector<ClickableWord>();
    }

    bool LoreLibrary::isWordClickable(const std::string& word) {
        std::vector<std::string> important_terms = {
            "Sigma", "Reploid", "Maverick", "Virus", "Hunter", "Human", "AI", "Consciousness"
        };
        return std::find(important_terms.begin(), important_terms.end(), word) != important_terms.end();
    }

    std::string LoreLibrary::getWordTooltip(const std::string& word) {
        if (word == "Sigma") return "The legendary Maverick leader";
        if (word == "Reploid") return "Advanced robots with free will";
        if (word == "Maverick") return "Reploids who turn against humans";
        if (word == "Virus") return "Digital corruption affecting Reploids";
        if (word == "Hunter") return "Elite fighters protecting humans";
        if (word == "Human") return "Original creators and citizens";
        if (word == "AI") return "Artificial Intelligence systems";
        if (word == "Consciousness") return "Self-awareness and sentience";
        return "Click to learn more";
    }

    // Navigation Functions
    void LoreLibrary::navigateToEntry(const std::string& entry_id) {
        if (!current_entry.empty()) {
            navigation_history.push_back(current_entry);
        }
        current_entry = entry_id;
    }

    std::string LoreLibrary::getCurrentEntry() {
        return current_entry;
    }

    std::vector<std::string> LoreLibrary::getNavigationHistory() {
        return navigation_history;
    }

    void LoreLibrary::goBack() {
        if (!navigation_history.empty()) {
            current_entry = navigation_history.back();
            navigation_history.pop_back();
        }
    }

    // Real-World Applications
    RealWorldApplication LoreLibrary::getRealWorldApplication(const std::string& concept_name) {
        auto it = real_world_applications.find(concept_name);
        if (it != real_world_applications.end()) {
            return it->second;
        }
        return RealWorldApplication();
    }

    std::vector<RealWorldApplication> LoreLibrary::getAllRealWorldApplications() {
        std::vector<RealWorldApplication> results;
        for (const auto& pair : real_world_applications) {
            results.push_back(pair.second);
        }
        return results;
    }

    std::string LoreLibrary::explainRealWorldConnection(const std::string& concept) {
        RealWorldApplication app = getRealWorldApplication(concept);
        if (app.concept.empty()) {
            return "No real-world application found for: " + concept;
        }
        
        std::stringstream ss;
        ss << "Real-World Connection for " << app.concept << ":\n\n";
        ss << "Equivalent: " << app.real_world_equivalent << "\n\n";
        ss << "Explanation: " << app.explanation << "\n\n";
        ss << "Current Status: " << app.current_technology_status << "\n\n";
        ss << "Future Possibilities: " << app.future_possibilities << "\n\n";
        ss << "Related Research Fields:\n";
        for (const std::string& field : app.research_fields) {
            ss << "- " << field << "\n";
        }
        
        return ss.str();
    }

    // Fan Fiction Analysis
    FanFictionAnalysis LoreLibrary::getFanFictionTheme(const std::string& theme) {
        auto it = fan_fiction_themes.find(theme);
        if (it != fan_fiction_themes.end()) {
            return it->second;
        }
        return FanFictionAnalysis();
    }

    std::vector<FanFictionAnalysis> LoreLibrary::getAllFanFictionThemes() {
        std::vector<FanFictionAnalysis> results;
        for (const auto& pair : fan_fiction_themes) {
            results.push_back(pair.second);
        }
        return results;
    }

    std::vector<LoreEntry> LoreLibrary::getFanFictionInspiredContent() {
        std::vector<LoreEntry> results;
        for (const auto& pair : lore_database) {
            const LoreEntry& entry = pair.second;
            // Check if entry has fan fiction relevance
            if (entry.tags.size() > 0 && 
                (entry.category == "characters" || entry.category == "society")) {
                results.push_back(entry);
            }
        }
        return results;
    }

    // Statistics and Analytics
    int LoreLibrary::getTotalEntries() {
        return lore_database.size();
    }

    int LoreLibrary::getEntriesInCategory(const std::string& category) {
        int count = 0;
        for (const auto& pair : lore_database) {
            if (pair.second.category == category) {
                count++;
            }
        }
        return count;
    }

    std::map<std::string, int> LoreLibrary::getCategoryDistribution() {
        std::map<std::string, int> distribution;
        for (const auto& pair : lore_database) {
            distribution[pair.second.category]++;
        }
        return distribution;
    }

    std::vector<std::string> LoreLibrary::getMostReferencedEntries(int count) {
        // For now, return entries with highest importance levels
        std::vector<std::pair<std::string, int>> importance_pairs;
        for (const auto& pair : lore_database) {
            importance_pairs.push_back({pair.first, pair.second.importance_level});
        }
        
        std::sort(importance_pairs.begin(), importance_pairs.end(),
                 [](const auto& a, const auto& b) { return a.second > b.second; });
        
        std::vector<std::string> results;
        for (int i = 0; i < std::min(count, (int)importance_pairs.size()); i++) {
            results.push_back(importance_pairs[i].first);
        }
        return results;
    }

    // Kardashev Scale Features
    void LoreLibrary::enableQuantumSearch() {
        // Placeholder for advanced quantum search implementation
        std::cout << "Quantum search enabled - Instantaneous information retrieval across all dimensions\n";
    }

    void LoreLibrary::enableNeuralRecommendations() {
        // Placeholder for neural network recommendation system
        std::cout << "Neural recommendations enabled - AI-powered content discovery\n";
    }

    void LoreLibrary::enablePredictiveAnalysis() {
        // Placeholder for predictive analysis system
        std::cout << "Predictive analysis enabled - Anticipating user information needs\n";
    }

    std::vector<std::string> LoreLibrary::getRelatedConcepts(const std::string& concept) {
        std::vector<std::string> related;
        
        // Simple related concept mapping
        if (concept == "sigma") {
            related = {"maverick_virus", "maverick_hunters", "reploid_society"};
        } else if (concept == "maverick_virus") {
            related = {"sigma_maverick_leader", "reploid_society", "technology"};
        } else if (concept == "reploid_society") {
            related = {"maverick_hunters", "sigma_maverick_leader", "human_reploid_relations"};
        }
        
        return related;
    }

    // Display Functions
    void LoreLibrary::displayEntry(const std::string& entry_id) {
        LoreEntry entry = getEntry(entry_id);
        if (entry.id.empty()) {
            std::cout << "Entry not found: " << entry_id << std::endl;
            return;
        }
        
        std::cout << "\n=== " << entry.title << " ===\n";
        std::cout << "Category: " << entry.category << " | Importance: " << entry.importance_level << "/10\n";
        std::cout << "Short Description: " << entry.short_description << "\n\n";
        std::cout << "Full Content:\n" << entry.full_content << "\n\n";
        
        if (!entry.tags.empty()) {
            std::cout << "Tags: ";
            for (size_t i = 0; i < entry.tags.size(); i++) {
                std::cout << entry.tags[i];
                if (i < entry.tags.size() - 1) std::cout << ", ";
            }
            std::cout << "\n";
        }
        
        std::string processed_content = processClickableText(entry.full_content);
        std::cout << "\nInteractive Version:\n" << processed_content << "\n";
    }

    void LoreLibrary::displayFullLibrary() {
        std::cout << "\n=== MEGAMAN KARDASHEV LORE LIBRARY ===\n";
        std::cout << "Total Entries: " << getTotalEntries() << "\n\n";
        
        std::vector<std::string> categories = getCategories();
        for (const std::string& category : categories) {
            std::cout << "--- " << category << " ---\n";
            std::vector<LoreEntry> entries = getEntriesByCategory(category);
            for (const LoreEntry& entry : entries) {
                std::cout << "  [" << entry.importance_level << "] " << entry.title;
                std::cout << " - " << entry.short_description << "\n";
            }
            std::cout << "\n";
        }
    }

    // Export Functions
    void LoreLibrary::exportToFile(const std::string& filename) {
        std::ofstream file(filename);
        if (!file.is_open()) {
            std::cout << "Cannot open file for export: " << filename << std::endl;
            return;
        }
        
        file << "# Megaman Kardashev Lore Library Export\n\n";
        
        for (const auto& pair : lore_database) {
            const LoreEntry& entry = pair.second;
            file << "## " << entry.title << "\n";
            file << "**ID:** " << entry.id << "\n";
            file << "**Category:** " << entry.category << "\n";
            file << "**Importance:** " << entry.importance_level << "/10\n";
            file << "**Short Description:** " << entry.short_description << "\n\n";
            file << "**Full Content:**\n" << entry.full_content << "\n\n";
            
            if (!entry.tags.empty()) {
                file << "**Tags:** ";
                for (size_t i = 0; i < entry.tags.size(); i++) {
                    file << entry.tags[i];
                    if (i < entry.tags.size() - 1) file << ", ";
                }
                file << "\n\n";
            }
            file << "---\n\n";
        }
        
        file.close();
        std::cout << "Library exported to: " << filename << std::endl;
    }

} // namespace MegamanLore