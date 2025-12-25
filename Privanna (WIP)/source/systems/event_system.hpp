/*
 * Event System - Optimized for Performance
 * Lock-free event queue with batch processing
 */

#ifndef EVENT_SYSTEM_HPP
#define EVENT_SYSTEM_HPP

#include <queue>
#include <mutex>
#include <atomic>
#include <functional>
#include <unordered_map>
#include <vector>
#include <memory>

namespace privanna {

enum class EventType {
    FACTION_UPDATE,
    UNIT_MOVED,
    MAGIC_CAST,
    COMBAT_RESOLVED,
    AI_DECISION,
    RESOURCE_CHANGED,
    TERRITORY_CAPTURED,
    ALLIANCE_FORMED,
    GAME_STATE_UPDATED
};

struct Event {
    EventType type;
    uint32_t timestamp;
    std::vector<uint8_t> data;
    
    Event(EventType t, const std::vector<uint8_t>& d) 
        : type(t), data(d) {
        timestamp = std::chrono::duration_cast<std::chrono::milliseconds>(
            std::chrono::high_resolution_clock::now().time_since_epoch()).count();
    }
};

class EventSystem {
private:
    // Lock-free event queue using ring buffer
    static constexpr size_t EVENT_QUEUE_SIZE = 65536;
    std::unique_ptr<Event[]> event_buffer_;
    std::atomic<size_t> write_index_{0};
    std::atomic<size_t> read_index_{0};
    
    // Event handlers
    std::unordered_map<EventType, std::vector<std::function<void(const Event&)>>> handlers_;
    
    // Performance optimization - batch processing
    std::vector<Event> event_batch_;
    static constexpr size_t BATCH_SIZE = 100;
    
public:
    EventSystem();
    ~EventSystem();
    
    bool initialize();
    void shutdown();
    
    // Optimized event publishing
    void publish_event(EventType type, const std::vector<uint8_t>& data);
    void publish_event_immediate(EventType type, const std::vector<uint8_t>& data);
    
    // Event subscription
    void subscribe(EventType type, std::function<void(const Event&)> handler);
    void unsubscribe(EventType type, uint32_t handler_id);
    
    // Batch processing
    void process_events();
    void process_events_batch();
    
    // Performance metrics
    size_t get_pending_events() const;
    size_t get_total_handlers() const;
    
private:
    void process_single_event(const Event& event);
    uint32_t next_handler_id_;
};

} // namespace privanna

#endif // EVENT_SYSTEM_HPP