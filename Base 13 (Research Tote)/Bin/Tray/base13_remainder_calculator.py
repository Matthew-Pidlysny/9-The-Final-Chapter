#!/usr/bin/env python3
"""
Base-13 Remainder System Calculator
Implements the formal remainder-based counting system with +3 phenomenon
"""

import math
from typing import Dict, List, Tuple, Optional
import json

class Base13RemainderSystem:
    """
    Implements the Base-13 Remainder System with +3 Phenomenon
    
    Key concepts:
    - Remainder triggers at: 11,12,13, 24,25,26, 37,38,39, etc.
    - Pattern: numbers in form {13k-2, 13k-1, 13k} for k >= 1
    - 9 groups per cycle (27 remainder increments)
    - 19 cycles for complete system
    """
    
    def __init__(self, alpha: float = 17/27):
        """
        Initialize the system
        
        Args:
            alpha: Compression factor for remainder adjustment
        """
        self.alpha = alpha
        self.cache = {}
        
    def is_remainder_trigger(self, n: int) -> bool:
        """
        Check if n triggers remainder counting
        
        A number triggers if it's in the pattern:
        11,12,13, 24,25,26, 37,38,39, ...
        
        Formula: 13k-2, 13k-1, or 13k for k >= 1
        """
        if n < 11:
            return False
        
        # Check if n is in form 13k-2, 13k-1, or 13k
        for offset in [2, 1, 0]:
            if (n + offset) % 13 == 0:
                k = (n + offset) // 13
                if k >= 1:
                    return True
        return False
    
    def get_remainder_group(self, n: int) -> Optional[int]:
        """
        Get which remainder group (1-171) this number belongs to
        Returns None if not a remainder trigger
        """
        if not self.is_remainder_trigger(n):
            return None
        
        # Find k where n is in {13k-2, 13k-1, 13k}
        for offset in [2, 1, 0]:
            if (n + offset) % 13 == 0:
                k = (n + offset) // 13
                return k
        return None
    
    def count_remainders(self, n: int) -> int:
        """
        Count total remainder triggers from 1 to n (inclusive)
        Uses optimized formula for efficiency
        """
        if n < 11:
            return 0
        
        # Use cache if available
        if n in self.cache:
            return self.cache[n]
        
        # Calculate number of complete groups
        # First group starts at 11 (k=1)
        # Each group spans 13 numbers
        
        if n < 11:
            count = 0
        elif n <= 13:
            # First group: 11, 12, 13
            count = min(3, n - 10)
        else:
            # Find which group we're in
            # Group k contains: 13k-2, 13k-1, 13k
            # So 13k-2 <= n means k <= (n+2)/13
            
            max_k = (n + 2) // 13
            
            # Count complete groups (each contributes 3)
            count = max_k * 3
            
            # Adjust for partial last group
            last_group_start = 13 * max_k - 2
            if n < last_group_start:
                # We overcounted, remove the incomplete group
                count -= 3
                # Add back what we actually have
                prev_k = max_k - 1
                if prev_k >= 1:
                    prev_group_start = 13 * prev_k - 2
                    if n >= prev_group_start:
                        count += min(3, n - prev_group_start + 1)
            else:
                # Adjust for partial last group
                count -= 3
                count += min(3, n - last_group_start + 1)
        
        self.cache[n] = count
        return count
    
    def effective_value(self, n: int) -> float:
        """
        Calculate effective value with remainder compression
        
        E(n) = n - alpha * R(n)
        
        where R(n) is the remainder count
        """
        R_n = self.count_remainders(n)
        return n - self.alpha * R_n
    
    def find_effective_target(self, target: float, 
                            max_search: int = 1000000,
                            tolerance: float = 0.1) -> Optional[Dict]:
        """
        Find n where E(n) ≈ target
        
        Uses binary search for efficiency
        """
        # Binary search approach
        left, right = 1, max_search
        best_n = None
        best_error = float('inf')
        
        while left <= right:
            mid = (left + right) // 2
            E_mid = self.effective_value(mid)
            error = abs(E_mid - target)
            
            if error < best_error:
                best_error = error
                best_n = mid
            
            if error < tolerance:
                return self._create_result_dict(best_n, target)
            
            if E_mid < target:
                left = mid + 1
            else:
                right = mid - 1
        
        if best_n is not None:
            return self._create_result_dict(best_n, target)
        
        return None
    
    def _create_result_dict(self, n: int, target: float) -> Dict:
        """Create result dictionary with all relevant information"""
        R_n = self.count_remainders(n)
        E_n = self.effective_value(n)
        
        return {
            'n': n,
            'target': target,
            'effective_value': E_n,
            'error': abs(E_n - target),
            'remainder_count': R_n,
            'base13_representation': self.to_base13(n),
            'compression_factor': R_n / n if n > 0 else 0,
            'cycle_number': (R_n // 27) + 1 if R_n > 0 else 0,
            'group_in_cycle': ((R_n % 27) // 3) + 1 if R_n > 0 else 0,
            'is_remainder_trigger': self.is_remainder_trigger(n)
        }
    
    def to_base13(self, n: int) -> str:
        """Convert decimal number to base-13 representation"""
        if n == 0:
            return "0"
        
        digits = "0123456789ABC"
        result = []
        
        while n > 0:
            result.append(digits[n % 13])
            n //= 13
        
        return ''.join(reversed(result))
    
    def from_base13(self, s: str) -> int:
        """Convert base-13 string to decimal"""
        digits = "0123456789ABC"
        result = 0
        
        for char in s.upper():
            result = result * 13 + digits.index(char)
        
        return result
    
    def analyze_range(self, start: int, end: int) -> Dict:
        """
        Analyze remainder patterns in a range
        """
        triggers = []
        groups = {}
        
        for n in range(start, end + 1):
            if self.is_remainder_trigger(n):
                triggers.append(n)
                group = self.get_remainder_group(n)
                if group not in groups:
                    groups[group] = []
                groups[group].append(n)
        
        return {
            'range': (start, end),
            'trigger_count': len(triggers),
            'triggers': triggers,
            'groups': groups,
            'group_count': len(groups)
        }
    
    def generate_scaling_table(self, powers: List[int] = None) -> Dict:
        """
        Generate table showing base-13 remainder equivalents for powers of 10
        """
        if powers is None:
            powers = [-1, 0, 1, 2, 3, 4]
        
        results = {}
        
        for power in powers:
            target = 10 ** power
            result = self.find_effective_target(target, max_search=10000000)
            
            if result:
                results[f"10^{power}"] = result
            else:
                results[f"10^{power}"] = {"error": "Not found"}
        
        return results
    
    def verify_key_values(self) -> Dict:
        """
        Verify key theoretical values
        """
        verifications = {}
        
        # Test E(117) = 100
        result_100 = self._create_result_dict(117, 100)
        verifications['E(117)_should_be_100'] = result_100
        
        # Test first cycle completion (9 groups = 27 remainders)
        # Last number of first cycle: group 9, which is 13*9-2 to 13*9
        # That's 115, 116, 117
        verifications['first_cycle_end'] = {
            'last_group': 9,
            'numbers': [115, 116, 117],
            'remainder_count': self.count_remainders(117),
            'expected_remainder_count': 27
        }
        
        # Test 19 cycles completion
        # Group 171 (19 * 9 = 171)
        last_group_num = 13 * 171
        verifications['nineteen_cycles_end'] = {
            'last_group': 171,
            'last_number': last_group_num,
            'remainder_count': self.count_remainders(last_group_num),
            'expected_remainder_count': 19 * 27
        }
        
        return verifications


def main():
    """Main execution function"""
    print("=" * 80)
    print("BASE-13 REMAINDER SYSTEM CALCULATOR")
    print("Implementing the +3 Phenomenon Integration")
    print("=" * 80)
    print()
    
    # Initialize system
    system = Base13RemainderSystem()
    
    # 1. Verify key theoretical values
    print("1. VERIFYING KEY THEORETICAL VALUES")
    print("-" * 80)
    verifications = system.verify_key_values()
    
    print("\n✓ Testing E(117) = 100:")
    result_100 = verifications['E(117)_should_be_100']
    print(f"  n = {result_100['n']}")
    print(f"  Effective Value = {result_100['effective_value']:.4f}")
    print(f"  Target = {result_100['target']}")
    print(f"  Error = {result_100['error']:.4f}")
    print(f"  Remainder Count = {result_100['remainder_count']}")
    print(f"  Base-13 = {result_100['base13_representation']}")
    
    print("\n✓ First Cycle Completion (9 groups):")
    first_cycle = verifications['first_cycle_end']
    print(f"  Last group: {first_cycle['last_group']}")
    print(f"  Numbers: {first_cycle['numbers']}")
    print(f"  Remainder count: {first_cycle['remainder_count']}")
    print(f"  Expected: {first_cycle['expected_remainder_count']}")
    print(f"  Match: {first_cycle['remainder_count'] == first_cycle['expected_remainder_count']}")
    
    print("\n✓ 19 Cycles Completion (171 groups):")
    nineteen = verifications['nineteen_cycles_end']
    print(f"  Last group: {nineteen['last_group']}")
    print(f"  Last number: {nineteen['last_number']}")
    print(f"  Remainder count: {nineteen['remainder_count']}")
    print(f"  Expected: {nineteen['expected_remainder_count']}")
    print(f"  Match: {nineteen['remainder_count'] == nineteen['expected_remainder_count']}")
    
    # 2. Analyze first few groups
    print("\n\n2. ANALYZING FIRST 9 GROUPS (First Cycle)")
    print("-" * 80)
    analysis = system.analyze_range(1, 120)
    
    for group_num in sorted(analysis['groups'].keys())[:9]:
        numbers = analysis['groups'][group_num]
        print(f"Group {group_num}: {numbers}")
    
    # 3. Generate scaling table
    print("\n\n3. SCALING TABLE: Powers of 10")
    print("-" * 80)
    print(f"{'Power':<10} {'Target':<15} {'n':<10} {'E(n)':<15} {'R(n)':<10} {'Base-13':<15}")
    print("-" * 80)
    
    scaling = system.generate_scaling_table(powers=[-1, 0, 1, 2, 3, 4])
    
    for power_str, result in sorted(scaling.items()):
        if 'error' not in result:
            power = int(power_str.split('^')[1])
            target = 10 ** power
            print(f"{power_str:<10} {target:<15.4f} {result['n']:<10} "
                  f"{result['effective_value']:<15.4f} {result['remainder_count']:<10} "
                  f"{result['base13_representation']:<15}")
    
    # 4. Deep analysis for large numbers
    print("\n\n4. DEEP ANALYSIS: Finding E(n) = 1000")
    print("-" * 80)
    result_1000 = system.find_effective_target(1000, max_search=10000000)
    
    if result_1000:
        print(f"  n = {result_1000['n']}")
        print(f"  Effective Value = {result_1000['effective_value']:.4f}")
        print(f"  Error = {result_1000['error']:.4f}")
        print(f"  Remainder Count = {result_1000['remainder_count']}")
        print(f"  Base-13 = {result_1000['base13_representation']}")
        print(f"  Compression Factor = {result_1000['compression_factor']:.6f}")
        print(f"  Cycle Number = {result_1000['cycle_number']}")
        print(f"  Group in Cycle = {result_1000['group_in_cycle']}")
    
    # 5. Pattern analysis
    print("\n\n5. PATTERN ANALYSIS: Compression Factor Evolution")
    print("-" * 80)
    print(f"{'n':<10} {'E(n)':<15} {'R(n)':<10} {'Compression':<15}")
    print("-" * 80)
    
    test_points = [13, 39, 117, 351, 1000, 2223, 5000, 10000]
    for n in test_points:
        E_n = system.effective_value(n)
        R_n = system.count_remainders(n)
        compression = R_n / n if n > 0 else 0
        print(f"{n:<10} {E_n:<15.4f} {R_n:<10} {compression:<15.6f}")
    
    # 6. Save results to JSON
    print("\n\n6. SAVING RESULTS")
    print("-" * 80)
    
    output_data = {
        'verifications': verifications,
        'scaling_table': scaling,
        'pattern_analysis': {
            str(n): {
                'effective_value': system.effective_value(n),
                'remainder_count': system.count_remainders(n),
                'compression': system.count_remainders(n) / n if n > 0 else 0
            }
            for n in test_points
        }
    }
    
    with open('base13_remainder_results.json', 'w') as f:
        json.dump(output_data, f, indent=2)
    
    print("✓ Results saved to: base13_remainder_results.json")
    
    print("\n" + "=" * 80)
    print("ANALYSIS COMPLETE")
    print("=" * 80)


if __name__ == "__main__":
    main()