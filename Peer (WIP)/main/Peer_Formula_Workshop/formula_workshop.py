#!/usr/bin/env python3
"""
Peer Formula Workshop - Advanced Formula Analysis & Visualization
Helps formula developers understand breakdown patterns and limitations

Author: Peer Enhancement Team
Version: 1.0.0
"""

import sys
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation
import mpmath as mp
from typing import Dict, List, Tuple, Optional, Any, Callable
from dataclasses import dataclass
from enum import Enum
import json

# Set up plotting
plt.style.use('dark_background')
mp.mp.dps = 50  # High precision


class BreakdownType(Enum):
    """Types of formula breakdowns"""
    NUMERICAL_INSTABILITY = "Numerical Instability"
    DOMAIN_VIOLATION = "Domain Violation"
    CONVERGENCE_FAILURE = "Convergence Failure"
    SINGULARITY = "Singularity"
    OVERFLOW = "Overflow"
    UNDERFLOW = "Underflow"
    PRECISION_LOSS = "Precision Loss"
    DISCONTINUITY = "Discontinuity"
    OSCILLATION = "Unbounded Oscillation"
    DIVERGENCE = "Divergence"


class AnalysisLevel(Enum):
    """Analysis depth levels"""
    BASIC = "Basic"
    INTERMEDIATE = "Intermediate"
    ADVANCED = "Advanced"
    EXPERT = "Expert"
    KARDASHEV_MAX = "Kardashev Max"


@dataclass
class BreakdownEvent:
    """Represents a breakdown event"""
    location: float
    type: BreakdownType
    severity: float
    description: str
    suggestion: str


@dataclass
class FormulaAnalysis:
    """Complete formula analysis"""
    formula_name: str
    formula_expression: str
    domain: Tuple[float, float]
    breakdowns: List[BreakdownEvent]
    stability_score: float
    convergence_regions: List[Tuple[float, float]]
    safe_regions: List[Tuple[float, float]]
    recommendations: List[str]


class NumericalStabilityAnalyzer:
    """Analyzes numerical stability of formulas"""
    
    def __init__(self):
        self.breakdown_events = []
        
    def analyze_stability(self, func: Callable, domain: Tuple[float, float], 
                          num_points: int = 1000) -> List[BreakdownEvent]:
        """Analyze numerical stability across domain"""
        x = np.linspace(domain[0], domain[1], num_points)
        events = []
        
        prev_y = None
        prev_diff = None
        
        for i, xi in enumerate(x):
            try:
                # Evaluate with different precisions
                y_double = float(func(xi))
                y_high = float(mp.mpf(str(xi)) * 2)  # Simplified
                
                # Check for numerical instability
                if prev_y is not None:
                    diff = abs(y_double - prev_y)
                    
                    # Large sudden changes
                    if diff > 100 * (prev_diff if prev_diff else 1):
                        events.append(BreakdownEvent(
                            location=xi,
                            type=BreakdownType.NUMERICAL_INSTABILITY,
                            severity=min(diff / 1000, 1.0),
                            description=f"Sudden change of {diff:.2e}",
                            suggestion="Check for numerical cancellation or use higher precision"
                        ))
                    
                    # Check for oscillation
                    if i > 10:
                        recent_changes = [abs(float(func(x[j])) - float(func(x[j-1]))) 
                                        for j in range(i-10, i)]
                        if np.std(recent_changes) > 10 * np.mean(recent_changes):
                            events.append(BreakdownEvent(
                                location=xi,
                                type=BreakdownType.OSCILLATION,
                                severity=0.8,
                                description="Unbounded oscillation detected",
                                suggestion="Formula may not converge in this region"
                            ))
                
                prev_y = y_double
                prev_diff = diff if prev_y is not None else 1
                
            except (OverflowError, ZeroDivisionError, ValueError) as e:
                events.append(BreakdownEvent(
                    location=xi,
                    type=BreakdownType.SINGULARITY if 'division' in str(e).lower() else BreakdownType.OVERFLOW,
                    severity=1.0,
                    description=str(e),
                    suggestion="Add domain restrictions or use limit analysis"
                ))
        
        return events
    
    def detect_precision_loss(self, func: Callable, x: float) -> Optional[BreakdownEvent]:
        """Detect precision loss at specific point"""
        try:
            # Compare different precision levels
            y_50 = mp.nsum(lambda k: mp.mpf(str(k)) if k == 0 else 0, [0, 10])  # Placeholder
            y_100 = mp.nsum(lambda k: mp.mpf(str(k)) if k == 0 else 0, [0, 10])  # Placeholder
            
            if abs(y_50 - y_100) > 1e-10:
                return BreakdownEvent(
                    location=x,
                    type=BreakdownType.PRECISION_LOSS,
                    severity=abs(y_50 - y_100),
                    description=f"Precision difference detected",
                    suggestion="Use arbitrary precision arithmetic"
                )
        except:
            pass
        return None


