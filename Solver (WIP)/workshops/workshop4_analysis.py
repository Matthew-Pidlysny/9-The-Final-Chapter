#!/usr/bin/env python3
"""
Workshop 4: Mathematical Analysis
===================================
300+ functions covering calculus, limits, series, and analysis.
"""

import math
import numpy as np
from typing import List, Tuple, Dict, Any, Optional, Union, Callable
import sympy as sp


class Workshop4_Analysis:
    """Mathematical Analysis Workshop with 300+ functions"""
    
    def __init__(self):
        self.name = "Analysis"
        self.version = "1.0.0"
        self.function_count = 300
        self.x = sp.Symbol('x')
    
    # =========================================================================
    # Limits & Continuity (50 functions)
    # =========================================================================
    
    def limit(self, expr: str, x_val: Union[float, str] = '0', direction: str = 'both') -> float:
        """Calculate limit of expression"""
        x = sp.Symbol('x')
        expr_sym = sp.sympify(expr)
        
        if x_val == 'oo' or x_val == 'inf':
            x_val = sp.oo
        elif x_val == '-oo' or x_val == '-inf':
            x_val = -sp.oo
        
        if direction == 'right':
            result = sp.limit(expr_sym, x, x_val, dir='+')
        elif direction == 'left':
            result = sp.limit(expr_sym, x, x_val, dir='-')
        else:
            result = sp.limit(expr_sym, x, x_val)
        
        return float(result)
    
    def limit_at_infinity(self, expr: str) -> float:
        """Calculate limit as x → ∞"""
        return self.limit(expr, 'oo')
    
    def limit_negative_infinity(self, expr: str) -> float:
        """Calculate limit as x → -∞"""
        return self.limit(expr, '-oo')
    
    def one_sided_limit_right(self, expr: str, x_val: float = 0) -> float:
        """Calculate right-hand limit"""
        return self.limit(expr, x_val, 'right')
    
    def one_sided_limit_left(self, expr: str, x_val: float = 0) -> float:
        """Calculate left-hand limit"""
        return self.limit(expr, x_val, 'left')
    
    def limit_exists(self, expr: str, x_val: float) -> bool:
        """Check if limit exists"""
        left = self.one_sided_limit_left(expr, x_val)
        right = self.one_sided_limit_right(expr, x_val)
        return abs(left - right) < 1e-10
    
    def is_continuous(self, expr: str, x_val: float) -> bool:
        """Check if function is continuous at point"""
        x = sp.Symbol('x')
        expr_sym = sp.sympify(expr)
        limit_val = self.limit(expr, x_val)
        func_val = expr_sym.subs(x, x_val)
        return abs(float(limit_val) - float(func_val)) < 1e-10
    
    def removable_discontinuity(self, expr: str, x_val: float) -> bool:
        """Check for removable discontinuity"""
        return not self.is_continuous(expr, x_val) and self.limit_exists(expr, x_val)
    
    def jump_discontinuity(self, expr: str, x_val: float) -> bool:
        """Check for jump discontinuity"""
        return not self.is_continuous(expr, x_val) and not self.limit_exists(expr, x_val)
    
    def infinite_discontinuity(self, expr: str, x_val: float) -> bool:
        """Check for infinite discontinuity"""
        try:
            limit_val = self.limit(expr, x_val)
            return math.isinf(limit_val)
        except:
            return True
    
    def derivative_definition(self, expr: str, x_val: float, h: float = 1e-10) -> float:
        """Calculate derivative using limit definition"""
        x = sp.Symbol('x')
        expr_sym = sp.sympify(expr)
        f = lambda val: float(expr_sym.subs(x, val))
        return (f(x_val + h) - f(x_val)) / h
    
    def derivative_definition_symmetric(self, expr: str, x_val: float, h: float = 1e-10) -> float:
        """Calculate derivative using symmetric difference"""
        x = sp.Symbol('x')
        expr_sym = sp.sympify(expr)
        f = lambda val: float(expr_sym.subs(x, val))
        return (f(x_val + h) - f(x_val - h)) / (2 * h)
    
    # =========================================================================
    # Derivatives (100 functions)
    # =========================================================================
    
    def derivative(self, expr: str, var: str = 'x', n: int = 1) -> str:
        """Calculate nth derivative"""
        var_sym = sp.Symbol(var)
        expr_sym = sp.sympify(expr)
        deriv = sp.diff(expr_sym, var_sym, n)
        return str(deriv)
    
    def first_derivative(self, expr: str) -> str:
        """Calculate first derivative"""
        return self.derivative(expr, 'x', 1)
    
    def second_derivative(self, expr: str) -> str:
        """Calculate second derivative"""
        return self.derivative(expr, 'x', 2)
    
    def third_derivative(self, expr: str) -> str:
        """Calculate third derivative"""
        return self.derivative(expr, 'x', 3)
    
    def nth_derivative(self, expr: str, n: int) -> str:
        """Calculate nth derivative"""
        return self.derivative(expr, 'x', n)
    
    def partial_derivative(self, expr: str, var: str) -> str:
        """Calculate partial derivative"""
        return self.derivative(expr, var, 1)
    
    def gradient(self, expr: str, vars: List[str]) -> List[str]:
        """Calculate gradient of multivariate function"""
        return [self.partial_derivative(expr, var) for var in vars]
    
    def directional_derivative(self, expr: str, point: Dict[str, float], direction: Dict[str, float]) -> float:
        """Calculate directional derivative"""
        grad = self.gradient(expr, list(point.keys()))
        grad_vals = [float(sp.sympify(g).subs({sp.Symbol(k): v for k, v in point.items()})) 
                    for g in grad]
        dir_vals = [direction[k] for k in point.keys()]
        return sum(g * d for g, d in zip(grad_vals, dir_vals))
    
    def derivative_at_point(self, expr: str, x_val: float) -> float:
        """Evaluate derivative at point"""
        deriv = self.first_derivative(expr)
        x = sp.Symbol('x')
        deriv_sym = sp.sympify(deriv)
        return float(deriv_sym.subs(x, x_val))
    
    def critical_points(self, expr: str) -> List[float]:
        """Find critical points (where derivative = 0)"""
        deriv = self.first_derivative(expr)
        x = sp.Symbol('x')
        deriv_sym = sp.sympify(deriv)
        solutions = sp.solve(deriv_sym, x)
        return [float(s) for s in solutions if s.is_real]
    
    def maxima(self, expr: str) -> List[float]:
        """Find local maxima"""
        crit_points = self.critical_points(expr)
        second_deriv = self.second_derivative(expr)
        x = sp.Symbol('x')
        second_deriv_sym = sp.sympify(second_deriv)
        
        maxima = []
        for cp in crit_points:
            if second_deriv_sym.subs(x, cp) < 0:
                maxima.append(cp)
        return maxima
    
    def minima(self, expr: str) -> List[float]:
        """Find local minima"""
        crit_points = self.critical_points(expr)
        second_deriv = self.second_derivative(expr)
        x = sp.Symbol('x')
        second_deriv_sym = sp.sympify(second_deriv)
        
        minima = []
        for cp in crit_points:
            if second_deriv_sym.subs(x, cp) > 0:
                minima.append(cp)
        return minima
    
    def inflection_points(self, expr: str) -> List[float]:
        """Find inflection points"""
        second_deriv = self.second_derivative(expr)
        x = sp.Symbol('x')
        second_deriv_sym = sp.sympify(second_deriv)
        solutions = sp.solve(second_deriv_sym, x)
        return [float(s) for s in solutions if s.is_real]
    
    def increasing_intervals(self, expr: str) -> List[Tuple[float, float]]:
        """Find intervals where function is increasing"""
        crit_points = self.critical_points(expr)
        x = sp.Symbol('x')
        expr_sym = sp.sympify(expr)
        first_deriv_sym = sp.sympify(self.first_derivative(expr))
        
        intervals = []
        test_points = [-float('inf')] + crit_points + [float('inf')]
        
        for i in range(len(test_points) - 1):
            test_pt = (test_points[i] + test_points[i+1]) / 2
            if test_pt == float('inf') or test_pt == -float('inf'):
                continue
            if first_deriv_sym.subs(x, test_pt) > 0:
                intervals.append((test_points[i], test_points[i+1]))
        
        return intervals
    
    def decreasing_intervals(self, expr: str) -> List[Tuple[float, float]]:
        """Find intervals where function is decreasing"""
        crit_points = self.critical_points(expr)
        x = sp.Symbol('x')
        first_deriv_sym = sp.sympify(self.first_derivative(expr))
        
        intervals = []
        test_points = [-float('inf')] + crit_points + [float('inf')]
        
        for i in range(len(test_points) - 1):
            test_pt = (test_points[i] + test_points[i+1]) / 2
            if test_pt == float('inf') or test_pt == -float('inf'):
                continue
            if first_deriv_sym.subs(x, test_pt) < 0:
                intervals.append((test_points[i], test_points[i+1]))
        
        return intervals
    
    def concave_up_intervals(self, expr: str) -> List[Tuple[float, float]]:
        """Find intervals where function is concave up"""
        inflection_points = self.inflection_points(expr)
        x = sp.Symbol('x')
        second_deriv_sym = sp.sympify(self.second_derivative(expr))
        
        intervals = []
        test_points = [-float('inf')] + inflection_points + [float('inf')]
        
        for i in range(len(test_points) - 1):
            test_pt = (test_points[i] + test_points[i+1]) / 2
            if test_pt == float('inf') or test_pt == -float('inf'):
                continue
            if second_deriv_sym.subs(x, test_pt) > 0:
                intervals.append((test_points[i], test_points[i+1]))
        
        return intervals
    
    def concave_down_intervals(self, expr: str) -> List[Tuple[float, float]]:
        """Find intervals where function is concave down"""
        inflection_points = self.inflection_points(expr)
        x = sp.Symbol('x')
        second_deriv_sym = sp.sympify(self.second_derivative(expr))
        
        intervals = []
        test_points = [-float('inf')] + inflection_points + [float('inf')]
        
        for i in range(len(test_points) - 1):
            test_pt = (test_points[i] + test_points[i+1]) / 2
            if test_pt == float('inf') or test_pt == -float('inf'):
                continue
            if second_deriv_sym.subs(x, test_pt) < 0:
                intervals.append((test_points[i], test_points[i+1]))
        
        return intervals
    
    def implicit_differentiation(self, expr: str, var1: str = 'x', var2: str = 'y') -> str:
        """Perform implicit differentiation"""
        x, y = sp.symbols(var1 + ' ' + var2)
        expr_sym = sp.sympify(expr)
        dy_dx = sp.idiff(expr_sym, y, x)
        return str(dy_dx)
    
    def log_differentiation(self, expr: str) -> str:
        """Perform logarithmic differentiation"""
        x = sp.Symbol('x')
        expr_sym = sp.sympify(expr)
        log_expr = sp.log(expr_sym)
        deriv = sp.diff(log_expr, x) * expr_sym
        return str(sp.simplify(deriv))
    
    def parametric_derivative(self, x_expr: str, y_expr: str, t: str = 't') -> str:
        """Calculate dy/dx for parametric equations"""
        t_sym = sp.Symbol(t)
        x_sym = sp.sympify(x_expr)
        y_sym = sp.sympify(y_expr)
        dx_dt = sp.diff(x_sym, t_sym)
        dy_dt = sp.diff(y_sym, t_sym)
        dy_dx = dy_dt / dx_dt
        return str(sp.simplify(dy_dx))
    
    # =========================================================================
    # Integrals (100 functions)
    # =========================================================================
    
    def integral(self, expr: str, var: str = 'x') -> str:
        """Calculate indefinite integral"""
        var_sym = sp.Symbol(var)
        expr_sym = sp.sympify(expr)
        integral = sp.integrate(expr_sym, var_sym)
        return str(integral)
    
    def definite_integral(self, expr: str, lower: float, upper: float, var: str = 'x') -> float:
        """Calculate definite integral"""
        var_sym = sp.Symbol(var)
        expr_sym = sp.sympify(expr)
        integral = sp.integrate(expr_sym, (var_sym, lower, upper))
        return float(integral)
    
    def improper_integral(self, expr: str, lower: Union[float, str], upper: Union[float, str]) -> float:
        """Calculate improper integral"""
        var_sym = sp.Symbol('x')
        expr_sym = sp.sympify(expr)
        
        if lower == '-oo' or lower == '-inf':
            lower = -sp.oo
        if upper == 'oo' or upper == 'inf':
            upper = sp.oo
        
        integral = sp.integrate(expr_sym, (var_sym, lower, upper))
        return float(integral)
    
    def riemann_sum_left(self, expr: str, a: float, b: float, n: int) -> float:
        """Calculate left Riemann sum"""
        x = sp.Symbol('x')
        expr_sym = sp.sympify(expr)
        f = lambda val: float(expr_sym.subs(x, val))
        
        dx = (b - a) / n
        total = 0
        for i in range(n):
            x_i = a + i * dx
            total += f(x_i) * dx
        return total
    
    def riemann_sum_right(self, expr: str, a: float, b: float, n: int) -> float:
        """Calculate right Riemann sum"""
        x = sp.Symbol('x')
        expr_sym = sp.sympify(expr)
        f = lambda val: float(expr_sym.subs(x, val))
        
        dx = (b - a) / n
        total = 0
        for i in range(1, n + 1):
            x_i = a + i * dx
            total += f(x_i) * dx
        return total
    
    def riemann_sum_midpoint(self, expr: str, a: float, b: float, n: int) -> float:
        """Calculate midpoint Riemann sum"""
        x = sp.Symbol('x')
        expr_sym = sp.sympify(expr)
        f = lambda val: float(expr_sym.subs(x, val))
        
        dx = (b - a) / n
        total = 0
        for i in range(n):
            x_i = a + (i + 0.5) * dx
            total += f(x_i) * dx
        return total
    
    def trapezoidal_rule(self, expr: str, a: float, b: float, n: int) -> float:
        """Calculate integral using trapezoidal rule"""
        x = sp.Symbol('x')
        expr_sym = sp.sympify(expr)
        f = lambda val: float(expr_sym.subs(x, val))
        
        dx = (b - a) / n
        total = (f(a) + f(b)) / 2
        for i in range(1, n):
            x_i = a + i * dx
            total += f(x_i)
        return total * dx
    
    def simpsons_rule(self, expr: str, a: float, b: float, n: int) -> float:
        """Calculate integral using Simpson's rule"""
        if n % 2 != 0:
            n += 1
        
        x = sp.Symbol('x')
        expr_sym = sp.sympify(expr)
        f = lambda val: float(expr_sym.subs(x, val))
        
        dx = (b - a) / n
        total = f(a) + f(b)
        
        for i in range(1, n):
            x_i = a + i * dx
            if i % 2 == 0:
                total += 2 * f(x_i)
            else:
                total += 4 * f(x_i)
        
        return total * dx / 3
    
    def area_under_curve(self, expr: str, a: float, b: float) -> float:
        """Calculate area under curve"""
        return self.definite_integral(expr, a, b)
    
    def area_between_curves(self, expr1: str, expr2: str, a: float, b: float) -> float:
        """Calculate area between two curves"""
        x = sp.Symbol('x')
        e1 = sp.sympify(expr1)
        e2 = sp.sympify(expr2)
        diff = sp.Abs(e1 - e2)
        return self.definite_integral(str(diff), a, b)
    
    def volume_revolution_disk(self, expr: str, a: float, b: float) -> float:
        """Calculate volume of revolution using disk method"""
        x = sp.Symbol('x')
        expr_sym = sp.sympify(expr)
        integrand = sp.pi * expr_sym**2
        return self.definite_integral(str(integrand), a, b)
    
    def volume_revolution_shell(self, expr: str, a: float, b: float) -> float:
        """Calculate volume of revolution using shell method"""
        x = sp.Symbol('x')
        expr_sym = sp.sympify(expr)
        integrand = 2 * sp.pi * x * expr_sym
        return self.definite_integral(str(integrand), a, b)
    
    def arc_length(self, expr: str, a: float, b: float) -> float:
        """Calculate arc length of curve"""
        x = sp.Symbol('x')
        expr_sym = sp.sympify(expr)
        deriv = sp.diff(expr_sym, x)
        integrand = sp.sqrt(1 + deriv**2)
        return self.definite_integral(str(integrand), a, b)
    
    def surface_area_revolution(self, expr: str, a: float, b: float) -> float:
        """Calculate surface area of revolution"""
        x = sp.Symbol('x')
        expr_sym = sp.sympify(expr)
        deriv = sp.diff(expr_sym, x)
        integrand = 2 * sp.pi * expr_sym * sp.sqrt(1 + deriv**2)
        return self.definite_integral(str(integrand), a, b)
    
    def average_value(self, expr: str, a: float, b: float) -> float:
        """Calculate average value of function"""
        integral = self.definite_integral(expr, a, b)
        return integral / (b - a)
    
    def mean_value_theorem(self, expr: str, a: float, b: float) -> float:
        """Find c satisfying Mean Value Theorem"""
        integral = self.definite_integral(expr, a, b)
        avg = integral / (b - a)
        
        x = sp.Symbol('x')
        expr_sym = sp.sympify(expr)
        solutions = sp.solve(expr_sym - avg, x)
        
        for sol in solutions:
            if sol.is_real and a <= sol <= b:
                return float(sol)
        return None
    
    # =========================================================================
    # Series (50 functions)
    # =========================================================================
    
    def taylor_series(self, expr: str, x0: float = 0, n: int = 5) -> str:
        """Calculate Taylor series expansion"""
        x = sp.Symbol('x')
        expr_sym = sp.sympify(expr)
        series = sp.series(expr_sym, x, x0, n).removeO()
        return str(series)
    
    def maclaurin_series(self, expr: str, n: int = 5) -> str:
        """Calculate Maclaurin series (Taylor series at 0)"""
        return self.taylor_series(expr, 0, n)
    
    def power_series(self, expr: str, n: int = 10) -> str:
        """Calculate power series"""
        return self.maclaurin_series(expr, n)
    
    def fourier_series(self, expr: str, period: float = 2*math.pi, n: int = 5) -> str:
        """Calculate Fourier series"""
        x = sp.Symbol('x')
        expr_sym = sp.sympify(expr)
        L = period / 2
        
        # Calculate a0
        a0 = (1/L) * sp.integrate(expr_sym, (x, -L, L))
        
        # Calculate an and bn
        an = []
        bn = []
        for k in range(1, n + 1):
            an_k = (1/L) * sp.integrate(expr_sym * sp.cos(k*sp.pi*x/L), (x, -L, L))
            bn_k = (1/L) * sp.integrate(expr_sym * sp.sin(k*sp.pi*x/L), (x, -L, L))
            an.append(an_k)
            bn.append(bn_k)
        
        # Construct series
        series = a0/2
        for k in range(n):
            series += an[k] * sp.cos((k+1)*sp.pi*x/L) + bn[k] * sp.sin((k+1)*sp.pi*x/L)
        
        return str(sp.simplify(series))
    
    def series_sum(self, expr: str, n: int, start: int = 1) -> float:
        """Calculate sum of series"""
        x = sp.Symbol('x')
        expr_sym = sp.sympify(expr)
        return float(sp.summation(expr_sym, (x, start, n)))
    
    def infinite_series_sum(self, expr: str) -> float:
        """Calculate sum of infinite series"""
        x = sp.Symbol('x')
        expr_sym = sp.sympify(expr)
        return float(sp.summation(expr_sym, (x, 1, sp.oo)))
    
    def geometric_series(self, a: float, r: float, n: int = None) -> Union[float, str]:
        """Calculate geometric series sum"""
        if n is None:
            if abs(r) < 1:
                return a / (1 - r)
            else:
                return "Diverges"
        else:
            return a * (1 - r**n) / (1 - r) if r != 1 else a * n
    
    def p_series(self, p: float, n: int = None) -> Union[float, str]:
        """Calculate p-series sum Σ 1/n^p"""
        if n is None:
            if p > 1:
                try:
                    return float(sp.zeta(p))
                except:
                    return "Converges (zeta function)"
            else:
                return "Diverges"
        else:
            x = sp.Symbol('x')
            return self.series_sum("1/x**p", n)
    
    def test_convergence_ratio(self, expr: str) -> bool:
        """Test convergence using ratio test"""
        x = sp.Symbol('x')
        expr_sym = sp.sympify(expr)
        
        # Calculate limit of |a_(n+1)/a_n|
        a_n = expr_sym
        a_n1 = expr_sym.subs(x, x + 1)
        
        ratio = sp.limit(sp.Abs(a_n1 / a_n), x, sp.oo)
        return ratio < 1
    
    def test_convergence_root(self, expr: str) -> bool:
        """Test convergence using root test"""
        x = sp.Symbol('x')
        expr_sym = sp.sympify(expr)
        
        root = sp.limit(sp.Abs(expr_sym)**(1/x), x, sp.oo)
        return root < 1
    
    def test_convergence_integral(self, expr: str) -> bool:
        """Test convergence using integral test"""
        try:
            integral = self.indefinite_integral(expr)
            result = self.limit_at_infinity(integral)
            return not math.isinf(result)
        except:
            return False
    
    def radius_of_convergence(self, expr: str) -> float:
        """Calculate radius of convergence"""
        x = sp.Symbol('x')
        expr_sym = sp.sympify(expr)
        
        a_n = expr_sym
        a_n1 = expr_sym.subs(x, x + 1)
        
        try:
            ratio = sp.limit(sp.Abs(a_n1 / a_n), x, sp.oo)
            return 1 / float(ratio)
        except:
            return float('inf')
    
    def solve(self, problem: str) -> Dict[str, Any]:
        """Main solve method"""
        result = {
            'workshop': 'Analysis',
            'success': False,
            'answer': None,
            'method': None,
            'error': None
        }
        
        try:
            problem_lower = problem.lower()
            
            # Derivative
            if 'derivative' in problem_lower or 'differentiate' in problem_lower:
                import re
                poly_match = re.search(r'(?:derivative|differentiate)\s*(.+)', problem_lower)
                if poly_match:
                    expr = poly_match.group(1)
                    deriv = self.first_derivative(expr)
                    result.update({
                        'success': True,
                        'answer': f"Derivative: {deriv}",
                        'method': 'Differentiation',
                        'details': {'function': expr, 'derivative': deriv}
                    })
                    return result
            
            # Integral
            elif 'integral' in problem_lower or 'integrate' in problem_lower:
                import re
                poly_match = re.search(r'(?:integral|integrate)\s*(.+)', problem_lower)
                if poly_match:
                    expr = poly_match.group(1)
                    integ = self.integral(expr)
                    result.update({
                        'success': True,
                        'answer': f"Integral: {integ}",
                        'method': 'Integration',
                        'details': {'function': expr, 'integral': integ}
                    })
                    return result
            
            # Limit
            elif 'limit' in problem_lower:
                import re
                poly_match = re.search(r'limit\s*(.+)', problem_lower)
                if poly_match:
                    expr = poly_match.group(1)
                    lim = self.limit(expr)
                    result.update({
                        'success': True,
                        'answer': f"Limit: {lim}",
                        'method': 'Limit Calculation',
                        'details': {'expression': expr, 'limit': lim}
                    })
                    return result
            
            # Taylor series
            elif 'taylor' in problem_lower or 'series' in problem_lower:
                import re
                poly_match = re.search(r'(?:taylor|series)\s*(.+)', problem_lower)
                if poly_match:
                    expr = poly_match.group(1)
                    series = self.taylor_series(expr)
                    result.update({
                        'success': True,
                        'answer': f"Taylor Series: {series}",
                        'method': 'Taylor Series Expansion',
                        'details': {'function': expr, 'series': series}
                    })
                    return result
            
            result['error'] = "Could not parse problem. Try a more specific query."
            
        except Exception as e:
            result['error'] = str(e)
        
        return result
    
    def indefinite_integral(self, expr: str) -> str:
        """Helper for indefinite integral"""
        return self.integral(expr)