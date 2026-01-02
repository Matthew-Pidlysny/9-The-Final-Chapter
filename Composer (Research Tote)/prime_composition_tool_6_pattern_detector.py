"""
PRIME COMPOSITION TOOL #6: PATTERN DETECTOR & COMPOSER
=====================================================
Detects and analyzes patterns in prime composition.

Features:
- Detects recurring patterns across primes
- Identifies composition rules and formulas
- Analyzes 0.6 = 3/5 patterns
- Maps geometric and arithmetic progressions
- Predicts composition for new primes
"""

import math
from fractions import Fraction
from decimal import Decimal, getcontext
import json
from typing import List, Dict, Tuple, Set
from collections import defaultdict, Counter
import itertools

getcontext().prec = 100

# Constants
C_STAR = 17 / 19
POINT_SIX = 3 / 5
PHI = (1 + math.sqrt(5)) / 2

class PatternDetector:
    """Detect and analyze patterns in prime composition."""
    
    def __init__(self):
        self.patterns = {
            'c_star_fractions': [],
            'point_six_fractions': [],
            'geometric_progressions': [],
            'arithmetic_progressions': [],
            'composition_rules': []
        }
        self.formulas = []
    
    def detect_fraction_patterns(self, primes: List[int]) -> Dict:
        """Detect fractional patterns involving C* and 0.6."""
        
        fraction_patterns = {
            'c_star_fractions': [],
            'point_six_fractions': [],
            'combined_patterns': []
        }
        
        for p in primes:
            # Find fractions close to C*
            c_star_k = round(p * C_STAR)
            if 1 <= c_star_k <= p:
                fraction = Fraction(c_star_k, p)
                error = abs(float(fraction) - C_STAR)
                
                if error < 0.01:
                    fraction_patterns['c_star_fractions'].append({
                        'prime': p,
                        'fraction': str(fraction),
                        'value': float(fraction),
                        'c_star_error': error,
                        'simplified': f"{c_star_k}/{p} ≈ C*"
                    })
            
            # Find fractions close to 0.6
            point_six_k = round(p * POINT_SIX)
            if 1 <= point_six_k <= p:
                fraction = Fraction(point_six_k, p)
                error = abs(float(fraction) - POINT_SIX)
                
                if error < 0.01:
                    fraction_patterns['point_six_fractions'].append({
                        'prime': p,
                        'fraction': str(fraction),
                        'value': float(fraction),
                        'point_six_error': error,
                        'simplified': f"{point_six_k}/{p} ≈ 0.6"
                    })
        
        # Find combined patterns
        for c_pattern in fraction_patterns['c_star_fractions']:
            for p6_pattern in fraction_patterns['point_six_fractions']:
                if c_pattern['prime'] == p6_pattern['prime']:
                    fraction_patterns['combined_patterns'].append({
                        'prime': c_pattern['prime'],
                        'c_star_fraction': c_pattern['fraction'],
                        'point_six_fraction': p6_pattern['fraction'],
                        'dual_pattern': True
                    })
        
        return fraction_patterns
    
    def detect_progression_patterns(self, primes: List[int]) -> Dict:
        """Detect arithmetic and geometric progressions in primes."""
        
        progression_patterns = {
            'arithmetic_progressions': [],
            'geometric_progressions': [],
            'composite_progressions': []
        }
        
        # Arithmetic progressions
        for length in [3, 4, 5]:
            for start_idx in range(len(primes) - length + 1):
                sequence = primes[start_idx:start_idx + length]
                differences = [sequence[i+1] - sequence[i] for i in range(length - 1)]
                
                if len(set(differences)) == 1:  # Arithmetic progression
                    progression_patterns['arithmetic_progressions'].append({
                        'length': length,
                        'sequence': sequence,
                        'common_difference': differences[0],
                        'start': sequence[0],
                        'end': sequence[-1]
                    })
        
        # Geometric progressions (ratios)
        for length in [3, 4]:
            for start_idx in range(len(primes) - length + 1):
                sequence = primes[start_idx:start_idx + length]
                ratios = [sequence[i+1] / sequence[i] for i in range(length - 1)]
                
                # Check if ratios are approximately equal
                if len(set(round(r, 2) for r in ratios)) == 1 and all(r > 1 for r in ratios):
                    progression_patterns['geometric_progressions'].append({
                        'length': length,
                        'sequence': sequence,
                        'common_ratio': round(ratios[0], 3),
                        'start': sequence[0],
                        'end': sequence[-1]
                    })
        
        # Composite patterns (mix of arithmetic and geometric)
        # Look for patterns like p, p+2, p+6 (prime triplet structure)
        for i in range(len(primes) - 2):
            p1, p2, p3 = primes[i:i+3]
            if p2 - p1 == 2 and p3 - p2 == 4:  # Prime triplet
                progression_patterns['composite_progressions'].append({
                    'type': 'prime_triplet',
                    'sequence': [p1, p2, p3],
                    'pattern': 'p, p+2, p+6'
                })
            elif p2 - p1 == 2 and p3 - p2 == 2:  # Twin pair extended
                progression_patterns['composite_progressions'].append({
                    'type': 'extended_twin',
                    'sequence': [p1, p2, p3],
                    'pattern': 'p, p+2, p+4'
                })
        
        return progression_patterns
    
    def detect_composition_rules(self, primes: List[int], composition_data: List[Dict]) -> List[Dict]:
        """Detect composition rules based on C* relationships."""
        
        rules = []
        
        # Rule 1: p × C* ≈ integer
        for i, p in enumerate(primes):
            if i < len(composition_data):
                p_times_c = p * C_STAR
                nearest_int = round(p_times_c)
                error = abs(p_times_c - nearest_int)
                
                if error < 0.01:
                    rules.append({
                        'rule_type': 'c_star_product',
                        'formula': f'{p} × C* ≈ {nearest_int}',
                        'prime': p,
                        'result': nearest_int,
                        'error': error,
                        'strength': max(0, 100 - error * 1000)
                    })
        
        # Rule 2: p / C* ≈ integer
        for i, p in enumerate(primes):
            if i < len(composition_data):
                p_div_c = p / C_STAR
                nearest_int = round(p_div_c)
                error = abs(p_div_c - nearest_int)
                
                if error < 0.01:
                    rules.append({
                        'rule_type': 'c_star_division',
                        'formula': f'{p} / C* ≈ {nearest_int}',
                        'prime': p,
                        'result': nearest_int,
                        'error': error,
                        'strength': max(0, 100 - error * 1000)
                    })
        
        # Rule 3: Fraction patterns
        fraction_patterns = self.detect_fraction_patterns(primes)
        for pattern in fraction_patterns['c_star_fractions']:
            rules.append({
                'rule_type': 'c_star_fraction',
                'formula': pattern['simplified'],
                'prime': pattern['prime'],
                'fraction': pattern['fraction'],
                'error': pattern['c_star_error'],
                'strength': max(0, 100 - pattern['c_star_error'] * 1000)
            })
        
        # Sort rules by strength
        rules.sort(key=lambda x: x['strength'], reverse=True)
        
        return rules
    
    def analyze_period_patterns(self, primes: List[int]) -> Dict:
        """Analyze patterns in reciprocal periods."""
        
        period_patterns = {
            'periods': {},
            'encoding_patterns': [],
            'length_distributions': {}
        }
        
        for p in primes:
            if p == 2 or p == 5:
                continue
            
            period = self._find_period(p)
            period_patterns['periods'][p] = period
            
            # Check for encoding patterns
            if period:
                encoding_analysis = {
                    'prime': p,
                    'period': period,
                    'period_ratio': period / p,
                    'special_encodings': []
                }
                
                # Check if period equals p-1 (reptend)
                if period == p - 1:
                    encoding_analysis['special_encodings'].append('reptend_maximal')
                
                # Check if period equals (p-1)/2
                if period == (p - 1) // 2:
                    encoding_analysis['special_encodings'].append('half_period')
                
                # Check 17-19 encoding
                if p in [17, 19] and period == 18:
                    encoding_analysis['special_encodings'].append('generator_encoding_18')
                
                period_patterns['encoding_patterns'].append(encoding_analysis)
        
        # Period length distribution
        period_lengths = list(period_patterns['periods'].values())
        period_counts = Counter(period_lengths)
        period_patterns['length_distributions'] = dict(period_counts)
        
        return period_patterns
    
    def _find_period(self, p: int) -> int:
        """Find period of 1/p."""
        if p == 2 or p == 5:
            return 0
        
        remainder = 1
        remainders_seen = {}
        position = 0
        
        while remainder != 0 and remainder not in remainders_seen:
            remainders_seen[remainder] = position
            remainder = (remainder * 10) % p
            position += 1
        
        return position if remainder == 0 else position - remainders_seen[remainder]
    
    def predict_composition(self, test_prime: int, rules: List[Dict]) -> Dict:
        """Predict composition for a new prime using detected rules."""
        
        prediction = {
            'prime': test_prime,
            'predictions': [],
            'confidence_scores': {},
            'dominant_pattern': None
        }
        
        # Test against detected rules
        for rule in rules[:10]:  # Use top 10 rules
            confidence = self._calculate_rule_confidence(test_prime, rule)
            
            if confidence > 0:
                prediction['predictions'].append({
                    'rule': rule['formula'],
                    'rule_type': rule['rule_type'],
                    'confidence': confidence,
                    'expected_result': self._apply_rule(test_prime, rule)
                })
        
        # Calculate confidence scores by rule type
        rule_type_confidence = defaultdict(list)
        for pred in prediction['predictions']:
            rule_type_confidence[pred['rule_type']].append(pred['confidence'])
        
        for rule_type, confidences in rule_type_confidence.items():
            prediction['confidence_scores'][rule_type] = sum(confidences) / len(confidences)
        
        # Find dominant pattern
        if prediction['confidence_scores']:
            dominant_type = max(prediction['confidence_scores'], key=prediction['confidence_scores'].get)
            prediction['dominant_pattern'] = {
                'type': dominant_type,
                'confidence': prediction['confidence_scores'][dominant_type]
            }
        
        return prediction
    
    def _calculate_rule_confidence(self, prime: int, rule: Dict) -> float:
        """Calculate confidence that a rule applies to a prime."""
        
        if rule['rule_type'] == 'c_star_product':
            prime_times_c = prime * C_STAR
            nearest_int = round(prime_times_c)
            error = abs(prime_times_c - nearest_int)
            return max(0, 100 - error * 1000)
        
        elif rule['rule_type'] == 'c_star_division':
            prime_div_c = prime / C_STAR
            nearest_int = round(prime_div_c)
            error = abs(prime_div_c - nearest_int)
            return max(0, 100 - error * 1000)
        
        elif rule['rule_type'] == 'c_star_fraction':
            k = round(prime * C_STAR)
            if 1 <= k <= prime:
                fraction = Fraction(k, prime)
                error = abs(float(fraction) - C_STAR)
                return max(0, 100 - error * 1000)
        
        return 0
    
    def _apply_rule(self, prime: int, rule: Dict) -> str:
        """Apply a rule to a prime and return result description."""
        
        if rule['rule_type'] == 'c_star_product':
            prime_times_c = prime * C_STAR
            nearest_int = round(prime_times_c)
            return f"{prime} × C* ≈ {nearest_int}"
        
        elif rule['rule_type'] == 'c_star_division':
            prime_div_c = prime / C_STAR
            nearest_int = round(prime_div_c)
            return f"{prime} / C* ≈ {nearest_int}"
        
        elif rule['rule_type'] == 'c_star_fraction':
            k = round(prime * C_STAR)
            return f"{k}/{prime} ≈ C*"
        
        return "Unknown rule"
    
    def analyze_primes_batch(self, primes: List[int], composition_data: List[Dict]) -> Dict:
        """Comprehensive pattern analysis of primes."""
        
        print(f"Detecting patterns in {len(primes)} primes...")
        
        # Detect all pattern types
        fraction_patterns = self.detect_fraction_patterns(primes)
        progression_patterns = self.detect_progression_patterns(primes)
        composition_rules = self.detect_composition_rules(primes, composition_data)
        period_patterns = self.analyze_period_patterns(primes)
        
        # Pattern synthesis
        pattern_synthesis = {
            'total_patterns': len(fraction_patterns['c_star_fractions']) + 
                            len(fraction_patterns['point_six_fractions']) +
                            len(progression_patterns['arithmetic_progressions']) +
                            len(progression_patterns['geometric_progressions']) +
                            len(composition_rules),
            'dominant_pattern_types': []
        }
        
        # Identify dominant patterns
        pattern_counts = {
            'c_star_fractions': len(fraction_patterns['c_star_fractions']),
            'point_six_fractions': len(fraction_patterns['point_six_fractions']),
            'arithmetic_progressions': len(progression_patterns['arithmetic_progressions']),
            'geometric_progressions': len(progression_patterns['geometric_progressions']),
            'composition_rules': len(composition_rules)
        }
        
        sorted_patterns = sorted(pattern_counts.items(), key=lambda x: x[1], reverse=True)
        pattern_synthesis['dominant_pattern_types'] = sorted_patterns[:3]
        
        return {
            'fraction_patterns': fraction_patterns,
            'progression_patterns': progression_patterns,
            'composition_rules': composition_rules[:20],  # Top 20 rules
            'period_patterns': period_patterns,
            'pattern_synthesis': pattern_synthesis
        }
    
    def export_results(self, results: Dict, filename: str = "pattern_detection_analysis.json"):
        """Export analysis results to JSON."""
        with open(filename, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"Pattern detection analysis saved to {filename}")

