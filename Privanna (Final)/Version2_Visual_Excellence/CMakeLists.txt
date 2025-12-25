cmake_minimum_required(VERSION 3.20)
project(PrivannaEngineV2 VERSION 2.0.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(Threads REQUIRED)

include_directories(${CMAKE_CURRENT_SOURCE_DIR}/../src ${CMAKE_CURRENT_SOURCE_DIR}/..)

add_executable(privanna_engine_v2
    ../src/core/privanna_engine_v2_demo.cpp
)

target_link_libraries(privanna_engine_v2 ${CMAKE_THREAD_LIBS_INIT})

message(STATUS "Privanna Engine V2 - Visual Excellence Build Ready")