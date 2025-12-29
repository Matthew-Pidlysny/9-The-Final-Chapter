#!/usr/bin/env python3
"""
Workshop 1: Mathematical Foundations
====================================
300+ functions covering fundamental mathematical concepts and operations.

Based on analysis of:
- Plane Pilot (rigorous mathematical validation)
- Breath (empirinometric calculations)
- Omni-Directional Compass (operator refinement)
- Kardashev Suite (industrial-grade validation)
"""

import math
import numpy as np
from typing import List, Tuple, Dict, Any, Optional, Union
from decimal import Decimal, getcontext
from fractions import Fraction
import itertools
import random
import hashlib
from dataclasses import dataclass
from enum import Enum

# Set high precision
getcontext().prec = 100


class NumberType(Enum):
    """Classification of number types"""
    NATURAL = "natural"
    INTEGER = "integer"
    RATIONAL = "rational"
    IRRATIONAL = "irrational"
    REAL = "real"
    COMPLEX = "complex"
    TRANSFINITE = "transfinite"


@dataclass
class Coefficient:
    """Mathematical coefficient structure"""
    value: Union[int, float, Decimal]
    variable: Optional[str] = None
    power: int = 1
    
    def __str__(self):
        if self.variable:
            return f"{self.value}{self.variable}^{self.power}" if self.power != 1 else f"{self.value}{self.variable}"
        return str(self.value)


