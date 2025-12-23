# External libraries for Plane Pilot
# Simplified implementations for educational purposes

add_library(plane_pilot_libs INTERFACE)

# Include directories
target_include_directories(plane_pilot_libs INTERFACE
    ${CMAKE_SOURCE_DIR}/external
)

# Add any external library dependencies here
# For example:
# target_link_libraries(plane_pilot_libs INTERFACE
#     ${GLFW_LIBRARIES}
#     ${OPENGL_LIBRARIES}
# )