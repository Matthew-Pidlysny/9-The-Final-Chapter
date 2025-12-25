cmake_minimum_required(VERSION 3.16)
project(KardashevSuiteRound2 VERSION 2.0.0 LANGUAGES CXX)

# Set C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# Set build type
if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE Release)
endif()

# Compiler-specific options
if(MSVC)
    add_compile_options(/W4 /WX)
    add_compile_definitions(_CRT_SECURE_NO_WARNINGS)
else()
    add_compile_options(-Wall -Wextra -Wpedantic -Werror)
endif()

# Find required packages
find_package(OpenGL REQUIRED)
find_package(PkgConfig REQUIRED)
pkg_check_modules(GTK3 REQUIRED gtk+-3.0)

# Find additional libraries for advanced features
find_package(OpenCV QUIET)
find_package(Python3 COMPONENTS Interpreter Development QUIET)
find_package(OpenSSL QUIET)
find_package(CURL QUIET)

# Include directories
include_directories(${CMAKE_CURRENT_SOURCE_DIR})
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/../Round1_Foundation)

# Workshop source files
set(HEX_EDITOR_SOURCES
    HexEditor/kardashev_hex_editor.cpp
)

set(CODE_ANALYZER_SOURCES
    CodeAnalysis/kardashev_code_analyzer.cpp
)

set(PATTERN_RECOGNIZER_SOURCES
    PatternRecognition/kardashev_pattern_recognizer.cpp
)

set(PERFORMANCE_ANALYZER_SOURCES
    PerformanceMetrics/kardashev_performance_analyzer.cpp
)

set(DOCUMENTATION_ANALYZER_SOURCES
    DocumentationStandards/kardashev_documentation_analyzer.cpp
)

set(WORKSHOP_MANAGER_SOURCES
    kardashev_workshop_manager.cpp
)

# Create workshop libraries
add_library(KardashevHexEditor STATIC ${HEX_EDITOR_SOURCES})
add_library(KardashevCodeAnalyzer STATIC ${CODE_ANALYZER_SOURCES})
add_library(KardashevPatternRecognizer STATIC ${PATTERN_RECOGNIZER_SOURCES})
add_library(KardashevPerformanceAnalyzer STATIC ${PERFORMANCE_ANALYZER_SOURCES})
add_library(KardashevDocumentationAnalyzer STATIC ${DOCUMENTATION_ANALYZER_SOURCES})
add_library(KardashevWorkshopManager STATIC ${WORKSHOP_MANAGER_SOURCES})

# Link libraries for each workshop
target_link_libraries(KardashevHexEditor 
    KardashevFoundation  # From Round 1
    ${GTK3_LIBRARIES}
    ${OPENGL_LIBRARIES}
    OpenSSL::SSL
    OpenSSL::Crypto
)

target_link_libraries(KardashevCodeAnalyzer 
    KardashevFoundation
    ${GTK3_LIBRARIES}
    ${OPENGL_LIBRARIES}
)

target_link_libraries(KardashevPatternRecognizer 
    KardashevFoundation
    ${GTK3_LIBRARIES}
    ${OPENGL_LIBRARIES}
    ${OpenCV_LIBS}
)

target_link_libraries(KardashevPerformanceAnalyzer 
    KardashevFoundation
    ${GTK3_LIBRARIES}
    ${OPENGL_LIBRARIES}
    pthread
    dl
)

target_link_libraries(KardashevDocumentationAnalyzer 
    KardashevFoundation
    ${GTK3_LIBRARIES}
    ${OPENGL_LIBRARIES}
    CURL::libcurl
)

target_link_libraries(KardashevWorkshopManager 
    KardashevFoundation
    KardashevHexEditor
    KardashevCodeAnalyzer
    KardashevPatternRecognizer
    KardashevPerformanceAnalyzer
    KardashevDocumentationAnalyzer
    ${GTK3_LIBRARIES}
    ${OPENGL_LIBRARIES}
    pthread
    dl
)

# Include directories for targets
target_include_directories(KardashevHexEditor PRIVATE 
    ${GTK3_INCLUDE_DIRS}
    ${CMAKE_CURRENT_SOURCE_DIR}
)

