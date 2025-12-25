/*
 * Threading System - High Performance Concurrency
 * Work-stealing queues, thread pools, lock-free data structures
 */

#ifndef THREADING_SYSTEM_HPP
#define THREADING_SYSTEM_HPP

#include <thread>
#include <vector>
#include <queue>
#include <mutex>
#include <atomic>
#include <condition_variable>
#include <functional>
#include <future>
#include <memory>

namespace privanna {

// Task wrapper for thread pool
class Task {
private:
    std::function<void()> function_;
    uint32_t priority_;
    std::chrono::steady_clock::time_point schedule_time_;
    
public:
    Task(std::function<void()> func, uint32_t priority = 0)
        : function_(std::move(func)), priority_(priority), 
          schedule_time_(std::chrono::steady_clock::now()) {}
    
    void execute() { function_(); }
    uint32_t get_priority() const { return priority_; }
    auto get_schedule_time() const { return schedule_time_; }
};

// Lock-free work queue for thread pool
class WorkQueue {
private:
    struct Node {
        std::unique_ptr<Task> task;
        std::atomic<Node*> next{nullptr};
    };
    
    std::atomic<Node*> head_{nullptr};
    std::atomic<Node*> tail_{nullptr};
    
public:
    WorkQueue() = default;
    ~WorkQueue();
    
    void push(std::unique_ptr<Task> task);
    std::unique_ptr<Task> pop();
    std::unique_ptr<Task> steal();
    bool empty() const;
};

// Worker thread with work-stealing
class Worker {
private:
    std::thread thread_;
    WorkQueue local_queue_;
    std::vector<WorkQueue*> all_queues_;
    std::atomic<bool> running_{false};
    std::atomic<size_t> tasks_completed_{0};
    uint32_t worker_id_;
    
public:
    Worker(uint32_t id, std::vector<WorkQueue*> queues);
    ~Worker();
    
    void start();
    void stop();
    void add_task(std::unique_ptr<Task> task);
    
    size_t get_tasks_completed() const { return tasks_completed_.load(); }
    uint32_t get_worker_id() const { return worker_id_; }
    
private:
    void worker_loop();
    std::unique_ptr<Task> get_task();
};

// High-performance thread pool
class ThreadPool {
private:
    std::vector<std::unique_ptr<Worker>> workers_;
    std::vector<WorkQueue> work_queues_;
    std::atomic<bool> shutdown_{false};
    
    // Performance metrics
    std::atomic<size_t> total_tasks_{0};
    std::atomic<size_t> completed_tasks_{0};
    
public:
    explicit ThreadPool(size_t num_threads = 0);
    ~ThreadPool();
    
    bool initialize();
    void shutdown();
    
    // Task submission
    template<typename F, typename... Args>
    auto submit(F&& f, Args&&... args) -> std::future<decltype(f(args...))>;
    
    void submit_task(std::unique_ptr<Task> task);
    
    // Priority tasks
    template<typename F, typename... Args>
    auto submit_priority(uint32_t priority, F&& f, Args&&... args) -> std::future<decltype(f(args...))>;
    
    // Performance monitoring
    size_t get_total_tasks() const { return total_tasks_.load(); }
    size_t get_completed_tasks() const { return completed_tasks_.load(); }
    size_t get_active_threads() const { return workers_.size(); }
    
    // Load balancing
    void rebalance_work();
    std::vector<size_t> get_worker_load() const;
    
private:
    Worker* get_least_loaded_worker();
    void update_metrics();
};

// Thread-local storage optimization
class ThreadLocalStorage {
private:
    thread_local static std::unordered_map<size_t, std::unique_ptr<void, void(*)(void*)>> data_;
    
public:
    template<typename T>
    static T* get(size_t key);
    
    template<typename T>
    static void set(size_t key, std::unique_ptr<T> value);
    
    static void clear();
};

// Barrier synchronization for thread coordination
class Barrier {
private:
    std::mutex mutex_;
    std::condition_variable cv_;
    size_t count_;
    size_t waiting_;
    size_t generation_;
    
public:
    explicit Barrier(size_t count) : count_(count), waiting_(0), generation_(0) {}
    
    void wait();
    void reset(size_t new_count);
};

// Main threading system
class ThreadingSystem {
private:
    std::unique_ptr<ThreadPool> thread_pool_;
    std::unique_ptr<Barrier> frame_barrier_;
    std::atomic<bool> initialized_{false};
    
    // Performance tracking
    std::atomic<uint64_t> total_thread_time_{0};
    std::atomic<size_t> context_switches_{0};
    
public:
    ThreadingSystem() = default;
    ~ThreadingSystem();
    
    bool initialize(size_t num_threads = 0);
    void shutdown();
    
    // Task execution
    template<typename F, typename... Args>
    auto submit_task(F&& f, Args&&... args) -> std::future<decltype(f(args...))>;
    
    template<typename F, typename... Args>
    auto submit_priority_task(uint32_t priority, F&& f, Args&&... args) -> std::future<decltype(f(args...))>;
    
    // Synchronization
    void sync_all_threads();
    void barrier_wait();
    
    // Thread utilities
    size_t get_thread_count() const;
    uint32_t get_current_thread_id() const;
    
    // Performance monitoring
    struct ThreadStats {
        size_t total_tasks;
        size_t completed_tasks;
        size_t active_threads;
        uint64_t total_thread_time;
        size_t context_switches;
        double cpu_utilization;
    };
    
    ThreadStats get_thread_stats() const;
    
private:
    void update_performance_stats();
};

} // namespace privanna

#endif // THREADING_SYSTEM_HPP