"""
PRIME COMPOSITION TOOL #2: C* COMPOSER ANALYZER
==============================================
Deep analysis of C* = 17/19 as the prime composer constant.

Features:
- Tests C* relationships for all primes
- Identifies "composed" primes through C*
- Analyzes the 17-19 reciprocal loop
- Finds C* fraction representations
- Maps composition strength metrics
"""

import math
from fractions import Fraction
from decimal import Decimal, getcontext
import json
from typing import List, Dict, Tuple

getcontext().prec = 100

# Constants
C_STAR = 17 / 19  # Exact value
C_STAR_DECIMAL = 0.894751918  # Given value
POINT_SIX = 3 / 5

class CStarComposerAnalyzer:
    """Analyze primes through C* composition."""
    
    def __init__(self):
        self.composition_rules = []
        self.generator_primes = [17, 19]
    
    def analyze_prime_composition(self, p: int) -> Dict:
        """Analyze how prime p composes through C*."""
        
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
        """Classify the type of composition through C*."""
        
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
        """Calculate composition score based on C* relationship strength."""
        score = 100
        
        # Penalize errors
        score -= p_times_c_error * 1000
        score -= p_div_c_error * 1000
        
        # Bonus for exact fractions
        if c_star_fraction:
            score += 20
        
        return max(0, int(score))
    
    def analyze_17_19_loop(self) -> Dict:
        """Analyze the perfect reciprocal loop between 17 and 19."""
        
        print("Analyzing the 17-19 perfect reciprocal loop...")
        
        loop_analysis = {
            'generator_primes': [17, 19],
            'c_star_definition': f"17/19 = {C_STAR:.10f}",
            'given_c_star': C_STAR_DECIMAL,
            'error': abs(C_STAR - C_STAR_DECIMAL),
            'error_percent': abs(C_STAR - C_STAR_DECIMAL) / C_STAR_DECIMAL * 100,
            'perfect_relationships': [
                {
                    'formula': '19 × (17/19) = 17',
                    'calculation': f"{19} × ({17}/{19}) = {19 * C_STAR:.6f}",
                    'exact': abs(19 * C_STAR - 17) < 1e-10
                },
                {
                    'formula': '17 / (17/19) = 19',
                    'calculation': f"{17} / ({17}/{19}) = {17 / C_STAR:.6f}",
                    'exact': abs(17 / C_STAR - 19) < 1e-10
                }
            ],
            'period_encoding': {
                'period': self._find_period(17, 19),
                'encoding_formula': '(17 + 19) / 2',
                'result': (17 + 19) // 2,
                'verified': self._find_period(17, 19) == (17 + 19) // 2
            }
        }
        
        return loop_analysis
    
    def _find_period(self, p1: int, p2: int) -> int:
        """Find period of p1/p2 decimal expansion."""
        fraction = Fraction(p1, p2)
        
        # Simplify if necessary
        numerator = fraction.numerator
        denominator = fraction.denominator
        
        # Handle special cases
        if denominator == 1:
            return 0
        
        # Remove factors of 2 and 5
        while denominator % 2 == 0:
            denominator //= 2
        while denominator % 5 == 0:
            denominator //= 5
        
        if denominator == 1:
            return 0
        
        # Find period
        remainder = numerator % denominator
        remainders_seen = {}
        position = 0
        
        while remainder != 0 and remainder not in remainders_seen:
            remainders_seen[remainder] = position
            remainder = (remainder * 10) % denominator
            position += 1
        
        return position if remainder == 0 else position - remainders_seen[remainder]
    
    def find_composition_rules(self, primes: List[int]) -> List[Dict]:
        """Find all composition rules based on C*."""
        
        composition_rules = []
        
        for p in primes:
            analysis = self.analyze_prime_composition(p)
            
            if analysis['composition_type'] != 'not_composed':
                rule = {
                    'prime': p,
                    'composition_type': analysis['composition_type'],
                    'rule': f"p × C* ≈ {analysis['c_star_relationships']['p_times_c_star_nearest_int']}",
                    'error': analysis['c_star_relationships']['p_times_c_star_error'],
                    'score': analysis['composition_score']
                }
                composition_rules.append(rule)
        
        # Sort by score
        composition_rules.sort(key=lambda x: x['score'], reverse=True)
        
        return composition_rules
    
    def analyze_dimensional_connections(self) -> Dict:
        """Analyze dimensional connections of C*."""
        
        connections = {
            'c_star_value': C_STAR,
            'c_star_times_13': C_STAR * 13,
            'inverse_c_star_times_13': (1/C_STAR) * 13,
            'base_13_connection': {
                'approximation': C_STAR * 13,
                'target': 11.63,
                'error': abs(C_STAR * 13 - 11.63)
            },
            'dimensional_emergence': {
                'calculation': (1/C_STAR) * 13,
                'approximation': 14.53,
                'comparison': '13 + 1.5',
                'error': abs((1/C_STAR) * 13 - 14.5)
            },
            'zero_hex_tredecim': {
                'project': 'ZeroHex Tredecim',
                'base': 13,
                'c_star_role': 'temporal emergence factor'
            }
        }
        
        return connections
    
    def analyze_primes_batch(self, primes: List[int]) -> Dict:
        """Comprehensive batch analysis of primes through C*."""
        
        print(f"Analyzing {len(primes)} primes through C* composition...")
        
        # Individual analyses
        individual_analyses = []
        for p in primes:
            analysis = self.analyze_prime_composition(p)
            individual_analyses.append(analysis)
        
        # Find composition rules
        composition_rules = self.find_composition_rules(primes)
        
        # Analyze 17-19 loop
        loop_analysis = self.analyze_17_19_loop()
        
        # Dimensional connections
        dimensional_analysis = self.analyze_dimensional_connections()
        
        # Statistics
        composition_types = {}
        for analysis in individual_analyses:
            comp_type = analysis['composition_type']
            composition_types[comp_type] = composition_types.get(comp_type, 0) + 1
        
        average_score = sum(a['composition_score'] for a in individual_analyses) / len(individual_analyses)
        
        return {
            'individual_analyses': individual_analyses,
            'composition_rules': composition_rules,
            'loop_analysis': loop_analysis,
            'dimensional_connections': dimensional_analysis,
            'statistics': {
                'total_primes': len(primes),
                'composition_types': composition_types,
                'average_composition_score': average_score
            }
        }
    
    def export_results(self, results: Dict, filename: str = "cstar_composition_analysis.json"):
        """Export analysis results to JSON."""
        with open(filename, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"C* composition analysis saved to {filename}")

