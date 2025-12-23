/*
 * PLANE PILOT - Educational Hadwiger-Nelson Geometry Software
 * Main Entry Point
 * 
 * An interactive educational platform for exploring Hadwiger-Nelson problem,
 * chromatic geometry, and advanced mathematical concepts through visual learning.
 */

#include <iostream>
#include <memory>
#include <exception>
#include <cstdlib>

#include "PlanePilotApp.h"
#include "utils/Logger.h"

int main(int argc, char* argv[]) {
    try {
        Logger::info("Starting Plane Pilot - Educational Geometry Software");
        Logger::info("===============================================");
        Logger::info("Hadwiger-Nelson Problem Explorer v1.0.0");
        Logger::info("Copyright (c) 2024 - Educational Mathematics Laboratory");
        Logger::info("===============================================");
        
        // Initialize and run the application
        PlanePilotApp app;
        
        if (!app.initialize()) {
            Logger::error("Failed to initialize Plane Pilot application");
            return EXIT_FAILURE;
        }
        
        Logger::info("Application initialized successfully");
        
        // Run main application loop
        int result = app.run();
        
        Logger::info("Plane Pilot application shutting down");
        return result;
        
    } catch (const std::exception& e) {
        Logger::error("Unhandled exception: " + std::string(e.what()));
        std::cerr << "Fatal error: " << e.what() << std::endl;
        return EXIT_FAILURE;
    } catch (...) {
        Logger::error("Unknown fatal error occurred");
        std::cerr << "Unknown fatal error occurred" << std::endl;
        return EXIT_FAILURE;
    }
}