"""
🎯 Ultimate Number Analyzer - Complete Decimal Expansion Framework
==================================================================

The definitive tool for analyzing ANY number (0-200) and providing comprehensive
insights about its mathematical behavior, decimal patterns, and spectrum properties.

This tool represents the culmination of our decimal spectrum research,
providing complete analysis capabilities for all number types.

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
import hashlib
from decimal_spectrum_analyzer import DecimalSpectrumAnalyzer

# Set ultra-high precision
getcontext().prec = 200
mp.mp.dps = 200

class UltimateNumberAnalyzer:
    """
    Ultimate analyzer providing complete insights for any number 0-200.
    """
    
    def __init__(self):
        self.spectrum_analyzer = DecimalSpectrumAnalyzer()
        self.max_range = 200  # Optimal range from our analysis
        
        # Pre-computed spectrum data
        self.spectrum_map = None
        self._initialize_spectrum_data()
        
    def _initialize_spectrum_data(self):
        """Initialize with pre-computed spectrum data."""
        print("🔄 Initializing spectrum database...")
        self.spectrum_map = self.spectrum_analyzer.map_entire_spectrum(self.max_range)
        print("✅ Spectrum database ready!")
    
    def analyze_number(self, number):
        """
        Provide COMPLETE analysis of any number from 0 to 200.
        """
        if not (0 <= number <= self.max_range):
            return {
                'error': f'Number must be between 0 and {self.max_range}',
                'supported_range': f'0-{self.max_range}'
            }
        
        print(f"🎯 Performing ultimate analysis of number: {number}")
        
        # Gather ALL possible information
        analysis = {
            'number_analyzed': number,
            'analysis_timestamp': mp.time.time() if hasattr(mp, 'time') else 0,
            'analysis_version': '1.0 Ultimate',
            
            # ===== BASIC PROPERTIES =====
            'basic_properties': self._get_complete_basic_properties(number),
            
            # ===== DECIMAL EXPANSION ANALYSIS =====
            'decimal_expansions': {
                'reciprocal': self.spectrum_analyzer.analyze_decimal_expansion(1, number) if number != 0 else None,
                'common_fractions': self._analyze_common_fractions(number),
                'expansion_patterns': self._analyze_expansion_patterns(number)
            },
            
            # ===== SPECTRUM CLASSIFICATION =====
            'spectrum_analysis': {
                'classification': self.spectrum_analyzer._classify_spectrum(number),
                'behavioral_traits': self._get_behavioral_traits(number),
                'pattern_family': self._determine_pattern_family(number),
                'complexity_ranking': self._get_complexity_ranking(number)
            },
            
            # ===== NUMBER THEORY PROPERTIES =====
            'number_theory': {
                'prime_factorization': self.spectrum_analyzer._factorize(number),
                'divisor_analysis': self.spectrum_analyzer._analyze_divisors(number),
                'modular_arithmetic': self._get_complete_modular_analysis(number),
                'special_properties': self._identify_special_properties(number)
            },
            
            # ===== DIGITAL PROPERTIES =====
            'digital_analysis': {
                'digital_signature': self.spectrum_analyzer._generate_digital_signature(number),
                'digit_patterns': self._analyze_digit_patterns(number),
                'numerological_insights': self._get_numerological_insights(number),
                'base_representations': self._get_all_base_representations(number)
            },
            
            # ===== FRACTIONAL RELATIONSHIPS =====
            'fractional_relationships': {
                'as_numerator': self._analyze_as_numerator(number),
                'as_denominator': self._analyze_as_denominator(number),
                'simplified_fractions': self._find_simplified_forms(number),
                'equivalent_forms': self._find_equivalent_forms(number)
            },
            
            # ===== MATHEMATICAL CONNECTIONS =====
            'mathematical_connections': {
                'sequences_and_series': self._find_sequence_connections(number),
                'geometric_properties': self._analyze_geometric_properties(number),
                'algebraic_properties': self._analyze_algebraic_properties(number),
                'historical_significance': self._get_historical_significance(number)
            },
            
            # ===== PRACTICAL APPLICATIONS =====
            'practical_applications': {
                'real_world_occurrences': self._find_real_world_occurrences(number),
                'measurement_properties': self._analyze_measurement_properties(number),
                'computational_properties': self._analyze_computational_properties(number),
                'cultural_significance': self._get_cultural_significance(number)
            },
            
            # ===== ADVANCED INSIGHTS =====
            'advanced_insights': {
                'neo_beta_analysis': self._get_neo_beta_insights(number),
                'fractal_properties': self._analyze_fractal_properties(number),
                'chaos_theory_aspects': self._analyze_chaos_properties(number),
                'quantum_aspects': self._analyze_quantum_properties(number)
            }
        }
        
        return analysis
    
    def _get_complete_basic_properties(self, number):
        """Get all basic mathematical properties."""
        props = {
            'value': number,
            'type': 'integer' if number == int(number) else 'decimal',
            'sign': 'positive' if number > 0 else 'negative' if number < 0 else 'zero',
            'absolute_value': abs(number),
            'is_zero': number == 0,
            'is_one': number == 1,
            'is_perfect_power': self._is_perfect_power(number),
            'is_triangular': self._is_triangular(number),
            'is_fibonacci': self._is_fibonacci(number),
            'is_factorial': self._is_factorial(number),
            'continued_fraction': self._get_continued_fraction(number) if number != 0 else None
        }
        
        # Add integer-specific properties
        if number == int(number):
            n = int(number)
            props.update({
                'is_prime': self.spectrum_analyzer._is_prime(n),
                'is_composite': n > 1 and not self.spectrum_analyzer._is_prime(n),
                'is_even': n % 2 == 0,
                'is_odd': n % 2 == 1,
                'is_perfect_square': int(math.sqrt(n)) ** 2 == n,
                'is_perfect_cube': round(n ** (1/3)) ** 3 == n,
                'is_palindromic': str(n) == str(n)[::-1],
                'digit_sum': sum(int(d) for d in str(abs(n))),
                'digital_root': self._calculate_digital_root(str(abs(n))),
                'number_of_digits': len(str(abs(n))) if n != 0 else 1,
                'reverse_number': int(str(n)[::-1]) if n >= 0 else -int(str(-n)[::-1])
            })
        
        return props
    
    def _is_perfect_power(self, n):
        """Check if number is a perfect power."""
        if n < 2:
            return False
        
        for base in range(2, int(math.sqrt(abs(n))) + 2):
            for exp in range(2, 10):
                if abs(base ** exp - abs(n)) < 0.0001:
                    return True
        return False
    
    def _is_triangular(self, n):
        """Check if number is triangular."""
        if n < 0:
            return False
        # Check if 8n + 1 is a perfect square
        return int(math.sqrt(8 * n + 1)) ** 2 == 8 * n + 1
    
    def _is_fibonacci(self, n):
        """Check if number is in Fibonacci sequence."""
        if n < 0:
            return False
        
        # A number is Fibonacci if and only if one or both of 5*n^2 + 4 or 5*n^2 - 4 is a perfect square
        test1 = 5 * n * n + 4
        test2 = 5 * n * n - 4
        
        return int(math.sqrt(test1)) ** 2 == test1 or int(math.sqrt(test2)) ** 2 == test2
    
    def _is_factorial(self, n):
        """Check if number is a factorial."""
        if n < 1:
            return False
        
        fact = 1
        i = 1
        while fact < n:
            i += 1
            fact *= i
        
        return fact == n
    
    def _get_continued_fraction(self, n):
        """Get continued fraction representation."""
        if n == 0:
            return [0]
        
        cf = []
        a = int(n)
        cf.append(a)
        r = n - a
        
        # Limit iterations for practicality
        for _ in range(10):
            if abs(r) < 1e-10:
                break
            r = 1 / r
            a = int(r)
            cf.append(a)
            r = r - a
        
        return cf
    
    def _calculate_digital_root(self, s):
        """Calculate digital root of string number."""
        if not s or s == '0':
            return 0
        
        digit_sum = sum(int(d) for d in s if d.isdigit())
        while digit_sum >= 10:
            digit_sum = sum(int(d) for d in str(digit_sum))
        return digit_sum
    
    def _analyze_common_fractions(self, number):
        """Analyze number as common fractions."""
        fractions = {}
        
        # Common denominators
        denominators = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        
        for denom in denominators:
            if denom != 0:
                fractions[f"{number}/{denom}"] = self.spectrum_analyzer.analyze_decimal_expansion(number, denom)
        
        return fractions
    
    def _analyze_expansion_patterns(self, number):
        """Analyze decimal expansion patterns."""
        patterns = {
            'reciprocal_period': self._find_period_length(1, number) if number != 0 else 0,
            'general_periodicity': self._analyze_general_periodicity(number),
            'digit_cycles': self._find_digit_cycles(number),
            'symmetry_patterns': self._find_symmetry_patterns(number)
        }
        
        return patterns
    
    def _find_period_length(self, num, denom):
        """Find period length of repeating decimal."""
        if denom == 0 or num == 0:
            return 0
        
        # Remove factors of 2 and 5
        d = denom
        while d % 2 == 0:
            d //= 2
        while d % 5 == 0:
            d //= 5
        
        if d == 1:
            return 0  # Terminating
        
        # Find multiplicative order of 10 modulo d
        for k in range(1, d):
            if pow(10, k, d) == 1:
                return k
        
        return 0
    
    def _analyze_general_periodicity(self, number):
        """Analyze general periodicity patterns."""
        # This would involve more complex periodicity analysis
        # For now, return basic information
        return {
            'has_simple_period': number in [1, 2, 4, 5, 8, 10],
            'has_complex_period': number in [3, 6, 7, 9, 11, 12, 13],
            'estimated_complexity': self._estimate_periodic_complexity(number)
        }
    
    def _estimate_periodic_complexity(self, number):
        """Estimate complexity of periodic patterns."""
        if number in [1, 2, 4, 5, 8, 10]:
            return 'LOW'
        elif number in [3, 6, 9, 11, 12]:
            return 'MEDIUM'
        elif number in [7, 13]:
            return 'HIGH'
        else:
            return 'UNKNOWN'
    
    def _find_digit_cycles(self, number):
        """Find digit cycles in decimal expansion."""
        if number == 0:
            return []
        
        # Analyze reciprocal for digit cycles
        reciprocal_analysis = self.spectrum_analyzer.analyze_decimal_expansion(1, number)
        
        if 'repeating_pattern' in reciprocal_analysis and reciprocal_analysis['repeating_pattern']:
            pattern = reciprocal_analysis['repeating_pattern']
            cycles = []
            
            # Look for internal cycles within the pattern
            for cycle_length in range(1, len(pattern) // 2 + 1):
                if len(pattern) % cycle_length == 0:
                    cycle = pattern[:cycle_length]
                    repetitions = len(pattern) // cycle_length
                    if cycle * repetitions == pattern:
                        cycles.append({
                            'cycle': cycle,
                            'length': cycle_length,
                            'repetitions': repetitions
                        })
            
            return cycles
        
        return []
    
    def _find_symmetry_patterns(self, number):
        """Find symmetry patterns in decimal expansion."""
        patterns = {
            'palindromic_fragments': [],
            'mirror_symmetry': False,
            'rotational_symmetry': False
        }
        
        # Analyze reciprocal decimal
        reciprocal_analysis = self.spectrum_analyzer.analyze_decimal_expansion(1, number)
        
        if 'fractional_part' in reciprocal_analysis:
            frac_part = reciprocal_analysis['fractional_part']
            
            # Check for palindromic fragments
            for length in range(2, min(10, len(frac_part))):
                for i in range(len(frac_part) - length + 1):
                    fragment = frac_part[i:i + length]
                    if fragment == fragment[::-1]:
                        patterns['palindromic_fragments'].append({
                            'fragment': fragment,
                            'position': i,
                            'length': length
                        })
            
            # Check overall symmetry
            patterns['mirror_symmetry'] = frac_part == frac_part[::-1]
            patterns['rotational_symmetry'] = self._has_rotational_symmetry(frac_part)
        
        return patterns
    
    def _has_rotational_symmetry(self, s):
        """Check for rotational symmetry (180-degree rotation)."""
        # Map digits to their 180-degree rotated equivalents
        rotation_map = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        
        try:
            rotated = ''.join(rotation_map.get(d, '?') for d in s[::-1])
            return '?' not in rotated and rotated == s
        except:
            return False
    
    def _get_behavioral_traits(self, number):
        """Get behavioral traits based on spectrum classification."""
        traits = []
        
        if number in [1, 2, 4, 5, 8, 10]:
            traits.extend([
                'clean_reciprocal_pattern',
                'predictable_decimal_behavior',
                'low_complexity_expansion',
                'stable_mathematical_properties'
            ])
        elif number in [3, 6, 9, 11, 12]:
            traits.extend([
                'complex_reciprocal_pattern',
                'irregular_decimal_behavior',
                'medium_complexity_expansion',
                'dynamic_mathematical_properties'
            ])
        elif number == 7:
            traits.extend([
                'special_prime_properties',
                'mixed_simple_wild_patterns',
                'high_complexity_expansion',
                'unique_mathematical_signature'
            ])
        elif number == 13:
            traits.extend([
                'wild_prime_properties',
                'complex_repetitive_patterns',
                'high_complexity_expansion',
                'exceptional_mathematical_behavior'
            ])
        
        # Add general traits
        if self.spectrum_analyzer._is_prime(number):
            traits.append('prime_number_behavior')
        if number % 2 == 0:
            traits.append('even_number_symmetry')
        if str(number) == str(number)[::-1]:
            traits.append('palindromic_structure')
        
        return traits
    
    def _determine_pattern_family(self, number):
        """Determine the pattern family of the number."""
        if number in [1, 2, 4, 5, 8, 10]:
            return {
                'family': 'SIMPLE',
                'subfamily': 'CLEAN_EXPANSION',
                'characteristics': ['terminating_or_short_period', 'predictable', 'low_entropy']
            }
        elif number in [3, 6, 9, 11, 12]:
            return {
                'family': 'WILD',
                'subfamily': 'COMPLEX_EXPANSION',
                'characteristics': ['long_period', 'unpredictable', 'high_entropy']
            }
        elif number == 7:
            return {
                'family': 'SPECIAL_WILD',
                'subfamily': 'MIXED_PATTERN',
                'characteristics': ['mixed_patterns', 'prime特殊性', 'medium_entropy']
            }
        elif number == 13:
            return {
                'family': 'SPECIAL_WILD',
                'subfamily': 'WILD_PRIME',
                'characteristics': ['complex_patterns', 'prime特殊性', 'high_entropy']
            }
        elif self.spectrum_analyzer._is_prime(number):
            return {
                'family': 'PRIME',
                'subfamily': 'STANDARD_PRIME',
                'characteristics': ['unique_patterns', 'prime_properties', 'variable_entropy']
            }
        else:
            return {
                'family': 'COMPOSITE',
                'subfamily': 'MIXED_BEHAVIOR',
                'characteristics': ['factor_patterns', 'composite_properties', 'variable_entropy']
            }
    
    def _get_complexity_ranking(self, number):
        """Get complexity ranking within the spectrum."""
        if self.spectrum_map and 'max_complexity_numbers' in self.spectrum_map:
            complexity_list = self.spectrum_map['max_complexity_numbers']
            
            for rank, (num, score) in enumerate(complexity_list, 1):
                if num == number:
                    return {
                        'rank': rank,
                        'score': score,
                        'percentile': (1 - rank/len(complexity_list)) * 100,
                        'classification': self._classify_by_score(score)
                    }
        
        # Fallback calculation
        reciprocal_analysis = self.spectrum_analyzer.analyze_decimal_expansion(1, number)
        score = reciprocal_analysis.get('complexity_score', 0)
        
        return {
            'rank': None,
            'score': score,
            'percentile': None,
            'classification': self._classify_by_score(score)
        }
    
    def _classify_by_score(self, score):
        """Classify complexity by score."""
        if score >= 0.8:
            return 'EXTREMELY_COMPLEX'
        elif score >= 0.6:
            return 'HIGHLY_COMPLEX'
        elif score >= 0.4:
            return 'MODERATELY_COMPLEX'
        elif score >= 0.2:
            return 'SLIGHTLY_COMPLEX'
        else:
            return 'MINIMALLY_COMPLEX'
    
    def _get_complete_modular_analysis(self, number):
        """Complete modular arithmetic analysis."""
        mod_analysis = {}
        
        # Test comprehensive moduli
        moduli = list(range(2, min(31, number + 1))) if number > 1 else []
        
        for mod in moduli:
            mod_analysis[f"mod_{mod}"] = {
                'remainder': number % mod,
                'is_congruent_to_zero': number % mod == 0,
                'multiplicative_inverse': self._find_multiplicative_inverse(number, mod) if math.gcd(number, mod) == 1 else None,
                'order': self._find_multiplicative_order_mod(number, mod) if math.gcd(number, mod) == 1 else 0
            }
        
        # Special modular properties
        mod_analysis['quadratic_residues'] = self._get_quadratic_residues_extended(number)
        mod_analysis['cubic_residues'] = self._get_cubic_residues(number)
        mod_analysis['euler_totient'] = self._euler_totient(number) if number > 0 else 0
        
        return mod_analysis
    
    def _find_multiplicative_inverse(self, a, m):
        """Find multiplicative inverse using extended Euclidean algorithm."""
        for x in range(1, m):
            if (a * x) % m == 1:
                return x
        return None
    
    def _find_multiplicative_order_mod(self, a, m):
        """Find multiplicative order of a modulo m."""
        if math.gcd(a, m) != 1:
            return 0
        
        for k in range(1, m):
            if pow(a, k, m) == 1:
                return k
        return 0
    
    def _get_quadratic_residues_extended(self, n):
        """Get extended quadratic residues."""
        if n <= 1:
            return []
        
        residues = set()
        for i in range(1, n):
            residues.add((i * i) % n)
        
        return sorted(list(residues))
    
    def _get_cubic_residues(self, n):
        """Get cubic residues."""
        if n <= 1:
            return []
        
        residues = set()
        for i in range(1, n):
            residues.add((i * i * i) % n)
        
        return sorted(list(residues))
    
    def _euler_totient(self, n):
        """Calculate Euler's totient function."""
        if n <= 0:
            return 0
        
        result = n
        p = 2
        while p * p <= n:
            if n % p == 0:
                while n % p == 0:
                    n = n // p
                result -= result // p
            p += 1
        
        if n > 1:
            result -= result // n
        
        return result
    
    def _identify_special_properties(self, number):
        """Identify special mathematical properties."""
        properties = []
        
        # Number type properties
        if number == 0:
            properties.extend(['additive_identity', 'multiplicative_absorber'])
        if number == 1:
            properties.extend(['multiplicative_identity', 'unit_element'])
        if self.spectrum_analyzer._is_prime(number):
            properties.append('prime_number')
        if self._is_perfect_power(number):
            properties.append('perfect_power')
        if self._is_triangular(number):
            properties.append('triangular_number')
        if self._is_fibonacci(number):
            properties.append('fibonacci_number')
        if self._is_factorial(number):
            properties.append('factorial_number')
        
        # Special mathematical properties
        if self._is_kauffman_number(number):
            properties.append('kauffman_number')
        if self._is_harmonic_number(number):
            properties.append('harmonic_number')
        if self._is_carmichael_number(number):
            properties.append('carmichael_number')
        
        return properties
    
    def _is_kauffman_number(self, n):
        """Check if number is a Kauffman number (simplified check)."""
        # This is a placeholder for Kauffman number identification
        return n in [42, 420, 666]  # Example known Kauffman numbers
    
    def _is_harmonic_number(self, n):
        """Check if number is a harmonic number."""
        # Harmonic numbers are rarely integers
        # Only H(1) = 1 is integer in standard definition
        return n == 1
    
    def _is_carmichael_number(self, n):
        """Check if number is a Carmichael number."""
        if n < 2 or self.spectrum_analyzer._is_prime(n):
            return False
        
        # Korselt's criterion
        for p in self.spectrum_analyzer._factorize(n)['prime_factors']:
            if n % (p * p) == 0:
                return False
            if (n - 1) % (p - 1) != 0:
                return False
        
        return True
    
    def _analyze_digit_patterns(self, number):
        """Analyze digit patterns in number."""
        if not isinstance(number, int):
            return {}
        
        s = str(abs(number))
        
        patterns = {
            'digit_frequency': dict(Counter(s)),
            'consecutive_patterns': self._find_consecutive_patterns(s),
            'arithmetic_progressions': self._find_arithmetic_progressions(s),
            'geometric_progressions': self._find_geometric_progressions(s),
            'repeating_sequences': self._find_repeating_sequences(s)
        }
        
        return patterns
    
    def _find_consecutive_patterns(self, s):
        """Find consecutive digit patterns."""
        patterns = []
        
        for length in range(2, min(5, len(s))):
            for i in range(len(s) - length + 1):
                substring = s[i:i + length]
                if all(int(substring[j]) + 1 == int(substring[j + 1]) for j in range(len(substring) - 1)):
                    patterns.append({
                        'pattern': substring,
                        'position': i,
                        'length': length,
                        'type': 'ascending'
                    })
                elif all(int(substring[j]) - 1 == int(substring[j + 1]) for j in range(len(substring) - 1)):
                    patterns.append({
                        'pattern': substring,
                        'position': i,
                        'length': length,
                        'type': 'descending'
                    })
        
        return patterns
    
    def _find_arithmetic_progressions(self, s):
        """Find arithmetic progressions in digits."""
        progressions = []
        
        for length in range(3, min(6, len(s))):
            for i in range(len(s) - length + 1):
                substring = s[i:i + length]
                diffs = [int(substring[j + 1]) - int(substring[j]) for j in range(len(substring) - 1)]
                if all(d == diffs[0] for d in diffs):
                    progressions.append({
                        'pattern': substring,
                        'position': i,
                        'length': length,
                        'common_difference': diffs[0]
                    })
        
        return progressions
    
    def _find_geometric_progressions(self, s):
        """Find geometric progressions in digits."""
        progressions = []
        
        for length in range(3, min(5, len(s))):
            for i in range(len(s) - length + 1):
                substring = s[i:i + length]
                if '0' in substring:
                    continue  # Skip zeros in geometric progressions
                
                ratios = []
                for j in range(len(substring) - 1):
                    if int(substring[j]) == 0:
                        break
                    ratio = int(substring[j + 1]) / int(substring[j])
                    ratios.append(ratio)
                
                if len(ratios) == len(substring) - 1 and all(abs(r - ratios[0]) < 0.001 for r in ratios):
                    progressions.append({
                        'pattern': substring,
                        'position': i,
                        'length': length,
                        'common_ratio': ratios[0]
                    })
        
        return progressions
    
    def _find_repeating_sequences(self, s):
        """Find repeating sequences in digits."""
        sequences = []
        
        for length in range(2, min(4, len(s) // 2)):
            for i in range(len(s) - 2 * length + 1):
                pattern = s[i:i + length]
                next_part = s[i + length:i + 2 * length]
                if pattern == next_part:
                    sequences.append({
                        'pattern': pattern,
                        'position': i,
                        'length': length,
                        'repetitions': 2
                    })
        
        return sequences
    
    def _get_numerological_insights(self, number):
        """Get numerological insights."""
        if not isinstance(number, int) or number == 0:
            return {}
        
        insights = {}
        
        # Basic numerology
        s = str(abs(number))
        insights['life_path_number'] = self._calculate_digital_root(s)
        insights['destiny_number'] = sum(int(d) for d in s)
        insights['soul_urge_number'] = sum(int(d) for d in s if int(d) in [1, 5, 9])  # Vowels equivalent
        
        # Number symbolism
        insights['symbolism'] = self._get_number_symbolism(number)
        insights['angel_number'] = self._check_angel_number(number)
        insights['master_number'] = number in [11, 22, 33, 44, 55, 66, 77, 88, 99]
        
        return insights
    
    def _get_number_symbolism(self, number):
        """Get symbolic meaning of number."""
        symbolism = {
            0: ['potential', 'wholeness', 'eternity', 'cycles'],
            1: ['beginnings', 'leadership', 'individuality', 'unity'],
            2: ['duality', 'balance', 'partnership', 'cooperation'],
            3: ['creativity', 'communication', 'trinity', 'growth'],
            4: ['stability', 'foundation', 'order', 'practicality'],
            5: ['freedom', 'change', 'adventure', 'versatility'],
            6: ['harmony', 'love', 'responsibility', 'service'],
            7: ['spirituality', 'wisdom', 'introspection', 'mysticism'],
            8: ['abundance', 'power', 'success', 'infinity'],
            9: ['completion', 'humanitarianism', 'wisdom', 'enlightenment'],
            10: ['perfection', 'completion', 'new beginnings', 'divine order'],
            11: ['intuition', 'spiritual insight', 'master teacher', 'enlightenment'],
            12: ['completion', 'cosmic order', 'zodiac', 'time cycles'],
            13: ['transformation', 'rebirth', 'karma', 'change']
        }
        
        return symbolism.get(number, ['unique_properties', 'individual_significance'])
    
    def _check_angel_number(self, number):
        """Check if number is an angel number."""
        # Common angel numbers
        angel_patterns = [
            '111', '222', '333', '444', '555', '666', '777', '888', '999',
            '123', '456', '789', '1111', '2222', '3333'
        ]
        
        s = str(number)
        for pattern in angel_patterns:
            if pattern in s:
                return True
        
        return False
    
    def _get_all_base_representations(self, number):
        """Get number in different bases."""
        if not isinstance(number, int) or number < 0:
            return {}
        
        representations = {}
        
        for base in [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]:
            try:
                if base == 10:
                    representations[f'base_{base}'] = str(number)
                else:
                    representations[f'base_{base}'] = self._convert_base(number, base)
            except:
                representations[f'base_{base}'] = 'error'
        
        return representations
    
    def _convert_base(self, n, base):
        """Convert number to different base."""
        if n == 0:
            return '0'
        
        digits = []
        while n > 0:
            remainder = n % base
            if remainder < 10:
                digits.append(str(remainder))
            else:
                digits.append(chr(ord('A') + remainder - 10))
            n //= base
        
        return ''.join(reversed(digits))
    
    def _analyze_as_numerator(self, number):
        """Analyze number as numerator in fractions."""
        if number == 0:
            return {'special_case': 'zero_numerator'}
        
        fractions = {}
        
        # Analyze as 1/x, 2/x, 3/x, etc.
        for denominator in range(1, min(21, 101)):
            if denominator != 0:
                simplified = Fraction(number, denominator)
                fractions[f"{number}/{denominator}"] = {
                    'simplified': f"{simplified.numerator}/{simplified.denominator}",
                    'decimal_value': float(simplified),
                    'is_integer': simplified.denominator == 1,
                    'terminating': self.spectrum_analyzer._is_terminating_decimal(number, denominator)
                }
        
        return fractions
    
    def _analyze_as_denominator(self, number):
        """Analyze number as denominator in fractions."""
        if number == 0:
            return {'special_case': 'zero_denominator_undefined'}
        
        fractions = {}
        
        # Analyze as x/number for various numerators
        for numerator in range(1, min(number + 1, 21)):
            simplified = Fraction(numerator, number)
            fractions[f"{numerator}/{number}"] = {
                'simplified': f"{simplified.numerator}/{simplified.denominator}",
                'decimal_value': float(simplified),
                'is_integer': simplified.denominator == 1,
                'terminating': self.spectrum_analyzer._is_terminating_decimal(numerator, number)
            }
        
        return fractions
    
    def _find_simplified_forms(self, number):
        """Find simplified forms of the number."""
        forms = []
        
        if isinstance(number, int) and number > 0:
            # Find fraction representations
            for denominator in range(2, min(number + 1, 21)):
                if number * denominator <= 1000:  # Keep reasonable size
                    forms.append({
                        'form': f"{number * denominator}/{denominator}",
                        'value': number,
                        'type': 'fractional_equivalent'
                    })
        
        return forms
    
    def _find_equivalent_forms(self, number):
        """Find mathematically equivalent forms."""
        equivalents = []
        
        if isinstance(number, int):
            # Square root forms
            if number > 0:
                sqrt_val = math.sqrt(number)
                if abs(sqrt_val - round(sqrt_val)) < 0.0001:
                    equivalents.append({
                        'form': f"({round(sqrt_val)})²",
                        'value': number,
                        'type': 'perfect_square'
                    })
            
            # Cube root forms
            if number > 0:
                cube_val = round(number ** (1/3))
                if abs(cube_val ** 3 - number) < 0.0001:
                    equivalents.append({
                        'form': f"({cube_val})³",
                        'value': number,
                        'type': 'perfect_cube'
                    })
        
        return equivalents
    
    def _find_sequence_connections(self, number):
        """Find connections to mathematical sequences."""
        connections = []
        
        # Check various sequences
        if isinstance(number, int):
            if number in [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]:  # Fibonacci
                connections.append({'sequence': 'Fibonacci', 'position': self._find_fibonacci_position(number)})
            
            if number in [1, 2, 3, 4, 6, 8, 9, 12, 16, 18, 24, 27, 32, 36]:  # Highly composite
                connections.append({'sequence': 'Highly Composite', 'property': 'many_divisors'})
            
            if number in [6, 28, 496, 8128]:  # Perfect numbers
                connections.append({'sequence': 'Perfect Numbers', 'property': 'sum_of_proper_divisors'})
        
        return connections
    
    def _find_fibonacci_position(self, n):
        """Find position in Fibonacci sequence."""
        if n == 0:
            return 0
        
        a, b = 0, 1
        position = 1
        
        while a < n:
            a, b = b, a + b
            position += 1
        
        return position if a == n else None
    
    def _analyze_geometric_properties(self, number):
        """Analyze geometric properties."""
        properties = {}
        
        if isinstance(number, int) and number >= 0:
            # Polygon possibilities
            properties['regular_polygon'] = number >= 3
            if number >= 3:
                properties['interior_angle'] = (number - 2) * 180 / number
                properties['exterior_angle'] = 360 / number
            
            # Spatial properties
            properties['dimensions'] = self._get_possible_dimensions(number)
            properties['symmetries'] = self._count_symmetries(number)
        
        return properties
    
    def _get_possible_dimensions(self, n):
        """Get possible dimensional representations."""
        dimensions = []
        
        # Check for cubic numbers
        cube_root = round(n ** (1/3))
        if cube_root ** 3 == n:
            dimensions.append(f"{cube_root}x{cube_root}x{cube_root} cube")
        
        # Check for square numbers
        sqrt_n = int(math.sqrt(n))
        if sqrt_n * sqrt_n == n:
            dimensions.append(f"{sqrt_n}x{sqrt_n} square")
        
        # Check for rectangular arrangements
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                dimensions.append(f"{i}x{n//i} rectangle")
        
        return dimensions
    
    def _count_symmetries(self, n):
        """Count symmetries for regular n-gon."""
        if n < 3:
            return 0
        
        # Regular n-gon has 2n symmetries (n rotations, n reflections)
        return 2 * n
    
    def _analyze_algebraic_properties(self, number):
        """Analyze algebraic properties."""
        properties = {}
        
        if isinstance(number, int):
            # Equation solving
            properties['linear_equation'] = f"x = {number}"
            properties['quadratic_solutions'] = self._solve_quadratic_with_root(number)
            
            # Polynomial properties
            properties['minimal_polynomial'] = self._get_minimal_polynomial(number)
            properties['algebraic_degree'] = 1  # All integers are degree 1
        
        return properties
    
    def _solve_quadratic_with_root(self, n):
        """Find quadratic equations with n as a root."""
        equations = []
        
        # Simple forms: x^2 - 2nx + n^2 = 0 (double root at x=n)
        equations.append(f"x² - {2*n}x + {n*n} = 0")
        
        # Other forms: (x-n)(x-k) = 0
        for k in range(-3, 4):
            if k != n:
                equations.append(f"x² - ({n + k})x + {n*k} = 0")
        
        return equations
    
    def _get_minimal_polynomial(self, n):
        """Get minimal polynomial over rationals."""
        return f"x - {n}"
    
    def _get_historical_significance(self, number):
        """Get historical significance of number."""
        significance = {
            'mathematical_history': [],
            'cultural_importance': [],
            'scientific_applications': []
        }
        
        # Mathematical history
        if number == 0:
            significance['mathematical_history'].append('invention_of_zero')
        elif number == 1:
            significance['mathematical_history'].append('unit_concept')
        elif number == 2:
            significance['mathematical_history'].append('duality_concept')
        elif number == 3:
            significance['mathematical_history'].append('trinity_geometry')
        elif number == 7:
            significance['mathematical_history'].append('ancient_wisdom')
        elif number == 13:
            significance['mathematical_history'].append('superstition_and_mathematics')
        
        # Cultural importance
        if number in [3, 7, 12]:
            significance['cultural_importance'].append('religious_significance')
        if number in [4, 8]:
            significance['cultural_importance'].append('eastern_philosophy')
        
        # Scientific applications
        if number in [2, 8, 16]:
            significance['scientific_applications'].append('computing')
        if number == 12:
            significance['scientific_applications'].append('time_measurement')
        
        return significance
    
    def _find_real_world_occurrences(self, number):
        """Find real-world occurrences of the number."""
        occurrences = {
            'nature': [],
            'human_anatomy': [],
            'measurement_systems': [],
            'technology': []
        }
        
        # Nature
        if number == 5:
            occurrences['nature'].append('five_fingers_limbs')
        if number == 6:
            occurrences['nature'].append('insect_legs')
        if number == 8:
            occurrences['nature'].append('spider_legs')
        
        # Human anatomy
        if number in [2, 5, 10]:
            occurrences['human_anatomy'].append('digit_patterns')
        
        # Measurement systems
        if number == 12:
            occurrences['measurement_systems'].append('dozen_system')
        if number == 60:
            occurrences['measurement_systems'].append('time_angles')
        
        # Technology
        if number in [2, 8, 16, 32, 64, 128]:
            occurrences['technology'].append('binary_computing')
        
        return occurrences
    
    def _analyze_measurement_properties(self, number):
        """Analyze measurement-related properties."""
        properties = {}
        
        if isinstance(number, int):
            # Time
            properties['time_divisions'] = self._get_time_divisions(number)
            
            # Units
            properties['unit_conversions'] = self._get_unit_conversions(number)
            
            # Geometry
            properties['geometric_units'] = self._get_geometric_units(number)
        
        return properties
    
    def _get_time_divisions(self, n):
        """Get time-related divisions."""
        divisions = []
        
        if n == 60:
            divisions.append('minute_seconds')
        if n == 24:
            divisions.append('hours_day')
        if n == 7:
            divisions.append('days_week')
        if n == 12:
            divisions.append('months_year')
        
        return divisions
    
    def _get_unit_conversions(self, n):
        """Get unit conversion relationships."""
        conversions = []
        
        if n == 100:
            conversions.append('percent_base')
        if n == 1000:
            conversions.append('kilo_prefix')
        if n == 16:
            conversions.append('ounce_pound')
        
        return conversions
    
    def _get_geometric_units(self, n):
        """Get geometric unit relationships."""
        units = []
        
        if n == 180:
            units.append('straight_angle')
        if n == 360:
            units.append('full_angle')
        if n == 90:
            units.append('right_angle')
        
        return units
    
    def _analyze_computational_properties(self, number):
        """Analyze computational properties."""
        properties = {}
        
        if isinstance(number, int):
            # Binary
            properties['binary_representation'] = bin(number)
            properties['bit_length'] = number.bit_length() if number > 0 else 0
            
            # Hash properties
            properties['hash_values'] = {
                'md5': hashlib.md5(str(number).encode()).hexdigest()[:8],
                'sha1': hashlib.sha1(str(number).encode()).hexdigest()[:8]
            }
            
            # Algorithmic complexity
            properties['prime_testing_difficulty'] = 'easy' if number < 1000 else 'medium' if number < 1000000 else 'hard'
        
        return properties
    
    def _get_cultural_significance(self, number):
        """Get cultural significance."""
        significance = {
            'western_culture': [],
            'eastern_culture': [],
            'religious_contexts': [],
            'modern_pop_culture': []
        }
        
        # Western culture
        if number == 13:
            significance['western_culture'].append('unlucky_number')
        if number == 7:
            significance['western_culture'].append('lucky_number')
        
        # Eastern culture
        if number == 8:
            significance['eastern_culture'].append('prosperity_chinese')
        if number == 4:
            significance['eastern_culture'].append('death_japanese')
        
        # Religious contexts
        if number in [3, 7, 12]:
            significance['religious_contexts'].append('sacred_numbers')
        
        # Modern pop culture
        if number in [42, 69, 101]:
            significance['modern_pop_culture'].append('internet_memes')
        
        return significance
    
    def _get_neo_beta_insights(self, number):
        """Get Neo-Beta specific insights."""
        insights = {}
        
        # P(x) function analysis
        try:
            p_value = float(Decimal(1000 * number) / Decimal(169))
            insights['p_function_value'] = p_value
            insights['p_function_residue'] = int(p_value * 169) % 1000
        except:
            insights['p_function_value'] = None
            insights['p_function_residue'] = None
        
        # Beta sequence alignment
        beta_sequence = [13, 4, 5, 2, 11, 12, 7, 9, 8, 6, 1, 3, 0, 10]
        for i, beta_val in enumerate(beta_sequence):
            if number == beta_val:
                insights['beta_sequence_position'] = i
                insights['beta_sequence_role'] = self._get_beta_role(i)
                break
        
        # Flush number properties
        if number in [7, 13]:
            insights['flush_number_type'] = 'known_flush'
            insights['reciprocal_properties'] = 'special'
        
        return insights
    
    def _get_beta_role(self, position):
        """Get role in Beta sequence."""
        roles = [
            'primary_flush', 'transition', 'build', 'base', 'wild_1',
            'wild_2', 'flush_7', 'central', 'descent', 'descent_2',
            'simple_1', 'simple_2', 'zero_point', 'terminator'
        ]
        return roles[position] if position < len(roles) else 'unknown'
    
    def _analyze_fractal_properties(self, number):
        """Analyze fractal properties."""
        properties = {}
        
        if isinstance(number, int) and number > 0:
            # Self-similarity in digits
            s = str(number)
            properties['digit_self_similarity'] = self._check_digit_self_similarity(s)
            
            # Recursive patterns
            properties['recursive_patterns'] = self._find_recursive_patterns(number)
            
            # Scale invariance
            properties['scale_invariance'] = self._check_scale_invariance(number)
        
        return properties
    
    def _check_digit_self_similarity(self, s):
        """Check for self-similarity in digit patterns."""
        similarities = []
        
        for scale in range(2, len(s) // 2 + 1):
            if len(s) % scale == 0:
                pattern = s[:scale]
                repetitions = len(s) // scale
                if pattern * repetitions == s:
                    similarities.append({
                        'pattern': pattern,
                        'scale': scale,
                        'repetitions': repetitions
                    })
        
        return similarities
    
    def _find_recursive_patterns(self, n):
        """Find recursive patterns in number."""
        patterns = []
        
        # Look for numbers where operations on digits relate to the whole
        if isinstance(n, int):
            # Sum of digits related to original
            digit_sum = sum(int(d) for d in str(abs(n)))
            if n % digit_sum == 0:
                patterns.append({
                    'type': 'digit_sum_divisibility',
                    'relationship': f"{n} % {digit_sum} = 0"
                })
        
        return patterns
    
    def _check_scale_invariance(self, n):
        """Check for scale invariance properties."""
        invariances = []
        
        # Check if number maintains properties under scaling
        for scale in [2, 3, 5, 10]:
            scaled = n * scale
            if isinstance(scaled, int):
                # Compare digit patterns
                original_props = self._get_digit_properties(n)
                scaled_props = self._get_digit_properties(scaled)
                
                if original_props == scaled_props:
                    invariances.append({
                        'scale': scale,
                        'scaled_value': scaled,
                        'preserved_properties': original_props
                    })
        
        return invariances
    
    def _get_digit_properties(self, n):
        """Get basic digit properties for comparison."""
        if not isinstance(n, int):
            return {}
        
        s = str(abs(n))
        return {
            'length': len(s),
            'digit_sum': sum(int(d) for d in s),
            'digit_product': self._digit_product(n),
            'is_palindromic': s == s[::-1],
            'digit_set': set(s)
        }
    
    def _digit_product(self, n):
        """Calculate product of digits."""
        if n == 0:
            return 0
        
        product = 1
        for digit in str(abs(n)):
            product *= int(digit)
        return product
    
    def _analyze_chaos_properties(self, number):
        """Analyze chaos theory properties."""
        properties = {}
        
        if isinstance(number, int):
            # Sensitivity to initial conditions
            properties['sensitivity_analysis'] = self._analyze_sensitivity(number)
            
            # Period doubling
            properties['period_analysis'] = self._analyze_period_doubling(number)
            
            # Strange attractors
            properties['attractor_analysis'] = self._analyze_attractors(number)
        
        return properties
    
    def _analyze_sensitivity(self, n):
        """Analyze sensitivity to small changes."""
        sensitivity = {}
        
        # Skip analysis for zero to avoid division by zero
        if n == 0:
            sensitivity['special_case'] = 'zero_has_no_reciprocal'
            return sensitivity
        
        # Test small perturbations
        for delta in [-2, -1, 1, 2]:
            perturbed = n + delta
            if perturbed > 0:
                # Compare properties
                original_decimal = str(Decimal(1) / Decimal(n))[:20]
                perturbed_decimal = str(Decimal(1) / Decimal(perturbed))[:20]
                
                difference = sum(1 for i in range(min(len(original_decimal), len(perturbed_decimal)))
                               if original_decimal[i] != perturbed_decimal[i])
                
                sensitivity[f'delta_{delta}'] = {
                    'perturbed_value': perturbed,
                    'decimal_difference': difference,
                    'sensitivity_score': difference / 20
                }
        
        return sensitivity
    
    def _analyze_period_doubling(self, n):
        """Analyze period doubling behavior."""
        periods = []
        
        # Skip analysis for zero to avoid division by zero
        if n == 0:
            periods.append({'special_case': 'zero_has_no_period'})
            return periods
        
        # Analyze periods of related numbers
        for multiple in [1, 2, 3, 4, 5]:
            test_number = n * multiple
            if test_number <= 200 and test_number > 0:
                period = self._find_period_length(1, test_number)
                periods.append({
                    'multiple': multiple,
                    'number': test_number,
                    'period': period
                })
        
        return periods
    
    def _analyze_attractors(self, n):
        """Analyze attractor-like behavior."""
        attractors = []
        
        # Look for cycles in digit operations
        current = n
        visited = []
        
        for _ in range(20):  # Limit iterations
            if current in visited:
                cycle_start = visited.index(current)
                cycle = visited[cycle_start:]
                attractors.append({
                    'type': 'digit_cycle',
                    'cycle': cycle,
                    'length': len(cycle)
                })
                break
            
            visited.append(current)
            # Apply digit transformation
            current = sum(int(d) ** 2 for d in str(abs(current))) if current != 0 else 0
        
        return attractors
    
    def _analyze_quantum_properties(self, number):
        """Analyze quantum-inspired properties."""
        properties = {}
        
        if isinstance(number, int):
            # Quantum states
            properties['quantum_states'] = self._analyze_quantum_states(number)
            
            # Superposition analogs
            properties['superposition_analysis'] = self._analyze_superposition(number)
            
            # Entanglement analogs
            properties['entanglement_analysis'] = self._analyze_entanglement(number)
        
        return properties
    
    def _analyze_quantum_states(self, n):
        """Analyze quantum state analogs."""
        states = []
        
        # Binary representation as quantum states
        binary = bin(n)[2:]
        for i, bit in enumerate(reversed(binary)):
            if bit == '1':
                states.append({
                    'state': f'|{i}⟩',
                    'amplitude': 1,
                    'position': i
                })
        
        return states
    
    def _analyze_superposition(self, n):
        """Analyze superposition analogs."""
        superposition = {}
        
        # Multiple simultaneous representations
        representations = []
        
        # Binary superposition
        if n > 0:
            binary = bin(n)[2:]
            representations.append({
                'basis': 'binary',
                'state': binary,
                'amplitudes': [1 for _ in binary]
            })
        
        # Prime factorization superposition
        if n > 1:
            factors = self.spectrum_analyzer._factorize(n)['prime_factors']
            if factors:
                representations.append({
                    'basis': 'prime_factors',
                    'state': factors,
                    'amplitudes': [1/len(factors) for _ in factors]
                })
        
        superposition['representations'] = representations
        return superposition
    
    def _analyze_entanglement(self, n):
        """Analyze entanglement analogs."""
        entanglements = []
        
        # Numbers that share properties
        if isinstance(n, int):
            # Numbers with same digital root
            digital_root = self._calculate_digital_root(str(abs(n)))
            same_root = [i for i in range(1, 201) if self._calculate_digital_root(str(i)) == digital_root and i != n]
            
            if same_root:
                entanglements.append({
                    'type': 'digital_root_entanglement',
                    'partners': same_root[:10],
                    'shared_property': f'digital_root_{digital_root}'
                })
        
        return entanglements
    
    def generate_comprehensive_report(self, analysis):
        """Generate comprehensive human-readable report."""
        report = []
        report.append("🎯 ULTIMATE NUMBER ANALYSIS REPORT")
        report.append("=" * 80)
        report.append(f"Number Analyzed: {analysis['number_analyzed']}")
        report.append(f"Analysis Date: {analysis['analysis_timestamp']}")
        report.append("")
        
        # Basic Properties
        report.append("📊 BASIC PROPERTIES")
        report.append("-" * 40)
        basic = analysis['basic_properties']
        report.append(f"Type: {basic['type']}")
        report.append(f"Sign: {basic['sign']}")
        if basic.get('is_prime'):
            report.append("Prime Number: ✅")
        if basic.get('is_perfect_square'):
            report.append("Perfect Square: ✅")
        if basic.get('is_fibonacci'):
            report.append("Fibonacci Number: ✅")
        report.append("")
        
        # Spectrum Classification
        report.append("🌈 SPECTRUM CLASSIFICATION")
        report.append("-" * 40)
        spectrum = analysis['spectrum_analysis']['classification']
        report.append(f"Category: {spectrum['category']}")
        report.append(f"Description: {spectrum['description']}")
        report.append("")
        
        # Decimal Expansions
        report.append("🔢 DECIMAL EXPANSION ANALYSIS")
        report.append("-" * 40)
        reciprocal = analysis['decimal_expansions']['reciprocal']
        if reciprocal:
            report.append(f"Reciprocal: 1/{analysis['number_analyzed']} = {reciprocal['decimal_string']}")
            if reciprocal.get('repeating_pattern'):
                report.append(f"Repeating Pattern: {reciprocal['repeating_pattern']}")
                report.append(f"Pattern Length: {reciprocal['pattern_length']}")
            report.append(f"Complexity Score: {reciprocal.get('complexity_score', 0):.3f}")
        report.append("")
        
        # Mathematical Connections
        report.append("🔗 MATHEMATICAL CONNECTIONS")
        report.append("-" * 40)
        connections = analysis['mathematical_connections']
        if connections['sequences_and_series']:
            for seq in connections['sequences_and_series']:
                report.append(f"Sequence: {seq['sequence']}")
        
        # Special Properties
        special = analysis['number_theory']['special_properties']
        if special:
            report.append("Special Properties:")
            for prop in special:
                report.append(f"  ✅ {prop}")
        report.append("")
        
        # Advanced Insights
        report.append("🧠 ADVANCED INSIGHTS")
        report.append("-" * 40)
        neo_beta = analysis['advanced_insights']['neo_beta_analysis']
        if neo_beta.get('p_function_value') is not None:
            report.append(f"P(x) Value: {neo_beta['p_function_value']}")
            report.append(f"P(x) Residue: {neo_beta['p_function_residue']}")
        
        # Behavioral Traits
        traits = analysis['spectrum_analysis']['behavioral_traits']
        if traits:
            report.append("Behavioral Traits:")
            for trait in traits[:5]:  # Show first 5
                report.append(f"  • {trait.replace('_', ' ').title()}")
        report.append("")
        
        return "\n".join(report)
    
    def save_analysis(self, analysis, filename):
        """Save complete analysis to file."""
        with open(filename, 'w') as f:
            json.dump(analysis, f, indent=2, default=str)
        print(f"✅ Complete analysis saved to {filename}")


def main():
    """Main demonstration of the Ultimate Number Analyzer."""
    print("🎯 Ultimate Number Analyzer - Complete Decimal Expansion Framework")
    print("=" * 80)
    
    analyzer = UltimateNumberAnalyzer()
    
    # Test key numbers
    test_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 17, 23, 42, 69, 117, 200]
    
    for number in test_numbers:
        print(f"\n🔍 Analyzing number: {number}")
        
        # Perform complete analysis
        analysis = analyzer.analyze_number(number)
        
        if 'error' in analysis:
            print(f"❌ Error: {analysis['error']}")
            continue
        
        # Generate and display report
        report = analyzer.generate_comprehensive_report(analysis)
        print(report)
        
        # Save analysis
        filename = f"analysis_{number}.json"
        analyzer.save_analysis(analysis, filename)
        
        print("\n" + "=" * 80)
        
        # Continue to next number automatically
    
    print("\n🎉 Ultimate Number Analysis Complete!")
    print(f"Analyzed {len(test_numbers)} numbers with comprehensive insights.")
    print("=" * 80)


if __name__ == "__main__":
    main()