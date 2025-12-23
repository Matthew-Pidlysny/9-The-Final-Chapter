/*
    * GeometrySequencing.h - Geometry Sequencing Workshop
    */

    #ifndef GEOMETRY_SEQUENCING_H
    #define GEOMETRY_SEQUENCING_H

    class PlanePilotApp;

    namespace PlanePilot {
    namespace Workshops {

    class GeometrySequencing {
    public:
        explicit GeometrySequencing(PlanePilotApp* app);
        ~GeometrySequencing();
        
        bool initialize();
        void update();
        void render();
        void handleInput();

    private:
        PlanePilotApp* m_app;
    };

    } // namespace Workshops
    } // namespace PlanePilot

    #endif // GEOMETRY_SEQUENCING_H