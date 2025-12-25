#!/bin/bash

# ASTRATECHNICA - EXTREMELY EPIC BUILD SCRIPT
# "Pave the way for a greater tomorrow!"

set -e

echo "========================================"
echo "  ASTRATECHNICA - EXTREMELY EPIC BUILD"
echo "  Pave the way for a greater tomorrow!"
echo "========================================"
echo

# Check if required tools are installed
echo "Checking build dependencies..."

# Check for CMake
if ! command -v cmake &> /dev/null; then
    echo "ERROR: CMake is not installed. Please install CMake 3.16 or later."
    exit 1
fi

CMAKE_VERSION=$(cmake --version | head -n1 | cut -d' ' -f3)
echo "Found CMake version: $CMAKE_VERSION"

# Check for C++ compiler
if command -v g++ &> /dev/null; then
    echo "Found g++ compiler: $(g++ --version | head -n1)"
    COMPILER="g++"
elif command -v clang++ &> /dev/null; then
    echo "Found clang++ compiler: $(clang++ --version | head -n1)"
    COMPILER="clang++"
else
    echo "ERROR: No C++ compiler found. Please install g++ or clang++."
    exit 1
fi

# Check for required libraries
echo "Checking for required libraries..."

# Check for OpenSSL
if pkg-config --exists openssl; then
    echo "✓ OpenSSL found: $(pkg-config --modversion openssl)"
else
    echo "⚠ OpenSSL not found via pkg-config, trying alternative detection..."
fi

# Check for libcurl
if pkg-config --exists libcurl; then
    echo "✓ libcurl found: $(pkg-config --modversion libcurl)"
else
    echo "⚠ libcurl not found via pkg-config, trying alternative detection..."
fi

# Check for optional AI/ML libraries
echo "Checking for optional AI/ML libraries..."

if pkg-config --exists torch; then
    echo "✓ PyTorch found: $(pkg-config --modversion torch)"
    AI_LIBS_AVAILABLE=true
else
    echo "⚠ PyTorch not found - AI features will be limited"
fi

if pkg-config --exists mlpack; then
    echo "✓ mlpack found: $(pkg-config --modversion mlpack)"
    AI_LIBS_AVAILABLE=true
else
    echo "⚠ mlpack not found - some ML features will be limited"
fi

if pkg-config --exists opencv4; then
    echo "✓ OpenCV found: $(pkg-config --modversion opencv4)"
    AI_LIBS_AVAILABLE=true
else
    echo "⚠ OpenCV not found - computer vision features will be limited"
fi

echo

# Create build directory
BUILD_DIR="build_astratechnica"
echo "Creating build directory: $BUILD_DIR"
rm -rf "$BUILD_DIR"
mkdir -p "$BUILD_DIR"
cd "$BUILD_DIR"

# Configure with CMake
echo "Configuring with CMake..."
BUILD_TYPE="Release"

if [ "$1" = "debug" ]; then
    BUILD_TYPE="Debug"
    echo "Building in Debug mode"
fi

CMAKE_ARGS=(
    -DCMAKE_BUILD_TYPE="$BUILD_TYPE"
    -DCMAKE_CXX_COMPILER="$COMPILER"
    -DCMAKE_INSTALL_PREFIX="$PWD/../install"
)

# Add debug flags if debug build
if [ "$BUILD_TYPE" = "Debug" ]; then
    CMAKE_ARGS+=(-DCMAKE_CXX_FLAGS="-g -O0 -Wall -Wextra -DDEBUG")
fi

# Try to find and configure AI libraries
if [ "$AI_LIBS_AVAILABLE" = true ]; then
    echo "AI libraries available - enabling advanced features"
    CMAKE_ARGS+=(-DENABLE_AI_FEATURES=ON)
else
    echo "Building without AI libraries - core features only"
    CMAKE_ARGS+=(-DENABLE_AI_FEATURES=OFF)
fi

# Run CMake configuration
echo "Running CMake with arguments: ${CMAKE_ARGS[@]}"
cmake .. "${CMAKE_ARGS[@]}"

if [ $? -ne 0 ]; then
    echo "ERROR: CMake configuration failed!"
    exit 1
fi

echo

# Build the project
echo "Building AstraTechnica..."
echo "This may take a few minutes as we're building something EXTREMELY EPIC!"

# Determine number of CPU cores for parallel build
if command -v nproc &> /dev/null; then
    CORES=$(nproc)
elif command -v sysctl &> /dev/null; then
    CORES=$(sysctl -n hw.ncpu)
else
    CORES=4
fi

echo "Using $CORES parallel jobs"

# Build
make -j"$CORES"

if [ $? -ne 0 ]; then
    echo "ERROR: Build failed!"
    exit 1
fi

echo

# Success!
echo "=========================================="
echo "  🚀 BUILD SUCCESSFUL! 🚀"
echo "=========================================="
echo

# Show build results
BINARY_PATH="$PWD/astratechnica"
if [ -f "$BINARY_PATH" ]; then
    echo "✓ Executable created: $BINARY_PATH"
    
    # Show binary size
    BINARY_SIZE=$(du -h "$BINARY_PATH" | cut -f1)
    echo "  Binary size: $BINARY_SIZE"
    
    # Show build info
    echo "  Build type: $BUILD_TYPE"
    echo "  Compiler: $COMPILER"
    echo "  Build directory: $PWD"
    
    echo
    echo "To run AstraTechnica:"
    echo "  $BINARY_PATH"
    echo
    echo "Or from the project root:"
    echo "  cd $BUILD_DIR && ./astratechnica"
    echo
    
    # Test if binary runs (quick check)
    echo "Running quick binary test..."
    if timeout 3s "$BINARY_PATH" --version 2>/dev/null; then
        echo "✓ Binary test passed!"
    else
        echo "⚠ Binary test failed or --version not implemented"
    fi
    
else
    echo "ERROR: Executable not found at expected location!"
    exit 1
fi

echo
echo "=========================================="
echo "  ASTRATECHICA IS READY TO PLAY!"
echo "  Pave the way for a greater tomorrow!"
echo "=========================================="
echo

# Additional info
echo "Game Features Available:"
echo "- 5 Unique Characters with different abilities"
echo "- Advanced Phone Integration with push notifications"
echo "- AI-powered enemies and companions"
echo "- Real-time world simulation"
echo "- Company management and cyber warfare"
echo "- The Ghazarkhan shadow government mechanics"
echo "- Extensive character progression system"
echo

if [ "$AI_LIBS_AVAILABLE" = true ]; then
    echo "Advanced AI Features Enabled:"
    echo "- Neural network decision making"
    echo "- Machine learning opponent adaptation"
    echo "- Predictive analytics"
    echo "- Computer vision capabilities"
    echo "- Natural language processing"
    echo
else
    echo "Note: Install AI libraries (PyTorch, mlpack, OpenCV) for advanced features:"
    echo "  sudo apt install libtorch-dev mlpack-dev libopencv-dev nlohmann-json3-dev"
    echo "  brew install libtorch mlpack opencv nlohmann-json"
    echo
fi

echo "Phone Integration Setup:"
echo "1. Configure server endpoint in game settings"
echo "2. Install companion mobile app (when available)"
echo "3. Enable notifications in system preferences"
echo

echo "Happy gaming! May your company dominate the digital world!"