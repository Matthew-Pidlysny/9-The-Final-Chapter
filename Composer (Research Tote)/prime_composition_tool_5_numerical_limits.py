"""
PRIME COMPOSITION TOOL #5: NUMERICAL LIMITS ANALYZER
==================================================
Analyzes numerical boundaries and termination properties of primes.

Features:
- Tests prime reciprocals at different precision scales
- Analyzes the 61-digit quantum limit hypothesis
- Studies entropy stabilization at numerical boundaries
- Maps termination patterns to composition
- Investigates physical vs mathematical reality
"""

import math
from fractions import Fraction
from decimal import Decimal, getcontext
import json
from typing import List, Dict, Tuple
import statistics

getcontext().prec = 200

# Constants
C_STAR = 17 / 19
POINT_SIX = 3 / 5
QUANTUM_LIMIT = 61
PLANCK_LIMIT = 35
COGNITIVE_LIMIT = 15

class NumericalLimitsAnalyzer:
    """Analyze numerical boundaries and termination properties."""
    
    def __init__(self):
        self.limits = {
            'cognitive': 15,
            'planck': 35,
            'quantum': 61,
            'practical': 100
        }
    
    def analyze_prime_at_limits(self, p: int) -> Dict:
        """Analyze prime p at different numerical limits."""
        
        limits_analysis = {
            'prime': p,
            'limit_analyses': {}
        }
        
        for limit_name, limit_digits in self.limits.items():
            # Get decimal expansion at this limit
            decimal = Decimal(1) / Decimal(p)
            decimal_str = str(decimal)
            
            if '.' in decimal_str:
                decimal_str = decimal_str.split('.')[1][:limit_digits]
            
            # Calculate entropy at this scale
            digit_counts = [0] * 10
            for digit in decimal_str:
                if digit.isdigit():
                    digit_counts[int(digit)] += 1
            
            total = sum(digit_counts)
            entropy = 0.0
            if total > 0:
                for count in digit_counts:
                    if count > 0:
                        p_i = count / total
                        entropy -= p_i * math.log2(p_i)
            
            # Check for termination patterns
            period = self._find_period_at_scale(p, limit_digits)
            is_stable = self._is_stable_at_scale(p, limit_digits)
            
            limits_analysis['limit_analyses'][limit_name] = {
                'digits': limit_digits,
                'decimal_expansion': decimal_str,
                'entropy': entropy,
                'normalized_entropy': entropy / math.log2(10),
                'period': period,
                'is_stable': is_stable,
                'terminates': period is not None and period <= limit_digits
            }
        
        return limits_analysis
    
    def _find_period_at_scale(self, p: int, max_digits: int) -> int:
        """Find period of 1/p within digit limit."""
        if p == 2 or p == 5:
            return None
        
        remainder = 1
        remainders_seen = {}
        position = 0
        
        while remainder != 0 and remainder not in remainders_seen and position < max_digits:
            remainders_seen[remainder] = position
            remainder = (remainder * 10) % p
            position += 1
        
        if remainder == 0:
            return position
        elif remainder in remainders_seen:
            return position - remainders_seen[remainder]
        else:
            return None  # Period exceeds limit
    
    def _is_stable_at_scale(self, p: int, scale: int) -> bool:
        """Check if entropy stabilizes at this scale."""
        if scale < 30:  # Need minimum scale for stability test
            return False
        
        # Compare entropy at scale/2 and scale
        decimal_half = Decimal(1) / Decimal(p)
        half_str = str(decimal_half).split('.')[1][:scale//2] if '.' in str(decimal_half) else ''
        
        decimal_full = Decimal(1) / Decimal(p)
        full_str = str(decimal_full).split('.')[1][:scale] if '.' in str(decimal_full) else ''
        
        # Calculate entropies
        entropy_half = self._calculate_entropy(half_str)
        entropy_full = self._calculate_entropy(full_str)
        
        # Consider stable if change is less than 1%
        return (entropy_half > 0 and abs(entropy_full - entropy_half) / entropy_half < 0.01)
    
    def _calculate_entropy(self, digit_string: str) -> float:
        """Calculate Shannon entropy of digit string."""
        if not digit_string:
            return 0.0
        
        digit_counts = [0] * 10
        for digit in digit_string:
            if digit.isdigit():
                digit_counts[int(digit)] += 1
        
        total = sum(digit_counts)
        entropy = 0.0
        if total > 0:
            for count in digit_counts:
                if count > 0:
                    p_i = count / total
                    entropy -= p_i * math.log2(p_i)
        
        return entropy
    
    def analyze_quantum_limit_hypothesis(self, primes: List[int]) -> Dict:
        """Test the quantum limit (61 digits) hypothesis."""
        
        quantum_analysis = {
            'hypothesis': 'Numbers terminate or stabilize at 61 digits (quantum limit)',
            'test_primes': len(primes),
            'terminations_at_61': 0,
            'stabilizations_at_61': 0,
            'entropy_at_61': [],
            'special_cases': []
        }
        
        for p in primes:
            analysis = self.analyze_prime_at_limits(p)
            quantum_data = analysis['limit_analyses']['quantum']
            
            if quantum_data['terminates']:
                quantum_analysis['terminations_at_61'] += 1
            
            if quantum_data['is_stable']:
                quantum_analysis['stabilizations_at_61'] += 1
            
            quantum_analysis['entropy_at_61'].append(quantum_data['normalized_entropy'])
            
            # Check for special cases
            if p in [17, 19]:
                quantum_analysis['special_cases'].append({
                    'prime': p,
                    'entropy': quantum_data['normalized_entropy'],
                    'period': quantum_data['period'],
                    'notes': 'Generator prime - defines C*'
                })
        
        # Statistics
        quantum_analysis['termination_rate'] = quantum_analysis['terminations_at_61'] / len(primes) * 100
        quantum_analysis['stabilization_rate'] = quantum_analysis['stabilizations_at_61'] / len(primes) * 100
        quantum_analysis['average_entropy'] = statistics.mean(quantum_analysis['entropy_at_61'])
        quantum_analysis['entropy_variance'] = statistics.variance(quantum_analysis['entropy_at_61'])
        
        return quantum_analysis
    
    def analyze_17_19_at_extreme_precision(self) -> Dict:
        """Analyze 17/19 at extreme precision to study limits."""
        
        print("Analyzing 17/19 at extreme precision...")
        
        # Test at various precisions
        precisions = [100, 200, 500, 1000, 2000]
        
        extreme_analysis = {
            'fraction': '17/19',
            'exact_value': str(Fraction(17, 19)),
            'c_star_value': str(C_STAR),
            'precision_tests': [],
            'limit_behavior': {}
        }
        
        for precision in precisions:
            # Temporarily set precision
            getcontext().prec = precision + 10
            
            decimal_17_19 = Decimal(17) / Decimal(19)
            decimal_str = str(decimal_17_19)
            
            if '.' in decimal_str:
                decimal_str = decimal_str.split('.')[1][:precision]
            
            # Extract period
            period_start = decimal_str.find('894736')
            period = self._extract_period(decimal_str)
            
            precision_data = {
                'precision': precision,
                'decimal_expansion': decimal_str[:100] + '...' if len(decimal_str) > 100 else decimal_str,
                'period_detected': period,
                'entropy': self._calculate_entropy(decimal_str),
                'normalized_entropy': self._calculate_entropy(decimal_str) / math.log2(10)
            }
            
            extreme_analysis['precision_tests'].append(precision_data)
        
        # Reset precision
        getcontext().prec = 200
        
        # Analyze limit behavior
        entropies = [test['normalized_entropy'] for test in extreme_analysis['precision_tests']]
        extreme_analysis['limit_behavior'] = {
            'entropy_converges': len(set(round(e, 6) for e in entropies[-3:])) == 1,
            'final_entropy': entropies[-1] if entropies else 0,
            'entropy_stabilization_point': self._find_entropy_stabilization(extreme_analysis['precision_tests'])
        }
        
        return extreme_analysis
    
    def _extract_period(self, decimal_str: str) -> int:
        """Extract repeating period from decimal string."""
        if not decimal_str:
            return 0
        
        # Look for repeating pattern
        for period_length in range(1, min(50, len(decimal_str) // 2)):
            pattern = decimal_str[:period_length]
            
            # Check if pattern repeats
            repeats = True
            for i in range(period_length, len(decimal_str) - period_length, period_length):
                if decimal_str[i:i+period_length] != pattern:
                    repeats = False
                    break
            
            if repeats:
                return period_length
        
        return len(decimal_str)  # If no repetition found, assume entire length
    
    def _find_entropy_stabilization(self, precision_tests: List[Dict]) -> int:
        """Find where entropy stabilizes across precision tests."""
        entropies = [test['normalized_entropy'] for test in precision_tests]
        
        for i in range(1, len(entropies)):
            if abs(entropies[i] - entropies[i-1]) < 1e-6:
                return precision_tests[i]['precision']
        
        return precision_tests[-1]['precision'] if precision_tests else 0
    
    def analyze_composition_vs_limits(self, primes: List[int]) -> Dict:
        """Analyze relationship between composition strength and numerical limits."""
        
        composition_limit_analysis = {
            'correlations': {},
            'patterns': [],
            'boundary_insights': []
        }
        
        for p in primes[:50]:  # Analyze first 50 primes
            limits_data = self.analyze_prime_at_limits(p)
            
            # Calculate composition metrics
            composition_score = self._calculate_composition_at_limits(limits_data)
            
            pattern = {
                'prime': p,
                'composition_score': composition_score,
                'quantum_entropy': limits_data['limit_analyses']['quantum']['normalized_entropy'],
                'stabilization_point': self._find_stabilization_point(limits_data),
                'terminates_at_quantum': limits_data['limit_analyses']['quantum']['terminates']
            }
            
            composition_limit_analysis['patterns'].append(pattern)
        
        # Correlations
        quantum_entropies = [p['quantum_entropy'] for p in composition_limit_analysis['patterns']]
        composition_scores = [p['composition_score'] for p in composition_limit_analysis['patterns']]
        
        if len(quantum_entropies) > 1 and len(composition_scores) > 1:
            correlation = self._calculate_correlation(quantum_entropies, composition_scores)
            composition_limit_analysis['correlations']['entropy_composition'] = correlation
        
        # Boundary insights
        high_composition = [p for p in composition_limit_analysis['patterns'] if p['composition_score'] > 70]
        if high_composition:
            avg_stabilization = statistics.mean([p['stabilization_point'] for p in high_composition])
            composition_limit_analysis['boundary_insights'].append({
                'insight': 'High composition primes stabilize at',
                'value': avg_stabilization,
                'interpretation': 'digits on average'
            })
        
        return composition_limit_analysis
    
    def _calculate_composition_at_limits(self, limits_data: Dict) -> float:
        """Calculate composition score based on limit behavior."""
        score = 0
        
        # Quantum limit bonus
        quantum_data = limits_data['limit_analyses']['quantum']
        if quantum_data['is_stable']:
            score += 30
        if quantum_data['terminates']:
            score += 20
        
        # Entropy bonus
        entropy_values = [data['normalized_entropy'] for data in limits_data['limit_analyses'].values()]
        avg_entropy = sum(entropy_values) / len(entropy_values)
        score += avg_entropy * 40
        
        # Stability bonus
        stable_count = sum(1 for data in limits_data['limit_analyses'].values() if data['is_stable'])
        score += stable_count * 5
        
        return min(100, score)
    
    def _find_stabilization_point(self, limits_data: Dict) -> int:
        """Find where prime stabilizes across limits."""
        for limit_name, data in limits_data['limit_analyses'].items():
            if data['is_stable']:
                return data['digits']
        return 0
    
    def _calculate_correlation(self, x: List[float], y: List[float]) -> float:
        """Calculate correlation coefficient between two lists."""
        if len(x) != len(y) or len(x) < 2:
            return 0.0
        
        n = len(x)
        mean_x = sum(x) / n
        mean_y = sum(y) / n
        
        numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
        sum_xx = sum((x[i] - mean_x) ** 2 for i in range(n))
        sum_yy = sum((y[i] - mean_y) ** 2 for i in range(n))
        
        denominator = math.sqrt(sum_xx * sum_yy)
        
        return numerator / denominator if denominator != 0 else 0.0
    
    def analyze_primes_batch(self, primes: List[int]) -> Dict:
        """Comprehensive numerical limits analysis."""
        
        print(f"Analyzing numerical limits for {len(primes)} primes...")
        
        # Quantum limit hypothesis test
        quantum_analysis = self.analyze_quantum_limit_hypothesis(primes)
        
        # 17/19 extreme precision analysis
        extreme_precision = self.analyze_17_19_at_extreme_precision()
        
        # Composition vs limits correlation
        composition_limits = self.analyze_composition_vs_limits(primes)
        
        return {
            'quantum_limit_analysis': quantum_analysis,
            'extreme_precision_17_19': extreme_precision,
            'composition_limits_correlation': composition_limits,
            'summary': {
                'total_primes_tested': len(primes),
                'quantum_limit_termination_rate': quantum_analysis['termination_rate'],
                'quantum_limit_stabilization_rate': quantum_analysis['stabilization_rate'],
                'average_entropy_at_61': quantum_analysis['average_entropy']
            }
        }
    
    def export_results(self, results: Dict, filename: str = "numerical_limits_analysis.json"):
        """Export analysis results to JSON."""
        with open(filename, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"Numerical limits analysis saved to {filename}")

def main():
    """Main demonstration."""
    print("=" * 80)
    print("PRIME COMPOSITION TOOL #5: NUMERICAL LIMITS ANALYZER")
    print("Analyzing numerical boundaries and termination properties")
    print("=" * 80)
    
    # Initialize analyzer
    analyzer = NumericalLimitsAnalyzer()
    
    # Test primes
    test_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
    
    print(f"\nAnalyzing numerical limits for {len(test_primes)} primes...")
    
    # Comprehensive analysis
    results = analyzer.analyze_primes_batch(test_primes)
    
    # Display results
    print("\n🔍 QUANTUM LIMIT HYPOTHESIS (61 digits):")
    quantum = results['quantum_limit_analysis']
    print(f"  Termination rate: {quantum['termination_rate']:.1f}%")
    print(f"  Stabilization rate: {quantum['stabilization_rate']:.1f}%")
    print(f"  Average entropy at 61 digits: {quantum['average_entropy']:.4f}")
    
    print("\n🌟 17/19 EXTREME PRECISION ANALYSIS:")
    extreme = results['extreme_precision_17_19']
    print(f"  Entropy converges: {extreme['limit_behavior']['entropy_converges']}")
    print(f"  Final entropy: {extreme['limit_behavior']['final_entropy']:.6f}")
    print(f"  Stabilization point: {extreme['limit_behavior']['entropy_stabilization_point']} digits")
    
    print("\n📊 COMPOSITION vs LIMITS:")
    correlation = results['composition_limits_correlation']
    if 'entropy_composition' in correlation['correlations']:
        corr_value = correlation['correlations']['entropy_composition']
        print(f"  Entropy-Composition correlation: {corr_value:.3f}")
    
    for insight in correlation['boundary_insights']:
        print(f"  {insight['insight']}: {insight['value']:.1f} {insight['interpretation']}")
    
    # Export results
    analyzer.export_results(results)
    
    print("\n✅ Numerical limits analysis complete!")

if __name__ == "__main__":
    main()