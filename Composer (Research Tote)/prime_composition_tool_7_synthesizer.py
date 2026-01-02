"""
PRIME COMPOSITION TOOL #7: UNIFIED COMPOSITION SYNTHESIZER
=======================================================
Synthesizes all composition analyses into unified theory.

Features:
- Integrates all 6 analysis tools
- Generates unified composition scores
- Identifies "master primes" with exceptional composition
- Creates composition formulas
- Provides comprehensive synthesis report
"""

import math
from fractions import Fraction
from decimal import Decimal, getcontext
import json
from typing import List, Dict, Tuple, Any
from collections import defaultdict
import statistics

getcontext().prec = 100

# Constants
C_STAR = 17 / 19
POINT_SIX = 3 / 5
PHI = (1 + math.sqrt(5)) / 2

class UnifiedCompositionSynthesizer:
    """Synthesizes all prime composition analyses."""
    
    def __init__(self):
        self.analysis_weights = {
            'reciprocal_space': 0.20,
            'c_star_composition': 0.25,
            'hardness_entropy': 0.20,
            'family_relationships': 0.15,
            'numerical_limits': 0.10,
            'pattern_detection': 0.10
        }
        self.master_threshold = 85
    
    def synthesize_prime_composition(self, prime_analyses: List[Dict]) -> Dict:
        """Synthesize all analyses into unified composition score."""
        
        synthesized_primes = []
        
        for analysis in prime_analyses:
            p = analysis['prime']
            
            # Extract individual scores
            scores = {
                'reciprocal_score': analysis.get('reciprocal_space', {}).get('composition_score', 0),
                'c_star_score': analysis.get('c_star_composition', {}).get('composition_score', 0),
                'hardness_score': analysis.get('hardness_analysis', {}).get('quantum_hardness', 0) * 100,
                'family_score': analysis.get('family_analysis', {}).get('family_count', 0) * 10,
                'limits_score': analysis.get('limits_analysis', {}).get('composition_score', 0),
                'pattern_score': analysis.get('pattern_analysis', {}).get('composition_score', 0)
            }
            
            # Calculate unified composition score
            unified_score = 0
            for score_type, score_value in scores.items():
                weight = self.analysis_weights.get(score_type.replace('_score', ''), 0)
                unified_score += score_value * weight
            
            # Determine composition class
            composition_class = self._classify_composition(unified_score)
            
            # Identify exceptional properties
            exceptional_properties = self._identify_exceptional_properties(analysis, scores)
            
            synthesized = {
                'prime': p,
                'individual_scores': scores,
                'unified_composition_score': unified_score,
                'composition_class': composition_class,
                'exceptional_properties': exceptional_properties,
                'synthesis_insights': self._generate_insights(analysis, unified_score)
            }
            
            synthesized_primes.append(synthesized)
        
        return synthesized_primes
    
    def _classify_composition(self, score: float) -> str:
        """Classify composition level."""
        if score >= 95:
            return "master_prime"
        elif score >= 85:
            return "exceptional"
        elif score >= 70:
            return "strong"
        elif score >= 50:
            return "moderate"
        elif score >= 30:
            return "weak"
        else:
            return "minimal"
    
    def _identify_exceptional_properties(self, analysis: Dict, scores: Dict) -> List[str]:
        """Identify exceptional properties of a prime."""
        properties = []
        
        p = analysis['prime']
        
        # Generator primes
        if p in [17, 19]:
            properties.append("C*_generator")
        
        # High C* relationship
        if scores.get('c_star_score', 0) > 80:
            properties.append("strong_C*_relationship")
        
        # Maximal hardness
        if scores.get('hardness_score', 0) > 95:
            properties.append("maximal_hardness")
        
        # Rich family structure
        if scores.get('family_score', 0) > 30:
            properties.append("rich_family_structure")
        
        # Exceptional reciprocal space
        if scores.get('reciprocal_score', 0) > 80:
            properties.append("exceptional_reciprocal_space")
        
        # Strong patterns
        if scores.get('pattern_score', 0) > 80:
            properties.append("strong_patterns")
        
        # Numerical stability
        if scores.get('limits_score', 0) > 80:
            properties.append("numerical_stability")
        
        return properties
    
    def _generate_insights(self, analysis: Dict, unified_score: float) -> List[str]:
        """Generate insights about prime composition."""
        insights = []
        
        p = analysis['prime']
        
        if unified_score >= 90:
            insights.append(f"Prime {p} exhibits exceptional composition across all analysis dimensions")
        
        if unified_score >= self.master_threshold:
            insights.append(f"Prime {p} qualifies as a 'master prime' with unified score > {self.master_threshold}")
        
        # Special insights for 17 and 19
        if p == 17:
            insights.append("Prime 17 is the lower generator of C* = 17/19")
        elif p == 19:
            insights.append("Prime 19 is the upper generator of C* = 17/19")
        
        # Reptend insights
        if analysis.get('hardness_analysis', {}).get('is_reptend', False):
            insights.append(f"Prime {p} is a reptend prime with maximal reciprocal complexity")
        
        # Family insights
        family_count = analysis.get('family_analysis', {}).get('family_count', 0)
        if family_count >= 3:
            insights.append(f"Prime {p} participates in {family_count} different prime families")
        
        return insights
    
    def identify_master_primes(self, synthesized_primes: List[Dict]) -> List[Dict]:
        """Identify master primes with exceptional composition."""
        
        master_primes = [p for p in synthesized_primes if p['unified_composition_score'] >= self.master_threshold]
        
        # Sort by unified score
        master_primes.sort(key=lambda x: x['unified_composition_score'], reverse=True)
        
        return master_primes
    
    def generate_composition_formulas(self, master_primes: List[Dict]) -> List[Dict]:
        """Generate composition formulas for master primes."""
        
        formulas = []
        
        for prime_data in master_primes:
            p = prime_data['prime']
            
            formula = {
                'prime': p,
                'composition_score': prime_data['unified_composition_score'],
                'formulas': []
            }
            
            # C* relationship formulas
            p_times_c = p * C_STAR
            p_div_c = p / C_STAR
            
            if abs(p_times_c - round(p_times_c)) < 0.01:
                formula['formulas'].append({
                    'type': 'c_star_product',
                    'formula': f"{p} × (17/19) ≈ {round(p_times_c)}",
                    'precision': abs(p_times_c - round(p_times_c))
                })
            
            if abs(p_div_c - round(p_div_c)) < 0.01:
                formula['formulas'].append({
                    'type': 'c_star_division',
                    'formula': f"{p} / (17/19) ≈ {round(p_div_c)}",
                    'precision': abs(p_div_c - round(p_div_c))
                })
            
            # Hardness formula
            hardness = prime_data['individual_scores'].get('hardness_score', 0) / 100
            if hardness > 0.95:
                formula['formulas'].append({
                    'type': 'hardness',
                    'formula': f"H({p}) = {hardness:.4f} (maximal)",
                    'interpretation': 'reptend prime'
                })
            
            # Reciprocal space formula
            if prime_data['exceptional_properties']:
                formula['formulas'].append({
                    'type': 'reciprocal_space',
                    'formula': f"R({p}) = dense in C* zone",
                    'interpretation': 'strong reciprocal structure'
                })
            
            formulas.append(formula)
        
        return formulas
    
    def create_composition_hierarchy(self, synthesized_primes: List[Dict]) -> Dict:
        """Create hierarchy of prime composition levels."""
        
        hierarchy = {
            'levels': {},
            'statistics': {},
            'transitions': {}
        }
        
        # Group by composition class
        for prime_data in synthesized_primes:
            comp_class = prime_data['composition_class']
            
            if comp_class not in hierarchy['levels']:
                hierarchy['levels'][comp_class] = []
            
            hierarchy['levels'][comp_class].append(prime_data)
        
        # Calculate statistics for each level
        for comp_class, primes in hierarchy['levels'].items():
            scores = [p['unified_composition_score'] for p in primes]
            hierarchy['statistics'][comp_class] = {
                'count': len(primes),
                'average_score': statistics.mean(scores),
                'min_score': min(scores),
                'max_score': max(scores),
                'score_range': max(scores) - min(scores)
            }
        
        # Analyze transitions between levels
        sorted_primes = sorted(synthesized_primes, key=lambda x: x['prime'])
        transitions = []
        
        for i in range(1, len(sorted_primes)):
            prev_class = sorted_primes[i-1]['composition_class']
            curr_class = sorted_primes[i]['composition_class']
            
            if prev_class != curr_class:
                transitions.append({
                    'from_prime': sorted_primes[i-1]['prime'],
                    'to_prime': sorted_primes[i]['prime'],
                    'from_class': prev_class,
                    'to_class': curr_class,
                    'score_change': sorted_primes[i]['unified_composition_score'] - sorted_primes[i-1]['unified_composition_score']
                })
        
        hierarchy['transitions'] = transitions
        
        return hierarchy
    
    def generate_synthesis_report(self, synthesized_primes: List[Dict]) -> Dict:
        """Generate comprehensive synthesis report."""
        
        master_primes = self.identify_master_primes(synthesized_primes)
        formulas = self.generate_composition_formulas(master_primes)
        hierarchy = self.create_composition_hierarchy(synthesized_primes)
        
        # Overall statistics
        all_scores = [p['unified_composition_score'] for p in synthesized_primes]
        
        report = {
            'executive_summary': {
                'total_primes_analyzed': len(synthesized_primes),
                'master_primes_found': len(master_primes),
                'average_composition_score': statistics.mean(all_scores),
                'highest_composition_score': max(all_scores),
                'composition_distribution': hierarchy['statistics']
            },
            'master_primes': master_primes,
            'composition_formulas': formulas,
            'composition_hierarchy': hierarchy,
            'key_insights': self._generate_key_insights(synthesized_primes, master_primes, hierarchy),
            'research_directions': self._suggest_research_directions(master_primes, formulas)
        }
        
        return report
    
    def _generate_key_insights(self, all_primes: List[Dict], master_primes: List[Dict], hierarchy: Dict) -> List[str]:
        """Generate key insights from synthesis."""
        
        insights = []
        
        # Master prime insights
        if len(master_primes) >= 2:
            insights.append(f"Found {len(master_primes)} master primes with unified composition scores > {self.master_threshold}")
            insights.append("Master primes exhibit exceptional properties across multiple analysis dimensions")
        
        # Generator prime insights
        generator_primes = [p for p in master_primes if p['prime'] in [17, 19]]
        if len(generator_primes) == 2:
            insights.append("Both generator primes (17, 19) qualify as master primes")
            insights.append("C* = 17/19 demonstrates exceptional compositional power")
        
        # Hierarchy insights
        if hierarchy['statistics']:
            most_common_class = max(hierarchy['statistics'], key=lambda x: hierarchy['statistics'][x]['count'])
            insights.append(f"Most common composition class: {most_common_class}")
        
        # Transition insights
        if len(hierarchy['transitions']) > 0:
            insights.append(f"Found {len(hierarchy['transitions'])} composition level transitions")
            significant_transitions = [t for t in hierarchy['transitions'] if abs(t['score_change']) > 20]
            if significant_transitions:
                insights.append(f"Found {len(significant_transitions)} significant composition changes")
        
        return insights
    
    def _suggest_research_directions(self, master_primes: List[Dict], formulas: List[Dict]) -> List[str]:
        """Suggest future research directions."""
        
        directions = []
        
        if master_primes:
            directions.append("Investigate why master primes achieve exceptional unified scores")
            directions.append("Study common properties among master primes to identify composition principles")
        
        if formulas:
            directions.append("Develop formal proofs for observed composition formulas")
            directions.append("Extend composition formulas to predict behavior of unanalyzed primes")
        
        directions.extend([
            "Investigate the relationship between C* and prime distribution at larger scales",
            "Study whether composition patterns persist in primes > 10^6",
            "Explore connections between composition strength and prime conjectures (Goldbach, Twin Prime, etc.)",
            "Develop algorithmic methods to predict composition scores for new primes",
            "Investigate physical or geometric interpretations of prime composition"
        ])
        
        return directions
    
    def synthesize_from_analyses(self, analyses: Dict) -> Dict:
        """Synthesize from individual analysis results."""
        
        # Combine all analyses into unified format
        unified_analyses = []
        
        primes = set()
        
        # Collect all unique primes from all analyses
        for analysis_type, analysis_data in analyses.items():
            if isinstance(analysis_data, dict) and 'individual_analyses' in analysis_data:
                for item in analysis_data['individual_analyses']:
                    if isinstance(item, dict) and 'prime' in item:
                        primes.add(item['prime'])
            elif isinstance(analysis_data, list):
                for item in analysis_data:
                    if isinstance(item, dict) and 'prime' in item:
                        primes.add(item['prime'])
        
        # Create unified analysis for each prime
        for p in sorted(list(primes)):
            unified_analysis = {'prime': p}
            
            # Extract data from each analysis type
            for analysis_type, analysis_data in analyses.items():
                if isinstance(analysis_data, dict) and 'individual_analyses' in analysis_data:
                    # Find data for this prime
                    prime_data = next((item for item in analysis_data['individual_analyses'] 
                                     if item.get('prime') == p), {})
                    unified_analysis[analysis_type] = prime_data
                elif isinstance(analysis_data, list):
                    prime_data = next((item for item in analysis_data if item.get('prime') == p), {})
                    unified_analysis[analysis_type] = prime_data
            
            unified_analyses.append(unified_analysis)
        
        # Generate synthesis
        synthesized_primes = self.synthesize_prime_composition(unified_analyses)
        
        # Create comprehensive report
        report = self.generate_synthesis_report(synthesized_primes)
        
        return {
            'synthesized_primes': synthesized_primes,
            'synthesis_report': report
        }
    
    def export_results(self, results: Dict, filename: str = "unified_composition_synthesis.json"):
        """Export synthesis results to JSON."""
        with open(filename, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"Unified composition synthesis saved to {filename}")

