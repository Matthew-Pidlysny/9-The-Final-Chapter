# Privanna Game Engine - CMake Configuration
# Massive Scale C++ Project Targeting 15,000+ Commits
# C++17/20 Standard with Modern Toolchain

cmake_minimum_required(VERSION 3.20)
project(PrivannaEngine VERSION 1.0.0 LANGUAGES CXX)

# Set C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# Build configuration
set(CMAKE_BUILD_TYPE Release)
set(CMAKE_CXX_FLAGS_RELEASE "-O3 -DNDEBUG -march=native")
set(CMAKE_CXX_FLAGS_DEBUG "-O0 -g -DDEBUG")

# Compiler-specific options
if(MSVC)
    add_compile_options(/W4 /permissive-)
    add_compile_definitions(_CRT_SECURE_NO_WARNINGS)
else()
    add_compile_options(-Wall -Wextra -Wpedantic)
    add_compile_options(-march=native)
endif()

# Find required packages
find_package(Threads REQUIRED)
find_package(PkgConfig REQUIRED)

# Core dependencies only for Version 1 (Efficiency Focus)
# Find basic system libraries
find_package(Threads REQUIRED)

# Optional dependencies will be added in later versions

# Include directories
include_directories(
    ${CMAKE_CURRENT_SOURCE_DIR}/src
    ${CMAKE_CURRENT_SOURCE_DIR}/include
    ${CMAKE_CURRENT_SOURCE_DIR}/third_party
)

# Source file organization - Version 1 (Efficiency Focus)
set(CORE_SOURCES
    src/core/privanna_engine.cpp
)

set(GAME_SOURCES
)

set(AI_SOURCES
)

set(RENDER_SOURCES
)

set(AUDIO_SOURCES
    src/audio/audio_core.cpp
    src/audio/music_system.cpp
    src/audio/sfx_system.cpp
    src/audio/voice_system.cpp
)

set(NETWORK_SOURCES
    src/network/network_core.cpp
    src/network/server_manager.cpp
    src/network/client_sync.cpp
    src/network/multiplayer_logic.cpp
    src/network/social_system.cpp
    src/network/anti_cheat.cpp
)

set(DATA_SOURCES
    src/data/database_system.cpp
    src/data/serialization.cpp
    src/data/compression_system.cpp
    src/data/localization.cpp
)

set(TOOLING_SOURCES
    src/tools/map_editor.cpp
    src/tools/faction_editor.cpp
    src/tools/scenario_editor.cpp
    src/tools/ai_editor.cpp
    src/tools/particle_editor.cpp
    src/tools/script_editor.cpp
)

set(UTILS_SOURCES
    src/utils/logger.cpp
    src/utils/file_utils.cpp
    src/utils/math_utils.cpp
    src/utils/string_utils.cpp
    src/utils/profiler.cpp
)

# Divine data block (faith-based system)
set(DIVINE_SOURCES
    src/core/divine_data_block.cpp
)

# Collect all sources
set(ALL_SOURCES
    ${CORE_SOURCES}
    ${GAME_SOURCES}
    ${AI_SOURCES}
    ${RENDER_SOURCES}
    ${AUDIO_SOURCES}
    ${NETWORK_SOURCES}
    ${DATA_SOURCES}
    ${TOOLING_SOURCES}
    ${UTILS_SOURCES}
    ${DIVINE_SOURCES}
)

# Create main executable
add_executable(privanna_engine
    src/main.cpp
    ${ALL_SOURCES}
)

# Link libraries for main executable
target_link_libraries(privanna_engine
    # Core libraries
    Threads::Threads
    
    # PyTorch
    ${TORCH_LIBRARIES}
    
    # OpenCV
    ${OpenCV_LIBS}
    
    # Graphics
    OpenGL::GL
    glfw
    glad
    ${SDL2_LIBRARIES}
    
    # Audio
    ${OPENAL_LIBRARY}
    ${VORBIS_LIBRARIES}
    ${OGG_LIBRARIES}
    
    # Networking
    Boost::system
    Boost::thread
    Boost::filesystem
    
    # Optional Vulkan
    $<IF:$<TARGET_EXISTS:Vulkan::Vulkan>,Vulkan::Vulkan>
    
    # System libraries
    ${CMAKE_DL_LIBS}
)

