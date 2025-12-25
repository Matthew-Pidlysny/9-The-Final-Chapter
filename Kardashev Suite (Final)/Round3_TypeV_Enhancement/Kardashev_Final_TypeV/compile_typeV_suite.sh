#!/bin/bash

# KARDASHEV TYPE V SUITE COMPILATION SCRIPT
# =========================================

echo "🔨 Compiling Kardashev Type V Suite..."

# Create build directory
mkdir -p build
cd build

# Compile Type V framework
echo "⚡ Compiling Type V Multiversal Framework..."
g++ -std=c++20 -I../Round1_Foundation -I../Round3_TypeV_Enhancement \
    ../Round3_TypeV_Enhancement/kardashev_typeV_multiversal.cpp \
    ../Round3_TypeV_Enhancement/implementation/k1v_typeV_industrial.cpp \
    -o kardashev_typev_suite \
    -pthread -lquantum -lmultiversal

echo "📚 Compiling Documentation..."
cd ../documentation
for tex_file in *.tex; do
    pdflatex "$tex_file"
    pdflatex "$tex_file"  # Second pass for references
done

echo "✅ Compilation completed!"
echo "📁 Executable: build/kardashev_typev_suite"
echo "📖 Documentation: documentation/*.pdf"

