#include "PrimeComposition3D.h"
#include "Shader.h"
#include <iostream>
#include <cmath>
#include <algorithm>
#include <chrono>
#include <thread>

namespace Enuanza {

// PrimeComposition3D Implementation
PrimeComposition3D::PrimeComposition3D()
    : m_window(nullptr)
    , m_audioSystem(std::make_unique<AudioSystem>())
    , m_particleSystem(std::make_unique<ParticleSystem>())
    , m_VAO(0), m_VBO(0), m_EBO(0)
    , m_cameraPos(glm::vec3(0.0f, 0.0f, 10.0f))
    , m_cameraFront(glm::vec3(0.0f, 0.0f, -1.0f))
    , m_cameraUp(glm::vec3(0.0f, 1.0f, 0.0f))
    , m_yaw(-90.0f), m_pitch(0.0f), m_fov(45.0f)
    , m_running(false), m_vrMode(false), m_currentMode(VisualizationMode::SPLASH)
    , m_time(0.0f), m_maxPrime(1000)
{
}

PrimeComposition3D::~PrimeComposition3D() {
    cleanup();
}

bool PrimeComposition3D::initialize() {
    std::cout << "Initializing Enuanza - Mathematical Immersion System..." << std::endl;
    
    // Initialize core systems
    if (!initializeGLFW()) {
        std::cerr << "Failed to initialize GLFW" << std::endl;
        return false;
    }
    
    if (!initializeOpenGL()) {
        std::cerr << "Failed to initialize OpenGL" << std::endl;
        return false;
    }
    
    if (!initializeAudio()) {
        std::cerr << "Failed to initialize audio system" << std::endl;
        // Continue without audio
    }
    
    if (!initializeShaders()) {
        std::cerr << "Failed to initialize shaders" << std::endl;
        return false;
    }
    
    // Initialize mathematical components
    generatePrimes();
    setupLighting();
    createParticleField();
    setupEventListeners();
    
    m_running = true;
    std::cout << "Enuanza initialized successfully!" << std::endl;
    return true;
}

bool PrimeComposition3D::initializeGLFW() {
    if (!glfwInit()) {
        std::cerr << "GLFW initialization failed" << std::endl;
        return false;
    }
    
    // Configure GLFW
    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 4);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 1);
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);
    glfwWindowHint(GLFW_SAMPLES, 4); // MSAA
    
    // Create window
    m_window = glfwCreateWindow(1920, 1080, "Enuanza - Mathematical Immersion", nullptr, nullptr);
    if (!m_window) {
        std::cerr << "Failed to create GLFW window" << std::endl;
        glfwTerminate();
        return false;
    }
    
    glfwMakeContextCurrent(m_window);
    
    // Set callbacks
    glfwSetWindowUserPointer(m_window, this);
    glfwSetFramebufferSizeCallback(m_window, framebufferSizeCallback);
    glfwSetCursorPosCallback(m_window, mouseCallback);
    glfwSetScrollCallback(m_window, scrollCallback);
    glfwSetKeyCallback(m_window, keyCallback);
    
    // Capture mouse
    glfwSetInputMode(m_window, GLFW_CURSOR, GLFW_CURSOR_DISABLED);
    
    return true;
}

bool PrimeComposition3D::initializeOpenGL() {
    // Initialize GLEW
    glewExperimental = GL_TRUE;
    if (glewInit() != GLEW_OK) {
        std::cerr << "Failed to initialize GLEW" << std::endl;
        return false;
    }
    
    // Configure OpenGL
    glEnable(GL_DEPTH_TEST);
    glEnable(GL_MULTISAMPLE);
    glEnable(GL_BLEND);
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
    
    // Set viewport
    int width, height;
    glfwGetFramebufferSize(m_window, &width, &height);
    glViewport(0, 0, width, height);
    
    // Set clear color
    glClearColor(0.04f, 0.0f, 0.13f, 1.0f); // Dark purple gradient
    
    return true;
}

bool PrimeComposition3D::initializeAudio() {
    return m_audioSystem->initialize();
}

