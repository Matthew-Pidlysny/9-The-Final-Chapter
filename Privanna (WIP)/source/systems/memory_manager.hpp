/*
 * Memory Manager - High Performance Memory System
 * Object pooling, arena allocation, cache-friendly structures
 */

#ifndef MEMORY_MANAGER_HPP
#define MEMORY_MANAGER_HPP

#include <memory>
#include <unordered_map>
#include <vector>
#include <atomic>
#include <mutex>
#include <cstddef>

namespace privanna {

// Memory pool for game objects
template<typename T, size_t PoolSize = 1024>
class ObjectPool {
private:
    alignas(T) char pool_[PoolSize * sizeof(T)];
    std::bitset<PoolSize> used_;
    std::atomic<size_t> next_free_{0};
    mutable std::mutex mutex_;
    
public:
    ObjectPool() = default;
    ~ObjectPool() = default;
    
    template<typename... Args>
    T* allocate(Args&&... args) {
        std::lock_guard<std::mutex> lock(mutex_);
        
        // Find next free slot
        for (size_t i = 0; i < PoolSize; ++i) {
            size_t idx = (next_free_ + i) % PoolSize;
            if (!used_[idx]) {
                used_[idx] = true;
                next_free_ = (idx + 1) % PoolSize;
                return new(pool_ + idx * sizeof(T)) T(std::forward<Args>(args)...);
            }
        }
        return nullptr; // Pool exhausted
    }
    
    void deallocate(T* ptr) {
        if (!ptr) return;
        
        std::lock_guard<std::mutex> lock(mutex_);
        size_t offset = reinterpret_cast<char*>(ptr) - pool_;
        size_t idx = offset / sizeof(T);
        
        if (idx < PoolSize && used_[idx]) {
            ptr->~T();
            used_[idx] = false;
        }
    }
    
    size_t capacity() const { return PoolSize; }
    size_t used_count() const { 
        std::lock_guard<std::mutex> lock(mutex_);
        return used_.count(); 
    }
};

// Arena allocator for game state
class ArenaAllocator {
private:
    std::vector<std::unique_ptr<char[]>> blocks_;
    std::vector<char*> free_blocks_;
    size_t block_size_;
    size_t current_offset_;
    char* current_block_;
    mutable std::mutex mutex_;
    
public:
    explicit ArenaAllocator(size_t block_size = 1024 * 1024) // 1MB blocks
        : block_size_(block_size), current_offset_(0), current_block_(nullptr) {}
    
    ~ArenaAllocator();
    
    void* allocate(size_t size, size_t alignment = 8);
    void reset(); // Clear all allocations
    size_t get_total_allocated() const;
    size_t get_block_count() const;
};

// Memory manager coordinates all memory systems
class MemoryManager {
private:
    // Object pools for common game types
    std::unordered_map<size_t, std::unique_ptr<void, void(*)(void*)>> pools_;
    
    // Arena allocator for game state
    std::unique_ptr<ArenaAllocator> arena_;
    
    // Performance tracking
    std::atomic<size_t> total_allocated_{0};
    std::atomic<size_t> peak_allocated_{0};
    std::atomic<size_t> allocation_count_{0};
    
    // Configuration
    size_t max_memory_;
    bool enable_profiling_;
    
public:
    explicit MemoryManager(size_t max_memory = 1024 * 1024 * 1024); // 1GB default
    ~MemoryManager();
    
    bool initialize();
    void shutdown();
    
    // Arena allocation
    void* allocate_arena(size_t size, size_t alignment = 8);
    void reset_arena();
    
    // Object pool allocation
    template<typename T, typename... Args>
    T* allocate_object(Args&&... args);
    
    template<typename T>
    void deallocate_object(T* ptr);
    
    // Performance monitoring
    size_t get_total_allocated() const { return total_allocated_.load(); }
    size_t get_peak_allocated() const { return peak_allocated_.load(); }
    size_t get_allocation_count() const { return allocation_count_.load(); }
    
    // Memory statistics
    struct MemoryStats {
        size_t total_allocated;
        size_t peak_allocated;
        size_t allocation_count;
        size_t arena_used;
        size_t pool_used;
        double fragmentation_ratio;
    };
    
    MemoryStats get_memory_stats() const;
    
private:
    void* allocate_raw(size_t size);
    void deallocate_raw(void* ptr, size_t size);
    
    template<typename T>
    void create_pool();
};

} // namespace privanna

#endif // MEMORY_MANAGER_HPP