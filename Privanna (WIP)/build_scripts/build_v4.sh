#!/bin/bash

echo "Building Privanna Engine Version 4..."

# Create build directory
mkdir -p build_v4
cd build_v4

# Compile all source files
g++ -std=c++17 -O2 -Wall -Wextra \
    -I../src \
    ../src/core/privanna_engine_v4.cpp \
    ../src/character/character_system.cpp \
    ../src/faction/faction_relationship_system.cpp \
    ../src/combat/combat_system.cpp \
    ../src/systems/event_system.cpp \
    ../src/systems/memory_manager.cpp \
    ../src/systems/threading_system.cpp \
    ../src/utils/logger.cpp \
    ../src/utils/math_utils.cpp \
    -o privanna_v4_demo \
    -lpthread

if [ $? -eq 0 ]; then
    echo "Build successful! Executable: build_v4/privanna_v4_demo"
    echo "Run with: ./build_v4/privanna_v4_demo"
else
    echo "Build failed!"
    exit 1
fi