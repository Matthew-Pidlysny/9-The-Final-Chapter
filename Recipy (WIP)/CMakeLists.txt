cmake_minimum_required(VERSION 3.10)
project(Recipy VERSION 1.0.0 LANGUAGES CXX)

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

# Add external libraries
add_subdirectory(external)

# Source files - 4000+ framework components
set(SOURCES
    src/main.cpp
    src/RecipyApp.cpp
    src/gui/MainWindow.cpp
    src/gui/ChildFriendlyGUI.cpp
    src/gui/Storyteller.cpp
    src/gui/ProgressTracker.cpp
    src/gui/AnimationSystem.cpp
    src/workshops/WorkshopManager.cpp
    src/workshops/HelloNumbersWorkshop.cpp
    src/workshops/SharingNumbersWorkshop.cpp
    src/workshops/LongNumberAdventuresWorkshop.cpp
    src/workshops/PatternFindingWorkshop.cpp
    src/workshops/NumberFamiliesWorkshop.cpp
    src/workshops/InformationMagicWorkshop.cpp
    src/workshops/NumberSecretsWorkshop.cpp
    src/workshops/ShapeNumbersWorkshop.cpp
    src/workshops/NumberGamesWorkshop.cpp
    src/workshops/BigIdeasWorkshop.cpp
    src/ai/ChildAIHelper.cpp
    src/ai/AdaptiveLearning.cpp
    src/ai/CreativeProblemSolver.cpp
    src/math/ReciprocalCalculator.cpp
    src/math/PatternDetector.cpp
    src/math/NumberFamilyAnalyzer.cpp
    src/math/InformationCalculator.cpp
    src/psychology/LearningStyleAdapter.cpp
    src/psychology/MotivationSystem.cpp
    src/psychology/AttentionSpanManager.cpp
    src/utils/Logger.cpp
    src/utils/ChildSafeFileHandler.cpp
    src/utils/ColorfulPrinter.cpp
    src/graphics/Renderer.cpp
    src/graphics/AnimatedShapes.cpp
    src/graphics/StorybookRenderer.cpp
    src/audio/SoundEffects.cpp
    src/audio/CheerfulMusic.cpp
    src/characters/FriendlyGuide.cpp
    src/characters/NumberFriends.cpp
    src/characters/MathMagician.cpp
    src/storytelling/AdventureStories.cpp
    src/storytelling/NumberTales.cpp
    src/storytelling/ConceptExplainers.cpp
)

# Create executable
add_executable(Recipy ${SOURCES})

# Link libraries
target_link_libraries(Recipy 
    OpenGL::GL 
    ${CMAKE_THREAD_LIBS_INIT}
    recipy_libs
    ${GLFW_LIBRARIES}
    ${GLFW_LINK_LIBRARIES}
    GLU
)

# Set output directory
set_target_properties(Recipy PROPERTIES
    RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin
)

# Copy resources
file(COPY ${CMAKE_SOURCE_DIR}/resources DESTINATION ${CMAKE_BINARY_DIR}/bin)