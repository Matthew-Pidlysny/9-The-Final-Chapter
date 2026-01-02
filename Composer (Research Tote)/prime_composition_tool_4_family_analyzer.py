"""
PRIME COMPOSITION TOOL #4: FAMILY RELATIONSHIP ANALYZER
======================================================
Analyzes prime families and their composition patterns.

Features:
- Identifies twin, cousin, sexy, and other prime families
- Analyzes family composition through C*
- Maps family relationships to composition strength
- Studies inter-family patterns
- Identifies "super families" with strong composition
"""

import math
from fractions import Fraction
from decimal import Decimal, getcontext
import json
from typing import List, Dict, Tuple, Set
from collections import defaultdict

getcontext().prec = 100

# Constants
C_STAR = 17 / 19
POINT_SIX = 3 / 5

class PrimeFamilyAnalyzer:
    """Analyze prime families and their composition patterns."""
    
    def __init__(self):
        self.family_types = {
            'twin': 2,
            'cousin': 4,
            'sexy': 6,
            'prime_triplet': [2, 4],
            'prime_quadruplet': [2, 4, 6],
            'sexy_triplet': [6, 12],
            'sophie_germain': None,  # Special case
            'safe': None,  # Special case
            'palindromic': None,
            'emirp': None
        }
    
    def analyze_prime_families(self, p: int, primes_set: Set[int]) -> Dict:
        """Analyze all family relationships for prime p."""
        
        families = {}
        
        # Basic gap families
        families['twin'] = p + 2 in primes_set
        families['twin_lower'] = p - 2 in primes_set
        families['cousin'] = p + 4 in primes_set
        families['cousin_lower'] = p - 4 in primes_set
        families['sexy'] = p + 6 in primes_set
        families['sexy_lower'] = p - 6 in primes_set
        
        # Prime constellations
        families['prime_triplet'] = self._is_prime_triplet(p, primes_set)
        families['prime_quadruplet'] = self._is_prime_quadruplet(p, primes_set)
        families['sexy_triplet'] = self._is_sexy_triplet(p, primes_set)
        
        # Sophie Germain and Safe
        families['sophie_germain'] = (2 * p + 1) in primes_set
        families['safe'] = p > 2 and ((p - 1) // 2) in primes_set
        
        # Palindromic and Emirp
        p_str = str(p)
        families['palindromic'] = p_str == p_str[::-1]
        families['emirp'] = p_str != p_str[::-1] and int(p_str[::-1]) in primes_set
        
        # Count family memberships
        family_count = sum(1 for key, value in families.items() 
                          if isinstance(value, bool) and value)
        
        return {
            'prime': p,
            'families': families,
            'family_count': family_count,
            'family_memberships': [key for key, value in families.items() 
                                 if isinstance(value, bool) and value]
        }
    
    def _is_prime_triplet(self, p: int, primes_set: Set[int]) -> bool:
        """Check if p is part of a prime triplet (p, p+2, p+6 or p, p+4, p+6)."""
        return ((p + 2 in primes_set and p + 6 in primes_set) or
                (p - 2 in primes_set and p + 4 in primes_set) or
                (p - 4 in primes_set and p - 6 in primes_set))
    
    def _is_prime_quadruplet(self, p: int, primes_set: Set[int]) -> bool:
        """Check if p is part of a prime quadruplet (p, p+2, p+6, p+8)."""
        return (p + 2 in primes_set and p + 6 in primes_set and p + 8 in primes_set)
    
    def _is_sexy_triplet(self, p: int, primes_set: Set[int]) -> bool:
        """Check if p is part of a sexy triplet (p, p+6, p+12)."""
        return (p + 6 in primes_set and p + 12 in primes_set)
    
    def analyze_family_composition_patterns(self, family_groups: Dict) -> Dict:
        """Analyze C* composition patterns within prime families."""
        
        composition_patterns = {}
        
        for family_type, prime_groups in family_groups.items():
            if not prime_groups:
                continue
            
            family_analysis = {
                'family_type': family_type,
                'total_groups': len(prime_groups),
                'composition_scores': [],
                'average_score': 0,
                'high_composition_groups': [],
                'pattern_insights': []
            }
            
            total_score = 0
            for group in prime_groups:
                group_score = sum(p.get('composition_score', 0) for p in group) / len(group)
                family_analysis['composition_scores'].append(group_score)
                total_score += group_score
                
                # Identify high composition groups
                if group_score > 70:
                    family_analysis['high_composition_groups'].append({
                        'primes': [p['prime'] for p in group],
                        'score': group_score
                    })
            
            family_analysis['average_score'] = total_score / len(prime_groups) if prime_groups else 0
            
            # Pattern insights
            if family_analysis['average_score'] > 60:
                family_analysis['pattern_insights'].append(f"High composition tendency in {family_type} families")
            
            if len(family_analysis['high_composition_groups']) > 0:
                family_analysis['pattern_insights'].append(f"Found {len(family_analysis['high_composition_groups'])} exceptional {family_type} groups")
            
            composition_patterns[family_type] = family_analysis
        
        return composition_patterns
    
    def group_primes_by_families(self, primes: List[int], prime_analyses: List[Dict]) -> Dict:
        """Group primes by their family relationships."""
        
        primes_set = set(primes)
        family_groups = defaultdict(list)
        
        # Analyze family relationships for each prime
        prime_family_data = {}
        for i, p in enumerate(primes):
            family_data = self.analyze_prime_families(p, primes_set)
            prime_family_data[p] = family_data
            
            # Add composition analysis
            if i < len(prime_analyses):
                family_data['composition_score'] = prime_analyses[i].get('composition_score', 0)
        
        # Create groups for each family type
        for family_type in ['twin', 'cousin', 'sexy', 'prime_triplet', 'prime_quadruplet', 'sexy_triplet']:
            if family_type in ['twin', 'cousin', 'sexy']:
                self._create_gap_groups(prime_family_data, family_groups, family_type, primes_set)
            elif family_type in ['prime_triplet', 'prime_quadruplet', 'sexy_triplet']:
                self._create_constellation_groups(prime_family_data, family_groups, family_type, primes_set)
        
        return dict(family_groups), prime_family_data
    
    def _create_gap_groups(self, prime_family_data: Dict, family_groups: Dict, 
                          family_type: str, primes_set: Set[int]):
        """Create groups for gap-based families."""
        gap = self.family_types[family_type]
        
        for p, family_data in prime_family_data.items():
            if family_data['families'].get(family_type, False):
                partner = p + gap
                if partner in prime_family_data:
                    # Create group without duplication
                    group = sorted([p, partner])
                    group_key = tuple(group)
                    
                    if group_key not in [tuple(sorted([item['prime'] for item in g])) 
                                       for g in family_groups.get(family_type, [])]:
                        family_groups[family_type].append([
                            {'prime': p, 'composition_score': family_data.get('composition_score', 0)},
                            {'prime': partner, 'composition_score': prime_family_data[partner].get('composition_score', 0)}
                        ])
    
    def _create_constellation_groups(self, prime_family_data: Dict, family_groups: Dict,
                                   family_type: str, primes_set: Set[int]):
        """Create groups for constellation families."""
        for p, family_data in prime_family_data.items():
            if family_data['families'].get(family_type, False):
                if family_type == 'prime_triplet':
                    groups = self._find_prime_triplets(p, primes_set, prime_family_data)
                elif family_type == 'prime_quadruplet':
                    groups = self._find_prime_quadruplets(p, primes_set, prime_family_data)
                elif family_type == 'sexy_triplet':
                    groups = self._find_sexy_triplets(p, primes_set, prime_family_data)
                
                for group in groups:
                    family_groups[family_type].append(group)
    
    def _find_prime_triplets(self, p: int, primes_set: Set[int], prime_family_data: Dict) -> List[List[Dict]]:
        """Find prime triplets containing p."""
        groups = []
        
        # Check (p, p+2, p+6)
        if (p + 2 in primes_set and p + 6 in primes_set):
            groups.append([
                {'prime': p, 'composition_score': prime_family_data[p].get('composition_score', 0)},
                {'prime': p + 2, 'composition_score': prime_family_data[p + 2].get('composition_score', 0)},
                {'prime': p + 6, 'composition_score': prime_family_data[p + 6].get('composition_score', 0)}
            ])
        
        # Check (p-4, p-2, p)
        if (p - 4 in primes_set and p - 2 in primes_set):
            groups.append([
                {'prime': p - 4, 'composition_score': prime_family_data[p - 4].get('composition_score', 0)},
                {'prime': p - 2, 'composition_score': prime_family_data[p - 2].get('composition_score', 0)},
                {'prime': p, 'composition_score': prime_family_data[p].get('composition_score', 0)}
            ])
        
        return groups
    
    def _find_prime_quadruplets(self, p: int, primes_set: Set[int], prime_family_data: Dict) -> List[List[Dict]]:
        """Find prime quadruplets containing p."""
        groups = []
        
        # Check (p, p+2, p+6, p+8)
        if (p + 2 in primes_set and p + 6 in primes_set and p + 8 in primes_set):
            groups.append([
                {'prime': p, 'composition_score': prime_family_data[p].get('composition_score', 0)},
                {'prime': p + 2, 'composition_score': prime_family_data[p + 2].get('composition_score', 0)},
                {'prime': p + 6, 'composition_score': prime_family_data[p + 6].get('composition_score', 0)},
                {'prime': p + 8, 'composition_score': prime_family_data[p + 8].get('composition_score', 0)}
            ])
        
        return groups
    
    def _find_sexy_triplets(self, p: int, primes_set: Set[int], prime_family_data: Dict) -> List[List[Dict]]:
        """Find sexy triplets containing p."""
        groups = []
        
        # Check (p, p+6, p+12)
        if (p + 6 in primes_set and p + 12 in primes_set):
            groups.append([
                {'prime': p, 'composition_score': prime_family_data[p].get('composition_score', 0)},
                {'prime': p + 6, 'composition_score': prime_family_data[p + 6].get('composition_score', 0)},
                {'prime': p + 12, 'composition_score': prime_family_data[p + 12].get('composition_score', 0)}
            ])
        
        return groups
    
    def analyze_super_families(self, family_groups: Dict) -> Dict:
        """Identify 'super families' with exceptional composition."""
        
        super_families = {}
        
        for family_type, groups in family_groups.items():
            if not groups:
                continue
            
            # Calculate family metrics
            family_scores = []
            for group in groups:
                group_score = sum(p['composition_score'] for p in group) / len(group)
                family_scores.append(group_score)
            
            # Find exceptional families (score > 80)
            exceptional_families = []
            for i, group in enumerate(groups):
                if family_scores[i] > 80:
                    exceptional_families.append({
                        'members': [p['prime'] for p in group],
                        'individual_scores': [p['composition_score'] for p in group],
                        'average_score': family_scores[i],
                        'family_type': family_type
                    })
            
            super_families[family_type] = {
                'total_groups': len(groups),
                'average_family_score': sum(family_scores) / len(family_scores) if family_scores else 0,
                'exceptional_families': exceptional_families,
                'super_family_ratio': len(exceptional_families) / len(groups) * 100 if groups else 0
            }
        
        return super_families
    
    def analyze_family_evolution(self, primes: List[int]) -> Dict:
        """Analyze how family relationships evolve with prime size."""
        
        # Divide primes into segments
        segment_size = len(primes) // 5
        segments = [primes[i:i+segment_size] for i in range(0, len(primes), segment_size)]
        
        evolution_analysis = {
            'segments': [],
            'trends': {}
        }
        
        for i, segment in enumerate(segments):
            segment_primes_set = set(segment)
            
            # Count families in this segment
            family_counts = {
                'twin': 0,
                'cousin': 0,
                'sexy': 0,
                'prime_triplet': 0,
                'sophie_germain': 0,
                'safe': 0
            }
            
            for p in segment:
                families = self.analyze_prime_families(p, segment_primes_set)
                for family_type in family_counts:
                    if families['families'].get(family_type, False):
                        family_counts[family_type] += 1
            
            segment_data = {
                'segment': i + 1,
                'prime_range': f"{segment[0]}-{segment[-1]}",
                'family_counts': family_counts,
                'family_density': {k: v / len(segment) * 100 for k, v in family_counts.items()}
            }
            
            evolution_analysis['segments'].append(segment_data)
        
        # Analyze trends
        for family_type in family_counts:
            densities = [seg['family_density'][family_type] for seg in evolution_analysis['segments']]
            evolution_analysis['trends'][family_type] = {
                'initial': densities[0] if densities else 0,
                'final': densities[-1] if densities else 0,
                'change': (densities[-1] - densities[0]) if densities else 0,
                'trend': 'increasing' if densities and densities[-1] > densities[0] else 'decreasing' if densities else 'stable'
            }
        
        return evolution_analysis
    
    def analyze_primes_batch(self, primes: List[int], composition_analyses: List[Dict]) -> Dict:
        """Comprehensive family analysis of primes."""
        
        print(f"Analyzing family relationships for {len(primes)} primes...")
        
        # Group primes by families
        family_groups, prime_family_data = self.group_primes_by_families(primes, composition_analyses)
        
        # Analyze composition patterns
        composition_patterns = self.analyze_family_composition_patterns(family_groups)
        
        # Identify super families
        super_families = self.analyze_super_families(family_groups)
        
        # Analyze family evolution
        evolution_analysis = self.analyze_family_evolution(primes)
        
        return {
            'family_groups': {k: v[:10] for k, v in family_groups.items()},  # Limit to first 10 groups
            'composition_patterns': composition_patterns,
            'super_families': super_families,
            'family_evolution': evolution_analysis,
            'statistics': {
                'total_primes': len(primes),
                'family_types_analyzed': len(family_groups),
                'total_family_groups': sum(len(groups) for groups in family_groups.values())
            }
        }
    
    def export_results(self, results: Dict, filename: str = "prime_family_analysis.json"):
        """Export analysis results to JSON."""
        with open(filename, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"Prime family analysis saved to {filename}")

def main():
    """Main demonstration."""
    print("=" * 80)
    print("PRIME COMPOSITION TOOL #4: FAMILY RELATIONSHIP ANALYZER")
    print("Analyzing prime families and their composition patterns")
    print("=" * 80)
    
    # Initialize analyzer
    analyzer = PrimeFamilyAnalyzer()
    
    # Test primes
    test_primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]
    
    # Mock composition analyses for demonstration
    mock_composition = [{'prime': p, 'composition_score': 50 + (p % 50)} for p in test_primes]
    
    print(f"\nAnalyzing families for {len(test_primes)} primes...")
    
    # Comprehensive analysis
    results = analyzer.analyze_primes_batch(test_primes, mock_composition)
    
    # Display results
    print("\n🌟 SUPER FAMILIES (High Composition):")
    for family_type, data in results['super_families'].items():
        if data['exceptional_families']:
            print(f"\n{family_type.upper()} FAMILIES:")
            print(f"  Exceptional families: {len(data['exceptional_families'])}")
            print(f"  Super family ratio: {data['super_family_ratio']:.1f}%")
            for family in data['exceptional_families'][:3]:
                print(f"    {family['members']} - Score: {family['average_score']:.1f}")
    
    print("\n📊 FAMILY EVOLUTION TRENDS:")
    for family_type, trend in results['family_evolution']['trends'].items():
        print(f"  {family_type}: {trend['initial']:.1f}% → {trend['final']:.1f}% ({trend['trend']})")
    
    # Export results
    analyzer.export_results(results)
    
    print("\n✅ Prime family analysis complete!")

if __name__ == "__main__":
    main()