bool PrimeComposition3D::initializeShaders() {
    // Load main shader
    m_shader = std::make_shared<Shader>("shaders/vertex.glsl", "shaders/fragment.glsl");
    if (!m_shader->isLoaded()) {
        std::cerr << "Failed to load main shader" << std::endl;
        return false;
    }
    
    // Load particle shader
    m_particleShader = std::make_shared<Shader>("shaders/particle_vertex.glsl", "shaders/particle_fragment.glsl");
    if (!m_particleShader->isLoaded()) {
        std::cerr << "Failed to load particle shader" << std::endl;
        return false;
    }
    
    return true;
}

void PrimeComposition3D::generatePrimes() {
    std::cout << "Generating prime numbers up to " << m_maxPrime << "..." << std::endl;
    
    // Sieve of Eratosthenes
    std::vector<bool> isPrime(m_maxPrime + 1, true);
    isPrime[0] = isPrime[1] = false;
    
    for (int i = 2; i * i <= m_maxPrime; ++i) {
        if (isPrime[i]) {
            for (int j = i * i; j <= m_maxPrime; j += i) {
                isPrime[j] = false;
            }
        }
    }
    
    // Create prime data
    m_primes.clear();
    for (int i = 2; i <= m_maxPrime; ++i) {
        if (isPrime[i]) {
            m_primes.emplace_back(i);
            
            // Create prime object
            glm::vec3 position = calculatePrimePosition(i);
            auto primeObj = std::make_unique<PrimeObject>(i, position);
            primeObj->initialize();
            m_primeObjects[i] = std::move(primeObj);
        }
    }
    
    std::cout << "Generated " << m_primes.size() << " prime numbers" << std::endl;
}

void PrimeComposition3D::setupLighting() {
    // Setup will be handled in shaders
}

void PrimeComposition3D::createParticleField() {
    m_particleSystem->initialize();
}

void PrimeComposition3D::setupEventListeners() {
    // Event listeners are set up through GLFW callbacks
}

void PrimeComposition3D::run() {
    std::cout << "Starting Enuanza main loop..." << std::endl;
    
    auto lastTime = std::chrono::high_resolution_clock::now();
    
    while (m_running && !glfwWindowShouldClose(m_window)) {
        auto currentTime = std::chrono::high_resolution_clock::now();
        float deltaTime = std::chrono::duration<float>(currentTime - lastTime).count();
        lastTime = currentTime;
        
        handleInput();
        update(deltaTime);
        render();
        
        glfwSwapBuffers(m_window);
        glfwPollEvents();
    }
    
    std::cout << "Enuanza main loop ended" << std::endl;
}

void PrimeComposition3D::render() {
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    
    // Create view and projection matrices
    glm::mat4 view = glm::lookAt(m_cameraPos, m_cameraPos + m_cameraFront, m_cameraUp);
    glm::mat4 projection = glm::perspective(glm::radians(m_fov), 
                                          1920.0f / 1080.0f, 0.1f, 1000.0f);
    
    // Render based on current mode
    switch (m_currentMode) {
        case VisualizationMode::SPLASH:
            renderSplashSequence();
            break;
        case VisualizationMode::COMPOSITION_EXPLORER:
            renderCompositionExplorer();
            break;
        case VisualizationMode::SINUSOIDAL_WAVES:
            renderSinusoidalWaves();
            break;
        case VisualizationMode::NETWORK_VIEW:
            renderNetworkView();
            break;
        case VisualizationMode::VR_MODE:
            // VR rendering would be handled here
            renderNetworkView(); // Fallback to network view
            break;
    }
    
    // Render particle system
    m_particleSystem->render(view, projection);
    
    // Render UI
    renderUI();
}

void PrimeComposition3D::renderSplashSequence() {
    glm::mat4 view = glm::lookAt(m_cameraPos, m_cameraPos + m_cameraFront, m_cameraUp);
    glm::mat4 projection = glm::perspective(glm::radians(m_fov), 
                                          1920.0f / 1080.0f, 0.1f, 1000.0f);
    
    m_shader->use();
    
    // Set uniforms
    m_shader->setMat4("view", view);
    m_shader->setMat4("projection", projection);
    m_shader->setFloat("time", m_time);
    m_shader->setVec3("lightPos", glm::vec3(5.0f, 5.0f, 5.0f));
    m_shader->setVec3("lightColor", glm::vec3(1.0f, 1.0f, 1.0f));
    m_shader->setVec3("viewPos", m_cameraPos);
    
    // Render prime objects in splash pattern
    for (auto& [prime, primeObj] : m_primeObjects) {
        glm::mat4 model = glm::mat4(1.0f);
        
        // Splash animation
        float splashRadius = 5.0f + sin(m_time * 2.0f + prime * 0.1f) * 2.0f;
        float angle = (prime / static_cast<float>(m_maxPrime)) * 2.0f * M_PI;
        float height = sin(m_time * 3.0f + prime * 0.2f) * 3.0f;
        
        model = glm::translate(model, glm::vec3(
            cos(angle) * splashRadius,
            height,
            sin(angle) * splashRadius
        ));
        
        model = glm::rotate(model, m_time + prime * 0.1f, glm::vec3(0.0f, 1.0f, 0.0f));
        model = glm::scale(model, glm::vec3(0.1f));
        
        m_shader->setMat4("model", model);
        primeObj->render(view, projection);
    }
}

