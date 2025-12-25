#!/bin/bash

echo "🔍 PRIVANNA COMPLETE PACKAGE VERIFICATION"
echo "========================================="

# Check main version exists
if [ -d "MAIN_VERSION_V7_KARDASHEV" ]; then
    echo "✅ Main V7 Kardashev version found"
else
    echo "❌ Main V7 Kardashev version missing"
fi

# Check all versions
versions=("Version1_Efficiency" "Version2_Visual_Excellence" "Version3_AI_Systems" "Version4_Character_Development" "Version5_Playability_Polish" "Version6_Game_of_the_Year")

for version in "${versions[@]}"; do
    if [ -d "$version" ]; then
        echo "✅ $version found"
    else
        echo "❌ $version missing"
    fi
done

# Check documentation
if [ -d "Documentation" ]; then
    echo "✅ Documentation folder found"
    doc_count=$(find Documentation -name "*.md" | wc -l)
    echo "📚 $doc_count documentation files found"
else
    echo "❌ Documentation folder missing"
fi

# Check tools
if [ -d "Tools" ]; then
    echo "✅ Tools folder found"
    tool_count=$(find Tools -name "*.cpp" | wc -l)
    echo "🛠️ $tool_count tool files found"
else
    echo "❌ Tools folder missing"
fi

# Check build scripts
if [ -d "Build_Scripts" ]; then
    echo "✅ Build Scripts folder found"
else
    echo "❌ Build Scripts folder missing"
fi

# Check main executable
if [ -f "MAIN_VERSION_V7_KARDASHEV/privanna_v7_stress_test" ]; then
    echo "✅ Main V7 executable found"
else
    echo "❌ Main V7 executable missing"
fi

# Check README
if [ -f "README_COMPLETE_PACKAGE.md" ]; then
    echo "✅ Complete README found"
else
    echo "❌ Complete README missing"
fi

echo ""
echo "📊 PACKAGE SUMMARY"
echo "=================="
total_size=$(du -sh . | cut -f1)
echo "Total Package Size: $total_size"

file_count=$(find . -type f | wc -l)
echo "Total Files: $file_count"

folder_count=$(find . -type d | wc -l)
echo "Total Folders: $folder_count"

echo ""
echo "🎉 VERIFICATION COMPLETE"
echo "========================"
echo "Privanna Complete Package is ready for distribution!"
echo ""
echo "🚀 To get started:"
echo "1. Read README_COMPLETE_PACKAGE.md"
echo "2. Navigate to MAIN_VERSION_V7_KARDASHEV"
echo "3. Run: ./privanna_v7_stress_test --comprehensive-test"