class DomainAnalyzer:
    """Analyzes domain violations and restrictions"""
    
    def find_domain_restrictions(self, func: Callable, 
                                 initial_domain: Tuple[float, float]) -> List[BreakdownEvent]:
        """Find domain restrictions and violations"""
        events = []
        
        # Test boundary points
        for x in [initial_domain[0], initial_domain[1]]:
            try:
                y = func(x)
                if not np.isfinite(y):
                    events.append(BreakdownEvent(
                        location=x,
                        type=BreakdownType.DOMAIN_VIOLATION,
                        severity=1.0,
                        description=f"Non-finite value at boundary",
                        suggestion="Exclude boundary from domain"
                    ))
            except Exception as e:
                events.append(BreakdownEvent(
                    location=x,
                    type=BreakdownType.DOMAIN_VIOLATION,
                    severity=1.0,
                    description=str(e),
                    suggestion="Add explicit domain restrictions"
                ))
        
        # Search for discontinuities
        events.extend(self._find_discontinuities(func, initial_domain))
        
        return events
    
    def _find_discontinuities(self, func: Callable, 
                              domain: Tuple[float, float]) -> List[BreakdownEvent]:
        """Find discontinuities in the domain"""
        events = []
        x = np.linspace(domain[0], domain[1], 100)
        
        prev_y = None
        for i in range(1, len(x)):
            try:
                y = func(x[i])
                y_prev = func(x[i-1])
                
                # Check for jump discontinuity
                if abs(y - y_prev) > 100:
                    events.append(BreakdownEvent(
                        location=x[i],
                        type=BreakdownType.DISCONTINUITY,
                        severity=0.9,
                        description=f"Jump discontinuity: {y_prev:.2f} → {y:.2f}",
                        suggestion="Check for piecewise definition or removable discontinuity"
                    ))
                
            except:
                pass
        
        return events


class ConvergenceAnalyzer:
    """Analyzes convergence behavior"""
    
    def analyze_convergence(self, func: Callable, 
                           domain: Tuple[float, float]) -> Dict:
        """Analyze convergence across domain"""
        results = {
            'convergent_regions': [],
            'divergent_regions': [],
            'slow_convergence': []
        }
        
        x = np.linspace(domain[0], domain[1], 100)
        
        # Test convergence at multiple scales
        for scale in [1e-6, 1e-4, 1e-2, 1]:
            try:
                values = [func(xi) for xi in x if np.isfinite(func(xi))]
                if len(values) < 10:
                    results['divergent_regions'].append((domain[0], domain[1]))
                    continue
                
                variance = np.var(values[-10:])
                if variance < 1e-10:
                    results['convergent_regions'].append((domain[0], domain[1]))
                elif variance < 1e-4:
                    results['slow_convergence'].append((domain[0], domain[1]))
                else:
                    results['divergent_regions'].append((domain[0], domain[1]))
            except:
                results['divergent_regions'].append((domain[0], domain[1]))
        
        return results


