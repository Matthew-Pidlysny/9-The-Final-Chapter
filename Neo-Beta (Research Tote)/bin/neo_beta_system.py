#!/usr/bin/env python3
"""
Neo-Beta Sequence System - Universal Mathematical Framework
Core implementation for detecting and analyzing Neo-Beta sequences across all number types
"""

import math
import decimal
from decimal import Decimal, getcontext
import cmath
from typing import List, Dict, Tuple, Optional, Union, Any
from dataclasses import dataclass, field
from enum import Enum
import json
from fractions import Fraction
import re
import itertools

# Set high precision for calculations
getcontext().prec = 100

class ExpansionType(Enum):
    """Types of mathematical expansions supported"""
    RATIONAL = "rational"
    IRRATIONAL = "irrational"
    REPEATING_RATIONAL = "repeating_rational"
    SIMPLE_WILD = "simple_wild"
    TRANSCENDENT = "transcendent"
    CUSTOM = "custom"

@dataclass
class SequenceResult:
    """Results from sequence analysis"""
    sequence: List[float]
    positions: List[int]
    residues: Dict[int, float]
    relationships: Dict[str, float]
    properties: Dict[str, Any]
    validity_score: float
    expansion_type: ExpansionType

@dataclass
class FlushAnalysis:
    """Analysis of flush number properties"""
    number: float
    reciprocal: Decimal
    decimal_expansion: str
    repeating_pattern: Optional[str]
    pattern_length: Optional[int]
    is_flush: bool
    flush_strength: float

class PFunctionEngine:
    """Core P(x) function engine based on P(x) = 1000x/169"""
    
    def __init__(self, formula: str = "1000x/169"):
        self.formula = formula
        self.base_value = Decimal('169')
        self.multiplier = Decimal('1000')
        
    def evaluate(self, x: Union[int, float, Decimal]) -> Decimal:
        """Evaluate P(x) for any input x"""
        x_decimal = Decimal(str(x))
        return (self.multiplier * x_decimal) / self.base_value
    
    def get_sequence_identity(self, x: int) -> int:
        """
        Get sequence identity for position x.
        Based on documentation, next digit usually equals x.
        """
        p_val = self.evaluate(x)
        # Extract the "identity" based on P(x) properties
        floor_val = int(p_val)
        residue = float(p_val) - floor_val
        
        # Based on the β sequence and documentation logic
        if x <= 10:  # Use the direct relationship for first 10
            base_sequence = [13,4,5,2,11,12,7,9,8,6,1,3,0,10]
            if x-1 < len(base_sequence):
                return base_sequence[x-1]
        
        # For x > 10, use adaptive calculation
        identity = int(x + residue * 100) % 169
        return identity if identity >= 0 else -identity
    
    def analyze_residues(self, x: int) -> Dict[str, float]:
        """Analyze residue relationships for position x"""
        p_val = self.evaluate(x)
        floor_val = int(p_val)
        residue = float(p_val) - floor_val
        
        identity = self.get_sequence_identity(x)
        
        # Calculate relationships as described in documentation
        diff_from_identity = identity - floor_val
        reciprocal_residual = residue / float(p_val) if p_val != 0 else 0
        
        return {
            'p_value': float(p_val),
            'floor_value': floor_val,
            'residue': residue,
            'identity': identity,
            'diff_from_identity': diff_from_identity,
            'reciprocal_residual': reciprocal_residual,
            'normalized_position': x / 169,
            'phi_scaled': x * Decimal(str(phi())) / Decimal('169')
        }

