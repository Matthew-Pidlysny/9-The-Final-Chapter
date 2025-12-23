/*
 * Logger.h - Simple Logging Utility
 */

#ifndef LOGGER_H
#define LOGGER_H

#include <string>
#include <fstream>
#include <mutex>
#include <iostream>

enum class LogLevel {
    DEBUG,
    INFO,
    WARNING,
    ERROR
};

class Logger {
public:
    static void initialize(const std::string& filename = "plane_pilot.log");
    static void setLevel(LogLevel level);
    static void debug(const std::string& message);
    static void info(const std::string& message);
    static void warning(const std::string& message);
    static void error(const std::string& message);
    static void shutdown();

private:
    static std::ofstream s_logFile;
    static std::mutex s_mutex;
    static LogLevel s_currentLevel;
    static bool s_initialized;
    
    static void log(LogLevel level, const std::string& message);
    static std::string levelToString(LogLevel level);
    static std::string getCurrentTimestamp();
};

#endif // LOGGER_H