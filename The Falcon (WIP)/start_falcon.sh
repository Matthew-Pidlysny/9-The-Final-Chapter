#!/bin/bash
# The Falcon Press Office Startup Script

echo "🚀 Starting The Falcon Press Office..."

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed"
    exit 1
fi

# Check if required files exist
if [ ! -f "falcon_press_office.py" ]; then
    echo "❌ falcon_press_office.py not found"
    exit 1
fi

# Start the application
echo "🎯 Launching The Falcon Press Office..."
python3 falcon_press_office.py
