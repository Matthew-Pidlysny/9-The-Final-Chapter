"""
PRIME COMPOSITION TOOL #3: HARDNESS & ENTROPY ANALYZER
=====================================================
Analyzes the "rock hardness" and entropy properties of primes.

Features:
- Calculates hardness metric based on reciprocal entropy
- Identifies reptend primes with maximal hardness
- Maps hardness to composition strength
- Analyzes entropy stabilization at different scales
- Correlates hardness with other prime properties
"""

import math
from fractions import Fraction
from decimal import Decimal, getcontext
import json
from typing import List, Dict, Tuple
import statistics

getcontext().prec = 200

# Constants
C_STAR = 17 / 19
POINT_SIX = 3 / 5

class HardnessAnalyzer:
    """Analyze hardness and entropy properties of primes."""
    
    def __init__(self):
        self.hardness_scale = {
            'soft': 0.0,
            'medium': 0.5,
            'hard': 0.8,
            'rock': 0.95,
            'maximal': 1.0
        }
    
    def calculate_entropy_at_scale(self, p: int, scale: int = 100) -> Dict:
        """Calculate entropy of reciprocal at different precision scales."""
        
        if p == 2 or p == 5:
            return {'entropy': 0.0, 'normalized': 0.0, 'scale': scale}
        
        # Get decimal expansion at specified scale
        decimal = Decimal(1) / Decimal(p)
        decimal_str = str(decimal)
        
        # Extract digits after decimal
        if '.' in decimal_str:
            decimal_str = decimal_str.split('.')[1][:scale]
        
        # Count digit frequencies
        digit_counts = [0] * 10
        for digit in decimal_str:
            if digit.isdigit():
                digit_counts[int(digit)] += 1
        
        # Calculate entropy
        total = sum(digit_counts)
        if total == 0:
            return {'entropy': 0.0, 'normalized': 0.0, 'scale': scale}
        
        entropy = 0.0
        for count in digit_counts:
            if count > 0:
                p_i = count / total
                entropy -= p_i * math.log2(p_i)
        
        # Normalize by maximum possible entropy (log2(10))
        max_entropy = math.log2(10)
        normalized_entropy = entropy / max_entropy
        
        return {
            'entropy': entropy,
            'normalized': normalized_entropy,
            'scale': scale,
            'digit_distribution': digit_counts
        }
    
    def calculate_hardness_spectrum(self, p: int) -> Dict:
        """Calculate hardness across multiple scales."""
        
        scales = [15, 35, 61, 100, 150, 200]
        hardness_values = {}
        
        for scale in scales:
            result = self.calculate_entropy_at_scale(p, scale)
            hardness_values[f'scale_{scale}'] = result['normalized']
        
        # Calculate overall hardness metrics
        all_values = list(hardness_values.values())
        
        return {
            'prime': p,
            'hardness_by_scale': hardness_values,
            'average_hardness': sum(all_values) / len(all_values),
            'max_hardness': max(all_values),
            'min_hardness': min(all_values),
            'hardness_variance': statistics.variance(all_values) if len(all_values) > 1 else 0,
            'quantum_limit_hardness': hardness_values.get('scale_61', 0),
            'stabilization_point': self._find_stabilization_point(p)
        }
    
    def _find_stabilization_point(self, p: int) -> int:
        """Find the scale where hardness stabilizes."""
        scales = [15, 35, 61, 100, 150]
        hardness_values = []
        
        for scale in scales:
            result = self.calculate_entropy_at_scale(p, scale)
            hardness_values.append(result['normalized'])
        
        # Look for stabilization (change < 0.01)
        for i in range(1, len(hardness_values)):
            if abs(hardness_values[i] - hardness_values[i-1]) < 0.01:
                return scales[i]
        
        return scales[-1]  # Return max scale if no stabilization
    
    def classify_hardness(self, hardness: float) -> str:
        """Classify hardness level."""
        if hardness >= 0.95:
            return "rock_hard"
        elif hardness >= 0.85:
            return "very_hard"
        elif hardness >= 0.70:
            return "hard"
        elif hardness >= 0.50:
            return "medium"
        else:
            return "soft"
    
    def analyze_reptend_hardness_correlation(self, primes: List[int]) -> Dict:
        """Analyze correlation between reptend property and hardness."""
        
        reptend_primes = []
        non_reptend_primes = []
        
        for p in primes:
            is_reptend = self._is_reptend_prime(p)
            hardness_spectrum = self.calculate_hardness_spectrum(p)
            
            prime_data = {
                'prime': p,
                'is_reptend': is_reptend,
                'hardness': hardness_spectrum['quantum_limit_hardness'],
                'average_hardness': hardness_spectrum['average_hardness'],
                'max_hardness': hardness_spectrum['max_hardness'],
                'hardness_class': self.classify_hardness(hardness_spectrum['quantum_limit_hardness'])
            }
            
            if is_reptend:
                reptend_primes.append(prime_data)
            else:
                non_reptend_primes.append(prime_data)
        
        # Calculate statistics
        reptend_hardness_values = [p['hardness'] for p in reptend_primes]
        non_reptend_hardness_values = [p['hardness'] for p in non_reptend_primes]
        
        correlation = {
            'reptend_primes': {
                'count': len(reptend_primes),
                'average_hardness': sum(reptend_hardness_values) / len(reptend_hardness_values) if reptend_hardness_values else 0,
                'max_hardness': max(reptend_hardness_values) if reptend_hardness_values else 0,
                'min_hardness': min(reptend_hardness_values) if reptend_hardness_values else 0
            },
            'non_reptend_primes': {
                'count': len(non_reptend_primes),
                'average_hardness': sum(non_reptend_hardness_values) / len(non_reptend_hardness_values) if non_reptend_hardness_values else 0,
                'max_hardness': max(non_reptend_hardness_values) if non_reptend_hardness_values else 0,
                'min_hardness': min(non_reptend_hardness_values) if non_reptend_hardness_values else 0
            },
            'correlation_strength': 0,
            'hardness_gap': 0
        }
        
        if reptend_hardness_values and non_reptend_hardness_values:
            correlation['hardness_gap'] = correlation['reptend_primes']['average_hardness'] - correlation['non_reptend_primes']['average_hardness']
            correlation['correlation_strength'] = abs(correlation['hardness_gap'])
        
        return correlation
    
    def _is_reptend_prime(self, p: int) -> bool:
        """Check if p is a reptend prime."""
        if p == 2 or p == 5:
            return False
        
        # Calculate period of 1/p
        remainder = 1
        remainders_seen = {}
        position = 0
        
        while remainder != 0 and remainder not in remainders_seen:
            remainders_seen[remainder] = position
            remainder = (remainder * 10) % p
            position += 1
        
        period = position if remainder == 0 else position - remainders_seen[remainder]
        return period == p - 1
    
    def analyze_hardness_composition_correlation(self, primes: List[int]) -> Dict:
        """Analyze correlation between hardness and C* composition."""
        
        analysis_results = []
        
        for p in primes:
            # Calculate hardness
            hardness_spectrum = self.calculate_hardness_spectrum(p)
            quantum_hardness = hardness_spectrum['quantum_limit_hardness']
            
            # Calculate C* relationship
            p_times_c = p * C_STAR
            p_times_c_error = abs(p_times_c - round(p_times_c))
            
            p_div_c = p / C_STAR
            p_div_c_error = abs(p_div_c - round(p_div_c))
            
            # Strong C* relationship?
            strong_c_relationship = p_times_c_error < 0.01 or p_div_c_error < 0.01
            
            analysis_results.append({
                'prime': p,
                'quantum_hardness': quantum_hardness,
                'hardness_class': self.classify_hardness(quantum_hardness),
                'p_times_c_error': p_times_c_error,
                'p_div_c_error': p_div_c_error,
                'strong_c_relationship': strong_c_relationship,
                'composition_score': max(0, 100 - p_times_c_error * 1000 - p_div_c_error * 1000)
            })
        
        # Correlation analysis
        high_hardness = [r for r in analysis_results if r['quantum_hardness'] >= 0.95]
        strong_c_related = [r for r in analysis_results if r['strong_c_relationship']]
        
        intersection = [r for r in high_hardness if r['strong_c_relationship']]
        
        correlation = {
            'total_primes': len(primes),
            'high_hardness_primes': len(high_hardness),
            'strong_c_related_primes': len(strong_c_related),
            'intersection_count': len(intersection),
            'correlation_percentage': len(intersection) / len(primes) * 100 if primes else 0
        }
        
        return {
            'individual_results': analysis_results,
            'correlation_analysis': correlation
        }
    
    def generate_hardness_ranking(self, primes: List[int]) -> List[Dict]:
        """Generate ranking of primes by hardness."""
        
        rankings = []
        
        for p in primes:
            hardness_spectrum = self.calculate_hardness_spectrum(p)
            
            ranking = {
                'rank': 0,  # Will be set after sorting
                'prime': p,
                'quantum_hardness': hardness_spectrum['quantum_limit_hardness'],
                'average_hardness': hardness_spectrum['average_hardness'],
                'max_hardness': hardness_spectrum['max_hardness'],
                'hardness_class': self.classify_hardness(hardness_spectrum['quantum_limit_hardness']),
                'is_reptend': self._is_reptend_prime(p),
                'stabilization_point': hardness_spectrum['stabilization_point']
            }
            
            rankings.append(ranking)
        
        # Sort by quantum limit hardness
        rankings.sort(key=lambda x: x['quantum_hardness'], reverse=True)
        
        # Assign ranks
        for i, ranking in enumerate(rankings):
            ranking['rank'] = i + 1
        
        return rankings
    
    def analyze_primes_batch(self, primes: List[int]) -> Dict:
        """Comprehensive hardness analysis of primes."""
        
        print(f"Analyzing hardness and entropy for {len(primes)} primes...")
        
        # Generate hardness ranking
        rankings = self.generate_hardness_ranking(primes)
        
        # Analyze reptend correlation
        reptend_correlation = self.analyze_reptend_hardness_correlation(primes)
        
        # Analyze C* composition correlation
        composition_correlation = self.analyze_hardness_composition_correlation(primes)
        
        # Hardness distribution
        hardness_classes = {}
        for ranking in rankings:
            hardness_class = ranking['hardness_class']
            hardness_classes[hardness_class] = hardness_classes.get(hardness_class, 0) + 1
        
        return {
            'hardness_rankings': rankings[:50],  # Top 50
            'reptend_correlation': reptend_correlation,
            'composition_correlation': composition_correlation,
            'hardness_distribution': hardness_classes
        }
    
    def export_results(self, results: Dict, filename: str = "hardness_entropy_analysis.json"):
        """Export analysis results to JSON."""
        with open(filename, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"Hardness and entropy analysis saved to {filename}")

