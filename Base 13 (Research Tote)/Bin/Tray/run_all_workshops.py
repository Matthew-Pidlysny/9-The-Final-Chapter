"""
Main Test Runner for All Workshop Modules
This script runs all three workshop modules and provides a comprehensive summary.
"""

import sys
import subprocess

def run_workshop(module_name, description):
    """Run a single workshop module"""
    print("\n" + "=" * 70)
    print(f"RUNNING: {description}")
    print("=" * 70)
    
    try:
        result = subprocess.run(
            [sys.executable, module_name],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        print(result.stdout)
        
        if result.stderr:
            print("STDERR:", result.stderr)
        
        return result.returncode == 0
    
    except subprocess.TimeoutExpired:
        print(f"ERROR: {module_name} timed out after 30 seconds")
        return False
    except Exception as e:
        print(f"ERROR running {module_name}: {e}")
        return False

def main():
    """Run all workshop modules"""
    print("=" * 70)
    print("BASE 13 RESEARCH PROJECT - COMPREHENSIVE TESTING SUITE")
    print("=" * 70)
    print("\nThis testing suite validates all three mathematical systems:")
    print("  1. Base 13 Mathematical System")
    print("  2. Sequinor Tredecim System")
    print("  3. Remainder-Based Counting System")
    print("\nRunning all workshop modules...\n")
    
    workshops = [
        ("workshop_module_1_base13.py", "Workshop Module 1: Base 13 Fundamentals"),
        ("workshop_module_2_sequinor.py", "Workshop Module 2: Sequinor Tredecim Exploration"),
        ("workshop_module_3_integrated.py", "Workshop Module 3: Integrated Systems Analysis")
    ]
    
    results = []
    
    for module, description in workshops:
        success = run_workshop(module, description)
        results.append((description, success))
    
    # Print final summary
    print("\n" + "=" * 70)
    print("FINAL SUMMARY - ALL WORKSHOPS")
    print("=" * 70)
    
    passed = sum(1 for _, success in results if success)
    total = len(results)
    
    for description, success in results:
        status = "✓ PASSED" if success else "✗ FAILED"
        print(f"  {status}: {description}")
    
    print("\n" + "=" * 70)
    print(f"OVERALL RESULT: {passed}/{total} workshop modules passed")
    print("=" * 70)
    
    if passed == total:
        print("\n🎉 SUCCESS! All workshop modules passed!")
        return 0
    else:
        print(f"\n⚠️  WARNING: {total - passed} workshop module(s) failed")
        return 1

if __name__ == "__main__":
    sys.exit(main())