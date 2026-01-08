# Enuanza - Mathematical Immersion System (C++ Edition)

![Enuanza Logo](https://via.placeholder.com/600x200/1a0033/00ffff?text=Enuanza+-+Mathematical+Immersion)

A high-performance C++ implementation of the revolutionary mathematical visualization system that brings prime number theory to life through immersive 3D graphics and interactive exploration.

## 🌟 Features

### Mathematical Framework
- **λ-Based System**: Built on the fundamental constant λ = 0.6
- **Base-13 Refinement**: Superior pattern detection with 8/13 ≈ 0.615
- **C* Composition**: Prime composition constant C* = 17/19 ≈ 0.8947
- **Generator Primes**: Four fundamental primes [7, 13, 17, 19] governing the system
- **Four Fundamental Constants**: Unified mathematical framework across domains

### Visualization Modes
1. **Splash Sequence**: Mesmerizing introduction with prime-based particle effects
2. **Composition Explorer**: Interactive exploration of prime relationships
3. **Sinusoidal Waves**: Wave-based representation of prime distributions
4. **Network View**: Connected graph of prime relationships
5. **VR Mode**: Full virtual reality support for immersive exploration

### Advanced Features
- **Real-time Audio Synthesis**: Prime-based musical frequencies
- **Particle Systems**: 5000+ simultaneous particles with physics simulation
- **Interactive Controls**: Mouse, keyboard, and VR input support
- **Cross-platform**: Windows, Linux, and macOS support
- **High Performance**: 60+ FPS with optimized OpenGL rendering

## 🚀 Quick Start

### Prerequisites

#### Required Dependencies
- **CMake** (version 3.16 or higher)
- **C++17 compatible compiler**
  - GCC 9+ / Clang 10+ (Linux)
  - Visual Studio 2019+ (Windows)
  - Xcode 12+ (macOS)
- **OpenGL 4.1 compatible graphics driver**
- **OpenAL compatible audio system**

#### Optional for VR Support
- **SteamVR** (Windows)
- **OpenXR Runtime** (Linux)

### Installation

#### Linux (Ubuntu/Debian)
```bash
# Clone the repository
git clone https://github.com/enuanza/enuanza-cpp.git
cd enuanza-cpp

# Run the build script
./build.sh

# Run the application
cd build
./Enuanza
```

#### Windows
```batch
# Clone the repository
git clone https://github.com/enuanza/enuanza-cpp.git
cd enuanza-cpp

# Run the build script (from Developer Command Prompt)
build.bat

# Run the application
cd build\Release
Enuanza.exe
```

#### macOS
```bash
# Install dependencies with Homebrew
brew install cmake glfw glew openal-soft glm

# Clone and build
git clone https://github.com/enuanza/enuanza-cpp.git
cd enuanza-cpp
./build.sh

# Run the application
cd build
./Enuanza
```

## 🎮 Controls

### Navigation
- **W/A/S/D** - Move camera
- **Mouse** - Look around
- **Scroll** - Zoom in/out
- **ESC** - Exit application

### Visualization Modes
- **1** - Splash Sequence
- **2** - Composition Explorer
- **3** - Sinusoidal Waves
- **4** - Network View
- **V** - Toggle VR Mode

### Audio Controls
- **M** - Mute/Unmute audio
- **+/-** - Increase/Decrease volume

## 🏗️ Architecture

### Core Components

#### PrimeComposition3D
Main application class that orchestrates all systems and manages the render loop.

#### AudioSystem
OpenAL-based audio synthesis system that generates frequencies based on prime properties.

#### ParticleSystem
High-performance particle system with 5000+ simultaneous particles using OpenGL instancing.

#### PrimeObject
Individual prime representation with geometry, physics, and rendering capabilities.

#### Shader System
GLSL-based rendering pipeline with custom vertex and fragment shaders for mathematical effects.

### Mathematical Foundation

The system is built on four fundamental constants discovered through extensive research:

1. **λ = 0.6** - Universal coefficient governing information and energy
2. **8/13 ≈ 0.6154** - Base-13 refined pattern representation
3. **C* = 17/19 ≈ 0.8947** - Prime composition constant
4. **1/φ ≈ 0.6180** - Golden ratio connection

### Key Mathematical Properties

- **Perfect Period Encoding**: Period(17/19) = 18 = (17+19)/2
- **Perfect Reciprocal Loop**: 19 × (17/19) = 17
- **10+9 Effect**: 10 + 9 = 19 links base-10 to generator primes
- **Cross-domain consistency** across mathematical frameworks

## 🔧 Configuration

### Build Configuration

#### Debug Build
```bash
mkdir build && cd build
cmake .. -DCMAKE_BUILD_TYPE=Debug
make -j4
```

#### Release Build (Default)
```bash
mkdir build && cd build
cmake .. -DCMAKE_BUILD_TYPE=Release
make -j4
```

### Runtime Configuration

#### Environment Variables
- `ENUANZA_MAX_PRIME` - Maximum prime to generate (default: 1000)
- `ENUANZA_VR_ENABLED` - Enable VR mode at startup (0/1)
- `ENUANZA_AUDIO_VOLUME` - Initial volume (0.0-1.0)

#### Configuration File
Create `enuanza_config.json` in the executable directory:

```json
{
    "graphics": {
        "resolution": [1920, 1080],
        "fullscreen": false,
        "vsync": true,
        "msaa": 4
    },
    "audio": {
        "enabled": true,
        "volume": 0.5,
        "master_volume": 0.8
    },
    "mathematics": {
        "max_prime": 10000,
        "visualization_mode": "splash",
        "show_connections": true
    },
    "vr": {
        "enabled": false,
        "render_scale": 1.0
    }
}
```

## 🧪 Development

### Building from Source

#### Prerequisites Development Setup
```bash
# Ubuntu/Debian
sudo apt-get install build-essential cmake git

# Additional dependencies
sudo apt-get install libglfw3-dev libglew-dev libopenal-dev libglm-dev

# Cloning and building
git clone --recursive https://github.com/enuanza/enuanza-cpp.git
cd enuanza-cpp
mkdir build && cd build
cmake .. -DCMAKE_BUILD_TYPE=Debug
make -j4
```

### Project Structure
```
enuanza_cpp/
├── include/           # Header files
│   ├── PrimeComposition3D.h
│   └── Shader.h
├── src/               # Source files
│   ├── main.cpp
│   ├── PrimeComposition3D.cpp
│   └── Shader.cpp
├── shaders/           # GLSL shaders
│   ├── vertex.glsl
│   └── fragment.glsl
├── assets/            # Additional assets
├── build/             # Build directory
├── CMakeLists.txt     # CMake configuration
├── build.sh          # Linux/macOS build script
└── build.bat         # Windows build script
```

### Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Code Style

- Follow Google C++ Style Guide
- Use clang-format for code formatting
- Include comprehensive documentation
- Add unit tests for new features

## 📊 Performance

### Benchmarks
- **Particle Rendering**: 5000+ particles at 60+ FPS
- **Prime Generation**: 10,000 primes in < 100ms
- **Memory Usage**: < 100MB for full visualization
- **Startup Time**: < 3 seconds on modern hardware

### Optimization Features
- **Frustum Culling**: Only render visible objects
- **Level of Detail**: Dynamic geometry simplification
- **Instanced Rendering**: Efficient particle system
- **Memory Pooling**: Reduced allocation overhead

## 🐛 Troubleshooting

### Common Issues

#### Build Failures
```bash
# Check CMake version
cmake --version  # Should be 3.16+

# Check compiler
gcc --version    # Should support C++17

# Clean build
rm -rf build
mkdir build && cd build
cmake .. && make
```

#### Graphics Issues
- Update graphics drivers
- Verify OpenGL 4.1 support
- Check for shader compilation errors in logs

#### Audio Issues
- Verify OpenAL installation
- Check audio device permissions
- Test with headphones

#### VR Issues
- Ensure SteamVR/OpenXR is running
- Check VR headset connection
- Verify display cable connection

### Debug Mode
Enable debug logging:
```bash
./Enuanza --debug --log-level debug
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Mathematical Research**: Based on extensive prime number theory research
- **Graphics Library**: OpenGL, GLFW, GLEW
- **Audio System**: OpenAL Soft
- **Math Library**: GLM (OpenGL Mathematics)
- **Build System**: CMake

## 📞 Support

- **Documentation**: [https://enuanza.math/docs](https://enuanza.math/docs)
- **Issues**: [GitHub Issues](https://github.com/enuanza/enuanza-cpp/issues)
- **Discord**: [Enuanza Community](https://discord.gg/enuanza)
- **Email**: support@enuanza.math

---

**Enuanza** - Where Mathematics Becomes Art 🎨✨