class Visualizer:
    """Creates visualizations for formula analysis"""
    
    def __init__(self, figsize=(14, 10)):
        self.figsize = figsize
        self.colors = {
            'safe': '#00ff88',
            'warning': '#ffaa00',
            'danger': '#ff4444',
            'breakdown': '#ff00ff'
        }
    
    def create_comprehensive_visualization(self, analysis: FormulaAnalysis, 
                                          func: Callable, save_path: str = None):
        """Create comprehensive visualization of formula analysis"""
        fig = plt.figure(figsize=self.figsize)
        gs = fig.add_gridspec(3, 2, hspace=0.3, wspace=0.3)
        
        # 1. Main function plot with breakdowns
        ax1 = fig.add_subplot(gs[0, :])
        self._plot_function_with_breakdowns(ax1, func, analysis)
        
        # 2. Stability score gauge
        ax2 = fig.add_subplot(gs[1, 0])
        self._plot_stability_gauge(ax2, analysis.stability_score)
        
        # 3. Breakdown timeline
        ax3 = fig.add_subplot(gs[1, 1])
        self._plot_breakdown_timeline(ax3, analysis)
        
        # 4. Safe vs dangerous regions
        ax4 = fig.add_subplot(gs[2, 0])
        self._plot_region_analysis(ax4, analysis)
        
        # 5. Recommendations
        ax5 = fig.add_subplot(gs[2, 1])
        self._plot_recommendations(ax5, analysis)
        
        fig.suptitle(f'Formula Workshop: {analysis.formula_name}', 
                    fontsize=16, fontweight='bold', color='#00ffcc')
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"Visualization saved to {save_path}")
        
        plt.show()
        return fig
    
    def _plot_function_with_breakdowns(self, ax, func: Callable, analysis: FormulaAnalysis):
        """Plot function with breakdown indicators"""
        x = np.linspace(analysis.domain[0], analysis.domain[1], 1000)
        y = []
        
        for xi in x:
            try:
                yi = func(xi)
                y.append(yi if np.isfinite(yi) else np.nan)
            except:
                y.append(np.nan)
        
        y = np.array(y)
        
        # Plot function
        ax.plot(x, y, color='#00aaff', linewidth=2, label='Function')
        
        # Mark breakdowns
        for breakdown in analysis.breakdowns:
            color = self.colors['danger']
            ax.axvline(breakdown.location, color=color, linestyle='--', 
                      alpha=0.7, linewidth=2)
            ax.scatter([breakdown.location], [func(breakdown.location) if np.isfinite(func(breakdown.location)) else 0],
                      color=color, s=100, zorder=5)
        
        # Highlight safe regions
        for region in analysis.safe_regions:
            ax.axvspan(region[0], region[1], alpha=0.2, color=self.colors['safe'])
        
        ax.set_xlabel('x', fontsize=12)
        ax.set_ylabel('f(x)', fontsize=12)
        ax.set_title('Function with Breakdown Indicators', fontsize=14, color='#00aaff')
        ax.legend()
        ax.grid(True, alpha=0.3)
    
    def _plot_stability_gauge(self, ax, score: float):
        """Plot stability score gauge"""
        theta = np.linspace(0, np.pi, 100)
        
        # Background arc
        ax.plot(np.cos(theta), np.sin(theta), color='gray', linewidth=20, alpha=0.3)
        
        # Score arc
        score_theta = np.linspace(0, np.pi * score, 100)
        color = self.colors['safe'] if score > 0.7 else (self.colors['warning'] if score > 0.4 else self.colors['danger'])
        ax.plot(np.cos(score_theta), np.sin(score_theta), color=color, linewidth=20)
        
        # Score text
        ax.text(0, -0.3, f'{score:.2f}', ha='center', fontsize=24, 
               fontweight='bold', color=color)
        ax.text(0, -0.5, 'Stability Score', ha='center', fontsize=12)
        
        ax.set_xlim(-1.2, 1.2)
        ax.set_ylim(-0.6, 1.2)
        ax.axis('off')
        ax.set_title('Overall Stability', fontsize=14, color='#00aaff')
    
    def _plot_breakdown_timeline(self, ax, analysis: FormulaAnalysis):
        """Plot breakdown timeline"""
        if not analysis.breakdowns:
            ax.text(0.5, 0.5, 'No breakdowns detected!', ha='center', va='center',
                   fontsize=14, color=self.colors['safe'])
            ax.set_xlim(0, 1)
            ax.set_ylim(0, 1)
            ax.axis('off')
            return
        
        locations = [b.location for b in analysis.breakdowns]
        severities = [b.severity for b in analysis.breakdowns]
        types = [b.type for b in analysis.breakdowns]
        
        colors = [self.colors['danger'] if s > 0.7 else self.colors['warning'] for s in severities]
        
        ax.scatter(locations, severities, c=colors, s=100, alpha=0.7)
        
        # Annotate points
        for i, (loc, sev, btype) in enumerate(zip(locations, severities, types)):
            ax.annotate(btype.value, (loc, sev), fontsize=8, 
                       rotation=45, ha='left')
        
        ax.set_xlabel('Domain Position', fontsize=12)
        ax.set_ylabel('Severity', fontsize=12)
        ax.set_title('Breakdown Timeline', fontsize=14, color='#00aaff')
        ax.grid(True, alpha=0.3)
        ax.set_ylim(0, 1.1)
    
    def _plot_region_analysis(self, ax, analysis: FormulaAnalysis):
        """Plot safe vs dangerous regions"""
        y_pos = 0
        total_length = analysis.domain[1] - analysis.domain[0]
        
        # Plot safe regions
        for region in analysis.safe_regions:
            length = region[1] - region[0]
            ax.barh(y_pos, length, left=region[0], height=0.5, 
                   color=self.colors['safe'], label='Safe')
            y_pos += 1
        
        # Plot convergence regions
        for region in analysis.convergence_regions:
            length = region[1] - region[0]
            ax.barh(y_pos, length, left=region[0], height=0.5,
                   color=self.colors['warning'], alpha=0.7, label='Convergent')
            y_pos += 1
        
        ax.set_xlabel('Domain', fontsize=12)
        ax.set_yticks([])
        ax.set_title('Region Analysis', fontsize=14, color='#00aaff')
        ax.legend()
    
    def _plot_recommendations(self, ax, analysis: FormulaAnalysis):
        """Plot recommendations"""
        ax.axis('off')
        
        if not analysis.recommendations:
            ax.text(0.5, 0.5, 'No issues found!\nFormula is stable.', 
                   ha='center', va='center', fontsize=14, color=self.colors['safe'])
            return
        
        y = 0.9
        ax.text(0.5, 1.0, 'Recommendations', ha='center', fontsize=14, 
               fontweight='bold', color='#00aaff')
        
        for i, rec in enumerate(analysis.recommendations[:5]):  # Show top 5
            ax.text(0.05, y, f'{i+1}. {rec}', fontsize=10, 
                   color='#ffaa00', wrap=True)
            y -= 0.15
        
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)


