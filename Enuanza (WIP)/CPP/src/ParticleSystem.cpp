#include "PrimeComposition3D.h"
#include <iostream>
#include <random>
#include <algorithm>

namespace Enuanza {

ParticleSystem::ParticleSystem(size_t maxParticles) 
    : m_maxParticles(maxParticles), m_emissionRate(10.0f)
    , m_VAO(0), m_VBO(0) {
    m_particles.reserve(maxParticles);
}

ParticleSystem::~ParticleSystem() {
    cleanup();
}

void ParticleSystem::initialize() {
    // Generate VAO and VBO
    glGenVertexArrays(1, &m_VAO);
    glGenBuffers(1, &m_VBO);
    
    glBindVertexArray(m_VAO);
    
    // Create VBO with dynamic data
    glBindBuffer(GL_ARRAY_BUFFER, m_VBO);
    glBufferData(GL_ARRAY_BUFFER, m_maxParticles * sizeof(Particle), nullptr, GL_DYNAMIC_DRAW);
    
    // Set vertex attributes
    // Position (vec3)
    glEnableVertexAttribArray(0);
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, sizeof(Particle), 
                         (void*)offsetof(Particle, position));
    
    // Color (vec4)
    glEnableVertexAttribArray(1);
    glVertexAttribPointer(1, 4, GL_FLOAT, GL_FALSE, sizeof(Particle), 
                         (void*)offsetof(Particle, color));
    
    // Life (float) - for alpha blending
    glEnableVertexAttribArray(2);
    glVertexAttribPointer(2, 1, GL_FLOAT, GL_FALSE, sizeof(Particle), 
                         (void*)offsetof(Particle, life));
    
    // Size (float)
    glEnableVertexAttribArray(3);
    glVertexAttribPointer(3, 1, GL_FLOAT, GL_FALSE, sizeof(Particle), 
                         (void*)offsetof(Particle, size));
    
    glBindVertexArray(0);
    
    // Load particle shader (assuming it exists)
    // m_shader = std::make_shared<Shader>("shaders/particle_vertex.glsl", "shaders/particle_fragment.glsl");
    
    std::cout << "Particle system initialized with " << m_maxParticles << " max particles" << std::endl;
}

void ParticleSystem::cleanup() {
    if (m_VAO) glDeleteVertexArrays(1, &m_VAO);
    if (m_VBO) glDeleteBuffers(1, &m_VBO);
}

void ParticleSystem::update(float deltaTime) {
    // Update existing particles
    for (auto& particle : m_particles) {
        updateParticle(particle, deltaTime);
    }
    
    // Remove dead particles
    m_particles.erase(
        std::remove_if(m_particles.begin(), m_particles.end(),
                      [](const Particle& p) { return p.life <= 0.0f; }),
        m_particles.end()
    );
    
    // Emit new particles based on emission rate
    float particlesToEmit = m_emissionRate * deltaTime;
    int particlesToCreate = static_cast<int>(particlesToEmit);
    
    if (particlesToCreate > 0 && m_particles.size() < m_maxParticles) {
        // Random emission point (will be overridden by specific emission calls)
        glm::vec3 emitPos(0.0f, 0.0f, 0.0f);
        emitParticles(emitPos, particlesToCreate);
    }
}

void ParticleSystem::render(const glm::mat4& viewMatrix, const glm::mat4& projectionMatrix) {
    if (m_particles.empty()) return;
    
    // Update VBO with current particle data
    glBindBuffer(GL_ARRAY_BUFFER, m_VBO);
    glBufferSubData(GL_ARRAY_BUFFER, 0, 
                   m_particles.size() * sizeof(Particle), 
                   m_particles.data());
    
    // Setup rendering state
    glEnable(GL_BLEND);
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
    glDepthMask(GL_FALSE);
    
    // Use particle shader if available
    // if (m_shader && m_shader->isLoaded()) {
    //     m_shader->use();
    //     m_shader->setMat4("view", viewMatrix);
    //     m_shader->setMat4("projection", projectionMatrix);
    // }
    
    glBindVertexArray(m_VAO);
    
    // Render particles as points
    glDrawArrays(GL_POINTS, 0, static_cast<GLsizei>(m_particles.size()));
    
    glBindVertexArray(0);
    
    // Restore rendering state
    glDepthMask(GL_TRUE);
    glDisable(GL_BLEND);
}

void ParticleSystem::emitParticles(const glm::vec3& position, int count) {
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_real_distribution<float> posDist(-1.0f, 1.0f);
    std::uniform_real_distribution<float> velDist(-2.0f, 2.0f);
    std::uniform_real_distribution<float> lifeDist(1.0f, 3.0f);
    std::uniform_real_distribution<float> sizeDist(0.01f, 0.05f);
    
    for (int i = 0; i < count && m_particles.size() < m_maxParticles; ++i) {
        Particle particle;
        
        // Position with some randomness
        particle.position = position + glm::vec3(
            posDist(gen) * 0.1f,
            posDist(gen) * 0.1f,
            posDist(gen) * 0.1f
        );
        
        // Velocity
        particle.velocity = glm::vec3(
            velDist(gen),
            fabs(velDist(gen)) + 1.0f, // Upward bias
            velDist(gen)
        );
        
        // Color (cyan to magenta gradient)
        float t = static_cast<float>(rand()) / RAND_MAX;
        particle.color = glm::vec4(
            0.0f + t * 1.0f,     // R: 0 to 1
            1.0f,                 // G: always 1
            1.0f - t * 1.0f,     // B: 1 to 0
            1.0f                  // A: always 1
        );
        
        // Life
        particle.maxLife = lifeDist(gen);
        particle.life = particle.maxLife;
        
        // Size
        particle.size = sizeDist(gen);
        
        m_particles.push_back(particle);
    }
}

void ParticleSystem::updateParticle(Particle& particle, float deltaTime) {
    // Update position
    particle.position += particle.velocity * deltaTime;
    
    // Apply gravity
    particle.velocity.y -= 9.81f * deltaTime;
    
    // Apply drag
    particle.velocity *= 0.99f;
    
    // Update life
    particle.life -= deltaTime;
    
    // Update alpha based on life
    if (particle.life > 0.0f) {
        particle.color.a = particle.life / particle.maxLife;
    }
    
    // Pulsing size effect
    particle.size *= 1.0f + sin(particle.life * 10.0f) * 0.1f * deltaTime;
}

} // namespace Enuanza