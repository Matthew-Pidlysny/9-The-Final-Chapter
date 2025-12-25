#!/bin/bash

# Privanna Engine Build Script
# Massive Scale C++ Project - 50+ Modules, 15,000+ Commit Target
# Automated build with dependency management and optimization

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Build configuration
BUILD_TYPE="${BUILD_TYPE:-Release}"
BUILD_DIR="${BUILD_DIR:-build}"
INSTALL_DIR="${INSTALL_DIR:-install}"
PARALLEL_JOBS="${PARALLEL_JOBS:-$(nproc)}"
ENABLE_TESTS="${ENABLE_TESTS:-ON}"
ENABLE_BENCHMARKS="${ENABLE_BENCHMARKS:-ON}"
ENABLE_VR="${ENABLE_VR:-OFF}"
ENABLE_CUDA="${ENABLE_CUDA:-OFF}"
DEVELOPMENT_MODE="${DEVELOPMENT_MODE:-OFF}"

# Print header
echo -e "${PURPLE}============================================${NC}"
echo -e "${PURPLE}    PRIVANNA ENGINE BUILD SYSTEM${NC}"
echo -e "${PURPLE}    Massive Scale C++ Project${NC}"
echo -e "${PURPLE}    Target: 15,000+ Commits${NC}"
echo -e "${PURPLE}============================================${NC}"
echo ""

# Function to print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

print_section() {
    echo -e "${CYAN}================================${NC}"
    echo -e "${CYAN}$1${NC}"
    echo -e "${CYAN}================================${NC}"
}

# Check system requirements
check_requirements() {
    print_section "Checking System Requirements"
    
    # Check CMake version
    if command -v cmake &> /dev/null; then
        CMAKE_VERSION=$(cmake --version | head -n1 | cut -d' ' -f3)
        print_status "CMake version: $CMAKE_VERSION"
        
        # Compare versions (requires CMake 3.20+)
        if [[ $(echo "$CMAKE_VERSION 3.20" | tr ' ' '\n' | sort -V | head -n1) != "3.20" ]]; then
            print_error "CMake version 3.20 or higher is required"
            exit 1
        fi
    else
        print_error "CMake is not installed"
        exit 1
    fi
    
    # Check compiler
    if command -v g++ &> /dev/null; then
        GCC_VERSION=$(g++ --version | head -n1 | cut -d' ' -f4)
        print_status "GCC version: $GCC_VERSION"
    elif command -v clang++ &> /dev/null; then
        CLANG_VERSION=$(clang++ --version | head -n1 | cut -d' ' -f3)
        print_status "Clang version: $CLANG_VERSION"
    else
        print_error "No suitable C++ compiler found"
        exit 1
    fi
    
    # Check Python (for AI models)
    if command -v python3 &> /dev/null; then
        PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
        print_status "Python version: $PYTHON_VERSION"
    else
        print_warning "Python3 not found - AI model training will be limited"
    fi
    
    # Check available memory
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        MEMORY_KB=$(grep MemTotal /proc/meminfo | awk '{print $2}')
        MEMORY_GB=$((MEMORY_KB / 1024 / 1024))
        print_status "Available RAM: ${MEMORY_GB}GB"
        
        if [[ $MEMORY_GB -lt 8 ]]; then
            print_warning "Less than 8GB RAM available - build may be slow"
        fi
    fi
    
    # Check disk space
    DISK_AVAILABLE=$(df . | tail -1 | awk '{print $4}')
    DISK_GB=$((DISK_AVAILABLE / 1024 / 1024))
    print_status "Available disk space: ${DISK_GB}GB"
    
    if [[ $DISK_GB -lt 10 ]]; then
        print_error "Insufficient disk space - at least 10GB required"
        exit 1
    fi
    
    print_success "System requirements check passed"
}

