cmake_minimum_required(VERSION 3.16)
project(Enuanza VERSION 1.0.0 LANGUAGES CXX)

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
else()
    add_compile_options(-Wall -Wextra -Wpedantic -Werror)
    if(CMAKE_BUILD_TYPE STREQUAL "Release")
        add_compile_options(-O3 -DNDEBUG)
    elseif(CMAKE_BUILD_TYPE STREQUAL "Debug")
        add_compile_options(-g -O0 -DDEBUG)
    endif()
endif()

# Find required packages
find_package(OpenGL REQUIRED)
find_package(glfw3 REQUIRED)
find_package(GLEW REQUIRED)
find_package(OpenAL REQUIRED)
find_package(glm REQUIRED)

# Include directories
include_directories(${CMAKE_SOURCE_DIR}/include)
include_directories(${CMAKE_SOURCE_DIR}/shaders)

# Source files
set(SOURCES
    src/main.cpp
    src/PrimeComposition3D.cpp
    src/Shader.cpp
    src/AudioSystem.cpp
    src/ParticleSystem.cpp
    src/PrimeObject.cpp
)

# Header files
set(HEADERS
    include/PrimeComposition3D.h
    include/Shader.h
)

# Shader files
set(SHADERS
    shaders/vertex.glsl
    shaders/fragment.glsl
    shaders/particle_vertex.glsl
    shaders/particle_fragment.glsl
)

# Create executable
add_executable(Enuanza ${SOURCES} ${HEADERS} ${SHADERS})

# Link libraries
target_link_libraries(Enuanza
    OpenGL::GL
    glfw
    GLEW::GLEW
    OpenAL::OpenAL
    glm::glm
    ${CMAKE_DL_LIBS}
)

# Platform-specific libraries
if(WIN32)
    target_link_libraries(Enuanza opengl32)
elseif(APPLE)
    find_package(Cocoa REQUIRED)
    target_link_libraries(Enuanza ${COCOA_LIBRARIES})
    target_link_libraries(Enuanza "-framework OpenGL")
    target_link_libraries(Enuanza "-framework OpenAL")
elseif(UNIX)
    target_link_libraries(Enuanza X11 Xi Xrandr Xcursor Xinerama)
endif()

# Copy shaders to build directory
add_custom_command(TARGET Enuanza POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E make_directory ${CMAKE_BINARY_DIR}/shaders
    COMMAND ${CMAKE_COMMAND} -E copy_directory ${CMAKE_SOURCE_DIR}/shaders ${CMAKE_BINARY_DIR}/shaders
)

# Installation rules
install(TARGETS Enuanza
    RUNTIME DESTINATION bin
    LIBRARY DESTINATION lib
    ARCHIVE DESTINATION lib
)

install(FILES ${SHADERS}
    DESTINATION share/Enuanza/shaders
)

# Create package
include(CPack)
set(CPACK_PACKAGE_NAME "Enuanza")
set(CPACK_PACKAGE_VERSION "1.0.0")
set(CPACK_PACKAGE_DESCRIPTION_SUMMARY "Enuanza - Mathematical Immersion System")
set(CPACK_PACKAGE_VENDOR "Enuanza Project")
set(CPACK_PACKAGE_CONTACT "info@enuanza.math")

if(WIN32)
    set(CPACK_GENERATOR "NSIS;ZIP")
elseif(APPLE)
    set(CPACK_GENERATOR "DragNDrop;ZIP")
else()
    set(CPACK_GENERATOR "DEB;RPM;ZIP")
endif()

# Print configuration summary
message(STATUS "================================================")
message(STATUS "  Enuanza Configuration Summary")
message(STATUS "================================================")
message(STATUS "Build type: ${CMAKE_BUILD_TYPE}")
message(STATUS "C++ standard: ${CMAKE_CXX_STANDARD}")
message(STATUS "Install prefix: ${CMAKE_INSTALL_PREFIX}")
message(STATUS "================================================")