# Set properties for PyTorch
set_property(TARGET privanna_engine PROPERTY CXX_STANDARD 17)
if(MSVC)
    set_property(TARGET privanna_engine PROPERTY MSVC_RUNTIME_TYPE "MultiThreadedDLL")
endif()

# Compiler-specific definitions for PyTorch
if(CMAKE_SYSTEM_NAME STREQUAL "Windows")
    target_compile_definitions(privanna_engine PRIVATE TORCH_API=__declspec(dllimport))
endif()

# Create static library for core engine
add_library(privanna_core STATIC ${CORE_SOURCES} ${DIVINE_SOURCES})
target_link_libraries(privanna_core Threads::Threads ${TORCH_LIBRARIES})

# Create AI library
add_library(privanna_ai STATIC ${AI_SOURCES})
target_link_libraries(privanna_ai ${TORCH_LIBRARIES} ${OpenCV_LIBS})

# Create game logic library
add_library(privanna_game STATIC ${GAME_SOURCES})
target_link_libraries(privanna_game privanna_core)

# Create renderer library
add_library(privanna_render STATIC ${RENDER_SOURCES})
target_link_libraries(privanna_render OpenGL::GL glfw glad)

# Create audio library
add_library(privanna_audio STATIC ${AUDIO_SOURCES})
target_link_libraries(privanna_audio ${OPENAL_LIBRARY} ${VORBIS_LIBRARIES} ${OGG_LIBRARIES})

# Create network library
add_library(privanna_network STATIC ${NETWORK_SOURCES})
target_link_libraries(privanna_network Boost::system Boost::thread Boost::filesystem)

# Module tests
enable_testing()

# Add unit tests for each module
add_subdirectory(tests)

# Benchmark tests
add_subdirectory(benchmarks)

# Documentation
find_package(Doxygen QUIET)
if(DOXYGEN_FOUND)
    configure_file(${CMAKE_CURRENT_SOURCE_DIR}/docs/Doxyfile.in 
                   ${CMAKE_CURRENT_BINARY_DIR}/Doxyfile @ONLY)
    add_custom_target(doc
        ${DOXYGEN_EXECUTABLE} ${CMAKE_CURRENT_BINARY_DIR}/Doxyfile
        WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
        COMMENT "Generating API documentation with Doxygen" VERBATIM)
endif()

# Installation
install(TARGETS privanna_engine
    RUNTIME DESTINATION bin
    LIBRARY DESTINATION lib
    ARCHIVE DESTINATION lib
)

# Install resources
install(DIRECTORY assets/
    DESTINATION share/privanna/assets
    FILES_MATCHING PATTERN "*.json" PATTERN "*.png" PATTERN "*.wav" PATTERN "*.obj"
)

# Install documentation
install(DIRECTORY docs/
    DESTINATION share/doc/privanna
    FILES_MATCHING PATTERN "*.md" PATTERN "*.pdf"
)

# Package configuration
include(CMakePackageConfigHelpers)

configure_package_config_file(
    "${CMAKE_CURRENT_SOURCE_DIR}/cmake/PrivannaEngineConfig.cmake.in"
    "${CMAKE_CURRENT_BINARY_DIR}/PrivannaEngineConfig.cmake"
    INSTALL_DESTINATION lib/cmake/PrivannaEngine
)

write_basic_package_version_file(
    "${CMAKE_CURRENT_BINARY_DIR}/PrivannaEngineConfigVersion.cmake"
    VERSION ${PROJECT_VERSION}
    COMPATIBILITY SameMajorVersion
)

install(FILES
    "${CMAKE_CURRENT_BINARY_DIR}/PrivannaEngineConfig.cmake"
    "${CMAKE_CURRENT_BINARY_DIR}/PrivannaEngineConfigVersion.cmake"
    DESTINATION lib/cmake/PrivannaEngine
)

