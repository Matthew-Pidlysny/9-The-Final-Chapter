#!/bin/bash

# Enuanza Build Script for Linux/macOS
# This script builds the C++ version of Enuanza with all dependencies

set -e

echo "================================================"
echo "    Enuanza C++ Build Script for Linux/macOS   "
echo "================================================"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if we're in the right directory
if [ ! -f "CMakeLists.txt" ]; then
    print_error "CMakeLists.txt not found. Please run this script from the enuanza_cpp directory."
    exit 1
fi

# Create build directory
print_status "Creating build directory..."
mkdir -p build
cd build

# Check for dependencies
print_status "Checking dependencies..."

# Check for cmake
if ! command -v cmake &> /dev/null; then
    print_error "CMake is not installed. Please install CMake (version 3.16 or higher)."
    exit 1
fi

# Check for pkg-config
if ! command -v pkg-config &> /dev/null; then
    print_warning "pkg-config not found. Some library detection may fail."
fi

# Install dependencies based on the package manager
install_dependencies() {
    if command -v apt-get &> /dev/null; then
        print_status "Installing dependencies with apt-get..."
        sudo apt-get update
        sudo apt-get install -y \
            build-essential \
            cmake \
            libglfw3-dev \
            libglew-dev \
            libopenal-dev \
            libglm-dev \
            libgl1-mesa-dev \
            libglu1-mesa-dev \
            libx11-dev \
            libxi-dev \
            libxrandr-dev \
            libxinerama-dev \
            libxcursor-dev \
            libwayland-dev \
            libxkbcommon-dev
    elif command -v yum &> /dev/null; then
        print_status "Installing dependencies with yum..."
        sudo yum install -y \
            gcc-c++ \
            cmake \
            glfw-devel \
            glew-devel \
            openal-devel \
            glm-devel \
            mesa-libGL-devel \
            libX11-devel \
            libXi-devel \
            libXrandr-devel \
            libXinerama-devel \
            libXcursor-devel
    elif command -v pacman &> /dev/null; then
        print_status "Installing dependencies with pacman..."
        sudo pacman -S --needed \
            base-devel \
            cmake \
            glfw \
            glew \
            openal \
            glm \
            mesa \
            libx11 \
            libxi \
            libxrandr \
            libxinerama \
            libxcursor
    elif command -v brew &> /dev/null; then
        print_status "Installing dependencies with Homebrew..."
        brew install \
            cmake \
            glfw \
            glew \
            openal-soft \
            glm
    else
        print_warning "Unable to detect package manager. Please install dependencies manually:"
        echo "  - CMake (3.16+)"
        echo "  - GLFW3"
        echo "  - GLEW"
        echo "  - OpenAL"
        echo "  - GLM"
        echo "  - OpenGL drivers"
        echo ""
        read -p "Continue anyway? (y/N): " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            exit 1
        fi
    fi
}

# Ask user if they want to install dependencies
read -p "Install missing dependencies? (y/N): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    install_dependencies
fi

# Configure with CMake
print_status "Configuring project with CMake..."
cmake .. -DCMAKE_BUILD_TYPE=Release

# Build the project
print_status "Building Enuanza..."
make -j$(nproc 2>/dev/null || sysctl -n hw.ncpu 2>/dev/null || echo 4)

# Check if build was successful
if [ -f "Enuanza" ]; then
    print_status "Build successful! Executable created: $(pwd)/Enuanza"
else
    print_error "Build failed! Please check the error messages above."
    exit 1
fi

# Run tests (if available)
print_status "Running basic tests..."
./Enuanza --help 2>/dev/null || print_warning "No help command available (this is normal)"

echo ""
print_status "Build complete! To run Enuanza:"
echo "  cd $(pwd)"
echo "  ./Enuanza"
echo ""
print_status "For VR support, ensure your VR runtime is installed and running."
echo "================================================"