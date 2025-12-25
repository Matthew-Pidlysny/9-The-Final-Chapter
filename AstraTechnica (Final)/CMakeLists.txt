cmake_minimum_required(VERSION 3.16)
project(AstraTechnica VERSION 1.0.0)

# Set C++ standard
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# Build type
if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE Release)
endif()

# Compiler flags
set(CMAKE_CXX_FLAGS_DEBUG "-g -O0 -Wall -Wextra -Wpedantic")
set(CMAKE_CXX_FLAGS_RELEASE "-O3 -DNDEBUG -march=native")

# Find required packages
find_package(PkgConfig REQUIRED)
find_package(Threads REQUIRED)

# Basic dependencies - make them optional for build
find_package(OpenSSL)
find_package(CURL)

# Optional AI/ML libraries
find_package(PkgConfig QUIET)
if(PkgConfig_FOUND)
    pkg_check_modules(TORCH torch)
    pkg_check_modules(MLPACK mlpack)
    pkg_check_modules(OPENCV4 opencv4)
    pkg_check_modules(NLOHMANN_JSON nlohmann_json)
endif()

# If not found, try alternative methods
if(NOT TORCH_FOUND)
    find_package(Torch QUIET)
endif()

if(NOT MLPACK_FOUND)
    find_package(mlpack QUIET)
endif()

if(NOT OPENCV4_FOUND)
    find_package(OpenCV QUIET)
endif()

if(NOT NLOHMANN_JSON_FOUND)
    find_package(nlohmann_json QUIET)
endif()

# Include directories
include_directories(src)

# Add subdirectories
add_subdirectory(src)

# Main executable
add_executable(astratechnica src/astratechnica/main.cpp)

# Link libraries
target_link_libraries(astratechnica
    PRIVATE
    astratechnica_core_lib
    astratechnica_character_lib
    astratechnica_phone_lib
    astratechnica_ai_lib
)

# Link external libraries
if(TORCH_FOUND)
    target_link_libraries(astratechnica PRIVATE ${TORCH_LIBRARIES})
    target_include_directories(astratechnica PRIVATE ${TORCH_INCLUDE_DIRS})
endif()

if(MLPACK_FOUND)
    target_link_libraries(astratechnica PRIVATE ${MLPACK_LIBRARIES})
    target_include_directories(astratechnica PRIVATE ${MLPACK_INCLUDE_DIRS})
endif()

if(OpenCV_FOUND)
    target_link_libraries(astratechnica PRIVATE ${OpenCV_LIBS})
endif()

if(CURL_FOUND)
    target_link_libraries(astratechnica PRIVATE ${CURL_LIBRARIES})
endif()

if(OPENSSL_FOUND)
    target_link_libraries(astratechnica PRIVATE OpenSSL::SSL OpenSSL::Crypto)
endif()

if(nlohmann_json_FOUND)
    target_link_libraries(astratechnica PRIVATE nlohmann_json::nlohmann_json)
endif()

# Compiler-specific options
target_compile_features(astratechnica PRIVATE cxx_std_20)

# Add definitions
target_compile_definitions(astratechnica PRIVATE
    ASTRATECHNICA_VERSION="${PROJECT_VERSION}"
    ASTRATECHNICA_BUILD_TYPE="${CMAKE_BUILD_TYPE}"
)

# Platform-specific settings
if(WIN32)
    target_link_libraries(astratechnica PRIVATE ws2_32 crypt32)
    add_definitions(-DWIN32_LEAN_AND_MEAN)
elseif(UNIX AND NOT APPLE)
    target_link_libraries(astratechnica PRIVATE Threads::Threads)
endif()

# Installation
install(TARGETS astratechnica
    RUNTIME DESTINATION bin
    LIBRARY DESTINATION lib
    ARCHIVE DESTINATION lib
)

# Print configuration summary
message(STATUS "")
message(STATUS "=== AstraTechnica Configuration Summary ===")
message(STATUS "Version: ${PROJECT_VERSION}")
message(STATUS "Build Type: ${CMAKE_BUILD_TYPE}")
message(STATUS "C++ Standard: ${CMAKE_CXX_STANDARD}")
message(STATUS "")
message(STATUS "External Libraries:")
message(STATUS "  OpenSSL: ${OPENSSL_FOUND}")
message(STATUS "  libcurl: ${CURL_FOUND}")
message(STATUS "  PyTorch: ${TORCH_FOUND}")
message(STATUS "  mlpack: ${MLPACK_FOUND}")
message(STATUS "  OpenCV: ${OpenCV_FOUND}")
message(STATUS "  nlohmann_json: ${nlohmann_json_FOUND}")
message(STATUS "")
message(STATUS "Install Prefix: ${CMAKE_INSTALL_PREFIX}")
message(STATUS "Binary Output: ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}")
message(STATUS "==============================================")