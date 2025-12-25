#!/bin/bash

# Farha Enhanced Game Build Script
echo "🌟 Building Farha Enhanced - 200+ Islamic Features 🌟"
echo "===================================================="

# Create build directory
echo "📁 Creating enhanced build directory..."
mkdir -p build
cd build

# Configure with CMake
echo "⚙️  Configuring enhanced version with CMake..."
cmake .. -DCMAKE_BUILD_TYPE=Release

if [ $? -ne 0 ]; then
    echo "❌ CMake configuration failed!"
    exit 1
fi

# Build the project
echo "🔨 Building the enhanced game..."
make -j$(nproc)

if [ $? -ne 0 ]; then
    echo "❌ Build failed!"
    exit 1
fi

# Copy executable to main directory
echo "📦 Copying enhanced executable..."
cp bin/farha_enhanced ../farha_v2

echo ""
echo "🎉 Enhanced build completed successfully!"
echo "🎮 Run the enhanced game with: ./farha_v2"
echo ""
echo "📚 Enhanced Islamic content included:"
echo "  • 50+ Extended Quranic verses with authentic context"
echo "  • 30+ Verified Hadith with complete authentication"
echo "  • 32+ Islamic concepts with practical applications"
echo "  • 15+ Enhanced historical territories"
echo "  • 10+ Battles with Islamic moral lessons"
echo "  • 70+ Achievement badges for Islamic character"
echo "  • 200+ Total authentic Islamic enhancements"
echo ""
echo "🌟 Experience comprehensive Islamic education!"
echo "🕌 Authentic • Educational • Character Building"