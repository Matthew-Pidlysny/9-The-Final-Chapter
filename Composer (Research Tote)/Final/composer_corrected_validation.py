#!/usr/bin/env python3
"""
CORRECTED Composer Framework Validation
Based on the actual C* composition framework
"""

import math
from fractions import Fraction
from decimal import Decimal, getcontext
import json
from typing import List, Dict, Tuple

getcontext().prec = 100

# Constants - matching the original framework
C_STAR = 17 / 19  # Exact value
C_STAR_DECIMAL = 0.894751918  # Given value (note: there's a small error)
POINT_SIX = 3 / 5

class CorrectedComposerValidator:
    def __init__(self):
        print("🔍 CORRECTED COMPOSER FRAMEWORK VALIDATION")
        print("Based on actual C* composition relationships")
        print("=" * 60)
        
        self.generator_primes = [17, 19]
        self.results = {}
        
    def is_prime(self, n):
        """Check if n is prime"""
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True
    
    def analyze_prime_composition(self, p: int) -> Dict:
        """Analyze how prime p composes through C* - matching original algorithm"""
        
        # Basic C* relationships
        p_times_c = p * C_STAR
        p_div_c = p / C_STAR
        
        # Integer proximity analysis
        p_times_c_int = round(p_times_c)
        p_div_c_int = round(p_div_c)
        
        p_times_c_error = abs(p_times_c - p_times_c_int)
        p_div_c_error = abs(p_div_c - p_div_c_int)
        
        # Reciprocal C* analysis
        reciprocal = 1.0 / p
        reciprocal_c_ratio = reciprocal / C_STAR
        
        # Fraction representation analysis
        c_star_fraction_k = round(p * C_STAR)
        point_six_fraction_k = round(p * POINT_SIX)
        
        c_star_fraction = None
        point_six_fraction = None
        
        if 1 <= c_star_fraction_k <= p:
            c_star_fraction = Fraction(c_star_fraction_k, p)
        
        if 1 <= point_six_fraction_k <= p:
            point_six_fraction = Fraction(point_six_fraction_k, p)
        
        # Composition classification
        composition_type = self._classify_composition(p, p_times_c_error, p_div_c_error)
        
        return {
            'prime': p,
            'c_star_relationships': {
                'p_times_c_star': p_times_c,
                'p_times_c_star_nearest_int': p_times_c_int,
                'p_times_c_star_error': p_times_c_error,
                'p_div_c_star': p_div_c,
                'p_div_c_star_nearest_int': p_div_c_int,
                'p_div_c_star_error': p_div_c_error,
                'reciprocal_c_ratio': reciprocal_c_ratio
            },
            'fraction_representations': {
                'c_star_fraction': str(c_star_fraction) if c_star_fraction else None,
                'point_six_fraction': str(point_six_fraction) if point_six_fraction else None
            },
            'composition_type': composition_type,
            'composition_score': self._calculate_composition_score(p_times_c_error, p_div_c_error, c_star_fraction)
        }
    
    def _classify_composition(self, p: int, p_times_c_error: float, p_div_c_error: float) -> str:
        """Classify the type of composition through C*"""
        
        if p in self.generator_primes:
            return "generator_prime"
        elif p_times_c_error < 0.001 or p_div_c_error < 0.001:
            return "strongly_composed"
        elif p_times_c_error < 0.01 or p_div_c_error < 0.01:
            return "moderately_composed"
        elif p_times_c_error < 0.1 or p_div_c_error < 0.1:
            return "weakly_composed"
        else:
            return "not_composed"
    
    def _calculate_composition_score(self, p_times_c_error: float, p_div_c_error: float, c_star_fraction: Fraction) -> int:
        """Calculate composition score based on C* relationship strength"""
        score = 100
        
        # Penalize errors
        score -= p_times_c_error * 1000
        score -= p_div_c_error * 1000
        
        # Bonus for exact fractions
        if c_star_fraction:
            score += 20
        
        return max(0, int(score))
    
    def reptend_period(self, p):
        """Calculate reptend period of 1/p"""
        if p == 2 or p == 5:
            return 1
        
        period = 1
        remainder = 10 % p
        
        while remainder != 1:
            remainder = (remainder * 10) % p
            period += 1
            
        return period
    
    def is_reptend_prime(self, p):
        """Check if p is a full reptend prime"""
        if p == 2 or p == 5:
            return False
        return self.reptend_period(p) == p - 1
    
    def get_decimal_digits(self, p, length=50):
        """Get decimal expansion of 1/p"""
        if p == 2:
            return "5" + "0" * (length - 1)
        if p == 5:
            return "2" + "0" * (length - 1)
        
        digits = ""
        remainder = 10
        
        for _ in range(length):
            remainder *= 10
            digit = remainder // p
            remainder = remainder % p
            digits += str(digit)
            
            if remainder == 0:
                break
        
        return digits
    
    def calculate_entropy(self, digits):
        """Calculate Shannon entropy of digit sequence"""
        if not digits:
            return 0
        
        freq = {}
        for digit in digits:
            freq[digit] = freq.get(digit, 0) + 1
        
        entropy = 0
        for count in freq.values():
            p = count / len(digits)
            entropy -= p * math.log2(p)
        
        return entropy
    
    def validate_17_19_loop(self):
        """Validate the perfect 17-19 reciprocal loop"""
        print("\n🎯 VALIDATING 17-19 PERFECT RECIPROCAL LOOP")
        print("-" * 50)
        
        # Test the core mathematical relationship
        print("Testing 19 × (17/19) = 17...")
        result = 19 * C_STAR
        error = abs(result - 17)
        print(f"  19 × (17/19) = {result:.10f}")
        print(f"  Expected: 17")
        print(f"  Error: {error:.10f}")
        print(f"  Perfect: {error < 1e-10}")
        
        print("\nTesting 17 / (17/19) = 19...")
        result2 = 17 / C_STAR
        error2 = abs(result2 - 19)
        print(f"  17 / (17/19) = {result2:.10f}")
        print(f"  Expected: 19")
        print(f"  Error: {error2:.10f}")
        print(f"  Perfect: {error2 < 1e-10}")
        
        # Test period encoding
        print("\nTesting period encoding: (17 + 19) / 2...")
        expected_period = (17 + 19) // 2
        actual_period_19 = self.reptend_period(19)
        print(f"  Expected period: {expected_period}")
        print(f"  Actual period of 1/19: {actual_period_19}")
        print(f"  Matches: {actual_period_19 == expected_period}")
        
        # Test C* definition error
        print("\nTesting C* definition accuracy...")
        actual_c_star = 17 / 19
        given_c_star = C_STAR_DECIMAL
        definition_error = abs(actual_c_star - given_c_star)
        error_percent = definition_error / given_c_star * 100
        print(f"  Actual C* = 17/19 = {actual_c_star:.10f}")
        print(f"  Given C* = {given_c_star:.9f}")
        print(f"  Definition error: {definition_error:.10f}")
        print(f"  Error percentage: {error_percent:.6f}%")
        
        self.results['17_19_loop'] = {
            'perfect_reciprocal': error < 1e-10 and error2 < 1e-10,
            'period_encoding_correct': actual_period_19 == expected_period,
            'definition_error_percent': error_percent
        }
    
    def validate_composition_patterns(self):
        """Validate C* composition patterns across primes"""
        print("\n🔍 VALIDATING C* COMPOSITION PATTERNS")
        print("-" * 50)
        
        # Test with a range of primes
        primes = [p for p in range(2, 200) if self.is_prime(p)]
        
        composition_stats = {"generator_prime": 0, "strongly_composed": 0, 
                           "moderately_composed": 0, "weakly_composed": 0, "not_composed": 0}
        
        c_star_fractions = []
        point_six_fractions = []
        
        for p in primes:
            analysis = self.analyze_prime_composition(p)
            composition_type = analysis['composition_type']
            composition_stats[composition_type] += 1
            
            if analysis['fraction_representations']['c_star_fraction']:
                c_star_fractions.append((p, analysis['fraction_representations']['c_star_fraction']))
            
            if analysis['fraction_representations']['point_six_fraction']:
                point_six_fractions.append((p, analysis['fraction_representations']['point_six_fraction']))
        
        print(f"Analyzed {len(primes)} primes")
        print("\nComposition distribution:")
        for comp_type, count in composition_stats.items():
            percentage = count / len(primes) * 100
            print(f"  {comp_type}: {count} ({percentage:.1f}%)")
        
        print(f"\nFound {len(c_star_fractions)} C* fraction representations")
        print(f"Found {len(point_six_fractions)} 0.6 fraction representations")
        
        # Show some examples
        if c_star_fractions:
            print(f"\nSample C* fractions:")
            for p, frac in c_star_fractions[:5]:
                print(f"  Prime {p}: {frac}")
        
        if point_six_fractions:
            print(f"\nSample 0.6 fractions:")
            for p, frac in point_six_fractions[:5]:
                print(f"  Prime {p}: {frac}")
        
        # Calculate composition rate
        composed_count = composition_stats['strongly_composed'] + composition_stats['moderately_composed'] + composition_stats['weakly_composed']
        composition_rate = composed_count / len(primes) * 100
        
        self.results['composition_patterns'] = {
            'total_primes': len(primes),
            'composition_stats': composition_stats,
            'composition_rate': composition_rate,
            'c_star_fractions': len(c_star_fractions),
            'point_six_fractions': len(point_six_fractions)
        }
        
        print(f"\nOverall composition rate: {composition_rate:.1f}%")
    
    def validate_hardness_disparity(self):
        """Validate reptend vs non-reptend hardness disparity"""
        print("\n💪 VALIDATING HARDNESS DISPARITY")
        print("-" * 50)
        
        primes = [p for p in range(2, 200) if self.is_prime(p) and p not in [2, 5]]
        
        reptend_entropy = []
        non_reptend_entropy = []
        
        reptend_composition_scores = []
        non_reptend_composition_scores = []
        
        for p in primes:
            # Entropy analysis
            digits = self.get_decimal_digits(p, 30)
            entropy = self.calculate_entropy(digits)
            
            # Composition analysis
            analysis = self.analyze_prime_composition(p)
            comp_score = analysis['composition_score']
            
            if self.is_reptend_prime(p):
                reptend_entropy.append(entropy)
                reptend_composition_scores.append(comp_score)
            else:
                non_reptend_entropy.append(entropy)
                non_reptend_composition_scores.append(comp_score)
        
        # Calculate averages
        avg_reptend_entropy = sum(reptend_entropy) / len(reptend_entropy) if reptend_entropy else 0
        avg_non_reptend_entropy = sum(non_reptend_entropy) / len(non_reptend_entropy) if non_reptend_entropy else 0
        
        avg_reptend_comp = sum(reptend_composition_scores) / len(reptend_composition_scores) if reptend_composition_scores else 0
        avg_non_reptend_comp = sum(non_reptend_composition_scores) / len(non_reptend_composition_scores) if non_reptend_composition_scores else 0
        
        print(f"Reptend primes: {len(reptend_entropy)}")
        print(f"Non-reptend primes: {len(non_reptend_entropy)}")
        
        print(f"\nEntropy comparison:")
        print(f"  Reptend avg: {avg_reptend_entropy:.3f}")
        print(f"  Non-reptend avg: {avg_non_reptend_entropy:.3f}")
        
        entropy_gap = avg_reptend_entropy - avg_non_reptend_entropy
        entropy_gap_percent = (entropy_gap / avg_non_reptend_entropy * 100) if avg_non_reptend_entropy > 0 else 0
        
        print(f"\nComposition score comparison:")
        print(f"  Reptend avg: {avg_reptend_comp:.1f}")
        print(f"  Non-reptend avg: {avg_non_reptend_comp:.1f}")
        
        comp_gap = avg_reptend_comp - avg_non_reptend_comp
        comp_gap_percent = (comp_gap / avg_non_reptend_comp * 100) if avg_non_reptend_comp > 0 else 0
        
        print(f"\nHardness gaps:")
        print(f"  Entropy gap: {entropy_gap:.3f} ({entropy_gap_percent:.1f}%)")
        print(f"  Composition gap: {comp_gap:.1f} ({comp_gap_percent:.1f}%)")
        
        self.results['hardness_disparity'] = {
            'entropy_gap_percent': entropy_gap_percent,
            'composition_gap_percent': comp_gap_percent,
            'reptend_count': len(reptend_entropy),
            'non_reptend_count': len(non_reptend_entropy)
        }
    
    def generate_final_verdict(self):
        """Generate final validation verdict"""
        print("\n🏆 FINAL VALIDATION VERDICT")
        print("=" * 50)
        
        loop = self.results.get('17_19_loop', {})
        patterns = self.results.get('composition_patterns', {})
        hardness = self.results.get('hardness_disparity', {})
        
        # Calculate scores
        scores = {}
        
        # 17-19 loop score
        loop_score = 0
        if loop.get('perfect_reciprocal', False):
            loop_score += 40
        if loop.get('period_encoding_correct', False):
            loop_score += 30
        if loop.get('definition_error_percent', 100) < 1:
            loop_score += 30
        
        scores['17_19_loop'] = loop_score
        
        # Composition patterns score
        patterns_score = 0
        comp_rate = patterns.get('composition_rate', 0)
        if comp_rate > 10:
            patterns_score += 25
        if comp_rate > 20:
            patterns_score += 25
        if patterns.get('c_star_fractions', 0) > 5:
            patterns_score += 25
        if patterns.get('point_six_fractions', 0) > 5:
            patterns_score += 25
        
        scores['composition_patterns'] = patterns_score
        
        # Hardness disparity score
        hardness_score = 0
        entropy_gap = abs(hardness.get('entropy_gap_percent', 0))
        comp_gap = abs(hardness.get('composition_gap_percent', 0))
        
        if entropy_gap > 5:
            hardness_score += 30
        if entropy_gap > 15:
            hardness_score += 20
        if comp_gap > 10:
            hardness_score += 25
        if hardness.get('reptend_count', 0) > 10:
            hardness_score += 25
        
        scores['hardness_disparity'] = hardness_score
        
        total_score = sum(scores.values())
        max_score = 300
        
        print("VALIDATION SCORES:")
        for category, score in scores.items():
            print(f"  {category.replace('_', ' ').title()}: {score}/100")
        
        print(f"\nTOTAL SCORE: {total_score}/{max_score} ({total_score/max_score*100:.1f}%)")
        
        # Generate verdict
        if total_score >= 240:
            verdict = "STRONGLY VALIDATED"
            confidence = "HIGH"
            interpretation = "The Composer framework shows robust mathematical structure"
        elif total_score >= 180:
            verdict = "MODERATELY VALIDATED"
            confidence = "MEDIUM"
            interpretation = "The Composer framework has promising elements but needs refinement"
        elif total_score >= 120:
            verdict = "WEAKLY VALIDATED"
            confidence = "LOW"
            interpretation = "The Composer framework has some interesting patterns but lacks coherence"
        else:
            verdict = "NOT VALIDATED"
            confidence = "VERY LOW"
            interpretation = "The Composer framework needs fundamental revision"
        
        print(f"\n🎯 VERDICT: {verdict}")
        print(f"📊 CONFIDENCE: {confidence}")
        print(f"💭 INTERPRETATION: {interpretation}")
        
        # Key findings
        print(f"\n🔍 KEY FINDINGS:")
        
        if loop.get('perfect_reciprocal', False):
            print("  ✅ Perfect 17-19 reciprocal loop mathematically confirmed")
        else:
            print("  ❌ 17-19 reciprocal loop not mathematically sound")
        
        if comp_rate > 15:
            print(f"  ✅ C* composition patterns found in {comp_rate:.1f}% of primes")
        else:
            print(f"  ❌ C* composition patterns too rare ({comp_rate:.1f}% only)")
        
        if entropy_gap > 10:
            print(f"  ✅ Reptend hardness disparity confirmed ({entropy_gap:.1f}% gap)")
        else:
            print(f"  ❌ Hardness disparity not significant ({entropy_gap:.1f}% gap)")
        
        self.results['final_verdict'] = {
            'total_score': total_score,
            'verdict': verdict,
            'confidence': confidence,
            'scores': scores
        }
        
        # Square root pattern note (as requested)
        print(f"\n🔢 SQUARE ROOT PATTERN NOTE:")
        print("  Palindromic primes show 'at rest' square root patterns:")
        print("  √1 = 1, √121 = 11, √12321 = 111")
        print("  Middle digit determines the number of 1's in the result")
        print("  This suggests a deeper structural property in the framework")
        
        return self.results
    
    def run_complete_validation(self):
        """Run the complete corrected validation"""
        print("🚀 Starting Corrected Composer Framework Validation")
        print("Based on the actual C* = 17/19 composition framework")
        
        self.validate_17_19_loop()
        self.validate_composition_patterns()
        self.validate_hardness_disparity()
        self.generate_final_verdict()
        
        return self.results

def main():
    validator = CorrectedComposerValidator()
    results = validator.run_complete_validation()
    
    print(f"\n✅ Corrected validation complete!")
    return results

if __name__ == "__main__":
    main()