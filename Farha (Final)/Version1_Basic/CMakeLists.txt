cmake_minimum_required(VERSION 3.10)
project(FarhaGame VERSION 1.0.0 LANGUAGES CXX)

# Set C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Compiler flags for optimization
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wextra")
set(CMAKE_CXX_FLAGS_RELEASE "-O3 -DNDEBUG")

# Define source files
set(SOURCES
    main.cpp
    farha_game.cpp
)

# Define header files
set(HEADERS
    farha_game.hpp
)

# Create executable
add_executable(farha_game ${SOURCES} ${HEADERS})

# Set output directory
set_target_properties(farha_game PROPERTIES
    RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin
)

# Installation
install(TARGETS farha_game
    RUNTIME DESTINATION bin
    COMPONENT applications
)

# Custom target for clean
add_custom_target(clean-all
    COMMAND ${CMAKE_BUILD_TOOL} clean
    COMMAND ${CMAKE_COMMAND} -E remove_directory ${CMAKE_BINARY_DIR}/bin
    COMMENT "Cleaning all build files"
)

# Print build information
message(STATUS "Building Farha Educational Game v${PROJECT_VERSION}")
message(STATUS "C++ Standard: ${CMAKE_CXX_STANDARD}")
message(STATUS "Build Type: ${CMAKE_BUILD_TYPE}")