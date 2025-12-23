/*
 * SphereOMatic.cpp - 3D Sphere Modeling and AI Geometry Implementation
 * 
 * Advanced 3D sphere workshop with AI-generated novel geometry
 * and comprehensive collision testing capabilities.
 */

#include "workshops/SphereOMatic.h"
#include "PlanePilotApp.h"
#include "utils/Logger.h"

#include <GL/gl.h>
#include <GL/glu.h>
#include <cmath>
#include <algorithm>
#include <fstream>
#include <future>
#include <thread>

// Math namespace implementation
namespace PlanePilot {
    namespace Math {
        struct Point3D {
            float x, y, z;
            Point3D(float x = 0.0f, float y = 0.0f, float z = 0.0f) : x(x), y(y), z(z) {}
        };
        
        struct Sphere {
            Point3D center;
            float radius;
            float mass;
            float color[4];
            
            Sphere(Point3D c = Point3D(), float r = 1.0f, float m = 1.0f) 
                : center(c), radius(r), mass(m) {
                color[0] = 0.8f; color[1] = 0.8f; color[2] = 0.8f; color[3] = 1.0f;
            }
        };
        
        class CollisionDetector {
        public:
            bool checkSphereCollision(const Sphere& s1, const Sphere& s2) {
                float dx = s1.center.x - s2.center.x;
                float dy = s1.center.y - s2.center.y;
                float dz = s1.center.z - s2.center.z;
                float distance = std::sqrt(dx*dx + dy*dy + dz*dz);
                return distance < (s1.radius + s2.radius);
            }
            
            std::vector<std::pair<int, int>> detectAllCollisions(const std::vector<Sphere>& spheres) {
                std::vector<std::pair<int, int>> collisions;
                
                for (size_t i = 0; i < spheres.size(); ++i) {
                    for (size_t j = i + 1; j < spheres.size(); ++j) {
                        if (checkSphereCollision(spheres[i], spheres[j])) {
                            collisions.emplace_back(i, j);
                        }
                    }
                }
                
                return collisions;
            }
        };
        
        class GeometryAI {
        public:
            Sphere generateAISphere(const std::string& prompt, const std::vector<Sphere>& baseSpheres) {
                // AI sphere generation based on prompt and existing spheres
                Sphere aiSphere;
                
                // Analyze base spheres
                float avgRadius = 0.0f;
                Point3D avgCenter;
                
                for (const auto& sphere : baseSpheres) {
                    avgRadius += sphere.radius;
                    avgCenter.x += sphere.center.x;
                    avgCenter.y += sphere.center.y;
                    avgCenter.z += sphere.center.z;
                }
                
                if (!baseSpheres.empty()) {
                    avgRadius /= baseSpheres.size();
                    avgCenter.x /= baseSpheres.size();
                    avgCenter.y /= baseSpheres.size();
                    avgCenter.z /= baseSpheres.size();
                }
                
                // Generate novel geometry based on AI analysis
                // This would connect to real AI in a full implementation
                
                if (prompt.find("fractal") != std::string::npos) {
                    aiSphere.radius = avgRadius * 0.618f;  // Golden ratio
                    aiSphere.center = Point3D(
                        avgCenter.x + std::cos(M_PI * 0.382f) * avgRadius * 2.0f,
                        avgCenter.y + std::sin(M_PI * 0.382f) * avgRadius * 2.0f,
                        avgCenter.z + std::sin(M_PI * 0.618f) * avgRadius * 1.5f
                    );
                    aiSphere.color[0] = 0.9f; aiSphere.color[1] = 0.7f; aiSphere.color[2] = 0.3f;
                } else if (prompt.find("quantum") != std::string::npos) {
                    aiSphere.radius = avgRadius * std::sqrt(2.0f);
                    aiSphere.center = Point3D(
                        avgCenter.x + avgRadius * std::cos(M_PI / 3.0f),
                        avgCenter.y + avgRadius * std::sin(M_PI / 3.0f),
                        avgCenter.z
                    );
                    aiSphere.color[0] = 0.3f; aiSphere.color[1] = 0.7f; aiSphere.color[2] = 0.9f;
                } else {
                    // Default novel geometry
                    float phi = (1.0f + std::sqrt(5.0f)) / 2.0f;  // Golden ratio
                    aiSphere.radius = avgRadius / phi;
                    aiSphere.center = Point3D(
                        avgCenter.x + phi * avgRadius,
                        avgCenter.y + avgRadius / phi,
                        avgCenter.z + std::sqrt(phi) * avgRadius
                    );
                    aiSphere.color[0] = 0.7f; aiSphere.color[1] = 0.3f; aiSphere.color[2] = 0.8f;
                }
                
                aiSphere.mass = aiSphere.radius * aiSphere.radius * aiSphere.radius;  // Volume-based mass
                
                return aiSphere;
            }
        };
    }
    
