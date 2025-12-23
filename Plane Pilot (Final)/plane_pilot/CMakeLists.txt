cmake_minimum_required(VERSION 3.10)
project(PlanePilot VERSION 1.0.0 LANGUAGES CXX)

# Set C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Find required packages
find_package(OpenGL REQUIRED)
find_package(glfw3 REQUIRED)
find_package(Threads REQUIRED)
find_package(PkgConfig REQUIRED)
pkg_check_modules(GLFW REQUIRED glfw3)

# Include directories
include_directories(${CMAKE_SOURCE_DIR}/include)
include_directories(${CMAKE_SOURCE_DIR}/external)
include_directories(${GLFW_INCLUDE_DIRS})

# Add external libraries (we'll create simple implementations)
add_subdirectory(external)

# Source files
set(SOURCES
    src/main.cpp
    src/PlanePilotApp.cpp
    src/gui/SplashScreen.cpp
    src/gui/MainWindow.cpp
    src/gui/WorkshopSelector.cpp
    src/gui/FontManager.cpp
    src/gui/ThemeManager.cpp
    src/workshops/HadwigerNelsonWorkshop.cpp
    src/workshops/ChromaticOlympics.cpp
    src/workshops/GeometrySequencing.cpp
    src/workshops/SphereOMatic.cpp
    src/graphics/Renderer.cpp
    src/graphics/Shader.cpp
    src/utils/Logger.cpp
)

# Create executable
add_executable(PlanePilot ${SOURCES})

# Link libraries
target_link_libraries(PlanePilot 
    OpenGL::GL 
    ${CMAKE_THREAD_LIBS_INIT}
    plane_pilot_libs
    ${GLFW_LIBRARIES}
    ${GLFW_LINK_LIBRARIES}
    GLU
)

# Set output directory
set_target_properties(PlanePilot PROPERTIES
    RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin
)

# Copy resources
file(COPY ${CMAKE_SOURCE_DIR}/resources DESTINATION ${CMAKE_BINARY_DIR}/bin)