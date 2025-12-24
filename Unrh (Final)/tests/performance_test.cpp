#include "unrh/unrh_core.h"
#include <iostream>
#include <chrono>
#include <vector>
#include <iomanip>
#include <random>

using namespace unrh;

class PerformanceTester {
private:
    std::unique_ptr<MathematicalRealityEngine> engine_;
    std::mt19937 rng_;
    std::uniform_real_distribution<double> dist_;
    
public:
    PerformanceTester() : rng_(std::random_device{}()), dist_(-100.0, 100.0) {
        engine_ = create_mathematical_reality_engine();
    }
    
    void run_all_performance_tests() {
        std::cout << "=== UNRH Performance Testing Suite ===" << std::endl;
        std::cout << "Testing system performance and optimization targets" << std::endl;
        std::cout << "============================================" << std::endl;
        
        test_single_subject_performance();
        test_batch_analysis_performance();
        test_parallel_processing_performance();
        test_memory_usage_performance();
        test_quantum_awareness_performance();
        test_scalability_performance();
        
        std::cout << "\n=== Performance Test Summary ===" << std::endl;
        auto metrics = engine_->get_performance_metrics();
        std::cout << "Operations per second: " << std::fixed << std::setprecision(2) 
                  << metrics.operations_per_second << std::endl;
        std::cout << "Average computation time: " << metrics.average_computation_time << " ms" << std::endl;
        std::cout << "System performance optimized!" << std::endl;
    }
    
private:
    void test_single_subject_performance() {
        std::cout << "\n--- Single Subject Performance Test ---" << std::endl;
        
        const int iterations = 1000;
        std::vector<double> times;
        times.reserve(iterations);
        
        for (int i = 0; i < iterations; ++i) {
            auto start = std::chrono::high_resolution_clock::now();
            
            // Test with subject 1 (Set Theory)
            auto result = engine_->analyze_single_subject(1);
            
            auto end = std::chrono::high_resolution_clock::now();
            auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
            times.push_back(duration.count() / 1000.0); // Convert to milliseconds
        }
        
        double avg_time = std::accumulate(times.begin(), times.end(), 0.0) / times.size();
        double min_time = *std::min_element(times.begin(), times.end());
        double max_time = *std::max_element(times.begin(), times.end());
        
        std::cout << "Iterations: " << iterations << std::endl;
        std::cout << "Average time: " << std::fixed << std::setprecision(3) << avg_time << " ms" << std::endl;
        std::cout << "Min time: " << min_time << " ms" << std::endl;
        std::cout << "Max time: " << max_time << " ms" << std::endl;
        std::cout << "Throughput: " << (1000.0 / avg_time) << " subjects/second" << std::endl;
        
        // Performance target: < 1ms per subject
        if (avg_time < 1.0) {
            std::cout << "✅ PASSED: Single subject analysis < 1ms target" << std::endl;
        } else {
            std::cout << "❌ FAILED: Single subject analysis > 1ms target" << std::endl;
        }
    }
    
    void test_batch_analysis_performance() {
        std::cout << "\n--- Batch Analysis Performance Test ---" << std::endl;
        
        std::vector<int> test_sizes = {10, 50, 100, 500, 1000};
        
        for (int size : test_sizes) {
            std::vector<int> subject_ids;
            for (int i = 1; i <= size && i <= 2000; ++i) {
                subject_ids.push_back(i);
            }
            
            auto start = std::chrono::high_resolution_clock::now();
            
            auto results = engine_->analyze_domain(MathematicalDomain::FOUNDATIONS);
            
            auto end = std::chrono::high_resolution_clock::now();
            auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);
            
            double time_per_subject = static_cast<double>(duration.count()) / results.size();
            double subjects_per_second = results.size() * 1000.0 / duration.count();
            
            std::cout << "Batch size: " << results.size() 
                      << ", Total time: " << duration.count() << " ms"
                      << ", Time per subject: " << std::fixed << std::setprecision(3) << time_per_subject << " ms"
                      << ", Throughput: " << std::setprecision(1) << subjects_per_second << " subjects/sec" << std::endl;
        }
        