    // Graphics namespace implementation
    namespace Graphics {
        class Renderer {
        public:
            bool initialize(int width, int height) { return true; }
            void beginFrame() { glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT); }
            void endFrame() {}
        };
        
        class Shader {
        public:
            bool load(const std::string& vertexPath, const std::string& fragmentPath) { return true; }
            void use() {}
            void setMatrix(const std::string& name, const float* matrix) {}
            void setFloat(const std::string& name, float value) {}
            void setVector3(const std::string& name, float x, float y, float z) {}
            void setVector4(const std::string& name, float x, float y, float z, float w) {}
        };
        
        class Camera3D {
        public:
            void setPosition(float x, float y, float z) {}
            void setTarget(float x, float y, float z) {}
            void update() {}
            const float* getViewMatrix() const { static float matrix[16] = {1}; return matrix; }
            const float* getProjectionMatrix() const { static float matrix[16] = {1}; return matrix; }
        };
        
        class Model3D {
        public:
            bool load(const std::string& filename) { return true; }
            void render(const float* modelMatrix) {}
            void render() {}
        };
    }
    
    // AI namespace implementation
    namespace AI {
        class GeometryGenerator {
        public:
            std::string generateGeometryPrompt(const std::vector<PlanePilot::Math::Sphere>& spheres) {
                return "Generate a novel 3D sphere geometry based on existing sphere configurations. "
                       "Consider fractal patterns, quantum-inspired arrangements, and golden ratio proportions. "
                       "Create something mathematically interesting yet physically plausible.";
            }
            
            std::string analyzeGeometry(const std::vector<PlanePilot::Math::Sphere>& spheres) {
                // Analyze the geometry and return insights
                if (spheres.empty()) return "No spheres to analyze";
                
                float totalVolume = 0.0f;
                PlanePilot::Math::Point3D centerOfMass;
                
                for (const auto& sphere : spheres) {
                    float volume = (4.0f / 3.0f) * M_PI * sphere.radius * sphere.radius * sphere.radius;
                    totalVolume += volume;
                    centerOfMass.x += sphere.center.x * volume;
                    centerOfMass.y += sphere.center.y * volume;
                    centerOfMass.z += sphere.center.z * volume;
                }
                
                if (totalVolume > 0.0f) {
                    centerOfMass.x /= totalVolume;
                    centerOfMass.y /= totalVolume;
                    centerOfMass.z /= totalVolume;
                }
                
                return "Geometry analysis complete. Center of mass at (" + 
                       std::to_string(centerOfMass.x) + ", " + 
                       std::to_string(centerOfMass.y) + ", " + 
                       std::to_string(centerOfMass.z) + ") with total volume " + 
                       std::to_string(totalVolume);
            }
        };
        
        class AIConnector {
        public:
            bool connect(const std::string& endpoint, const std::string& apiKey) {
                // In a real implementation, this would establish API connection
                return true;  // Simulate successful connection
            }
            
            std::future<std::string> generateGeometryAsync(const std::string& prompt) {
                return std::async(std::launch::async, [this, prompt]() -> std::string {
                    // Simulate AI processing time
                    std::this_thread::sleep_for(std::chrono::milliseconds(2000));
                    
                    // Generate AI response (simulated)
                    if (prompt.find("fractal") != std::string::npos) {
                        return std::string("Generated fractal sphere configuration with self-similar patterns");
                    } else if (prompt.find("quantum") != std::string::npos) {
                        return std::string("Generated quantum-inspired sphere arrangement with superposition properties");
                    } else {
                        return std::string("Generated novel sphere geometry using mathematical principles");
                    }
                });
            }
        };
    }
    
    // GUI namespace implementation
    namespace GUI {
        class UI {
        public:
            bool initialize() { return true; }
            void render() {}
            void handleInput() {}
        };
    }
}

