#!/usr/bin/env python3
"""
Composer Framework Diagnostic Tool
Investigate the actual structure and claims
"""

import os
import sys
from pathlib import Path

def analyze_composer_folder():
    """Deep analysis of Composer folder structure"""
    print("🔍 COMPOSER FRAMEWORK DIAGNOSTIC ANALYSIS")
    print("=" * 60)
    
    # Find Composer folder
    composer_path = None
    for root, dirs, files in os.walk("/workspace"):
        if "Composer" in dirs or "Research Tote" in dirs:
            composer_path = os.path.join(root, "Composer" if "Composer" in dirs else "Research Tote")
            break
    
    if not composer_path:
        print("❌ Composer/Research Tote folder not found!")
        return
    
    print(f"📁 Found Composer folder at: {composer_path}")
    
    # List all files
    print("\n📄 All files in Composer folder:")
    all_files = []
    for root, dirs, files in os.walk(composer_path):
        for file in files:
            file_path = os.path.join(root, file)
            rel_path = os.path.relpath(file_path, composer_path)
            all_files.append(rel_path)
            print(f"  {rel_path}")
    
    print(f"\n📊 Total files found: {len(all_files)}")
    
    # Look for key files
    key_files = [f for f in all_files if any(keyword in f.lower() for keyword in ['readme', 'main', 'core', 'framework', 'validation', 'test'])]
    if key_files:
        print(f"\n🎯 Key files identified:")
        for f in key_files:
            print(f"  {f}")
    
    # Examine main content files
    print(f"\n📖 Examining main content files...")
    for file in all_files[:10]:  # First 10 files
        full_path = os.path.join(composer_path, file)
        try:
            with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                
            print(f"\n📄 {file}:")
            print(f"  Size: {len(content)} characters")
            print(f"  First 200 chars: {content[:200].strip()}")
            
            # Look for C* mentions
            if "17/19" in content or "C*" in content:
                print("  🎯 Contains C* references!")
                
            # Look for 0.6 pattern
            if "0.6" in content:
                print("  🎯 Contains 0.6 pattern references!")
                
        except Exception as e:
            print(f"  ❌ Error reading: {e}")
    
    return composer_path, all_files

def examine_original_claims():
    """Examine the original claims from the research"""
    print(f"\n🎯 ORIGINAL CLAIMS ANALYSIS")
    print("-" * 40)
    
    # Check if we have any documentation files
    docs = [f for f in os.listdir("/workspace") if f.endswith('.md') and 'composer' in f.lower()]
    
    if docs:
        print(f"Found documentation files: {docs}")
        for doc in docs:
            print(f"\n📄 Examining {doc}:")
            with open(f"/workspace/{doc}", 'r') as f:
                content = f.read()
                
            # Look for specific claims
            if "98.13%" in content:
                print("  📊 Found 98.13% claim")
            if "76.31%" in content:
                print("  📊 Found 76.31% claim")
            if "0.6" in content:
                print("  📊 Found 0.6 pattern references")
                
    else:
        print("No composer documentation found in workspace")

def test_basic_claims():
    """Test the most basic claims to understand the framework"""
    print(f"\n🧪 TESTING BASIC CLAIMS")
    print("-" * 40)
    
    # Test 1: What is the actual period relationship?
    print("1. Testing period relationship...")
    
    # Calculate periods for small primes
    def reptend_period(p):
        if p == 2 or p == 5:
            return 1
        period = 1
        remainder = 10 % p
        while remainder != 1:
            remainder = (remainder * 10) % p
            period += 1
        return period
    
    primes = [7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
    
    for p in primes:
        period = reptend_period(p)
        print(f"  Prime {p}: period {period}")
        
        # Check if period equals (17+19)/2 = 18
        if period == 18:
            print(f"    🎯 Period matches 18!")
    
    # Test 2: What is the actual 0.6 pattern?
    print(f"\n2. Testing 0.6 pattern...")
    
    for p in primes:
        # Test k/p ≈ 0.6
        for k in range(1, p):
            frac = k / p
            if abs(frac - 0.6) < 0.01:
                print(f"  Prime {p}: {k}/{p} = {frac:.4f} ≈ 0.6 🎯")
                break
        else:
            print(f"  Prime {p}: No 0.6 fraction found")
    
    # Test 3: What about 17 and 19 specifically?
    print(f"\n3. Testing primes 17 and 19...")
    
    p17 = 17
    p19 = 19
    
    period_17 = reptend_period(p17)
    period_19 = reptend_period(p19)
    
    print(f"  Prime 17: period {period_17}")
    print(f"  Prime 19: period {period_19}")
    print(f"  (17+19)/2 = {(17+19)/2}")
    print(f"  17/19 = {17/19:.6f}")
    
    # Check if period_19 equals 18
    if period_19 == 18:
        print(f"  🎯 Prime 19 has period 18 = (17+19)/2!")

def main():
    print("🔍 COMPOSER FRAMEWORK EMERGENCY DIAGNOSTIC")
    print("=" * 60)
    
    # Analyze the actual folder structure
    composer_path, files = analyze_composer_folder()
    
    # Examine original claims
    examine_original_claims()
    
    # Test basic understanding
    test_basic_claims()
    
    print(f"\n🚨 DIAGNOSTIC COMPLETE")
    print("Need to revise understanding based on actual framework structure")

if __name__ == "__main__":
    main()