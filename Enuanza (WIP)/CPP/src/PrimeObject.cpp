#include "PrimeComposition3D.h"
#include <iostream>
#include <cmath>

namespace Enuanza {

PrimeObject::PrimeObject(int prime, const glm::vec3& position) 
    : m_prime(prime), m_data(prime), m_position(position)
    , m_rotation(0.0f), m_scale(0.1f) {
    
    updateColor();
}

PrimeObject::~PrimeObject() {
    cleanup();
}

void PrimeObject::initialize() {
    createGeometry();
    std::cout << "Prime object " << m_prime << " initialized" << std::endl;
}

void PrimeObject::cleanup() {
    if (m_VAO) glDeleteVertexArrays(1, &m_VAO);
    if (m_VBO) glDeleteBuffers(1, &m_VBO);
    if (m_EBO) glDeleteBuffers(1, &m_EBO);
}

void PrimeObject::update(float deltaTime) {
    // Rotate based on prime properties
    float rotationSpeed = 1.0f + (m_prime % 7) * 0.5f;
    m_rotation.y += rotationSpeed * deltaTime;
    m_rotation.x += rotationSpeed * 0.5f * deltaTime;
    
    // Update color based on energy
    updateColor();
    
    // Pulsing scale based on lambda energy
    float pulseFactor = 1.0f + sin(m_data.lambdaEnergy * deltaTime * 2.0f) * 0.1f;
    m_scale = 0.05f + m_prime * 0.0001f * pulseFactor;
}

void PrimeObject::render(const glm::mat4& viewMatrix, const glm::mat4& projectionMatrix) {
    if (!m_VAO) return;
    
    glm::mat4 model = glm::mat4(1.0f);
    model = glm::translate(model, m_position);
    model = glm::rotate(model, m_rotation.x, glm::vec3(1.0f, 0.0f, 0.0f));
    model = glm::rotate(model, m_rotation.y, glm::vec3(0.0f, 1.0f, 0.0f));
    model = glm::rotate(model, m_rotation.z, glm::vec3(0.0f, 0.0f, 1.0f));
    model = glm::scale(model, glm::vec3(m_scale));
    
    // Set shader uniforms (assuming shader is already in use)
    // if (m_shader && m_shader->isLoaded()) {
    //     m_shader->setMat4("model", model);
    //     m_shader->setVec4("objectColor", glm::value_ptr(m_color));
    // }
    
    glBindVertexArray(m_VAO);
    glDrawElements(GL_TRIANGLES, 36, GL_UNSIGNED_INT, 0);
    glBindVertexArray(0);
}

void PrimeObject::createGeometry() {
    // Create a cube for each prime (simple geometry)
    float size = 1.0f;
    std::vector<float> vertices = {
        // Front face
        -size, -size,  size,
         size, -size,  size,
         size,  size,  size,
        -size,  size,  size,
        // Back face
        -size, -size, -size,
        -size,  size, -size,
         size,  size, -size,
         size, -size, -size,
        // Top face
        -size,  size, -size,
        -size,  size,  size,
         size,  size,  size,
         size,  size, -size,
        // Bottom face
        -size, -size, -size,
         size, -size, -size,
         size, -size,  size,
        -size, -size,  size,
        // Right face
         size, -size, -size,
         size,  size, -size,
         size,  size,  size,
         size, -size,  size,
        // Left face
        -size, -size, -size,
        -size, -size,  size,
        -size,  size,  size,
        -size,  size, -size
    };
    
    std::vector<unsigned int> indices = {
        0,  1,  2,  0,  2,  3,    // Front
        4,  5,  6,  4,  6,  7,    // Back
        8,  9,  10, 8,  10, 11,   // Top
        12, 13, 14, 12, 14, 15,   // Bottom
        16, 17, 18, 16, 18, 19,   // Right
        20, 21, 22, 20, 22, 23    // Left
    };
    
    // Generate OpenGL objects
    glGenVertexArrays(1, &m_VAO);
    glGenBuffers(1, &m_VBO);
    glGenBuffers(1, &m_EBO);
    
    // Bind and fill VAO
    glBindVertexArray(m_VAO);
    
    // Bind and fill VBO
    glBindBuffer(GL_ARRAY_BUFFER, m_VBO);
    glBufferData(GL_ARRAY_BUFFER, vertices.size() * sizeof(float), vertices.data(), GL_STATIC_DRAW);
    
    // Bind and fill EBO
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, m_EBO);
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices.size() * sizeof(unsigned int), 
                indices.data(), GL_STATIC_DRAW);
    
    // Set vertex attributes
    // Position attribute
    glEnableVertexAttribArray(0);
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(float), (void*)0);
    
    // Unbind
    glBindVertexArray(0);
}

void PrimeObject::updateColor() {
    // Calculate color based on prime energy and properties
    float energy = m_data.totalEnergy;
    float lambdaRatio = m_data.lambdaEnergy / (m_data.lambdaEnergy + m_data.base13Energy);
    
    // Create color based on lambda/base13 energy ratio
    m_color.r = 0.0f + lambdaRatio * 1.0f;        // Red: lambda energy
    m_color.g = 0.5f + energy * 0.5f;             // Green: total energy
    m_color.b = 1.0f - lambdaRatio * 1.0f;        // Blue: base13 energy
    m_color.a = 0.8f + energy * 0.2f;             // Alpha: based on energy
    
    // Add some pulsing based on prime
    float pulse = sin(m_prime * 0.1f) * 0.1f;
    m_color.r = std::clamp(m_color.r + pulse, 0.0f, 1.0f);
    m_color.g = std::clamp(m_color.g + pulse, 0.0f, 1.0f);
    m_color.b = std::clamp(m_color.b + pulse, 0.0f, 1.0f);
}

} // namespace Enuanza