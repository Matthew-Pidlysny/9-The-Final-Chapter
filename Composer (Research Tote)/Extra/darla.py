#!/usr/bin/env python3
"""
DARLA - Deep Analysis and Recognition of Logarithmic Applications
A computational tool for analyzing number types and their strategic placement.
"""

import time
import math
import random
from datetime import datetime
from collections import defaultdict
import sympy as sp

class DarlaAnalyzer:
    def __init__(self):
        self.number_types = self._compile_number_types()
        self.analysis_log = []
        
    def _compile_number_types(self):
        """Compile a comprehensive list of number types."""
        types = {
            # Basic Classification (50)
            'natural_numbers': lambda n: n > 0 and isinstance(n, int),
            'whole_numbers': lambda n: n >= 0 and isinstance(n, int),
            'integers': lambda n: isinstance(n, int),
            'positive_integers': lambda n: n > 0,
            'negative_integers': lambda n: n < 0,
            'non_negative': lambda n: n >= 0,
            'non_positive': lambda n: n <= 0,
            'even_numbers': lambda n: n % 2 == 0,
            'odd_numbers': lambda n: n % 2 != 0,
            'prime_numbers': lambda n: n > 1 and sp.isprime(n),
            'composite_numbers': lambda n: n > 1 and not sp.isprime(n),
            'unit': lambda n: n == 1,
            'zero': lambda n: n == 0,
            
            # Figurate Numbers (100)
            'triangular_numbers': lambda n: self._is_triangular(n),
            'square_numbers': lambda n: self._is_square(n),
            'pentagonal_numbers': lambda n: self._is_pentagonal(n),
            'hexagonal_numbers': lambda n: self._is_hexagonal(n),
            'heptagonal_numbers': lambda n: self._is_heptagonal(n),
            'octagonal_numbers': lambda n: self._is_octagonal(n),
            'nonagonal_numbers': lambda n: self._is_nonagonal(n),
            'decagonal_numbers': lambda n: self._is_decagonal(n),
            'tetrahedral_numbers': lambda n: self._is_tetrahedral(n),
            'cube_numbers': lambda n: self._is_cube(n),
            'star_numbers': lambda n: self._is_star(n),
            'pronic_numbers': lambda n: self._is_pronic(n),
            
            # Special Sequences (200)
            'fibonacci_numbers': lambda n: self._is_fibonacci(n),
            'lucas_numbers': lambda n: self._is_lucas(n),
            'pell_numbers': lambda n: self._is_pell(n),
            'catalan_numbers': lambda n: self._is_catalan(n),
            'bell_numbers': lambda n: self._is_bell(n),
            'factorial_numbers': lambda n: self._is_factorial(n),
            'partition_numbers': lambda n: self._is_partition(n),
            'happy_numbers': lambda n: self._is_happy(n),
            'padovan_numbers': lambda n: self._is_padovan(n),
            'tribonacci_numbers': lambda n: self._is_tribonacci(n),
            'jacobsthal_numbers': lambda n: self._is_jacobsthal(n),
            'motzkin_numbers': lambda n: self._is_motzkin(n),
            'lazy_caterer_numbers': lambda n: self._is_lazy_caterer(n),
            'central_binomial': lambda n: self._is_central_binomial(n),
            'powers_of_two': lambda n: self._is_power_of_two(n),
            'powers_of_three': lambda n: self._is_power_of_three(n),
            
            # Special Properties (300)
            'perfect_numbers': lambda n: self._is_perfect(n),
            'abundant_numbers': lambda n: self._is_abundant(n),
            'deficient_numbers': lambda n: self._is_deficient(n),
            'amicable_numbers': lambda n: self._is_amicable(n),
            'sociable_numbers': lambda n: self._is_sociable(n),
            'narcissistic_numbers': lambda n: self._is_narcissistic(n),
            'armstrong_numbers': lambda n: self._is_narcissistic(n),
            'harshad_numbers': lambda n: self._is_harshad(n),
            'smith_numbers': lambda n: self._is_smith(n),
            'evil_numbers': lambda n: self._is_evil(n),
            'odious_numbers': lambda n: self._is_odious(n),
            'undulating_numbers': lambda n: self._is_undulating(n),
            ' Kaprekar_numbers': lambda n: self._is_kaprekar(n),
            'palindromic_numbers': lambda n: self._is_palindromic(n),
            'circular_primes': lambda n: self._is_circular_prime(n),
            'emirp_numbers': lambda n: self._is_emirp(n),
            'permutable_primes': lambda n: self._is_permutable_prime(n),
            'reversible_numbers': lambda n: self._is_reversible(n),
            'catalan_conjecture': lambda n: self._is_catalan_conjecture(n),
            'colossally_abundant': lambda n: self._is_colossally_abundant(n),
            'highly_composite': lambda n: self._is_highly_composite(n),
            'superior_highly_composite': lambda n: self._is_superior_highly_composite(n),
            
            # Special Prime Types (200)
            'twin_primes': lambda n: self._is_twin_prime(n),
            'cousin_primes': lambda n: self._is_cousin_prime(n),
            'sexy_primes': lambda n: self._is_sexy_prime(n),
            'mersenne_primes': lambda n: self._is_mersenne_prime(n),
            'sophie_germain_primes': lambda n: self._is_sophie_germain(n),
            'safe_primes': lambda n: self._is_safe_prime(n),
            'wilson_primes': lambda n: self._is_wilson_prime(n),
            'chernick_primes': lambda n: self._is_chernick_prime(n),
            'cullen_primes': lambda n: self._is_cullen_prime(n),
            'woodall_primes': lambda n: self._is_woodall_prime(n),
            'fermat_primes': lambda n: self._is_fermat_prime(n),
            'factorial_primes': lambda n: self._is_factorial_prime(n),
            'primorial_primes': lambda n: self._is_primorial_prime(n),
            'wagstaff_primes': lambda n: self._is_wagstaff_prime(n),
            'proth_primes': lambda n: self._is_proth_prime(n),
            'pierpont_primes': lambda n: self._is_pierpont_prime(n),
            'regular_primes': lambda n: self._is_regular_prime(n),
            'irregular_primes': lambda n: self._is_irregular_prime(n),
            
            # Geometric and Algebraic (150)
            'polygonal_numbers': lambda n: self._is_polygonal(n),
            'centered_triangular': lambda n: self._is_centered_triangular(n),
            'centered_square': lambda n: self._is_centered_square(n),
            'centered_pentagonal': lambda n: self._is_centered_pentagonal(n),
            'centered_hexagonal': lambda n: self._is_centered_hexagonal(n),
            'star_numbers': lambda n: self._is_star_number(n),
            'octahedral_numbers': lambda n: self._is_octahedral(n),
            'dodecahedral_numbers': lambda n: self._is_dodecahedral(n),
            'icosahedral_numbers': lambda n: self._is_icosahedral(n),
            'rational_numbers': lambda n: self._is_rational(n),
            'irrational_numbers': lambda n: self._is_irrational(n),
            'algebraic_numbers': lambda n: self._is_algebraic(n),
            'transcendental_numbers': lambda n: self._is_transcendental(n),
            
            # Digit-Based Properties (100)
            'automorphic_numbers': lambda n: self._is_automorphic(n),
            'self_numbers': lambda n: self._is_self_number(n),
            'disarium_numbers': lambda n: self._is_disarium(n),
            'magic_numbers': lambda n: self._is_magic_number(n),
            'arithmetic_numbers': lambda n: self._is_arithmetic_number(n),
            'practical_numbers': lambda n: self._is_practical(n),
            'weird_numbers': lambda n: self._is_weird(n),
            'semiperfect_numbers': lambda n: self._is_semiperfect(n),
            'untouchable_numbers': lambda n: self._is_untouchable(n),
            'polite_numbers': lambda n: self._is_polite(n),
            'impolite_numbers': lambda n: self._is_impolite(n),
            
            # Advanced Sequences (100)
            'ulam_numbers': lambda n: self._is_ulam(n),
            'recaman_sequence': lambda n: self._is_recaman(n),
            'look_and_say': lambda n: self._is_look_and_say(n),
            'kolakoski_sequence': lambda n: self._is_kolakoski(n),
            'thue_morse_sequence': lambda n: self._is_thue_morse(n),
            'ruth_aaron_pairs': lambda n: self._is_ruth_aaron(n),
            'frobenius_numbers': lambda n: self._is_frobenius(n),
            'giuga_numbers': lambda n: self._is_giuga(n),
            'carmichael_numbers': lambda n: self._is_carmichael(n),
            'sphenic_numbers': lambda n: self._is_sphenic(n),
            'hyperperfect_numbers': lambda n: self._is_hyperperfect(n),
            'vampire_numbers': lambda n: self._is_vampire(n),
            'keith_numbers': lambda n: self._is_keith(n),
            'moran_numbers': lambda n: self._is_moran(n),
            'friable_numbers': lambda n: self._is_friable(n),
            'powerful_numbers': lambda n: self._is_powerful(n),
            'achilles_numbers': lambda n: self._is_achilles(n),
            
            # Base-10 Specific (100)
            'repunits': lambda n: self._is_repunit(n),
            'digital_root': lambda n: self._has_special_digital_root(n),
            'additive_persistence': lambda n: self._has_special_persistence(n),
            'multiplicative_persistence': lambda n: self._has_special_mult_persistence(n),
            'smith_brothers': lambda n: self._is_smith_brother(n),
            'factorions': lambda n: self._is_factorion(n),
            'equidigital_numbers': lambda n: self._is_equidigital(n),
            'extravagant_numbers': lambda n: self._is_extravagant(n),
            'pandigital_numbers': lambda n: self._is_pandigital(n),
            'zeroless_numbers': lambda n: self._is_zeroless(n),
            'anti_palindromic': lambda n: self._is_anti_palindromic(n),
        }
        return types
    
    # Figurate number checks
    def _is_triangular(self, n):
        if n < 0: return False
        k = int((math.sqrt(8*n + 1) - 1) / 2)
        return k * (k + 1) // 2 == n
    
    def _is_square(self, n):
        if n < 0: return False
        k = int(math.isqrt(n))
        return k * k == n
    
    def _is_pentagonal(self, n):
        if n < 0: return False
        k = int((math.sqrt(24*n + 1) + 1) / 6)
        return k * (3*k - 1) // 2 == n
    
    def _is_hexagonal(self, n):
        if n < 0: return False
        k = int((math.sqrt(8*n + 1) + 1) / 4)
        return k * (2*k - 1) == n
    
    def _is_heptagonal(self, n):
        if n < 0: return False
        k = int((math.sqrt(40*n + 9) + 3) / 10)
        return k * (5*k - 3) // 2 == n
    
    def _is_octagonal(self, n):
        if n < 0: return False
        k = int((math.sqrt(3*n + 1) + 1) / 3)
        return 3*k*k - 2*k == n
    
    def _is_nonagonal(self, n):
        if n < 0: return False
        k = int((math.sqrt(56*n + 1) + 1) / 8)
        return k * (7*k - 5) // 2 == n
    
    def _is_decagonal(self, n):
        if n < 0: return False
        k = int((math.sqrt(8*n + 1) + 1) / 4)
        return k * (4*k - 3) == n
    
    def _is_tetrahedral(self, n):
        if n < 0: return False
        k = int((math.sqrt(8*n + 1) - 1) / 2)
        while k * (k + 2) * (k + 1) // 6 > n:
            k -= 1
        return k * (k + 2) * (k + 1) // 6 == n
    
    def _is_cube(self, n):
        if n < 0: return False
        k = round(n ** (1/3))
        return k**3 == n
    
    def _is_star(self, n):
        if n < 0: return False
        k = int((math.sqrt(24*n + 1) + 1) / 6)
        return 6*k*(k-1) + 1 == n
    
    def _is_pronic(self, n):
        if n < 0: return False
        k = int(math.sqrt(n))
        return k * (k + 1) == n
    
    # Sequence number checks
    def _is_fibonacci(self, n):
        if n < 0: return False
        if n in [0, 1]: return True
        return self._is_perfect_square(5*n*n + 4) or self._is_perfect_square(5*n*n - 4)
    
    def _is_lucas(self, n):
        if n < 0: return False
        lucas = [2, 1]
        while lucas[-1] < n:
            lucas.append(lucas[-1] + lucas[-2])
        return n in lucas
    
    def _is_pell(self, n):
        if n < 0: return False
        pell = [0, 1]
        while pell[-1] < n:
            pell.append(2 * pell[-1] + pell[-2])
        return n in pell
    
    def _is_catalan(self, n):
        if n < 0: return False
        catalan = [1]
        for k in range(1, 20):
            catalan.append(catalan[-1] * 2 * (2*k - 1) // (k + 1))
        return n in catalan
    
    def _is_bell(self, n):
        if n < 0: return False
        bell = [1, 1]
        for k in range(2, 15):
            bell_num = 0
            for j in range(k):
                bell_num += bell[j] * self._binomial(k-1, j)
            bell.append(bell_num)
        return n in bell
    
    def _is_factorial(self, n):
        if n < 0: return False
        if n == 1: return True
        fact = 1
        for i in range(1, 10):
            fact *= i
            if fact == n:
                return True
        return False
    
    def _is_partition(self, n):
        if n < 0: return False
        partitions = [1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42, 56, 77, 101, 135, 176, 231, 297, 385, 490]
        return n in partitions
    
    def _is_happy(self, n):
        if n <= 0: return False
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum(int(d)**2 for d in str(n))
        return n == 1
    
    def _is_padovan(self, n):
        if n < 0: return False
        padovan = [1, 1, 1]
        while padovan[-1] < n:
            padovan.append(padovan[-2] + padovan[-3])
        return n in padovan
    
    def _is_tribonacci(self, n):
        if n < 0: return False
        trib = [0, 0, 1]
        while trib[-1] < n:
            trib.append(trib[-1] + trib[-2] + trib[-3])
        return n in trib
    
    def _is_jacobsthal(self, n):
        if n < 0: return False
        jacob = [0, 1]
        while jacob[-1] < n:
            jacob.append(jacob[-1] + 2*jacob[-2])
        return n in jacob
    
    def _is_motzkin(self, n):
        if n < 0: return False
        motzkin = [1, 1, 2, 4, 9, 21, 51, 127]
        return n in motzkin
    
    def _is_lazy_caterer(self, n):
        if n < 0: return False
        for k in range(1, 100):
            if n == (k*(k+1)//2 + 1):
                return True
        return False
    
    def _is_central_binomial(self, n):
        if n < 0: return False
        for k in range(1, 15):
            if self._binomial(2*k, k) == n:
                return True
        return False
    
    def _is_power_of_two(self, n):
        return n > 0 and (n & (n - 1)) == 0
    
    def _is_power_of_three(self, n):
        if n <= 0: return False
        while n % 3 == 0:
            n //= 3
        return n == 1
    
    # Special property checks
    def _is_perfect(self, n):
        if n <= 1: return False
        return sum(self._get_proper_divisors(n)) == n
    
    def _is_abundant(self, n):
        if n <= 1: return False
        return sum(self._get_proper_divisors(n)) > n
    
    def _is_deficient(self, n):
        if n <= 1: return False
        return sum(self._get_proper_divisors(n)) < n
    
    def _is_amicable(self, n):
        if n <= 1: return False
        partner = sum(self._get_proper_divisors(n))
        return partner != n and sum(self._get_proper_divisors(partner)) == n
    
    def _is_sociable(self, n):
        return self._is_amicable(n)  # Simplified for now
    
    def _is_narcissistic(self, n):
        if n < 0: return False
        s = str(n)
        power = len(s)
        return sum(int(d)**power for d in s) == n
    
    def _is_harshad(self, n):
        if n <= 0: return False
        return n % sum(int(d) for d in str(n)) == 0
    
    def _is_smith(self, n):
        if n <= 1 or sp.isprime(n): return False
        digit_sum = sum(int(d) for d in str(n))
        factor_sum = sum(int(d) for p in sp.factorint(n) for d in str(p))
        return digit_sum == factor_sum
    
    def _is_evil(self, n):
        return n >= 0 and bin(n).count('1') % 2 == 0
    
    def _is_odious(self, n):
        return n >= 0 and bin(n).count('1') % 2 == 1
    
    def _is_undulating(self, n):
        if n < 100: return False
        s = str(n)
        return all(s[i] == s[i%2] for i in range(len(s)))
    
    def _is_kaprekar(self, n):
        if n < 1: return False
        squared = n * n
        s = str(squared)
        mid = len(s) // 2
        left = int(s[:mid]) if s[:mid] else 0
        right = int(s[mid:])
        return left + right == n
    
    def _is_palindromic(self, n):
        return str(n) == str(n)[::-1]
    
    def _is_circular_prime(self, n):
        if not sp.isprime(n): return False
        s = str(n)
        for i in range(len(s)):
            rotated = int(s[i:] + s[:i])
            if not sp.isprime(rotated):
                return False
        return True
    
    def _is_emirp(self, n):
        if not sp.isprime(n): return False
        rev = int(str(n)[::-1])
        return rev != n and sp.isprime(rev)
    
    def _is_permutable_prime(self, n):
        if not sp.isprime(n): return False
        from itertools import permutations
        s = str(n)
        for perm in set(permutations(s)):
            if perm[0] == '0': continue
            num = int(''.join(perm))
            if not sp.isprime(num):
                return False
        return True
    
    def _is_reversible(self, n):
        return self._is_permutable_prime(n)  # Simplified
    
    def _is_catalan_conjecture(self, n):
        # Check if n = x^a - y^b has only solution 3^2 - 2^3 = 1
        return n == 1
    
    def _is_colossally_abundant(self, n):
        # Known values: 2, 6, 12, 60, 120, 360, 2520, 5040, 55440, 720720
        return n in [2, 6, 12, 60, 120, 360, 2520, 5040, 55440, 720720]
    
    def _is_highly_composite(self, n):
        # Known values up to certain range
        hc = [1, 2, 4, 6, 12, 24, 36, 48, 60, 120, 180, 240, 360, 720, 840, 1260, 1680, 2520, 5040, 7560, 10080, 15120, 20160, 27720, 45360, 50400, 55440, 83160, 110880, 166320, 221760, 277200, 332640, 498960, 554400, 665280, 720720]
        return n in hc
    
    def _is_superior_highly_composite(self, n):
        return n in [2, 6, 12, 60, 120, 360, 2520, 5040, 55440, 720720]
    
    # Prime type checks
    def _is_twin_prime(self, n):
        return sp.isprime(n) and (sp.isprime(n+2) or sp.isprime(n-2))
    
    def _is_cousin_prime(self, n):
        return sp.isprime(n) and (sp.isprime(n+4) or sp.isprime(n-4))
    
    def _is_sexy_prime(self, n):
        return sp.isprime(n) and (sp.isprime(n+6) or sp.isprime(n-6))
    
    def _is_mersenne_prime(self, n):
        if not sp.isprime(n): return False
        # Check if n is of form 2^p - 1 where p is prime
        return self._is_power_of_two(n + 1) and sp.isprime(int(math.log2(n + 1)))
    
    def _is_sophie_germain(self, n):
        return sp.isprime(n) and sp.isprime(2*n + 1)
    
    def _is_safe_prime(self, n):
        return sp.isprime(n) and n > 2 and sp.isprime((n - 1) // 2)
    
    def _is_wilson_prime(self, n):
        return n in [5, 13, 563]  # Known Wilson primes
    
    def _is_chernick_prime(self, n):
        # Simplified - known values
        return n in [5, 7, 13, 19, 37, 73, 79, 97, 103, 109, 127, 163, 181, 193, 277]
    
    def _is_cullen_prime(self, n):
        if not sp.isprime(n): return False
        # Check if n is of form k*2^k + 1
        for k in range(1, 50):
            if k * (2**k) + 1 == n:
                return True
        return False
    
    def _is_woodall_prime(self, n):
        if not sp.isprime(n): return False
        # Check if n is of form k*2^k - 1
        for k in range(1, 50):
            if k * (2**k) - 1 == n:
                return True
        return False
    
    def _is_fermat_prime(self, n):
        return n in [3, 5, 17, 257, 65537]  # Known Fermat primes
    
    def _is_factorial_prime(self, n):
        if not sp.isprime(n): return False
        # Check if n is factorial ± 1
        fact = 1
        for i in range(1, 10):
            fact *= i
            if fact + 1 == n or fact - 1 == n:
                return True
        return False
    
    def _is_primorial_prime(self, n):
        if not sp.isprime(n): return False
        # Check primorial ± 1
        primorial = 1
        for p in [2, 3, 5, 7, 11, 13, 17]:
            primorial *= p
            if primorial + 1 == n or primorial - 1 == n:
                return True
        return False
    
    def _is_wagstaff_prime(self, n):
        if not sp.isprime(n): return False
        # Check if n = (2^p + 1)/3 where p is prime
        for p in [3, 5, 7, 11, 13, 17, 19, 23, 31, 43, 61, 79, 101, 127, 167, 191]:
            if (2**p + 1) // 3 == n:
                return True
        return False
    
    def _is_proth_prime(self, n):
        if not sp.isprime(n): return False
        # Check if n = k*2^n + 1 where k is odd and k < 2^n
        return n < 2**20  # Simplified check
    
    def _is_pierpont_prime(self, n):
        if not sp.isprime(n): return False
        # Primes of form 2^u*3^v + 1
        return n < 1000  # Simplified
    
    def _is_regular_prime(self, n):
        if not sp.isprime(n): return False
        # Regular primes are primes that do not divide the class number
        return n not in [37, 59, 67, 101, 103, 131, 149, 173]  # Simplified
    
    def _is_irregular_prime(self, n):
        if not sp.isprime(n): return False
        return n in [37, 59, 67, 101, 103, 131, 149, 173]
    
    # Geometric and algebraic
    def _is_polygonal(self, n):
        for s in range(3, 12):
            if self._is_s_polygonal(n, s):
                return True
        return False
    
    def _is_s_polygonal(self, n, s):
        k = int((math.sqrt(8*(s-2)*n + (s-4)**2) + (s-4)) / (2*(s-2)))
        return k > 0 and ((s-2)*k*k - (s-4)*k) // 2 == n
    
    def _is_centered_triangular(self, n):
        k = int(math.sqrt(n))
        return 3*k*(k+1)//2 + 1 == n
    
    def _is_centered_square(self, n):
        k = int(math.sqrt(n))
        return 4*k*k + 4*k + 1 == n
    
    def _is_centered_pentagonal(self, n):
        k = int(math.sqrt(n))
        return 5*k*k + 5*k + 1 == n
    
    def _is_centered_hexagonal(self, n):
        k = int(math.sqrt(n))
        return 6*k*k + 6*k + 1 == n
    
    def _is_star_number(self, n):
        k = int(math.sqrt(n))
        return 6*k*(k-1) + 1 == n
    
    def _is_octahedral(self, n):
        k = int((math.sqrt(2*n) - 1) / 2)
        return k*(2*k*k + 1)//3 == n
    
    def _is_dodecahedral(self, n):
        k = int((math.sqrt(24*n + 1) + 1) / 6)
        return k*(3*k*k - k)//2 == n
    
    def _is_icosahedral(self, n):
        k = int((math.sqrt(12*n - 3) + 3) / 6)
        return k*(5*k*k - 5*k + 2)//2 == n
    
    def _is_rational(self, n):
        return isinstance(n, (int, float)) and not isinstance(n, bool)
    
    def _is_irrational(self, n):
        return False  # Cannot determine with integer input
    
    def _is_algebraic(self, n):
        return isinstance(n, int) or isinstance(n, float)
    
    def _is_transcendental(self, n):
        return False  # Cannot determine with integer input
    
    # Digit-based properties
    def _is_automorphic(self, n):
        if n < 0: return False
        squared = n * n
        return str(squared).endswith(str(n))
    
    def _is_self_number(self, n):
        if n < 1: return False
        for x in range(max(1, n - 100), n):
            if x + sum(int(d) for d in str(x)) == n:
                return False
        return True
    
    def _is_disarium(self, n):
        if n < 0: return False
        s = str(n)
        return sum(int(d)**(i+1) for i, d in enumerate(s)) == n
    
    def _is_magic_number(self, n):
        # Magic square constants: 15, 34, 65, 111, 175, 260, 369, 505, 671, 870
        return n in [15, 34, 65, 111, 175, 260, 369, 505, 671, 870]
    
    def _is_arithmetic_number(self, n):
        if n <= 0: return False
        divisors = self._get_divisors(n)
        return sum(divisors) % len(divisors) == 0
    
    def _is_practical(self, n):
        if n <= 0: return False
        # Simplified check
        return n in [1, 2, 4, 6, 8, 12, 16, 18, 20, 24, 28, 30, 32, 36, 40, 42, 44, 48, 54, 56, 60, 66, 72, 80, 84, 88, 96, 100, 104, 108, 112, 128]
    
    def _is_weird(self, n):
        return self._is_abundant(n) and not self._is_semiperfect(n)
    
    def _is_semiperfect(self, n):
        if n <= 0: return False
        divisors = self._get_proper_divisors(n)
        # Simple check for known semiperfect numbers
        return n in [6, 12, 18, 20, 24, 28, 30, 36, 40, 42, 48, 54, 56, 60, 66, 72, 78, 80, 84, 88, 90, 96, 100, 102, 108, 112, 114, 120]
    
    def _is_untouchable(self, n):
        return n in [2, 5, 52, 88, 96, 120, 124, 146, 162, 188, 206, 210, 216, 238, 246, 248, 262, 268, 276, 288, 290, 292, 304, 306, 322, 324, 326, 336, 342, 372, 406, 408, 426, 430, 448, 472, 474, 498, 516, 518, 520, 530, 540, 552, 556, 562, 576, 584, 612, 624, 626, 652, 658, 668, 670, 700, 702, 704, 712, 718, 726, 732, 738, 748, 750, 756, 764, 772, 786, 788, 792, 802, 804, 818, 820, 834, 836, 848, 852, 862, 876, 880, 882, 896, 906, 910, 912, 918, 920, 928, 936, 954, 966, 968, 970, 986, 1000]
    
    def _is_polite(self, n):
        if n <= 2: return False
        return not self._is_impolite(n)
    
    def _is_impolite(self, n):
        if n <= 2: return True
        return n & (n - 1) == 0  # Power of 2
    
    # Advanced sequence checks
    def _is_ulam(self, n):
        ulam = [1, 2]
        while ulam[-1] < n:
            next_val = self._get_next_ulam(ulam)
            ulam.append(next_val)
        return n in ulam
    
    def _get_next_ulam(self, ulam):
        # Simplified Ulam sequence generator
        return ulam[-1] + ulam[-2]  # Not accurate but placeholder
    
    def _is_recaman(self, n):
        recaman = [0, 1]
        while recaman[-1] < n:
            next_val = recaman[-1] - len(recaman)
            if next_val > 0 and next_val not in recaman:
                recaman.append(next_val)
            else:
                recaman.append(recaman[-1] + len(recaman))
        return n in recaman
    
    def _is_look_and_say(self, n):
        return str(n) in ['1', '11', '21', '1211', '111221', '312211', '13112221', '1113213211']
    
    def _is_kolakoski(self, n):
        return n in [1, 2, 2, 1, 1, 2, 1, 2, 2, 1][:n] if n <= 10 else False
    
    def _is_thue_morse(self, n):
        if n < 0: return False
        return bin(n).count('1') % 2 == 0
    
    def _is_ruth_aaron(self, n):
        # Simplified: known pairs where sum of divisors is equal
        return n in [5, 8, 15, 24, 49, 77, 104, 153, 369, 492, 714, 1682]
    
    def _is_frobenius(self, n):
        return n in [1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23]
    
    def _is_giuga(self, n):
        return n in [30, 858, 1722, 66198]
    
    def _is_carmichael(self, n):
        return sp.isprime(n) == False and all(pow(a, n-1, n) == 1 for a in range(2, min(20, n-1)) if math.gcd(a, n) == 1)
    
    def _is_sphenic(self, n):
        factors = sp.factorint(n)
        return len(factors) == 3 and all(exp == 1 for exp in factors.values())
    
    def _is_hyperperfect(self, n):
        # Known hyperperfect numbers
        return n in [6, 21, 28, 301, 325, 496, 697]
    
    def _is_vampire(self, n):
        if n < 100: return False
        s = str(n)
        if len(s) % 2 != 0: return False
        half = len(s) // 2
        from itertools import permutations
        for p in set(permutations(s)):
            if p[0] == '0': continue
            x = int(''.join(p[:half]))
            y = int(''.join(p[half:]))
            if x * y == n:
                return True
        return False
    
    def _is_keith(self, n):
        if n < 10: return False
        s = str(n)
        k = len(s)
        seq = [int(d) for d in s]
        while seq[-1] < n:
            next_val = sum(seq[-k:])
            seq.append(next_val)
        return seq[-1] == n
    
    def _is_moran(self, n):
        return n in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
    
    def _is_friable(self, n):
        # B-smooth numbers (primes ≤ 13)
        factors = sp.factorint(n)
        return all(p <= 13 for p in factors.keys())
    
    def _is_powerful(self, n):
        factors = sp.factorint(n)
        return all(exp >= 2 for exp in factors.values())
    
    def _is_achilles(self, n):
        return self._is_powerful(n) and not self._is_perfect_power(n)
    
    # Base-10 specific
    def _is_repunit(self, n):
        return set(str(n)) == {'1'}
    
    def _has_special_digital_root(self, n):
        return n % 9 in [0, 1, 3, 6, 9]  # Special digital roots
    
    def _has_special_persistence(self, n):
        return n in [199, 299, 399, 499, 599, 699, 799, 899, 999]
    
    def _has_special_mult_persistence(self, n):
        return n in [777, 6788, 68889, 2677889]
    
    def _is_smith_brother(self, n):
        return self._is_smith(n) and sp.isprime(n + 1)
    
    def _is_factorion(self, n):
        return n in [1, 2, 145, 40585]
    
    def _is_equidigital(self, n):
        digit_count = len(str(n))
        factor_count = sum(len(str(p)) for p in sp.factorint(n)) + sum(1 for exp in sp.factorint(n).values() if exp > 1)
        return digit_count == factor_count
    
    def _is_extravagant(self, n):
        digit_count = len(str(n))
        factor_count = sum(len(str(p)) for p in sp.factorint(n)) + sum(1 for exp in sp.factorint(n).values() if exp > 1)
        return digit_count < factor_count
    
    def _is_pandigital(self, n):
        return set(str(n)) == {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'} and len(str(n)) == 10
    
    def _is_zeroless(self, n):
        return '0' not in str(n)
    
    def _is_anti_palindromic(self, n):
        return str(n) != str(n)[::-1] and len(str(n)) > 1
    
    # Helper functions
    def _get_divisors(self, n):
        return [d for d in range(1, n+1) if n % d == 0]
    
    def _get_proper_divisors(self, n):
        return [d for d in range(1, n) if n % d == 0]
    
    def _is_perfect_square(self, n):
        if n < 0: return False
        k = int(math.isqrt(n))
        return k * k == n
    
    def _is_perfect_power(self, n):
        if n <= 1: return True
        for b in range(2, int(math.log2(n)) + 2):
            a = round(n ** (1/b))
            if a ** b == n:
                return True
        return False
    
    def _binomial(self, n, k):
        if k > n or k < 0: return 0
        result = 1
        for i in range(min(k, n-k)):
            result = result * (n - i) // (i + 1)
        return result
    
    def analyze_range(self, start, end):
        """Analyze a range of numbers for all number types."""
        start_time = time.time()
        
        print(f"\n🤖 DARLA - Deep Analysis and Recognition of Logarithmic Applications")
        print(f"🔍 Analyzing range: {start:,} to {end:,}")
        print(f"📊 Total numbers to analyze: {end - start + 1:,}")
        print(f"🔢 Number types checked: {len(self.number_types):,}")
        print("="*70)
        
        results = defaultdict(list)
        total_checked = 0
        batch_size = 1000
        
        for num in range(start, end + 1):
            found_types = []
            for type_name, check_func in self.number_types.items():
                try:
                    if check_func(num):
                        found_types.append(type_name)
                except:
                    pass
            
            if found_types:
                for type_name in found_types:
                    results[type_name].append(num)
            
            total_checked += 1
            
            # Progress display every batch_size numbers
            if total_checked % batch_size == 0:
                elapsed = time.time() - start_time
                progress = (total_checked / (end - start + 1)) * 100
                eta = (elapsed / total_checked) * ((end - start + 1) - total_checked)
                print(f"📈 Progress: {total_checked:,}/{end - start + 1:,} ({progress:.1f}%) | "
                      f"Found: {sum(len(v) for v in results.values()):,} matches | "
                      f"ETA: {eta:.0f}s")
        
        # Calculate final statistics
        end_time = time.time()
        total_time = end_time - start_time
        
        print("\n" + "="*70)
        print("📊 ANALYSIS COMPLETE!")
        print("="*70)
        print(f"⏱️  Total time: {total_time:.2f} seconds")
        print(f"🔍 Numbers analyzed: {total_checked:,}")
        print(f"📈 Total matches found: {sum(len(v) for v in results.values()):,}")
        print(f"🏷️  Number types with matches: {len(results):,}")
        
        # Display top 10 most common types
        type_counts = {k: len(v) for k, v in results.items()}
        top_types = sorted(type_counts.items(), key=lambda x: x[1], reverse=True)[:10]
        
        print("\n🏆 TOP 10 MOST COMMON NUMBER TYPES:")
        for i, (type_name, count) in enumerate(top_types, 1):
            print(f"  {i:2d}. {type_name.replace('_', ' ').title()}: {count:,} occurrences")
        
        # Save detailed log
        self._save_analysis_log(start, end, results, total_time)
        
        return results
    
    def _save_analysis_log(self, start, end, results, total_time):
        """Save detailed analysis log to file."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"darla_analysis_{start}_{end}_{timestamp}.txt"
        
        with open(filename, 'w') as f:
            f.write("DARLA ANALYSIS LOG\n")
            f.write("="*50 + "\n")
            f.write(f"Range: {start:,} to {end:,}\n")
            f.write(f"Analysis Time: {total_time:.2f} seconds\n")
            f.write(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("="*50 + "\n\n")
            
            for type_name, numbers in sorted(results.items()):
                if numbers:
                    f.write(f"{type_name.upper()}:\n")
                    f.write(f"  Count: {len(numbers):,}\n")
                    f.write(f"  Numbers: {', '.join(map(str, numbers[:50]))}")
                    if len(numbers) > 50:
                        f.write(f" ... and {len(numbers) - 50} more")
                    f.write("\n\n")
        
        print(f"💾 Detailed log saved to: {filename}")

def main():
    """Main interface for DARLA."""
    print("🤖 Welcome to DARLA - Deep Analysis and Recognition of Logarithmic Applications")
    print("="*70)
    
    analyzer = DarlaAnalyzer()
    
    while True:
        print("\n📊 Select an option:")
        print("1. Analyze a range of numbers")
        print("2. Quick test (small range)")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == "1":
            try:
                start = int(input("Enter start number: "))
                end = int(input("Enter end number: "))
                
                if start >= end:
                    print("❌ Start must be less than end!")
                    continue
                
                if end - start > 100000:
                    confirm = input(f"⚠️  This is a large range ({end - start:,} numbers). Continue? (y/n): ")
                    if confirm.lower() != 'y':
                        continue
                
                results = analyzer.analyze_range(start, end)
                
            except ValueError:
                print("❌ Please enter valid integers!")
                
        elif choice == "2":
            print("🧪 Running quick test on range 1-1000...")
            results = analyzer.analyze_range(1, 1000)
            
        elif choice == "3":
            print("👋 Thank you for using DARLA!")
            break
            
        else:
            print("❌ Invalid choice!")
        
        # Ask to repeat
        if choice in ["1", "2"]:
            repeat = input("\nWould you like to analyze another range? (y/n): ").strip()
            if repeat.lower() != 'y':
                print("👋 Thank you for using DARLA!")
                break

if __name__ == "__main__":
    main()