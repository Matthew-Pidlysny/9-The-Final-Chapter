cmake_minimum_required(VERSION 3.25)
project(DarkContinent VERSION 1.0.0 LANGUAGES CXX)

# Set C++ standard
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# Set build type
if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE Release)
endif()

# Compiler-specific options
if(MSVC)
    add_compile_options(/W4 /permissive-)
else()
    add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# Find required packages
find_package(OpenGL REQUIRED)
find_package(PkgConfig REQUIRED)
find_package(Threads REQUIRED)

# Find SFML
find_package(SFML 2.6 COMPONENTS graphics audio network system window REQUIRED)

# Find OpenGL
find_package(OpenGL REQUIRED)

# Include directories
include_directories(${CMAKE_CURRENT_SOURCE_DIR})
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/include)

# Add subdirectories
add_subdirectory(src)

# Main executable
add_executable(DarkContinent
    main.cpp
    src/GameEngine.cpp
    src/GameBoard.cpp
    src/Player.cpp
    src/Card.cpp
    src/CardSystem.cpp
    src/CombatSystem.cpp
    src/PopulationCounter.cpp
    src/EconomySystem.cpp
    src/NetworkManager.cpp
    src/SaveSystem.cpp
    src/EventManager.cpp
    src/UnitedStates.cpp
    src/Russia.cpp
    src/EuropeanUnion.cpp
    src/SouthernAlliance.cpp
    src/DarkContinent.cpp
    src/AmericaDeck.cpp
    src/CommunismDeck.cpp
    src/DivineWillDeck.cpp
    src/MischiefDeck.cpp
    src/EUInfluenceDeck.cpp
    src/AllianceDeck.cpp
    src/Renderer.cpp
    src/UIManager.cpp
    src/MapRenderer.cpp
    src/PieceRenderer.cpp
    src/CardRenderer.cpp
    src/InputManager.cpp
    src/AudioManager.cpp
    src/ResourceManager.cpp
    src/UnitManager.cpp
    src/FortificationSystem.cpp
    src/MovementSystem.cpp
    src/InfluenceSystem.cpp
    src/MathUtils.cpp
    src/FileUtils.cpp
    src/StringUtils.cpp
    src/ConfigSystem.cpp
    src/Logger.cpp
    src/AnimationSystem.cpp
    src/game_simulation.cpp
)

# Link libraries
target_link_libraries(DarkContinent
    ${SFML_LIBRARIES}
    ${OPENGL_LIBRARIES}
    Threads::Threads
)

# Platform-specific libraries
if(WIN32)
    target_link_libraries(DarkContinent ws2_32)
elseif(UNIX AND NOT APPLE)
    find_package(X11 REQUIRED)
    target_link_libraries(DarkContinent ${X11_LIBRARIES})
endif()

# Copy assets to build directory
add_custom_command(TARGET DarkContinent POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E copy_directory
    ${CMAKE_SOURCE_DIR}/assets $<TARGET_FILE_DIR:DarkContinent>/assets
)

# Copy documentation to build directory
add_custom_command(TARGET DarkContinent POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E copy
    ${CMAKE_SOURCE_DIR}/Game_Rules.md $<TARGET_FILE_DIR:DarkContinent>/Game_Rules.md
    COMMAND ${CMAKE_COMMAND} -E copy
    ${CMAKE_SOURCE_DIR}/README.md $<TARGET_FILE_DIR:DarkContinent>/README.md
)

# Installation
install(TARGETS DarkContinent
    RUNTIME DESTINATION bin
    LIBRARY DESTINATION lib
    ARCHIVE DESTINATION lib
)

install(DIRECTORY assets DESTINATION share/DarkContinent)
install(FILES Game_Rules.md README.md DESTINATION share/DarkContinent/doc)

# Package configuration
set(CPACK_PACKAGE_NAME "DarkContinent")
set(CPACK_PACKAGE_VERSION "${PROJECT_VERSION}")
set(CPACK_PACKAGE_DESCRIPTION_SUMMARY "Dark Continent 5-Player Strategy Game")
set(CPACK_PACKAGE_VENDOR "NinjaTech AI")
set(CPACK_PACKAGE_CONTACT "support@darkcontinent.game")

if(WIN32)
    set(CPACK_GENERATOR "NSIS;ZIP")
    set(CPACK_NSIS_DISPLAY_NAME "Dark Continent")
    set(CPACK_NSIS_PACKAGE_NAME "DarkContinent")
elseif(APPLE)
    set(CPACK_GENERATOR "DragNDrop;ZIP")
else()
    set(CPACK_GENERATOR "DEB;RPM;ZIP")
    set(CPACK_DEBIAN_PACKAGE_DEPENDS "libsfml-dev, libopengl-dev")
    set(CPACK_RPM_PACKAGE_REQUIRES "sfml-devel, opengl-devel")
endif()

include(CPack)

# Custom targets for development
add_custom_target(run
    COMMAND DarkContinent
    DEPENDS DarkContinent
    WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
)

add_custom_target(test
    COMMAND ./DarkContinent --test-simulation
    DEPENDS DarkContinent
    WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
)

add_custom_target(valgrind
    COMMAND valgrind --leak-check=full ./DarkContinent
    DEPENDS DarkContinent
    WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
)

# Documentation generation
find_package(Doxygen)
if(DOXYGEN_FOUND)
    configure_file(${CMAKE_CURRENT_SOURCE_DIR}/docs/Doxyfile.in
                   ${CMAKE_CURRENT_BINARY_DIR}/Doxyfile @ONLY)
    add_custom_target(doc
        ${DOXYGEN_EXECUTABLE} ${CMAKE_CURRENT_BINARY_DIR}/Doxyfile
        WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
        COMMENT "Generating API documentation with Doxygen"
        VERBATIM
    )
endif()