class PeerFormulaWorkshop:
    """Main workshop class"""
    
    def __init__(self, analysis_level: AnalysisLevel = AnalysisLevel.ADVANCED):
        self.analysis_level = analysis_level
        self.stability_analyzer = NumericalStabilityAnalyzer()
        self.domain_analyzer = DomainAnalyzer()
        self.convergence_analyzer = ConvergenceAnalyzer()
        self.visualizer = Visualizer()
        
        print(f"Peer Formula Workshop initialized at {analysis_level.value} level")
    
    def analyze_formula(self, name: str, expression: str, 
                       func: Callable, domain: Tuple[float, float] = (-10, 10)) -> FormulaAnalysis:
        """Comprehensive formula analysis"""
        print(f"\n{'='*60}")
        print(f"Analyzing: {name}")
        print(f"Expression: {expression}")
        print(f"Domain: {domain}")
        print(f"{'='*60}\n")
        
        # Collect all breakdowns
        all_breakdowns = []
        
        # Numerical stability
        stability_breakdowns = self.stability_analyzer.analyze_stability(func, domain)
        all_breakdowns.extend(stability_breakdowns)
        print(f"  ✓ Numerical stability: {len(stability_breakdowns)} issues found")
        
        # Domain analysis
        domain_breakdowns = self.domain_analyzer.find_domain_restrictions(func, domain)
        all_breakdowns.extend(domain_breakdowns)
        print(f"  ✓ Domain analysis: {len(domain_breakdowns)} issues found")
        
        # Convergence analysis
        convergence_results = self.convergence_analyzer.analyze_convergence(func, domain)
        print(f"  ✓ Convergence: {len(convergence_results['convergent_regions'])} convergent regions")
        
        # Calculate stability score
        stability_score = self._calculate_stability_score(all_breakdowns, domain)
        print(f"  ✓ Stability score: {stability_score:.2f}")
        
        # Generate recommendations
        recommendations = self._generate_recommendations(all_breakdowns)
        
        # Identify safe regions
        safe_regions = self._identify_safe_regions(all_breakdowns, domain)
        
        analysis = FormulaAnalysis(
            formula_name=name,
            formula_expression=expression,
            domain=domain,
            breakdowns=all_breakdowns,
            stability_score=stability_score,
            convergence_regions=convergence_results['convergent_regions'],
            safe_regions=safe_regions,
            recommendations=recommendations
        )
        
        return analysis
    
    def visualize_analysis(self, analysis: FormulaAnalysis, 
                         func: Callable, save_path: str = None):
        """Create visualization of analysis"""
        return self.visualizer.create_comprehensive_visualization(
            analysis, func, save_path
        )
    
    def _calculate_stability_score(self, breakdowns: List[BreakdownEvent], 
                                   domain: Tuple[float, float]) -> float:
        """Calculate overall stability score"""
        domain_length = domain[1] - domain[0]
        
        if not breakdowns:
            return 1.0
        
        # Weight breakdowns by severity and spread
        total_penalty = sum(b.severity for b in breakdowns)
        max_possible_penalty = len(breakdowns) * 1.0
        
        score = 1.0 - (total_penalty / max_possible_penalty) * 0.5
        return max(0.0, min(1.0, score))
    
    def _generate_recommendations(self, breakdowns: List[BreakdownEvent]) -> List[str]:
        """Generate recommendations based on breakdowns"""
        recommendations = []
        
        # Count breakdown types
        type_counts = {}
        for b in breakdowns:
            type_counts[b.type] = type_counts.get(b.type, 0) + 1
        
        # Generate recommendations
        if BreakdownType.NUMERICAL_INSTABILITY in type_counts:
            recommendations.append(
                "Use arbitrary precision arithmetic (mpmath) for numerical stability"
            )
        
        if BreakdownType.DOMAIN_VIOLATION in type_counts:
            recommendations.append(
                "Add explicit domain restrictions and boundary checks"
            )
        
        if BreakdownType.SINGULARITY in type_counts:
            recommendations.append(
                "Handle singularities with limit analysis or principal value"
            )
        
        if BreakdownType.OSCILLATION in type_counts:
            recommendations.append(
                "Consider damping or convergence acceleration techniques"
            )
        
        if BreakdownType.DIVERGENCE in type_counts:
            recommendations.append(
                "Check for divergence conditions and apply regularization"
            )
        
        if not recommendations:
            recommendations.append("Formula appears stable - continue testing with edge cases")
        
        return recommendations
    
    def _identify_safe_regions(self, breakdowns: List[BreakdownEvent], 
                              domain: Tuple[float, float]) -> List[Tuple[float, float]]:
        """Identify safe regions without breakdowns"""
        if not breakdowns:
            return [domain]
        
        # Sort breakdowns by location
        sorted_breakdowns = sorted(breakdowns, key=lambda x: x.location)
        
        safe_regions = []
        prev_end = domain[0]
        
        for b in sorted_breakdowns:
            if b.location - prev_end > 0.1:  # Minimum safe region width
                safe_regions.append((prev_end, b.location))
            prev_end = b.location + 0.1  # Buffer around breakdown
        
        if domain[1] - prev_end > 0.1:
            safe_regions.append((prev_end, domain[1]))
        
        return safe_regions