# Install dependencies
install_dependencies() {
    print_section "Installing Dependencies"
    
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        # Linux dependencies
        print_status "Installing Linux dependencies..."
        
        # Check package manager
        if command -v apt-get &> /dev/null; then
            # Ubuntu/Debian
            sudo apt-get update
            sudo apt-get install -y \
                build-essential \
                cmake \
                pkg-config \
                libgl1-mesa-dev \
                libglu1-mesa-dev \
                libglfw3-dev \
                libglew-dev \
                libopenal-dev \
                libvorbis-dev \
                libogg-dev \
                libsdl2-dev \
                libboost-all-dev \
                libopencv-dev \
                git \
                python3 \
                python3-pip \
                wget \
                curl
                
        elif command -v yum &> /dev/null; then
            # CentOS/RHEL/Fedora
            sudo yum groupinstall -y "Development Tools"
            sudo yum install -y \
                cmake \
                pkgconfig \
                mesa-libGL-devel \
                mesa-libGLU-devel \
                glfw-devel \
                glew-devel \
                openal-devel \
                libvorbis-devel \
                libogg-devel \
                SDL2-devel \
                boost-devel \
                opencv-devel \
                git \
                python3 \
                python3-pip \
                wget \
                curl
        fi
        
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS dependencies
        print_status "Installing macOS dependencies..."
        
        if command -v brew &> /dev/null; then
            brew install cmake pkg-config glfw glew openal-soft libvorbis libogg sdl2 boost opencv git python3 wget
        else
            print_error "Homebrew is required for macOS dependency installation"
            exit 1
        fi
        
    elif [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "cygwin" ]]; then
        # Windows dependencies
        print_status "Windows detected - please ensure Visual Studio 2019+ with C++ development tools is installed"
        print_status "Install vcpkg and run: vcpkg install glfw3 glew openal-soft libvorbis libogg sdl2 boost opencv"
    fi
    
    # Install Python packages
    if command -v pip3 &> /dev/null; then
        print_status "Installing Python packages..."
        pip3 install --user torch torchvision opencv-python numpy matplotlib
    fi
    
    print_success "Dependencies installed"
}

# Download and setup LibTorch (PyTorch C++)
setup_libtorch() {
    print_section "Setting Up LibTorch (PyTorch C++)"
    
    LIBTORCH_DIR="third_party/libtorch"
    
    if [[ ! -d "$LIBTORCH_DIR" ]]; then
        print_status "Downloading LibTorch..."
        
        # Create third_party directory
        mkdir -p third_party
        
        # Download LibTorch (CPU optimized for compatibility)
        if [[ "$OSTYPE" == "linux-gnu"* ]]; then
            wget https://download.pytorch.org/libtorch/cpu/libtorch-shared-with-deps-latest.zip -O libtorch.zip
        elif [[ "$OSTYPE" == "darwin"* ]]; then
            wget https://download.pytorch.org/libtorch/cpu/libtorch-macos-latest.zip -O libtorch.zip
        else
            print_error "LibTorch download not supported on this platform"
            exit 1
        fi
        
        # Extract LibTorch
        unzip libtorch.zip -d third_party/
        rm libtorch.zip
        
        # Rename if necessary
        if [[ -d "third_party/libtorch" ]]; then
            print_status "LibTorch extracted successfully"
        else
            print_error "LibTorch extraction failed"
            exit 1
        fi
    else
        print_status "LibTorch already exists, skipping download"
    fi
    
    print_success "LibTorch setup complete"
}

