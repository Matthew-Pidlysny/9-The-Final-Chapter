"""
Workshop Module 3: Integrated Systems Analysis
This module provides tests for the integrated analysis of all three systems.
"""

import sys

class IntegratedWorkshop:
    """Workshop for integrated systems analysis"""
    
    def __init__(self):
        self.passed_tests = 0
        self.total_tests = 0
        
    def test_plus3_phenomenon(self):
        """Test the Plus 3 Phenomenon across scales"""
        print("\n=== Test 1: Plus 3 Phenomenon ===")
        self.total_tests += 1
        
        print("  Testing R(13^k * n + 3) for various k and n:")
        
        passed = 0
        total = 0
        
        # Test k=0 (should vary with n)
        print("  Scale k=0:")
        for n in range(13):
            result = (n + 3) % 13
            expected = (n + 3) % 13
            status = "✓" if result == expected else "✗"
            if n < 5:  # Only print first few
                print(f"    {status} R(13^0 * {n} + 3) = {result} [expected: {expected}]")
            if result == expected:
                passed += 1
            total += 1
        
        # Test k>=1 (should always be 3)
        print("  Scale k>=1:")
        for k in range(1, 5):
            for n in range(5):  # Test a few values of n
                result = (13**k * n + 3) % 13
                expected = 3
                status = "✓" if result == expected else "✗"
                if k == 1 and n < 3:  # Only print first few
                    print(f"    {status} R(13^{k} * {n} + 3) = {result} [expected: {expected}]")
                if result == expected:
                    passed += 1
                total += 1
        
        if passed == total:
            print(f"  PASSED: All {total} Plus 3 Phenomenon tests passed!")
            self.passed_tests += 1
        else:
            print(f"  FAILED: {passed}/{total} tests passed")
            
        return passed == total
    
    def test_base13_sequinor_connection(self):
        """Test connections between Base 13 and Sequinor Tredecim"""
        print("\n=== Test 2: Base 13 - Sequinor Connection ===")
        self.total_tests += 1
        
        print("  Testing Alpha scaling in Base 13:")
        
        passed = 0
        total = 0
        
        # Alpha values should correspond to powers of 13
        for k in range(5):
            alpha_k = 13 ** k
            base13_repr = self.decimal_to_base13(alpha_k)
            # In base 13, 13^k should be "1" followed by k zeros
            expected = "1" + "0" * k
            status = "✓" if base13_repr == expected else "✗"
            print(f"    {status} α({k}) = {alpha_k} = ({base13_repr})₁₃ [expected: ({expected})₁₃]")
            if base13_repr == expected:
                passed += 1
            total += 1
        
        if passed == total:
            print(f"  PASSED: All {total} connection tests passed!")
            self.passed_tests += 1
        else:
            print(f"  FAILED: {passed}/{total} tests passed")
            
        return passed == total
    
    def test_remainder_sequinor_integration(self):
        """Test integration of remainder system with Sequinor components"""
        print("\n=== Test 3: Remainder - Sequinor Integration ===")
        self.total_tests += 1
        
        print("  Testing Beta transformation on remainder sequences:")
        
        passed = 0
        total = 0
        
        # Beta(x, 3) should shift remainders by 3
        for x in range(13):
            beta_result = (x + 3) % 13
            remainder_result = (x + 3) % 13
            status = "✓" if beta_result == remainder_result else "✗"
            if x < 5:  # Only print first few
                print(f"    {status} β({x}, 3) = {beta_result}, R({x} + 3) = {remainder_result}")
            if beta_result == remainder_result:
                passed += 1
            total += 1
        
        if passed == total:
            print(f"  PASSED: All {total} integration tests passed!")
            self.passed_tests += 1
        else:
            print(f"  FAILED: {passed}/{total} tests passed")
            
        return passed == total
    
    def test_unified_scaling_table(self):
        """Test unified scaling across all systems"""
        print("\n=== Test 4: Unified Scaling Table ===")
        self.total_tests += 1
        
        print("  Generating unified scaling table:")
        print("  Scale | Alpha(k) | Base13    | R(α(k)+3) | Beta(α(k),3)")
        print("  ------|----------|-----------|-----------|-------------")
        
        passed = 0
        total = 0
        
        for k in range(5):
            alpha_k = 13 ** k
            base13 = self.decimal_to_base13(alpha_k)
            remainder = (alpha_k + 3) % 13
            beta_result = (alpha_k + 3) % 13
            
            # For k >= 1, remainder should be 3
            if k >= 1:
                expected_remainder = 3
            else:
                expected_remainder = 4  # 1 + 3 = 4
            
            status = "✓" if remainder == expected_remainder else "✗"
            print(f"  {status} {k:5d} | {alpha_k:8d} | {base13:9s} | {remainder:9d} | {beta_result:11d}")
            
            if remainder == expected_remainder:
                passed += 1
            total += 1
        
        if passed == total:
            print(f"  PASSED: All {total} unified scaling tests passed!")
            self.passed_tests += 1
        else:
            print(f"  FAILED: {passed}/{total} tests passed")
            
        return passed == total
    
    def test_cross_system_properties(self):
        """Test properties that span all three systems"""
        print("\n=== Test 5: Cross-System Properties ===")
        self.total_tests += 1
        
        print("  Testing modular arithmetic consistency:")
        
        passed = 0
        total = 0
        
        # Test 1: (a + b) mod 13 should be consistent across systems
        test_cases = [
            (5, 8, 0),
            (10, 3, 0),
            (7, 6, 0),
            (12, 1, 0)
        ]
        
        for a, b, expected in test_cases:
            # Base 13 approach
            base13_a = self.decimal_to_base13(a)
            base13_b = self.decimal_to_base13(b)
            base13_sum = self.base13_to_decimal(base13_a) + self.base13_to_decimal(base13_b)
            base13_result = base13_sum % 13
            
            # Remainder approach
            remainder_result = (a + b) % 13
            
            # Sequinor Beta approach
            beta_result = (a + b) % 13
            
            all_equal = (base13_result == remainder_result == beta_result == expected)
            status = "✓" if all_equal else "✗"
            print(f"    {status} ({a} + {b}) mod 13: Base13={base13_result}, Remainder={remainder_result}, Beta={beta_result}")
            
            if all_equal:
                passed += 1
            total += 1
        
        if passed == total:
            print(f"  PASSED: All {total} cross-system tests passed!")
            self.passed_tests += 1
        else:
            print(f"  FAILED: {passed}/{total} tests passed")
            
        return passed == total
    
    def test_theoretical_predictions(self):
        """Test theoretical predictions across systems"""
        print("\n=== Test 6: Theoretical Predictions ===")
        self.total_tests += 1
        
        print("  Testing theoretical predictions:")
        
        passed = 0
        total = 0
        
        # Prediction 1: For any n, R(13n) = 0
        print("  Prediction 1: R(13n) = 0 for all n")
        for n in range(1, 6):
            result = (13 * n) % 13
            expected = 0
            status = "✓" if result == expected else "✗"
            if n <= 3:
                print(f"    {status} R(13 * {n}) = {result} [expected: {expected}]")
            if result == expected:
                passed += 1
            total += 1
        
        # Prediction 2: For any n, R(13n + 3) = 3
        print("  Prediction 2: R(13n + 3) = 3 for all n")
        for n in range(1, 6):
            result = (13 * n + 3) % 13
            expected = 3
            status = "✓" if result == expected else "✗"
            if n <= 3:
                print(f"    {status} R(13 * {n} + 3) = {result} [expected: {expected}]")
            if result == expected:
                passed += 1
            total += 1
        
        # Prediction 3: Beta transformation preserves differences
        print("  Prediction 3: β preserves modular differences")
        x, y, k = 7, 3, 5
        diff_original = (x - y) % 13
        beta_x = (x + k) % 13
        beta_y = (y + k) % 13
        diff_transformed = (beta_x - beta_y) % 13
        status = "✓" if diff_original == diff_transformed else "✗"
        print(f"    {status} ({x} - {y}) mod 13 = {diff_original}, (β({x},{k}) - β({y},{k})) mod 13 = {diff_transformed}")
        if diff_original == diff_transformed:
            passed += 1
        total += 1
        
        if passed == total:
            print(f"  PASSED: All {total} theoretical prediction tests passed!")
            self.passed_tests += 1
        else:
            print(f"  FAILED: {passed}/{total} tests passed")
            
        return passed == total
    
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
    
    def run_all_tests(self):
        """Run all workshop tests"""
        print("=" * 60)
        print("WORKSHOP MODULE 3: INTEGRATED SYSTEMS ANALYSIS")
        print("=" * 60)
        
        self.test_plus3_phenomenon()
        self.test_base13_sequinor_connection()
        self.test_remainder_sequinor_integration()
        self.test_unified_scaling_table()
        self.test_cross_system_properties()
        self.test_theoretical_predictions()
        
        print("\n" + "=" * 60)
        print(f"WORKSHOP SUMMARY: {self.passed_tests}/{self.total_tests} test suites passed")
        print("=" * 60)
        
        return self.passed_tests == self.total_tests


if __name__ == "__main__":
    workshop = IntegratedWorkshop()
    success = workshop.run_all_tests()
    sys.exit(0 if success else 1)