void PrimeComposition3D::renderCompositionExplorer() {
    glm::mat4 view = glm::lookAt(m_cameraPos, m_cameraPos + m_cameraFront, m_cameraUp);
    glm::mat4 projection = glm::perspective(glm::radians(m_fov), 
                                          1920.0f / 1080.0f, 0.1f, 1000.0f);
    
    m_shader->use();
    m_shader->setMat4("view", view);
    m_shader->setMat4("projection", projection);
    m_shader->setFloat("time", m_time);
    m_shader->setVec3("lightPos", glm::vec3(5.0f, 5.0f, 5.0f));
    m_shader->setVec3("lightColor", glm::vec3(1.0f, 1.0f, 1.0f));
    m_shader->setVec3("viewPos", m_cameraPos);
    
    // Render primes in composition pattern
    for (auto& [prime, primeObj] : m_primeObjects) {
        glm::mat4 model = glm::mat4(1.0f);
        model = glm::translate(model, primeObj->getPosition());
        model = glm::rotate(model, m_time * 0.5f + prime * 0.01f, glm::vec3(0.0f, 1.0f, 0.0f));
        model = glm::scale(model, glm::vec3(0.05f + primeObj->getPrime() * 0.0001f));
        
        m_shader->setMat4("model", model);
        primeObj->render(view, projection);
    }
}

void PrimeComposition3D::renderSinusoidalWaves() {
    glm::mat4 view = glm::lookAt(m_cameraPos, m_cameraPos + m_cameraFront, m_cameraUp);
    glm::mat4 projection = glm::perspective(glm::radians(m_fov), 
                                          1920.0f / 1080.0f, 0.1f, 1000.0f);
    
    m_shader->use();
    m_shader->setMat4("view", view);
    m_shader->setMat4("projection", projection);
    m_shader->setFloat("time", m_time);
    m_shader->setVec3("lightPos", glm::vec3(5.0f, 5.0f, 5.0f));
    m_shader->setVec3("lightColor", glm::vec3(1.0f, 1.0f, 1.0f));
    m_shader->setVec3("viewPos", m_cameraPos);
    
    // Render primes in wave pattern
    for (size_t i = 0; i < m_primes.size(); ++i) {
        const auto& primeData = m_primes[i];
        glm::mat4 model = glm::mat4(1.0f);
        
        float x = (i / static_cast<float>(m_primes.size())) * 20.0f - 10.0f;
        float y = sin(x * 2.0f + m_time * 2.0f) * 3.0f;
        float z = cos(x * 1.5f + m_time * 1.5f) * 2.0f;
        
        model = glm::translate(model, glm::vec3(x, y, z));
        model = glm::rotate(model, m_time + primeData.prime * 0.01f, glm::vec3(1.0f, 0.0f, 0.0f));
        model = glm::scale(model, glm::vec3(0.08f));
        
        m_shader->setMat4("model", model);
        
        if (m_primeObjects.find(primeData.prime) != m_primeObjects.end()) {
            m_primeObjects[primeData.prime]->render(view, projection);
        }
    }
}

