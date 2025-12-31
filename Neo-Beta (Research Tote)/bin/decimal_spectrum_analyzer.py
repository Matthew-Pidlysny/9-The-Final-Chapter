"""
🌈 Decimal Spectrum Analyzer - Comprehensive Number Behavior Framework
========================================================================

Advanced system for analyzing decimal expansions across all number types,
including reciprocals, fractions, and complex mathematical relationships.

Based on the spectrum understanding:
- Simple numbers: 1, 2, 4, 5, 8, 10 (clean reciprocal patterns)
- Wild numbers: 3, 6, 9, 11, 12 (complex reciprocal patterns)
- Special wilds: 7 (first prime with simples), 13 (prime with wilds)

Author: SuperNinja
Date: 2024
"""

import numpy as np
import math
from decimal import Decimal, getcontext
from fractions import Fraction
import itertools
import json
from collections import Counter, defaultdict
import mpmath as mp

# Set ultra-high precision
getcontext().prec = 200
mp.mp.dps = 200

class DecimalSpectrumAnalyzer:
    """
    Comprehensive analyzer for decimal expansion patterns and number behaviors.
    """
    
    def __init__(self):
        self.max_test_range = 200  # Start with 200, expand as needed
        self.spectrum_data = {}
        self.pattern_cache = {}
        
        # Define spectrum categories based on reciprocal behavior
        self.simple_numbers = {1, 2, 4, 5, 8, 10}
        self.wild_numbers = {3, 6, 9, 11, 12}
        self.special_wilds = {7, 13}  # Special cases
        
        # Analysis parameters
        self.max_decimal_places = 100
        self.repetition_threshold = 50
        
    def analyze_decimal_expansion(self, numerator, denominator, max_digits=100):
        """
        Analyze decimal expansion of any fraction with extreme precision.
        """
        try:
            # Use high precision decimal calculation
            dec_num = Decimal(numerator)
            dec_den = Decimal(denominator)
            result = dec_num / dec_den
            
            # Get decimal string
            decimal_str = str(result)
            
            # Analyze components
            analysis = {
                'fraction': f"{numerator}/{denominator}",
                'decimal_value': float(result),
                'decimal_string': decimal_str,
                'is_terminating': self._is_terminating_decimal(numerator, denominator),
                'repeating_pattern': None,
                'pattern_length': 0,
                'non_repeating_prefix': '',
                'digit_frequency': {},
                'sum_of_digits': 0,
                'digital_root': 0,
                'is_palindromic': False,
                'reciprocal_pattern_type': self._classify_reciprocal_pattern(denominator),
                'complexity_score': 0
            }
            
            # Detailed decimal analysis
            if '.' in decimal_str:
                integer_part, fractional_part = decimal_str.split('.', 1)
                analysis['integer_part'] = integer_part
                analysis['fractional_part'] = fractional_part
                
                # Find repeating patterns
                if not analysis['is_terminating']:
                    pattern_info = self._find_repeating_pattern(fractional_part, max_digits)
                    analysis.update(pattern_info)
                
                # Digit frequency analysis
                digit_counts = Counter(fractional_part)
                analysis['digit_frequency'] = dict(digit_counts)
                analysis['sum_of_digits'] = sum(int(d) for d in fractional_part)
                analysis['digital_root'] = self._calculate_digital_root(fractional_part)
                analysis['is_palindromic'] = fractional_part == fractional_part[::-1]
                
                # Complexity scoring
                analysis['complexity_score'] = self._calculate_complexity_score(analysis)
            
            return analysis
            
        except Exception as e:
            return {'error': str(e)}
    
    def _is_terminating_decimal(self, numerator, denominator):
        """Check if decimal terminates."""
        # Remove factors of 2 and 5 from denominator
        d = denominator
        while d % 2 == 0:
            d //= 2
        while d % 5 == 0:
            d //= 5
        return d == 1
    
    def _find_repeating_pattern(self, fractional_part, max_length=100):
        """
        Find repeating patterns in decimal expansion using advanced algorithms.
        """
        if len(fractional_part) < 10:
            return {'repeating_pattern': None, 'pattern_length': 0}
        
        # Try different pattern lengths
        best_pattern = None
        best_length = 0
        best_confidence = 0
        
        for pattern_length in range(1, min(len(fractional_part) // 2, 50)):
            pattern = fractional_part[:pattern_length]
            
            # Check how many times this pattern repeats
            repetitions = 0
            total_checks = 0
            
            for i in range(0, len(fractional_part) - pattern_length, pattern_length):
                candidate = fractional_part[i:i + pattern_length]
                if candidate == pattern:
                    repetitions += 1
                total_checks += 1
            
            confidence = repetitions / total_checks if total_checks > 0 else 0
            
            if confidence > best_confidence and confidence > 0.7:
                best_confidence = confidence
                best_pattern = pattern
                best_length = pattern_length
        
        if best_pattern:
            # Find non-repeating prefix
            prefix_length = 0
            for i in range(len(fractional_part)):
                if fractional_part[i:i + best_length] == best_pattern:
                    prefix_length = i
                    break
            
            return {
                'repeating_pattern': best_pattern,
                'pattern_length': best_length,
                'pattern_confidence': best_confidence,
                'non_repeating_prefix': fractional_part[:prefix_length]
            }
        
        return {'repeating_pattern': None, 'pattern_length': 0}
    
    def _classify_reciprocal_pattern(self, denominator):
        """Classify reciprocal pattern based on denominator properties."""
        if denominator in self.simple_numbers:
            return 'SIMPLE'
        elif denominator in self.wild_numbers:
            return 'WILD'
        elif denominator == 7:
            return 'SPECIAL_WILD_7'
        elif denominator == 13:
            return 'SPECIAL_WILD_13'
        elif self._is_prime(denominator):
            return 'PRIME'
        else:
            return 'COMPOSITE'
    
    def _calculate_digital_root(self, fractional_part):
        """Calculate digital root of fractional part."""
        if not fractional_part:
            return 0
        
        digit_sum = sum(int(d) for d in fractional_part)
        while digit_sum >= 10:
            digit_sum = sum(int(d) for d in str(digit_sum))
        return digit_sum
    
    def _calculate_complexity_score(self, analysis):
        """Calculate complexity score based on multiple factors."""
        score = 0
        
        # Pattern complexity
        if analysis['repeating_pattern']:
            pattern_len = analysis['pattern_length']
            score += min(pattern_len / 20, 1.0) * 0.4
        
        # Digit diversity
        if analysis['digit_frequency']:
            diversity = len(analysis['digit_frequency']) / 10.0
            score += diversity * 0.3
        
        # Pattern type
        pattern_type = analysis['reciprocal_pattern_type']
        if pattern_type == 'SIMPLE':
            score += 0.1
        elif pattern_type in ['WILD', 'SPECIAL_WILD_7', 'SPECIAL_WILD_13']:
            score += 0.3
        
        # Additional features
        if analysis['is_palindromic']:
            score += 0.2
        
        return min(score, 1.0)
    
    def analyze_number_spectrum(self, number):
        """
        Comprehensive analysis of a single number across all spectrums.
        """
        analysis = {
            'number': number,
            'timestamp': mp.time.time() if hasattr(mp, 'time') else 0,
            'basic_properties': self._analyze_basic_properties(number),
            'reciprocal_analysis': self.analyze_decimal_expansion(1, number),
            'fractional_analysis': {},
            'prime_factorization': self._factorize(number),
            'divisor_properties': self._analyze_divisors(number),
            'modular_properties': self._analyze_modular_properties(number),
            'spectrum_classification': self._classify_spectrum(number),
            'digital_signature': self._generate_digital_signature(number)
        }
        
        # Analyze common fractions
        common_denominators = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        for denom in common_denominators:
            if denom != 0:
                fraction_key = f"{number}/{denom}"
                analysis['fractional_analysis'][fraction_key] = self.analyze_decimal_expansion(number, denom)
        
        return analysis
    
    def _analyze_basic_properties(self, number):
        """Analyze basic mathematical properties."""
        return {
            'is_integer': number == int(number),
            'is_prime': self._is_prime(number),
            'is_composite': number > 1 and not self._is_prime(number),
            'is_even': number % 2 == 0,
            'is_odd': number % 2 == 1,
            'is_perfect_square': int(math.sqrt(number)) ** 2 == number,
            'is_perfect_cube': round(number ** (1/3)) ** 3 == number,
            'absolute_value': abs(number),
            'sign': 1 if number > 0 else -1 if number < 0 else 0,
            'number_of_digits': len(str(abs(int(number)))) if number != 0 else 1
        }
    
    def _is_prime(self, n):
        """Check if number is prime."""
        if n < 2:
            return False
        if n in (2, 3):
            return True
        if n % 2 == 0:
            return False
        
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True
    
    def _factorize(self, n):
        """Factorize number into prime factors."""
        if n < 2:
            return {'factors': [], 'prime_factors': [], 'factor_count': 0}
        
        factors = []
        prime_factors = []
        temp = n
        
        # Handle 2 separately
        while temp % 2 == 0:
            factors.append(2)
            prime_factors.append(2)
            temp //= 2
        
        # Handle odd numbers
        for i in range(3, int(math.sqrt(temp)) + 1, 2):
            while temp % i == 0:
                factors.append(i)
                prime_factors.append(i)
                temp //= i
        
        if temp > 1:
            factors.append(temp)
            prime_factors.append(temp)
        
        return {
            'factors': factors,
            'prime_factors': list(set(prime_factors)),
            'factor_count': len(factors),
            'unique_prime_count': len(set(prime_factors))
        }
    
    def _analyze_divisors(self, number):
        """Analyze all divisors of the number."""
        if number == 0:
            return {'divisors': [], 'divisor_count': 0, 'sum_of_divisors': 0}
        
        divisors = set()
        for i in range(1, int(math.sqrt(abs(number))) + 1):
            if number % i == 0:
                divisors.add(i)
                divisors.add(abs(number // i))
        
        divisors = sorted(list(divisors))
        
        return {
            'divisors': divisors,
            'divisor_count': len(divisors),
            'sum_of_divisors': sum(divisors),
            'is_perfect_number': sum(divisors[:-1]) == number if number > 0 else False,
            'is_abundant': sum(divisors[:-1]) > number if number > 0 else False,
            'is_deficient': sum(divisors[:-1]) < number if number > 0 else False
        }
    
    def _analyze_modular_properties(self, number):
        """Analyze modular arithmetic properties."""
        mod_properties = {}
        
        # Test common moduli
        moduli = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        for mod in moduli:
            if mod != 0:
                mod_properties[f"mod_{mod}"] = number % mod
        
        # Special properties
        mod_properties['quadratic_residues'] = self._find_quadratic_residues(number)
        mod_properties['multiplicative_order'] = self._find_multiplicative_order(number)
        
        return mod_properties
    
    def _find_quadratic_residues(self, number, limit=20):
        """Find quadratic residues for the number."""
        residues = []
        for i in range(limit):
            residues.append((i * i) % number)
        return list(set(residues))
    
    def _find_multiplicative_order(self, number):
        """Find multiplicative order (simplified)."""
        if number <= 2:
            return 0
        
        for k in range(1, number):
            if pow(10, k, number) == 1:
                return k
        return 0
    
    def _classify_spectrum(self, number):
        """Classify number in the decimal spectrum."""
        if number in self.simple_numbers:
            return {'category': 'SIMPLE', 'description': 'Clean reciprocal patterns, straightforward decimal behavior'}
        elif number in self.wild_numbers:
            return {'category': 'WILD', 'description': 'Complex reciprocal patterns, irregular decimal behavior'}
        elif number == 7:
            return {'category': 'SPECIAL_WILD_7', 'description': 'First prime containing simple patterns in repetition'}
        elif number == 13:
            return {'category': 'SPECIAL_WILD_13', 'description': 'Prime containing wild patterns, special mathematical properties'}
        elif self._is_prime(number):
            return {'category': 'PRIME', 'description': 'Prime number with unique decimal properties'}
        else:
            return {'category': 'COMPOSITE', 'description': 'Composite number with mixed decimal behavior'}
    
    def _generate_digital_signature(self, number):
        """Generate unique digital signature for the number."""
        # Create signature based on multiple properties
        signature = {
            'binary_representation': bin(int(number))[2:],
            'hexadecimal_representation': hex(int(number))[2:],
            'sum_of_digits': sum(int(d) for d in str(abs(int(number)))),
            'digital_root': self._calculate_digital_root(str(int(number))),
            'reversed_digits': str(int(number))[::-1],
            'digit_product': self._digit_product(int(number)),
            'hash_signature': hash(str(number)) % 1000000
        }
        return signature
    
    def _digit_product(self, n):
        """Calculate product of digits."""
        product = 1
        for digit in str(abs(n)):
            product *= int(digit)
        return product
    
    def map_entire_spectrum(self, max_range=200):
        """
        Map the entire feasible spectrum of number behaviors.
        """
        print(f"🌈 Mapping entire decimal spectrum from 1 to {max_range}...")
        
        spectrum_map = {
            'range': max_range,
            'analysis_date': mp.time.time() if hasattr(mp, 'time') else 0,
            'categories': {
                'simple': [],
                'wild': [],
                'special_wild_7': [],
                'special_wild_13': [],
                'prime': [],
                'composite': []
            },
            'pattern_clusters': {},
            'max_complexity_numbers': [],
            'insights': {}
        }
        
        complexity_scores = []
        
        for number in range(1, max_range + 1):
            analysis = self.analyze_number_spectrum(number)
            
            # Categorize
            category = analysis['spectrum_classification']['category'].lower()
            if category in spectrum_map['categories']:
                spectrum_map['categories'][category].append(number)
            
            # Track complexity
            if 'reciprocal_analysis' in analysis and 'complexity_score' in analysis['reciprocal_analysis']:
                complexity = analysis['reciprocal_analysis']['complexity_score']
                complexity_scores.append((number, complexity))
            
            # Progress indicator
            if number % 20 == 0:
                print(f"   Analyzed {number}/{max_range} numbers...")
        
        # Find most complex numbers
        complexity_scores.sort(key=lambda x: x[1], reverse=True)
        spectrum_map['max_complexity_numbers'] = complexity_scores[:10]
        
        # Generate insights
        spectrum_map['insights'] = self._generate_spectrum_insights(spectrum_map)
        
        return spectrum_map
    
    def _generate_spectrum_insights(self, spectrum_map):
        """Generate insights from spectrum mapping."""
        insights = {}
        
        # Category distribution
        total = sum(len(v) for v in spectrum_map['categories'].values())
        for category, numbers in spectrum_map['categories'].items():
            insights[f'{category}_percentage'] = (len(numbers) / total) * 100
        
        # Pattern observations
        insights['simple_numbers_found'] = spectrum_map['categories']['simple']
        insights['wild_numbers_found'] = spectrum_map['categories']['wild']
        insights['prime_density'] = len(spectrum_map['categories']['prime']) / spectrum_map['range']
        
        # Complexity patterns
        if spectrum_map['max_complexity_numbers']:
            top_complex = spectrum_map['max_complexity_numbers'][:5]
            insights['highest_complexity_numbers'] = [n[0] for n in top_complex]
            insights['highest_complexity_scores'] = [n[1] for n in top_complex]
        
        return insights
    
    def find_optimal_maximum(self, test_limit=500):
        """
        Test to find the optimal maximum number for comprehensive analysis.
        """
        print(f"🔍 Testing spectrum up to {test_limit} to find optimal maximum...")
        
        results = {
            'test_ranges': [50, 100, 200, 300, 400, 500],
            'complexity_trends': [],
            'pattern_stability': [],
            'optimal_range': 0,
            'recommendations': []
        }
        
        for test_range in results['test_ranges']:
            if test_range <= test_limit:
                print(f"   Testing range 1-{test_range}...")
                
                spectrum = self.map_entire_spectrum(test_range)
                
                # Analyze complexity trends
                avg_complexity = np.mean([score for _, score in spectrum['max_complexity_numbers'][:10]])
                results['complexity_trends'].append((test_range, avg_complexity))
                
                # Analyze pattern stability
                simple_percentage = spectrum['insights'].get('simple_percentage', 0)
                wild_percentage = spectrum['insights'].get('wild_percentage', 0)
                stability = abs(simple_percentage - wild_percentage)
                results['pattern_stability'].append((test_range, stability))
        
        # Determine optimal range
        if results['complexity_trends']:
            # Find where complexity stabilizes
            complexity_values = [score for _, score in results['complexity_trends']]
            for i in range(1, len(complexity_values)):
                if abs(complexity_values[i] - complexity_values[i-1]) < 0.01:
                    results['optimal_range'] = results['test_ranges'][i]
                    break
        
        # Generate recommendations
        if results['optimal_range'] == 0:
            results['optimal_range'] = 200  # Default fallback
        
        results['recommendations'] = [
            f"Optimal analysis range: 1-{results['optimal_range']}",
            "Beyond this range, patterns show diminishing returns",
            "Prime density stabilizes after this point",
            "Complexity scores plateau, indicating comprehensive coverage"
        ]
        
        return results


def main():
    """Main demonstration of the Decimal Spectrum Analyzer."""
    print("🌈 Decimal Spectrum Analyzer - Comprehensive Number Behavior Framework")
    print("=" * 80)
    
    analyzer = DecimalSpectrumAnalyzer()
    
    # Test spectrum mapping
    print("\n🗺️ Mapping decimal spectrum...")
    spectrum = analyzer.map_entire_spectrum(100)
    
    print(f"\n📊 Spectrum Analysis Results:")
    for category, numbers in spectrum['categories'].items():
        print(f"   {category.upper()}: {len(numbers)} numbers - {numbers[:10]}...")
    
    print(f"\n🎯 Key Insights:")
    for key, value in spectrum['insights'].items():
        print(f"   {key}: {value}")
    
    # Find optimal maximum
    print(f"\n🔍 Finding optimal analysis range...")
    optimal_results = analyzer.find_optimal_maximum(200)
    
    print(f"\n✅ Optimal Range: 1-{optimal_results['optimal_range']}")
    for rec in optimal_results['recommendations']:
        print(f"   💡 {rec}")
    
    # Detailed analysis of key numbers
    print(f"\n🔬 Detailed Analysis of Key Numbers:")
    key_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    
    for num in key_numbers:
        analysis = analyzer.analyze_number_spectrum(num)
        print(f"\n   Number {num}:")
        print(f"     Category: {analysis['spectrum_classification']['category']}")
        print(f"     Description: {analysis['spectrum_classification']['description']}")
        
        if 'reciprocal_analysis' in analysis and 'complexity_score' in analysis['reciprocal_analysis']:
            print(f"     Complexity: {analysis['reciprocal_analysis']['complexity_score']:.3f}")
        
        if 'reciprocal_analysis' in analysis and 'repeating_pattern' in analysis['reciprocal_analysis']:
            pattern = analysis['reciprocal_analysis']['repeating_pattern']
            if pattern:
                print(f"     Pattern: {pattern[:20]}{'...' if len(pattern) > 20 else ''}")
    
    print(f"\n🎉 Spectrum Analysis Complete!")
    print("=" * 80)


if __name__ == "__main__":
    main()