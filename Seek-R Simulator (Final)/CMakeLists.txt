# SEEK-R: Kardashev First Person Simulator
# =======================================
# Type V Multiversal Civilization Reality Engine
# 38 Wisdom Wheels • Infinite Paths • VR • Quantum Rendering

cmake_minimum_required(VERSION 3.16)
project(SeekR VERSION 1.0.0 LANGUAGES CXX)

# Set C++ standard for quantum computing capabilities
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# Build configuration
set(CMAKE_BUILD_TYPE Release)
set(CMAKE_CXX_FLAGS_RELEASE "-O3 -DNDEBUG -march=native -mtune=native -ffast-math")

# Compiler flags for maximum performance
if(CMAKE_CXX_COMPILER_ID MATCHES "GNU|Clang")
    add_compile_options(-Wall -Wextra -Wpedantic)
    add_compile_options(-fno-omit-frame-pointer)
    add_compile_options(-mavx2 -mfma) # Enable AVX2 for quantum calculations
endif()

# Find required packages
find_package(OpenGL REQUIRED)
find_package(PkgConfig REQUIRED)
pkg_check_modules(GLFW REQUIRED glfw3)
find_package(GLEW REQUIRED)
find_package(Vulkan REQUIRED)
find_package(Threads REQUIRED)

# Find Python for Stargazer integration
find_package(Python3 COMPONENTS Interpreter Development REQUIRED)

# Include directories
include_directories(${CMAKE_CURRENT_SOURCE_DIR})
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/seek_r_engine)
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/../)
include_directories(${Python3_INCLUDE_DIRS})

# Stargazer Python modules (from parent directory)
set(STARGAZER_SOURCES
    ../stargazer_main.py
    ../stargazer_3d_processor.py
    ../stargazer_brush_analyzer.py
    ../stargazer_shape_transformer.py
    ../stargazer_test_suite.py
    ../wisdom_wheels_document.txt
)

# Seek-R Engine sources
set(SEEKR_ENGINE_SOURCES
    seek_r_engine/kardashev_quantum_renderer.cpp
    seek_r_engine/kardashev_quantum_renderer.hpp
    seek_r_engine/wisdom_wheels_transformer.cpp
    seek_r_engine/wisdom_wheels_transformer.hpp
)

# Main application source
set(SEEKR_MAIN_SOURCE
    seek_r_main.cpp
)

# Create Seek-R Engine library
add_library(seek_r_engine STATIC ${SEEKR_ENGINE_SOURCES})

# Set properties for Seek-R Engine
set_target_properties(seek_r_engine PROPERTIES
    VERSION ${PROJECT_VERSION}
    SOVERSION ${PROJECT_VERSION_MAJOR}
    CXX_STANDARD 20
    CXX_STANDARD_REQUIRED ON
)

# Link libraries for Seek-R Engine
target_link_libraries(seek_r_engine 
    ${OPENGL_LIBRARIES}
    ${GLFW_LIBRARIES}
    GLEW::GLEW
    Vulkan::Vulkan
    Threads::Threads
    ${Python3_LIBRARIES}
    -ldl # Python dynamic linking
)

target_include_directories(seek_r_engine PRIVATE ${GLFW_INCLUDE_DIRS})
target_include_directories(seek_r_engine PRIVATE ${Python3_INCLUDE_DIRS})

# Create Seek-R executable
add_executable(seek_r ${SEEKR_MAIN_SOURCE})

# Link Seek-R executable with engine
target_link_libraries(seek_r 
    seek_r_engine
    ${OPENGL_LIBRARIES}
    ${GLFW_LIBRARIES}
    GLEW::GLEW
    Vulkan::Vulkan
    Threads::Threads
    ${Python3_LIBRARIES}
    -ldl # Python dynamic linking
)

target_include_directories(seek_r PRIVATE ${GLFW_INCLUDE_DIRS})
target_include_directories(seek_r PRIVATE ${Python3_INCLUDE_DIRS})

# Set properties for Seek-R executable
set_target_properties(seek_r PROPERTIES
    CXX_STANDARD 20
    CXX_STANDARD_REQUIRED ON
    RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}
)

# Copy Stargazer files to build directory
file(COPY ${STARGAZER_SOURCES} DESTINATION ${CMAKE_BINARY_DIR}/stargazer)

# Installation rules
install(TARGETS seek_r
    RUNTIME DESTINATION bin
    LIBRARY DESTINATION lib
    ARCHIVE DESTINATION lib
)

install(FILES ${STARGAZER_SOURCES}
    DESTINATION share/seek_r/stargazer
)

# Testing
enable_testing()

# Add unit tests for Seek-R components
add_executable(seek_r_tests
    tests/test_quantum_renderer.cpp
    tests/test_wisdom_wheels.cpp
    tests/test_vr_integration.cpp
)

target_link_libraries(seek_r_tests 
    seek_r_engine
    ${OPENGL_LIBRARIES}
    ${GLFW_LIBRARIES}
    GLEW::GLEW
    Vulkan::Vulkan
    Threads::Threads
)

add_test(NAME SeekRUnitTests COMMAND seek_r_tests)

# Performance benchmarks
add_executable(seek_r_benchmark
    benchmark/benchmark_main.cpp
    benchmark/benchmark_quantum.cpp
    benchmark/benchmark_vr.cpp
)

target_link_libraries(seek_r_benchmark 
    seek_r_engine
    ${OPENGL_LIBRARIES}
    ${GLFW_LIBRARIES}
    GLEW::GLEW
    Vulkan::Vulkan
    Threads::Threads
)

# Custom targets for development
add_custom_target(run_seek_r
    COMMAND seek_r
    WORKING_DIRECTORY ${CMAKE_BINARY_DIR}
    DEPENDS seek_r
    COMMENT "Running Seek-R First Person Simulator"
)

add_custom_target(test_seek_r
    COMMAND ctest --output-on-failure
    WORKING_DIRECTORY ${CMAKE_BINARY_DIR}
    DEPENDS seek_r_tests
    COMMENT "Running Seek-R unit tests"
)

# Package configuration
include(CPack)
set(CPACK_PACKAGE_NAME "SeekR")
set(CPACK_PACKAGE_VERSION ${PROJECT_VERSION})
set(CPACK_PACKAGE_DESCRIPTION_SUMMARY "Kardashev First Person Reality Simulator")
set(CPACK_PACKAGE_VENDOR "SuperNinja AI Research Division")

# Print configuration summary
message(STATUS "")
message(STATUS "Seek-R Configuration Summary:")
message(STATUS "  Version: ${PROJECT_VERSION}")
message(STATUS "  Build Type: ${CMAKE_BUILD_TYPE}")
message(STATUS "  C++ Standard: ${CMAKE_CXX_STANDARD}")
message(STATUS "  Install Prefix: ${CMAKE_INSTALL_PREFIX}")
message(STATUS "")
message(STATUS "Dependencies Found:")
message(STATUS "  OpenGL: ${OPENGL_FOUND}")
message(STATUS "  GLFW3: ${GLFW_FOUND}")
message(STATUS "  GLEW: ${GLEW_FOUND}")
message(STATUS "  Vulkan: ${Vulkan_FOUND}")
message(STATUS "  Python3: ${Python3_FOUND}")
message(STATUS "")
message(STATUS "Build Targets:")
message(STATUS "  seek_r           - Main executable")
message(STATUS "  seek_r_engine    - Engine library")
message(STATUS "  seek_r_tests     - Unit tests")
message(STATUS "  seek_r_benchmark - Performance benchmarks")
message(STATUS "")