void PrimeComposition3D::renderNetworkView() {
    glm::mat4 view = glm::lookAt(m_cameraPos, m_cameraPos + m_cameraFront, m_cameraUp);
    glm::mat4 projection = glm::perspective(glm::radians(m_fov), 
                                          1920.0f / 1080.0f, 0.1f, 1000.0f);
    
    m_shader->use();
    m_shader->setMat4("view", view);
    m_shader->setMat4("projection", projection);
    m_shader->setFloat("time", m_time);
    m_shader->setVec3("lightPos", glm::vec3(5.0f, 5.0f, 5.0f));
    m_shader->setVec3("lightColor", glm::vec3(1.0f, 1.0f, 1.0f));
    m_shader->setVec3("viewPos", m_cameraPos);
    
    // Render network of primes
    for (auto& [prime, primeObj] : m_primeObjects) {
        glm::mat4 model = glm::mat4(1.0f);
        model = glm::translate(model, primeObj->getPosition());
        model = glm::rotate(model, m_time * 0.3f, glm::vec3(0.0f, 1.0f, 0.0f));
        
        float scale = 0.03f + (prime / static_cast<float>(m_maxPrime)) * 0.05f;
        model = glm::scale(model, glm::vec3(scale));
        
        m_shader->setMat4("model", model);
        primeObj->render(view, projection);
    }
}

void PrimeComposition3D::renderUI() {
    // UI rendering would be implemented here using a 2D rendering library
    // For now, we'll skip UI rendering in the C++ version
}

void PrimeComposition3D::update(float deltaTime) {
    m_time += deltaTime;
    
    // Update particle system
    m_particleSystem->update(deltaTime);
    
    // Update based on current mode
    switch (m_currentMode) {
        case VisualizationMode::SPLASH:
            updateSplashSequence(deltaTime);
            break;
        case VisualizationMode::COMPOSITION_EXPLORER:
            updateCompositionExplorer(deltaTime);
            break;
        case VisualizationMode::SINUSOIDAL_WAVES:
            updateSinusoidalWaves(deltaTime);
            break;
        case VisualizationMode::NETWORK_VIEW:
            updateNetworkView(deltaTime);
            break;
        case VisualizationMode::VR_MODE:
            updateNetworkView(deltaTime);
            break;
    }
    
    // Update prime objects
    for (auto& [prime, primeObj] : m_primeObjects) {
        primeObj->update(deltaTime);
    }
}

void PrimeComposition3D::updateSplashSequence(float deltaTime) {
    // Emit particles based on prime energy
    for (const auto& primeData : m_primes) {
        if (rand() / static_cast<float>(RAND_MAX) < primeData.totalEnergy * 0.01f) {
            glm::vec3 position = calculatePrimePosition(primeData.prime);
            m_particleSystem->emitParticles(position, 1);
        }
    }
}

void PrimeComposition3D::updateCompositionExplorer(float deltaTime) {
    // Update composition explorer logic
}

void PrimeComposition3D::updateSinusoidalWaves(float deltaTime) {
    // Update wave logic
}

void PrimeComposition3D::updateNetworkView(float deltaTime) {
    // Update network connections
}

void PrimeComposition3D::handleInput() {
    // Camera movement
    float cameraSpeed = 2.5f * 0.016f; // Assuming 60 FPS
    
    if (glfwGetKey(m_window, GLFW_KEY_W) == GLFW_PRESS)
        m_cameraPos += cameraSpeed * m_cameraFront;
    if (glfwGetKey(m_window, GLFW_KEY_S) == GLFW_PRESS)
        m_cameraPos -= cameraSpeed * m_cameraFront;
    if (glfwGetKey(m_window, GLFW_KEY_A) == GLFW_PRESS)
        m_cameraPos -= glm::normalize(glm::cross(m_cameraFront, m_cameraUp)) * cameraSpeed;
    if (glfwGetKey(m_window, GLFW_KEY_D) == GLFW_PRESS)
        m_cameraPos += glm::normalize(glm::cross(m_cameraFront, m_cameraUp)) * cameraSpeed;
}

void PrimeComposition3D::startSplashSequence() {
    m_currentMode = VisualizationMode::SPLASH;
    std::cout << "Started Splash Sequence visualization mode" << std::endl;
}

void PrimeComposition3D::startCompositionExplorer() {
    m_currentMode = VisualizationMode::COMPOSITION_EXPLORER;
    std::cout << "Started Composition Explorer visualization mode" << std::endl;
}

void PrimeComposition3D::startSinusoidalWaves() {
    m_currentMode = VisualizationMode::SINUSOIDAL_WAVES;
    std::cout << "Started Sinusoidal Waves visualization mode" << std::endl;
}

