"""
Workshop Module 1: Base 13 Fundamentals
This module provides interactive exercises and tests for exploring Base 13 mathematics.
"""

import sys

class Base13Workshop:
    """Workshop for Base 13 fundamentals"""
    
    def __init__(self):
        self.passed_tests = 0
        self.total_tests = 0
        
    def test_conversion_decimal_to_base13(self):
        """Test conversion from decimal to Base 13"""
        print("\n=== Test 1: Decimal to Base 13 Conversion ===")
        self.total_tests += 1
        
        test_cases = [
            (0, "0"),
            (13, "10"),
            (26, "20"),
            (169, "100"),
            (247, "160"),
            (1000, "5BA")
        ]
        
        passed = 0
        for decimal, expected_base13 in test_cases:
            result = self.decimal_to_base13(decimal)
            status = "✓" if result == expected_base13 else "✗"
            print(f"  {status} {decimal} (decimal) = {result} (base 13) [expected: {expected_base13}]")
            if result == expected_base13:
                passed += 1
        
        if passed == len(test_cases):
            print(f"  PASSED: All {len(test_cases)} conversion tests passed!")
            self.passed_tests += 1
        else:
            print(f"  FAILED: {passed}/{len(test_cases)} tests passed")
            
        return passed == len(test_cases)
    
    def test_conversion_base13_to_decimal(self):
        """Test conversion from Base 13 to decimal"""
        print("\n=== Test 2: Base 13 to Decimal Conversion ===")
        self.total_tests += 1
        
        test_cases = [
            ("0", 0),
            ("10", 13),
            ("20", 26),
            ("100", 169),
            ("160", 247),
            ("5BA", 1000),
            ("A", 10),
            ("B", 11),
            ("C", 12)
        ]
        
        passed = 0
        for base13, expected_decimal in test_cases:
            result = self.base13_to_decimal(base13)
            status = "✓" if result == expected_decimal else "✗"
            print(f"  {status} {base13} (base 13) = {result} (decimal) [expected: {expected_decimal}]")
            if result == expected_decimal:
                passed += 1
        
        if passed == len(test_cases):
            print(f"  PASSED: All {len(test_cases)} conversion tests passed!")
            self.passed_tests += 1
        else:
            print(f"  FAILED: {passed}/{len(test_cases)} tests passed")
            
        return passed == len(test_cases)
    
    def test_base13_addition(self):
        """Test addition in Base 13"""
        print("\n=== Test 3: Base 13 Addition ===")
        self.total_tests += 1
        
        test_cases = [
            ("5", "8", "10"),
            ("A", "3", "10"),
            ("C", "1", "10"),
            ("A7C", "5B8", "1034"),
            ("1", "C", "10")
        ]
        
        passed = 0
        for a, b, expected in test_cases:
            result = self.add_base13(a, b)
            status = "✓" if result == expected else "✗"
            print(f"  {status} {a} + {b} = {result} [expected: {expected}]")
            if result == expected:
                passed += 1
        
        if passed == len(test_cases):
            print(f"  PASSED: All {len(test_cases)} addition tests passed!")
            self.passed_tests += 1
        else:
            print(f"  FAILED: {passed}/{len(test_cases)} tests passed")
            
        return passed == len(test_cases)
    
    def test_divisibility_rules(self):
        """Test divisibility rules in Base 13"""
        print("\n=== Test 4: Divisibility Rules ===")
        self.total_tests += 1
        
        # Test divisibility by 2
        print("  Testing divisibility by 2:")
        test_cases_2 = [
            (26, True),   # ends in 0 (even)
            (27, False),  # ends in 1 (odd)
            (40, True),   # ends in 4 (even)
            (41, False)   # ends in 5 (odd)
        ]
        
        passed_2 = 0
        for num, expected in test_cases_2:
            result = self.is_divisible_by_2(num)
            status = "✓" if result == expected else "✗"
            base13 = self.decimal_to_base13(num)
            print(f"    {status} {num} ({base13} in base 13) divisible by 2: {result} [expected: {expected}]")
            if result == expected:
                passed_2 += 1
        
        # Test divisibility by 3
        print("  Testing divisibility by 3:")
        test_cases_3 = [
            (39, True),   # 3*13 = 39
            (40, False),
            (27, True),   # 27 = 3*9
            (28, False)
        ]
        
        passed_3 = 0
        for num, expected in test_cases_3:
            result = self.is_divisible_by_3(num)
            status = "✓" if result == expected else "✗"
            base13 = self.decimal_to_base13(num)
            print(f"    {status} {num} ({base13} in base 13) divisible by 3: {result} [expected: {expected}]")
            if result == expected:
                passed_3 += 1
        
        # Test divisibility by 13
        print("  Testing divisibility by 13:")
        test_cases_13 = [
            (13, True),
            (26, True),
            (27, False),
            (169, True)
        ]
        
        passed_13 = 0
        for num, expected in test_cases_13:
            result = self.is_divisible_by_13(num)
            status = "✓" if result == expected else "✗"
            base13 = self.decimal_to_base13(num)
            print(f"    {status} {num} ({base13} in base 13) divisible by 13: {result} [expected: {expected}]")
            if result == expected:
                passed_13 += 1
        
        total_passed = passed_2 + passed_3 + passed_13
        total_cases = len(test_cases_2) + len(test_cases_3) + len(test_cases_13)
        
        if total_passed == total_cases:
            print(f"  PASSED: All {total_cases} divisibility tests passed!")
            self.passed_tests += 1
        else:
            print(f"  FAILED: {total_passed}/{total_cases} tests passed")
            
        return total_passed == total_cases
    
    def test_modular_arithmetic(self):
        """Test modular arithmetic in Base 13"""
        print("\n=== Test 5: Modular Arithmetic (mod 13) ===")
        self.total_tests += 1
        
        test_cases = [
            (15, 2),
            (26, 0),
            (27, 1),
            (100, 9),
            (169, 0),
            (247, 0)
        ]
        
        passed = 0
        for num, expected_remainder in test_cases:
            result = num % 13
            status = "✓" if result == expected_remainder else "✗"
            print(f"  {status} {num} mod 13 = {result} [expected: {expected_remainder}]")
            if result == expected_remainder:
                passed += 1
        
        if passed == len(test_cases):
            print(f"  PASSED: All {len(test_cases)} modular arithmetic tests passed!")
            self.passed_tests += 1
        else:
            print(f"  FAILED: {passed}/{len(test_cases)} tests passed")
            
        return passed == len(test_cases)
    
    # Helper methods
    def decimal_to_base13(self, n):
        """Convert decimal to Base 13"""
        if n == 0:
            return "0"
        
        digits = "0123456789ABC"
        result = ""
        
        while n > 0:
            result = digits[n % 13] + result
            n //= 13
        
        return result
    
    def base13_to_decimal(self, s):
        """Convert Base 13 to decimal"""
        digits = "0123456789ABC"
        result = 0
        
        for char in s:
            result = result * 13 + digits.index(char)
        
        return result
    
    def add_base13(self, a, b):
        """Add two Base 13 numbers"""
        dec_a = self.base13_to_decimal(a)
        dec_b = self.base13_to_decimal(b)
        return self.decimal_to_base13(dec_a + dec_b)
    
    def is_divisible_by_2(self, n):
        """Check if number is divisible by 2 using Base 13 rule"""
        base13 = self.decimal_to_base13(n)
        last_digit = base13[-1]
        even_digits = "0246A8C"
        return last_digit in even_digits
    
    def is_divisible_by_3(self, n):
        """Check if number is divisible by 3 using Base 13 rule"""
        base13 = self.decimal_to_base13(n)
        digit_sum = sum(self.base13_to_decimal(d) for d in base13)
        return digit_sum % 3 == 0
    
    def is_divisible_by_13(self, n):
        """Check if number is divisible by 13 using Base 13 rule"""
        base13 = self.decimal_to_base13(n)
        return base13[-1] == "0"
    
    def run_all_tests(self):
        """Run all workshop tests"""
        print("=" * 60)
        print("WORKSHOP MODULE 1: BASE 13 FUNDAMENTALS")
        print("=" * 60)
        
        self.test_conversion_decimal_to_base13()
        self.test_conversion_base13_to_decimal()
        self.test_base13_addition()
        self.test_divisibility_rules()
        self.test_modular_arithmetic()
        
        print("\n" + "=" * 60)
        print(f"WORKSHOP SUMMARY: {self.passed_tests}/{self.total_tests} test suites passed")
        print("=" * 60)
        
        return self.passed_tests == self.total_tests


if __name__ == "__main__":
    workshop = Base13Workshop()
    success = workshop.run_all_tests()
    sys.exit(0 if success else 1)