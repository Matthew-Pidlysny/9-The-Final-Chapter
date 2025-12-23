/*
    * Renderer.h - Graphics Renderer
    */

    #ifndef RENDERER_H
    #define RENDERER_H

    namespace PlanePilot {
    namespace Graphics {

    class Renderer {
    public:
        Renderer();
        ~Renderer();
        
        bool initialize(int width, int height);
        void resize(int width, int height);
        void beginFrame();
        void endFrame();

    private:
        int m_width;
        int m_height;
    };

    } // namespace Graphics
    } // namespace PlanePilot

    #endif // RENDERER_H