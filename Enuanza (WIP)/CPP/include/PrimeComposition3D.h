#ifndef PRIME_COMPOSITION_3D_H
#define PRIME_COMPOSITION_3D_H

#include <vector>
#include <map>
#include <memory>
#include <string>
#include <functional>

// OpenGL and GLFW includes
#include <GL/glew.h>
#include <GLFW/glfw3.h>

// Audio system includes
#include <AL/al.h>
#include <AL/alc.h>

// Math includes
#include <glm/glm.hpp>
#include <glm/gtc/matrix_transform.hpp>
#include <glm/gtc/type_ptr.hpp>

namespace Enuanza {

// Mathematical Constants
struct MathConstants {
    static constexpr double LAMBDA = 0.6;                    // Primary constant
    static constexpr double BASE13_REFINED = 8.0/13.0;       // Base-13 manifestation
    static constexpr double C_STAR = 17.0/19.0;              // Prime composition constant
    static constexpr double GOLDEN_RATIO_INV = 1.0/1.618033988749895; // Golden ratio inverse
    static constexpr std::vector<int> GENERATOR_PRIMES = {7, 13, 17, 19};
};

// Prime Data Structure
struct PrimeData {
    int prime;
    double lambdaEnergy;
    double base13Energy;
    double totalEnergy;
    glm::vec3 position;
    glm::vec4 color;
    std::vector<int> connections;
    
    PrimeData(int p) : prime(p) {
        lambdaEnergy = calculateLambdaEnergy(p);
        base13Energy = calculateBase13Energy(p);
        totalEnergy = lambdaEnergy + base13Energy;
    }
    
private:
    double calculateLambdaEnergy(int p) {
        return MathConstants::LAMBDA * (1.0 + sin(p * MathConstants::LAMBDA));
    }
    
    double calculateBase13Energy(int p) {
        double base13Value = static_cast<double>(p % 13) / 13.0;
        return MathConstants::BASE13_REFINED * (1.0 + cos(base13Value * 2.0 * M_PI));
    }
};

// Audio System
class AudioSystem {
public:
    AudioSystem();
    ~AudioSystem();
    
    bool initialize();
    void cleanup();
    void setVolume(float volume);
    void setMuted(bool muted);
    float getVolume() const { return m_volume; }
    bool isMuted() const { return m_muted; }
    
    void playPrimeFrequency(int prime);
    void stopPrimeFrequency(int prime);
    void playBackgroundMusic();
    void stopBackgroundMusic();
    
private:
    ALCdevice* m_device;
    ALCcontext* m_context;
    ALuint m_source;
    std::map<int, ALuint> m_primeBuffers;
    float m_volume;
    bool m_muted;
    
    bool initializeOpenAL();
    void generatePrimeFrequencies();
    ALuint generateToneBuffer(float frequency, float duration);
};

// Particle System
class ParticleSystem {
public:
    ParticleSystem(size_t maxParticles = 5000);
    ~ParticleSystem();
    
    void initialize();
    void cleanup();
    void update(float deltaTime);
    void render(const glm::mat4& viewMatrix, const glm::mat4& projectionMatrix);
    
    void emitParticles(const glm::vec3& position, int count);
    void setEmissionRate(float rate) { m_emissionRate = rate; }
    size_t getParticleCount() const { return m_particles.size(); }
    
private:
    struct Particle {
        glm::vec3 position;
        glm::vec3 velocity;
        glm::vec4 color;
        float life;
        float maxLife;
        float size;
    };
    
    std::vector<Particle> m_particles;
    size_t m_maxParticles;
    float m_emissionRate;
    
    GLuint m_VAO, m_VBO;
    std::shared_ptr<class Shader> m_shader;
    
    void updateParticle(Particle& particle, float deltaTime);
    void renderParticles(const glm::mat4& viewMatrix, const glm::mat4& projectionMatrix);
};

// Visualization Modes
enum class VisualizationMode {
    SPLASH,
    COMPOSITION_EXPLORER,
    SINUSOIDAL_WAVES,
    NETWORK_VIEW,
    VR_MODE
};

// Main Application Class
class PrimeComposition3D {
public:
    PrimeComposition3D();
    ~PrimeComposition3D();
    
