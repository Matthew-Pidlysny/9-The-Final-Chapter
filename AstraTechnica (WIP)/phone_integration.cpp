#include "phone_integration.hpp"
#include "../core/game_engine.hpp"
#include <iostream>
#include <sstream>
#include <random>
#include <algorithm>
#include <ctime>
#include <openssl/sha.h>
#include <openssl/aes.h>
#include <openssl/rand.h>
#include <curl/curl.h>
#include <nlohmann/json.hpp>

namespace AstraTechnica {

    // PhoneIntegration Implementation
    PhoneIntegration::PhoneIntegration() {
        device_id = generate_device_fingerprint();
        generate_encryption_keys();
    }
    
    PhoneIntegration::~PhoneIntegration() {
        shutdown();
    }
    
    bool PhoneIntegration::initialize() {
        try {
            // Initialize libcurl
            curl_global_init(CURL_GLOBAL_DEFAULT);
            
            // Start worker threads
            should_stop.store(false);
            notification_thread = std::thread(&PhoneIntegration::notification_worker, this);
            server_thread = std::thread(&PhoneIntegration::server_worker, this);
            
            // Set initial state
            current_state.store(PhoneAppState::ONLINE);
            notifications_enabled.store(true);
            
            std::cout << "Phone Integration initialized successfully" << std::endl;
            return true;
        } catch (const std::exception& e) {
            std::cerr << "Failed to initialize Phone Integration: " << e.what() << std::endl;
            return false;
        }
    }
    
    void PhoneIntegration::shutdown() {
        should_stop.store(true);
        notification_cv.notify_all();
        
        if (notification_thread.joinable()) {
            notification_thread.join();
        }
        
        if (server_thread.joinable()) {
            server_thread.join();
        }
        
        curl_global_cleanup();
        std::cout << "Phone Integration shutdown completed" << std::endl;
    }
    
    bool PhoneIntegration::connect_to_server(const std::string& endpoint) {
        std::lock_guard<std::mutex> lock(state_mutex);
        server_endpoint = endpoint;
        
        if (establish_secure_connection()) {
            server_connected.store(true);
            std::cout << "Connected to AstraTechnica server: " << endpoint << std::endl;
            return true;
        }
        
        return false;
    }
    
    void PhoneIntegration::disconnect_from_server() {
        std::lock_guard<std::mutex> lock(state_mutex);
        server_connected.store(false);
        server_endpoint.clear();
    }
    
    bool PhoneIntegration::register_device(const std::string& device_name) {
        nlohmann::json registration_data;
        registration_data["device_id"] = device_id;
        registration_data["device_name"] = device_name;
        registration_data["timestamp"] = std::chrono::duration_cast<std::chrono::seconds>(
            std::chrono::system_clock::now().time_since_epoch()).count();
        
        std::string response = send_to_server(registration_data.dump());
        
        if (!response.empty()) {
            try {
                auto json_response = nlohmann::json::parse(response);
                if (json_response.contains("user_token")) {
                    user_token = json_response["user_token"];
                    return true;
                }
            } catch (...) {
                // JSON parsing failed
            }
        }
        
        return false;
    }
    
    std::string PhoneIntegration::send_notification(const PushNotification& notification) {
        if (!notifications_enabled.load() || current_state.load() == PhoneAppState::OFFLINE) {
            return "";
        }
        
        // Rate limiting check
        if (is_rate_limited()) {
            return "";
        }
        
        std::string notification_id = generate_notification_id();
        PushNotification notification_copy = notification;
        notification_copy.id = notification_id;
        notification_copy.timestamp = std::chrono::system_clock::now();
        
        {
            std::lock_guard<std::mutex> lock(notification_mutex);
            notification_queue.push(notification_copy);
            active_notifications[notification_id] = notification_copy;
        }
        
        notification_cv.notify_one();
        
        std::cout << "Notification queued: " << notification.title << " (ID: " << notification_id << ")" << std::endl;
        return notification_id;
    }
    
