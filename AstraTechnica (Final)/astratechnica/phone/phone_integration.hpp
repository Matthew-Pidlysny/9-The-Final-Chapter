#ifndef ASTRATECHNICA_PHONE_INTEGRATION_HPP
#define ASTRATECHNICA_PHONE_INTEGRATION_HPP

#include <string>
#include <vector>
#include <map>
#include <memory>
#include <functional>
#include <thread>
#include <mutex>
#include <atomic>
#include <queue>
#include <condition_variable>
#include <chrono>
#include <ctime>

namespace AstraTechnica {

    // Push notification structure
    struct PushNotification {
        std::string id;
        std::string title;
        std::string message;
        std::string category;
        int priority; // 1-5, 5 being highest
        std::chrono::system_clock::time_point timestamp;
        std::map<std::string, std::string> data;
        
        // Action buttons
        std::vector<std::string> action_buttons;
        
        // Auto-expire time (minutes)
        int expire_minutes = 60;
    };

    // Phone app states
    enum class PhoneAppState {
        OFFLINE,
        ONLINE,
        BACKGROUND,
        ACTIVE
    };

    // Notification response
    struct NotificationResponse {
        std::string notification_id;
        std::string action;
        std::map<std::string, std::string> response_data;
        std::chrono::system_clock::time_point timestamp;
    };

    // Security levels
    enum class SecurityLevel {
        NONE,
        BASIC,
        ENHANCED,
        MAXIMUM
    };

    // Phone Integration Class
    class PhoneIntegration {
    private:
        // Core systems
        std::atomic<PhoneAppState> current_state{PhoneAppState::OFFLINE};
        std::atomic<SecurityLevel> security_level{SecurityLevel::ENHANCED};
        std::atomic<bool> notifications_enabled{true};
        
        // Threading
        std::thread notification_thread;
        std::thread server_thread;
        std::mutex notification_mutex;
        std::mutex response_mutex;
        std::mutex state_mutex;
        std::condition_variable notification_cv;
        
        // Notification queue
        std::queue<PushNotification> notification_queue;
        std::map<std::string, PushNotification> active_notifications;
        std::queue<NotificationResponse> response_queue;
        
        // Device management
        std::string device_id;
        std::string user_token;
        std::map<std::string, std::string> device_info;
        
        // Server communication
        std::string server_endpoint;
        std::atomic<bool> server_connected{false};
        std::atomic<bool> should_stop{false};
        
        // Security
        std::string encryption_key;
        std::map<std::string, std::chrono::system_clock::time_point> failed_attempts;
        
        // Game event callbacks
        std::map<std::string, std::function<void(const NotificationResponse&)>> action_handlers;
        
    public:
        PhoneIntegration();
        ~PhoneIntegration();
        
        // Core initialization
        bool initialize();
        void shutdown();
        bool connect_to_server(const std::string& endpoint);
        void disconnect_from_server();
        
        // Device management
        bool register_device(const std::string& device_name);
        void set_device_info(const std::map<std::string, std::string>& info);
        std::string get_device_id() const { return device_id; }
        
        // Security management
        void set_security_level(SecurityLevel level);
        SecurityLevel get_security_level() const { return security_level.load(); }
        bool authenticate_user(const std::string& credentials);
        void generate_encryption_keys();
        
        // Notification management
        std::string send_notification(const PushNotification& notification);
        std::string send_notification(const std::string& title, const std::string& message, 
                                   int priority = 3, const std::string& category = "general");
        void send_critical_alert(const std::string& title, const std::string& message);
        
        // Game-specific notifications
        void notify_company_event(const std::string& event, const std::map<std::string, std::string>& details);
        void notify_server_status(const std::string& server_id, int health, const std::string& status);
        void notify_hack_attempt(const std::string& source, int threat_level);
        void notify_ghazarkhan_activity(const std::string& activity, int severity);
        void notify_investigation_update(const std::string& status);
        void notify_market_change(const std::string& asset, double old_price, double new_price);
        void notify_crew_status(const std::string& crew_member, const std::string& status);
        void notify_turn_update(int turn_number);
        void notify_emergency_situation(const std::string& emergency_type);
        
        // Response handling
        void register_action_handler(const std::string& action, 
                                   std::function<void(const NotificationResponse&)> handler);
        void handle_notification_response(const NotificationResponse& response);
        std::vector<NotificationResponse> get_pending_responses();
        
        // State management
        void set_app_state(PhoneAppState state);
        PhoneAppState get_app_state() const { return current_state.load(); }
        void enable_notifications(bool enabled);
        bool are_notifications_enabled() const { return notifications_enabled.load(); }
        
        // Real-time events
        void start_background_monitoring();
        void stop_background_monitoring();
        void process_real_time_events();
        
        // Security and privacy
        bool verify_request(const std::string& request_data, const std::string& signature);
        std::string encrypt_data(const std::string& data);
        std::string decrypt_data(const std::string& encrypted_data);
        void log_security_event(const std::string& event_type, const std::string& details);
        
        // Analytics and monitoring
        void track_notification_delivery(const std::string& notification_id, bool delivered);
        void track_user_action(const std::string& action, const std::map<std::string, std::string>& context);
        std::map<std::string, int> get_notification_statistics();
        
        // Testing and debugging
        void simulate_incoming_notification(const PushNotification& notification);
        void simulate_server_response(const std::string& response_data);
        void dump_notification_history();
        
        // Configuration
        void set_server_endpoint(const std::string& endpoint);
        void set_notification_limits(int max_per_hour, int max_per_day);
        void configure_auto_expire_minutes(int minutes);
        
    private:
        // Internal methods
        void notification_worker();
        void server_worker();
        void process_notification_queue();
        void cleanup_expired_notifications();
        std::string generate_notification_id();
        bool is_rate_limited();
        void update_notification_statistics(const std::string& type, bool success);
        
        // Network communication
        bool send_to_server(const std::string& data);
        std::string receive_from_server();
        bool establish_secure_connection();
        
        // Security helpers
        std::string generate_device_fingerprint();
        bool validate_device_integrity();
        void rotate_encryption_keys();
        
        // Rate limiting
        std::map<std::string, std::vector<std::chrono::system_clock::time_point>> rate_limit_tracker;
        int max_notifications_per_hour = 100;
        int max_notifications_per_day = 1000;
    };

    // Phone App Manager - High-level interface
    class PhoneAppManager {
    private:
        std::unique_ptr<PhoneIntegration> phone_integration;
        std::map<std::string, std::function<void()>> game_event_subscribers;
        
    public:
        PhoneAppManager();
        ~PhoneAppManager();
        
        bool initialize();
        void shutdown();
        
        // Game event registration
        void register_game_event(const std::string& event_name, std::function<void()> handler);
        
        // High-level notification methods
        void alert_player(const std::string& message);
        void request_player_action(const std::string& action_description, 
                                 const std::vector<std::string>& options);
        void update_game_state(const std::map<std::string, std::string>& state);
        
        // Configuration
        void set_player_preferences(const std::map<std::string, std::string>& preferences);
        
        // Integration with game systems
        void integrate_with_character_system(class Character* character);
        void integrate_with_company_system(class Company* company);
        void integrate_with_ai_system(class AISystem* ai_system);
        
        // Get access to underlying phone integration
        PhoneIntegration* get_phone_integration() { return phone_integration.get(); }
    };

} // namespace AstraTechnica

#endif // ASTRATECHNICA_PHONE_INTEGRATION_HPP