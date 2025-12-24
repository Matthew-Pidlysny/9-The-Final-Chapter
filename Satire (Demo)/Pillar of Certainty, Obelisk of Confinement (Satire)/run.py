#!/usr/bin/env python3
"""
Quick start script for The TransRational Airline
"""

import sys
import os

# Add src directory to path
src_path = os.path.join(os.path.dirname(__file__), 'src')
sys.path.insert(0, src_path)

try:
    from main import main
    print("🛫 Starting The TransRational Airline...")
    main()
except ImportError as e:
    print(f"Import error: {e}")
    print("Please ensure you're running from the transrational_airline directory")
except Exception as e:
    print(f"Error starting application: {e}")