def main():
    """Main demonstration."""
    print("=" * 80)
    print("PRIME COMPOSITION TOOL #7: UNIFIED COMPOSITION SYNTHESIZER")
    print("Synthesizing all prime composition analyses")
    print("=" * 80)
    
    # Initialize synthesizer
    synthesizer = UnifiedCompositionSynthesizer()
    
    # Mock comprehensive analyses for demonstration
    mock_analyses = {
        'reciprocal_space': {
            'individual_analyses': [
                {'prime': p, 'composition_score': 50 + p % 40} for p in [17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
            ]
        },
        'c_star_composition': {
            'individual_analyses': [
                {'prime': p, 'composition_score': 60 + p % 35} for p in [17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
            ]
        },
        'hardness_analysis': {
            'individual_analyses': [
                {'prime': p, 'quantum_hardness': 0.8 + (p % 20) / 100, 'is_reptend': p % 3 == 0} 
                for p in [17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
            ]
        },
        'family_analysis': {
            'individual_analyses': [
                {'prime': p, 'family_count': p % 5} for p in [17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
            ]
        },
        'limits_analysis': {
            'individual_analyses': [
                {'prime': p, 'composition_score': 40 + p % 45} for p in [17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
            ]
        },
        'pattern_analysis': {
            'individual_analyses': [
                {'prime': p, 'composition_score': 55 + p % 38} for p in [17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
            ]
        }
    }
    
    print(f"\nSynthesizing composition analyses...")
    
    # Comprehensive synthesis
    results = synthesizer.synthesize_from_analyses(mock_analyses)
    
    # Display results
    print("\n🌟 SYNTHESIS REPORT:")
    report = results['synthesis_report']['executive_summary']
    print(f"  Total primes analyzed: {report['total_primes_analyzed']}")
    print(f"  Master primes found: {report['master_primes_found']}")
    print(f"  Average composition score: {report['average_composition_score']:.1f}")
    print(f"  Highest composition score: {report['highest_composition_score']:.1f}")
    
    print("\n👑 MASTER PRIMES:")
    master_primes = results['synthesis_report']['master_primes']
    for i, prime_data in enumerate(master_primes):
        print(f"  {i+1}. Prime {prime_data['prime']} - Score: {prime_data['unified_composition_score']:.1f}")
        print(f"     Class: {prime_data['composition_class']}")
        print(f"     Properties: {', '.join(prime_data['exceptional_properties'])}")
    
    print("\n🔑 KEY INSIGHTS:")
    for insight in results['synthesis_report']['key_insights']:
        print(f"  • {insight}")
    
    print("\n🔬 RESEARCH DIRECTIONS:")
    for direction in results['synthesis_report']['research_directions'][:5]:
        print(f"  • {direction}")
    
    # Export results
    synthesizer.export_results(results)
    
    print("\n✅ Unified composition synthesis complete!")

if __name__ == "__main__":
    main()