# CPack configuration for packaging
include(CPack)
set(CPACK_PACKAGE_NAME "PrivannaEngine")
set(CPACK_PACKAGE_VERSION ${PROJECT_VERSION})
set(CPACK_PACKAGE_DESCRIPTION_SUMMARY "Massive Scale Game Engine - Privanna")
set(CPACK_PACKAGE_VENDOR "Privanna Development Team")
set(CPACK_RESOURCE_FILE_LICENSE "${CMAKE_CURRENT_SOURCE_DIR}/LICENSE")
set(CPACK_RESOURCE_FILE_README "${CMAKE_CURRENT_SOURCE_DIR}/README.md")

# Platform-specific packaging
if(WIN32)
    set(CPACK_GENERATOR "NSIS;ZIP")
    set(CPACK_NSIS_DISPLAY_NAME "Privanna Engine")
elseif(APPLE)
    set(CPACK_GENERATOR "DragNDrop;TGZ")
else()
    set(CPACK_GENERATOR "DEB;RPM;TGZ")
    set(CPACK_DEBIAN_PACKAGE_DEPENDS "libgl1-mesa-glx, libopenal1, libvorbisfile3")
endif()

# Development mode configuration
option(PRIVANNA_DEVELOPMENT_MODE "Enable development mode features" OFF)
if(PRIVANNA_DEVELOPMENT_MODE)
    target_compile_definitions(privanna_engine PRIVATE PRIVANNA_DEVELOPMENT_MODE)
    add_compile_options(-O0 -g -fsanitize=address -fsanitize=undefined)
    target_link_options(privanna_engine -fsanitize=address -fsanitize=undefined)
endif()

# Performance profiling mode
option(PRIVANNA_PROFILING "Enable performance profiling" OFF)
if(PRIVANNA_PROFILING)
    target_compile_definitions(privanna_engine PRIVATE PRIVANNA_PROFILING)
    find_package(gperftools QUIET)
    if(GPERFTOOLS_FOUND)
        target_link_libraries(privanna_engine profiler)
    endif()
endif()

# VR support
option(PRIVANNA_VR_SUPPORT "Enable VR support" OFF)
if(PRIVANNA_VR_SUPPORT)
    find_package(OpenVR QUIET)
    if(OPENVR_FOUND)
        target_link_libraries(privanna_engine OpenVR::OpenVR)
        target_compile_definitions(privanna_engine PRIVATE PRIVANNA_VR_SUPPORT)
    endif()
endif()

# AI acceleration with CUDA
option(PRIVANNA_CUDA_ACCELERATION "Enable CUDA acceleration for AI" OFF)
if(PRIVANNA_CUDA_ACCELERATION)
    enable_language(CUDA)
    find_package(CUDAToolkit QUIET)
    if(CUDAToolkit_FOUND)
        target_link_libraries(privanna_engine CUDA::cudart CUDA::cuda)
        target_compile_definitions(privanna_engine PRIVATE PRIVANNA_CUDA_ACCELERATION)
    endif()
endif()

# Print configuration summary
message(STATUS "")
message(STATUS "Privanna Engine Configuration Summary:")
message(STATUS "  Version: ${PROJECT_VERSION}")
message(STATUS "  Build Type: ${CMAKE_BUILD_TYPE}")
message(STATUS "  C++ Standard: ${CMAKE_CXX_STANDARD}")
message(STATUS "  Install Prefix: ${CMAKE_INSTALL_PREFIX}")
message(STATUS "")
message(STATUS "Features:")
message(STATUS "  Development Mode: ${PRIVANNA_DEVELOPMENT_MODE}")
message(STATUS "  Profiling: ${PRIVANNA_PROFILING}")
message(STATUS "  VR Support: ${PRIVANNA_VR_SUPPORT}")
message(STATUS "  CUDA Acceleration: ${PRIVANNA_CUDA_ACCELERATION}")
message(STATUS "")
message(STATUS "Libraries:")
message(STATUS "  PyTorch: ${TORCH_VERSION}")
message(STATUS "  OpenCV: ${OpenCV_VERSION}")
message(STATUS "  OpenGL: ${OPENGL_VERSION}")
message(STATUS "  Boost: ${Boost_VERSION}")
message(STATUS "")