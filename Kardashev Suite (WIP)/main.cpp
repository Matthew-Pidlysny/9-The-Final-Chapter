/*
 * Kardashev Suite - Main Application Entry Point
 * Round 1: Foundation Implementation
 * 
 * SuperNinja and 9 Software present: Kardashev Suite
 * Type V Multiversal Software Evaluation System
 */

#include "kardashev_file_types.h"
#include "kardashev_dependency_system.h"
#include "kardashev_gui_framework.h"
#include "kardashev_evaluation_engine.h"

#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <exception>

using namespace KardashevSuite;
using namespace KardashevSuite::GUI;
using namespace KardashevSuite::Evaluation;

class KardashevSuiteApp {
private:
    std::unique_ptr<Application> app_;
    std::unique_ptr<KardashevEvaluationEngine> evaluation_engine_;
    std::unique_ptr<KardashevDependencyManager> dependency_manager_;
    std::shared_ptr<Window> main_window_;
    
public:
    KardashevSuiteApp() = default;
    ~KardashevSuiteApp() = default;
    
    bool initialize() {
        std::cout << "=== Kardashev Suite - Round 1 Foundation ===" << std::endl;
        std::cout << "SuperNinja & 9 Software Present" << std::endl;
        std::cout << "Type V Multiversal Software Evaluation System" << std::endl;
        std::cout << std::endl;
        
        try {
            // Initialize GUI application
            app_ = ApplicationFactory::create_application();
            if (!app_->initialize()) {
                std::cerr << "Failed to initialize GUI application" << std::endl;
                return false;
            }
            
            // Initialize evaluation engine
            evaluation_engine_ = std::make_unique<KardashevEvaluationEngine>();
            
            // Register evaluators for different metrics
            evaluation_engine_->register_evaluator(MetricType::CODE_QUALITY, 
                std::make_unique<CodeQualityEvaluator>());
            evaluation_engine_->register_evaluator(MetricType::PERFORMANCE, 
                std::make_unique<PerformanceEvaluator>());
            evaluation_engine_->register_evaluator(MetricType::SECURITY, 
                std::make_unique<SecurityEvaluator>());
            
            // Initialize dependency manager
            dependency_manager_ = std::make_unique<KardashevDependencyManager>();
            
            // Create main window
            main_window_ = app_->create_window();
            if (!main_window_->create("Kardashev Suite - Round 1 Foundation", 1200, 800)) {
                std::cerr << "Failed to create main window" << std::endl;
                return false;
            }
            
            setup_main_ui();
            
            std::cout << "Kardashev Suite initialized successfully!" << std::endl;
            return true;
            
        } catch (const std::exception& e) {
            std::cerr << "Initialization error: " << e.what() << std::endl;
            return false;
        }
    }
    
    void setup_main_ui() {
        // Create main panel
        auto main_panel = WidgetFactory::create_panel();
        main_window_->set_root_widget(main_panel);
        
        // Create title label
        auto title_label = WidgetFactory::create_label("Kardashev Suite - Round 1 Foundation");
        
        // Create evaluation button
        auto eval_button = WidgetFactory::create_button();
        eval_button->set_on_click([this]() { run_evaluation_demo(); });
        
        // Create file type demo buttons
        auto k1_button = WidgetFactory::create_button();
        k1_button->set_on_click([this]() { create_demo_file(KardashevLevel::K1); });
        
        auto k2_button = WidgetFactory::create_button();
        k2_button->set_on_click([this]() { create_demo_file(KardashevLevel::K2); });
        
        auto k3_button = WidgetFactory::create_button();
        k3_button->set_on_click([this]() { create_demo_file(KardashevLevel::K3); });
        
        auto k4_button = WidgetFactory::create_button();
        k4_button->set_on_click([this]() { create_demo_file(KardashevLevel::K4); });
        
        auto k5_button = WidgetFactory::create_button();
        k5_button->set_on_click([this]() { create_demo_file(KardashevLevel::K5); });
        
        // Add widgets to main panel (simplified layout)
        main_panel->add_child(title_label);
        main_panel->add_child(eval_button);
        main_panel->add_child(k1_button);
        main_panel->add_child(k2_button);
        main_panel->add_child(k3_button);
        main_panel->add_child(k4_button);
        main_panel->add_child(k5_button);
    }
    
    void run_evaluation_demo() {
        std::cout << "\n=== Running Kardashev Evaluation Demo ===" << std::endl;
        
        // Evaluate the repository we analyzed
        EvaluationResult result = evaluation_engine_->evaluate_project(
            "../9-The-Final-Chapter", KardashevLevel::K5);
        
        std::cout << "Evaluation Results:" << std::endl;
        std::cout << "Overall Score: " << result.overall_score << std::endl;
        std::cout << "Assessed Level: " << static_cast<int>(result.assessed_level) << std::endl;
        std::cout << "Industrial Standards: " << (result.meets_industrial_standards ? "YES" : "NO") << std::endl;
        std::cout << "Evaluation Time: " << result.evaluation_time.count() << "ms" << std::endl;
        
        std::cout << "\nMetric Scores:" << std::endl;
        for (const auto& [metric, score] : result.metric_scores) {
            std::cout << "  " << static_cast<int>(metric) << ": " << score << std::endl;
        }
        
        std::cout << "\nStrengths:" << std::endl;
        for (const auto& strength : result.strengths) {
            std::cout << "  + " << strength << std::endl;
        }
        
        std::cout << "\nRecommendations:" << std::endl;
        for (const auto& recommendation : result.recommendations) {
            std::cout << "  * " << recommendation << std::endl;
        }
    }
    
    void create_demo_file(KardashevLevel level) {
        auto kardashev_file = KardashevFileFactory::create_file(level);
        if (!kardashev_file) {
            std::cout << "Failed to create Kardashev file for level " << static_cast<int>(level) << std::endl;
            return;
        }
        
        // Set up metadata
        KardashevFileMetadata metadata = kardashev_file->get_metadata();
        metadata.author = "SuperNinja & 9 Software";
        metadata.description = "Kardashev Suite Round 1 Demo File";
        
        kardashev_file->set_metadata(metadata);
        
        // Create demo filename
        std::string filename = "demo_k" + std::to_string(static_cast<int>(level)) + 
                              KardashevFileFactory::create_file(level)->get_metadata().version + 
                              KardashevFileImpl<level>::get_file_extension();
        
        // Save demo file
        if (kardashev_file->save(filename)) {
            std::cout << "Created demo file: " << filename << std::endl;
            std::cout << "Level: " << KardashevFileImpl<level>::get_level_description() << std::endl;
            std::cout << "Quality Score: " << kardashev_file->evaluate_quality() << std::endl;
        } else {
            std::cout << "Failed to save demo file: " << filename << std::endl;
        }
    }
    
    void run() {
        std::cout << "\nStarting Kardashev Suite GUI..." << std::endl;
        main_window_->show();
        app_->run();
    }
    
    void cleanup() {
        if (app_) {
            app_->cleanup();
        }
    }
};

int main(int argc, char* argv[]) {
    try {
        KardashevSuiteApp app;
        
        if (!app.initialize()) {
            std::cerr << "Failed to initialize Kardashev Suite" << std::endl;
            return 1;
        }
        
        app.run();
        app.cleanup();
        
    } catch (const std::exception& e) {
        std::cerr << "Application error: " << e.what() << std::endl;
        return 1;
    }
    
    return 0;
}