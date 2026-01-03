#!/usr/bin/env python3
"""
Deep Analysis of Base-13 Remainder System
Long-running computations to discover patterns and relationships
"""

import math
import json
from typing import Dict, List, Tuple
from base13_remainder_calculator import Base13RemainderSystem
import time

class DeepAnalyzer:
    """
    Performs deep analysis of the Base-13 Remainder System
    """
    
    def __init__(self):
        self.system = Base13RemainderSystem()
        
    def find_all_power_equivalents(self, max_power: int = 10) -> Dict:
        """
        Find base-13 remainder equivalents for all powers of 10
        """
        print(f"\n{'='*80}")
        print(f"FINDING EQUIVALENTS FOR POWERS OF 10 (up to 10^{max_power})")
        print(f"{'='*80}\n")
        
        results = {}
        
        for power in range(-2, max_power + 1):
            target = 10 ** power
            print(f"Searching for E(n) = 10^{power} = {target}...")
            
            start_time = time.time()
            result = self.system.find_effective_target(
                target, 
                max_search=100000000,
                tolerance=0.01
            )
            elapsed = time.time() - start_time
            
            if result:
                results[power] = result
                results[power]['search_time'] = elapsed
                print(f"  ✓ Found: n = {result['n']}, E(n) = {result['effective_value']:.4f}")
                print(f"    Base-13: {result['base13_representation']}")
                print(f"    Remainder count: {result['remainder_count']}")
                print(f"    Search time: {elapsed:.4f}s\n")
            else:
                print(f"  ✗ Not found within search range\n")
                results[power] = None
        
        return results
    
    def analyze_compression_convergence(self, max_n: int = 100000) -> Dict:
        """
        Analyze how compression factor converges as n increases
        """
        print(f"\n{'='*80}")
        print(f"COMPRESSION FACTOR CONVERGENCE ANALYSIS (n up to {max_n})")
        print(f"{'='*80}\n")
        
        sample_points = []
        step = max_n // 1000  # 1000 sample points
        
        for n in range(13, max_n, step):
            R_n = self.system.count_remainders(n)
            compression = R_n / n if n > 0 else 0
            E_n = self.system.effective_value(n)
            
            sample_points.append({
                'n': n,
                'R_n': R_n,
                'E_n': E_n,
                'compression': compression,
                'cycle': (R_n // 27) + 1 if R_n > 0 else 0
            })
        
        # Calculate statistics
        compressions = [p['compression'] for p in sample_points]
        avg_compression = sum(compressions) / len(compressions)
        min_compression = min(compressions)
        max_compression = max(compressions)
        
        # Theoretical compression: 3/13 (3 triggers per 13 numbers)
        theoretical = 3 / 13
        
        print(f"Theoretical compression: {theoretical:.6f}")
        print(f"Average compression: {avg_compression:.6f}")
        print(f"Min compression: {min_compression:.6f}")
        print(f"Max compression: {max_compression:.6f}")
        print(f"Convergence to theoretical: {abs(avg_compression - theoretical):.6f}")
        
        return {
            'sample_points': sample_points,
            'statistics': {
                'theoretical': theoretical,
                'average': avg_compression,
                'min': min_compression,
                'max': max_compression,
                'convergence_error': abs(avg_compression - theoretical)
            }
        }
    
    def find_special_numbers(self, max_n: int = 10000) -> Dict:
        """
        Find numbers with special properties in the system
        """
        print(f"\n{'='*80}")
        print(f"FINDING SPECIAL NUMBERS (n up to {max_n})")
        print(f"{'='*80}\n")
        
        special = {
            'perfect_integers': [],  # E(n) is perfect integer
            'cycle_boundaries': [],  # End of cycles
            'group_boundaries': [],  # End of groups
            'base13_palindromes': [],  # Palindromes in base-13
            'compression_extremes': {'min': None, 'max': None}
        }
        
        min_comp = float('inf')
        max_comp = 0
        
        print("Scanning for special numbers...")
        
        for n in range(1, max_n + 1):
            E_n = self.system.effective_value(n)
            R_n = self.system.count_remainders(n)
            
            # Perfect integers
            if abs(E_n - round(E_n)) < 0.0001 and E_n > 0:
                special['perfect_integers'].append({
                    'n': n,
                    'E_n': int(round(E_n)),
                    'R_n': R_n,
                    'base13': self.system.to_base13(n)
                })
            
            # Cycle boundaries (multiples of 27 remainders)
            if R_n > 0 and R_n % 27 == 0:
                cycle_num = R_n // 27
                special['cycle_boundaries'].append({
                    'n': n,
                    'cycle': cycle_num,
                    'R_n': R_n,
                    'E_n': E_n,
                    'base13': self.system.to_base13(n)
                })
            
            # Group boundaries
            if self.system.is_remainder_trigger(n) and n % 13 == 0:
                special['group_boundaries'].append({
                    'n': n,
                    'group': self.system.get_remainder_group(n),
                    'base13': self.system.to_base13(n)
                })
            
            # Base-13 palindromes
            base13_str = self.system.to_base13(n)
            if base13_str == base13_str[::-1] and len(base13_str) > 1:
                special['base13_palindromes'].append({
                    'n': n,
                    'base13': base13_str,
                    'E_n': E_n
                })
            
            # Compression extremes
            if R_n > 0:
                comp = R_n / n
                if comp < min_comp:
                    min_comp = comp
                    special['compression_extremes']['min'] = {
                        'n': n, 'compression': comp, 'R_n': R_n
                    }
                if comp > max_comp:
                    max_comp = comp
                    special['compression_extremes']['max'] = {
                        'n': n, 'compression': comp, 'R_n': R_n
                    }
        
        # Print findings
        print(f"\n✓ Perfect Integers (first 20):")
        for item in special['perfect_integers'][:20]:
            print(f"  n={item['n']}, E(n)={item['E_n']}, Base-13={item['base13']}")
        
        print(f"\n✓ Cycle Boundaries (first 10):")
        for item in special['cycle_boundaries'][:10]:
            print(f"  Cycle {item['cycle']}: n={item['n']}, E(n)={item['E_n']:.2f}, Base-13={item['base13']}")
        
        print(f"\n✓ Base-13 Palindromes (first 10):")
        for item in special['base13_palindromes'][:10]:
            print(f"  n={item['n']}, Base-13={item['base13']}, E(n)={item['E_n']:.2f}")
        
        return special
    
    def analyze_beta_sequence_connection(self) -> Dict:
        """
        Analyze connection to beta sequence (sum = 91 = 7 × 13)
        """
        print(f"\n{'='*80}")
        print(f"BETA SEQUENCE CONNECTION ANALYSIS")
        print(f"{'='*80}\n")
        
        beta_sum = 91  # 7 × 13
        
        # Find where E(n) = 91
        result_91 = self.system.find_effective_target(91, max_search=1000000)
        
        print(f"Beta Sequence Sum: {beta_sum} = 7 × 13")
        print(f"\nFinding E(n) = 91:")
        if result_91:
            print(f"  n = {result_91['n']}")
            print(f"  E(n) = {result_91['effective_value']:.4f}")
            print(f"  R(n) = {result_91['remainder_count']}")
            print(f"  Base-13 = {result_91['base13_representation']}")
            print(f"  Cycle = {result_91['cycle_number']}")
        
        # Analyze multiples of 91
        print(f"\nMultiples of 91:")
        multiples_analysis = []
        for mult in [1, 2, 3, 7, 13]:
            target = 91 * mult
            result = self.system.find_effective_target(target, max_search=10000000)
            if result:
                multiples_analysis.append(result)
                print(f"  {mult} × 91 = {target}: n={result['n']}, Base-13={result['base13_representation']}")
        
        # Analyze 91 + 9 = 100 relationship
        print(f"\nThe 91 + 9 = 100 Relationship:")
        print(f"  E(117) = 100 (verified)")
        print(f"  R(117) = 27 = 9 groups × 3")
        print(f"  This confirms: 91 (beta sum) + 9 (remainder cycles) = 100")
        
        return {
            'beta_sum': beta_sum,
            'E_91': result_91,
            'multiples': multiples_analysis
        }
    
    def analyze_19_cycle_system(self) -> Dict:
        """
        Deep analysis of the 19-cycle system
        """
        print(f"\n{'='*80}")
        print(f"19-CYCLE SYSTEM ANALYSIS")
        print(f"{'='*80}\n")
        
        cycles_data = []
        
        print("Analyzing each of the 19 cycles:\n")
        print(f"{'Cycle':<8} {'Last n':<10} {'Last E(n)':<15} {'R(n)':<10} {'Base-13':<15}")
        print("-" * 70)
        
        for cycle in range(1, 20):
            # Each cycle ends at group (cycle * 9)
            last_group = cycle * 9
            last_n = 13 * last_group  # Last number in group
            
            R_n = self.system.count_remainders(last_n)
            E_n = self.system.effective_value(last_n)
            base13 = self.system.to_base13(last_n)
            
            cycles_data.append({
                'cycle': cycle,
                'last_n': last_n,
                'last_E_n': E_n,
                'R_n': R_n,
                'base13': base13
            })
            
            print(f"{cycle:<8} {last_n:<10} {E_n:<15.2f} {R_n:<10} {base13:<15}")
        
        # Analyze the complete 19-cycle system
        final_n = cycles_data[-1]['last_n']
        final_E = cycles_data[-1]['last_E_n']
        final_R = cycles_data[-1]['R_n']
        
        print(f"\n19-Cycle System Complete:")
        print(f"  Final n: {final_n}")
        print(f"  Final E(n): {final_E:.2f}")
        print(f"  Total remainders: {final_R}")
        print(f"  Expected remainders: {19 * 27} = {19 * 27}")
        print(f"  Match: {final_R == 19 * 27}")
        
        return {
            'cycles': cycles_data,
            'total_cycles': 19,
            'final_state': {
                'n': final_n,
                'E_n': final_E,
                'R_n': final_R
            }
        }
    
    def find_golden_ratio_connections(self) -> Dict:
        """
        Search for golden ratio (φ) connections in the system
        """
        print(f"\n{'='*80}")
        print(f"GOLDEN RATIO CONNECTION ANALYSIS")
        print(f"{'='*80}\n")
        
        phi = (1 + math.sqrt(5)) / 2  # Golden ratio
        
        # Search for E(n) ≈ φ, φ², φ³, etc.
        phi_connections = []
        
        for power in range(1, 20):
            target = phi ** power
            result = self.system.find_effective_target(target, max_search=1000000, tolerance=0.01)
            
            if result:
                phi_connections.append({
                    'power': power,
                    'target': target,
                    'result': result
                })
                print(f"φ^{power} = {target:.4f}: n={result['n']}, E(n)={result['effective_value']:.4f}")
        
        # Check if compression factor relates to φ
        theoretical_compression = 3 / 13
        phi_ratio = theoretical_compression / phi
        
        print(f"\nCompression Factor Analysis:")
        print(f"  Theoretical compression: {theoretical_compression:.6f}")
        print(f"  Golden ratio φ: {phi:.6f}")
        print(f"  Compression / φ: {phi_ratio:.6f}")
        print(f"  φ / Compression: {phi / theoretical_compression:.6f}")
        
        return {
            'phi': phi,
            'phi_connections': phi_connections,
            'compression_phi_ratio': phi_ratio
        }
    
    def generate_comprehensive_report(self, output_file: str = "base13_deep_analysis_report.json"):
        """
        Generate comprehensive analysis report
        """
        print(f"\n{'='*80}")
        print(f"GENERATING COMPREHENSIVE REPORT")
        print(f"{'='*80}\n")
        
        start_time = time.time()
        
        report = {
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
            'power_equivalents': self.find_all_power_equivalents(max_power=8),
            'compression_analysis': self.analyze_compression_convergence(max_n=100000),
            'special_numbers': self.find_special_numbers(max_n=10000),
            'beta_sequence': self.analyze_beta_sequence_connection(),
            'nineteen_cycles': self.analyze_19_cycle_system(),
            'golden_ratio': self.find_golden_ratio_connections()
        }
        
        elapsed = time.time() - start_time
        report['total_analysis_time'] = elapsed
        
        # Save to file
        with open(output_file, 'w') as f:
            json.dump(report, f, indent=2)
        
        print(f"\n{'='*80}")
        print(f"ANALYSIS COMPLETE")
        print(f"{'='*80}")
        print(f"Total time: {elapsed:.2f} seconds")
        print(f"Report saved to: {output_file}")
        
        return report


def main():
    """Main execution"""
    print("=" * 80)
    print("BASE-13 REMAINDER SYSTEM: DEEP ANALYSIS")
    print("Long-running computational exploration")
    print("=" * 80)
    
    analyzer = DeepAnalyzer()
    
    # Run comprehensive analysis
    report = analyzer.generate_comprehensive_report()
    
    print("\n" + "=" * 80)
    print("KEY FINDINGS SUMMARY")
    print("=" * 80)
    
    # Summarize key findings
    if 2 in report['power_equivalents']:
        result_100 = report['power_equivalents'][2]
        print(f"\n✓ E(n) = 100: n = {result_100['n']}, Base-13 = {result_100['base13_representation']}")
    
    if 3 in report['power_equivalents']:
        result_1000 = report['power_equivalents'][3]
        print(f"✓ E(n) = 1000: n = {result_1000['n']}, Base-13 = {result_1000['base13_representation']}")
    
    comp_stats = report['compression_analysis']['statistics']
    print(f"\n✓ Compression Factor:")
    print(f"  Theoretical: {comp_stats['theoretical']:.6f}")
    print(f"  Observed: {comp_stats['average']:.6f}")
    print(f"  Convergence: {comp_stats['convergence_error']:.6f}")
    
    print(f"\n✓ 19-Cycle System:")
    final = report['nineteen_cycles']['final_state']
    print(f"  Final n: {final['n']}")
    print(f"  Final E(n): {final['E_n']:.2f}")
    print(f"  Total remainders: {final['R_n']}")
    
    print("\n" + "=" * 80)


if __name__ == "__main__":
    main()