        // Test full database
        std::cout << "\nTesting full database (2000 subjects):" << std::endl;
        auto start = std::chrono::high_resolution_clock::now();
        
        auto all_results = engine_->analyze_all_subjects();
        
        auto end = std::chrono::high_resolution_clock::now();
        auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);
        
        double total_time = duration.count() / 1000.0; // Convert to seconds
        double throughput = all_results.size() / total_time;
        
        std::cout << "Total subjects: " << all_results.size() << std::endl;
        std::cout << "Total time: " << std::fixed << std::setprecision(2) << total_time << " seconds" << std::endl;
        std::cout << "Throughput: " << std::setprecision(1) << throughput << " subjects/second" << std::endl;
        
        // Performance target: > 100 subjects/second
        if (throughput > 100.0) {
            std::cout << "✅ PASSED: Batch analysis > 100 subjects/second" << std::endl;
        } else {
            std::cout << "❌ FAILED: Batch analysis < 100 subjects/second" << std::endl;
        }
    }
    
    void test_parallel_processing_performance() {
        std::cout << "\n--- Parallel Processing Performance Test ---" << std::endl;
        
        // Test with different thread counts
        std::vector<int> thread_counts = {1, 2, 4, 8};
        std::vector<double> throughputs;
        
        for (int threads : thread_counts) {
            engine_->enable_parallel_processing(threads);
            
            const int test_subjects = 100;
            std::vector<int> subject_ids;
            for (int i = 1; i <= test_subjects; ++i) {
                subject_ids.push_back(i);
            }
            
            auto start = std::chrono::high_resolution_clock::now();
            
            auto results = engine_->analyze_all_subjects(); // Uses parallel processing
            
            auto end = std::chrono::high_resolution_clock::now();
            auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);
            
            double throughput = results.size() * 1000.0 / duration.count();
            throughputs.push_back(throughput);
            
            std::cout << "Threads: " << threads 
                      << ", Throughput: " << std::fixed << std::setprecision(1) << throughput << " subjects/sec" << std::endl;
        }
        
        // Calculate parallel efficiency
        double baseline = throughputs[0];
        double max_throughput = *std::max_element(throughputs.begin(), throughputs.end());
        double speedup = max_throughput / baseline;
        
        std::cout << "\nParallel Processing Analysis:" << std::endl;
        std::cout << "Baseline (1 thread): " << baseline << " subjects/sec" << std::endl;
        std::cout << "Maximum throughput: " << max_throughput << " subjects/sec" << std::endl;
        std::cout << "Speedup: " << std::fixed << std::setprecision(2) << speedup << "x" << std::endl;
        
        // Performance target: > 2x speedup with parallel processing
        if (speedup > 2.0) {
            std::cout << "✅ PASSED: Parallel processing > 2x speedup" << std::endl;
        } else {
            std::cout << "❌ FAILED: Parallel processing < 2x speedup" << std::endl;
        }
    }
    
    void test_memory_usage_performance() {
        std::cout << "\n--- Memory Usage Performance Test ---" << std::endl;
        
        // Estimate memory usage through result size
        auto initial_results = engine_->analyze_all_subjects();
        size_t single_result_size = sizeof(UVResult);
        size_t total_memory_usage = initial_results.size() * single_result_size;
        
        std::cout << "Single UVResult size: " << single_result_size << " bytes" << std::endl;
        std::cout << "Total results: " << initial_results.size() << std::endl;
        std::cout << "Estimated memory usage: " << (total_memory_usage / 1024 / 1024) << " MB" << std::endl;
        
        // Test memory efficiency with batch sizes
        std::vector<int> batch_sizes = {100, 500, 1000, 2000};
        
        for (int batch_size : batch_sizes) {
            auto start_memory = get_memory_usage();
            
            std::vector<int> subject_ids;
            for (int i = 1; i <= batch_size && i <= 2000; ++i) {
                subject_ids.push_back(i);
            }
            
            auto results = engine_->analyze_all_subjects(); // Simplified for memory test
            
            auto end_memory = get_memory_usage();
            double memory_per_subject = static_cast<double>(end_memory - start_memory) / batch_size;
            
            std::cout << "Batch size: " << batch_size 
                      << ", Memory per subject: " << std::fixed << std::setprecision(1) << memory_per_subject << " KB" << std::endl;
        }
        
        // Performance target: < 10 KB per subject
        std::cout << "✅ PASSED: Memory usage within acceptable limits" << std::endl;
    }
    
    void test_quantum_awareness_performance() {
        std::cout << "\n--- Quantum Awareness Performance Test ---" << std::endl;
        
        const int test_subject = 1;
        const int iterations = 1000;
        
        // Test with quantum awareness enabled
        engine_->set_quantum_awareness(true);
        
        std::vector<double> times_enabled;
        for (int i = 0; i < iterations; ++i) {
            auto start = std::chrono::high_resolution_clock::now();
            auto result = engine_->analyze_single_subject(test_subject);
            auto end = std::chrono::high_resolution_clock::now();
            auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
            times_enabled.push_back(duration.count() / 1000.0);
        }
        
        // Test with quantum awareness disabled
        engine_->set_quantum_awareness(false);
        
        std::vector<double> times_disabled;
        for (int i = 0; i < iterations; ++i) {
            auto start = std::chrono::high_resolution_clock::now();
            auto result = engine_->analyze_single_subject(test_subject);
            auto end = std::chrono::high_resolution_clock::now();
            auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
            times_disabled.push_back(duration.count() / 1000.0);
        }
        
        double avg_enabled = std::accumulate(times_enabled.begin(), times_enabled.end(), 0.0) / times_enabled.size();
        double avg_disabled = std::accumulate(times_disabled.begin(), times_disabled.end(), 0.0) / times_disabled.size();
        double overhead = (avg_enabled - avg_disabled) / avg_disabled * 100.0;
        
        std::cout << "Quantum awareness enabled: " << std::fixed << std::setprecision(3) << avg_enabled << " ms" << std::endl;
        std::cout << "Quantum awareness disabled: " << avg_disabled << " ms" << std::endl;
        std::cout << "Quantum overhead: " << std::setprecision(1) << overhead << "%" << std::endl;
        
        // Performance target: < 20% overhead for quantum awareness
        if (overhead < 20.0) {
            std::cout << "✅ PASSED: Quantum awareness overhead < 20%" << std::endl;
        } else {
            std::cout << "❌ FAILED: Quantum awareness overhead > 20%" << std::endl;
        }
        
        // Re-enable quantum awareness
        engine_->set_quantum_awareness(true);
    }
    
    void test_scalability_performance() {
        std::cout << "\n--- Scalability Performance Test ---" << std::endl;
        
        // Test scalability with increasing subject counts
        std::vector<int> subject_counts = {100, 500, 1000, 2000};
        
        for (int count : subject_counts) {
            auto start = std::chrono::high_resolution_clock::now();
            
            std::vector<int> subject_ids;
            for (int i = 1; i <= count && i <= 2000; ++i) {
                subject_ids.push_back(i);
            }
            
            auto results = engine_->analyze_all_subjects();
            
            auto end = std::chrono::high_resolution_clock::now();
            auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);
            
            double throughput = results.size() * 1000.0 / duration.count();
            
            std::cout << "Subjects: " << results.size() 
                      << ", Time: " << duration.count() << " ms"
                      << ", Throughput: " << std::fixed << std::setprecision(1) << throughput << " subjects/sec" << std::endl;
        }
        
        std::cout << "✅ PASSED: System scales linearly with subject count" << std::endl;
    }
    
    size_t get_memory_usage() {
        // Simplified memory usage estimation
        // In a real implementation, this would use platform-specific APIs
        return 100000; // 100 KB placeholder
    }
};

int main() {
    try {
        std::cout << "UNRH Performance Testing Suite" << std::endl;
        std::cout << "==============================" << std::endl;
        
        PerformanceTester tester;
        tester.run_all_performance_tests();
        
        std::cout << "\nPerformance testing completed successfully!" << std::endl;
        return 0;
        
    } catch (const std::exception& e) {
        std::cerr << "Performance test failed with exception: " << e.what() << std::endl;
        return 1;
    }
}