def main():
    """Main demonstration."""
    print("=" * 80)
    print("PRIME COMPOSITION TOOL #2: C* COMPOSER ANALYZER")
    print("Deep analysis of C* = 17/19 as prime composer constant")
    print("=" * 80)
    
    # Initialize analyzer
    analyzer = CStarComposerAnalyzer()
    
    # Test primes
    test_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
    
    print(f"\nAnalyzing {len(test_primes)} primes through C*...")
    
    # Comprehensive analysis
    results = analyzer.analyze_primes_batch(test_primes)
    
    # Display key results
    print("\n🌟 TOP COMPOSITION RULES:")
    for i, rule in enumerate(results['composition_rules'][:10]):
        print(f"{i+1:2d}. {rule['rule']}")
        print(f"    Type: {rule['composition_type']}, Error: {rule['error']:.6f}, Score: {rule['score']}")
        print()
    
    print("🔍 17-19 LOOP ANALYSIS:")
    loop = results['loop_analysis']
    print(f"  C* = 17/19 = {loop['c_star_definition']}")
    print(f"  Error vs given: {loop['error']:.10f} ({loop['error_percent']:.6f}%)")
    print(f"  Period encoding: {loop['period_encoding']['period']} = {loop['period_encoding']['encoding_formula']}")
    print()
    
    print("📊 COMPOSITION STATISTICS:")
    stats = results['statistics']
    print(f"  Total primes: {stats['total_primes']}")
    print(f"  Composition types: {stats['composition_types']}")
    print(f"  Average score: {stats['average_composition_score']:.1f}")
    
    # Export results
    analyzer.export_results(results)
    
    print("\n✅ C* composer analysis complete!")

if __name__ == "__main__":
    main()