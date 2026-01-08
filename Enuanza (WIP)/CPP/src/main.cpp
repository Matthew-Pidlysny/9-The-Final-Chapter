#include "../include/PrimeComposition3D.h"
#include <iostream>
#include <exception>

int main() {
    try {
        std::cout << "================================================" << std::endl;
        std::cout << "    Enuanza - Mathematical Immersion System    " << std::endl;
        std::cout << "         C++ Edition - Prime Framework        " << std::endl;
        std::cout << "================================================" << std::endl;
        std::cout << "Initializing λ-Based Mathematical Framework..." << std::endl;
        std::cout << "Constants: λ=0.6, 8/13≈0.615, C*=17/19≈0.895" << std::endl;
        std::cout << "Generator Primes: [7, 13, 17, 19]" << std::endl;
        std::cout << "================================================" << std::endl;
        
        // Create and initialize the application
        Enuanza::PrimeComposition3D app;
        
        if (!app.initialize()) {
            std::cerr << "Failed to initialize Enuanza application!" << std::endl;
            return -1;
        }
        
        std::cout << "\nControls:" << std::endl;
        std::cout << "  W/A/S/D - Move camera" << std::endl;
        std::cout << "  Mouse   - Look around" << std::endl;
        std::cout << "  Scroll  - Zoom in/out" << std::endl;
        std::cout << "  1-4     - Switch visualization modes" << std::endl;
        std::cout << "  V       - Toggle VR mode" << std::endl;
        std::cout << "  M       - Mute/unmute audio" << std::endl;
        std::cout << "  ESC     - Exit" << std::endl;
        std::cout << "================================================" << std::endl;
        std::cout << "Starting mathematical immersion..." << std::endl;
        std::cout << "================================================" << std::endl;
        
        // Run the main loop
        app.run();
        
        std::cout << "\nThank you for exploring mathematical beauty with Enuanza!" << std::endl;
        std::cout << "================================================" << std::endl;
        
        return 0;
        
    } catch (const std::exception& e) {
        std::cerr << "Fatal error: " << e.what() << std::endl;
        return -1;
    } catch (...) {
        std::cerr << "Unknown fatal error occurred!" << std::endl;
        return -1;
    }
}