def main():
    """Main demonstration."""
    print("=" * 80)
    print("PRIME COMPOSITION TOOL #6: PATTERN DETECTOR & COMPOSER")
    print("Detecting and analyzing patterns in prime composition")
    print("=" * 80)
    
    # Initialize detector
    detector = PatternDetector()
    
    # Test primes
    test_primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]
    
    # Mock composition data for demonstration
    mock_composition = [{'prime': p, 'composition_score': 50 + (p % 50)} for p in test_primes]
    
    print(f"\nDetecting patterns in {len(test_primes)} primes...")
    
    # Comprehensive analysis
    results = detector.analyze_primes_batch(test_primes, mock_composition)
    
    # Display results
    print("\n🌟 DOMINANT PATTERN TYPES:")
    for pattern_type, count in results['pattern_synthesis']['dominant_pattern_types']:
        print(f"  {pattern_type}: {count} patterns")
    
    print("\n🔍 TOP COMPOSITION RULES:")
    for i, rule in enumerate(results['composition_rules'][:10]):
        print(f"{i+1:2d}. {rule['formula']} (strength: {rule['strength']:.1f})")
    
    print("\n📊 FRACTION PATTERNS:")
    print(f"  C* fractions: {len(results['fraction_patterns']['c_star_fractions'])}")
    print(f"  0.6 fractions: {len(results['fraction_patterns']['point_six_fractions'])}")
    print(f"  Combined patterns: {len(results['fraction_patterns']['combined_patterns'])}")
    
    # Test prediction
    print("\n🔮 PREDICTION EXAMPLE:")
    test_prime = 131
    prediction = detector.predict_composition(test_prime, results['composition_rules'])
    
    print(f"  Predicting composition for prime {test_prime}:")
    if prediction['dominant_pattern']:
        print(f"  Dominant pattern: {prediction['dominant_pattern']['type']} (confidence: {prediction['dominant_pattern']['confidence']:.1f}%)")
    
    for pred in prediction['predictions'][:3]:
        print(f"    {pred['rule']} (confidence: {pred['confidence']:.1f}%)")
    
    # Export results
    detector.export_results(results)
    
    print("\n✅ Pattern detection analysis complete!")

if __name__ == "__main__":
    main()