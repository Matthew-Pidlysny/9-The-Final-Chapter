cmake_minimum_required(VERSION 3.10)
project(FarhaAllahInspired)

# Set C++ standard
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Bismillah ir-Rahman ir-Raheem
# CMake configuration for Farha Version 3: Allah Blessed Educational Experience

# Source files
set(SOURCES
    farha_allah_inspired.cpp
    main.cpp
)

# Header files
set(HEADERS
    farha_allah_inspired.hpp
)

# Create executable
add_executable(farha_v3 ${SOURCES} ${HEADERS})

# Compiler flags for Islamic educational content
target_compile_options(farha_v3 PRIVATE
    -Wall
    -Wextra
    -std=c++11
)

# Include directories
target_include_directories(farha_v3 PRIVATE ${CMAKE_CURRENT_SOURCE_DIR})

# Post-build message for the glory of Allah
add_custom_command(TARGET farha_v3 POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E echo ""
    COMMAND ${CMAKE_COMMAND} -E echo "Alhamdulillah! Farha Version 3 compiled successfully!"
    COMMAND ${CMAKE_COMMAND} -E echo "Bismillah ir-Rahman ir-Raheem - Ready for Islamic education!"
    COMMAND ${CMAKE_COMMAND} -E echo "May Allah bless this educational effort!"
    COMMAND ${CMAKE_COMMAND} -E echo ""
)

# Install target
install(TARGETS farha_v3 DESTINATION bin)

# Islamic educational documentation
configure_file(
    "${CMAKE_CURRENT_SOURCE_DIR}/README.md"
    "${CMAKE_CURRENT_BINARY_DIR}/README.md"
    COPYONLY
)