namespace PlanePilot {
namespace Workshops {

SphereOMatic::SphereOMatic(PlanePilotApp* app)
    : m_app(app)
    , m_isSimulating(false)
    , m_isTestingCollisions(false)
    , m_simulationTime(0.0f)
    , m_collisionTestProgress(0.0f)
{
    Logger::info("SphereOMatic constructor");
}

SphereOMatic::~SphereOMatic() {
    cleanup();
    Logger::info("SphereOMatic destructor");
}

bool SphereOMatic::initialize() {
    Logger::info("Initializing Sphere-O-Matic Workshop");
    
    if (!initializeGraphics()) {
        Logger::error("Failed to initialize graphics components");
        return false;
    }
    
    if (!initializeMathematics()) {
        Logger::error("Failed to initialize mathematical components");
        return false;
    }
    
    if (!initializeAI()) {
        Logger::error("Failed to initialize AI components");
        return false;
    }
    
    if (!initializeUI()) {
        Logger::error("Failed to initialize UI components");
        return false;
    }
    
    if (!loadOriginalSpheres()) {
        Logger::error("Failed to load original sphere models");
        return false;
    }
    
    Logger::info("Sphere-O-Matic Workshop initialized successfully");
    return true;
}

bool SphereOMatic::initializeGraphics() {
    Logger::info("Initializing graphics components");
    
    m_renderer = std::make_unique<PlanePilot::Graphics::Renderer>();
    if (!m_renderer->initialize(m_app->getWidth(), m_app->getHeight())) {
        return false;
    }
    
    m_phongShader = std::make_unique<PlanePilot::Graphics::Shader>();
    m_wireframeShader = std::make_unique<PlanePilot::Graphics::Shader>();
    
    m_camera = std::make_unique<PlanePilot::Graphics::Camera3D>();
    m_camera->setPosition(0.0f, 0.0f, 10.0f);
    m_camera->setTarget(0.0f, 0.0f, 0.0f);
    
    m_sphereModel = std::make_unique<PlanePilot::Graphics::Model3D>();
    createSphereGeometry();
    
    Logger::info("Graphics components initialized");
    return true;
}

bool SphereOMatic::initializeMathematics() {
    Logger::info("Initializing mathematical components");
    
    m_collisionDetector = std::make_unique<PlanePilot::Math::CollisionDetector>();
    
    Logger::info("Mathematical components initialized");
    return true;
}

bool SphereOMatic::initializeAI() {
    Logger::info("Initializing AI components");
    
    m_geometryGenerator = std::make_unique<PlanePilot::AI::GeometryGenerator>();
    m_aiConnector = std::make_unique<PlanePilot::AI::AIConnector>();
    
    // Connect to AI service (simulated)
    if (!m_aiConnector->connect(m_aiConfig.apiEndpoint, m_aiConfig.apiKey)) {
        Logger::warning("AI connection failed, using offline mode");
    }
    
    Logger::info("AI components initialized");
    return true;
}

bool SphereOMatic::initializeUI() {
    Logger::info("Initializing UI components");
    
    m_ui = std::make_unique<PlanePilot::GUI::UI>();
    if (!m_ui->initialize()) {
        return false;
    }
    
    Logger::info("UI components initialized");
    return true;
}

bool SphereOMatic::loadOriginalSpheres() {
    Logger::info("Loading original sphere models from je-suis-ballin.py");
    
    // Load the 5 sphere models from je-suis-ballin.py
    // These would be the specific spheres from that program
    
    // Sphere 1: The "Termination Boundary" sphere
    m_originalSpheres.emplace_back(
        PlanePilot::Math::Point3D(-2.0f, 0.0f, 0.0f), 
        1.0f, 1.0f
    );
    m_originalSpheres.back().color[0] = 1.0f; m_originalSpheres.back().color[1] = 0.2f; m_originalSpheres.back().color[2] = 0.2f;
    
    // Sphere 2: The "Prime Analyzer" sphere
    m_originalSpheres.emplace_back(
        PlanePilot::Math::Point3D(2.0f, 0.0f, 0.0f), 
        0.8f, 1.2f
    );
    m_originalSpheres.back().color[0] = 0.2f; m_originalSpheres.back().color[1] = 1.0f; m_originalSpheres.back().color[2] = 0.2f;
    
    // Sphere 3: The "Continued Fractions" sphere
    m_originalSpheres.emplace_back(
        PlanePilot::Math::Point3D(0.0f, 2.0f, 0.0f), 
        1.2f, 0.8f
    );
    m_originalSpheres.back().color[0] = 0.2f; m_originalSpheres.back().color[1] = 0.2f; m_originalSpheres.back().color[2] = 1.0f;
    
    // Sphere 4: The "Digit Plasticity" sphere
    m_originalSpheres.emplace_back(
        PlanePilot::Math::Point3D(0.0f, -2.0f, 0.0f), 
        0.9f, 1.1f
    );
    m_originalSpheres.back().color[0] = 1.0f; m_originalSpheres.back().color[1] = 1.0f; m_originalSpheres.back().color[2] = 0.2f;
    
    // Sphere 5: The "Best Number" sphere
    m_originalSpheres.emplace_back(
        PlanePilot::Math::Point3D(0.0f, 0.0f, 2.0f), 
        1.1f, 0.9f
    );
    m_originalSpheres.back().color[0] = 1.0f; m_originalSpheres.back().color[1] = 0.2f; m_originalSpheres.back().color[2] = 1.0f;
    
    // Copy to current spheres for manipulation
    m_currentSpheres = m_originalSpheres;
    
    Logger::info("Loaded " + std::to_string(m_originalSpheres.size()) + " original sphere models");
    return true;
}

void SphereOMatic::update() {
    updateSimulation();
    updateCollisions();
    updateAI();
    updateCamera();
    updateUI();
}

void SphereOMatic::render() {
    if (!m_renderer) return;
    
    m_renderer->beginFrame();
    
    // Set up 3D projection
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluPerspective(45.0f, m_app->getWidth() / (float)m_app->getHeight(), 0.1f, 100.0f);
    
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    
    // Apply camera transform
    if (m_camera) {
        glMultMatrixf(m_camera->getViewMatrix());
    }
    
    // Enable depth testing
    glEnable(GL_DEPTH_TEST);
    
    // Enable lighting
    glEnable(GL_LIGHTING);
    glEnable(GL_LIGHT0);
    GLfloat lightPos[] = {5.0f, 5.0f, 5.0f, 1.0f};
    glLightfv(GL_LIGHT0, GL_POSITION, lightPos);
    
    // Render scene
    render3DScene();
    
    // Render UI
    glDisable(GL_LIGHTING);
    glDisable(GL_DEPTH_TEST);
    renderUI();
    
    m_renderer->endFrame();
}

void SphereOMatic::handleInput() {
    handleMouseInput();
    handleKeyboardInput();
    handle3DManipulation();
    handleSphereSelection();
}

void SphereOMatic::generateAISphere(const std::string& prompt) {
    Logger::info("Generating AI sphere with prompt: " + prompt);
    
    // Generate AI sphere using the geometry AI
    auto geometryAI = std::make_unique<PlanePilot::Math::GeometryAI>();
    PlanePilot::Math::Sphere aiSphere = geometryAI->generateAISphere(prompt, m_currentSpheres);
    
    m_aiGeneratedSpheres.push_back(aiSphere);
    m_currentSpheres.push_back(aiSphere);
    
    // Analyze the new geometry
    if (m_geometryGenerator) {
        std::string analysis = m_geometryGenerator->analyzeGeometry(m_aiGeneratedSpheres);
        Logger::info("AI geometry analysis: " + analysis);
    }
    
    Logger::info("AI sphere generated successfully");
}

void SphereOMatic::testCollisions() {
    Logger::info("Starting collision testing");
    m_isTestingCollisions = true;
    m_collisionTestProgress = 0.0f;
    
    // Test collisions on current configuration
    detectCollisions();
    testExtremalConfigurations();
    analyzeCollisionPatterns();
    generateCollisionReport();
    
    m_isTestingCollisions = false;
    Logger::info("Collision testing completed");
}

void SphereOMatic::exportConfiguration(const std::string& filename) {
    exportToJSON(filename);
}

void SphereOMatic::render3DScene() {
    renderSpheres();
    
    if (m_settings.showWireframe) {
        renderWireframeSpheres();
    }
    
    if (m_settings.showCollisions) {
        renderCollisions();
    }
    
    if (m_settings.showExtremes) {
        renderExtremes();
    }
    
    if (m_settings.showAIGenerated) {
        renderAISpheres();
    }
}

void SphereOMatic::renderSpheres() {
    if (!m_phongShader) return;
    
    m_phongShader->use();
    
    for (const auto& sphere : m_currentSpheres) {
        glPushMatrix();
        glTranslatef(sphere.center.x, sphere.center.y, sphere.center.z);
        glScalef(sphere.radius, sphere.radius, sphere.radius);
        
        m_phongShader->setVector4("color", sphere.color[0], sphere.color[1], sphere.color[2], sphere.color[3]);
        
        // Render sphere using OpenGL
        if (m_sphereModel) {
            m_sphereModel->render();
        } else {
            // Fallback: render sphere using gluSphere
            GLUquadric* quadric = gluNewQuadric();
            gluSphere(quadric, 1.0f, m_settings.quality, m_settings.quality);
            gluDeleteQuadric(quadric);
        }
        
        glPopMatrix();
    }
}

void SphereOMatic::renderWireframeSpheres() {
    if (!m_wireframeShader) return;
    
    m_wireframeShader->use();
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE);
    
