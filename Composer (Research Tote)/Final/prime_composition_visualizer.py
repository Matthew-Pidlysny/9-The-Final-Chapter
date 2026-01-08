#!/usr/bin/env python3
"""
Prime Composition Visualizer
Visualizing the "plastic conspiracy" - digit waves, energy flows, and prime networks
"""

import math
import json
from collections import defaultdict
import numpy as np

class PrimeCompositionVisualizer:
    def __init__(self):
        self.lambda_val = 0.6
        self.base13_refined = 8/13
        self.generator_primes = [7, 13, 17, 19]
        
    def generate_primes(self, limit):
        """Generate primes up to limit"""
        sieve = [True] * (limit + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, int(math.sqrt(limit)) + 1):
            if sieve[i]:
                sieve[i*i::i] = [False] * len(sieve[i*i::i])
        return [i for i, is_prime in enumerate(sieve) if is_prime]
    
    def visualize_digit_wave_pattern(self, number):
        """Create visual representation of digit wave patterns"""
        digits = [int(d) for d in str(number)]
        
        visualization = {
            'number': number,
            'digits': digits,
            'wave_graph': [],
            'energy_peaks': [],
            'wave_signature': ''
        }
        
        # Create wave graph
        for i, digit in enumerate(digits):
            # Calculate local wave energy
            if i == 0 or i == len(digits) - 1:
                local_energy = digit
            else:
                # Wave energy based on position in sequence
                prev_digit = digits[i-1]
                next_digit = digits[i+1]
                
                # Oscillation detection
                if (prev_digit < digit > next_digit) or (prev_digit > digit < next_digit):
                    local_energy = digit * 1.5  # Boost for wave peaks/troughs
                elif prev_digit < digit < next_digit or prev_digit > digit > next_digit:
                    local_energy = digit * 1.2  # Moderate boost for monotonic
                else:
                    local_energy = digit
            
            visualization['wave_graph'].append(local_energy)
            
            # Mark energy peaks
            if local_energy > digit * 1.3:
                visualization['energy_peaks'].append({
                    'position': i,
                    'digit': digit,
                    'energy': local_energy,
                    'type': 'peak' if local_energy > digit * 1.4 else 'wave'
                })
        
        # Create wave signature string
        for i in range(len(digits)-1):
            if digits[i] < digits[i+1]:
                visualization['wave_signature'] += '/'
            elif digits[i] > digits[i+1]:
                visualization['wave_signature'] += '\\'
            else:
                visualization['wave_signature'] += '='
        
        return visualization
    
    def map_lambda_energy_landscape(self, primes):
        """Map the λ-energy landscape across prime sequences"""
        landscape = {
            'prime_positions': [],
            'lambda_energy_levels': [],
            'energy_valleys': [],
            'energy_peaks': [],
            'flow_directions': []
        }
        
        for i, prime in enumerate(primes[:1000]):  # Sample for visualization
            # Calculate λ-energy
            k_lambda = round(prime * self.lambda_val)
            lambda_ratio = k_lambda / prime
            lambda_energy = 1 - abs(lambda_ratio - self.lambda_val)
            
            landscape['prime_positions'].append(i)
            landscape['lambda_energy_levels'].append(lambda_energy)
            
            # Mark energy valleys (low λ-energy)
            if lambda_energy < 0.5:
                landscape['energy_valleys'].append({
                    'position': i,
                    'prime': prime,
                    'energy': lambda_energy,
                    'type': 'valley'
                })
            
            # Mark energy peaks (high λ-energy)
            if lambda_energy > 0.95:
                landscape['energy_peaks'].append({
                    'position': i,
                    'prime': prime,
                    'energy': lambda_energy,
                    'type': 'peak'
                })
            
            # Determine flow direction (toward generators)
            min_distance_to_generator = min(abs(prime - gen) for gen in self.generator_primes)
            flow_strength = 1 / (1 + min_distance_to_generator / 100)
            landscape['flow_directions'].append(flow_strength)
        
        return landscape
    
    def trace_prime_evolution_chains(self, start_prime, max_generations=5):
        """Trace evolutionary chains showing how primes connect and evolve"""
        evolution = {
            'start_prime': start_prime,
            'evolution_chain': [],
            'mutation_points': [],
            'convergence_targets': []
        }
        
        current = start_prime
        for generation in range(max_generations):
            # Find next evolutionary step
            candidates = []
            
            # λ-based evolution
            for multiplier in [0.4, 0.5, 0.6, 0.7, 0.8]:
                target = round(current * multiplier)
                if target > 1 and target != current and self.is_prime(target):
                    lambda_strength = 1 - abs((target/current) - self.lambda_val)
                    candidates.append({
                        'target': target,
                        'method': 'lambda_evolution',
                        'strength': lambda_strength,
                        'description': f"λ × {current} → {target}"
                    })
            
            # Generator-based evolution
            for gen in self.generator_primes:
                # Composite evolution
                composite = current + gen
                if self.is_prime(composite):
                    candidates.append({
                        'target': composite,
                        'method': 'generator_addition',
                        'strength': 0.7,
                        'description': f"{current} + {gen} → {composite}"
                    })
                
                # Differential evolution
                diff = abs(current - gen)
                if diff > 1 and self.is_prime(diff):
                    candidates.append({
                        'target': diff,
                        'method': 'generator_differential',
                        'strength': 0.6,
                        'description': f"|{current} - {gen}| → {diff}"
                    })
            
            if not candidates:
                break
            
            # Choose strongest evolutionary step
            best_candidate = max(candidates, key=lambda x: x['strength'])
            
            evolution['evolution_chain'].append({
                'generation': generation + 1,
                'from': current,
                'to': best_candidate['target'],
                'method': best_candidate['method'],
                'strength': best_candidate['strength'],
                'description': best_candidate['description']
            })
            
            # Check for mutation points (significant jumps)
            if abs(best_candidate['target'] - current) > current * 0.3:
                evolution['mutation_points'].append({
                    'generation': generation + 1,
                    'jump_size': abs(best_candidate['target'] - current),
                    'mutation_type': best_candidate['method']
                })
            
            # Check if converged to generator
            if best_candidate['target'] in self.generator_primes:
                evolution['convergence_targets'].append(best_candidate['target'])
                break
            
            current = best_candidate['target']
        
        return evolution
    
    def analyze_composition_network(self, primes):
        """Analyze the overall composition network structure"""
        network = {
            'nodes': [],
            'edges': [],
            'clusters': {},
            'central_hubs': [],
            'energy_flows': []
        }
        
        # Create nodes for high-energy primes
        for prime in primes[:2000]:
            # Calculate comprehensive energy
            k_lambda = round(prime * self.lambda_val)
            lambda_energy = 1 - abs((k_lambda/prime) - self.lambda_val)
            
            k_base13 = round(prime * self.base13_refined)
            base13_energy = 1 - abs((k_base13/prime) - self.base13_refined)
            
            total_energy = (lambda_energy * 0.6 + base13_energy * 0.4)
            
            if total_energy > 0.85:  # High-energy threshold
                network['nodes'].append({
                    'id': prime,
                    'energy': total_energy,
                    'type': 'generator' if prime in self.generator_primes else 'high_energy',
                    'connections': 0
                })
        
        # Create edges based on λ-relationships
        for i, node1 in enumerate(network['nodes']):
            for node2 in network['nodes'][i+1:]:
                # Check for λ-relationship
                ratio = min(node1['id'], node2['id']) / max(node1['id'], node2['id'])
                if abs(ratio - self.lambda_val) < 0.1:
                    network['edges'].append({
                        'from': node1['id'],
                        'to': node2['id'],
                        'type': 'lambda_connection',
                        'strength': 1 - abs(ratio - self.lambda_val)
                    })
        
        # Identify clusters and hubs
        connection_counts = defaultdict(int)
        for edge in network['edges']:
            connection_counts[edge['from']] += 1
            connection_counts[edge['to']] += 1
        
        # Update node connections
        for node in network['nodes']:
            node['connections'] = connection_counts[node['id']]
        
        # Find central hubs (highly connected nodes)
        network['central_hubs'] = sorted(
            [n for n in network['nodes'] if n['connections'] > 3],
            key=lambda x: x['connections'],
            reverse=True
        )
        
        return network
    
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
    
    def generate_comprehensive_visualization(self):
        """Generate complete visualization of the plastic conspiracy"""
        print("=== PRIME COMPOSITION VISUALIZATION SYSTEM ===\n")
        
        # Generate prime dataset
        print("Generating prime dataset...")
        primes = self.generate_primes(40000)
        primes = primes[:30000]  # Use 30,000 primes
        print(f"Generated {len(primes)} primes for visualization\n")
        
        # Visualization 1: Digit Wave Patterns
        print("1. Creating digit wave visualizations...")
        wave_visualizations = []
        
        # Sample primes for wave analysis
        wave_samples = [11, 13, 17, 19, 37, 41, 43, 101, 103, 107]
        for prime in wave_samples:
            if prime in primes:
                # Analyze the prime itself
                prime_wave = self.visualize_digit_wave_pattern(prime)
                wave_visualizations.append({
                    'type': 'prime_wave',
                    'number': prime,
                    'visualization': prime_wave
                })
                
                # Analyze its square
                square = prime * prime
                square_wave = self.visualize_digit_wave_pattern(square)
                wave_visualizations.append({
                    'type': 'square_wave',
                    'number': square,
                    'root_prime': prime,
                    'visualization': square_wave
                })
        
        print(f"Created {len(wave_visualizations)} wave visualizations")
        
        # Visualization 2: λ-Energy Landscape
        print("2. Mapping λ-energy landscape...")
        energy_landscape = self.map_lambda_energy_landscape(primes)
        
        print(f"Mapped landscape with {len(energy_landscape['energy_peaks'])} peaks and {len(energy_landscape['energy_valleys'])} valleys")
        
        # Visualization 3: Evolution Chains
        print("3. Tracing prime evolution chains...")
        evolution_chains = []
        
        # Trace chains from various starting points
        sample_primes = [23, 29, 31, 37, 41, 43, 47, 53, 59, 61]
        for prime in sample_primes:
            if prime in primes:
                chain = self.trace_prime_evolution_chains(prime)
                if len(chain['evolution_chain']) > 1:
                    evolution_chains.append(chain)
        
        print(f"Traced {len(evolution_chains)} evolution chains")
        
        # Visualization 4: Composition Network
        print("4. Building composition network...")
        composition_network = self.analyze_composition_network(primes)
        
        print(f"Built network with {len(composition_network['nodes'])} nodes and {len(composition_network['edges'])} edges")
        print(f"Identified {len(composition_network['central_hubs'])} central hubs")
        
        # Compile comprehensive visualization
        comprehensive_viz = {
            'metadata': {
                'total_primes': len(primes),
                'visualization_types': ['digit_waves', 'energy_landscape', 'evolution_chains', 'composition_network'],
                'lambda_constant': self.lambda_val,
                'base13_constant': self.base13_refined
            },
            'digit_waves': {
                'total_visualizations': len(wave_visualizations),
                'examples': wave_visualizations[:8],  # First 8 for display
                'wave_types': list(set(viz['visualization']['wave_signature'] for viz in wave_visualizations))
            },
            'energy_landscape': energy_landscape,
            'evolution_chains': {
                'total_chains': len(evolution_chains),
                'examples': evolution_chains[:10],  # First 10 for display
                'convergence_rate': len([c for c in evolution_chains if c['convergence_targets']]) / len(evolution_chains)
            },
            'composition_network': {
                'network_stats': {
                    'nodes': len(composition_network['nodes']),
                    'edges': len(composition_network['edges']),
                    'hubs': len(composition_network['central_hubs'])
                },
                'top_hubs': composition_network['central_hubs'][:10]
            }
        }
        
        # Save comprehensive visualization
        with open('prime_composition_visualization.json', 'w') as f:
            json.dump(comprehensive_viz, f, indent=2)
        
        # Display key findings
        print(f"\n=== VISUALIZATION INSIGHTS ===")
        print(f"🌊 Wave Patterns: {len(wave_visualizations)} visualizations showing digit oscillations")
        print(f"⚡ Energy Landscape: {len(energy_landscape['energy_peaks'])} high-energy peaks, {len(energy_landscape['energy_valleys'])} valleys")
        print(f"🔗 Evolution Chains: {comprehensive_viz['evolution_chains']['convergence_rate']:.1%} converge to generators")
        print(f"🕸️ Network Hubs: {len(composition_network['central_hubs'])} highly connected primes discovered")
        
        # Show examples
        print(f"\n=== WAVE SIGNATURE EXAMPLES ===")
        for viz in wave_visualizations[:6]:
            if viz['type'] == 'square_wave':
                print(f"Prime {viz['root_prime']}² = {viz['number']}: {viz['visualization']['wave_signature']}")
        
        print(f"\n=== TOP CENTRAL HUBS ===")
        for hub in comprehensive_viz['composition_network']['top_hubs'][:5]:
            print(f"Prime {hub['id']}: {hub['connections']} connections, {hub['energy']:.3f} energy")
        
        print(f"\nComplete visualization saved to prime_composition_visualization.json")
        
        return comprehensive_viz

def main():
    visualizer = PrimeCompositionVisualizer()
    results = visualizer.generate_comprehensive_visualization()
    return results

if __name__ == "__main__":
    main()