    std::string PhoneIntegration::send_notification(const std::string& title, const std::string& message, 
                                                    int priority, const std::string& category) {
        PushNotification notification;
        notification.title = title;
        notification.message = message;
        notification.priority = priority;
        notification.category = category;
        notification.timestamp = std::chrono::system_clock::now();
        
        return send_notification(notification);
    }
    
    void PhoneIntegration::send_critical_alert(const std::string& title, const std::string& message) {
        PushNotification alert;
        alert.title = "🚨 CRITICAL: " + title;
        alert.message = message;
        alert.priority = 5;
        alert.category = "critical";
        alert.action_buttons = {"Acknowledge", "View Details"};
        alert.expire_minutes = 5; // Critical alerts expire quickly
        
        send_notification(alert);
    }
    
    // Game-specific notification methods
    void PhoneIntegration::notify_company_event(const std::string& event, const std::map<std::string, std::string>& details) {
        std::ostringstream oss;
        oss << "Company Event: " << event;
        
        PushNotification notification;
        notification.title = "Company Update";
        notification.message = oss.str();
        notification.priority = 3;
        notification.category = "company";
        notification.data = details;
        
        send_notification(notification);
    }
    
    void PhoneIntegration::notify_server_status(const std::string& server_id, int health, const std::string& status) {
        std::ostringstream oss;
        oss << "Server " << server_id << ": " << status << " (Health: " << health << "%)";
        
        std::string priority = health < 30 ? "4" : "2";
        send_notification("Server Alert", oss.str(), std::stoi(priority), "servers");
    }
    
    void PhoneIntegration::notify_hack_attempt(const std::string& source, int threat_level) {
        std::ostringstream oss;
        oss << "Hack attempt detected from " << source << " (Threat Level: " << threat_level << ")";
        
        send_critical_alert("Security Alert", oss.str());
    }
    
    void PhoneIntegration::notify_ghazarkhan_activity(const std::string& activity, int severity) {
        std::ostringstream oss;
        oss << "Ghazarkhan activity: " << activity << " (Severity: " << severity << ")";
        
        PushNotification notification;
        notification.title = "🌑 Shadow Activity";
        notification.message = oss.str();
        notification.priority = severity > 7 ? 5 : 3;
        notification.category = "ghazarkhan";
        notification.action_buttons = {"Investigate", "Ignore"};
        
        send_notification(notification);
    }
    
    void PhoneIntegration::notify_investigation_update(const std::string& status) {
        send_notification("Investigation", status, 3, "investigation");
    }
    
    void PhoneIntegration::notify_market_change(const std::string& asset, double old_price, double new_price) {
        double change_percent = ((new_price - old_price) / old_price) * 100;
        std::ostringstream oss;
        oss << asset << ": $" << new_price << " (" << (change_percent >= 0 ? "+" : "") << change_percent << "%)";
        
        send_notification("Market Update", oss.str(), abs(change_percent) > 10 ? 4 : 2, "market");
    }
    
    void PhoneIntegration::notify_crew_status(const std::string& crew_member, const std::string& status) {
        send_notification("Crew Update", crew_member + ": " + status, 2, "crew");
    }
    
    void PhoneIntegration::notify_turn_update(int turn_number) {
        std::ostringstream oss;
        oss << "Turn " << turn_number << " has begun. Check your company status.";
        
        send_notification("Turn Update", oss.str(), 2, "game");
    }
    
    void PhoneIntegration::notify_emergency_situation(const std::string& emergency_type) {
        send_critical_alert("EMERGENCY", emergency_type);
    }
    
    void PhoneIntegration::register_action_handler(const std::string& action, 
                                                   std::function<void(const NotificationResponse&)> handler) {
        action_handlers[action] = handler;
    }
    
    void PhoneIntegration::handle_notification_response(const NotificationResponse& response) {
        std::lock_guard<std::mutex> lock(response_mutex);
        response_queue.push(response);
        
        // Execute registered handler
        auto it = action_handlers.find(response.action);
        if (it != action_handlers.end()) {
            it->second(response);
        }
        
        std::cout << "Received response for notification " << response.notification_id << ": " << response.action << std::endl;
    }
    