# Download AI models
download_ai_models() {
    print_section "Downloading Pre-trained AI Models"
    
    MODELS_DIR="models"
    
    if [[ ! -d "$MODELS_DIR" ]]; then
        mkdir -p "$MODELS_DIR"
    fi
    
    # Create placeholder model files (in real implementation, download from server)
    print_status "Creating AI model placeholders..."
    
    cat > "$MODELS_DIR/strategic_ai.pt" << 'EOF'
# Placeholder for Strategic AI model
# In production, this would be a trained PyTorch model
EOF
    
    cat > "$MODELS_DIR/tactical_ai.pt" << 'EOF'
# Placeholder for Tactical AI model
# In production, this would be a trained PyTorch model
EOF
    
    cat > "$MODELS_DIR/economic_ai.pt" << 'EOF'
# Placeholder for Economic AI model
# In production, this would be a trained PyTorch model
EOF
    
    cat > "$MODELS_DIR/diplomatic_ai.pt" << 'EOF'
# Placeholder for Diplomatic AI model
# In production, this would be a trained PyTorch model
EOF
    
    cat > "$MODELS_DIR/creative_ai.pt" << 'EOF'
# Placeholder for Creative AI model
# In production, this would be a trained PyTorch model
EOF
    
    print_success "AI models setup complete"
}

# Configure build with CMake
configure_build() {
    print_section "Configuring Build with CMake"
    
    # Create build directory
    mkdir -p "$BUILD_DIR"
    cd "$BUILD_DIR"
    
    # CMake configuration options
    CMAKE_OPTS=(
        "-DCMAKE_BUILD_TYPE=$BUILD_TYPE"
        "-DCMAKE_INSTALL_PREFIX=../$INSTALL_DIR"
        "-DENABLE_TESTS=$ENABLE_TESTS"
        "-DENABLE_BENCHMARKS=$ENABLE_BENCHMARKS"
        "-DPRIVANNA_VR_SUPPORT=$ENABLE_VR"
        "-DPRIVANNA_CUDA_ACCELERATION=$ENABLE_CUDA"
        "-DPRIVANNA_DEVELOPMENT_MODE=$DEVELOPMENT_MODE"
    )
    
    # Additional optimizations for Release build
    if [[ "$BUILD_TYPE" == "Release" ]]; then
        CMAKE_OPTS+=("-DCMAKE_CXX_FLAGS_RELEASE=-O3 -DNDEBUG -march=native -flto")
        CMAKE_OPTS+=("-DCMAKE_INTERPROCEDURAL_OPTIMIZATION=ON")
    fi
    
    # Run CMake configuration
    print_status "Running CMake configuration..."
    cmake .. "${CMAKE_OPTS[@]}"
    
    print_success "CMake configuration complete"
}

# Build the project
build_project() {
    print_section "Building Privanna Engine"
    
    # Build with parallel jobs
    print_status "Building with $PARALLEL_JOBS parallel jobs..."
    
    if [[ "$BUILD_TYPE" == "Release" ]]; then
        # Use all available cores for Release build
        make -j"$PARALLEL_JOBS" VERBOSE=1
    else
        # Use fewer cores for Debug build to reduce memory usage
        DEBUG_JOBS=$((PARALLEL_JOBS / 2))
        make -j"$DEBUG_JOBS" VERBOSE=1
    fi
    
    print_success "Build completed"
}

# Run tests
run_tests() {
    if [[ "$ENABLE_TESTS" == "ON" ]]; then
        print_section "Running Tests"
        
        print_status "Running unit tests..."
        if ctest --output-on-failure --parallel "$PARALLEL_JOBS"; then
            print_success "All tests passed"
        else
            print_warning "Some tests failed"
        fi
        
        # Run benchmarks if enabled
        if [[ "$ENABLE_BENCHMARKS" == "ON" ]]; then
            print_status "Running benchmarks..."
            if ctest --output-on-failure --label-match benchmark --parallel "$PARALLEL_JOBS"; then
                print_success "Benchmarks completed"
            fi
        fi
    fi
}

# Install the project
install_project() {
    print_section "Installing Privanna Engine"
    
    print_status "Installing to $INSTALL_DIR..."
    make install
    
    print_success "Installation complete"
}