def main():
    """Main demonstration."""
    print("=" * 80)
    print("PRIME COMPOSITION TOOL #3: HARDNESS & ENTROPY ANALYZER")
    print("Analyzing rock hardness and entropy properties of primes")
    print("=" * 80)
    
    # Initialize analyzer
    analyzer = HardnessAnalyzer()
    
    # Test primes
    test_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    
    print(f"\nAnalyzing hardness for {len(test_primes)} primes...")
    
    # Comprehensive analysis
    results = analyzer.analyze_primes_batch(test_primes)
    
    # Display top results
    print("\n🌟 TOP 10 HARDEST PRIMES:")
    for i, ranking in enumerate(results['hardness_rankings'][:10]):
        reptend_marker = "🐍" if ranking['is_reptend'] else "  "
        print(f"{i+1:2d}. Prime {ranking['prime']:3d} - Hardness: {ranking['quantum_hardness']:.4f} {reptend_marker}")
        print(f"    Class: {ranking['hardness_class']}, Stabilizes at: {ranking['stabilization_point']} digits")
    
    print("\n🔍 REPTEND CORRELATION:")
    reptend_corr = results['reptend_correlation']
    print(f"  Reptend primes: {reptend_corr['reptend_primes']['count']}")
    print(f"  Average hardness: {reptend_corr['reptend_primes']['average_hardness']:.4f}")
    print(f"  Non-reptend primes: {reptend_corr['non_reptend_primes']['count']}")
    print(f"  Average hardness: {reptend_corr['non_reptend_primes']['average_hardness']:.4f}")
    print(f"  Hardness gap: {reptend_corr['hardness_gap']:.4f}")
    
    print("\n📊 HARDNESS DISTRIBUTION:")
    for hardness_class, count in results['hardness_distribution'].items():
        print(f"  {hardness_class}: {count} primes")
    
    # Export results
    analyzer.export_results(results)
    
    print("\n✅ Hardness and entropy analysis complete!")

if __name__ == "__main__":
    main()