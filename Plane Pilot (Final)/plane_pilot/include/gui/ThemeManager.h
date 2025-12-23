/*
    * ThemeManager.h - Theme Management System
    */

    #ifndef THEME_MANAGER_H
    #define THEME_MANAGER_H

    #include <string>
    #include <unordered_map>

    namespace PlanePilot {
    namespace GUI {

    struct ThemeColors {
        float background[4];
        float foreground[4];
        float accent[4];
        float highlight[4];
    };

    class ThemeManager {
    public:
        ThemeManager();
        ~ThemeManager();
        
        bool initialize();
        void shutdown();
        
        void loadDefaultTheme();
        void loadTheme(const std::string& name);
        
        const ThemeColors& getCurrentTheme() const;
        const float* getBackgroundColor() const;
        const float* getForegroundColor() const;
        const float* getAccentColor() const;
        
    private:
        std::unordered_map<std::string, ThemeColors> m_themes;
        std::string m_currentTheme;
        bool m_initialized;
    };

    } // namespace GUI
    } // namespace PlanePilot

    #endif // THEME_MANAGER_H