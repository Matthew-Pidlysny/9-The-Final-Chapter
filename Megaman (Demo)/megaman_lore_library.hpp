#ifndef MEGAMAN_LORE_LIBRARY_HPP
#define MEGAMAN_LORE_LIBRARY_HPP

#include <string>
#include <vector>
#include <map>
#include <unordered_map>
#include <memory>
#include <functional>
#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>

namespace MegamanLore {

    // Core Lore Entry Structure
    struct LoreEntry {
        std::string id;
        std::string title;
        std::string short_description;
        std::string full_content;
        std::vector<std::string> tags;
        std::vector<std::string> references;
        std::vector<std::string> related_entries;
        std::string category;
        int importance_level;  // 1-10 scale
        bool is_clickable;
        bool has_sub_entries;
        
        LoreEntry() : importance_level(5), is_clickable(true), has_sub_entries(false) {}
    };

    // Interactive Word System
    struct ClickableWord {
        std::string word;
        std::string entry_id;
        std::string tooltip;
        int position_start;
        int position_end;
    };

    // Real-World Application Structure
    struct RealWorldApplication {
        std::string concept_name;
        std::string real_world_equivalent;
        std::string explanation;
        std::string current_technology_status;
        std::string future_possibilities;
        std::vector<std::string> research_fields;
    };

    // Fan Fiction Analysis Structure
    struct FanFictionAnalysis {
        std::string theme;
        int frequency;  // How often this appears in fan fiction
        std::vector<std::string> common_elements;
        std::vector<std::string> variations;
        double popularity_score;  // Based on community engagement
        std::string analysis_notes;
    };

    // Main Lore Library Class
    class LoreLibrary {
    private:
        std::unordered_map<std::string, LoreEntry> lore_database;
        std::unordered_map<std::string, std::vector<ClickableWord>> clickable_words_map;
        std::unordered_map<std::string, RealWorldApplication> real_world_applications;
        std::unordered_map<std::string, FanFictionAnalysis> fan_fiction_themes;
        std::vector<std::string> navigation_history;
        std::string current_entry;
        
        // Internal helper methods
        std::string extractClickableWords(const std::string& content, const std::string& entry_id);
        void loadSigmaData();
        void loadReploidSocietyData();
        void loadFanFictionAnalysis();
        void loadRealWorldApplications();
        
    public:
        // Constructor
        LoreLibrary();
        
        // Core Library Functions
        void initializeDatabase();
        LoreEntry getEntry(const std::string& entry_id);
        std::vector<LoreEntry> getEntriesByCategory(const std::string& category);
        std::vector<LoreEntry> searchEntries(const std::string& query);
        std::vector<std::string> getCategories();
        
        // Interactive System Functions
        std::string processClickableText(const std::string& content);
        std::vector<ClickableWord> getClickableWords(const std::string& entry_id);
        bool isWordClickable(const std::string& word);
        std::string getWordTooltip(const std::string& word);
        
        // Navigation Functions
        void navigateToEntry(const std::string& entry_id);
        std::string getCurrentEntry();
        std::vector<std::string> getNavigationHistory();
        void goBack();
        
        // Real-World Applications
        RealWorldApplication getRealWorldApplication(const std::string& concept_name);
        std::vector<RealWorldApplication> getAllRealWorldApplications();
        std::string explainRealWorldConnection(const std::string& concept_name);
        
        // Fan Fiction Analysis
        FanFictionAnalysis getFanFictionTheme(const std::string& theme);
        std::vector<FanFictionAnalysis> getAllFanFictionThemes();
        std::vector<LoreEntry> getFanFictionInspiredContent();
        
        // Export/Import Functions
        void exportToFile(const std::string& filename);
        void importFromFile(const std::string& filename);
        std::string generateInteractiveHTML();
        
        // Statistics and Analytics
        int getTotalEntries();
        int getEntriesInCategory(const std::string& category);
        std::map<std::string, int> getCategoryDistribution();
        std::vector<std::string> getMostReferencedEntries(int count = 10);
        
        // Kardashev Scale Features
        void enableQuantumSearch();
        void enableNeuralRecommendations();
        void enablePredictiveAnalysis();
        std::vector<std::string> getRelatedConcepts(const std::string& concept_name);
        
        // Advanced Features
        void addCustomEntry(const LoreEntry& entry);
        void updateEntry(const std::string& entry_id, const LoreEntry& updated_entry);
        void deleteEntry(const std::string& entry_id);
        bool entryExists(const std::string& entry_id);
        
        // Display Functions
        void displayEntry(const std::string& entry_id);
        void displayEntrySummary(const std::string& entry_id);
        void displayCategoryOverview(const std::string& category);
        void displayFullLibrary();
    };

    // Helper Classes
    class TextProcessor {
    public:
        static std::vector<std::string> tokenize(const std::string& text);
        static std::string highlightClickableWords(const std::string& text, 
                                                  const std::vector<ClickableWord>& words);
        static std::string generateTooltip(const std::string& word, const std::string& description);
        static bool isImportantTerm(const std::string& word);
    };

    class SearchEngine {
    private:
        LoreLibrary* library;
        
    public:
        SearchEngine(LoreLibrary* lib) : library(lib) {}
        
        std::vector<LoreEntry> advancedSearch(const std::string& query, 
                                             const std::vector<std::string>& filters = {});
        std::vector<LoreEntry> searchByTag(const std::string& tag);
        std::vector<LoreEntry> searchByImportance(int min_level, int max_level = 10);
        std::vector<LoreEntry> getRelatedEntries(const std::string& entry_id);
    };

    class RecommendationSystem {
    private:
        LoreLibrary* library;
        
    public:
        RecommendationSystem(LoreLibrary* lib) : library(lib) {}
        
        std::vector<LoreEntry> getRecommendations(const std::string& entry_id);
        std::vector<LoreEntry> getPopularEntries();
        std::vector<LoreEntry> getTrendingTopics();
        std::vector<LoreEntry> getBeginnerRecommendations();
    };

} // namespace MegamanLore

#endif // MEGAMAN_LORE_LIBRARY_HPP