/*
 * Logger.cpp - Simple Logging Implementation
 */

#include "utils/Logger.h"
#include <chrono>
#include <iomanip>
#include <sstream>

// Static member definitions
std::ofstream Logger::s_logFile;
std::mutex Logger::s_mutex;
LogLevel Logger::s_currentLevel = LogLevel::INFO;
bool Logger::s_initialized = false;

void Logger::initialize(const std::string& filename) {
    std::lock_guard<std::mutex> lock(s_mutex);
    
    if (!s_initialized) {
        s_logFile.open(filename, std::ios::out | std::ios::app);
        s_initialized = true;
        info("Logger initialized");
    }
}

void Logger::setLevel(LogLevel level) {
    std::lock_guard<std::mutex> lock(s_mutex);
    s_currentLevel = level;
}

void Logger::debug(const std::string& message) {
    log(LogLevel::DEBUG, message);
}

void Logger::info(const std::string& message) {
    log(LogLevel::INFO, message);
}

void Logger::warning(const std::string& message) {
    log(LogLevel::WARNING, message);
}

void Logger::error(const std::string& message) {
    log(LogLevel::ERROR, message);
}

void Logger::shutdown() {
    std::lock_guard<std::mutex> lock(s_mutex);
    
    if (s_initialized) {
        info("Logger shutting down");
        s_logFile.close();
        s_initialized = false;
    }
}

void Logger::log(LogLevel level, const std::string& message) {
    if (level < s_currentLevel) {
        return;
    }
    
    std::lock_guard<std::mutex> lock(s_mutex);
    
    std::string timestamp = getCurrentTimestamp();
    std::string levelStr = levelToString(level);
    
    // Log to console
    std::cout << "[" << timestamp << "] [" << levelStr << "] " << message << std::endl;
    
    // Log to file if initialized
    if (s_initialized && s_logFile.is_open()) {
        s_logFile << "[" << timestamp << "] [" << levelStr << "] " << message << std::endl;
        s_logFile.flush();
    }
}

std::string Logger::levelToString(LogLevel level) {
    switch (level) {
        case LogLevel::DEBUG: return "DEBUG";
        case LogLevel::INFO: return "INFO";
        case LogLevel::WARNING: return "WARNING";
        case LogLevel::ERROR: return "ERROR";
        default: return "UNKNOWN";
    }
}

std::string Logger::getCurrentTimestamp() {
    auto now = std::chrono::system_clock::now();
    auto time_t = std::chrono::system_clock::to_time_t(now);
    auto ms = std::chrono::duration_cast<std::chrono::milliseconds>(
        now.time_since_epoch()) % 1000;
    
    std::stringstream ss;
    ss << std::put_time(std::localtime(&time_t), "%Y-%m-%d %H:%M:%S");
    ss << '.' << std::setfill('0') << std::setw(3) << ms.count();
    
    return ss.str();
}