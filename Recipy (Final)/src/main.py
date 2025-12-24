#!/usr/bin/env python3
"""
Recipy: Revolutionary Educational Framework for Grade 1 Mathematics
Python Implementation

Transforms advanced mathematical analyzer concepts into loving, 
child-centered learning experiences for Grade 1 students.

Author: Educational Revolution Team
License: Educational Love License
"""

import sys
import os
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent))

from recipy_app import RecipyApp

def main():
    """Main entry point for Recipy educational framework"""
    print("🌟 Welcome to Recipy - Where Math Meets Love! 🌟")
    print("=" * 60)
    
    try:
        app = RecipyApp()
        app.run()
    except KeyboardInterrupt:
        print("\n\n💖 Thank you for learning with Recipy! Come back soon!")
    except Exception as e:
        print(f"\n❌ Oops! Something went wrong: {e}")
        print("Let's try again together!")

if __name__ == "__main__":
    main()