cmake_minimum_required(VERSION 3.16)
project(KardashevSuite VERSION 1.0.0 LANGUAGES CXX)

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

# Include directories
include_directories(${CMAKE_CURRENT_SOURCE_DIR})
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/../../9-The-Final-Chapter)

# Source files
set(KARDASHEV_SUITE_SOURCES
    main.cpp
    kardashev_file_types.cpp
)

# Create executable
add_executable(kardashev_suite ${KARDASHEV_SUITE_SOURCES})

# Link libraries
target_link_libraries(kardashev_suite 
    ${GTK3_LIBRARIES}
    ${OPENGL_LIBRARIES}
    pthread
    dl
)

# Include directories for targets
target_include_directories(kardashev_suite PRIVATE 
    ${GTK3_INCLUDE_DIRS}
    ${CMAKE_CURRENT_SOURCE_DIR}
)

# Compiler flags for targets
target_compile_options(kardashev_suite PRIVATE 
    ${GTK3_CFLAGS_OTHER}
)

# Install targets
install(TARGETS kardashev_suite
    RUNTIME DESTINATION bin
)

# Install configuration files
install(FILES 
    README.md
    LICENSE
    DESTINATION share/kardashev_suite
)

# Create demo files for each Kardashev level
add_custom_target(create_demo_files
    COMMAND ${CMAKE_COMMAND} -E echo "Creating Kardashev demo files..."
    COMMAND ${CMAKE_COMMAND} -E touch demo_k1_file.k1
    COMMAND ${CMAKE_COMMAND} -E touch demo_k2_file.k2
    COMMAND ${CMAKE_COMMAND} -E touch demo_k3_file.k3
    COMMAND ${CMAKE_COMMAND} -E touch demo_k4_file.k4
    COMMAND ${CMAKE_COMMAND} -E touch demo_k5_file.k5
    COMMENT "Creating demo files for all Kardashev levels"
)

# Testing
enable_testing()
add_test(NAME kardashev_suite_basic_test COMMAND kardashev_suite --test)

# Documentation
find_package(Doxygen)
if(DOXYGEN_FOUND)
    set(DOXYGEN_INPUT_DIR ${CMAKE_CURRENT_SOURCE_DIR})
    set(DOXYGEN_OUTPUT_DIR ${CMAKE_CURRENT_BINARY_DIR}/docs)
    
    configure_file(${CMAKE_CURRENT_SOURCE_DIR}/Doxyfile.in 
                   ${CMAKE_CURRENT_BINARY_DIR}/Doxyfile @ONLY)
    
    add_custom_target(docs
        ${DOXYGEN_EXECUTABLE} ${CMAKE_CURRENT_BINARY_DIR}/Doxyfile
        WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
        COMMENT "Generating API documentation with Doxygen" VERBATIM
    )
endif()

# Package configuration
set(CPACK_PACKAGE_NAME "KardashevSuite")
set(CPACK_PACKAGE_VERSION "${PROJECT_VERSION}")
set(CPACK_PACKAGE_DESCRIPTION_SUMMARY "Type V Multiversal Software Evaluation System")
set(CPACK_PACKAGE_VENDOR "SuperNinja & 9 Software")
set(CPACK_PACKAGE_CONTACT "superninja@9software.com")
set(CPACK_RESOURCE_FILE_LICENSE "${CMAKE_CURRENT_SOURCE_DIR}/LICENSE")
set(CPACK_RESOURCE_FILE_README "${CMAKE_CURRENT_SOURCE_DIR}/README.md")

include(CPack)

# Industrial deployment settings
if(INDUSTRIAL_DEPLOYMENT)
    set(CMAKE_INSTALL_PREFIX "/opt/kardashev_suite" CACHE PATH "Installation prefix for industrial deployment")
    set(CMAKE_BUILD_TYPE "RelWithDebInfo" CACHE STRING "Build type for industrial deployment")
    
    # Industrial-grade compiler optimizations
    if(NOT MSVC)
        target_compile_options(kardashev_suite PRIVATE -O3 -march=native -mtune=native)
    endif()
endif()

# Kardashev Level-specific builds
option(BUILD_K5_MULTIVERSAL "Build with Type V Multiversal capabilities" ON)
option(BUILD_K4_QUANTUM "Build with K4 Quantum readiness" ON)
option(BUILD_K3_AI "Build with K3 AI integration" ON)

if(BUILD_K5_MULTIVERSAL)
    add_compile_definitions(KARDASHEV_K5_ENABLED)
    message(STATUS "Building with K5 Multiversal capabilities")
endif()

if(BUILD_K4_QUANTUM)
    add_compile_definitions(KARDASHEV_K4_ENABLED)
    message(STATUS "Building with K4 Quantum readiness")
endif()

if(BUILD_K3_AI)
    add_compile_definitions(KARDASHEV_K3_ENABLED)
    message(STATUS "Building with K3 AI integration")
endif()

# Performance profiling
option(ENABLE_PROFILING "Enable performance profiling for industrial analysis" OFF)
if(ENABLE_PROFILING)
    add_compile_definitions(KARDASHEV_PROFILING_ENABLED)
    if(NOT MSVC)
        target_compile_options(kardashev_suite PRIVATE -pg -g)
    endif()
endif()