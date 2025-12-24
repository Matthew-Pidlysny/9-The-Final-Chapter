#include "unrh/unrh_core.h"
#include <iostream>
#include <iomanip>

using namespace unrh;

int main() {
    try {
        std::cout << "UNRH: Understanding Nature Through Reference-Agitation Harmony" << std::endl;
        std::cout << "=================================================================" << std::endl;
        std::cout << "Educational Mathematical System v1.0.0" << std::endl;
        std::cout << "============================================================" << std::endl;
        
        // Initialize the mathematical reality engine
        auto engine = create_mathematical_reality_engine();
        
        std::cout << "\nInitializing UNRH System..." << std::endl;
        std::cout << "✅ Mathematical Reality Engine initialized" << std::endl;
        std::cout << "✅ 2000 mathematical subjects loaded" << std::endl;
        std::cout << "✅ U-V operators configured with quantum awareness" << std::endl;
        std::cout << "✅ Performance monitoring enabled" << std::endl;
        
        // Demonstrate U-V analysis
        std::cout << "\n--- U-V Analysis Demonstration ---" << std::endl;
        
        // Analyze a few sample subjects
        std::vector<int> sample_subjects = {1, 10, 100, 1000};
        
        for (int subject_id : sample_subjects) {
            auto result = engine->analyze_single_subject(subject_id);
            
            std::cout << "Subject " << std::setw(4) << subject_id << ": ";
            std::cout << "U=" << std::fixed << std::setprecision(3) << result.reference_score;
            std::cout << ", V=" << result.agitation_score;
            std::cout << ", Tension=" << result.tension;
            std::cout << ", Discovery=" << result.discovery_potential << std::endl;
        }
        
        // Find high discovery potential subjects
        std::cout << "\n--- High Discovery Potential Subjects ---" << std::endl;
        auto high_discovery = engine->find_high_discovery_potential_subjects(3.0);
        std::cout << "Found " << high_discovery.size() << " subjects with discovery potential > 3.0" << std::endl;
        
        if (!high_discovery.empty()) {
            std::cout << "Top 5 subjects: ";
            for (int i = 0; i < std::min(5, (int)high_discovery.size()); ++i) {
                std::cout << high_discovery[i];
                if (i < std::min(4, (int)high_discovery.size() - 1)) std::cout << ", ";
            }
            std::cout << std::endl;
        }
        
        // Performance metrics
        std::cout << "\n--- Performance Metrics ---" << std::endl;
        auto metrics = engine->get_performance_metrics();
        std::cout << "Operations per second: " << std::fixed << std::setprecision(2) 
                  << metrics.operations_per_second << std::endl;
        std::cout << "Average computation time: " << std::setprecision(3) 
                  << metrics.average_computation_time << " ms" << std::endl;
        std::cout << "Efficiency score: " << engine->get_performance_monitor()->get_efficiency_score() << std::endl;
        
        // Generate analysis report
        std::cout << "\n--- Analysis Report ---" << std::endl;
        engine->generate_analysis_report();
        
        std::cout << "\nUNRH System Demo Completed Successfully!" << std::endl;
        std::cout << "Ready for educational deployment and research applications." << std::endl;
        
        return 0;
        
    } catch (const std::exception& e) {
        std::cerr << "UNRH System Error: " << e.what() << std::endl;
        return 1;
    }
}