    std::vector<NotificationResponse> PhoneIntegration::get_pending_responses() {
        std::lock_guard<std::mutex> lock(response_mutex);
        std::vector<NotificationResponse> responses;
        
        while (!response_queue.empty()) {
            responses.push_back(response_queue.front());
            response_queue.pop();
        }
        
        return responses;
    }
    
    void PhoneIntegration::set_security_level(SecurityLevel level) {
        security_level.store(level);
        
        if (level >= SecurityLevel::ENHANCED) {
            rotate_encryption_keys();
        }
    }
    
    bool PhoneIntegration::authenticate_user(const std::string& credentials) {
        // Implement proper authentication logic here
        // For now, basic validation
        if (credentials.length() >= 8) {
            return true;
        }
        return false;
    }
    
    void PhoneIntegration::generate_encryption_keys() {
        // Generate AES-256 key
        encryption_key.resize(32);
        RAND_bytes(reinterpret_cast<unsigned char*>(&encryption_key[0]), 32);
    }
    
    std::string PhoneIntegration::generate_device_fingerprint() {
        std::ostringstream oss;
        oss << std::hex << std::time(nullptr) << "_" << rand();
        return oss.str();
    }
    
    std::string PhoneIntegration::generate_notification_id() {
        std::random_device rd;
        std::mt19937 gen(rd());
        std::uniform_int_distribution<> dis(100000, 999999);
        
        std::ostringstream oss;
        oss << "notif_" << dis(gen) << "_" << std::chrono::duration_cast<std::chrono::milliseconds>(
            std::chrono::system_clock::now().time_since_epoch()).count();
        return oss.str();
    }
    
    // Worker threads
    void PhoneIntegration::notification_worker() {
        while (!should_stop.load()) {
            std::unique_lock<std::mutex> lock(notification_mutex);
            
            notification_cv.wait(lock, [this] {
                return !notification_queue.empty() || should_stop.load();
            });
            
            if (should_stop.load()) break;
            
            process_notification_queue();
        }
    }
    
    void PhoneIntegration::server_worker() {
        while (!should_stop.load()) {
            if (server_connected.load()) {
                // Process server communications
                std::string server_data = receive_from_server();
                if (!server_data.empty()) {
                    // Handle server responses
                    try {
                        auto json_data = nlohmann::json::parse(server_data);
                        if (json_data.contains("type") && json_data["type"] == "notification") {
                            // Process server-sent notification
                            PushNotification server_notif;
                            server_notif.title = json_data.value("title", "");
                            server_notif.message = json_data.value("message", "");
                            server_notif.priority = json_data.value("priority", 3);
                            send_notification(server_notif);
                        }
                    } catch (...) {
                        // Invalid JSON, ignore
                    }
                }
            }
            
            std::this_thread::sleep_for(std::chrono::seconds(5));
        }
    }
    
    void PhoneIntegration::process_notification_queue() {
        while (!notification_queue.empty()) {
            PushNotification notification = notification_queue.front();
            notification_queue.pop();
            
            // Send to server if connected
            if (server_connected.load()) {
                nlohmann::json notification_data;
                notification_data["id"] = notification.id;
                notification_data["title"] = notification.title;
                notification_data["message"] = notification.message;
                notification_data["priority"] = notification.priority;
                notification_data["category"] = notification.category;
                notification_data["device_id"] = device_id;
                notification_data["timestamp"] = std::chrono::duration_cast<std::chrono::seconds>(
                    notification.timestamp.time_since_epoch()).count();
                
                if (!notification.data.empty()) {
                    notification_data["data"] = notification.data;
                }
                
                if (!notification.action_buttons.empty()) {
                    notification_data["actions"] = notification.action_buttons;
                }
                
                send_to_server(notification_data.dump());
            }
            
            update_notification_statistics("sent", true);
        }
    }
    
