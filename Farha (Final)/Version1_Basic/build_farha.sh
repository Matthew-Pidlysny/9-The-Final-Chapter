#!/bin/bash

# Farha Game Build Script
echo "🌟 Building Farha - Educational Caliphate Game 🌟"
echo "=================================================="

# Create build directory
echo "📁 Creating build directory..."
mkdir -p build
cd build

# Configure with CMake
echo "⚙️  Configuring with CMake..."
cmake .. -DCMAKE_BUILD_TYPE=Release

if [ $? -ne 0 ]; then
    echo "❌ CMake configuration failed!"
    exit 1
fi

# Build the project
echo "🔨 Building the game..."
make -j$(nproc)

if [ $? -ne 0 ]; then
    echo "❌ Build failed!"
    exit 1
fi

# Copy executable to main directory
echo "📦 Copying executable..."
cp bin/farha_game ../farha_v1

echo ""
echo "🎉 Build completed successfully!"
echo "🎮 Run the game with: ./farha_v1"
echo ""
echo "📚 Educational content included:"
echo "  • Rashiddun Caliphate history"
echo "  • 4 Qul (Quranic chapters)"
echo "  • Authentic Hadith"
echo "  • Historical battles"
echo ""
echo "🌟 Enjoy learning about Islamic history!"