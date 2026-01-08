#!/usr/bin/env python3
"""
Enhanced Sinusoidal Pattern Tester
Deep investigation of the "plastic conspiracy" - digit waves, energy efficiency, and prime chains
"""

import math
import json
from collections import defaultdict
import numpy as np

class EnhancedSinusoidalTester:
    def __init__(self):
        self.lambda_val = 0.6
        self.base13_refined = 8/13
        self.generator_primes = [7, 13, 17, 19]
        
    def generate_primes(self, limit):
        """Generate primes up to limit using sieve"""
        sieve = [True] * (limit + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, int(math.sqrt(limit)) + 1):
            if sieve[i]:
                sieve[i*i::i] = [False] * len(sieve[i*i::i])
        return [i for i, is_prime in enumerate(sieve) if is_prime]
    
    def analyze_sinusoidal_waves(self, number):
        """Deep analysis of sinusoidal wave properties"""
        analysis = {
            'number': number,
            'wave_properties': {
                'amplitude': 0,
                'frequency': 0,
                'phase': 0,
                'wave_type': 'none'
            },
            'digit_waves': [],
            'palindromic_waves': []
        }
        
        digits = [int(d) for d in str(number)]
        
        if len(digits) < 3:
            return analysis
        
        # Convert digits to wave signal
        digit_signal = np.array(digits)
        
        # Simple wave analysis using FFT-like approach
        for window_size in range(3, min(len(digits), 10)):
            for i in range(len(digits) - window_size + 1):
                window = digits[i:i+window_size]
                
                # Check for sinusoidal patterns
                is_wave = False
                wave_type = 'none'
                
                # Peak-trough-peak pattern
                if len(window) >= 3:
                    if (window[0] < window[1] > window[2]) or (window[0] > window[1] < window[2]):
                        is_wave = True
                        wave_type = 'local_oscillation'
                
                # Symmetric pattern
                if window == window[::-1] and len(window) > 2:
                    is_wave = True
                    wave_type = 'symmetric'
                
                # Monotonic wave
                if all(window[i] <= window[i+1] for i in range(len(window)-1)) or \
                   all(window[i] >= window[i+1] for i in range(len(window)-1)):
                    is_wave = True
                    wave_type = 'monotonic'
                
                if is_wave:
                    # Calculate simple wave properties
                    amplitude = (max(window) - min(window)) / 2
                    center = (max(window) + min(window)) / 2
                    
                    analysis['digit_waves'].append({
                        'position': i,
                        'window_size': window_size,
                        'wave_type': wave_type,
                        'digits': window,
                        'amplitude': amplitude,
                        'center': center
                    })
        
        # Analyze palindromic properties for wave behavior
        if str(number) == str(number)[::-1]:
            # Find the center and analyze outward symmetry
            center_idx = len(digits) // 2
            left_wave = digits[:center_idx]
            right_wave = digits[-center_idx:] if len(digits) % 2 == 0 else digits[-center_idx+1:]
            
            if left_wave == right_wave[::-1]:
                analysis['palindromic_waves'].append({
                    'type': 'perfect_symmetry',
                    'center': center_idx,
                    'left_half': left_wave,
                    'right_half': right_wave
                })
        
        # Overall wave classification
        if analysis['digit_waves']:
            avg_amplitude = sum(w['amplitude'] for w in analysis['digit_waves']) / len(analysis['digit_waves'])
            analysis['wave_properties']['amplitude'] = avg_amplitude
            analysis['wave_properties']['wave_type'] = 'complex'
        
        return analysis
    
    def trace_lambda_gravity_chains(self, prime, max_depth=5):
        """Trace how λ acts as gravitational force pulling primes to generators"""
        chain = {
            'prime': prime,
            'lambda_gravity_chain': [],
            'generators_reached': [],
            'gravity_strength': []
        }
        
        current = prime
        visited = {current}
        
        for step in range(max_depth):
            # Find all primes that are λ-multiples of current
            lambda_targets = []
            for multiplier in [0.4, 0.5, 0.6, 0.7, 0.8]:  # Range around λ
                target = round(current * multiplier)
                if target > 1 and target != current and target not in visited:
                    if self.is_prime(target):
                        lambda_ratio = target / current
                        strength = 1 - abs(lambda_ratio - self.lambda_val)
                        lambda_targets.append({
                            'target': target,
                            'ratio': lambda_ratio,
                            'strength': strength,
                            'multiplier': multiplier
                        })
            
            if not lambda_targets:
                break
            
            # Choose strongest λ-connection
            best_target = max(lambda_targets, key=lambda x: x['strength'])
            
            chain['lambda_gravity_chain'].append({
                'step': step + 1,
                'from': current,
                'to': best_target['target'],
                'ratio': best_target['ratio'],
                'strength': best_target['strength'],
                'operation': f"λ × {current} ≈ {best_target['target']}"
            })
            
            chain['gravity_strength'].append(best_target['strength'])
            current = best_target['target']
            visited.add(current)
            
            # Check if we reached a generator
            if current in self.generator_primes:
                chain['generators_reached'].append(current)
                break
        
        return chain
    
    def analyze_even_digit_conspiracy(self, primes):
        """Deep analysis of even digit distribution patterns"""
        conspiracy = {
            'even_digit_frequencies': defaultdict(list),
            'positional_waves': defaultdict(lambda: defaultdict(list)),
            'wave_patterns': [],
            'conspiracy_strength': 0
        }
        
        for idx, prime in enumerate(primes):
            prime_str = str(prime)
            
            for pos, digit_char in enumerate(prime_str):
                digit = int(digit_char)
                
                if digit % 2 == 0:  # Even digit
                    conspiracy['even_digit_frequencies'][digit].append({
                        'prime': prime,
                        'position': pos,
                        'index': idx,
                        'value': digit
                    })
                    
                    conspiracy['positional_waves'][pos][digit].append(idx)
        
        # Look for wave patterns in even digit appearances
        for digit, appearances in conspiracy['even_digit_frequencies'].items():
            if len(appearances) >= 3:
                indices = [app['index'] for app in appearances]
                
                # Check for periodic patterns
                if len(indices) >= 4:
                    differences = [indices[i+1] - indices[i] for i in range(len(indices)-1)]
                    
                    # Look for consistent spacing (wave frequency)
                    if len(set(differences)) <= 2:  # Some regularity
                        avg_period = sum(differences) / len(differences)
                        conspiracy['wave_patterns'].append({
                            'digit': digit,
                            'type': 'periodic_appearance',
                            'period': avg_period,
                            'appearances': indices[:10],  # First 10 for display
                            'total_appearances': len(indices)
                        })
                
                # Check for wave-like patterns in spacing
                if len(indices) >= 5:
                    # Simple wave detection: look for alternating patterns
                    wave_detected = False
                    for i in range(len(indices)-3):
                        if (indices[i] < indices[i+1] > indices[i+2] < indices[i+3]) or \
                           (indices[i] > indices[i+1] < indices[i+2] > indices[i+3]):
                            wave_detected = True
                            break
                    
                    if wave_detected:
                        conspiracy['wave_patterns'].append({
                            'digit': digit,
                            'type': 'sinusoidal_spacing',
                            'wave_positions': indices[:10],
                            'total_appearances': len(indices)
                        })
        
        # Calculate conspiracy strength
        total_even_appearances = sum(len(apps) for apps in conspiracy['even_digit_frequencies'].values())
        wave_patterns_found = len(conspiracy['wave_patterns'])
        conspiracy['conspiracy_strength'] = wave_patterns_found / max(1, total_even_appearances / 100)
        
        return conspiracy
    
    def measure_composition_energy(self, prime):
        """Measure the "energy efficiency" of prime composition"""
        energy = {
            'prime': prime,
            'lambda_energy': 0,
            'base13_energy': 0,
            'generator_energy': 0,
            'sinusoidal_energy': 0,
            'total_energy': 0
        }
        
        # Lambda energy: closeness to λ patterns
        k_lambda = round(prime * self.lambda_val)
        lambda_ratio = k_lambda / prime
        energy['lambda_energy'] = 1 - abs(lambda_ratio - self.lambda_val)
        
        # Base-13 energy
        k_base13 = round(prime * self.base13_refined)
        base13_ratio = k_base13 / prime
        energy['base13_energy'] = 1 - abs(base13_ratio - self.base13_refined)
        
        # Generator energy: connections to generators
        generator_scores = []
        for gen in self.generator_primes:
            # Distance-based energy
            distance_ratio = min(prime, gen) / max(prime, gen)
            # Mod-based energy
            mod_energy = 1.0 if prime % gen in [1, gen-1] else 0.5
            generator_scores.append((distance_ratio + mod_energy) / 2)
        energy['generator_energy'] = sum(generator_scores) / len(generator_scores)
        
        # Sinusoidal energy from digit patterns
        wave_analysis = self.analyze_sinusoidal_waves(prime)
        if wave_analysis['digit_waves']:
            avg_amplitude = sum(w['amplitude'] for w in wave_analysis['digit_waves']) / len(wave_analysis['digit_waves'])
            energy['sinusoidal_energy'] = min(1.0, avg_amplitude / 4.5)  # Normalize by max possible amplitude
        
        # Total weighted energy
        energy['total_energy'] = (
            energy['lambda_energy'] * 0.3 +
            energy['base13_energy'] * 0.25 +
            energy['generator_energy'] * 0.25 +
            energy['sinusoidal_energy'] * 0.2
        )
        
        return energy
    
    def is_prime(self, n):
        """Simple primality test"""
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True
    
    def comprehensive_30000_analysis(self):
        """Complete analysis of the plastic conspiracy across 30,000 primes"""
        print("=== ENHANCED SINUSOIDAL CONSPIRACY ANALYSIS ===\n")
        
        # Generate 30,000 primes
        print("Generating 30,000 primes...")
        primes = self.generate_primes(350000)  # Overshoot to ensure 30,000 primes
        primes = primes[:30000]
        print(f"Generated {len(primes)} primes\n")
        
        # Analysis 1: Deep sinusoidal wave analysis
        print("1. Deep sinusoidal wave analysis...")
        sinusoidal_results = []
        for prime in primes[:5000]:  # Sample for computational efficiency
            wave_analysis = self.analyze_sinusoidal_waves(prime * prime)  # Analyze squares
            if wave_analysis['digit_waves'] or wave_analysis['palindromic_waves']:
                sinusoidal_results.append({
                    'prime': prime,
                    'square': prime * prime,
                    'wave_analysis': wave_analysis
                })
        
        print(f"Found {len(sinusoidal_results)} primes with sinusoidal square properties")
        
        # Analysis 2: Lambda gravity chains
        print("2. Tracing λ-gravity chains...")
        gravity_chains = []
        for prime in primes[:200]:  # Sample for detailed chain analysis
            chain = self.trace_lambda_gravity_chains(prime)
            if chain['generators_reached'] or len(chain['lambda_gravity_chain']) > 2:
                gravity_chains.append(chain)
        
        print(f"Found {len(gravity_chains)} primes with strong λ-gravity chains")
        
        # Analysis 3: Even digit conspiracy
        print("3. Analyzing even digit conspiracy...")
        digit_conspiracy = self.analyze_even_digit_conspiracy(primes[:10000])
        
        print(f"Conspiracy strength: {digit_conspiracy['conspiracy_strength']:.3f}")
        print(f"Wave patterns found: {len(digit_conspiracy['wave_patterns'])}")
        
        # Analysis 4: Composition energy measurement
        print("4. Measuring composition energy...")
        energy_results = []
        for prime in primes[:5000]:  # Sample for energy analysis
            energy = self.measure_composition_energy(prime)
            energy_results.append(energy)
        
        high_energy_primes = [e for e in energy_results if e['total_energy'] > 0.8]
        print(f"Found {len(high_energy_primes)} high-energy primes (>80% efficiency)")
        
        # Compile comprehensive results
        comprehensive_results = {
            'analysis_scope': {
                'total_primes': len(primes),
                'sinusoidal_sample': 5000,
                'gravity_chain_sample': 200,
                'digit_conspiracy_sample': 10000,
                'energy_sample': 5000
            },
            'sinusoidal_discoveries': {
                'total_sinusoidal_primes': len(sinusoidal_results),
                'examples': sinusoidal_results[:10],
                'wave_types': list(set(w['wave_analysis']['wave_properties']['wave_type'] 
                                     for w in sinusoidal_results if w['wave_analysis']['wave_properties']['wave_type'] != 'none'))
            },
            'lambda_gravity_network': {
                'total_chains': len(gravity_chains),
                'chains_to_generators': [c for c in gravity_chains if c['generators_reached']],
                'examples': gravity_chains[:15]
            },
            'digit_conspiracy_evidence': digit_conspiracy,
            'energy_distribution': {
                'high_energy_primes': len(high_energy_primes),
                'average_energy': sum(e['total_energy'] for e in energy_results) / len(energy_results),
                'top_energetic_primes': sorted(energy_results, key=lambda x: x['total_energy'], reverse=True)[:20]
            }
        }
        
        # Save results
        with open('enhanced_sinusoidal_conspiracy_30000.json', 'w') as f:
            json.dump(comprehensive_results, f, indent=2)
        
        # Display key findings
        print(f"\n=== PLASTIC CONSPIRACY REVEALED ===")
        print(f"🌊 Sinusoidal Primes: {comprehensive_results['sinusoidal_discoveries']['total_sinusoidal_primes']}")
        print(f"🔗 λ-Gravity Chains: {len(comprehensive_results['lambda_gravity_network']['chains_to_generators'])}")
        print(f"🎲 Conspiracy Strength: {comprehensive_results['digit_conspiracy_evidence']['conspiracy_strength']:.3f}")
        print(f"⚡ High-Energy Primes: {comprehensive_results['energy_distribution']['high_energy_primes']}")
        print(f"📊 Average Energy: {comprehensive_results['energy_distribution']['average_energy']:.3f}")
        
        print(f"\nDetailed conspiracy analysis saved to enhanced_sinusoidal_conspiracy_30000.json")
        
        return comprehensive_results

def main():
    tester = EnhancedSinusoidalTester()
    results = tester.comprehensive_30000_analysis()
    return results

if __name__ == "__main__":
    main()