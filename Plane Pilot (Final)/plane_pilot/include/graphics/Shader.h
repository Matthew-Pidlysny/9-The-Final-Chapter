/*
    * Shader.h - OpenGL Shader
    */

    #ifndef SHADER_H
    #define SHADER_H

    #include <string>

    namespace PlanePilot {
    namespace Graphics {

    class Shader {
    public:
        Shader();
        ~Shader();
        
        bool load(const std::string& vertexPath, const std::string& fragmentPath);
        void use();
        void setMatrix(const std::string& name, const float* matrix);
        void setFloat(const std::string& name, float value);
        void setVector3(const std::string& name, float x, float y, float z);

    private:
        unsigned int m_program;
    };

    } // namespace Graphics
    } // namespace PlanePilot

    #endif // SHADER_H