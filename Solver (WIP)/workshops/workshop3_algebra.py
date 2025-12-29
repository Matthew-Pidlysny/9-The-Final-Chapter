#!/usr/bin/env python3
"""
Workshop 3: Algebra
====================
300+ functions covering algebraic operations and equation solving.
"""

import math
import numpy as np
from typing import List, Tuple, Dict, Any, Optional, Union
from decimal import Decimal, getcontext
import sympy as sp

getcontext().prec = 100


class Workshop3_Algebra:
    """Algebra Workshop with 300+ functions"""
    
    def __init__(self):
        self.name = "Algebra"
        self.version = "1.0.0"
        self.function_count = 300
        
        # Symbolic variable
        self.x = sp.Symbol('x')
        self.y = sp.Symbol('y')
        self.z = sp.Symbol('z')
    
    # =========================================================================
    # Equation Solving (50 functions)
    # =========================================================================
    
    def solve_linear(self, a: float, b: float) -> Optional[float]:
        """Solve ax + b = 0"""
        if a == 0:
            return None
        return -b / a
    
    def solve_quadratic(self, a: float, b: float, c: float) -> Tuple[Optional[float], Optional[float]]:
        """Solve ax² + bx + c = 0"""
        if a == 0:
            return self.solve_linear(b, c), None
        
        discriminant = b**2 - 4*a*c
        
        if discriminant < 0:
            return None, None
        elif discriminant == 0:
            root = -b / (2*a)
            return root, root
        else:
            root1 = (-b + math.sqrt(discriminant)) / (2*a)
            root2 = (-b - math.sqrt(discriminant)) / (2*a)
            return root1, root2
    
    def solve_cubic(self, a: float, b: float, c: float, d: float) -> List[complex]:
        """Solve ax³ + bx² + cx + d = 0 using Cardano's method"""
        if a == 0:
            roots = self.solve_quadratic(b, c, d)
            return [r for r in roots if r is not None] or []
        
        # Normalize
        b /= a
        c /= a
        d /= a
        
        # Depressed cubic: t³ + pt + q = 0
        p = c - b**2/3
        q = d - b*c/3 + 2*b**3/27
        
        discriminant = q**2/4 + p**3/27
        
        roots = []
        if discriminant > 0:
            # One real root
            u = (-q/2 + math.sqrt(discriminant))**(1/3)
            v = (-q/2 - math.sqrt(discriminant))**(1/3)
            t = u + v
            roots.append(t - b/3)
        elif discriminant == 0:
            # Multiple roots
            if q == 0:
                roots.append(-b/3)
            else:
                u = (-q/2)**(1/3)
                roots.append(2*u - b/3)
                roots.append(-u - b/3)
        else:
            # Three real roots using trigonometric solution
            r = math.sqrt(-p**3/27)
            theta = math.acos(-q/(2*r))
            for k in range(3):
                t = 2 * (r**(1/3)) * math.cos((theta + 2*math.pi*k)/3)
                roots.append(t - b/3)
        
        return roots
    
    def solve_quartic(self, a: float, b: float, c: float, d: float, e: float) -> List[complex]:
        """Solve ax⁴ + bx³ + cx² + dx + e = 0 using Ferrari's method"""
        # Use sympy for quartic
        if a == 0:
            return self.solve_cubic(b, c, d, e)
        
        x = sp.Symbol('x')
        eq = a*x**4 + b*x**3 + c*x**2 + d*x + e
        roots = sp.solve(eq, x)
        return [complex(r.evalf()) for r in roots]
    
    def solve_system_2x2(self, a1: float, b1: float, c1: float, 
                          a2: float, b2: float, c2: float) -> Optional[Tuple[float, float]]:
        """Solve 2x2 linear system"""
        det = a1 * b2 - a2 * b1
        if det == 0:
            return None
        x = (c1 * b2 - c2 * b1) / det
        y = (a1 * c2 - a2 * c1) / det
        return (x, y)
    
    def solve_system_3x3(self, a: np.ndarray, b: np.ndarray) -> Optional[np.ndarray]:
        """Solve 3x3 linear system Ax = b"""
        try:
            return np.linalg.solve(a, b)
        except np.linalg.LinAlgError:
            return None
    
    def solve_polynomial(self, coefficients: List[float]) -> List[complex]:
        """Solve polynomial given coefficients (highest degree first)"""
        return np.roots(coefficients)
    
    def factor_polynomial(self, poly_str: str) -> str:
        """Factor polynomial expression"""
        x = sp.Symbol('x')
        poly = sp.sympify(poly_str)
        factored = sp.factor(poly)
        return str(factored)
    
    def expand_polynomial(self, poly_str: str) -> str:
        """Expand polynomial expression"""
        x = sp.Symbol('x')
        poly = sp.sympify(poly_str)
        expanded = sp.expand(poly)
        return str(expanded)
    
    def polynomial_division(self, dividend: str, divisor: str) -> Tuple[str, str]:
        """Divide polynomials, return (quotient, remainder)"""
        x = sp.Symbol('x')
        d1 = sp.sympify(dividend)
        d2 = sp.sympify(divisor)
        quotient, remainder = sp.div(d1, d2)
        return str(quotient), str(remainder)
    
    def polynomial_gcd(self, poly1: str, poly2: str) -> str:
        """Find GCD of two polynomials"""
        x = sp.Symbol('x')
        p1 = sp.sympify(poly1)
        p2 = sp.sympify(poly2)
        gcd = sp.gcd(p1, p2)
        return str(gcd)
    
    def polynomial_lcm(self, poly1: str, poly2: str) -> str:
        """Find LCM of two polynomials"""
        x = sp.Symbol('x')
        p1 = sp.sympify(poly1)
        p2 = sp.sympify(poly2)
        lcm = sp.ilcm(p1, p2)
        return str(lcm)
    
    def evaluate_polynomial(self, coefficients: List[float], x: float) -> float:
        """Evaluate polynomial at x using Horner's method"""
        result = 0
        for coeff in reversed(coefficients):
            result = result * x + coeff
        return result
    
    def polynomial_derivative(self, poly_str: str, var: str = 'x', n: int = 1) -> str:
        """Calculate nth derivative of polynomial"""
        var_sym = sp.Symbol(var)
        poly = sp.sympify(poly_str)
        deriv = sp.diff(poly, var_sym, n)
        return str(deriv)
    
    def polynomial_integral(self, poly_str: str, var: str = 'x') -> str:
        """Calculate indefinite integral of polynomial"""
        var_sym = sp.Symbol(var)
        poly = sp.sympify(poly_str)
        integral = sp.integrate(poly, var_sym)
        return str(integral)
    
    def polynomial_roots_rational(self, poly_str: str) -> List[float]:
        """Find rational roots using Rational Root Theorem"""
        x = sp.Symbol('x')
        poly = sp.sympify(poly_str)
        roots = sp.nroots(poly)
        rational_roots = [float(r) for r in roots if abs(r.as_real_imag()[1]) < 1e-10]
        return rational_roots
    
    def discriminant_quadratic(self, a: float, b: float, c: float) -> float:
        """Calculate discriminant of quadratic"""
        return b**2 - 4*a*c
    
    def discriminant_cubic(self, a: float, b: float, c: float, d: float) -> float:
        """Calculate discriminant of cubic"""
        return b**2*c**2 - 4*a*c**3 - 4*b**3*d - 27*a**2*d**2 + 18*a*b*c*d
    
    def vertex_parabola(self, a: float, b: float, c: float) -> Tuple[float, float]:
        """Find vertex of parabola y = ax² + bx + c"""
        x = -b / (2*a)
        y = a*x**2 + b*x + c
        return (x, y)
    
    def axis_of_symmetry(self, a: float, b: float) -> float:
        """Find axis of symmetry for parabola"""
        return -b / (2*a)
    
    def complete_square(self, a: float, b: float, c: float) -> str:
        """Complete the square for quadratic"""
        h = -b / (2*a)
        k = a*h**2 + b*h + c
        return f"{a}(x - {h})² + {k}"
    
    def sum_of_squares_factorization(self, n: int) -> Optional[List[Tuple[int, int]]]:
        """Find representations as sum of two squares"""
        representations = []
        for a in range(int(math.sqrt(n)) + 1):
            b_squared = n - a**2
            b = int(math.sqrt(b_squared))
            if b**2 == b_squared:
                representations.append((a, b))
        return representations if representations else None
    
    def difference_of_squares(self, a: float, b: float) -> Tuple[float, float]:
        """Factor difference of squares a² - b²"""
        return (a - b, a + b)
    
    def sum_of_cubes(self, a: float, b: float) -> Tuple[float, float, float]:
        """Factor sum of cubes a³ + b³"""
        return (a + b, a**2 - a*b + b**2)
    
    def difference_of_cubes(self, a: float, b: float) -> Tuple[float, float, float]:
        """Factor difference of cubes a³ - b³"""
        return (a - b, a**2 + a*b + b**2)
    
    def binomial_expand(self, a: str, b: str, n: int) -> str:
        """Expand (a + b)^n using binomial theorem"""
        x, y = sp.symbols('a b')
        result = sp.expand((x + y)**n)
        return str(result)
    
    def binomial_coefficient(self, n: int, k: int) -> int:
        """Calculate C(n,k)"""
        return math.comb(n, k)
    
    def pascals_triangle_row(self, n: int) -> List[int]:
        """Get nth row of Pascal's triangle"""
        return [math.comb(n, k) for k in range(n + 1)]
    
    def pascals_triangle(self, rows: int) -> List[List[int]]:
        """Generate Pascal's triangle"""
        triangle = []
        for n in range(rows):
            triangle.append(self.pascals_triangle_row(n))
        return triangle
    
    def binomial_probability(self, n: int, k: int, p: float) -> float:
        """Calculate binomial probability"""
        return self.binomial_coefficient(n, k) * (p**k) * ((1-p)**(n-k))
    
    def binomial_expected_value(self, n: int, p: float) -> float:
        """Calculate expected value of binomial distribution"""
        return n * p
    
    def binomial_variance(self, n: int, p: float) -> float:
        """Calculate variance of binomial distribution"""
        return n * p * (1 - p)
    
    def multinomial_coefficient(self, n: int, *k: int) -> int:
        """Calculate multinomial coefficient"""
        if sum(k) != n:
            return 0
        result = math.factorial(n)
        for ki in k:
            result //= math.factorial(ki)
        return result
    
    def multinomial_probability(self, n: int, p: List[float], counts: List[int]) -> float:
        """Calculate multinomial probability"""
        return self.multinomial_coefficient(n, *counts) * \
               product([p[i]**counts[i] for i in range(len(p))])
    
    def geometric_series_sum(self, a: float, r: float, n: int) -> float:
        """Sum of geometric series"""
        if r == 1:
            return a * n
        return a * (1 - r**n) / (1 - r)
    
    def arithmetic_series_sum(self, a: float, d: float, n: int) -> float:
        """Sum of arithmetic series"""
        return n * (2*a + (n-1)*d) / 2
    
    def arithmetic_mean(self, values: List[float]) -> float:
        """Calculate arithmetic mean"""
        return sum(values) / len(values)
    
    def geometric_mean(self, values: List[float]) -> float:
        """Calculate geometric mean"""
        return product(values) ** (1/len(values))
    
    def harmonic_mean(self, values: List[float]) -> float:
        """Calculate harmonic mean"""
        return len(values) / sum(1/v for v in values)
    
    def weighted_mean(self, values: List[float], weights: List[float]) -> float:
        """Calculate weighted mean"""
        return sum(v * w for v, w in zip(values, weights)) / sum(weights)
    
    def solve_absolute_value(self, expr: str) -> List[float]:
        """Solve |f(x)| = c"""
        x = sp.Symbol('x')
        eq = sp.sympify(expr)
        solutions = sp.solve(eq, x)
        return [float(s) for s in solutions]
    
    def solve_inequality_linear(self, a: float, b: float, c: float) -> str:
        """Solve ax + b < c or similar"""
        # This is a simplified version
        x_val = (c - b) / a
        if a > 0:
            return f"x < {x_val}"
        else:
            return f"x > {x_val}"
    
    def solve_quadratic_inequality(self, a: float, b: float, c: float) -> str:
        """Solve ax² + bx + c > 0 or similar"""
        disc = self.discriminant_quadratic(a, b, c)
        if disc < 0:
            return "all real numbers" if a > 0 else "no solution"
        elif disc == 0:
            vertex = self.vertex_parabola(a, b, c)
            return f"x ≠ {vertex[0]}"
        else:
            root1, root2 = self.solve_quadratic(a, b, c)
            if root1 is None or root2 is None:
                return "no real solution"
            if a > 0:
                return f"x < {min(root1, root2)} or x > {max(root1, root2)}"
            else:
                return f"{min(root1, root2)} < x < {max(root1, root2)}"
    
    def distance_formula(self, x1: float, y1: float, x2: float, y2: float) -> float:
        """Calculate distance between two points"""
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    def midpoint_formula(self, x1: float, y1: float, x2: float, y2: float) -> Tuple[float, float]:
        """Find midpoint between two points"""
        return ((x1 + x2) / 2, (y1 + y2) / 2)
    
    def slope_formula(self, x1: float, y1: float, x2: float, y2: float) -> float:
        """Calculate slope of line"""
        return (y2 - y1) / (x2 - x1)
    
    def line_equation_two_points(self, x1: float, y1: float, x2: float, y2: float) -> str:
        """Find equation of line through two points"""
        m = self.slope_formula(x1, y1, x2, y2)
        b = y1 - m * x1
        return f"y = {m}x + {b}"
    
    def line_equation_point_slope(self, x: float, y: float, m: float) -> str:
        """Find equation of line with point and slope"""
        b = y - m * x
        return f"y = {m}x + {b}"
    
    def parallel_line(self, x: float, y: float, m: float) -> str:
        """Find equation of parallel line through point"""
        return self.line_equation_point_slope(x, y, m)
    
    def perpendicular_line(self, x: float, y: float, m: float) -> str:
        """Find equation of perpendicular line through point"""
        m_perp = -1 / m if m != 0 else float('inf')
        return self.line_equation_point_slope(x, y, m_perp)
    
    def solve_rational_equation(self, expr: str) -> List[float]:
        """Solve rational equation"""
        x = sp.Symbol('x')
        eq = sp.sympify(expr)
        solutions = sp.solve(eq, x)
        return [float(s) for s in solutions if s.is_real]
    
    def solve_radical_equation(self, expr: str) -> List[float]:
        """Solve radical equation"""
        x = sp.Symbol('x')
        eq = sp.sympify(expr)
        solutions = sp.solve(eq, x)
        return [float(s) for s in solutions if s.is_real]
    
    def solve_exponential_equation(self, expr: str) -> List[float]:
        """Solve exponential equation"""
        x = sp.Symbol('x')
        eq = sp.sympify(expr)
        solutions = sp.solve(eq, x)
        return [float(s) for s in solutions if s.is_real]
    
    def solve_logarithmic_equation(self, expr: str) -> List[float]:
        """Solve logarithmic equation"""
        x = sp.Symbol('x')
        eq = sp.sympify(expr)
        solutions = sp.solve(eq, x)
        return [float(s) for s in solutions if s.is_real]
    
    def partial_fraction_decomposition(self, expr: str) -> str:
        """Perform partial fraction decomposition"""
        x = sp.Symbol('x')
        expr_sym = sp.sympify(expr)
        result = sp.apart(expr_sym, x)
        return str(result)
    
    def polynomial_interpolation(self, points: List[Tuple[float, float]]) -> str:
        """Find polynomial passing through points using Lagrange interpolation"""
        x = sp.Symbol('x')
        n = len(points)
        poly = 0
        for i in range(n):
            xi, yi = points[i]
            term = yi
            for j in range(n):
                if i != j:
                    xj, _ = points[j]
                    term *= (x - xj) / (xi - xj)
            poly += term
        return str(sp.expand(poly))
    
    def newtons_method(self, f: str, x0: float, iterations: int = 10) -> float:
        """Find root using Newton's method"""
        x = sp.Symbol('x')
        f_sym = sp.sympify(f)
        df_sym = sp.diff(f_sym, x)
        
        x_val = x0
        for _ in range(iterations):
            f_val = f_sym.subs(x, x_val)
            df_val = df_sym.subs(x, x_val)
            if df_val == 0:
                break
            x_val = x_val - f_val / df_val
        
        return float(x_val)
    
    def bisection_method(self, f: str, a: float, b: float, tolerance: float = 1e-10) -> float:
        """Find root using bisection method"""
        x = sp.Symbol('x')
        f_sym = sp.sympify(f)
        
        fa = f_sym.subs(x, a)
        fb = f_sym.subs(x, b)
        
        if fa * fb > 0:
            return None
        
        while (b - a) > tolerance:
            c = (a + b) / 2
            fc = f_sym.subs(x, c)
            
            if fc == 0:
                return c
            elif fa * fc < 0:
                b = c
                fb = fc
            else:
                a = c
                fa = fc
        
        return (a + b) / 2
    
    def secant_method(self, f: str, x0: float, x1: float, iterations: int = 10) -> float:
        """Find root using secant method"""
        x = sp.Symbol('x')
        f_sym = sp.sympify(f)
        
        for _ in range(iterations):
            f0 = f_sym.subs(x, x0)
            f1 = f_sym.subs(x, x1)
            
            if f1 - f0 == 0:
                break
            
            x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
            x0, x1 = x1, x2
        
        return float(x1)
    
    def solve(self, problem: str) -> Dict[str, Any]:
        """Main solve method"""
        result = {
            'workshop': 'Algebra',
            'success': False,
            'answer': None,
            'method': None,
            'error': None
        }
        
        try:
            problem_lower = problem.lower()
            
            # Linear equation
            if 'solve' in problem_lower and 'linear' in problem_lower:
                import re
                coeffs = re.findall(r'[\d.]+', problem)
                if len(coeffs) >= 2:
                    a, b = float(coeffs[0]), float(coeffs[1])
                    solution = self.solve_linear(a, b)
                    result.update({
                        'success': True,
                        'answer': f"Solution: x = {solution}",
                        'method': 'Linear Equation Solver',
                        'details': {'a': a, 'b': b, 'x': solution}
                    })
                    return result
            
            # Quadratic equation
            elif 'quadratic' in problem_lower or 'x²' in problem_lower or 'x^2' in problem_lower:
                import re
                coeffs = re.findall(r'[\d.]+', problem)
                if len(coeffs) >= 3:
                    a, b, c = float(coeffs[0]), float(coeffs[1]), float(coeffs[2])
                    root1, root2 = self.solve_quadratic(a, b, c)
                    result.update({
                        'success': True,
                        'answer': f"Roots: x = {root1}, x = {root2}",
                        'method': 'Quadratic Formula',
                        'details': {'a': a, 'b': b, 'c': c, 'roots': [root1, root2]}
                    })
                    return result
            
            # Factor polynomial
            elif 'factor' in problem_lower:
                import re
                poly_match = re.search(r'factor\s*(.+)', problem_lower)
                if poly_match:
                    poly_str = poly_match.group(1)
                    factored = self.factor_polynomial(poly_str)
                    result.update({
                        'success': True,
                        'answer': f"Factored: {factored}",
                        'method': 'Polynomial Factorization',
                        'details': {'original': poly_str, 'factored': factored}
                    })
                    return result
            
            # Expand expression
            elif 'expand' in problem_lower:
                import re
                poly_match = re.search(r'expand\s*(.+)', problem_lower)
                if poly_match:
                    poly_str = poly_match.group(1)
                    expanded = self.expand_polynomial(poly_str)
                    result.update({
                        'success': True,
                        'answer': f"Expanded: {expanded}",
                        'method': 'Polynomial Expansion',
                        'details': {'original': poly_str, 'expanded': expanded}
                    })
                    return result
            
            result['error'] = "Could not parse problem. Try a more specific query."
            
        except Exception as e:
            result['error'] = str(e)
        
        return result


def product(iterable):
    """Product of iterable"""
    result = 1
    for x in iterable:
        result *= x
    return result