/*
    * FontManager.h - Font Management System
    */

    #ifndef FONT_MANAGER_H
    #define FONT_MANAGER_H

    #include <string>
    #include <unordered_map>

    namespace PlanePilot {
    namespace GUI {

    class FontManager {
    public:
        FontManager();
        ~FontManager();
        
        bool initialize();
        void shutdown();
        
        void loadFont(const std::string& name, const std::string& path);
        void* getFont(const std::string& name) const;
        
    private:
        std::unordered_map<std::string, void*> m_fonts;
        bool m_initialized;
    };

    } // namespace GUI
    } // namespace PlanePilot

    #endif // FONT_MANAGER_H