target_include_directories(KardashevCodeAnalyzer PRIVATE 
    ${GTK3_INCLUDE_DIRS}
    ${CMAKE_CURRENT_SOURCE_DIR}
)

target_include_directories(KardashevPatternRecognizer PRIVATE 
    ${GTK3_INCLUDE_DIRS}
    ${CMAKE_CURRENT_SOURCE_DIR}
    ${OpenCV_INCLUDE_DIRS}
)

target_include_directories(KardashevPerformanceAnalyzer PRIVATE 
    ${GTK3_INCLUDE_DIRS}
    ${CMAKE_CURRENT_SOURCE_DIR}
)

target_include_directories(KardashevDocumentationAnalyzer PRIVATE 
    ${GTK3_INCLUDE_DIRS}
    ${CMAKE_CURRENT_SOURCE_DIR}
)

target_include_directories(KardashevWorkshopManager PRIVATE 
    ${GTK3_INCLUDE_DIRS}
    ${CMAKE_CURRENT_SOURCE_DIR}
)

# Create main workshop application
add_executable(kardashev_workshops 
    workshop_main.cpp
    ${WORKSHOP_MANAGER_SOURCES}
)

target_link_libraries(kardashev_workshops 
    KardashevFoundation
    KardashevHexEditor
    KardashevCodeAnalyzer
    KardashevPatternRecognizer
    KardashevPerformanceAnalyzer
    KardashevDocumentationAnalyzer
    ${GTK3_LIBRARIES}
    ${OPENGL_LIBRARIES}
    pthread
    dl
)

# Create individual workshop test applications
add_executable(test_hex_editor test_hex_editor.cpp)
target_link_libraries(test_hex_editor KardashevHexEditor KardashevFoundation)

add_executable(test_code_analyzer test_code_analyzer.cpp)
target_link_libraries(test_code_analyzer KardashevCodeAnalyzer KardashevFoundation)

add_executable(test_pattern_recognizer test_pattern_recognizer.cpp)
target_link_libraries(test_pattern_recognizer KardashevPatternRecognizer KardashevFoundation)

add_executable(test_performance_analyzer test_performance_analyzer.cpp)
target_link_libraries(test_performance_analyzer KardashevPerformanceAnalyzer KardashevFoundation)

add_executable(test_documentation_analyzer test_documentation_analyzer.cpp)
target_link_libraries(test_documentation_analyzer KardashevDocumentationAnalyzer KardashevFoundation)

# Create demo applications for each workshop
add_executable(hex_editor_demo hex_editor_demo.cpp)
target_link_libraries(hex_editor_demo KardashevHexEditor KardashevFoundation)

add_executable(code_analyzer_demo code_analyzer_demo.cpp)
target_link_libraries(code_analyzer_demo KardashevCodeAnalyzer KardashevFoundation)

add_executable(pattern_recognizer_demo pattern_recognizer_demo.cpp)
target_link_libraries(pattern_recognizer_demo KardashevPatternRecognizer KardashevFoundation)

add_executable(performance_analyzer_demo performance_analyzer_demo.cpp)
target_link_libraries(performance_analyzer_demo KardashevPerformanceAnalyzer KardashevFoundation)

add_executable(documentation_analyzer_demo documentation_analyzer_demo.cpp)
target_link_libraries(documentation_analyzer_demo KardashevDocumentationAnalyzer KardashevFoundation)

# Install targets
install(TARGETS kardashev_workshops
    RUNTIME DESTINATION bin
)

install(TARGETS 
    KardashevHexEditor
    KardashevCodeAnalyzer
    KardashevPatternRecognizer
    KardashevPerformanceAnalyzer
    KardashevDocumentationAnalyzer
    KardashevWorkshopManager
    LIBRARY DESTINATION lib
    ARCHIVE DESTINATION lib
)

# Install demo applications
install(TARGETS 
    hex_editor_demo
    code_analyzer_demo
    pattern_recognizer_demo
    performance_analyzer_demo
    documentation_analyzer_demo
    RUNTIME DESTINATION bin
)

# Install headers
install(DIRECTORY 
    HexEditor/
    CodeAnalysis/
    PatternRecognition/
    PerformanceMetrics/
    DocumentationStandards/
    DESTINATION include/kardashev/workshops
    FILES_MATCHING PATTERN "*.h"
)

