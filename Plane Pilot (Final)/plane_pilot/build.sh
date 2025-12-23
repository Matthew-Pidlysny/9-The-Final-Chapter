#!/bin/bash

# Plane Pilot Build Script
# Educational Hadwiger-Nelson Geometry Software

echo "=========================================="
echo "Building Plane Pilot Educational Software"
echo "=========================================="

# Check dependencies
echo "Checking dependencies..."

# Check for CMake
if ! command -v cmake &> /dev/null; then
    echo "Error: CMake is required but not installed."
    echo "Please install CMake (version 3.10 or higher)"
    exit 1
fi

# Check for C++ compiler
if ! command -v g++ &> /dev/null; then
    echo "Error: g++ compiler is required but not installed."
    echo "Please install build-essential package"
    exit 1
fi

# Check for OpenGL development libraries
if ! pkg-config --exists gl; then
    echo "Error: OpenGL development libraries are required."
    echo "Please install libgl1-mesa-dev package"
    exit 1
fi

# Check for GLFW
if ! pkg-config --exists glfw3; then
    echo "Warning: GLFW3 not found, attempting to install..."
    # Try to install GLFW3 (Ubuntu/Debian)
    if command -v apt-get &> /dev/null; then
        sudo apt-get update
        sudo apt-get install -y libglfw3-dev
    else
        echo "Please install GLFW3 development libraries manually"
        exit 1
    fi
fi

echo "Dependencies check completed."
echo ""

# Create build directory
echo "Creating build directory..."
mkdir -p build
cd build

# Configure with CMake
echo "Configuring with CMake..."
cmake .. -DCMAKE_BUILD_TYPE=Release

if [ $? -ne 0 ]; then
    echo "Error: CMake configuration failed."
    exit 1
fi

echo ""

# Build the project
echo "Building Plane Pilot..."
make -j$(nproc)

if [ $? -ne 0 ]; then
    echo "Error: Build failed."
    exit 1
fi

echo ""

# Create distribution directory
echo "Creating distribution package..."
mkdir -p ../dist
mkdir -p ../dist/bin
mkdir -p ../dist/resources
mkdir -p ../dist/docs

# Copy executable
if [ -f "bin/PlanePilot" ]; then
    cp bin/PlanePilot ../dist/bin/
    echo "✓ Executable copied"
else
    echo "Warning: Executable not found"
fi

# Copy resources
if [ -d "../resources" ]; then
    cp -r ../resources/* ../dist/resources/
    echo "✓ Resources copied"
fi

# Copy documentation
if [ -f "../README.md" ]; then
    cp ../README.md ../dist/docs/
    echo "✓ Documentation copied"
fi

# Copy build script
cp ../build.sh ../dist/
echo "✓ Build script copied"

echo ""
echo "=========================================="
echo "BUILD SUCCESSFUL!"
echo "=========================================="
echo ""
echo "Plane Pilot has been built successfully!"
echo ""
echo "To run the application:"
echo "  cd dist"
echo "  ./bin/PlanePilot"
echo ""
echo "Distribution package created in 'dist' directory"
echo "Ready for classroom deployment!"
echo ""

# Test if executable exists and is executable
if [ -f "../dist/bin/PlanePilot" ]; then
    echo "Testing executable..."
    if [ -x "../dist/bin/PlanePilot" ]; then
        echo "✓ Executable is properly built and executable"
    else
        echo "Warning: Executable may not have proper permissions"
        chmod +x ../dist/bin/PlanePilot
        echo "✓ Permissions fixed"
    fi
else
    echo "Warning: Executable may not have been created properly"
fi

echo ""
echo "Build process completed. Plane Pilot is ready for educational use!"