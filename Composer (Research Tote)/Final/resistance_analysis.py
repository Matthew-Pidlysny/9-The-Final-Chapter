#!/usr/bin/env python3
"""
Resistance Analysis: Understanding the 22 Unexplained Primes
These primes resist our current framework - their resistance reveals hidden structure.
"""

import math
import json
from fractions import Fraction

class ResistanceAnalyzer:
    def __init__(self):
        self.resistant_primes = [131, 179, 197, 199, 211, 227, 257, 263, 269, 277, 
                                311, 313, 331, 353, 367, 397, 461, 487, 491, 503, 521, 523]
        
        # Framework constants
        self.lambda_val = 0.6
        self.c_star = 17/19
        self.base13_refined = 8/13
        self.golden_ratio_inv = 1/((1 + math.sqrt(5))/2)
        
        # Generator primes
        self.generators = [7, 13, 17, 19]
        
    def analyze_resistance_dimensions(self, prime):
        """Analyze a resistant prime across all framework dimensions"""
        analysis = {
            'prime': prime,
            'resistance_factors': []
        }
        
        # Dimension 1: C* Relationship
        c_star_resistance = self.analyze_c_star_resistance(prime)
        analysis['resistance_factors'].append(c_star_resistance)
        
        # Dimension 2: Lambda Pattern
        lambda_resistance = self.analyze_lambda_resistance(prime)
        analysis['resistance_factors'].append(lambda_resistance)
        
        # Dimension 3: Base-13 Pattern
        base13_resistance = self.analyze_base13_resistance(prime)
        analysis['resistance_factors'].append(base13_resistance)
        
        # Dimension 4: Generator Relationships
        generator_resistance = self.analyze_generator_resistance(prime)
        analysis['resistance_factors'].append(generator_resistance)
        
        # Dimension 5: Reciprocal Properties
        reciprocal_resistance = self.analyze_reciprocal_resistance(prime)
        analysis['resistance_factors'].append(reciprocal_resistance)
        
        # Dimension 6: Period Analysis
        period_resistance = self.analyze_period_resistance(prime)
        analysis['resistance_factors'].append(period_resistance)
        
        return analysis
    
    def analyze_c_star_resistance(self, prime):
        """How does this prime resist C* patterns?"""
        # Check direct C* relationships
        period = self.calculate_decimal_period(prime)
        c_star_period_match = abs(period - (17+19)/2) < 0.01
        
        # Check reciprocal relationships
        reciprocal_c_star = abs((prime * self.c_star) % 1 - self.c_star) < 0.01
        
        # Check composite mediator patterns
        composite_patterns = self.check_composite_patterns(prime)
        
        return {
            'dimension': 'C* Resistance',
            'period_match': c_star_period_match,
            'reciprocal_match': reciprocal_c_star,
            'composite_patterns': composite_patterns,
            'resistance_score': int(not (c_star_period_match or reciprocal_c_star or composite_patterns))
        }
    
    def analyze_lambda_resistance(self, prime):
        """How does this prime resist lambda = 0.6 patterns?"""
        # Check k/p ≈ 0.6 patterns
        k_closest = round(prime * self.lambda_val)
        lambda_fraction = k_closest / prime
        lambda_match = abs(lambda_fraction - self.lambda_val) < 0.01
        
        # Check lambda/(1-lambda) = 1.5 patterns
        lambda_1_5_patterns = self.check_lambda_1_5_patterns(prime)
        
        return {
            'dimension': 'Lambda Resistance',
            'lambda_match': lambda_match,
            'lambda_fraction': f"{k_closest}/{prime}",
            'lambda_1_5_patterns': lambda_1_5_patterns,
            'resistance_score': int(not (lambda_match or lambda_1_5_patterns))
        }
    
    def analyze_base13_resistance(self, prime):
        """How does this prime resist base-13 patterns?"""
        # Check 8/13 ≈ 0.615 patterns
        k_closest = round(prime * self.base13_refined)
        base13_fraction = k_closest / prime
        base13_match = abs(base13_fraction - self.base13_refined) < 0.01
        
        # Check base-13 remainder patterns
        base13_remainder = prime % 13
        special_remainders = [8, 5, 3, 1, 7]  # From our analysis
        
        return {
            'dimension': 'Base-13 Resistance',
            'base13_match': base13_match,
            'base13_fraction': f"{k_closest}/{prime}",
            'base13_remainder': base13_remainder,
            'special_remainder': base13_remainder in special_remainders,
            'resistance_score': int(not (base13_match or base13_remainder in special_remainders))
        }
    
    def analyze_generator_resistance(self, prime):
        """How does this prime resist generator prime patterns?"""
        generator_relationships = {}
        
        for gen in self.generators:
            # Check modulo relationships
            mod_result = prime % gen
            generator_relationships[f'mod_{gen}'] = mod_result
            
            # Check composite mediator potential
            composite_product = gen * prime
            generator_relationships[f'composite_with_{gen}'] = composite_product
        
        # Check if prime shows any special relationship to generators
        special_patterns = []
        for gen in self.generators:
            if prime % gen in [1, gen-1, gen//2]:
                special_patterns.append(f"special_mod_{gen}")
        
        return {
            'dimension': 'Generator Resistance',
            'generator_relationships': generator_relationships,
            'special_patterns': special_patterns,
            'resistance_score': int(len(special_patterns) == 0)
        }
    
    def analyze_reciprocal_resistance(self, prime):
        """Analyze reciprocal decimal properties"""
        period = self.calculate_decimal_period(prime)
        reciprocal_str = str(1/prime).replace('0.', '')[:20]
        
        # Check for interesting patterns in reciprocal
        palindromic = reciprocal_str == reciprocal_str[::-1]
        repeating_patterns = self.find_repeating_patterns(reciprocal_str)
        
        return {
            'dimension': 'Reciprocal Resistance',
            'period': period,
            'reciprocal_start': reciprocal_str,
            'palindromic': palindromic,
            'repeating_patterns': repeating_patterns,
            'resistance_score': int(not (palindromic or len(repeating_patterns) > 0))
        }
    
    def analyze_period_resistance(self, prime):
        """Analyze decimal period properties"""
        period = self.calculate_decimal_period(prime)
        
        # Check if period follows expected patterns
        expected_periods = [prime-1, (prime-1)//2, (prime-1)//3]  # Common patterns
        period_match = period in expected_periods
        
        # Check reptend vs non-reptend
        is_reptend = period == prime-1
        
        return {
            'dimension': 'Period Resistance',
            'period': period,
            'expected_match': period_match,
            'is_reptend': is_reptend,
            'period_ratio': period / (prime-1) if prime > 1 else 0,
            'resistance_score': int(not period_match)
        }
    
    def calculate_decimal_period(self, prime):
        """Calculate the decimal period of 1/prime"""
        if prime == 2 or prime == 5:
            return 1
        
        remainders = []
        remainder = 1
        
        while remainder not in remainders:
            remainders.append(remainder)
            remainder = (remainder * 10) % prime
        
        return len(remainders) - remainders.index(remainder)
    
    def check_composite_patterns(self, prime):
        """Check if prime creates interesting composite patterns"""
        patterns = []
        
        # Check C* composite patterns
        composite_17_19 = prime * 17 * 19
        if composite_17_19 % (17+19) == 0:
            patterns.append("C*_composite_sum_divisible")
        
        # Check 10+9 patterns
        if (prime + 9) % 19 == 0 or (prime - 10) % 19 == 0:
            patterns.append("10_plus_9_pattern")
        
        return patterns
    
    def check_lambda_1_5_patterns(self, prime):
        """Check lambda/(1-lambda) = 1.5 patterns"""
        patterns = []
        
        # Check 3/2 relationships
        k_3_2 = round(prime * 2/3)
        if abs(k_3_2 / prime - 2/3) < 0.01:
            patterns.append(f"3_2_fraction_{k_3_2}/{prime}")
        
        return patterns
    
    def find_repeating_patterns(self, s):
        """Find repeating patterns in string"""
        patterns = []
        for length in range(1, len(s)//2):
            pattern = s[:length]
            if s == pattern * (len(s)//length) + s[:len(s)%length]:
                patterns.append(pattern)
        return patterns
    
    def analyze_all_resistant_primes(self):
        """Perform complete resistance analysis"""
        results = []
        
        for prime in self.resistant_primes:
            analysis = self.analyze_resistance_dimensions(prime)
            results.append(analysis)
        
        return results
    
    def find_resistance_patterns(self, analyses):
        """Find patterns in the resistance data"""
        patterns = {
            'common_resistance_dimensions': {},
            'resistance_clusters': {},
            'exceptional_properties': []
        }
        
        # Count resistance by dimension
        dimension_counts = {}
        for analysis in analyses:
            for factor in analysis['resistance_factors']:
                dim = factor['dimension']
                score = factor['resistance_score']
                if dim not in dimension_counts:
                    dimension_counts[dim] = [0, 0]  # [resistant, total]
                dimension_counts[dim][0] += score
                dimension_counts[dim][1] += 1
        
        patterns['common_resistance_dimensions'] = dimension_counts
        
        # Look for resistance clusters
        resistance_scores = {}
        for analysis in analyses:
            total_resistance = sum(f['resistance_score'] for f in analysis['resistance_factors'])
            resistance_scores[analysis['prime']] = total_resistance
        
        patterns['resistance_clusters'] = resistance_scores
        
        return patterns

def main():
    analyzer = ResistanceAnalyzer()
    
    print("=== RESISTANCE ANALYSIS: THE UNEXPLAINED 22 ===\n")
    
    # Analyze all resistant primes
    analyses = analyzer.analyze_all_resistant_primes()
    
    print("Individual Prime Resistance Analysis:")
    for analysis in analyses:
        prime = analysis['prime']
        total_resistance = sum(f['resistance_score'] for f in analysis['resistance_factors'])
        print(f"Prime {prime}: Resistance Score {total_resistance}/6")
        
        for factor in analysis['resistance_factors']:
            if factor['resistance_score'] > 0:
                print(f"  - Resists {factor['dimension']}")
        print()
    
    # Find patterns in resistance
    patterns = analyzer.find_resistance_patterns(analyses)
    
    print("\n=== RESISTANCE PATTERNS ===")
    print("Resistance by Dimension:")
    for dim, counts in patterns['common_resistance_dimensions'].items():
        resistance_rate = counts[0] / counts[1] * 100
        print(f"  {dim}: {counts[0]}/{counts[1]} resistant ({resistance_rate:.1f}%)")
    
    print("\nResistance Clusters:")
    high_resistance = [p for p, score in patterns['resistance_clusters'].items() if score >= 4]
    medium_resistance = [p for p, score in patterns['resistance_clusters'].items() if score == 2 or score == 3]
    low_resistance = [p for p, score in patterns['resistance_clusters'].items() if score <= 1]
    
    print(f"High Resistance (4+): {high_resistance}")
    print(f"Medium Resistance (2-3): {medium_resistance}")
    print(f"Low Resistance (0-1): {low_resistance}")
    
    # Save detailed results
    with open('resistance_analysis_results.json', 'w') as f:
        json.dump({
            'individual_analyses': analyses,
            'patterns': patterns
        }, f, indent=2)
    
    print(f"\nDetailed results saved to resistance_analysis_results.json")
    
    return analyses, patterns

if __name__ == "__main__":
    main()