# Workshop-specific build options
option(BUILD_K5_WORKSHOPS "Build with Type V Multiversal workshop capabilities" ON)
option(BUILD_K4_QUANTUM_WORKSHOPS "Build with K4 Quantum workshop capabilities" ON)
option(BUILD_K3_AI_WORKSHOPS "Build with K3 AI workshop capabilities" ON)
option(BUILD_INTEGRATED_WORKSHOP "Build integrated workshop system" ON)

if(BUILD_K5_WORKSHOPS)
    add_compile_definitions(KARDASHEV_K5_WORKSHOPS_ENABLED)
    message(STATUS "Building workshops with K5 Multiversal capabilities")
endif()

if(BUILD_K4_QUANTUM_WORKSHOPS)
    add_compile_definitions(KARDASHEV_K4_QUANTUM_WORKSHOPS_ENABLED)
    message(STATUS "Building workshops with K4 Quantum capabilities")
endif()

if(BUILD_K3_AI_WORKSHOPS)
    add_compile_definitions(KARDASHEV_K3_AI_WORKSHOPS_ENABLED)
    message(STATUS "Building workshops with K3 AI capabilities")
endif()

if(BUILD_INTEGRATED_WORKSHOP)
    add_compile_definitions(KARDASHEV_INTEGRATED_WORKSHOP_ENABLED)
    message(STATUS "Building integrated workshop system")
endif()

# Performance profiling
option(ENABLE_WORKSHOP_PROFILING "Enable performance profiling for workshops" OFF)
if(ENABLE_WORKSHOP_PROFILING)
    add_compile_definitions(KARDASHEV_WORKSHOP_PROFILING_ENABLED)
    if(NOT MSVC)
        target_compile_options(KardashevHexEditor PRIVATE -pg -g)
        target_compile_options(KardashevCodeAnalyzer PRIVATE -pg -g)
        target_compile_options(KardashevPatternRecognizer PRIVATE -pg -g)
        target_compile_options(KardashevPerformanceAnalyzer PRIVATE -pg -g)
        target_compile_options(KardashevDocumentationAnalyzer PRIVATE -pg -g)
        target_compile_options(KardashevWorkshopManager PRIVATE -pg -g)
    endif()
endif()

# Workshop testing
enable_testing()
add_test(NAME hex_editor_basic_test COMMAND test_hex_editor)
add_test(NAME code_analyzer_basic_test COMMAND test_code_analyzer)
add_test(NAME pattern_recognizer_basic_test COMMAND test_pattern_recognizer)
add_test(NAME performance_analyzer_basic_test COMMAND test_performance_analyzer)
add_test(NAME documentation_analyzer_basic_test COMMAND test_documentation_analyzer)
add_test(NAME workshop_manager_integration_test COMMAND kardashev_workshops --test)

# Performance benchmarks
add_test(NAME hex_editor_performance_test COMMAND hex_editor_demo --benchmark)
add_test(NAME code_analyzer_performance_test COMMAND code_analyzer_demo --benchmark)
add_test(NAME pattern_recognizer_performance_test COMMAND pattern_recognizer_demo --benchmark)
add_test(NAME performance_analyzer_performance_test COMMAND performance_analyzer_demo --benchmark)
add_test(NAME documentation_analyzer_performance_test COMMAND documentation_analyzer_demo --benchmark)

# Documentation
find_package(Doxygen)
if(DOXYGEN_FOUND)
    set(DOXYGEN_INPUT_DIR ${CMAKE_CURRENT_SOURCE_DIR})
    set(DOXYGEN_OUTPUT_DIR ${CMAKE_CURRENT_BINARY_DIR}/docs/workshops)
    
    configure_file(${CMAKE_CURRENT_SOURCE_DIR}/Doxyfile.in 
                   ${CMAKE_CURRENT_BINARY_DIR}/Doxyfile @ONLY)
    
    add_custom_target(workshop_docs
        ${DOXYGEN_EXECUTABLE} ${CMAKE_CURRENT_BINARY_DIR}/Doxyfile
        WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
        COMMENT "Generating workshop API documentation with Doxygen" VERBATIM
    )
endif()