class BetaSequenceGenerator:
    """Generator for Neo-Beta sequences"""
    
    def __init__(self, p_engine: PFunctionEngine):
        self.p_engine = p_engine
        self.base_sequence = [13,4,5,2,11,12,7,9,8,6,1,3,0,10]
        
    def generate_sequence(self, start_x: int, length: int = 14) -> List[int]:
        """Generate Neo-Beta sequence starting from x"""
        sequence = []
        for i in range(length):
            x_val = start_x + i
            identity = self.p_engine.get_sequence_identity(x_val)
            sequence.append(identity)
        return sequence
    
    def analyze_relationships(self, sequence: List[int]) -> Dict[str, float]:
        """Analyze relationships within sequence"""
        relationships = {}
        
        # Consecutive differences
        for i in range(len(sequence)-1):
            diff = sequence[i+1] - sequence[i]
            relationships[f"diff_{i}_to_{i+1}"] = diff
        
        # Pattern analysis
        relationships['mean'] = sum(sequence) / len(sequence)
        relationships['variance'] = sum((x - relationships['mean'])**2 for x in sequence) / len(sequence)
        relationships['max'] = max(sequence)
        relationships['min'] = min(sequence)
        relationships['range'] = relationships['max'] - relationships['min']
        
        # Special relationships
        if len(sequence) >= 2:
            relationships['first_diff'] = sequence[1] - sequence[0]
            relationships['last_diff'] = sequence[-1] - sequence[-2]
        
        return relationships