# Generate build report
generate_report() {
    print_section "Build Report"
    
    echo "Build Configuration:"
    echo "  Build Type: $BUILD_TYPE"
    echo "  Parallel Jobs: $PARALLEL_JOBS"
    echo "  Tests Enabled: $ENABLE_TESTS"
    echo "  Benchmarks Enabled: $ENABLE_BENCHMARKS"
    echo "  VR Support: $ENABLE_VR"
    echo "  CUDA Acceleration: $ENABLE_CUDA"
    echo "  Development Mode: $DEVELOPMENT_MODE"
    echo ""
    
    # Calculate build time
    BUILD_END=$(date +%s)
    BUILD_DURATION=$((BUILD_END - BUILD_START))
    echo "Build Duration: ${BUILD_DURATION}s"
    echo ""
    
    # Show file sizes
    if [[ -f "$BUILD_DIR/privanna_engine" ]]; then
        ENGINE_SIZE=$(du -h "$BUILD_DIR/privanna_engine" | cut -f1)
        echo "Engine Binary Size: $ENGINE_SIZE"
    fi
    
    # Show library dependencies
    if command -v ldd &> /dev/null && [[ -f "$BUILD_DIR/privanna_engine" ]]; then
        echo ""
        echo "Library Dependencies:"
        ldd "$BUILD_DIR/privanna_engine" | grep -E "(libtorch|libopencv|libGL|libOpenAL)"
    fi
    
    echo ""
    print_success "Build report generated"
}

# Main build function
main() {
    BUILD_START=$(date +%s)
    
    print_status "Starting Privanna Engine build process..."
    print_status "Build started at $(date)"
    
    # Run build steps
    check_requirements
    install_dependencies
    setup_libtorch
    download_ai_models
    configure_build
    build_project
    run_tests
    install_project
    generate_report
    
    print_success "Privanna Engine build completed successfully!"
    print_status "Build completed at $(date)"
    
    # Show next steps
    echo ""
    print_section "Next Steps"
    echo "1. Run the engine:"
    echo "   cd $INSTALL_DIR/bin"
    echo "   ./privanna_engine"
    echo ""
    echo "2. Test AI systems:"
    echo "   ./privanna_engine --test-ai"
    echo ""
    echo "3. Start development server:"
    echo "   ./privanna_engine --server-mode --port 7777"
    echo ""
    echo "4. Generate documentation:"
    echo "   make doc  (if Doxygen is installed)"
}

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --build-type)
            BUILD_TYPE="$2"
            shift 2
            ;;
        --parallel-jobs)
            PARALLEL_JOBS="$2"
            shift 2
            ;;
        --enable-tests)
            ENABLE_TESTS="ON"
            shift
            ;;
        --disable-tests)
            ENABLE_TESTS="OFF"
            shift
            ;;
        --enable-vr)
            ENABLE_VR="ON"
            shift
            ;;
        --enable-cuda)
            ENABLE_CUDA="ON"
            shift
            ;;
        --development-mode)
            DEVELOPMENT_MODE="ON"
            shift
            ;;
        --clean)
            print_status "Cleaning build directory..."
            rm -rf "$BUILD_DIR" "$INSTALL_DIR"
            exit 0
            ;;
        --help)
            echo "Privanna Engine Build Script"
            echo ""
            echo "Usage: $0 [options]"
            echo ""
            echo "Options:"
            echo "  --build-type TYPE      Build type (Debug|Release) [default: Release]"
            echo "  --parallel-jobs N      Number of parallel build jobs [default: nproc]"
            echo "  --enable-tests         Enable unit tests [default: ON]"
            echo "  --disable-tests        Disable unit tests"
            echo "  --enable-vr            Enable VR support [default: OFF]"
            echo "  --enable-cuda          Enable CUDA acceleration [default: OFF]"
            echo "  --development-mode     Enable development mode features [default: OFF]"
            echo "  --clean                Clean build directory and exit"
            echo "  --help                 Show this help message"
            exit 0
            ;;
        *)
            print_error "Unknown option: $1"
            echo "Use --help for usage information"
            exit 1
            ;;
    esac
done

# Run main function
main "$@"