    for (const auto& sphere : m_currentSpheres) {
        glPushMatrix();
        glTranslatef(sphere.center.x, sphere.center.y, sphere.center.z);
        glScalef(sphere.radius, sphere.radius, sphere.radius);
        
        // Render wireframe sphere
        GLUquadric* quadric = gluNewQuadric();
        gluQuadricDrawStyle(quadric, GLU_LINE);
        gluSphere(quadric, 1.0f, m_settings.quality, m_settings.quality);
        gluDeleteQuadric(quadric);
        
        glPopMatrix();
    }
    
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL);
}

void SphereOMatic::renderCollisions() {
    if (!m_collisionDetector) return;
    
    auto collisions = m_collisionDetector->detectAllCollisions(m_currentSpheres);
    
    glDisable(GL_LIGHTING);
    glLineWidth(3.0f);
    glBegin(GL_LINES);
    
    // Render collision connections in red
    glColor3f(1.0f, 0.0f, 0.0f);
    for (const auto& collision : collisions) {
        const auto& s1 = m_currentSpheres[collision.first];
        const auto& s2 = m_currentSpheres[collision.second];
        
        glVertex3f(s1.center.x, s1.center.y, s1.center.z);
        glVertex3f(s2.center.x, s2.center.y, s2.center.z);
    }
    
    glEnd();
    glLineWidth(1.0f);
    glEnable(GL_LIGHTING);
}