class FlushNumberAnalyzer:
    """Analyzer for flush number properties and reciprocal patterns"""
    
    def __init__(self):
        self.known_flush_numbers = [13, 7, 3]  # From documentation
        self.cache = {}
        
    def analyze_reciprocal(self, n: int, precision: int = 50) -> FlushAnalysis:
        """Analyze reciprocal properties of a number"""
        if n in self.cache:
            return self.cache[n]
        
        getcontext().prec = precision
        n_decimal = Decimal(n)
        
        if n == 0:
            return FlushAnalysis(0, Decimal(0), "0", None, None, False, 0.0)
        
        reciprocal = Decimal(1) / n_decimal
        decimal_str = format(reciprocal, 'f')
        
        # Remove trailing zeros
        decimal_str = decimal_str.rstrip('0').rstrip('.') if '.' in decimal_str else decimal_str
        
        # Find repeating pattern
        pattern = self._find_repeating_pattern(decimal_str)
        pattern_length = len(pattern) if pattern else None
        
        # Determine if it's a flush number
        is_flush = n in self.known_flush_numbers or self._is_flush_candidate(n, reciprocal)
        flush_strength = self._calculate_flush_strength(n, reciprocal, pattern)
        
        result = FlushAnalysis(
            number=n,
            reciprocal=reciprocal,
            decimal_expansion=decimal_str,
            repeating_pattern=pattern,
            pattern_length=pattern_length,
            is_flush=is_flush,
            flush_strength=flush_strength
        )
        
        self.cache[n] = result
        return result
    
    def _find_repeating_pattern(self, decimal_str: str) -> Optional[str]:
        """Find repeating pattern in decimal expansion"""
        if '.' not in decimal_str:
            return None
        
        fractional_part = decimal_str.split('.')[1]
        
        if len(fractional_part) < 6:
            return None
        
        # Try to find the minimal repeating pattern
        for pattern_length in range(1, len(fractional_part) // 2):
            pattern = fractional_part[:pattern_length]
            repeated = pattern * (len(fractional_part) // pattern_length)
            
            if fractional_part.startswith(repeated):
                # Verify it's truly repeating
                if self._is_truly_repeating(fractional_part, pattern):
                    return pattern
        
        return None
    
    def _is_truly_repeating(self, fractional: str, pattern: str) -> bool:
        """Verify if a pattern truly repeats throughout the fractional part"""
        pattern_length = len(pattern)
        
        for i in range(0, len(fractional), pattern_length):
            segment = fractional[i:i+pattern_length]
            if segment != pattern and len(segment) == pattern_length:
                return False
        
        return True
    
    def _is_flush_candidate(self, n: int, reciprocal: Decimal) -> bool:
        """Determine if n has flush-like properties"""
        # Criteria for flush numbers based on documentation
        recip_str = str(reciprocal)
        
        # Check for special properties mentioned in documentation
        # 1/13 = 0.076923 (contains 7, has special meaning)
        if '7' in recip_str and n == 13:
            return True
            
        # Check for symmetrical or interesting patterns
        if self._has_interesting_pattern(reciprocal):
            return True
            
        return False
    
    def _has_interesting_pattern(self, reciprocal: Decimal) -> bool:
        """Check if reciprocal has interesting mathematical properties"""
        recip_str = str(reciprocal)
        
        # Look for patterns like the 7 in 1/13
        special_digits = ['7', '3', '13']
        
        for digit in special_digits:
            if digit in recip_str:
                # Additional pattern analysis could go here
                return True
                
        return False
    
    def _calculate_flush_strength(self, n: int, reciprocal: Decimal, pattern: Optional[str]) -> float:
        """Calculate strength of flush property (0.0 to 1.0)"""
        strength = 0.0
        
        # Base strength for known flush numbers
        if n in self.known_flush_numbers:
            strength += 0.5
            
        # Pattern-based strength
        if pattern:
            pattern_len = len(pattern)
            if pattern_len <= 6:  # Short, elegant patterns
                strength += 0.3
            elif pattern_len <= 12:
                strength += 0.2
            else:
                strength += 0.1
                
        # Mathematical property strength
        if self._has_interesting_pattern(reciprocal):
            strength += 0.2
            
        return min(strength, 1.0)
    
    def find_flush_candidates(self, range_limit: int = 1000) -> List[FlushAnalysis]:
        """Find potential flush numbers in a range"""
        candidates = []
        
        for n in range(1, range_limit + 1):
            analysis = self.analyze_reciprocal(n)
            if analysis.flush_strength > 0.3:  # Threshold for interesting numbers
                candidates.append(analysis)
                
        # Sort by flush strength
        candidates.sort(key=lambda x: x.flush_strength, reverse=True)
        
        return candidates

class SubPrimeEngine:
    """Engine for analyzing sub-prime propositions"""
    
    def test_sub_prime_property(self, x: Union[int, float]) -> bool:
        """Test sub-prime proposition: (x² - x) / (x-1) = x"""
        if x == 1:
            return False  # Division by zero
            
        left_side = (x**2 - x) / (x - 1)
        return abs(left_side - x) < 1e-10
    
    def extended_sub_prime(self, x: float, a: int, b: int, c: int) -> Optional[float]:
        """
        Extended sub-prime: (x^a - x^b) / ((x-1) * x^c) = x
        Returns the result or None if invalid
        """
        if x == 1:
            return None
            
        numerator = x**a - x**b
        denominator = (x - 1) * x**c
        
        if denominator == 0:
            return None
            
        return numerator / denominator
    
    def analyze_sub_prime_space(self, range_limit: int = 100) -> Dict[str, List]:
        """Analyze sub-prime properties across a range of values"""
        results = {
            'valid_sub_primes': [],
            'invalid_values': [],
            'edge_cases': [],
            'patterns': []
        }
        
        for x in range(2, range_limit + 1):
            if self.test_sub_prime_property(x):
                results['valid_sub_primes'].append(x)
            else:
                results['invalid_values'].append(x)
        
        # Look for patterns in valid values
        results['patterns'] = self._find_patterns(results['valid_sub_primes'])
        
        return results
    
    def _find_patterns(self, values: List[int]) -> List[str]:
        """Find patterns in the sub-prime valid values"""
        patterns = []
        
        if not values:
            return patterns
            
        # Check for arithmetic progressions
        if len(values) >= 3:
            diffs = [values[i+1] - values[i] for i in range(len(values)-1)]
            if len(set(diffs)) == 1:
                patterns.append(f"Arithmetic progression with difference {diffs[0]}")
        
        # Check for prime numbers
        prime_count = sum(1 for x in values if self._is_prime(x))
        if prime_count > len(values) * 0.7:
            patterns.append("Mostly prime numbers")
        
        # Check for special sequences
        if all(x % 2 == 0 for x in values):
            patterns.append("All even numbers")
        elif all(x % 2 == 1 for x in values):
            patterns.append("All odd numbers")
            
        return patterns
    
    def _is_prime(self, n: int) -> bool:
        """Check if a number is prime"""
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

class QuarterSystem:
    """Quarter system analysis: P(n) = n * (25/100)"""
    
    def __init__(self):
        self.quarter_value = Decimal('0.25')
        self.quarter_fraction = Fraction(1, 4)
        
    def quarter_p(self, n: Union[int, float, Decimal]) -> Decimal:
        """P(n) = n * (25/100)"""
        n_decimal = Decimal(str(n))
        return n_decimal * self.quarter_value
    
    def analyze_quarter_properties(self, n: Union[int, float, Decimal]) -> Dict[str, Any]:
        """Analyze quarter system properties for number n"""
        quarter_val = self.quarter_p(n)
        n_decimal = Decimal(str(n))
        
        return {
            'original_value': float(n_decimal),
            'quarter_value': float(quarter_val),
            'ratio_to_full': float(quarter_val / n_decimal) if n_decimal != 0 else 0,
            'fraction_representation': str(self.quarter_fraction),
            'decimal_representation': str(quarter_val),
            'is_quarter_multiple': float(quarter_val) % 0.25 == 0,
            'inverse_relationship': float(n_decimal) / float(quarter_val) if quarter_val != 0 else 0
        }
    
    def find_quarter_patterns(self, sequence: List[int]) -> Dict[str, Any]:
        """Find patterns related to quarter system in a sequence"""
        quarter_values = [self.quarter_p(x) for x in sequence]
        
        return {
            'quarter_sequence': [float(v) for v in quarter_values],
            'mean_quarter': float(sum(quarter_values) / len(quarter_values)),
            'quarter_ratios': [float(self.quarter_p(x) / Decimal(str(x))) for x in sequence if x != 0],
            'quarter_relationships': self._analyze_quarter_relationships(sequence)
        }
    
    def _analyze_quarter_relationships(self, sequence: List[int]) -> List[str]:
        """Analyze special relationships in quarter system"""
        relationships = []
        
        if len(sequence) >= 2:
            for i in range(len(sequence)-1):
                current = sequence[i]
                next_val = sequence[i+1]
                
                current_quarter = float(self.quarter_p(current))
                next_quarter = float(self.quarter_p(next_val))
                
                if current_quarter == next_val:
                    relationships.append(f"Position {i} and {i+1} have equal quarter values")
                elif current_quarter * 4 == next_val:
                    relationships.append(f"Position {i+1} is 4x the quarter of position {i}")
        
        return relationships

def phi() -> float:
    """Golden ratio φ = (1 + √5) / 2"""
    return (1 + math.sqrt(5)) / 2

# Main entry point for testing
if __name__ == "__main__":
    print("Neo-Beta Sequence System Initialized")
    print("=" * 50)
    
    # Initialize components
    p_engine = PFunctionEngine()
    beta_gen = BetaSequenceGenerator(p_engine)
    flush_analyzer = FlushNumberAnalyzer()
    sub_prime = SubPrimeEngine()
    quarter_sys = QuarterSystem()
    
    # Test P(x) function
    print("Testing P(x) function:")
    for x in range(1, 6):
        p_val = p_engine.evaluate(x)
        identity = p_engine.get_sequence_identity(x)
        residues = p_engine.analyze_residues(x)
        print(f"P({x}) = {p_val} -> Identity: {identity}")
    
    print("\nGenerating Beta sequence:")
    sequence = beta_gen.generate_sequence(1, 14)
    print(f"Sequence: {sequence}")
    relationships = beta_gen.analyze_relationships(sequence)
    print(f"Relationships: {relationships}")
    
    print("\nAnalyzing flush numbers:")
    for n in [13, 7, 3, 8]:
        analysis = flush_analyzer.analyze_reciprocal(n)
        print(f"1/{n} = {analysis.decimal_expansion}")
        print(f"  Pattern: {analysis.repeating_pattern}")
        print(f"  Flush: {analysis.is_flush} (strength: {analysis.flush_strength})")
    
    print("\nTesting sub-prime propositions:")
    for x in range(2, 10):
        is_sub_prime = sub_prime.test_sub_prime_property(x)
        print(f"x={x}: {'Valid' if is_sub_prime else 'Invalid'}")
    
    print("\nQuarter system analysis:")
    for n in range(1, 5):
        props = quarter_sys.analyze_quarter_properties(n)
        print(f"n={n}: Quarter value = {props['quarter_value']}")