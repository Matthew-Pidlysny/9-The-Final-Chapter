#ifndef SHADER_H
#define SHADER_H

#include <string>
#include <fstream>
#include <sstream>
#include <iostream>
#include <GL/glew.h>

class Shader {
public:
    Shader();
    Shader(const std::string& vertexPath, const std::string& fragmentPath);
    ~Shader();
    
    bool load(const std::string& vertexPath, const std::string& fragmentPath);
    void use();
    
    // Utility uniform functions
    void setBool(const std::string& name, bool value);
    void setInt(const std::string& name, int value);
    void setFloat(const std::string& name, float value);
    void setVec2(const std::string& name, const float* value);
    void setVec3(const std::string& name, const float* value);
    void setVec4(const std::string& name, const float* value);
    void setMat2(const std::string& name, const float* value);
    void setMat3(const std::string& name, const float* value);
    void setMat4(const std::string& name, const float* value);
    
    // GLM overloads
    void setVec2(const std::string& name, float x, float y);
    void setVec3(const std::string& name, float x, float y, float z);
    void setVec4(const std::string& name, float x, float y, float z, float w);
    
    bool isLoaded() const { return m_loaded; }
    unsigned int getID() const { return m_ID; }
    
private:
    unsigned int m_ID;
    bool m_loaded;
    
    void checkCompileErrors(GLuint shader, std::string type);
    std::string loadShaderSource(const std::string& filePath);
};

#endif // SHADER_H