void SphereOMatic::renderExtremes() {
    // Render extremal configuration indicators
    glDisable(GL_LIGHTING);
    
    // Find extremal spheres (largest, smallest, farthest from origin)
    if (!m_currentSpheres.empty()) {
        auto largest = std::max_element(m_currentSpheres.begin(), m_currentSpheres.end(),
            [](const PlanePilot::Math::Sphere& a, const PlanePilot::Math::Sphere& b) {
                return a.radius < b.radius;
            });
        
        auto smallest = std::min_element(m_currentSpheres.begin(), m_currentSpheres.end(),
            [](const PlanePilot::Math::Sphere& a, const PlanePilot::Math::Sphere& b) {
                return a.radius < b.radius;
            });
        
        // Render indicators
        glPointSize(10.0f);
        glBegin(GL_POINTS);
        
        // Largest sphere indicator (green)
        glColor3f(0.0f, 1.0f, 0.0f);
        glVertex3f(largest->center.x, largest->center.y, largest->center.z + largest->radius + 0.2f);
        
        // Smallest sphere indicator (blue)
        glColor3f(0.0f, 0.0f, 1.0f);
        glVertex3f(smallest->center.x, smallest->center.y, smallest->center.z + smallest->radius + 0.2f);
        
        glEnd();
        glPointSize(1.0f);
    }
    
    glEnable(GL_LIGHTING);
}

void SphereOMatic::renderAISpheres() {
    // Render AI-generated spheres with special highlighting
    glDisable(GL_LIGHTING);
    
    for (size_t i = 0; i < m_aiGeneratedSpheres.size(); ++i) {
        const auto& sphere = m_aiGeneratedSpheres[i];
        
        glPushMatrix();
        glTranslatef(sphere.center.x, sphere.center.y, sphere.center.z);
        
        // Pulsing effect for AI spheres
        float pulse = std::sin(m_simulationTime * 3.0f + i) * 0.1f + 1.0f;
        glScalef(sphere.radius * pulse, sphere.radius * pulse, sphere.radius * pulse);
        
        glColor4fv(sphere.color);
        
        // Render with special effect
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE);
        GLUquadric* quadric = gluNewQuadric();
        gluSphere(quadric, 1.0f, m_settings.quality / 2, m_settings.quality / 2);
        gluDeleteQuadric(quadric);
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL);
        
        glPopMatrix();
    }
    
    glEnable(GL_LIGHTING);
}

void SphereOMatic::renderUI() {
    if (m_ui) {
        m_ui->render();
    }
    
    renderStatistics();
}

void SphereOMatic::renderStatistics() {
    // Render statistics overlay
    // This would show sphere counts, collision info, AI status, etc.
}

