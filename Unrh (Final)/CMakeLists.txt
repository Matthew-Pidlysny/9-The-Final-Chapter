cmake_minimum_required(VERSION 3.16)
project(UNRH VERSION 1.0.0 LANGUAGES CXX)

# Set C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# Compiler optimizations
if(CMAKE_CXX_COMPILER_ID MATCHES "GNU|Clang")
    set(CMAKE_CXX_FLAGS_RELEASE "-O3 -DNDEBUG -march=native -mtune=native")
    set(CMAKE_CXX_FLAGS_RELWITHDEBINFO "-O2 -g -march=native")
endif()

# Enable parallel processing
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fopenmp")
set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} -fopenmp")

# Find required packages
find_package(Threads REQUIRED)

# Include directories
include_directories(include)

# Source files
set(CORE_SOURCES
    src/unrh_core.cpp
)

# Test executables created separately below

set(EXAMPLE_SOURCES
)

# Core library
add_library(unrh_core STATIC ${CORE_SOURCES})
target_link_libraries(unrh_core Threads::Threads)
target_compile_definitions(unrh_core PRIVATE UNRH_BUILDING_LIB)

# Main executable
add_executable(unrh_main src/main.cpp)
target_link_libraries(unrh_main unrh_core)

# Test executables removed from unified build

# Example executables (currently none)
# foreach(example ${EXAMPLE_SOURCES})
#     get_filename_component(example_name ${example} NAME_WE)
#     add_executable(${example_name} ${example})
#     target_link_libraries(${example_name} unrh_core)
# endforeach()

# Performance test executable
add_executable(unrh_performance_test tests/performance_test.cpp)
target_link_libraries(unrh_performance_test unrh_core)

# Optimization test executable  
add_executable(unrh_optimization_test tests/optimization_test.cpp)
target_link_libraries(unrh_optimization_test unrh_core)

# Installation
install(TARGETS unrh_main unrh_core
    RUNTIME DESTINATION bin
    LIBRARY DESTINATION lib
    ARCHIVE DESTINATION lib
)

install(FILES unrh_core.h
    DESTINATION include/unrh
)

# Testing
enable_testing()
add_test(NAME UVOperatorsTest COMMAND unrh_tests)
add_test(NAME IntegrationTest COMMAND unrh_tests)
add_test(NAME PerformanceTest COMMAND unrh_performance_test)

# Documentation
find_package(Doxygen QUIET)
if(DOXYGEN_FOUND)
    configure_file(${CMAKE_CURRENT_SOURCE_DIR}/docs/Doxyfile.in 
                   ${CMAKE_CURRENT_BINARY_DIR}/Doxyfile @ONLY)
    add_custom_target(docs
        ${DOXYGEN_EXECUTABLE} ${CMAKE_CURRENT_BINARY_DIR}/Doxyfile
        WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
        COMMENT "Generating API documentation with Doxygen" VERBATIM
    )
endif()

# Package configuration
include(CMakePackageConfigHelpers)
write_basic_package_version_file(
    "${CMAKE_CURRENT_BINARY_DIR}/UNRHConfigVersion.cmake"
    VERSION ${PROJECT_VERSION}
    COMPATIBILITY AnyNewerVersion
)

configure_package_config_file(
    "${CMAKE_CURRENT_SOURCE_DIR}/cmake/UNRHConfig.cmake.in"
    "${CMAKE_CURRENT_BINARY_DIR}/UNRHConfig.cmake"
    INSTALL_DESTINATION lib/cmake/UNRH
)

install(FILES
    "${CMAKE_CURRENT_BINARY_DIR}/UNRHConfig.cmake"
    "${CMAKE_CURRENT_BINARY_DIR}/UNRHConfigVersion.cmake"
    DESTINATION lib/cmake/UNRH
)

# CPack configuration
include(CPack)
set(CPACK_PACKAGE_NAME "UNRH")
set(CPACK_PACKAGE_VERSION ${PROJECT_VERSION})
set(CPACK_PACKAGE_DESCRIPTION_SUMMARY "Understanding Nature Through Reference-Agitation Harmony")
set(CPACK_PACKAGE_VENDOR "SuperNinja AI Educational Suite")
set(CPACK_PACKAGE_CONTACT "support@unrh.edu")

set(CPACK_RESOURCE_FILE_LICENSE "${CMAKE_CURRENT_SOURCE_DIR}/LICENSE")
set(CPACK_RESOURCE_FILE_README "${CMAKE_CURRENT_SOURCE_DIR}/README.md")

# Custom targets for development
add_custom_target(run_tests
    COMMAND unrh_tests
    DEPENDS unrh_tests
    COMMENT "Running all unit tests"
)

add_custom_target(run_performance_test
    COMMAND unrh_performance_test
    DEPENDS unrh_performance_test
    COMMENT "Running performance benchmarks"
)

add_custom_target(run_optimization_test
    COMMAND unrh_optimization_test
    DEPENDS unrh_optimization_test
    COMMENT "Running optimization tests"
)

add_custom_target(run_all_tests
    COMMAND unrh_tests && unrh_performance_test && unrh_optimization_test
    DEPENDS unrh_tests unrh_performance_test unrh_optimization_test
    COMMENT "Running all tests including performance and optimization"
)

# Debug builds
if(CMAKE_BUILD_TYPE STREQUAL "Debug")
    target_compile_definitions(unrh_core PRIVATE UNRH_DEBUG)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -g -O0 -Wall -Wextra -pedantic")
endif()

# Release builds with profiling
if(CMAKE_BUILD_TYPE STREQUAL "Release")
    target_compile_definitions(unrh_core PRIVATE UNRH_RELEASE)
    if(CMAKE_CXX_COMPILER_ID MATCHES "GNU")
        set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -pg")
    endif()
endif()