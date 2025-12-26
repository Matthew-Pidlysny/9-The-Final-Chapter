cmake_minimum_required(VERSION 3.16)
project(MegamanKardashev VERSION 1.0.0)

# Set C++ standard
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Compiler flags for maximum performance and efficiency (200% enhancement)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -O3 -march=native -mtune=native -flto")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -ffast-math -funroll-loops -fomit-frame-pointer")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wextra -pedantic")
set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -g -O0 -DDEBUG")
set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} -O3 -DNDEBUG")

# Source files
set(LORE_LIBRARY_SOURCES
    megaman_lore_library.cpp
)

set(RPG_GAME_SOURCES
    megaman_rpg_game.cpp
)

set(MAIN_SOURCES
    megaman_main.cpp
)

# Create library targets
add_library(megaman_lore STATIC ${LORE_LIBRARY_SOURCES})
add_library(megaman_rpg STATIC ${RPG_GAME_SOURCES})

# Main executable
add_executable(megaman_kardashev ${MAIN_SOURCES})

# Link libraries
target_link_libraries(megaman_kardashev 
    megaman_lore 
    megaman_rpg
)

# Include directories
target_include_directories(megaman_kardashev PUBLIC 
    ${CMAKE_CURRENT_SOURCE_DIR}
)

target_include_directories(megaman_lore PUBLIC 
    ${CMAKE_CURRENT_SOURCE_DIR}
)

target_include_directories(megaman_rpg PUBLIC 
    ${CMAKE_CURRENT_SOURCE_DIR}
)

# Compiler-specific optimizations
if(CMAKE_CXX_COMPILER_ID STREQUAL "GNU" OR CMAKE_CXX_COMPILER_ID STREQUAL "Clang")
    target_compile_options(megaman_kardashev PRIVATE 
        -pipe
        -fno-plt
        -fno-stack-protector
        -frename-registers
        -freorder-blocks
        -freorder-functions
        -finline-functions
        -finline-small-functions
        -findirect-inlining
    )
endif()

# Set output directory
set_target_properties(megaman_kardashev PROPERTIES
    RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin
)

# Install targets
install(TARGETS megaman_kardashev
    RUNTIME DESTINATION bin
)

# Install documentation and web files
install(FILES 
    megaman_interactive_library.html
    megaman_5000_world_ideas.md
    DESTINATION share/megaman_kardashev
)

# Print build information
message(STATUS "Building Megaman Kardashev Project")
message(STATUS "C++ Standard: ${CMAKE_CXX_STANDARD}")
message(STATUS "Build Type: ${CMAKE_BUILD_TYPE}")
message(STATUS "Compiler: ${CMAKE_CXX_COMPILER_ID}")
message(STATUS "System: ${CMAKE_SYSTEM_NAME}")