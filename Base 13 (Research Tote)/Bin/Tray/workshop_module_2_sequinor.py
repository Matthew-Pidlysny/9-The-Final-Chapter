"""
Workshop Module 2: Sequinor Tredecim Exploration
This module provides interactive exercises and tests for exploring the Sequinor Tredecim system.
"""

import sys
import math

class SequinorWorkshop:
    """Workshop for Sequinor Tredecim system"""
    
    def __init__(self):
        self.passed_tests = 0
        self.total_tests = 0
        
    def test_alpha_component(self):
        """Test Alpha component (foundational scaling)"""
        print("\n=== Test 1: Alpha Component (Scaling) ===")
        self.total_tests += 1
        
        test_cases = [
            (0, 1),
            (1, 13),
            (2, 169),
            (3, 2197),
            (4, 28561)
        ]
        
        passed = 0
        for n, expected in test_cases:
            result = self.alpha(n)
            status = "✓" if result == expected else "✗"
            print(f"  {status} α({n}) = {result} [expected: {expected}]")
            if result == expected:
                passed += 1
        
        if passed == len(test_cases):
            print(f"  PASSED: All {len(test_cases)} Alpha tests passed!")
            self.passed_tests += 1
        else:
            print(f"  FAILED: {passed}/{len(test_cases)} tests passed")
            
        return passed == len(test_cases)
    
    def test_beta_component(self):
        """Test Beta component (transformation rules)"""
        print("\n=== Test 2: Beta Component (Transformations) ===")
        self.total_tests += 1
        
        test_cases = [
            (5, 3, 8),
            (10, 5, 2),
            (12, 2, 1),
            (0, 7, 7),
            (11, 3, 1)
        ]
        
        passed = 0
        for x, k, expected in test_cases:
            result = self.beta(x, k)
            status = "✓" if result == expected else "✗"
            print(f"  {status} β({x}, {k}) = {result} [expected: {expected}]")
            if result == expected:
                passed += 1
        
        if passed == len(test_cases):
            print(f"  PASSED: All {len(test_cases)} Beta tests passed!")
            self.passed_tests += 1
        else:
            print(f"  FAILED: {passed}/{len(test_cases)} tests passed")
            
        return passed == len(test_cases)
    
    def test_gamma_component(self):
        """Test Gamma component (periodicity)"""
        print("\n=== Test 3: Gamma Component (Periodicity) ===")
        self.total_tests += 1
        
        test_cases = [
            (13, 2, 1),   # 13 mod 2 = 1
            (13, 3, 1),   # 13 mod 3 = 1
            (13, 7, 2),   # ord_7(13) = 2
            (13, 5, 4),   # ord_5(13) = 4
            (13, 11, 5)   # ord_11(13) = 5
        ]
        
        passed = 0
        for a, m, expected in test_cases:
            result = self.gamma(a, m)
            status = "✓" if result == expected else "✗"
            print(f"  {status} γ({a}, {m}) = {result} [expected: {expected}]")
            if result == expected:
                passed += 1
        
        if passed == len(test_cases):
            print(f"  PASSED: All {len(test_cases)} Gamma tests passed!")
            self.passed_tests += 1
        else:
            print(f"  FAILED: {passed}/{len(test_cases)} tests passed")
            
        return passed == len(test_cases)
    
    def test_delta_component(self):
        """Test Delta component (deviation measurement)"""
        print("\n=== Test 4: Delta Component (Deviation) ===")
        self.total_tests += 1
        
        test_cases = [
            (15, 2, 0),   # 15 ≡ 2 (mod 13)
            (10, 3, 7),
            (5, 12, 6),
            (0, 0, 0),
            (26, 0, 0)    # 26 ≡ 0 (mod 13)
        ]
        
        passed = 0
        for x, x_ideal, expected in test_cases:
            result = self.delta(x, x_ideal)
            status = "✓" if result == expected else "✗"
            print(f"  {status} δ({x}, {x_ideal}) = {result} [expected: {expected}]")
            if result == expected:
                passed += 1
        
        if passed == len(test_cases):
            print(f"  PASSED: All {len(test_cases)} Delta tests passed!")
            self.passed_tests += 1
        else:
            print(f"  FAILED: {passed}/{len(test_cases)} tests passed")
            
        return passed == len(test_cases)
    
    def test_epsilon_component(self):
        """Test Epsilon component (precision bounds)"""
        print("\n=== Test 5: Epsilon Component (Precision) ===")
        self.total_tests += 1
        
        test_cases = [
            (0, 1.0),
            (1, 1/13),
            (2, 1/169),
            (3, 1/2197)
        ]
        
        passed = 0
        for n, expected in test_cases:
            result = self.epsilon(n)
            status = "✓" if abs(result - expected) < 1e-10 else "✗"
            print(f"  {status} ε({n}) = {result:.10f} [expected: {expected:.10f}]")
            if abs(result - expected) < 1e-10:
                passed += 1
        
        if passed == len(test_cases):
            print(f"  PASSED: All {len(test_cases)} Epsilon tests passed!")
            self.passed_tests += 1
        else:
            print(f"  FAILED: {passed}/{len(test_cases)} tests passed")
            
        return passed == len(test_cases)
    
    def test_component_interactions(self):
        """Test interactions between components"""
        print("\n=== Test 6: Component Interactions ===")
        self.total_tests += 1
        
        print("  Testing Alpha-Beta interaction:")
        # α(2) = 169, β(169, 3) should give (169 + 3) mod 13 = 172 mod 13 = 3
        alpha_2 = self.alpha(2)
        beta_result = self.beta(alpha_2, 3)
        expected = 3
        status = "✓" if beta_result == expected else "✗"
        print(f"    {status} β(α(2), 3) = β({alpha_2}, 3) = {beta_result} [expected: {expected}]")
        test1_passed = beta_result == expected
        
        print("  Testing Delta-Beta preservation:")
        # δ(β(x, k), β(y, k)) should equal δ(x, y)
        x, y, k = 5, 8, 3
        delta_original = self.delta(x, y)
        beta_x = self.beta(x, k)
        beta_y = self.beta(y, k)
        delta_transformed = self.delta(beta_x, beta_y)
        status = "✓" if delta_original == delta_transformed else "✗"
        print(f"    {status} δ({x}, {y}) = {delta_original}, δ(β({x}, {k}), β({y}, {k})) = {delta_transformed}")
        test2_passed = delta_original == delta_transformed
        
        if test1_passed and test2_passed:
            print(f"  PASSED: All component interaction tests passed!")
            self.passed_tests += 1
        else:
            print(f"  FAILED: Some interaction tests failed")
            
        return test1_passed and test2_passed
    
    # Component implementations
    def alpha(self, n, alpha_0=1):
        """Alpha component: α(n) = 13^n * α_0"""
        return (13 ** n) * alpha_0
    
    def beta(self, x, k):
        """Beta component: β(x, k) = (x + k) mod 13"""
        return (x + k) % 13
    
    def gamma(self, a, m):
        """Gamma component: multiplicative order of a modulo m"""
        if math.gcd(a, m) != 1:
            return None
        
        order = 1
        current = a % m
        
        while current != 1:
            current = (current * a) % m
            order += 1
            if order > m:  # Safety check
                return None
        
        return order
    
    def delta(self, x, x_ideal):
        """Delta component: δ(x, x_ideal) = |x - x_ideal| mod 13"""
        return abs(x - x_ideal) % 13
    
    def epsilon(self, n):
        """Epsilon component: ε(n) = 13^(-n)"""
        return 13 ** (-n)
    
    def run_all_tests(self):
        """Run all workshop tests"""
        print("=" * 60)
        print("WORKSHOP MODULE 2: SEQUINOR TREDECIM EXPLORATION")
        print("=" * 60)
        
        self.test_alpha_component()
        self.test_beta_component()
        self.test_gamma_component()
        self.test_delta_component()
        self.test_epsilon_component()
        self.test_component_interactions()
        
        print("\n" + "=" * 60)
        print(f"WORKSHOP SUMMARY: {self.passed_tests}/{self.total_tests} test suites passed")
        print("=" * 60)
        
        return self.passed_tests == self.total_tests


if __name__ == "__main__":
    workshop = SequinorWorkshop()
    success = workshop.run_all_tests()
    sys.exit(0 if success else 1)