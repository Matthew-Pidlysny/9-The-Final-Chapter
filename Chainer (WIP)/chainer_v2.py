"""
Chainer Mathematical Engine
Core mathematical computation engine for decimal analysis, number classification,
and interpretive theory implementation based on the 12 Universal System Rules.

This module implements the theoretical framework for understanding how decimals
appear in different strings through positional notation and prime factor alignment.
"""

import math
from decimal import Decimal, getcontext
from typing import Dict, List, Tuple, Optional, Set
from fractions import Fraction
import functools

# Set high precision for decimal calculations
getcontext().prec = 100

class NumberClassifier:
    """
    Implements the 12 Universal System Rules for number classification
    based on prime factor alignment with bases.
    """
    
    def __init__(self):
        # Precomputed primes for efficiency
        self.prime_cache = {}
        self.factor_cache = {}
    
    @functools.lru_cache(maxsize=1000)
    def prime_factors(self, n: int) -> Set[int]:
        """Compute prime factors of n with caching."""
        if n in self.factor_cache:
            return self.factor_cache[n]
        
        factors = set()
        # Handle negative numbers
        if n < 0:
            n = -n
        
        # Handle 0 and 1
        if n == 0:
            self.factor_cache[0] = set()
            return set()
        if n == 1:
            self.factor_cache[1] = set()
            return set()
        
        # Factor out 2s
        while n % 2 == 0:
            factors.add(2)
            n //= 2
        
        # Factor out odd numbers up to sqrt(n)
        i = 3
        max_factor = math.sqrt(n) + 1
        while i <= max_factor:
            while n % i == 0:
                factors.add(i)
                n //= i
                max_factor = math.sqrt(n) + 1
            i += 2
        
        # If remaining n > 1, it's prime
        if n > 1:
            factors.add(n)
        
        self.factor_cache[n] = factors
        return factors
    
    def is_simple(self, n: int, base: int = 10) -> bool:
        """
        Universal Rule 2: A number is Simple if all prime factors divide the base.
        Note: 1 is always Simple (Rule 5), 0 is handled separately.
        """
        if n == 1:
            return True  # Rule 5
        if n == 0:
            return False  # 0 has undefined reciprocal, not Simple by our definition
        
        n_factors = self.prime_factors(abs(n))
        base_factors = self.prime_factors(base)
        
        # Rule 2: All prime factors of n must divide the base
        return n_factors.issubset(base_factors)
    
    def classify_number(self, n: int, base: int = 10) -> Dict[str, any]:
        """Complete classification of a number according to the Universal System."""
        classification = {
            'number': n,
            'base': base,
            'prime_factors': list(self.prime_factors(abs(n))),
            'is_simple': self.is_simple(n, base),
            'is_wild': not self.is_simple(n, base),
            'is_factor': n > 1 and n in self.prime_factors(base),
            'repeating_period': None
        }
        
        # Special handling for 0
        if n == 0:
            classification.update({
                'is_simple': False,
                'is_wild': True,
                'is_factor': False,
                'note': '0 is the structural origin, not computable via reciprocal'
            })
        
        return classification

# Initialize global instance
classifier = NumberClassifier()

# Test the engine with key numbers
if __name__ == '__main__':
    test_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    
    print("=== Chainer Mathematical Engine Test ===")
    print()
    
    for n in test_numbers:
        result = classifier.classify_number(n)
        print(f"Number {n}:")
        print(f"  Classification: {result['is_simple'] and 'Simple' or 'Wild'}")
        print(f"  Prime factors: {result['prime_factors']}")
        if result['is_factor']:
            print(f"  Factor Prime: Yes")
        print()
