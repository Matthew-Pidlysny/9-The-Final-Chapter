/*
    * ChromaticOlympics.h - Chromatic Olympics Workshop
    */

    #ifndef CHROMATIC_OLYMPICS_H
    #define CHROMATIC_OLYMPICS_H

    class PlanePilotApp;

    namespace PlanePilot {
    namespace Workshops {

    class ChromaticOlympics {
    public:
        explicit ChromaticOlympics(PlanePilotApp* app);
        ~ChromaticOlympics();
        
        bool initialize();
        void update();
        void render();
        void handleInput();

    private:
        PlanePilotApp* m_app;
    };

    } // namespace Workshops
    } // namespace PlanePilot

    #endif // CHROMATIC_OLYMPICS_H