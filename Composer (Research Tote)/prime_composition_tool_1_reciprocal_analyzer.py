"""
PRIME COMPOSITION TOOL #1: RECIPROCAL SPACE ANALYZER
=====================================================
Analyzes primes through their reciprocal space structure.

Features:
- Generates reciprocal trees (1/p to p/p)
- Finds C* relationships in reciprocal space
- Calculates period and encoding patterns
- Identifies "hard points" in numerical space
- Maps reciprocal structure to composition
"""

import math
from fractions import Fraction
from decimal import Decimal, getcontext
import json
from typing import List, Dict, Tuple
import itertools

getcontext().prec = 100

# Constants
C_STAR = 17 / 19
POINT_SIX = 3 / 5

class ReciprocalSpaceAnalyzer:
    """Analyze primes in reciprocal space."""
    
    def __init__(self):
        self.results = []
    
    def generate_reciprocal_tree(self, p: int) -> List[Fraction]:
        """Generate the complete reciprocal tree for prime p."""
        tree = []
        for k in range(1, p + 1):
            tree.append(Fraction(k, p))
        return tree
    
    def find_c_star_patterns(self, p: int, tree: List[Fraction]) -> List[Dict]:
        """Find all patterns involving C* in the reciprocal tree."""
        patterns = []
        
        for i, frac in enumerate(tree):
            value = float(frac)
            
            # Check various C* relationships
            checks = {
                'direct_to_c': abs(value - C_STAR),
                'c_divided': abs(value - (C_STAR / 2)),
                'c_multiplied': abs(value - (C_STAR * 2)),
                'c_over_p': abs(float(Fraction(1, p)) - (C_STAR / p)),
                'c_times_p': abs(value - (C_STAR * p)) if C_STAR * p <= 1 else float('inf'),
                'inverse_c': abs(value - (1 / C_STAR)),
            }
            
            for pattern_name, error in checks.items():
                if error < 0.01:  # Within 1% tolerance
                    patterns.append({
                        'fraction': str(frac),
                        'value': value,
                        'pattern': pattern_name,
                        'error': error,
                        'position': i + 1
                    })
        
        return patterns
    
    def analyze_period_encoding(self, p: int) -> Dict:
        """Analyze how the period encodes prime information."""
        if p == 2 or p == 5:
            return {'period': None, 'encoding': 'non-reptend base case'}
        
        # Calculate period of 1/p
        remainder = 1
        remainders_seen = {}
        position = 0
        
        while remainder != 0 and remainder not in remainders_seen:
            remainders_seen[remainder] = position
            remainder = (remainder * 10) % p
            position += 1
        
        period = position if remainder == 0 else position - remainders_seen[remainder]
        
        # Analyze encoding
        encoding_info = {
            'period': period,
            'is_reptend': period == p - 1,
            'period_ratio': period / p if p > 0 else 0,
            'special_patterns': []
        }
        
        # Check for special encoding patterns
        if period == (p + 1) // 2 and p % 4 == 3:
            encoding_info['special_patterns'].append('half_period_plus_half')
        
        if period == p - 1:
            encoding_info['special_patterns'].append('full_reptend_maximal')
        
        # Check 17-19 encoding: period = (p1 + p2)/2
        if p in [17, 19]:
            encoding_info['special_patterns'].append('generator_prime_encoding')
            encoding_info['period_sum_relation'] = period == (17 + 19) // 2
        
        return encoding_info
    
    def calculate_reciprocal_density(self, p: int, tree: List[Fraction]) -> Dict:
        """Calculate density metrics in reciprocal space."""
        values = [float(frac) for frac in tree]
        
        # Spacing analysis
        spacings = []
        for i in range(len(values) - 1):
            spacings.append(values[i+1] - values[i])
        
        density_info = {
            'mean_spacing': sum(spacings) / len(spacings) if spacings else 0,
            'min_spacing': min(spacings) if spacings else 0,
            'max_spacing': max(spacings) if spacings else 0,
            'spacing_variance': self._calculate_variance(spacings),
            'c_star_zone_coverage': 0,
            'point_six_zone_coverage': 0
        }
        
        # Calculate coverage in special zones
        c_star_zone = sum(1 for v in values if abs(v - C_STAR) < 0.05)
        point_six_zone = sum(1 for v in values if abs(v - POINT_SIX) < 0.05)
        
        density_info['c_star_zone_coverage'] = c_star_zone / len(values) * 100
        density_info['point_six_zone_coverage'] = point_six_zone / len(values) * 100
        
        return density_info
    
    def _calculate_variance(self, values: List[float]) -> float:
        """Calculate variance of a list of values."""
        if not values:
            return 0.0
        mean = sum(values) / len(values)
        return sum((x - mean) ** 2 for x in values) / len(values)
    
    def analyze_prime(self, p: int) -> Dict:
        """Complete reciprocal space analysis for prime p."""
        print(f"Analyzing prime {p} in reciprocal space...")
        
        # Generate reciprocal tree
        tree = self.generate_reciprocal_tree(p)
        
        # Find C* patterns
        c_star_patterns = self.find_c_star_patterns(p, tree)
        
        # Analyze period encoding
        period_info = self.analyze_period_encoding(p)
        
        # Calculate density metrics
        density_info = self.calculate_reciprocal_density(p, tree)
        
        # Compose the result
        analysis = {
            'prime': p,
            'reciprocal_tree_size': len(tree),
            'c_star_patterns': c_star_patterns,
            'period_encoding': period_info,
            'density_metrics': density_info,
            'composition_score': self._calculate_composition_score(c_star_patterns, period_info, density_info)
        }
        
        return analysis
    
    def _calculate_composition_score(self, patterns: List[Dict], period_info: Dict, density: Dict) -> int:
        """Calculate composition score based on reciprocal space properties."""
        score = 0
        
        # C* pattern score
        score += len(patterns) * 10
        
        # Period encoding score
        if period_info.get('is_reptend', False):
            score += 25
        if period_info.get('period', 0):
            score += min(period_info.get('period', 0) / 2, 20)
        
        # Density score
        score += density['c_star_zone_coverage'] / 2
        score += density['point_six_zone_coverage'] / 2
        
        return int(score)
    
    def analyze_primes_batch(self, primes: List[int]) -> List[Dict]:
        """Analyze multiple primes and return results."""
        self.results = []
        
        for p in primes:
            analysis = self.analyze_prime(p)
            self.results.append(analysis)
        
        return self.results
    
    def export_results(self, filename: str = "reciprocal_space_analysis.json"):
        """Export analysis results to JSON."""
        with open(filename, 'w') as f:
            json.dump(self.results, f, indent=2)
        print(f"Reciprocal space analysis saved to {filename}")

