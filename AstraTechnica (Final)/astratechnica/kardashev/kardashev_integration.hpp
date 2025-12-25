#pragma once

// Kardashev Max Integration Header
// This file provides gentle integration of Kardashev Max systems
// without modifying existing core game engine files

#include "kardashev_max_system.hpp"

namespace AstraTechnica {
namespace KardashevIntegration {

/**
 * Kardashev Integration Manager
 * Provides seamless integration of Type V Multiversal systems
 * with existing AstraTechnica game engine
 */
class KardashevIntegrationManager {
private:
    static std::unique_ptr<KardashevMax::KardashevMaxSystem> kardashev_system;
    static bool initialized;
    
public:
    // Initialize Kardashev Max systems
    static void initialize_kardashev_max();
    
    // Get access to Kardashev systems
    static KardashevMax::KardashevMaxSystem* get_kardashev_system();
    
    // Check if Type V status is achieved
    static bool is_type_v_achieved();
    
    // Get total enhancement count
    static uint64_t get_total_enhancements();
    
    // Enable enterprise mode
    static void enable_enterprise_mode();
    
    // Update Kardashev systems (call from game loop)
    static void update_kardashev_systems();
    
    // Enterprise deployment recipe
    static std::string get_enterprise_deployment_recipe();
};

} // namespace KardashevIntegration
} // namespace AstraTechnica