void PrimeComposition3D::startNetworkView() {
    m_currentMode = VisualizationMode::NETWORK_VIEW;
    std::cout << "Started Network View visualization mode" << std::endl;
}

void PrimeComposition3D::toggleVRMode() {
    m_vrMode = !m_vrMode;
    m_currentMode = m_vrMode ? VisualizationMode::VR_MODE : VisualizationMode::NETWORK_VIEW;
    std::cout << "VR mode " << (m_vrMode ? "enabled" : "disabled") << std::endl;
}

void PrimeComposition3D::toggleAudio() {
    bool currentMuted = m_audioSystem->isMuted();
    m_audioSystem->setMuted(!currentMuted);
    std::cout << "Audio " << (currentMuted ? "unmuted" : "muted") << std::endl;
}

void PrimeComposition3D::setVolume(float volume) {
    m_audioSystem->setVolume(std::clamp(volume, 0.0f, 1.0f));
}

void PrimeComposition3D::setMuted(bool muted) {
    m_audioSystem->setMuted(muted);
}

void PrimeComposition3D::analyzeSpecificPrime(int prime) {
    std::cout << "Analyzing prime: " << prime << std::endl;
    
    if (m_primeObjects.find(prime) != m_primeObjects.end()) {
        // Play prime frequency
        m_audioSystem->playPrimeFrequency(prime);
        
        // Focus camera on prime
        glm::vec3 primePos = m_primeObjects[prime]->getPosition();
        m_cameraPos = primePos + glm::vec3(0.0f, 0.0f, 5.0f);
        m_cameraFront = glm::normalize(primePos - m_cameraPos);
    }
}

void PrimeComposition3D::setPrimeRange(int maxPrime) {
    m_maxPrime = maxPrime;
    generatePrimes();
}

glm::vec3 PrimeComposition3D::calculatePrimePosition(int prime, const glm::vec3& center) {
    // Calculate position based on prime properties
    float lambdaEnergy = MathConstants::LAMBDA * (1.0f + sin(prime * MathConstants::LAMBDA));
    float base13Energy = MathConstants::BASE13_REFINED * (1.0f + cos((prime % 13) * 2.0f * M_PI / 13.0f));
    
    // Spiral positioning
    float angle = prime * 0.5f;
    float radius = lambdaEnergy * 3.0f + base13Energy * 2.0f;
    float height = (prime % 7) * 0.5f - 1.5f;
    
    return center + glm::vec3(
        cos(angle) * radius,
        height,
        sin(angle) * radius
    );
}

glm::vec4 PrimeComposition3D::calculatePrimeColor(int prime, float energy) {
    // Color based on prime properties
    float hue = fmod(prime * 0.1f, 1.0f);
    float saturation = 0.7f + energy * 0.3f;
    float value = 0.8f + energy * 0.2f;
    
    // HSV to RGB conversion (simplified)
    float r, g, b;
    float h = hue * 6.0f;
    float c = value * saturation;
    float x = c * (1.0f - fabs(fmod(h, 2.0f) - 1.0f));
    float m = value - c;
    
    if (h < 1.0f) { r = c; g = x; b = 0; }
    else if (h < 2.0f) { r = x; g = c; b = 0; }
    else if (h < 3.0f) { r = 0; g = c; b = x; }
    else if (h < 4.0f) { r = 0; g = x; b = c; }
    else if (h < 5.0f) { r = x; g = 0; b = c; }
    else { r = c; g = 0; b = x; }
    
    return glm::vec4(r + m, g + m, b + m, 1.0f);
}

std::vector<int> PrimeComposition3D::findPrimeConnections(int prime) {
    std::vector<int> connections;
    
    // Find connections based on mathematical properties
    for (int genPrime : MathConstants::GENERATOR_PRIMES) {
        if (prime % genPrime == 0 && prime != genPrime) {
            connections.push_back(genPrime);
        }
    }
    
    // Add lambda-based connections
    int lambdaConnection = static_cast<int>(prime * MathConstants::LAMBDA);
    if (std::find(m_primes.begin(), m_primes.end(), lambdaConnection) != m_primes.end()) {
        connections.push_back(lambdaConnection);
    }
    
    return connections;
}

