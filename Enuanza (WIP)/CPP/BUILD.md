# Build Instructions for Enuanza C++ Edition

This document provides detailed build instructions for Enuanza on all supported platforms.

## Table of Contents

1. [System Requirements](#system-requirements)
2. [Dependencies](#dependencies)
3. [Platform-Specific Instructions](#platform-specific-instructions)
4. [Advanced Build Options](#advanced-build-options)
5. [Troubleshooting](#troubleshooting)

## System Requirements

### Minimum Requirements
- **OS**: Windows 10, Ubuntu 18.04+, macOS 10.15+
- **CPU**: Dual-core 2.0 GHz processor
- **RAM**: 4 GB RAM
- **GPU**: OpenGL 4.1 compatible graphics card
- **Storage**: 500 MB available space

### Recommended Requirements
- **OS**: Windows 11, Ubuntu 20.04+, macOS 12+
- **CPU**: Quad-core 3.0 GHz processor
- **RAM**: 8 GB RAM
- **GPU**: Dedicated graphics card with 4+ GB VRAM
- **Storage**: 1 GB available space

## Dependencies

### Core Dependencies
- **CMake** 3.16 or higher
- **C++17 compatible compiler**
- **OpenGL 4.1 drivers**
- **OpenAL** (audio system)

### Graphics Libraries
- **GLFW** 3.3+ (window management)
- **GLEW** (OpenGL extension loading)
- **GLM** (mathematics library)

### Platform-Specific

#### Linux
- X11 development libraries
- PulseAudio or ALSA for audio

#### Windows
- Visual Studio 2019+ or MinGW-w64
- Windows SDK 10.0+

#### macOS
- Xcode 12+ or Xcode Command Line Tools
- Cocoa framework

## Platform-Specific Instructions

### Ubuntu/Debian

#### 1. Install Dependencies
```bash
# Update package list
sudo apt update

# Install build tools
sudo apt install -y build-essential cmake git

# Install graphics libraries
sudo apt install -y libglfw3-dev libglew-dev libglm-dev

# Install audio system
sudo apt install -y libopenal-dev

# Install X11 development libraries
sudo apt install -y libx11-dev libxi-dev libxrandr-dev libxinerama-dev libxcursor-dev

# Install OpenGL development libraries
sudo apt install -y libgl1-mesa-dev libglu1-mesa-dev
```

#### 2. Build
```bash
# Clone repository
git clone https://github.com/enuanza/enuanza-cpp.git
cd enuanza-cpp

# Configure build
mkdir build && cd build
cmake .. -DCMAKE_BUILD_TYPE=Release

# Compile
make -j$(nproc)

# Run
./Enuanza
```

### Windows

#### Option 1: Using vcpkg (Recommended)

##### 1. Install vcpkg
```powershell
# Clone vcpkg
git clone https://github.com/Microsoft/vcpkg.git C:\vcpkg
cd C:\vcpkg

# Bootstrap vcpkg
.\bootstrap-vcpkg.bat

# Add to PATH (optional)
[Environment]::SetEnvironmentVariable("VCPKG_ROOT", "C:\vcpkg", "User")
```

##### 2. Install Dependencies
```powershell
# Install required packages
.\vcpkg install glfw3:x64-windows glew:x64-windows openal-soft:x64-windows glm:x64-windows
```

##### 3. Build with Visual Studio
```batch
REM Open Developer Command Prompt for VS
cd path\to\enuanza-cpp

REM Create build directory
mkdir build && cd build

REM Configure with CMake
cmake .. -DCMAKE_TOOLCHAIN_FILE=C:\vcpkg\scripts\buildsystems\vcpkg.cmake -DCMAKE_BUILD_TYPE=Release

REM Build
cmake --build . --config Release

REM Run
cd Release
Enuanza.exe
```

#### Option 2: Using vcpkg with MSBuild

```batch
REM Configure and build in one step
cmake --build . --config Release --target install
```

### macOS

#### 1. Install Xcode and Homebrew
```bash
# Install Xcode Command Line Tools
xcode-select --install

# Install Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

#### 2. Install Dependencies
```bash
# Install dependencies with Homebrew
brew install cmake glfw glew openal-soft glm

# Verify installation
brew list --versions cmake glfw glew openal-soft glm
```

#### 3. Build
```bash
# Clone repository
git clone https://github.com/enuanza/enuanza-cpp.git
cd enuanza-cpp

# Configure build
mkdir build && cd build
cmake .. -DCMAKE_BUILD_TYPE=Release

# Compile
make -j$(sysctl -n hw.ncpu)

# Run
./Enuanza
```

### Fedora/CentOS/RHEL

```bash
# Install dependencies
sudo dnf install -y gcc-c++ cmake git
sudo dnf install -y glfw-devel glew-devel openal-devel glm-devel
sudo dnf install -y mesa-libGL-devel libX11-devel libXi-devel

# Build
git clone https://github.com/enuanza/enuanza-cpp.git
cd enuanza-cpp
mkdir build && cd build
cmake .. -DCMAKE_BUILD_TYPE=Release
make -j$(nproc)
./Enuanza
```

### Arch Linux

```bash
# Install dependencies
sudo pacman -S --needed base-devel cmake git
sudo pacman -S glfw glew openal glm

# Build
git clone https://github.com/enuanza/enuanza-cpp.git
cd enuanza-cpp
mkdir build && cd build
cmake .. -DCMAKE_BUILD_TYPE=Release
make -j$(nproc)
./Enuanza
```

## Advanced Build Options

### Debug Build

```bash
# Configure for debugging
cmake .. -DCMAKE_BUILD_TYPE=Debug -DENABLE_LOGGING=ON

# Build with debug symbols
make -j$(nproc)

# Run with debugging
gdb ./Enuanza
```

### Static Linking

```bash
# Configure for static linking
cmake .. -DCMAKE_BUILD_TYPE=Release -DSTATIC_LINKING=ON

# Build
make -j$(nproc)
```

### Custom Installation Prefix

```bash
# Install to custom directory
cmake .. -DCMAKE_INSTALL_PREFIX=/opt/enuanza

# Build and install
make -j$(nproc)
sudo make install
```

### Cross-Compilation

#### Linux to Windows (MinGW)

```bash
# Install MinGW toolchain
sudo apt install -y mingw-w64 x86_64-w64-mingw32-g++

# Configure for cross-compilation
cmake .. -DCMAKE_TOOLCHAIN_FILE=../cmake/mingw-w64-x86_64.cmake

# Build
make -j$(nproc)
```

## Troubleshooting

### Common Build Errors

#### CMake Version Too Old
```
CMake Error: CMake 3.16 or higher is required
```

**Solution**: Install a newer version of CMake
```bash
# Ubuntu/Debian
sudo apt remove cmake
wget https://github.com/Kitware/CMake/releases/download/v3.24.2/cmake-3.24.2-linux-x86_64.sh
sudo sh cmake-3.24.2-linux-x86_64.sh --skip-license --prefix=/usr/local
```

#### OpenGL Headers Missing
```
fatal error: GL/gl.h: No such file or directory
```

**Solution**: Install OpenGL development headers
```bash
# Ubuntu/Debian
sudo apt install -y libgl1-mesa-dev libglu1-mesa-dev

# Fedora/CentOS
sudo dnf install -y mesa-libGL-devel libglvnd-devel
```

#### OpenAL Not Found
```
CMake Error: Could NOT find OpenAL
```

**Solution**: Install OpenAL development libraries
```bash
# Ubuntu/Debian
sudo apt install -y libopenal-dev

# Fedora/CentOS
sudo dnf install -y openal-devel

# macOS
brew install openal-soft
```

#### GLFW Not Found
```
CMake Error: Could NOT find GLFW
```

**Solution**: Install GLFW development libraries
```bash
# Ubuntu/Debian
sudo apt install -y libglfw3-dev

# Fedora/CentOS
sudo dnf install -y glfw-devel

# macOS
brew install glfw
```

### Runtime Issues

#### Black Screen or No Graphics
- Update graphics drivers
- Verify OpenGL 4.1 support:
  ```bash
  glxinfo | grep "OpenGL version"
  ```
- Check shader compilation errors in console output

#### No Audio
- Verify OpenAL installation:
  ```bash
  aplay -l  # List audio devices
  ```
- Check system audio settings
- Test with headphones

#### Performance Issues
- Verify graphics drivers are up to date
- Check system resource usage:
  ```bash
  htop  # Linux
  # Task Manager on Windows
  # Activity Monitor on macOS
  ```
- Try reducing graphics quality in settings

### VR-Specific Issues

#### VR Not Detected
- Ensure SteamVR is running (Windows)
- Install OpenXR runtime (Linux)
- Check VR headset connection
- Verify VR runtime permissions

#### Motion Sickness
- Reduce movement speed
- Enable teleportation movement
- Increase frame rate
- Adjust FOV settings

### Getting Help

If you encounter issues not covered here:

1. **Check the logs**: Run with `--debug` flag for detailed logging
2. **Search GitHub Issues**: Check if the issue is already reported
3. **Create an issue**: Include system information, error messages, and steps to reproduce
4. **Join Discord**: Get help from the community in real-time

### System Information Collection

To help diagnose issues, please provide:

```bash
# System information
uname -a
lscpu
free -h
glxinfo | grep OpenGL
aplay -l
```

For Windows, include:
- Windows version
- Graphics card model and driver version
- Visual Studio version
- Direct output of `dxdiag`

---

For additional support, visit [https://enuanza.math/support](https://enuanza.math/support)