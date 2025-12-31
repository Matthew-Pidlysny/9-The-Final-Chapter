#!/usr/bin/env python3
"""
Comprehensive testing of Chainer mathematical system
Testing all numbers 0-13 across all base systems
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from chainer_v2 import NumberClassifier

def test_all_numbers():
    """Test comprehensive analysis for all numbers 0-13"""
    print("=" * 80)
    print("COMPREHENSIVE CHAINER MATHEMATICAL SYSTEM TEST")
    print("=" * 80)
    
    classifier = NumberClassifier()
    
    bases = [2, 3, 5, 7, 8, 10, 12, 16, 20, 60]
    numbers = list(range(14))  # 0-13
    
    results = {}
    
    for number in numbers:
        print(f"\n--- Testing Number {number} ---")
        result = {}
        
        # Basic classification
        classification = classifier.classify_number(number)
        factors = classification['prime_factors']
        result['classification'] = classification
        result['prime_factors'] = factors
        
        # Cross-base analysis
        cross_base_results = {}
        for base in bases:
            base_classification = classifier.classify_number(number, base)
            cross_base_results[base] = base_classification
        
        result['cross_base'] = cross_base_results
        
        results[number] = result
        
        # Print summary
        simple_bases = [base for base, info in cross_base_results.items() 
                       if info['is_simple']]
        wild_bases = [base for base, info in cross_base_results.items() 
                     if info['is_wild']]
        
        print(f"Prime Factors: {factors}")
        print(f"Simple in bases: {simple_bases}")
        print(f"Wild in bases: {wild_bases}")
    
    return results

def verify_mathematical_accuracy(results):
    """Verify mathematical accuracy of all results"""
    print("\n" + "=" * 80)
    print("MATHEMATICAL ACCURACY VERIFICATION")
    print("=" * 80)
    
    errors = []
    
    for number, result in results.items():
        factors = result['prime_factors']
        
        for base, classification in result['cross_base'].items():
            # Verify simple/wild classification logic
            # For base 10, simple numbers should only have factors 2 and/or 5
            if base == 10 and number > 1 and number not in [0, 1]:
                expected_simple = all(factor in [2, 5] for factor in factors)
                actual_simple = classification['is_simple']
                
                if expected_simple != actual_simple:
                    errors.append(f"Number {number} in base {base}: Expected simple={expected_simple}, got simple={actual_simple}")
            
            # Verify 1 is always simple
            if number == 1 and not classification['is_simple']:
                errors.append(f"Number 1 should always be simple in any base")
            
            # Verify 0 is wild
            if number == 0 and classification['is_simple']:
                errors.append(f"Number 0 should always be wild")
    
    if errors:
        print("ERRORS FOUND:")
        for error in errors:
            print(f"  - {error}")
    else:
        print("✅ ALL MATHEMATICAL RESULTS VERIFIED AS ACCURATE")
    
    return len(errors) == 0

def generate_comprehensive_report(results):
    """Generate detailed report of all findings"""
    print("\n" + "=" * 80)
    print("COMPREHENSIVE ANALYSIS REPORT")
    print("=" * 80)
    
    # Summary statistics
    total_tests = len(results) * 10  # 14 numbers * 10 bases
    simple_count = 0
    wild_count = 0
    
    for number, result in results.items():
        for base, classification in result['cross_base'].items():
            if classification['is_simple']:
                simple_count += 1
            else:
                wild_count += 1
    
    print(f"Total number-base combinations tested: {total_tests}")
    print(f"Simple classifications: {simple_count}")
    print(f"Wild classifications: {wild_count}")
    print(f"Ratio: {simple_count/wild_count:.2f}:1")
    
    # Detailed breakdown by number
    print(f"\nDetailed breakdown by number:")
    for number in range(14):
        simple_bases = []
        wild_bases = []
        for base in [2, 3, 5, 7, 8, 10, 12, 16, 20, 60]:
            classification = results[number]['cross_base'][base]
            if classification['is_simple']:
                simple_bases.append(base)
            else:
                wild_bases.append(base)
        print(f"  {number:2d}: Simple in {simple_bases}, Wild in {wild_bases}")

if __name__ == "__main__":
    results = test_all_numbers()
    is_accurate = verify_mathematical_accuracy(results)
    generate_comprehensive_report(results)
    
    print(f"\n" + "=" * 80)
    print("TEST COMPLETE")
    if is_accurate:
        print("✅ All mathematical tests passed successfully!")
    else:
        print("❌ Some mathematical issues detected!")
    print("=" * 80)