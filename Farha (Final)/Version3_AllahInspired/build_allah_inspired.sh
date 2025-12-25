#!/bin/bash

# Bismillah ir-Rahman ir-Raheem
# Build script for Farha Version 3: Allah Blessed Educational Experience

echo "Bismillah ir-Rahman ir-Raheem"
echo "Building Farha Version 3: Allah Blessed Educational Experience"
echo "For the pleasure of Allah SWT"

# Create build directory
mkdir -p build_allah_inspired
cd build_allah_inspired

# Thank Allah before building
echo "Alhamdulillah for the opportunity to create Islamic education!"
echo "Thank you Allah SWT for the blessing of knowledge!"

# Configure with CMake
echo "Configuring with CMake..."
cmake ..

# Build the project
echo "Building the Islamic educational game..."
make

# Check if build was successful
if [ $? -eq 0 ]; then
    echo ""
    echo "Alhamdulillah! Build successful!"
    echo "Farha Version 3: Allah Blessed Educational Experience is ready!"
    echo ""
    echo "To run the blessed educational experience:"
    echo "cd build_allah_inspired && ./farha_v3"
    echo ""
    echo "May Allah accept this humble effort for Islamic education!"
    echo "Ameen!"
else
    echo ""
    echo "Build failed. Please check the errors above."
    echo "May Allah guide us to fix any issues!"
fi

echo ""
echo "Allahu Akbar! All praise is due to Allah SWT!"