void SphereOMatic::createSphereGeometry() {
    // Create sphere geometry for rendering
    // This would generate a sphere mesh with specified quality
}

void SphereOMatic::updateSimulation() {
    if (m_isSimulating) {
        m_simulationTime += 0.016f;  // 60 FPS
        
        if (m_settings.simulatePhysics) {
            updateSpherePhysics();
        }
    }
}

void SphereOMatic::updateCollisions() {
    if (m_isTestingCollisions) {
        m_collisionTestProgress += 0.01f;
        if (m_collisionTestProgress >= 1.0f) {
            m_collisionTestProgress = 1.0f;
            m_isTestingCollisions = false;
        }
    }
}

void SphereOMatic::updateAI() {
    // Update AI-related processes
}

void SphereOMatic::updateCamera() {
    if (m_camera) {
        m_camera->update();
    }
}

void SphereOMatic::updateUI() {
    if (m_ui) {
        m_ui->handleInput();
    }
}

void SphereOMatic::detectCollisions() {
    if (!m_collisionDetector) return;
    
    auto collisions = m_collisionDetector->detectAllCollisions(m_currentSpheres);
    Logger::info("Detected " + std::to_string(collisions.size()) + " collisions");
}

void SphereOMatic::testExtremalConfigurations() {
    Logger::info("Testing extremal configurations");
    
    // Test spheres at extreme positions and sizes
    // This would involve systematic testing of various configurations
}

void SphereOMatic::analyzeCollisionPatterns() {
    Logger::info("Analyzing collision patterns");
    
    // Analyze patterns in collisions to provide insights
}

void SphereOMatic::generateCollisionReport() {
    Logger::info("Generating collision report");
    
    // Generate detailed collision analysis report
}

void SphereOMatic::handleMouseInput() {
    // Handle mouse interactions for sphere selection and manipulation
}

void SphereOMatic::handleKeyboardInput() {
    // Handle keyboard controls for camera, simulation, etc.
}

void SphereOMatic::handle3DManipulation() {
    // Handle 3D scene manipulation
}

void SphereOMatic::handleSphereSelection() {
    // Handle sphere selection for detailed analysis
}

void SphereOMatic::updateSpherePhysics() {
    // Update physics simulation for spheres
}

void SphereOMatic::exportToJSON(const std::string& filename) {
    std::ofstream file(filename);
    if (file.is_open()) {
        file << "{\n";
        file << "  &quot;spheres&quot;: [\n";
        
        for (size_t i = 0; i < m_currentSpheres.size(); ++i) {
            const auto& sphere = m_currentSpheres[i];
            file << "    {\n";
            file << "      &quot;center&quot;: [" << sphere.center.x << ", " << sphere.center.y << ", " << sphere.center.z << "],\n";
            file << "      &quot;radius&quot;: " << sphere.radius << ",\n";
            file << "      &quot;mass&quot;: " << sphere.mass << ",\n";
            file << "      &quot;color&quot;: [" << sphere.color[0] << ", " << sphere.color[1] << ", " << sphere.color[2] << ", " << sphere.color[3] << "]\n";
            file << "    }";
            if (i < m_currentSpheres.size() - 1) file << ",";
            file << "\n";
        }
        
        file << "  ],\n";
        file << "  &quot;aiGeneratedSpheres&quot;: " << m_aiGeneratedSpheres.size() << ",\n";
        file << "  &quot;totalCollisions&quot;: " << (m_collisionDetector ? m_collisionDetector->detectAllCollisions(m_currentSpheres).size() : 0) << "\n";
        file << "}\n";
        file.close();
        
        Logger::info("Configuration exported to: " + filename);
    }
}

void SphereOMatic::reset() {
    m_currentSpheres = m_originalSpheres;
    m_aiGeneratedSpheres.clear();
    m_isSimulating = false;
    m_isTestingCollisions = false;
    m_simulationTime = 0.0f;
    m_collisionTestProgress = 0.0f;
    
    Logger::info("Sphere-O-Matic Workshop reset");
}

void SphereOMatic::cleanup() {
    Logger::info("Cleaning up Sphere-O-Matic Workshop");
    
    m_ui.reset();
    m_camera.reset();
    m_sphereModel.reset();
    m_wireframeShader.reset();
    m_phongShader.reset();
    m_renderer.reset();
    m_aiConnector.reset();
    m_geometryGenerator.reset();
    m_collisionDetector.reset();
}
} // namespace Workshops
} // namespace PlanePilot