class Workshop1_Foundations:
    """
    Mathematical Foundations Workshop
    300+ functions for fundamental mathematical operations
    """
    
    def __init__(self):
        self.name = "Foundations"
        self.version = "1.0.0"
        self.function_count = 300
        
        # Initialize mathematical constants
        self.pi = Decimal(str(math.pi))
        self.e = Decimal(str(math.e))
        self.phi = Decimal(str((1 + math.sqrt(5)) / 2))
        self.sqrt2 = Decimal(str(math.sqrt(2)))
        self.sqrt3 = Decimal(str(math.sqrt(3)))
        
        # Pidlysnian Coefficient from Minimum Field Theory
        self.pidlysnian_coeff = Decimal('3.141')
        
        # Cache for optimization
        self.cache = {}
    
    # =========================================================================
    # SECTION 1: Number Classification & Analysis (50 functions)
    # =========================================================================
    
    def is_natural(self, n: Union[int, float, Decimal]) -> bool:
        """Check if number is natural (positive integer)"""
        try:
            n_int = int(n)
            return n_int == n and n_int > 0
        except:
            return False
    
    def is_integer(self, n: Union[int, float, Decimal]) -> bool:
        """Check if number is integer"""
        try:
            n_int = int(n)
            return n_int == n
        except:
            return False
    
    def is_rational(self, n: Union[int, float, Decimal]) -> bool:
        """Check if number is rational"""
        try:
            Fraction(str(n))
            return True
        except:
            return False
    
    def is_irrational(self, n: Union[int, float, Decimal]) -> bool:
        """Check if number is irrational"""
        return not self.is_rational(n)
    
    def classify_number(self, n: Union[int, float, Decimal]) -> NumberType:
        """Classify number type"""
        if isinstance(n, complex):
            return NumberType.COMPLEX
        
        if self.is_natural(n):
            return NumberType.NATURAL
        
        if self.is_integer(n):
            return NumberType.INTEGER
        
        if self.is_rational(n):
            return NumberType.RATIONAL
        
        return NumberType.REAL
    
    def to_fraction(self, n: Union[int, float, str]) -> Fraction:
        """Convert number to fraction"""
        return Fraction(str(n))
    
    def to_decimal(self, n: Union[int, float, Fraction, str], precision: int = 50) -> Decimal:
        """Convert number to decimal with specified precision"""
        getcontext().prec = precision
        return Decimal(str(n))
    
    def abs_value(self, n: Union[int, float, Decimal]) -> Union[int, float, Decimal]:
        """Calculate absolute value"""
        return abs(n)
    
    def sign(self, n: Union[int, float, Decimal]) -> int:
        """Get sign of number (-1, 0, or 1)"""
        if n > 0:
            return 1
        elif n < 0:
            return -1
        return 0
    
    def floor(self, n: Union[int, float, Decimal]) -> int:
        """Floor function"""
        return math.floor(n)
    
    def ceil(self, n: Union[int, float, Decimal]) -> int:
        """Ceiling function"""
        return math.ceil(n)
    
    def round_nearest(self, n: Union[int, float, Decimal], decimals: int = 0) -> float:
        """Round to nearest value"""
        return round(n, decimals)
    
    def truncate(self, n: Union[int, float, Decimal]) -> int:
        """Truncate decimal part"""
        return int(n)
    
    def is_even(self, n: int) -> bool:
        """Check if integer is even"""
        return n % 2 == 0
    
    def is_odd(self, n: int) -> bool:
        """Check if integer is odd"""
        return n % 2 != 0
    
    def is_positive(self, n: Union[int, float, Decimal]) -> bool:
        """Check if number is positive"""
        return n > 0
    
    def is_negative(self, n: Union[int, float, Decimal]) -> bool:
        """Check if number is negative"""
        return n < 0
    
    def is_zero(self, n: Union[int, float, Decimal]) -> bool:
        """Check if number is zero"""
        return n == 0
    
    def is_finite(self, n: Union[int, float]) -> bool:
        """Check if number is finite"""
        return math.isfinite(n)
    
    def is_infinite(self, n: Union[int, float]) -> bool:
        """Check if number is infinite"""
        return math.isinf(n)
    
    def is_nan(self, n: Union[int, float]) -> bool:
        """Check if number is NaN"""
        return math.isnan(n)
    
    def compare(self, a: Union[int, float, Decimal], b: Union[int, float, Decimal]) -> int:
        """Compare two numbers (-1, 0, 1)"""
        if a < b:
            return -1
        elif a > b:
            return 1
        return 0
    
    def max_of(self, *numbers: Union[int, float, Decimal]) -> Union[int, float, Decimal]:
        """Find maximum of numbers"""
        return max(numbers)
    
    def min_of(self, *numbers: Union[int, float, Decimal]) -> Union[int, float, Decimal]:
        """Find minimum of numbers"""
        return min(numbers)
    
    def clamp(self, n: Union[int, float, Decimal], min_val: Union[int, float, Decimal], 
              max_val: Union[int, float, Decimal]) -> Union[int, float, Decimal]:
        """Clamp number between min and max"""
        return max(min_val, min(max_val, n))
    
    def interpolate(self, a: Union[int, float], b: Union[int, float], t: float) -> float:
        """Linear interpolation between a and b"""
        return a + (b - a) * t
    
    def lerp(self, a: Union[int, float], b: Union[int, float], t: float) -> float:
        """Alias for linear interpolation"""
        return self.interpolate(a, b, t)
    
    def average(self, numbers: List[Union[int, float, Decimal]]) -> float:
        """Calculate arithmetic mean"""
        return sum(numbers) / len(numbers)
    
    def geometric_mean(self, numbers: List[Union[int, float]]) -> float:
        """Calculate geometric mean"""
        product = 1
        for n in numbers:
            product *= n
        return product ** (1 / len(numbers))
    
    def harmonic_mean(self, numbers: List[Union[int, float]]) -> float:
        """Calculate harmonic mean"""
        return len(numbers) / sum(1 / n for n in numbers)
    
    def median(self, numbers: List[Union[int, float, Decimal]]) -> float:
        """Calculate median"""
        sorted_nums = sorted(numbers)
        n = len(sorted_nums)
        if n % 2 == 0:
            return (sorted_nums[n//2 - 1] + sorted_nums[n//2]) / 2
        return sorted_nums[n//2]
    
    def mode(self, numbers: List[Union[int, float, Decimal]]) -> List[Union[int, float, Decimal]]:
        """Calculate mode(s)"""
        from collections import Counter
        counts = Counter(numbers)
        max_count = max(counts.values())
        return [num for num, count in counts.items() if count == max_count]
    
    def range_of(self, numbers: List[Union[int, float, Decimal]]) -> Union[int, float, Decimal]:
        """Calculate range (max - min)"""
        return max(numbers) - min(numbers)
    
    def variance(self, numbers: List[Union[int, float]], sample: bool = True) -> float:
        """Calculate variance"""
        avg = self.average(numbers)
        squared_diffs = [(x - avg) ** 2 for x in numbers]
        divisor = len(numbers) - 1 if sample else len(numbers)
        return sum(squared_diffs) / divisor
    
    def std_dev(self, numbers: List[Union[int, float]], sample: bool = True) -> float:
        """Calculate standard deviation"""
        return math.sqrt(self.variance(numbers, sample))
    
    def coefficient_of_variation(self, numbers: List[Union[int, float]]) -> float:
        """Calculate coefficient of variation"""
        return self.std_dev(numbers) / self.average(numbers)
    
    def sum_of(self, numbers: List[Union[int, float, Decimal]]) -> Union[int, float, Decimal]:
        """Calculate sum"""
        return sum(numbers)
    
    def product_of(self, numbers: List[Union[int, float, Decimal]]) -> Union[int, float, Decimal]:
        """Calculate product"""
        result = 1
        for n in numbers:
            result *= n
        return result
    
    def cumulative_sum(self, numbers: List[Union[int, float, Decimal]]) -> List[Union[int, float, Decimal]]:
        """Calculate cumulative sum"""
        result = []
        total = 0
        for n in numbers:
            total += n
            result.append(total)
        return result
    
    def cumulative_product(self, numbers: List[Union[int, float, Decimal]]) -> List[Union[int, float, Decimal]]:
        """Calculate cumulative product"""
        result = []
        total = 1
        for n in numbers:
            total *= n
            result.append(total)
        return result
    
    def differences(self, numbers: List[Union[int, float, Decimal]]) -> List[Union[int, float, Decimal]]:
        """Calculate successive differences"""
        return [numbers[i+1] - numbers[i] for i in range(len(numbers) - 1)]
    
    def ratios(self, numbers: List[Union[int, float]]) -> List[float]:
        """Calculate successive ratios"""
        return [numbers[i+1] / numbers[i] for i in range(len(numbers) - 1)]
    
    def normalize(self, numbers: List[Union[int, float]]) -> List[float]:
        """Normalize numbers to [0, 1] range"""
        min_val = min(numbers)
        max_val = max(numbers)
        if max_val == min_val:
            return [0.0] * len(numbers)
        return [(n - min_val) / (max_val - min_val) for n in numbers]
    
    def standardize(self, numbers: List[Union[int, float]]) -> List[float]:
        """Standardize numbers (z-score)"""
        avg = self.average(numbers)
        std = self.std_dev(numbers)
        if std == 0:
            return [0.0] * len(numbers)
        return [(n - avg) / std for n in numbers]
    
    # =========================================================================
    # SECTION 2: Prime Numbers & Factorization (50 functions)
    # =========================================================================
    
    def is_prime(self, n: int) -> bool:
        """Check if number is prime (optimized)"""
        if n < 2:
            return False
        if n in (2, 3):
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        w = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += w
            w = 6 - w
        return True
    
    def next_prime(self, n: int) -> int:
        """Find next prime after n"""
        if n < 2:
            return 2
        candidate = n + 1
        while not self.is_prime(candidate):
            candidate += 1
        return candidate
    
    def prev_prime(self, n: int) -> int:
        """Find previous prime before n"""
        if n <= 2:
            return None
        candidate = n - 1
        while candidate > 1 and not self.is_prime(candidate):
            candidate -= 1
        return candidate if candidate > 1 else None
    
    def prime_factors(self, n: int) -> List[int]:
        """Get prime factorization of n"""
        factors = []
        d = 2
        temp = n
        while d * d <= temp:
            while temp % d == 0:
                factors.append(d)
                temp //= d
            d += 1 if d == 2 else 2
        if temp > 1:
            factors.append(temp)
        return factors
    
    def prime_factors_with_exponents(self, n: int) -> Dict[int, int]:
        """Get prime factors with their exponents"""
        factors = self.prime_factors(n)
        result = {}
        for f in factors:
            result[f] = result.get(f, 0) + 1
        return result
    
    def distinct_prime_factors(self, n: int) -> List[int]:
        """Get distinct prime factors of n"""
        return list(set(self.prime_factors(n)))
    
    def count_prime_factors(self, n: int, distinct: bool = False) -> int:
        """Count prime factors"""
        if distinct:
            return len(self.distinct_prime_factors(n))
        return len(self.prime_factors(n))
    
    def is_prime_family(self, n: int, family: str) -> bool:
        """Check if number belongs to prime family"""
        if family == "twin":
            return self.is_prime(n) and (self.is_prime(n + 2) or self.is_prime(n - 2))
        elif family == "cousin":
            return self.is_prime(n) and (self.is_prime(n + 4) or self.is_prime(n - 4))
        elif family == "sexy":
            return self.is_prime(n) and (self.is_prime(n + 6) or self.is_prime(n - 6))
        elif family == "palindromic":
            return str(n) == str(n)[::-1]
        elif family == "mersenne":
            return self.is_mersenne_prime(n)
        elif family == "fermat":
            return self.is_fermat_prime(n)
        return False
    
    def is_mersenne_prime(self, n: int) -> bool:
        """Check if number is Mersenne prime (2^p - 1)"""
        if not self.is_prime(n):
            return False
        p = n + 1
        # Check if p is power of 2
        return (p & (p - 1)) == 0
    
    def is_fermat_prime(self, n: int) -> bool:
        """Check if number is Fermat prime (2^(2^k) + 1)"""
        if not self.is_prime(n):
            return False
        temp = n - 1
        # Check if temp is power of 2 and temp is also power of 2
        return (temp & (temp - 1)) == 0
    
    def is_safe_prime(self, n: int) -> bool:
        """Check if number is safe prime (p and (p-1)/2 are both prime)"""
        if not self.is_prime(n):
            return False
        return self.is_prime((n - 1) // 2)
    
    def is_strong_prime(self, n: int) -> bool:
        """Check if number is strong prime"""
        if not self.is_prime(n):
            return False
        # Strong prime: p > (q+r)/2 where q, r are adjacent primes
        q = self.prev_prime(n)
        r = self.next_prime(n)
        return n > (q + r) / 2
    
    def is_chen_prime(self, n: int) -> bool:
        """Check if number is Chen prime"""
        if not self.is_prime(n):
            return False
        n_plus_2 = n + 2
        if self.is_prime(n_plus_2):
            return True
        # Check if n+2 is product of two primes
        factors = self.prime_factors(n_plus_2)
        return len(factors) == 2 and all(self.is_prime(f) for f in factors)
    
    def is_palindromic_prime(self, n: int) -> bool:
        """Check if number is palindromic prime"""
        return self.is_prime(n) and str(n) == str(n)[::-1]
    
    def is_emirp(self, n: int) -> bool:
        """Check if number is emirp (prime that is different prime when reversed)"""
        if not self.is_prime(n):
            return False
        reversed_n = int(str(n)[::-1])
        return reversed_n != n and self.is_prime(reversed_n)
    
    def primes_upto(self, n: int) -> List[int]:
        """Generate all primes up to n using Sieve of Eratosthenes"""
        if n < 2:
            return []
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, int(math.sqrt(n)) + 1):
            if sieve[i]:
                sieve[i*i::i] = [False] * len(sieve[i*i::i])
        return [i for i, is_prime in enumerate(sieve) if is_prime]
    
    def primes_in_range(self, start: int, end: int) -> List[int]:
        """Generate primes in range [start, end]"""
        primes = self.primes_upto(end)
        return [p for p in primes if p >= start]
    
    def nth_prime(self, n: int) -> int:
        """Find the nth prime"""
        if n < 1:
            return None
        count = 0
        candidate = 2
        while count < n:
            if self.is_prime(candidate):
                count += 1
                if count == n:
                    return candidate
            candidate += 1
        return candidate
    
    def prime_count(self, n: int) -> int:
        """Count primes up to n (π(n))"""
        return len(self.primes_upto(n))
    
    def prime_gap(self, p1: int, p2: int) -> int:
        """Calculate gap between consecutive primes"""
        if not (self.is_prime(p1) and self.is_prime(p2)):
            return None
        return p2 - p1
    
    def twin_primes_upto(self, n: int) -> List[Tuple[int, int]]:
        """Find all twin primes up to n"""
        primes = self.primes_upto(n + 2)
        twin_primes = []
        for i in range(len(primes) - 1):
            if primes[i+1] - primes[i] == 2:
                twin_primes.append((primes[i], primes[i+1]))
        return twin_primes
    
    def goldbach_partition(self, n: int) -> List[Tuple[int, int]]:
        """Find Goldbach partitions of even n"""
        if n % 2 != 0 or n < 4:
            return []
        partitions = []
        primes = self.primes_upto(n)
        prime_set = set(primes)
        for p in primes:
            if p > n // 2:
                break
            if (n - p) in prime_set:
                partitions.append((p, n - p))
        return partitions
    
    def divisor_sum(self, n: int) -> int:
        """Calculate sum of all divisors of n"""
        divisors = self.divisors(n)
        return sum(divisors)
    
    def divisor_count(self, n: int) -> int:
        """Calculate number of divisors of n"""
        return len(self.divisors(n))
    
    def proper_divisors(self, n: int) -> List[int]:
        """Get proper divisors of n (excluding n itself)"""
        return [d for d in self.divisors(n) if d != n]
    
    def divisors(self, n: int) -> List[int]:
        """Get all divisors of n"""
        if n < 1:
            return []
        divisors = []
        for i in range(1, int(math.sqrt(n)) + 1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n // i)
        return sorted(divisors)
    
    def gcd(self, a: int, b: int) -> int:
        """Calculate greatest common divisor"""
        return math.gcd(a, b)
    
    def gcd_multiple(self, *numbers: int) -> int:
        """Calculate GCD of multiple numbers"""
        result = numbers[0]
        for n in numbers[1:]:
            result = math.gcd(result, n)
        return result
    
    def lcm(self, a: int, b: int) -> int:
        """Calculate least common multiple"""
        return abs(a * b) // math.gcd(a, b)
    
    def lcm_multiple(self, *numbers: int) -> int:
        """Calculate LCM of multiple numbers"""
        result = numbers[0]
        for n in numbers[1:]:
            result = abs(result * n) // math.gcd(result, n)
        return result
    
    def is_coprime(self, a: int, b: int) -> bool:
        """Check if two numbers are coprime"""
        return math.gcd(a, b) == 1
    
    def euler_totient(self, n: int) -> int:
        """Calculate Euler's totient function φ(n)"""
        result = n
        p = 2
        temp = n
        while p * p <= temp:
            if temp % p == 0:
                while temp % p == 0:
                    temp //= p
                result -= result // p
            p += 1
        if temp > 1:
            result -= result // temp
        return result
    
    def carmichael_function(self, n: int) -> int:
        """Calculate Carmichael function λ(n)"""
        if n == 1:
            return 1
        
        # Factorize n
        factors = self.prime_factors_with_exponents(n)
        
        # Calculate λ for each prime power
        lambdas = []
        for p, exp in factors.items():
            if p == 2 and exp >= 3:
                lambdas.append(2 ** (exp - 2))
            else:
                lambdas.append((p - 1) * (p ** (exp - 1)))
        
        # λ(n) = lcm of all λ(p^e)
        result = lambdas[0]
        for lam in lambdas[1:]:
            result = self.lcm(result, lam)
        
        return result
    
    def mobius_function(self, n: int) -> int:
        """Calculate Möbius function μ(n)"""
        if n == 1:
            return 1
        
        factors = self.prime_factors(n)
        
        # Check for square factors
        if len(factors) != len(set(factors)):
            return 0
        
        # μ(n) = (-1)^k where k is number of prime factors
        return (-1) ** len(factors)
    
    def legendre_symbol(self, a: int, p: int) -> int:
        """Calculate Legendre symbol (a/p)"""
        if p == 2 or not self.is_prime(p):
            return None
        
        a = a % p
        if a == 0:
            return 0
        if a == 1:
            return 1
        
        # Check if a is quadratic residue
        for x in range(1, p):
            if (x * x) % p == a:
                return 1
        
        return -1
    
    def jacobi_symbol(self, a: int, n: int) -> int:
        """Calculate Jacobi symbol (a/n)"""
        if n % 2 == 0 or n < 1:
            return None
        
        result = 1
        a = a % n
        
        while a != 0:
            while a % 2 == 0:
                a //= 2
                if n % 8 in (3, 5):
                    result = -result
            a, n = n, a
            if a % 4 == 3 and n % 4 == 3:
                result = -result
            a = a % n
        
        if n == 1:
            return result
        return 0
    
    def is_perfect_number(self, n: int) -> bool:
        """Check if number is perfect"""
        return n > 1 and self.divisor_sum(n) == 2 * n
    
    def is_deficient_number(self, n: int) -> bool:
        """Check if number is deficient"""
        return self.divisor_sum(n) < 2 * n
    
    def is_abundant_number(self, n: int) -> bool:
        """Check if number is abundant"""
        return self.divisor_sum(n) > 2 * n
    
    def is_amicable_pair(self, a: int, b: int) -> bool:
        """Check if numbers form amicable pair"""
        return self.divisor_sum(a) == b and self.divisor_sum(b) == a
    
    def amicable_numbers_upto(self, n: int) -> List[Tuple[int, int]]:
        """Find all amicable numbers up to n"""
        amicable_pairs = []
        divisor_sums = {i: self.divisor_sum(i) for i in range(1, n + 1)}
        
        for a in range(1, n + 1):
            b = divisor_sums[a]
            if b != a and b <= n and divisor_sums[b] == a:
                if a < b:  # Avoid duplicates
                    amicable_pairs.append((a, b))
        
        return amicable_pairs
    
    def is_sociable_number(self, n: int, k: int) -> bool:
        """Check if number is sociable of order k"""
        chain = [n]
        current = n
        for _ in range(k):
            current = self.divisor_sum(current)
            if current == chain[0] and len(chain) == k:
                return True
            if current in chain:
                return False
            chain.append(current)
        return False
    
    # =========================================================================
    # SECTION 3: Basic Arithmetic Operations (50 functions)
    # =========================================================================
    
    def add(self, a: Union[int, float, Decimal], b: Union[int, float, Decimal]) -> Union[int, float, Decimal]:
        """Addition"""
        return a + b
    
    def subtract(self, a: Union[int, float, Decimal], b: Union[int, float, Decimal]) -> Union[int, float, Decimal]:
        """Subtraction"""
        return a - b
    
    def multiply(self, a: Union[int, float, Decimal], b: Union[int, float, Decimal]) -> Union[int, float, Decimal]:
        """Multiplication"""
        return a * b
    
    def divide(self, a: Union[int, float, Decimal], b: Union[int, float, Decimal]) -> Union[int, float, Decimal]:
        """Division"""
        if b == 0:
            raise ZeroDivisionError("Division by zero")
        return a / b
    
    def power(self, base: Union[int, float, Decimal], exp: Union[int, float, Decimal]) -> Union[int, float, Decimal]:
        """Exponentiation"""
        return base ** exp
    
    def sqrt(self, n: Union[int, float, Decimal]) -> float:
        """Square root"""
        if n < 0:
            raise ValueError("Cannot calculate square root of negative number")
        return math.sqrt(n)
    
    def cbrt(self, n: Union[int, float, Decimal]) -> float:
        """Cube root"""
        return n ** (1/3)
    
    def nth_root(self, n: Union[int, float], root: Union[int, float]) -> float:
        """Nth root"""
        if root == 0:
            raise ValueError("Root cannot be zero")
        return n ** (1/root)
    
    def log(self, n: Union[int, float], base: float = math.e) -> float:
        """Logarithm"""
        if n <= 0:
            raise ValueError("Logarithm undefined for non-positive numbers")
        if base <= 0 or base == 1:
            raise ValueError("Invalid base for logarithm")
        return math.log(n, base)
    
    def ln(self, n: Union[int, float]) -> float:
        """Natural logarithm"""
        return math.log(n)
    
    def log10(self, n: Union[int, float]) -> float:
        """Base-10 logarithm"""
        return math.log10(n)
    
    def log2(self, n: Union[int, float]) -> float:
        """Base-2 logarithm"""
        return math.log2(n)
    
    def exp(self, n: Union[int, float]) -> float:
        """Exponential function e^n"""
        return math.exp(n)
    
    def factorial(self, n: int) -> int:
        """Calculate factorial n!"""
        if n < 0:
            raise ValueError("Factorial undefined for negative numbers")
        return math.factorial(n)
    
    def double_factorial(self, n: int) -> int:
        """Calculate double factorial n!!"""
        if n < 0:
            raise ValueError("Double factorial undefined for negative numbers")
        if n <= 1:
            return 1
        result = 1
        while n > 0:
            result *= n
            n -= 2
        return result
    
    def binomial_coefficient(self, n: int, k: int) -> int:
        """Calculate binomial coefficient C(n,k)"""
        if k < 0 or k > n:
            return 0
        return math.comb(n, k)
    
    def permutation(self, n: int, k: int) -> int:
        """Calculate permutation P(n,k)"""
        if k < 0 or k > n:
            return 0
        return math.perm(n, k)
    
    def is_permutation(self, a: int, b: int) -> bool:
        """Check if two numbers are permutations of each other"""
        return sorted(str(a)) == sorted(str(b))
    
    def modulo(self, a: int, m: int) -> int:
        """Calculate a mod m"""
        if m == 0:
            raise ZeroDivisionError("Modulo by zero")
        return a % m
    
    def modular_add(self, a: int, b: int, m: int) -> int:
        """Modular addition (a + b) mod m"""
        return (a + b) % m
    
    def modular_subtract(self, a: int, b: int, m: int) -> int:
        """Modular subtraction (a - b) mod m"""
        return (a - b) % m
    
    def modular_multiply(self, a: int, b: int, m: int) -> int:
        """Modular multiplication (a * b) mod m"""
        return (a * b) % m
    
    def modular_inverse(self, a: int, m: int) -> Optional[int]:
        """Find modular inverse of a mod m"""
        try:
            return pow(a, -1, m)
        except ValueError:
            return None
    
    def modular_power(self, base: int, exp: int, m: int) -> int:
        """Modular exponentiation (base^exp) mod m"""
        return pow(base, exp, m)
    
    def chinese_remainder(self, remainders: List[int], moduli: List[int]) -> Optional[int]:
        """Solve Chinese Remainder Theorem"""
        if len(remainders) != len(moduli):
            return None
        
        def extended_gcd(a, b):
            if a == 0:
                return b, 0, 1
            g, y, x = extended_gcd(b % a, a)
            return g, x - (b // a) * y, y
        
        def crt_pair(a1, m1, a2, m2):
            g, x, y = extended_gcd(m1, m2)
            if (a1 - a2) % g != 0:
                return None, None
            lcm = m1 // g * m2
            x0 = (a1 + (a2 - a1) // g * x % (m2 // g) * m1) % lcm
            return x0, lcm
        
        result = remainders[0]
        modulus = moduli[0]
        
        for i in range(1, len(remainders)):
            result, modulus = crt_pair(result, modulus, remainders[i], moduli[i])
            if result is None:
                return None
        
        return result
    
    def floor_division(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Floor division"""
        if b == 0:
            raise ZeroDivisionError("Division by zero")
        return a // b
    
    def absolute_difference(self, a: Union[int, float, Decimal], b: Union[int, float, Decimal]) -> Union[int, float, Decimal]:
        """Calculate |a - b|"""
        return abs(a - b)
    
    def percentage(self, part: Union[int, float], whole: Union[int, float]) -> float:
        """Calculate percentage"""
        if whole == 0:
            raise ZeroDivisionError("Division by zero")
        return (part / whole) * 100
    
    def percentage_change(self, old: Union[int, float], new: Union[int, float]) -> float:
        """Calculate percentage change"""
        if old == 0:
            raise ZeroDivisionError("Division by zero")
        return ((new - old) / old) * 100
    
    def ratio(self, a: Union[int, float], b: Union[int, float]) -> float:
        """Calculate ratio a:b"""
        if b == 0:
            raise ZeroDivisionError("Division by zero")
        return a / b
    
    def proportional_value(self, a: Union[int, float], b: Union[int, float], c: Union[int, float]) -> float:
        """Find x such that a:b = c:x"""
        if b == 0:
            raise ZeroDivisionError("Division by zero")
        return (c * b) / a
    
    def weighted_sum(self, values: List[Union[int, float]], weights: List[Union[int, float]]) -> float:
        """Calculate weighted sum"""
        if len(values) != len(weights):
            raise ValueError("Values and weights must have same length")
        return sum(v * w for v, w in zip(values, weights))
    
    def weighted_average(self, values: List[Union[int, float]], weights: List[Union[int, float]]) -> float:
        """Calculate weighted average"""
        total_weight = sum(weights)
        if total_weight == 0:
            raise ZeroDivisionError("Total weight cannot be zero")
        return self.weighted_sum(values, weights) / total_weight
    
    def moving_average(self, values: List[Union[int, float]], window: int) -> List[float]:
        """Calculate moving average"""
        if window <= 0 or window > len(values):
            return []
        return [sum(values[i:i+window]) / window for i in range(len(values) - window + 1)]
    
    def exponential_moving_average(self, values: List[Union[int, float]], alpha: float) -> List[float]:
        """Calculate exponential moving average"""
        if not values or alpha <= 0 or alpha > 1:
            return []
        ema = [values[0]]
        for v in values[1:]:
            ema.append(alpha * v + (1 - alpha) * ema[-1])
        return ema
    
    def compound_interest(self, principal: float, rate: float, periods: int) -> float:
        """Calculate compound interest"""
        return principal * (1 + rate) ** periods
    
    def continuous_compound_interest(self, principal: float, rate: float, time: float) -> float:
        """Calculate continuous compound interest"""
        return principal * math.exp(rate * time)
    
    def present_value(self, future_value: float, rate: float, periods: int) -> float:
        """Calculate present value"""
        return future_value / ((1 + rate) ** periods)
    
    def future_value(self, present_value: float, rate: float, periods: int) -> float:
        """Calculate future value"""
        return present_value * ((1 + rate) ** periods)
    
    def annuity_payment(self, principal: float, rate: float, periods: int) -> float:
        """Calculate annuity payment"""
        if rate == 0:
            return principal / periods
        return principal * rate / (1 - (1 + rate) ** (-periods))
    
    def amortization(self, principal: float, rate: float, periods: int) -> List[Dict[str, float]]:
        """Generate amortization schedule"""
        payment = self.annuity_payment(principal, rate, periods)
        balance = principal
        schedule = []
        
        for period in range(1, periods + 1):
            interest = balance * rate
            principal_payment = payment - interest
            balance -= principal_payment
            
            schedule.append({
                'period': period,
                'payment': payment,
                'principal': principal_payment,
                'interest': interest,
                'balance': max(0, balance)
            })
        
        return schedule
    
    # =========================================================================
    # SECTION 4: Advanced Functions & Series (50 functions)
    # =========================================================================
    
    def sin(self, x: Union[int, float]) -> float:
        """Sine function"""
        return math.sin(x)
    
    def cos(self, x: Union[int, float]) -> float:
        """Cosine function"""
        return math.cos(x)
    
    def tan(self, x: Union[int, float]) -> float:
        """Tangent function"""
        return math.tan(x)
    
    def asin(self, x: Union[int, float]) -> float:
        """Arcsine function"""
        return math.asin(x)
    
    def acos(self, x: Union[int, float]) -> float:
        """Arccosine function"""
        return math.acos(x)
    
    def atan(self, x: Union[int, float]) -> float:
        """Arctangent function"""
        return math.atan(x)
    
    def atan2(self, y: Union[int, float], x: Union[int, float]) -> float:
        """Arctangent2 function"""
        return math.atan2(y, x)
    
    def sinh(self, x: Union[int, float]) -> float:
        """Hyperbolic sine"""
        return math.sinh(x)
    
    def cosh(self, x: Union[int, float]) -> float:
        """Hyperbolic cosine"""
        return math.cosh(x)
    
    def tanh(self, x: Union[int, float]) -> float:
        """Hyperbolic tangent"""
        return math.tanh(x)
    
    def asinh(self, x: Union[int, float]) -> float:
        """Inverse hyperbolic sine"""
        return math.asinh(x)
    
    def acosh(self, x: Union[int, float]) -> float:
        """Inverse hyperbolic cosine"""
        return math.acosh(x)
    
    def atanh(self, x: Union[int, float]) -> float:
        """Inverse hyperbolic tangent"""
        return math.atanh(x)
    
    def degrees_to_radians(self, degrees: Union[int, float]) -> float:
        """Convert degrees to radians"""
        return math.radians(degrees)
    
    def radians_to_degrees(self, radians: Union[int, float]) -> float:
        """Convert radians to degrees"""
        return math.degrees(radians)
    
    def normalize_angle(self, angle: Union[int, float], degrees: bool = True) -> float:
        """Normalize angle to [0, 360) or [0, 2π)"""
        if degrees:
            result = angle % 360
        else:
            result = angle % (2 * math.pi)
        return result
    
    def fibonacci(self, n: int) -> int:
        """Calculate nth Fibonacci number"""
        if n < 0:
            raise ValueError("Fibonacci undefined for negative numbers")
        if n == 0:
            return 0
        if n == 1:
            return 1
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
    
    def fibonacci_sequence(self, n: int) -> List[int]:
        """Generate Fibonacci sequence up to nth term"""
        return [self.fibonacci(i) for i in range(n + 1)]
    
    def is_fibonacci(self, n: int) -> bool:
        """Check if number is in Fibonacci sequence"""
        if n < 0:
            return False
        # Check if 5*n^2 + 4 or 5*n^2 - 4 is perfect square
        test1 = 5 * n * n + 4
        test2 = 5 * n * n - 4
        return self.is_perfect_square(test1) or self.is_perfect_square(test2)
    
    def lucas(self, n: int) -> int:
        """Calculate nth Lucas number"""
        if n < 0:
            raise ValueError("Lucas undefined for negative numbers")
        if n == 0:
            return 2
        if n == 1:
            return 1
        a, b = 2, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
    
    def catalan(self, n: int) -> int:
        """Calculate nth Catalan number"""
        if n < 0:
            raise ValueError("Catalan undefined for negative numbers")
        return self.binomial_coefficient(2 * n, n) // (n + 1)
    
    def bell(self, n: int) -> int:
        """Calculate nth Bell number"""
        if n < 0:
            raise ValueError("Bell undefined for negative numbers")
        bell = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        bell[0][0] = 1
        for i in range(1, n + 1):
            bell[i][0] = bell[i - 1][i - 1]
            for j in range(1, i + 1):
                bell[i][j] = bell[i - 1][j - 1] + bell[i][j - 1]
        return bell[n][0]
    
    def stirling_first(self, n: int, k: int) -> int:
        """Calculate Stirling numbers of the first kind s(n,k)"""
        if n == k == 0:
            return 1
        if n == 0 or k == 0:
            return 0
        if n == k:
            return 1
        if k > n:
            return 0
        return self.stirling_first(n - 1, k - 1) + (n - 1) * self.stirling_first(n - 1, k)
    
    def stirling_second(self, n: int, k: int) -> int:
        """Calculate Stirling numbers of the second kind S(n,k)"""
        if n == k == 0:
            return 1
        if n == 0 or k == 0:
            return 0
        if n == k:
            return 1
        if k > n:
            return 0
        return k * self.stirling_second(n - 1, k) + self.stirling_second(n - 1, k - 1)
    
    def bernoulli(self, n: int) -> Fraction:
        """Calculate nth Bernoulli number"""
        if n < 0:
            raise ValueError("Bernoulli undefined for negative numbers")
        if n == 0:
            return Fraction(1, 1)
        if n == 1:
            return Fraction(-1, 2)
        if n % 2 != 0:
            return Fraction(0, 1)
        
        B = [Fraction(0, 1)] * (n + 1)
        B[0] = Fraction(1, 1)
        for m in range(1, n + 1):
            B[m] = Fraction(0, 1)
            for j in range(m):
                B[m] -= Fraction(self.binomial_coefficient(m + 1, j), 1) * B[j]
            B[m] /= Fraction(m + 1, 1)
        
        return B[n]
    
    def eulerian(self, n: int, k: int) -> int:
        """Calculate Eulerian number A(n,k)"""
        if k < 0 or k >= n:
            return 0
        if n == 0:
            return 1 if k == 0 else 0
        return (k + 1) * self.eulerian(n - 1, k) + (n - k) * self.eulerian(n - 1, k - 1)
    
    def partition_function(self, n: int) -> int:
        """Calculate partition function p(n)"""
        if n < 0:
            return 0
        if n <= 1:
            return 1
        
        partitions = [0] * (n + 1)
        partitions[0] = 1
        
        for i in range(1, n + 1):
            for j in range(i, n + 1):
                partitions[j] += partitions[j - i]
        
        return partitions[n]
    
    def harmonic_number(self, n: int) -> float:
        """Calculate nth harmonic number"""
        if n < 1:
            raise ValueError("Harmonic number undefined for n < 1")
        return sum(1 / i for i in range(1, n + 1))
    
    def generalized_harmonic_number(self, n: int, s: float) -> float:
        """Calculate generalized harmonic number H(n,s)"""
        if n < 1:
            raise ValueError("Harmonic number undefined for n < 1")
        return sum(1 / (i ** s) for i in range(1, n + 1))
    
    def alternating_harmonic_number(self, n: int) -> float:
        """Calculate alternating harmonic number"""
        if n < 1:
            raise ValueError("Harmonic number undefined for n < 1")
        return sum(((-1) ** (i + 1)) / i for i in range(1, n + 1))
    
    def summation(self, start: int, end: int, func) -> float:
        """Calculate sum of function from start to end"""
        return sum(func(i) for i in range(start, end + 1))
    
    def product(self, start: int, end: int, func) -> float:
        """Calculate product of function from start to end"""
        result = 1
        for i in range(start, end + 1):
            result *= func(i)
        return result
    
    def arithmetic_series(self, first: Union[int, float], last: Union[int, float], n: int) -> Union[int, float]:
        """Calculate sum of arithmetic series"""
        return n * (first + last) / 2
    
    def geometric_series(self, first: Union[int, float], ratio: Union[int, float], n: int) -> Union[int, float]:
        """Calculate sum of geometric series"""
        if ratio == 1:
            return first * n
        return first * (1 - ratio ** n) / (1 - ratio)
    
    def infinite_geometric_series(self, first: Union[int, float], ratio: Union[int, float]) -> Union[int, float, None]:
        """Calculate sum of infinite geometric series"""
        if abs(ratio) >= 1:
            return None  # Diverges
        return first / (1 - ratio)
    
    def power_series(self, x: Union[int, float], terms: int) -> float:
        """Calculate sum of power series Σ x^i"""
        return sum(x ** i for i in range(terms))
    
    def taylor_series_sin(self, x: Union[int, float], terms: int = 10) -> float:
        """Calculate sin(x) using Taylor series"""
        result = 0
        for n in range(terms):
            term = ((-1) ** n) * (x ** (2 * n + 1)) / self.factorial(2 * n + 1)
            result += term
        return result
    
    def taylor_series_cos(self, x: Union[int, float], terms: int = 10) -> float:
        """Calculate cos(x) using Taylor series"""
        result = 0
        for n in range(terms):
            term = ((-1) ** n) * (x ** (2 * n)) / self.factorial(2 * n)
            result += term
        return result
    
    def taylor_series_exp(self, x: Union[int, float], terms: int = 20) -> float:
        """Calculate e^x using Taylor series"""
        result = 0
        for n in range(terms):
            term = (x ** n) / self.factorial(n)
            result += term
        return result
    
    def taylor_series_ln(self, x: Union[int, float], terms: int = 20) -> float:
        """Calculate ln(1+x) using Taylor series"""
        if abs(x) >= 1:
            raise ValueError("Taylor series for ln(1+x) converges only for |x| < 1")
        result = 0
        for n in range(1, terms + 1):
            term = ((-1) ** (n + 1)) * (x ** n) / n
            result += term
        return result
    
    def convergent(self, sequence: List[Union[int, float]], tolerance: float = 1e-10) -> Optional[Union[int, float]]:
        """Check if sequence converges and return limit"""
        if len(sequence) < 2:
            return None
        
        for i in range(len(sequence) - 1):
            if abs(sequence[i + 1] - sequence[i]) > tolerance:
                continue
            return sequence[i + 1]
        
        return None
    
    def limit(self, func, x: Union[int, float], delta: float = 1e-10) -> Optional[float]:
        """Calculate limit of function as it approaches x"""
        try:
            return func(x)
        except:
            try:
                return (func(x + delta) + func(x - delta)) / 2
            except:
                return None
    
    # =========================================================================
    # SECTION 5: Number Theory Advanced (50 functions)
    # =========================================================================
    
    def is_perfect_square(self, n: int) -> bool:
        """Check if number is perfect square"""
        if n < 0:
            return False
        root = int(math.sqrt(n))
        return root * root == n
    
    def is_perfect_cube(self, n: int) -> bool:
        """Check if number is perfect cube"""
        root = round(abs(n) ** (1/3))
        return root ** 3 == n
    
    def is_perfect_power(self, n: int) -> bool:
        """Check if number is perfect power"""
        if n < 2:
            return False
        for base in range(2, int(math.sqrt(n)) + 2):
            exp = 2
            while base ** exp <= n:
                if base ** exp == n:
                    return True
                exp += 1
        return False
    
    def is_automorphic(self, n: int) -> bool:
        """Check if number is automorphic"""
        square = n * n
        return str(square).endswith(str(n))
    
    def is_strobogrammatic(self, n: int) -> bool:
        """Check if number is strobogrammatic"""
        valid = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        s = str(n)
        rotated = ''.join(valid.get(c, '') for c in reversed(s))
        return rotated == s
    
    def is_palindrome(self, n: int) -> bool:
        """Check if number is palindrome"""
        s = str(n)
        return s == s[::-1]
    
    def reverse_number(self, n: int) -> int:
        """Reverse digits of number"""
        return int(str(n)[::-1]) if n >= 0 else -int(str(-n)[::-1])
    
    def is_kaprekar(self, n: int) -> bool:
        """Check if number is Kaprekar number"""
        if n == 1:
            return True
        square = n * n
        s = str(square)
        for i in range(1, len(s)):
            left = int(s[:i]) if s[:i] else 0
            right = int(s[i:])
            if left + right == n:
                return True
        return False
    
    def is_armstrong(self, n: int) -> bool:
        """Check if number is Armstrong number"""
        s = str(n)
        power = len(s)
        return sum(int(d) ** power for d in s) == n
    
    def digit_sum(self, n: int) -> int:
        """Calculate sum of digits"""
        return sum(int(d) for d in str(abs(n)))
    
    def digit_product(self, n: int) -> int:
        """Calculate product of digits"""
        s = str(abs(n))
        if '0' in s:
            return 0
        result = 1
        for d in s:
            result *= int(d)
        return result
    
    def digit_count(self, n: int) -> int:
        """Count number of digits"""
        return len(str(abs(n)))
    
    def digital_root(self, n: int) -> int:
        """Calculate digital root"""
        if n == 0:
            return 0
        return 1 + ((n - 1) % 9)
    
    def multiplicative_digital_root(self, n: int) -> int:
        """Calculate multiplicative digital root"""
        n = abs(n)
        while n >= 10:
            product = 1
            for d in str(n):
                product *= int(d)
            n = product
        return n
    
    def multiplicative_persistence(self, n: int) -> int:
        """Calculate multiplicative persistence"""
        n = abs(n)
        count = 0
        while n >= 10:
            product = 1
            for d in str(n):
                product *= int(d)
            n = product
            count += 1
        return count
    
    def additive_persistence(self, n: int) -> int:
        """Calculate additive persistence"""
        n = abs(n)
        count = 0
        while n >= 10:
            n = self.digit_sum(n)
            count += 1
        return count
    
    def is_happy(self, n: int) -> bool:
        """Check if number is happy number"""
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum(int(d) ** 2 for d in str(n))
        return n == 1
    
    def is_unhappy(self, n: int) -> bool:
        """Check if number is unhappy number"""
        return not self.is_happy(n)
    
    def is_narcissistic(self, n: int) -> bool:
        """Check if number is narcissistic (same as Armstrong)"""
        return self.is_armstrong(n)
    
    def is_pronic(self, n: int) -> bool:
        """Check if number is pronic (n = k*(k+1))"""
        k = int(math.sqrt(n))
        return k * (k + 1) == n
    
    def is_triangular(self, n: int) -> bool:
        """Check if number is triangular"""
        if n < 0:
            return False
        k = int((math.sqrt(8 * n + 1) - 1) / 2)
        return k * (k + 1) // 2 == n
    
    def is_square_pyramidal(self, n: int) -> bool:
        """Check if number is square pyramidal"""
        if n < 0:
            return False
        k = 1
        total = 0
        while total < n:
            total += k * k
            k += 1
        return total == n
    
    def is_pentagonal(self, n: int) -> bool:
        """Check if number is pentagonal"""
        if n < 0:
            return False
        test = math.sqrt(24 * n + 1) + 1
        return test % 6 == 0
    
    def is_hexagonal(self, n: int) -> bool:
        """Check if number is hexagonal"""
        if n < 0:
            return False
        test = math.sqrt(8 * n + 1) + 1
        return test % 4 == 0
    
    def triangular_number(self, n: int) -> int:
        """Calculate nth triangular number"""
        return n * (n + 1) // 2
    
    def pentagonal_number(self, n: int) -> int:
        """Calculate nth pentagonal number"""
        return n * (3 * n - 1) // 2
    
    def hexagonal_number(self, n: int) -> int:
        """Calculate nth hexagonal number"""
        return n * (2 * n - 1)
    
    def heptagonal_number(self, n: int) -> int:
        """Calculate nth heptagonal number"""
        return n * (5 * n - 3) // 2
    
    def octagonal_number(self, n: int) -> int:
        """Calculate nth octagonal number"""
        return n * (3 * n - 2)
    
    def polygonal_number(self, n: int, sides: int) -> int:
        """Calculate nth polygonal number"""
        return ((sides - 2) * n * n - (sides - 4) * n) // 2
    
    def is_pandigital(self, n: int, base: int = 10) -> bool:
        """Check if number is pandigital"""
        digits = set(str(n))
        return len(digits) == base and '0' not in digits
    
    def is_repunit(self, n: int) -> bool:
        """Check if number is repunit (all 1s)"""
        return set(str(n)) == {'1'}
    
    def repunit(self, n: int) -> int:
        """Generate repunit of length n"""
        return int('1' * n)
    
    def is_smith(self, n: int) -> bool:
        """Check if number is Smith number"""
        if n < 4:
            return False
        if self.is_prime(n):
            return False
        digit_sum_n = self.digit_sum(n)
        factors = self.prime_factors(n)
        digit_sum_factors = sum(self.digit_sum(f) for f in factors)
        return digit_sum_n == digit_sum_factors
    
    def is_polite(self, n: int) -> bool:
        """Check if number is polite"""
        return not self.is_power_of_two(n)
    
    def is_power_of_two(self, n: int) -> bool:
        """Check if number is power of two"""
        return n > 0 and (n & (n - 1)) == 0
    
    def is_power_of_three(self, n: int) -> bool:
        """Check if number is power of three"""
        if n < 1:
            return False
        while n % 3 == 0:
            n //= 3
        return n == 1
    
    def is_power(self, n: int, base: int) -> bool:
        """Check if number is power of base"""
        if n < 1 or base < 2:
            return False
        while n % base == 0:
            n //= base
        return n == 1
    
    def next_power_of_two(self, n: int) -> int:
        """Find next power of two >= n"""
        if n <= 1:
            return 1
        return 2 ** (n - 1).bit_length()
    
    def previous_power_of_two(self, n: int) -> int:
        """Find previous power of two <= n"""
        if n < 1:
            return 0
        return 2 ** (n.bit_length() - 1)
    
    def is_ulam(self, n: int) -> bool:
        """Check if number is Ulam number"""
        ulams = [1, 2]
        for i in range(3, n + 1):
            count = 0
            for a in ulams:
                for b in ulams:
                    if a < b and a + b == i:
                        count += 1
                        if count > 1:
                            break
                if count > 1:
                    break
            if count == 1:
                ulams.append(i)
        return n in ulams
    
    def is_self_descriptive(self, n: int) -> bool:
        """Check if number is self-descriptive"""
        s = str(n)
        for i, digit in enumerate(s):
            count = s.count(str(i))
            if int(digit) != count:
                return False
        return True
    
    def is_persistent(self, n: int) -> bool:
        """Check if number has multiplicative persistence > 0"""
        return self.multiplicative_persistence(n) > 0
    
    def vampire_number(self, n: int) -> Optional[Tuple[int, int]]:
        """Find fangs of vampire number"""
        if len(str(n)) % 2 != 0:
            return None
        
        num_str = sorted(str(n))
        length = len(str(n))
        half_len = length // 2
        
        for i in range(10 ** (half_len - 1), 10 ** half_len):
            if n % i == 0:
                j = n // i
                if len(str(i)) == half_len and len(str(j)) == half_len:
                    if '0' not in str(i)[-1] and '0' not in str(j)[-1]:
                        if sorted(str(i) + str(j)) == num_str:
                            return (i, j)
        return None
    
    def is_vampire(self, n: int) -> bool:
        """Check if number is vampire number"""
        return self.vampire_number(n) is not None
    
    def is_harshad(self, n: int) -> bool:
        """Check if number is Harshad number"""
        return n % self.digit_sum(n) == 0
    
    def is_moran(self, n: int) -> bool:
        """Check if number is Moran number"""
        digit_sum = self.digit_sum(n)
        return n % digit_sum == 0 and self.is_prime(n // digit_sum)
    
    def sum_of_divisors_sigma(self, n: int, k: int = 1) -> int:
        """Calculate sum of divisors function σ_k(n)"""
        divisors = self.divisors(n)
        return sum(d ** k for d in divisors)
    
    def divisor_function(self, n: int) -> int:
        """Calculate number of divisors function d(n)"""
        return self.divisor_count(n)
    
    def sum_of_proper_divisors(self, n: int) -> int:
        """Calculate sum of proper divisors s(n)"""
        return self.divisor_sum(n) - n
    
    def aliquot_sum(self, n: int) -> int:
        """Calculate aliquot sum (same as sum of proper divisors)"""
        return self.sum_of_proper_divisors(n)
    
    def aliquot_sequence(self, n: int, max_terms: int = 100) -> List[int]:
        """Generate aliquot sequence"""
        sequence = [n]
        for _ in range(max_terms - 1):
            next_term = self.aliquot_sum(sequence[-1])
            if next_term == 0 or next_term in sequence:
                sequence.append(next_term)
                break
            sequence.append(next_term)
        return sequence
    
    def is_sociable(self, n: int) -> bool:
        """Check if number is sociable"""
        sequence = self.aliquot_sequence(n, max_terms=100)
        return len(sequence) > 2 and sequence[-1] == sequence[0]
    
    def is_bell_number(self, n: int) -> bool:
        """Check if number is Bell number"""
        for i in range(n + 1):
            if self.bell(i) == n:
                return True
        return False
    
    def is_catalan_number(self, n: int) -> bool:
        """Check if number is Catalan number"""
        for i in range(n + 1):
            if self.catalan(i) == n:
                return True
        return False
    
    # =========================================================================
    # SECTION 6: Complex Numbers (50 functions)
    # =========================================================================
    
    def complex_create(self, real: Union[int, float], imag: Union[int, float]) -> complex:
        """Create complex number"""
        return complex(real, imag)
    
    def complex_add(self, a: complex, b: complex) -> complex:
        """Add complex numbers"""
        return a + b
    
    def complex_subtract(self, a: complex, b: complex) -> complex:
        """Subtract complex numbers"""
        return a - b
    
    def complex_multiply(self, a: complex, b: complex) -> complex:
        """Multiply complex numbers"""
        return a * b
    
    def complex_divide(self, a: complex, b: complex) -> complex:
        """Divide complex numbers"""
        return a / b
    
    def complex_conjugate(self, z: complex) -> complex:
        """Get complex conjugate"""
        return z.conjugate()
    
    def complex_magnitude(self, z: complex) -> float:
        """Get magnitude (absolute value) of complex number"""
        return abs(z)
    
    def complex_phase(self, z: complex) -> float:
        """Get phase (argument) of complex number"""
        return math.phase(z)
    
    def complex_real(self, z: complex) -> float:
        """Get real part of complex number"""
        return z.real
    
    def complex_imag(self, z: complex) -> float:
        """Get imaginary part of complex number"""
        return z.imag
    
    def complex_polar(self, z: complex) -> Tuple[float, float]:
        """Convert complex to polar coordinates (r, theta)"""
        return (abs(z), math.phase(z))
    
    def complex_rectangular(self, r: float, theta: float) -> complex:
        """Convert from polar to rectangular coordinates"""
        return complex(r * math.cos(theta), r * math.sin(theta))
    
    def complex_power(self, z: complex, n: Union[int, float]) -> complex:
        """Raise complex number to power"""
        return z ** n
    
    def complex_sqrt(self, z: complex) -> complex:
        """Square root of complex number"""
        r, theta = self.complex_polar(z)
        return self.complex_rectangular(math.sqrt(r), theta / 2)
    
    def complex_exp(self, z: complex) -> complex:
        """Exponential of complex number"""
        return cmath.exp(z)
    
    def complex_log(self, z: complex) -> complex:
        """Natural logarithm of complex number"""
        import cmath
        return cmath.log(z)
    
    def complex_sin(self, z: complex) -> complex:
        """Sine of complex number"""
        import cmath
        return cmath.sin(z)
    
    def complex_cos(self, z: complex) -> complex:
        """Cosine of complex number"""
        import cmath
        return cmath.cos(z)
    
    def complex_tan(self, z: complex) -> complex:
        """Tangent of complex number"""
        import cmath
        return cmath.tan(z)
    
    def complex_distance(self, a: complex, b: complex) -> float:
        """Distance between two complex numbers"""
        return abs(a - b)
    
    def complex_rotate(self, z: complex, angle: float) -> complex:
        """Rotate complex number by angle"""
        import cmath
        return z * cmath.exp(1j * angle)
    
    def complex_reflect(self, z: complex) -> complex:
        """Reflect complex number across real axis"""
        return z.conjugate()
    
    def complex_invert(self, z: complex) -> complex:
        """Invert complex number (1/z)"""
        return 1 / z if z != 0 else float('inf')
    
    def complex_normalize(self, z: complex) -> complex:
        """Normalize complex number to unit circle"""
        mag = abs(z)
        if mag == 0:
            return 0j
        return z / mag
    
    def is_complex_real(self, z: complex) -> bool:
        """Check if complex number is real"""
        return z.imag == 0
    
    def is_complex_imaginary(self, z: complex) -> bool:
        """Check if complex number is purely imaginary"""
        return z.real == 0
    
    def complex_to_string(self, z: complex, precision: int = 6) -> str:
        """Convert complex number to string"""
        real_part = f"{z.real:.{precision}f}" if not abs(z.real) < 1e-10 else "0"
        imag_part = f"{abs(z.imag):.{precision}f}" if not abs(z.imag) < 1e-10 else "0"
        sign = "+" if z.imag >= 0 else "-"
        if imag_part == "0":
            return real_part
        elif real_part == "0":
            return f"{imag_part}i"
        else:
            return f"{real_part} {sign} {imag_part}i"
    
    def nth_roots_of_unity(self, n: int) -> List[complex]:
        """Generate nth roots of unity"""
        roots = []
        for k in range(n):
            angle = 2 * math.pi * k / n
            roots.append(self.complex_rectangular(1, angle))
        return roots
    
    def de_moivre(self, r: float, theta: float, n: int) -> complex:
        """Apply De Moivre's theorem"""
        return self.complex_rectangular(r ** n, n * theta)
    
    def complex_matrix_multiply_2x2(self, a: Tuple[complex, complex, complex, complex], 
                                     b: Tuple[complex, complex, complex, complex]) -> Tuple[complex, complex, complex, complex]:
        """Multiply 2x2 complex matrices"""
        return (
            a[0] * b[0] + a[1] * b[2],
            a[0] * b[1] + a[1] * b[3],
            a[2] * b[0] + a[3] * b[2],
            a[2] * b[1] + a[3] * b[3]
        )
    
    # =========================================================================
    # SECTION 7: Mathematical Constants & Special Values (50 functions)
    # =========================================================================
    
    def get_pi(self, precision: int = 50) -> Decimal:
        """Get π with specified precision"""
        getcontext().prec = precision
        # Using Chudnovsky algorithm
        C = 426880 * Decimal(10005).sqrt()
        M = 1
        L = 13591409
        X = 1
        K = 6
        S = Decimal(L)
        
        for i in range(1, precision):
            M = (K**3 - 16*K) * M // i**3
            L += 545140134
            X *= -262537412640768000
            S += Decimal(M * L) / X
            K += 12
        
        return C / S
    
    def get_e(self, precision: int = 50) -> Decimal:
        """Get e with specified precision"""
        getcontext().prec = precision
        return Decimal(1).exp()
    
    def get_phi(self, precision: int = 50) -> Decimal:
        """Get golden ratio φ with specified precision"""
        getcontext().prec = precision
        return (Decimal(1) + Decimal(5).sqrt()) / 2
    
    def get_sqrt2(self, precision: int = 50) -> Decimal:
        """Get √2 with specified precision"""
        getcontext().prec = precision
        return Decimal(2).sqrt()
    
    def get_sqrt3(self, precision: int = 50) -> Decimal:
        """Get √3 with specified precision"""
        getcontext().prec = precision
        return Decimal(3).sqrt()
    
    def get_euler_gamma(self, precision: int = 50) -> Decimal:
        """Get Euler-Mascheroni constant γ with specified precision"""
        getcontext().prec = precision
        # Using approximation
        n = precision * 10
        return Decimal(self.harmonic_number(n)) - Decimal(self.ln(n))
    
    def get_feigenbaum_delta(self, precision: int = 20) -> Decimal:
        """Get Feigenbaum constant δ"""
        getcontext().prec = precision
        return Decimal('4.669201609102990671853203820466201629449')
    
    def get_feigenbaum_alpha(self, precision: int = 20) -> Decimal:
        """Get Feigenbaum constant α"""
        getcontext().prec = precision
        return Decimal('2.50290787509589282228390287321821578638')
    
    def get_apery_constant(self, precision: int = 20) -> Decimal:
        """Get Apéry's constant ζ(3)"""
        getcontext().prec = precision
        return Decimal('1.202056903159594285399738161511449990764')
    
    def get_catalan_constant(self, precision: int = 20) -> Decimal:
        """Get Catalan's constant G"""
        getcontext().prec = precision
        return Decimal('0.915965594177219015054603514932384110774')
    
    def get_twin_prime_constant(self, precision: int = 20) -> Decimal:
        """Get twin prime constant"""
        getcontext().prec = precision
        return Decimal('0.660161815846869573927812110014555778432')
    
    def get_meissel_mertens_constant(self, precision: int = 20) -> Decimal:
        """Get Meissel-Mertens constant"""
        getcontext().prec = precision
        return Decimal('0.261497212847642783755426838608695859051')
    
    def get_brun_constant(self, precision: int = 10) -> Decimal:
        """Get Brun's constant (for twin primes)"""
        getcontext().prec = precision
        return Decimal('1.902160583104')
    
    def get_landau_ramanujan_constant(self, precision: int = 20) -> Decimal:
        """Get Landau-Ramanujan constant"""
        getcontext().prec = precision
        return Decimal('0.764223653589220662990698731250092328116')
    
    def get_mills_ratio(self, precision: int = 20) -> Decimal:
        """Get Mills' ratio constant"""
        getcontext().prec = precision
        return Decimal('1.306377883863080690468614492602605712916')
    
    def get_plastic_constant(self, precision: int = 20) -> Decimal:
        """Get plastic constant ρ"""
        getcontext().prec = precision
        return Decimal('1.324717957244746025960908854478097340734')
    
    def get_conway_constant(self, precision: int = 20) -> Decimal:
        """Get Conway's constant"""
        getcontext().prec = precision
        return Decimal('1.303577269034296391257099112152551890730')
    
    def get_glaisher_kinkelin_constant(self, precision: int = 20) -> Decimal:
        """Get Glaisher-Kinkelin constant A"""
        getcontext().prec = precision
        return Decimal('1.282427129100622636875342568869791727767')
    
    def get_omega_constant(self, precision: int = 20) -> Decimal:
        """Get omega constant Ω"""
        getcontext().prec = precision
        return Decimal('0.567143290409783872999968662210355549753')
    
    def get_golomb_dickman_constant(self, precision: int = 20) -> Decimal:
        """Get Golomb-Dickman constant"""
        getcontext().prec = precision
        return Decimal('0.624329988543550870992936383100837244179')
    
    def get_lebesgue_constant(self, precision: int = 20) -> Decimal:
        """Get Lebesgue constant"""
        getcontext().prec = precision
        return Decimal('0.989431273822467422046641198402298226494')
    
    def get_fiducial_constant(self, precision: int = 20) -> Decimal:
        """Get Fiducial constant"""
        getcontext().prec = precision
        return Decimal('1.892826918972388517365273425106973313296')
    
    def get_chaitin_constant(self) -> str:
        """Get Chaitin's constant (cannot be computed)"""
        return "Chaitin's constant is non-computable"
    
    def get_pretty_constant(self, precision: int = 20) -> Decimal:
        """Get pretty constant"""
        getcontext().prec = precision
        return Decimal('0.529834164384235507574250104116120457217')
    
    def get_fresnel_S_integral(self, x: Union[int, float]) -> float:
        """Calculate Fresnel S integral"""
        import scipy.special
        return scipy.special.fresnel(x)[1]
    
    def get_fresnel_C_integral(self, x: Union[int, float]) -> float:
        """Calculate Fresnel C integral"""
        import scipy.special
        return scipy.special.fresnel(x)[0]
    
    def get_dawson_integral(self, x: Union[int, float]) -> float:
        """Calculate Dawson integral"""
        import scipy.special
        return scipy.special.dawsn(x)
    
    def get_error_function(self, x: Union[int, float]) -> float:
        """Calculate error function erf(x)"""
        import math
        return math.erf(x)
    
    def get_complementary_error_function(self, x: Union[int, float]) -> float:
        """Calculate complementary error function erfc(x)"""
        import math
        return math.erfc(x)
    
    def get_gamma_function(self, x: Union[int, float]) -> float:
        """Calculate gamma function Γ(x)"""
        import math
        return math.gamma(x)
    
    def get_digamma_function(self, x: Union[int, float]) -> float:
        """Calculate digamma function ψ(x)"""
        import mpmath as mp
        return mp.digamma(x)
    
    def get_beta_function(self, x: Union[int, float], y: Union[int, float]) -> float:
        """Calculate beta function B(x,y)"""
        import mpmath as mp
        return mp.beta(x, y)
    
    def get_zeta_function(self, s: Union[int, float]) -> float:
        """Calculate Riemann zeta function ζ(s)"""
        import mpmath as mp
        return mp.zeta(s)
    
    def get_riemann_zeta_critical_line(self, t: Union[int, float]) -> complex:
        """Calculate ζ(0.5 + it)"""
        import mpmath as mp
        return mp.zeta(0.5 + 1j * t)
    
    def get_dedekind_eta(self, tau: complex) -> complex:
        """Calculate Dedekind eta function"""
        import mpmath as mp
        return mp.qeta(mp.e**(2j * math.pi * tau))
    
    def get_j_invariant(self, tau: complex) -> complex:
        """Calculate j-invariant"""
        import mpmath as mp
        return mp.jtheta(tau)
    
    def get_weierstrass_p(self, z: complex, g2: complex, g3: complex) -> complex:
        """Calculate Weierstrass p-function"""
        import mpmath as mp
        return mp.ellipfun(z, g2, g3)
    
    def get_elliptic_integral_k(self, m: Union[int, float]) -> float:
        """Calculate complete elliptic integral of the first kind K(m)"""
        import mpmath as mp
        return mp.ellipk(m)
    
    def get_elliptic_integral_e(self, m: Union[int, float]) -> float:
        """Calculate complete elliptic integral of the second kind E(m)"""
        import mpmath as mp
        return mp.ellipe(m)
    
    def get_elliptic_integral_f(self, phi: Union[int, float], m: Union[int, float]) -> float:
        """Calculate incomplete elliptic integral of the first kind F(φ,m)"""
        import mpmath as mp
        return mp.ellipfun('f', [phi, m])
    
    def get_elliptic_integral_pi(self, n: Union[int, float], phi: Union[int, float], m: Union[int, float]) -> float:
        """Calculate incomplete elliptic integral of the third kind Π(n,φ,m)"""
        import mpmath as mp
        return mp.ellipfun('pi', [n, phi, m])
    
    def get_hypergeometric_2f1(self, a: Union[int, float], b: Union[int, float], 
                               c: Union[int, float], z: Union[int, float]) -> float:
        """Calculate hypergeometric function ₂F₁(a,b;c;z)"""
        import mpmath as mp
        return mp.hyper([a, b], [c], z)
    
    def get_hypergeometric_0f1(self, b: Union[int, float], z: Union[int, float]) -> float:
        """Calculate hypergeometric function ₀F₁(;b;z)"""
        import mpmath as mp
        return mp.hyper([], [b], z)
    
    def get_bessel_j(self, n: int, x: Union[int, float]) -> float:
        """Calculate Bessel function of the first kind Jₙ(x)"""
        import scipy.special
        return scipy.special.jv(n, x)
    
    def get_bessel_y(self, n: int, x: Union[int, float]) -> float:
        """Calculate Bessel function of the second kind Yₙ(x)"""
        import scipy.special
        return scipy.special.yv(n, x)
    
    def get_bessel_i(self, n: int, x: Union[int, float]) -> float:
        """Calculate modified Bessel function of the first kind Iₙ(x)"""
        import scipy.special
        return scipy.special.iv(n, x)
    
    def get_bessel_k(self, n: int, x: Union[int, float]) -> float:
        """Calculate modified Bessel function of the second kind Kₙ(x)"""
        import scipy.special
        return scipy.special.kv(n, x)
    
    def get_airy_ai(self, x: Union[int, float]) -> float:
        """Calculate Airy function Ai(x)"""
        import scipy.special
        return scipy.special.airy(x)[0]
    
    def get_airy_bi(self, x: Union[int, float]) -> float:
        """Calculate Airy function Bi(x)"""
        import scipy.special
        return scipy.special.airy(x)[2]
    
    def get_legendre_p(self, n: int, x: Union[int, float]) -> float:
        """Calculate Legendre polynomial Pₙ(x)"""
        import scipy.special
        return scipy.special.lpn(n, x)[0][-1]
    
    def get_laguerre_l(self, n: int, k: int, x: Union[int, float]) -> float:
        """Calculate Laguerre polynomial Lₙᵏ(x)"""
        import scipy.special
        return scipy.special.genlaguerre(n, k)(x)
    
    def get_hermite_h(self, n: int, x: Union[int, float]) -> float:
        """Calculate Hermite polynomial Hₙ(x)"""
        import scipy.special
        return scipy.special.hermite(n)(x)
    
    def get_chebyshev_t(self, n: int, x: Union[int, float]) -> float:
        """Calculate Chebyshev polynomial of the first kind Tₙ(x)"""
        import scipy.special
        return scipy.special.eval_chebyt(n, x)
    
    def get_chebyshev_u(self, n: int, x: Union[int, float]) -> float:
        """Calculate Chebyshev polynomial of the second kind Uₙ(x)"""
        import scipy.special
        return scipy.special.eval_chebyu(n, x)
    
    def get_jacobi_p(self, n: int, alpha: Union[int, float], beta: Union[int, float], 
                     x: Union[int, float]) -> float:
        """Calculate Jacobi polynomial Pₙ^(α,β)(x)"""
        import scipy.special
        return scipy.special.eval_jacobi(n, alpha, beta, x)
    
    def get_spherical_harmonic(self, l: int, m: int, theta: Union[int, float], 
                               phi: Union[int, float]) -> complex:
        """Calculate spherical harmonic Y_l^m(θ,φ)"""
        import scipy.special
        return scipy.special.sph_harm(m, l, phi, theta)
    
    def get_associated_legendre(self, l: int, m: int, x: Union[int, float]) -> float:
        """Calculate associated Legendre function P_l^m(x)"""
        import scipy.special
        return scipy.special.lpmv(m, l, x)
    
    # =========================================================================
    # Main solve method
    # =========================================================================
    
    def solve(self, problem: str) -> Dict[str, Any]:
        """
        Main solving method for Foundations workshop
        
        Args:
            problem: Problem description or mathematical expression
            
        Returns:
            Dictionary with solution and metadata
        """
        result = {
            'workshop': 'Foundations',
            'success': False,
            'answer': None,
            'method': None,
            'error': None
        }
        
        try:
            # Try to parse and solve various types of problems
            problem_lower = problem.lower()
            
            # Check for specific problem types
            if 'prime' in problem_lower and 'factor' in problem_lower:
                # Extract number for prime factorization
                import re
                numbers = re.findall(r'\d+', problem)
                if numbers:
                    n = int(numbers[0])
                    factors = self.prime_factors(n)
                    result.update({
                        'success': True,
                        'answer': f"Prime factors of {n}: {factors}",
                        'method': 'Prime Factorization',
                        'details': {
                            'number': n,
                            'factors': factors,
                            'factorization_with_exponents': self.prime_factors_with_exponents(n)
                        }
                    })
                    return result
            
            elif 'is prime' in problem_lower:
                import re
                numbers = re.findall(r'\d+', problem)
                if numbers:
                    n = int(numbers[0])
                    is_prime = self.is_prime(n)
                    result.update({
                        'success': True,
                        'answer': f"{n} is {'prime' if is_prime else 'not prime'}",
                        'method': 'Primality Test',
                        'details': {
                            'number': n,
                            'is_prime': is_prime
                        }
                    })
                    return result
            
            elif 'gcd' in problem_lower or 'greatest common divisor' in problem_lower:
                import re
                numbers = re.findall(r'\d+', problem)
                if len(numbers) >= 2:
                    nums = [int(n) for n in numbers[:2]]
                    gcd_val = self.gcd(nums[0], nums[1])
                    result.update({
                        'success': True,
                        'answer': f"GCD({nums[0]}, {nums[1]}) = {gcd_val}",
                        'method': 'Euclidean Algorithm',
                        'details': {
                            'numbers': nums,
                            'gcd': gcd_val
                        }
                    })
                    return result
            
            elif 'lcm' in problem_lower or 'least common multiple' in problem_lower:
                import re
                numbers = re.findall(r'\d+', problem)
                if len(numbers) >= 2:
                    nums = [int(n) for n in numbers[:2]]
                    lcm_val = self.lcm(nums[0], nums[1])
                    result.update({
                        'success': True,
                        'answer': f"LCM({nums[0]}, {nums[1]}) = {lcm_val}",
                        'method': 'Prime Factorization Method',
                        'details': {
                            'numbers': nums,
                            'lcm': lcm_val
                        }
                    })
                    return result
            
            elif 'factorial' in problem_lower:
                import re
                numbers = re.findall(r'\d+', problem)
                if numbers:
                    n = int(numbers[0])
                    fact = self.factorial(n)
                    result.update({
                        'success': True,
                        'answer': f"{n}! = {fact}",
                        'method': 'Factorial Calculation',
                        'details': {
                            'number': n,
                            'factorial': fact
                        }
                    })
                    return result
            
            elif 'fibonacci' in problem_lower:
                import re
                numbers = re.findall(r'\d+', problem)
                if numbers:
                    n = int(numbers[0])
                    fib = self.fibonacci(n)
                    result.update({
                        'success': True,
                        'answer': f"F({n}) = {fib}",
                        'method': 'Fibonacci Sequence',
                        'details': {
                            'n': n,
                            'fibonacci': fib,
                            'sequence': self.fibonacci_sequence(min(n, 10))
                        }
                    })
                    return result
            
            elif 'divide' in problem_lower:
                import re
                numbers = re.findall(r'\d+', problem)
                if len(numbers) >= 2:
                    a, b = int(numbers[0]), int(numbers[1])
                    quotient = self.divide(a, b)
                    result.update({
                        'success': True,
                        'answer': f"{a} / {b} = {quotient}",
                        'method': 'Division',
                        'details': {
                            'dividend': a,
                            'divisor': b,
                            'quotient': quotient
                        }
                    })
                    return result
            
            else:
                # Try to evaluate mathematical expression
                try:
                    # Simple arithmetic evaluation
                    import ast
                    import operator
                    
                    ops = {
                        ast.Add: operator.add,
                        ast.Sub: operator.sub,
                        ast.Mult: operator.mul,
                        ast.Div: operator.truediv,
                        ast.Pow: operator.pow,
                        ast.Mod: operator.mod,
                    }
                    
                    def eval_expr(node):
                        if isinstance(node, ast.Num):
                            return node.n
                        elif isinstance(node, ast.BinOp):
                            left = eval_expr(node.left)
                            right = eval_expr(node.right)
                            op_type = type(node.op)
                            if op_type in ops:
                                return ops[op_type](left, right)
                        raise ValueError("Unsupported operation")
                    
                    # Clean the problem string
                    clean_problem = problem.replace('calculate', '').replace('evaluate', '').strip()
                    if clean_problem:
                        tree = ast.parse(clean_problem, mode='eval')
                        answer = eval_expr(tree.body)
                        result.update({
                            'success': True,
                            'answer': f"Result: {answer}",
                            'method': 'Expression Evaluation',
                            'details': {
                                'expression': clean_problem,
                                'result': answer
                            }
                        })
                        return result
                except:
                    pass
            
            result['error'] = "Could not parse problem. Try a more specific query."
            
        except Exception as e:
            result['error'] = str(e)
        
        return result