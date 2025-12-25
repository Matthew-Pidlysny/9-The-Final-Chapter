cmake_minimum_required(VERSION 3.20)
project(PrivannaEngineV1 VERSION 1.0.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(Threads REQUIRED)

include_directories(${CMAKE_CURRENT_SOURCE_DIR}/../src ${CMAKE_CURRENT_SOURCE_DIR}/..)

add_executable(privanna_engine_v1
    ../src/core/privanna_engine_minimal.cpp
)

target_link_libraries(privanna_engine_v1 ${CMAKE_THREAD_LIBS_INIT})

message(STATUS "Privanna Engine V1 - Minimal Build Ready")