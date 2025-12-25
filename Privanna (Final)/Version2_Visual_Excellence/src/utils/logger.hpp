/*
 * Logger System - High Performance Logging
 */

#ifndef LOGGER_HPP
#define LOGGER_HPP

#include <string>
#include <fstream>
#include <mutex>
#include <atomic>

namespace privanna::logger {

enum class Level {
    DEBUG = 0,
    INFO = 1,
    WARN = 2,
    ERROR = 3
};

class Logger {
private:
    static std::atomic<Level> min_level_;
    static std::mutex log_mutex_;
    static std::ofstream log_file_;
    
public:
    static void initialize(const std::string& filename, Level min_level = Level::INFO);
    static void shutdown();
    
    template<typename... Args>
    static void debug(const std::string& format, Args... args);
    
    template<typename... Args>
    static void info(const std::string& format, Args... args);
    
    template<typename... Args>
    static void warn(const std::string& format, Args... args);
    
    template<typename... Args>
    static void error(const std::string& format, Args... args);
    
private:
    static void log(Level level, const std::string& message);
    static std::string format_message(const std::string& format);
    
    template<typename T, typename... Args>
    static std::string format_message(const std::string& format, T value, Args... args);
};

// Template implementations
template<typename... Args>
void Logger::debug(const std::string& format, Args... args) {
    if (min_level_.load() <= Level::DEBUG) {
        log(Level::DEBUG, format_message(format, args...));
    }
}

template<typename... Args>
void Logger::info(const std::string& format, Args... args) {
    if (min_level_.load() <= Level::INFO) {
        log(Level::INFO, format_message(format, args...));
    }
}

template<typename... Args>
void Logger::warn(const std::string& format, Args... args) {
    if (min_level_.load() <= Level::WARN) {
        log(Level::WARN, format_message(format, args...));
    }
}

template<typename... Args>
void Logger::error(const std::string& format, Args... args) {
    if (min_level_.load() <= Level::ERROR) {
        log(Level::ERROR, format_message(format, args...));
    }
}

template<typename T, typename... Args>
std::string Logger::format_message(const std::string& format, T value, Args... args) {
    size_t pos = format.find("{}");
    if (pos == std::string::npos) return format;
    
    std::ostringstream oss;
    oss << value;
    return format_message(format.substr(0, pos) + oss.str() + format.substr(pos + 2), args...);
}

} // namespace privanna::logger

// Convenience macros
#define LOG_DEBUG(...) ::privanna::logger::Logger::debug(__VA_ARGS__)
#define LOG_INFO(...) ::privanna::logger::Logger::info(__VA_ARGS__)
#define LOG_WARN(...) ::privanna::logger::Logger::warn(__VA_ARGS__)
#define LOG_ERROR(...) ::privanna::logger::Logger::error(__VA_ARGS__)

#endif // LOGGER_HPP