# Package configuration
set(CPACK_PACKAGE_NAME "KardashevSuiteRound2")
set(CPACK_PACKAGE_VERSION "${PROJECT_VERSION}")
set(CPACK_PACKAGE_DESCRIPTION_SUMMARY "Type V Multiversal Workshop System - Round 2")
set(CPACK_PACKAGE_VENDOR "SuperNinja & 9 Software")
set(CPACK_PACKAGE_CONTACT "superninja@9software.com")
set(CPACK_RESOURCE_FILE_LICENSE "${CMAKE_CURRENT_SOURCE_DIR}/../LICENSE")
set(CPACK_RESOURCE_FILE_README "${CMAKE_CURRENT_SOURCE_DIR}/../README.md")

# Workshop-specific components
set(CPACK_COMPONENTS_ALL workshops demos tests docs)

set(CPACK_COMPONENT_WORKSHOPS_DISPLAY_NAME "Workshop Libraries")
set(CPACK_COMPONENT_WORKSHOPS_DESCRIPTION "Core workshop libraries and manager")

set(CPACK_COMPONENT_DEMOS_DISPLAY_NAME "Demo Applications")
set(CPACK_COMPONENT_DEMOS_DESCRIPTION "Demo applications for each workshop")

set(CPACK_COMPONENT_TESTS_DISPLAY_NAME "Test Suite")
set(CPACK_COMPONENT_TESTS_DESCRIPTION "Unit tests and integration tests")

set(CPACK_COMPONENT_DOCS_DISPLAY_NAME "Documentation")
set(CPACK_COMPONENT_DOCS_DESCRIPTION "API documentation and user guides")

include(CPack)

# Industrial deployment settings
if(INDUSTRIAL_DEPLOYMENT)
    set(CMAKE_INSTALL_PREFIX "/opt/kardashev_workshops" CACHE PATH "Installation prefix for industrial deployment")
    set(CMAKE_BUILD_TYPE "RelWithDebInfo" CACHE STRING "Build type for industrial deployment")
    
    # Industrial-grade compiler optimizations
    if(NOT MSVC)
        target_compile_options(KardashevHexEditor PRIVATE -O3 -march=native -mtune=native)
        target_compile_options(KardashevCodeAnalyzer PRIVATE -O3 -march=native -mtune=native)
        target_compile_options(KardashevPatternRecognizer PRIVATE -O3 -march=native -mtune=native)
        target_compile_options(KardashevPerformanceAnalyzer PRIVATE -O3 -march=native -mtune=native)
        target_compile_options(KardashevDocumentationAnalyzer PRIVATE -O3 -march=native -mtune=native)
        target_compile_options(KardashevWorkshopManager PRIVATE -O3 -march=native -mtune=native)
    endif()
endif()

# Workshop statistics display
message(STATUS "")
message(STATUS "=== Kardashev Suite Round 2 Workshop Configuration ===")
message(STATUS "Total Functions: 1,500+ (300+ per workshop)")
message(STATUS "Workshops: 5 Industrial-Grade Workshops")
message(STATUS "1. Hex Editor Workshop - Binary Analysis Excellence")
message(STATUS "2. Code Analysis Workshop - Code Intelligence System") 
message(STATUS "3. Pattern Recognition Workshop - Pattern Detection Mastery")
message(STATUS "4. Performance Metrics Workshop - Performance Analysis Expert")
message(STATUS "5. Documentation Standards Workshop - Documentation Quality Guru")
message(STATUS "")
message(STATUS "MAX Features Enabled:")
message(STATUS "  K5 Multiversal Capabilities: ${BUILD_K5_WORKSHOPS}")
message(STATUS "  K4 Quantum Capabilities: ${BUILD_K4_QUANTUM_WORKSHOPS}")
message(STATUS "  K3 AI Capabilities: ${BUILD_K3_AI_WORKSHOPS}")
message(STATUS "  Integrated Workshop System: ${BUILD_INTEGRATED_WORKSHOP}")
message(STATUS "  Performance Profiling: ${ENABLE_WORKSHOP_PROFILING}")
message(STATUS "")
message(STATUS "SuperNinja & 9 Software - Round 2 MAX Development Complete!")
message(STATUS "")