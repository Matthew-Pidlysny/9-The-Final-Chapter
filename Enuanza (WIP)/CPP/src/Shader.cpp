#include "Shader.h"
#include <glm/glm.hpp>
#include <glm/gtc/type_ptr.hpp>

Shader::Shader() : m_ID(0), m_loaded(false) {
}

Shader::Shader(const std::string& vertexPath, const std::string& fragmentPath) : m_ID(0), m_loaded(false) {
    load(vertexPath, fragmentPath);
}

Shader::~Shader() {
    if (m_loaded) {
        glDeleteProgram(m_ID);
    }
}

bool Shader::load(const std::string& vertexPath, const std::string& fragmentPath) {
    // Load shader sources
    std::string vertexCode = loadShaderSource(vertexPath);
    std::string fragmentCode = loadShaderSource(fragmentPath);
    
    if (vertexCode.empty() || fragmentCode.empty()) {
        std::cerr << "Failed to load shader files" << std::endl;
        return false;
    }
    
    const char* vShaderCode = vertexCode.c_str();
    const char* fShaderCode = fragmentCode.c_str();
    
    // Compile shaders
    GLuint vertex, fragment;
    
    // Vertex Shader
    vertex = glCreateShader(GL_VERTEX_SHADER);
    glShaderSource(vertex, 1, &vShaderCode, NULL);
    glCompileShader(vertex);
    checkCompileErrors(vertex, "VERTEX");
    
    // Fragment Shader
    fragment = glCreateShader(GL_FRAGMENT_SHADER);
    glShaderSource(fragment, 1, &fShaderCode, NULL);
    glCompileShader(fragment);
    checkCompileErrors(fragment, "FRAGMENT");
    
    // Shader Program
    m_ID = glCreateProgram();
    glAttachShader(m_ID, vertex);
    glAttachShader(m_ID, fragment);
    glLinkProgram(m_ID);
    checkCompileErrors(m_ID, "PROGRAM");
    
    // Delete shaders as they're linked into our program now
    glDeleteShader(vertex);
    glDeleteShader(fragment);
    
    m_loaded = true;
    return true;
}

void Shader::use() {
    if (m_loaded) {
        glUseProgram(m_ID);
    }
}

void Shader::setBool(const std::string& name, bool value) {
    if (m_loaded) {
        glUniform1i(glGetUniformLocation(m_ID, name.c_str()), (int)value);
    }
}

void Shader::setInt(const std::string& name, int value) {
    if (m_loaded) {
        glUniform1i(glGetUniformLocation(m_ID, name.c_str()), value);
    }
}

void Shader::setFloat(const std::string& name, float value) {
    if (m_loaded) {
        glUniform1f(glGetUniformLocation(m_ID, name.c_str()), value);
    }
}

void Shader::setVec2(const std::string& name, const float* value) {
    if (m_loaded) {
        glUniform2fv(glGetUniformLocation(m_ID, name.c_str()), 1, value);
    }
}

void Shader::setVec3(const std::string& name, const float* value) {
    if (m_loaded) {
        glUniform3fv(glGetUniformLocation(m_ID, name.c_str()), 1, value);
    }
}

void Shader::setVec4(const std::string& name, const float* value) {
    if (m_loaded) {
        glUniform4fv(glGetUniformLocation(m_ID, name.c_str()), 1, value);
    }
}

void Shader::setMat2(const std::string& name, const float* value) {
    if (m_loaded) {
        glUniformMatrix2fv(glGetUniformLocation(m_ID, name.c_str()), 1, GL_FALSE, value);
    }
}

void Shader::setMat3(const std::string& name, const float* value) {
    if (m_loaded) {
        glUniformMatrix3fv(glGetUniformLocation(m_ID, name.c_str()), 1, GL_FALSE, value);
    }
}

void Shader::setMat4(const std::string& name, const float* value) {
    if (m_loaded) {
        glUniformMatrix4fv(glGetUniformLocation(m_ID, name.c_str()), 1, GL_FALSE, value);
    }
}

// GLM overloads
void Shader::setVec2(const std::string& name, float x, float y) {
    float val[2] = {x, y};
    setVec2(name, val);
}

void Shader::setVec3(const std::string& name, float x, float y, float z) {
    float val[3] = {x, y, z};
    setVec3(name, val);
}

void Shader::setVec4(const std::string& name, float x, float y, float z, float w) {
    float val[4] = {x, y, z, w};
    setVec4(name, val);
}

void Shader::checkCompileErrors(GLuint shader, std::string type) {
    GLint success;
    GLchar infoLog[1024];
    
    if (type != "PROGRAM") {
        glGetShaderiv(shader, GL_COMPILE_STATUS, &success);
        if (!success) {
            glGetShaderInfoLog(shader, 1024, NULL, infoLog);
            std::cerr << "ERROR::SHADER_COMPILATION_ERROR of type: " << type << "\n" 
                      << infoLog << "\n -- --------------------------------------------------- -- " << std::endl;
        }
    } else {
        glGetProgramiv(shader, GL_LINK_STATUS, &success);
        if (!success) {
            glGetProgramInfoLog(shader, 1024, NULL, infoLog);
            std::cerr << "ERROR::PROGRAM_LINKING_ERROR of type: " << type << "\n" 
                      << infoLog << "\n -- --------------------------------------------------- -- " << std::endl;
        }
    }
}

std::string Shader::loadShaderSource(const std::string& filePath) {
    std::ifstream shaderFile;
    std::stringstream shaderStream;
    
    // Ensure ifstream objects can throw exceptions
    shaderFile.exceptions(std::ifstream::failbit | std::ifstream::badbit);
    
    try {
        // Open files
        shaderFile.open(filePath);
        
        // Read file's buffer contents into streams
        shaderStream << shaderFile.rdbuf();
        
        // Close file handlers
        shaderFile.close();
        
        // Convert stream into string
        return shaderStream.str();
    } catch (std::ifstream::failure& e) {
        std::cerr << "ERROR::SHADER::FILE_NOT_SUCCESSFULLY_READ: " << filePath << std::endl;
        return "";
    }
}