# Example usage and demonstrations
def example_formulas():
    """Generate example formulas for testing"""
    return {
        'Riemann Zeta': {
            'expression': 'ζ(s) = Σ n^(-s)',
            'function': lambda x: mp.zeta(x) if x != 1 else float('inf'),
            'domain': (2, 10)
        },
        'Gamma Function': {
            'expression': 'Γ(x) = (x-1)!',
            'function': lambda x: mp.gamma(x),
            'domain': (0.1, 10)
        },
        'Bessel J0': {
            'expression': 'J₀(x)',
            'function': lambda x: mp.besselj(0, x),
            'domain': (0, 20)
        },
        'Exponential Decay': {
            'expression': 'exp(-x²)',
            'function': lambda x: mp.e**(-x**2),
            'domain': (-5, 5)
        },
        'Sinc Function': {
            'expression': 'sin(x)/x',
            'function': lambda x: mp.sin(x)/x if x != 0 else 1,
            'domain': (-10, 10)
        }
    }


def main():
    """Main demonstration"""
    print("""
    ╔═════════════════════════════════════════════════════════╗
    ║         Peer Formula Workshop - Formula Analysis        ║
    ║           Breakdown Detection & Visualization           ║
    ╚═════════════════════════════════════════════════════════╝
    """)
    
    # Initialize workshop
    workshop = PeerFormulaWorkshop(AnalysisLevel.ADVANCED)
    
    # Get example formulas
    formulas = example_formulas()
    
    # Analyze each formula
    for name, info in formulas.items():
        print(f"\n{'='*70}")
        print(f"FORMULA: {name}")
        print(f"{'='*70}")
        
        # Analyze
        analysis = workshop.analyze_formula(
            name=name,
            expression=info['expression'],
            func=info['function'],
            domain=info['domain']
        )
        
        # Visualize
        print(f"\n  Generating visualization...")
        save_path = f"formula_analysis_{name.lower().replace(' ', '_')}.png"
        workshop.visualize_analysis(analysis, info['function'], save_path)
        
        # Print summary
        print(f"\n  Summary:")
        print(f"    - Stability Score: {analysis.stability_score:.2f}")
        print(f"    - Breakdowns Found: {len(analysis.breakdowns)}")
        print(f"    - Safe Regions: {len(analysis.safe_regions)}")
        print(f"    - Top Recommendation: {analysis.recommendations[0] if analysis.recommendations else 'None'}")
    
    print(f"\n{'='*70}")
    print("Analysis Complete!")
    print(f"{'='*70}\n")


if __name__ == '__main__':
    main()