void PrimeComposition3D::cleanup() {
    m_running = false;
    
    // Cleanup prime objects
    m_primeObjects.clear();
    
    // Cleanup particle system
    if (m_particleSystem) {
        m_particleSystem->cleanup();
    }
    
    // Cleanup audio system
    if (m_audioSystem) {
        m_audioSystem->cleanup();
    }
    
    // Cleanup OpenGL resources
    if (m_VAO) glDeleteVertexArrays(1, &m_VAO);
    if (m_VBO) glDeleteBuffers(1, &m_VBO);
    if (m_EBO) glDeleteBuffers(1, &m_EBO);
    
    // Cleanup GLFW
    if (m_window) {
        glfwDestroyWindow(m_window);
    }
    glfwTerminate();
    
    std::cout << "Enuanza cleanup completed" << std::endl;
}

// Static callback implementations
void PrimeComposition3D::framebufferSizeCallback(GLFWwindow* window, int width, int height) {
    auto* app = static_cast<PrimeComposition3D*>(glfwGetWindowUserPointer(window));
    if (app) {
        app->processFramebufferSize(width, height);
    }
}

void PrimeComposition3D::mouseCallback(GLFWwindow* window, double xpos, double ypos) {
    auto* app = static_cast<PrimeComposition3D*>(glfwGetWindowUserPointer(window));
    if (app) {
        app->processMouseMovement(xpos, ypos);
    }
}

void PrimeComposition3D::scrollCallback(GLFWwindow* window, double xoffset, double yoffset) {
    auto* app = static_cast<PrimeComposition3D*>(glfwGetWindowUserPointer(window));
    if (app) {
        app->processScroll(xoffset, yoffset);
    }
}

void PrimeComposition3D::keyCallback(GLFWwindow* window, int key, int scancode, int action, int mods) {
    auto* app = static_cast<PrimeComposition3D*>(glfwGetWindowUserPointer(window));
    if (app) {
        app->processKeyboard(key, scancode, action, mods);
    }
}

void PrimeComposition3D::processFramebufferSize(int width, int height) {
    glViewport(0, 0, width, height);
}

void PrimeComposition3D::processMouseMovement(double xpos, double ypos) {
    static double lastX = 1920.0 / 2.0;
    static double lastY = 1080.0 / 2.0;
    static bool firstMouse = true;
    
    if (firstMouse) {
        lastX = xpos;
        lastY = ypos;
        firstMouse = false;
    }
    
    double xoffset = xpos - lastX;
    double yoffset = lastY - ypos; // Reversed since y-coordinates go from bottom to top
    
    lastX = xpos;
    lastY = ypos;
    
    float sensitivity = 0.1f;
    xoffset *= sensitivity;
    yoffset *= sensitivity;
    
    m_yaw += xoffset;
    m_pitch += yoffset;
    
    // Constrain pitch
    if (m_pitch > 89.0f) m_pitch = 89.0f;
    if (m_pitch < -89.0f) m_pitch = -89.0f;
    
    // Update camera front vector
    glm::vec3 front;
    front.x = cos(glm::radians(m_yaw)) * cos(glm::radians(m_pitch));
    front.y = sin(glm::radians(m_pitch));
    front.z = sin(glm::radians(m_yaw)) * cos(glm::radians(m_pitch));
    m_cameraFront = glm::normalize(front);
}

void PrimeComposition3D::processScroll(double xoffset, double yoffset) {
    m_fov -= yoffset;
    if (m_fov < 1.0f) m_fov = 1.0f;
    if (m_fov > 45.0f) m_fov = 45.0f;
}

void PrimeComposition3D::processKeyboard(int key, int scancode, int action, int mods) {
    if (action == GLFW_PRESS) {
        switch (key) {
            case GLFW_KEY_ESCAPE:
                m_running = false;
                break;
            case GLFW_KEY_1:
                startSplashSequence();
                break;
            case GLFW_KEY_2:
                startCompositionExplorer();
                break;
            case GLFW_KEY_3:
                startSinusoidalWaves();
                break;
            case GLFW_KEY_4:
                startNetworkView();
                break;
            case GLFW_KEY_V:
                toggleVRMode();
                break;
            case GLFW_KEY_M:
                toggleAudio();
                break;
            case GLFW_KEY_SPACE:
                // Handle space bar for interactions
                break;
        }
    }
}

} // namespace Enuanza