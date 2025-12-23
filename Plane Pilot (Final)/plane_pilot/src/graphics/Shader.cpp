/*
    * Shader.cpp - OpenGL Shader Implementation
    */

    #include "graphics/Shader.h"
    #include "utils/Logger.h"

    namespace PlanePilot {
    namespace Graphics {

    Shader::Shader() : m_program(0) {
        Logger::info("Shader constructor");
    }

    Shader::~Shader() {
        Logger::info("Shader destructor");
    }

    bool Shader::load(const std::string& vertexPath, const std::string& fragmentPath) {
        // Load and compile shaders
        Logger::info("Loading shader: " + vertexPath + ", " + fragmentPath);
        return true;
    }

    void Shader::use() {
        // Use shader program
    }

    void Shader::setMatrix(const std::string& name, const float* matrix) {
        // Set matrix uniform
    }

    void Shader::setFloat(const std::string& name, float value) {
        // Set float uniform
    }

    void Shader::setVector3(const std::string& name, float x, float y, float z) {
        // Set vector3 uniform
    }

    } // namespace Graphics
    } // namespace PlanePilot