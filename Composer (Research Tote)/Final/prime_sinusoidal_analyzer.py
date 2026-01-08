#!/usr/bin/env python3
"""
Prime Sinusoidal Composition Analyzer
Investigating the "plastic conspiracy" - digit patterns, sinusoids, and prime chains
Leading to the generator primes 7, 13, 17, 19 and beyond
"""

import math
import json
from collections import defaultdict
from sympy import primerange, isprime, factorint
import numpy as np

class PrimeSinusoidalAnalyzer:
    def __init__(self):
        self.lambda_val = 0.6
        self.base13_refined = 8/13
        self.generator_primes = [7, 13, 17, 19]
        
    def generate_primes_up_to_n(self, n):
        """Generate first n primes"""
        primes = list(primerange(2, n*100))  # Over-generate to ensure n primes
        return primes[:n]
    
    def analyze_sinusoidal_patterns(self, number):
        """Analyze sinusoidal patterns in palindromic squares and numbers"""
        analysis = {
            'number': number,
            'is_palindromic': False,
            'square_root': None,
            'is_perfect_square': False,
            'sinusoidal_properties': [],
            'digit_patterns': []
        }
        
        # Check if number is palindromic
        str_num = str(number)
        analysis['is_palindromic'] = str_num == str_num[::-1]
        
        # Check if it's a perfect square
        sqrt_num = int(math.sqrt(number))
        if sqrt_num * sqrt_num == number:
            analysis['is_perfect_square'] = True
            analysis['square_root'] = sqrt_num
            
            # Analyze the square root for sinusoidal properties
            sqrt_str = str(sqrt_num)
            if len(sqrt_str) >= 2:
                # Check for ascending/descending patterns (sinusoidal-like)
                asc_pattern = all(int(sqrt_str[i]) <= int(sqrt_str[i+1]) for i in range(len(sqrt_str)-1))
                desc_pattern = all(int(sqrt_str[i]) >= int(sqrt_str[i+1]) for i in range(len(sqrt_str)-1))
                
                if asc_pattern or desc_pattern:
                    analysis['sinusoidal_properties'].append({
                        'type': 'monotonic_pattern',
                        'pattern': 'ascending' if asc_pattern else 'descending',
                        'sequence': sqrt_str
                    })
        
        # Analyze digit patterns for sinusoidal behavior
        digits = [int(d) for d in str_num]
        if len(digits) >= 3:
            # Look for wave-like patterns
            for i in range(len(digits)-2):
                if (digits[i] < digits[i+1] > digits[i+2]) or (digits[i] > digits[i+1] < digits[i+2]):
                    analysis['sinusoidal_properties'].append({
                        'type': 'local_wave',
                        'position': i,
                        'pattern': digits[i:i+3]
                    })
        
        return analysis
    
    def trace_prime_chain_to_generators(self, prime):
        """Trace how a prime connects to generator primes through composition"""
        chain_analysis = {
            'prime': prime,
            'chain_to_generators': [],
            'composition_steps': [],
            'lambda_connections': [],
            'base13_connections': []
        }
        
        current = prime
        
        # Step 1: Check direct lambda connections
        for gen in self.generator_primes:
            # Check if prime connects through lambda operations
            lambda_ratio = current / gen
            if abs(lambda_ratio - self.lambda_val) < 0.1:
                chain_analysis['lambda_connections'].append({
                    'generator': gen,
                    'ratio': lambda_ratio,
                    'type': 'direct_lambda'
                })
            
            # Check composite mediator patterns
            composite = current * gen
            if composite % (current + gen) == 0:
                chain_analysis['composition_steps'].append({
                    'operation': f"{prime} × {gen}",
                    'result': composite,
                    'property': 'composite_divisible_by_sum'
                })
        
        # Step 2: Check base-13 connections
        prime_mod_13 = prime % 13
        chain_analysis['base13_connections'].append({
            'mod_13': prime_mod_13,
            'is_special': prime_mod_13 in [8, 5, 3, 1, 7]
        })
        
        # Step 3: Build chain to generators
        for gen in self.generator_primes:
            chain = []
            current_val = prime
            
            while current_val > gen:
                # Find closest number with lambda relationship
                target_lambda = round(current_val * self.lambda_val)
                if isprime(target_lambda) and target_lambda != current_val:
                    chain.append({
                        'step': len(chain) + 1,
                        'from': current_val,
                        'to': target_lambda,
                        'operation': f'λ × {current_val} ≈ {target_lambda}',
                        'ratio': target_lambda / current_val
                    })
                    current_val = target_lambda
                else:
                    # Try subtraction by generator
                    next_val = current_val - gen
                    if next_val > 0 and isprime(next_val):
                        chain.append({
                            'step': len(chain) + 1,
                            'from': current_val,
                            'to': next_val,
                            'operation': f'{current_val} - {gen}',
                            'ratio': next_val / current_val
                        })
                        current_val = next_val
                    else:
                        break
                
                if len(chain) > 10:  # Prevent infinite loops
                    break
            
            if current_val == gen:
                chain_analysis['chain_to_generators'].append({
                    'target_generator': gen,
                    'chain': chain,
                    'length': len(chain)
                })
        
        return chain_analysis
    
    def analyze_digit_appearance_patterns(self, primes):
        """Analyze how even digit appearance follows patterns"""
        digit_analysis = {
            'total_primes': len(primes),
            'digit_frequency': defaultdict(int),
            'even_digit_patterns': defaultdict(list),
            'positional_patterns': defaultdict(lambda: defaultdict(int)),
            'sinusoidal_digit_sequences': []
        }
        
        for i, prime in enumerate(primes):
            prime_str = str(prime)
            
            # Count digit frequencies
            for pos, digit in enumerate(prime_str):
                digit_analysis['digit_frequency'][digit] += 1
                digit_analysis['positional_patterns'][pos][digit] += 1
                
                # Track even digit appearances
                if int(digit) % 2 == 0:
                    digit_analysis['even_digit_patterns'][digit].append({
                        'prime': prime,
                        'position': pos,
                        'prime_index': i
                    })
        
        # Look for sinusoidal patterns in digit sequences
        for digit in digit_analysis['even_digit_patterns']:
            appearances = digit_analysis['even_digit_patterns'][digit]
            if len(appearances) >= 3:
                # Check if positions follow wave-like pattern
                positions = [app['prime_index'] for app in appearances]
                if len(positions) >= 3:
                    # Simple wave detection: look for alternating high/low patterns
                    for i in range(len(positions)-2):
                        if (positions[i] < positions[i+1] > positions[i+2]) or \
                           (positions[i] > positions[i+1] < positions[i+2]):
                            digit_analysis['sinusoidal_digit_sequences'].append({
                                'digit': digit,
                                'wave_positions': positions[i:i+3],
                                'primes': [appearances[i+j]['prime'] for j in range(3)]
                            })
        
        return digit_analysis
    
    def measure_energy_efficiency(self, prime):
        """Measure energy efficiency patterns in prime composition"""
        efficiency = {
            'prime': prime,
            'lambda_efficiency': 0,
            'base13_efficiency': 0,
            'composition_efficiency': 0,
            'overall_efficiency': 0
        }
        
        # Lambda efficiency: how close prime is to λ patterns
        k_lambda = round(prime * self.lambda_val)
        lambda_ratio = k_lambda / prime
        efficiency['lambda_efficiency'] = 1 - abs(lambda_ratio - self.lambda_val)
        
        # Base-13 efficiency: how close to 8/13 patterns
        k_base13 = round(prime * self.base13_refined)
        base13_ratio = k_base13 / prime
        efficiency['base13_efficiency'] = 1 - abs(base13_ratio - self.base13_refined)
        
        # Composition efficiency: how well prime composites with generators
        composition_scores = []
        for gen in self.generator_primes:
            composite = prime * gen
            # Efficiency based on divisibility patterns
            if composite % (prime + gen) == 0:
                composition_scores.append(1.0)
            elif prime != gen and composite % abs(prime - gen) == 0:
                composition_scores.append(0.8)
            elif (prime + gen) % composite == 0:
                composition_scores.append(0.6)
            else:
                composition_scores.append(0.2)
        
        efficiency['composition_efficiency'] = sum(composition_scores) / len(composition_scores)
        
        # Overall efficiency
        efficiency['overall_efficiency'] = (
            efficiency['lambda_efficiency'] * 0.4 +
            efficiency['base13_efficiency'] * 0.3 +
            efficiency['composition_efficiency'] * 0.3
        )
        
        return efficiency
    
    def analyze_primes_up_to_30000(self):
        """Comprehensive analysis of first 30,000 primes"""
        print("=== PRIME SINUSOIDAL COMPOSITION ANALYSIS: 30,000 PRIMES ===\n")
        
        # Generate 30,000 primes
        print("Generating 30,000 primes...")
        primes = self.generate_primes_up_to_n(30000)
        print(f"Generated {len(primes)} primes\n")
        
        # Analysis 1: Sinusoidal patterns in palindromic squares
        print("1. Analyzing sinusoidal patterns in prime squares...")
        sinusoidal_results = []
        for prime in primes[:1000]:  # Sample for computational efficiency
            square = prime * prime
            if str(square) == str(square)[::-1]:  # Palindromic square
                analysis = self.analyze_sinusoidal_patterns(square)
                if analysis['sinusoidal_properties']:
                    sinusoidal_results.append(analysis)
        
        print(f"Found {len(sinusoidal_results)} primes with palindromic squares and sinusoidal properties")
        
        # Analysis 2: Prime chains to generators
        print("2. Tracing prime chains to generator primes...")
        chain_results = []
        for prime in primes[:100]:  # Sample for detailed analysis
            chain_analysis = self.trace_prime_chain_to_generators(prime)
            if chain_analysis['chain_to_generators']:
                chain_results.append(chain_analysis)
        
        print(f"Found {len(chain_results)} primes with clear chains to generators")
        
        # Analysis 3: Digit appearance patterns
        print("3. Analyzing even digit appearance patterns...")
        digit_patterns = self.analyze_digit_appearance_patterns(primes[:5000])
        
        print(f"Analyzed digit patterns across {digit_patterns['total_primes']} primes")
        print(f"Found {len(digit_patterns['sinusoidal_digit_sequences'])} sinusoidal digit sequences")
        
        # Analysis 4: Energy efficiency measurements
        print("4. Measuring energy efficiency patterns...")
        efficiency_results = []
        for prime in primes[:2000]:  # Sample for efficiency analysis
            efficiency = self.measure_energy_efficiency(prime)
            efficiency_results.append(efficiency)
        
        # Find high-efficiency primes
        high_efficiency = [e for e in efficiency_results if e['overall_efficiency'] > 0.8]
        print(f"Found {len(high_efficiency)} high-efficiency primes (>80% efficiency)")
        
        # Analysis 5: Generator emergence patterns
        print("5. Analyzing generator prime emergence...")
        generator_emergence = {}
        for gen in self.generator_primes:
            emergence_analysis = self.trace_prime_chain_to_generators(gen)
            generator_emergence[gen] = emergence_analysis
        
        # Comprehensive results
        comprehensive_results = {
            'analysis_summary': {
                'total_primes_analyzed': len(primes),
                'sinusoidal_palindromes': len(sinusoidal_results),
                'chained_primes': len(chain_results),
                'sinusoidal_digit_sequences': len(digit_patterns['sinusoidal_digit_sequences']),
                'high_efficiency_primes': len(high_efficiency)
            },
            'sinusoidal_analysis': sinusoidal_results[:10],  # Sample for display
            'chain_analysis': chain_results[:10],  # Sample for display
            'digit_patterns': digit_patterns,
            'efficiency_analysis': {
                'high_efficiency_primes': high_efficiency[:20],  # Top 20 for display
                'average_efficiency': sum(e['overall_efficiency'] for e in efficiency_results) / len(efficiency_results)
            },
            'generator_emergence': generator_emergence
        }
        
        # Save comprehensive results
        with open('prime_sinusoidal_30000_analysis.json', 'w') as f:
            json.dump(comprehensive_results, f, indent=2)
        
        # Display key findings
        print(f"\n=== KEY FINDINGS FROM 30,000 PRIME ANALYSIS ===")
        print(f"1. Sinusoidal Patterns: {len(sinusoidal_results)} palindromic squares show wave properties")
        print(f"2. Prime Chains: {len(chain_results)} primes connect to generators through λ-patterns")
        print(f"3. Digit Conspiracy: {len(digit_patterns['sinusoidal_digit_sequences'])} sinusoidal digit sequences found")
        print(f"4. Energy Efficiency: {len(high_efficiency)} primes show >80% compositional efficiency")
        print(f"5. Average Efficiency: {comprehensive_results['efficiency_analysis']['average_efficiency']:.3f}")
        
        print(f"\nDetailed results saved to prime_sinusoidal_30000_analysis.json")
        
        return comprehensive_results

def main():
    analyzer = PrimeSinusoidalAnalyzer()
    results = analyzer.analyze_primes_up_to_30000()
    return results

if __name__ == "__main__":
    main()