    bool PhoneIntegration::send_to_server(const std::string& data) {
        if (!server_connected.load()) return false;
        
        CURL* curl = curl_easy_init();
        if (!curl) return false;
        
        std::string response;
        curl_easy_setopt(curl, CURLOPT_URL, server_endpoint.c_str());
        curl_easy_setopt(curl, CURLOPT_POSTFIELDS, data.c_str());
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, +[](void* contents, size_t size, size_t nmemb, void* userp) -> size_t {
            ((std::string*)userp)->append((char*)contents, size * nmemb);
            return size * nmemb;
        });
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, &response);
        
        CURLcode res = curl_easy_perform(curl);
        curl_easy_cleanup(curl);
        
        return res == CURLE_OK;
    }
    
    std::string PhoneIntegration::receive_from_server() {
        // Implement server polling or WebSocket connection
        // For now, return empty string (will be implemented with actual server)
        return "";
    }
    
    bool PhoneIntegration::establish_secure_connection() {
        // Implement TLS/SSL connection establishment
        return !server_endpoint.empty();
    }
    
    bool PhoneIntegration::is_rate_limited() {
        auto now = std::chrono::system_clock::now();
        auto hour_ago = now - std::chrono::hours(1);
        auto day_ago = now - std::chrono::hours(24);
        
        // Clean old entries
        for (auto it = rate_limit_tracker.begin(); it != rate_limit_tracker.end();) {
            auto& timestamps = it->second;
            timestamps.erase(std::remove_if(timestamps.begin(), timestamps.end(),
                [hour_ago](const auto& timestamp) { return timestamp < hour_ago; }), timestamps.end());
            
            if (timestamps.empty()) {
                it = rate_limit_tracker.erase(it);
            } else {
                ++it;
            }
        }
        
        // Check hourly limit
        auto& hourly = rate_limit_tracker["hourly"];
        auto& daily = rate_limit_tracker["daily"];
        
        if (hourly.size() >= max_notifications_per_hour || daily.size() >= max_notifications_per_day) {
            return true;
        }
        
        hourly.push_back(now);
        daily.push_back(now);
        
        return false;
    }
    
    void PhoneIntegration::update_notification_statistics(const std::string& type, bool success) {
        // Update statistics tracking
    }
    
    void PhoneIntegration::rotate_encryption_keys() {
        generate_encryption_keys();
    }
    
    // PhoneAppManager Implementation
    PhoneAppManager::PhoneAppManager() {
        phone_integration = std::make_unique<PhoneIntegration>();
    }
    
    PhoneAppManager::~PhoneAppManager() {
        shutdown();
    }
    
    bool PhoneAppManager::initialize() {
        return phone_integration->initialize();
    }
    
    void PhoneAppManager::shutdown() {
        phone_integration->shutdown();
    }
    
    void PhoneAppManager::alert_player(const std::string& message) {
        phone_integration->send_notification("AstraTechnica", message, 3, "game");
    }
    
    void PhoneAppManager::request_player_action(const std::string& action_description, 
                                               const std::vector<std::string>& options) {
        PushNotification notification;
        notification.title = "Action Required";
        notification.message = action_description;
        notification.priority = 4;
        notification.category = "action_required";
        notification.action_buttons = options;
        
        phone_integration->send_notification(notification);
    }
    
    void PhoneAppManager::update_game_state(const std::map<std::string, std::string>& state) {
        PushNotification notification;
        notification.title = "Game State Update";
        notification.message = "Your game state has been updated";
        notification.priority = 2;
        notification.category = "state_update";
        notification.data = state;
        
        phone_integration->send_notification(notification);
    }
    
    void PhoneAppManager::register_game_event(const std::string& event_name, std::function<void()> handler) {
        game_event_subscribers[event_name] = handler;
    }
    
    void PhoneAppManager::set_player_preferences(const std::map<std::string, std::string>& preferences) {
        // Apply player preferences to phone integration
        auto it = preferences.find("notifications_enabled");
        if (it != preferences.end()) {
            phone_integration->enable_notifications(it->second == "true");
        }
        
        it = preferences.find("security_level");
        if (it != preferences.end()) {
            int level = std::stoi(it->second);
            phone_integration->set_security_level(static_cast<SecurityLevel>(level));
        }
    }
    
} // namespace AstraTechnica