    bool initialize();
    void run();
    void cleanup();
    
    // Visualization Controls
    void startSplashSequence();
    void startCompositionExplorer();
    void startSinusoidalWaves();
    void startNetworkView();
    void toggleVRMode();
    
    // Audio Controls
    void toggleAudio();
    void setVolume(float volume);
    void setMuted(bool muted);
    
    // Prime Analysis
    void analyzeSpecificPrime(int prime);
    void setPrimeRange(int maxPrime);
    
    // Getters
    bool isRunning() const { return m_running; }
    VisualizationMode getCurrentMode() const { return m_currentMode; }
    
private:
    // Core Systems
    GLFWwindow* m_window;
    std::unique_ptr<AudioSystem> m_audioSystem;
    std::unique_ptr<ParticleSystem> m_particleSystem;
    
    // OpenGL Resources
    GLuint m_VAO, m_VBO, m_EBO;
    std::shared_ptr<class Shader> m_shader;
    std::shared_ptr<class Shader> m_particleShader;
    
    // Camera and Controls
    glm::vec3 m_cameraPos;
    glm::vec3 m_cameraFront;
    glm::vec3 m_cameraUp;
    float m_yaw, m_pitch;
    float m_fov;
    
    // State
    bool m_running;
    bool m_vrMode;
    VisualizationMode m_currentMode;
    float m_time;
    
    // Prime Data
    std::vector<PrimeData> m_primes;
    std::map<int, std::unique_ptr<class PrimeObject>> m_primeObjects;
    int m_maxPrime;
    
    // Initialization Methods
    bool initializeGLFW();
    bool initializeOpenGL();
    bool initializeAudio();
    bool initializeShaders();
    void generatePrimes();
    void setupLighting();
    void createParticleField();
    void setupEventListeners();
    
    // Rendering Methods
    void render();
    void renderSplashSequence();
    void renderCompositionExplorer();
    void renderSinusoidalWaves();
    void renderNetworkView();
    void renderUI();
    
    // Update Methods
    void update(float deltaTime);
    void updateSplashSequence(float deltaTime);
    void updateCompositionExplorer(float deltaTime);
    void updateSinusoidalWaves(float deltaTime);
    void updateNetworkView(float deltaTime);
    
    // Utility Methods
    void handleInput();
    void calculateFrameTiming();
    glm::vec3 calculatePrimePosition(int prime, const glm::vec3& center = glm::vec3(0.0f));
    glm::vec4 calculatePrimeColor(int prime, float energy);
    std::vector<int> findPrimeConnections(int prime);
    
    // Static Callbacks
    static void framebufferSizeCallback(GLFWwindow* window, int width, int height);
    static void mouseCallback(GLFWwindow* window, double xpos, double ypos);
    static void scrollCallback(GLFWwindow* window, double xoffset, double yoffset);
    static void keyCallback(GLFWwindow* window, int key, int scancode, int action, int mods);
    
    // Instance callbacks
    void processFramebufferSize(int width, int height);
    void processMouseMovement(double xpos, double ypos);
    void processScroll(double xoffset, double yoffset);
    void processKeyboard(int key, int scancode, int action, int mods);
};

// Prime Object Class
class PrimeObject {
public:
    PrimeObject(int prime, const glm::vec3& position);
    ~PrimeObject();
    
    void initialize();
    void cleanup();
    void update(float deltaTime);
    void render(const glm::mat4& viewMatrix, const glm::mat4& projectionMatrix);
    
    int getPrime() const { return m_prime; }
    const glm::vec3& getPosition() const { return m_position; }
    void setPosition(const glm::vec3& pos) { m_position = pos; }
    
private:
    int m_prime;
    PrimeData m_data;
    glm::vec3 m_position;
    glm::vec3 m_rotation;
    glm::vec3 m_scale;
    glm::vec4 m_color;
    
    GLuint m_VAO, m_VBO, m_EBO;
    std::shared_ptr<Shader> m_shader;
    
    void createGeometry();
    void updateColor();
};

} // namespace Enuanza

#endif // PRIME_COMPOSITION_3D_H