def main():
    """Main demonstration."""
    print("=" * 80)
    print("PRIME COMPOSITION TOOL #1: RECIPROCAL SPACE ANALYZER")
    print("Analyzing primes through reciprocal space structure")
    print("=" * 80)
    
    # Initialize analyzer
    analyzer = ReciprocalSpaceAnalyzer()
    
    # Test primes
    test_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    
    print(f"\nAnalyzing {len(test_primes)} primes...")
    
    # Analyze primes
    results = analyzer.analyze_primes_batch(test_primes)
    
    # Display top results
    print("\n🌟 TOP PRIMES BY RECIPROCAL COMPOSITION SCORE:")
    top_primes = sorted(results, key=lambda x: x['composition_score'], reverse=True)
    
    for i, result in enumerate(top_primes[:10]):
        print(f"{i+1:2d}. Prime {result['prime']:3d} - Score: {result['composition_score']:3d}")
        print(f"    C* patterns: {len(result['c_star_patterns'])}")
        print(f"    Reptend: {'Yes' if result['period_encoding']['is_reptend'] else 'No'}")
        print(f"    C* zone coverage: {result['density_metrics']['c_star_zone_coverage']:.1f}%")
        print()
    
    # Special focus on 17 and 19
    print("🔍 SPECIAL ANALYSIS: GENERATOR PRIMES 17 and 19")
    for p in [17, 19]:
        result = next(r for r in results if r['prime'] == p)
        print(f"\nPrime {p}:")
        print(f"  Period: {result['period_encoding']['period']}")
        print(f"  C* patterns found: {len(result['c_star_patterns'])}")
        for pattern in result['c_star_patterns'][:3]:
            print(f"    {pattern['fraction']} ≈ {pattern['pattern']} (error: {pattern['error']:.6f})")
    
    # Export results
    analyzer.export_results()
    
    print("\n✅ Reciprocal space analysis complete!")

if __name__ == "__main__":
    main()