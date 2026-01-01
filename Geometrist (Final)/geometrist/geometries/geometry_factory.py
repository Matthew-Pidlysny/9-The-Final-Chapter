"""
Geometry Factory

Intelligent geometry selection and dynamic creation system that chooses
the most efficient geometry for any given information and can create
new geometries when necessary.
"""

from typing import Dict, List, Any, Optional, Type, Union
from dataclasses import dataclass
import numpy as np
from enum import Enum, auto

from ..core.geometry_base import GeometryEngine, GeometryType, InformationSphere
from ..core.quanta import InformationQuanta, QuantaProperties
from ..core.coordinates import TysonCoordinate

from .hadwiger_nelson import HadwigerNelsonEngine
from .banachian import BanachianEngine
from .fuzzy import FuzzyEngine
from .quantum import QuantumEngine
from .relational import RelationalEngine


class SelectionStrategy(Enum):
    """Strategies for geometry selection"""
    EFFICIENCY = auto()       # Choose fastest/most efficient
    ACCURACY = auto()         # Choose most accurate
    BALANCE = auto()          # Balance efficiency and accuracy
    ADAPTIVE = auto()         # Adaptive selection based on input
    THEORETICAL = auto()      # Choose theoretically optimal


@dataclass
class GeometryMetrics:
    """Metrics for evaluating geometry performance"""
    efficiency_score: float = 0.0      # 0.0 to 1.0, computational efficiency
    accuracy_score: float = 0.0        # 0.0 to 1.0, representation accuracy
    complexity_handling: float = 0.0   # 0.0 to 1.0, handles complexity well
    scalability_score: float = 0.0     # 0.0 to 1.0, scales with size
    novelty_score: float = 0.0         # 0.0 to 1.0, novel representations
    theoretical_foundation: float = 0.0 # 0.0 to 1.0, mathematical rigor


class DynamicGeometry:
    """Dynamically created geometry for novel situations"""
    
    def __init__(self, name: str, foundation: str, constraints: Dict[str, Any]):
        self.name = name
        self.foundation = foundation  # Mathematical foundation
        self.constraints = constraints
        self.performance_history = []
        self.adaptation_count = 0
    
    def record_performance(self, metrics: GeometryMetrics):
        """Record performance metrics"""
        self.performance_history.append(metrics)
    
    def get_average_performance(self) -> GeometryMetrics:
        """Get average performance metrics"""
        if not self.performance_history:
            return GeometryMetrics()
        
        avg_metrics = GeometryMetrics()
        n = len(self.performance_history)
        
        for metric in self.performance_history:
            avg_metrics.efficiency_score += metric.efficiency_score / n
            avg_metrics.accuracy_score += metric.accuracy_score / n
            avg_metrics.complexity_handling += metric.complexity_handling / n
            avg_metrics.scalability_score += metric.scalability_score / n
            avg_metrics.novelty_score += metric.novelty_score / n
            avg_metrics.theoretical_foundation += metric.theoretical_foundation / n
        
        return avg_metrics


class GeometryFactory:
    """
    Intelligent geometry selection and creation system
    
    Analyzes information quanta to select the most efficient geometry
    from the available arsenal, or creates new geometries when existing
    ones are insufficient.
    """
    
    def __init__(self):
        # Initialize all geometry engines
        self.geometry_engines: Dict[GeometryType, GeometryEngine] = {
            GeometryType.HADWIGER_NELSON: HadwigerNelsonEngine(),
            GeometryType.BANACHIAN: BanachianEngine(),
            GeometryType.FUZZY: FuzzyEngine(),
            GeometryType.QUANTUM: QuantumEngine(),
            GeometryType.RELATIONAL: RelationalEngine()
        }
        
        # Performance tracking
        self.performance_history: Dict[GeometryType, List[GeometryMetrics]] = {
            geom_type: [] for geom_type in GeometryType
        }
        
        # Dynamic geometry registry
        self.dynamic_geometries: Dict[str, DynamicGeometry] = {}
        
        # Selection strategy
        self.selection_strategy = SelectionStrategy.ADAPTIVE
        
        # Theoretical foundations for new geometries
        self.theoretical_foundations = [
            "hyperbolic_manifolds",
            "fractal_geometry", 
            "topological_data_analysis",
            "information_geometry",
            "non_euclidean_geometries",
            "algebraic_geometry",
            "differential_geometry",
            "category_theory_spaces",
            "quantum_gravity_geometries",
            "complex_network_geometries"
        ]
        
        # Initialize geometry profiles
        self._initialize_geometry_profiles()
    
    def _initialize_geometry_profiles(self):
        """Initialize performance profiles for each geometry"""
        self.geometry_profiles = {
            GeometryType.HADWIGER_NELSON: GeometryMetrics(
                efficiency_score=0.7,
                accuracy_score=0.8,
                complexity_handling=0.6,
                scalability_score=0.7,
                novelty_score=0.8,
                theoretical_foundation=0.9
            ),
            GeometryType.BANACHIAN: GeometryMetrics(
                efficiency_score=0.8,
                accuracy_score=0.9,
                complexity_handling=0.7,
                scalability_score=0.8,
                novelty_score=0.6,
                theoretical_foundation=0.9
            ),
            GeometryType.FUZZY: GeometryMetrics(
                efficiency_score=0.6,
                accuracy_score=0.7,
                complexity_handling=0.9,
                scalability_score=0.6,
                novelty_score=0.8,
                theoretical_foundation=0.8
            ),
            GeometryType.QUANTUM: GeometryMetrics(
                efficiency_score=0.5,
                accuracy_score=0.8,
                complexity_handling=0.8,
                scalability_score=0.5,
                novelty_score=0.9,
                theoretical_foundation=0.9
            ),
            GeometryType.RELATIONAL: GeometryMetrics(
                efficiency_score=0.4,
                accuracy_score=0.9,
                complexity_handling=1.0,
                scalability_score=0.4,
                novelty_score=1.0,
                theoretical_foundation=0.8
            )
        }
    
    def select_optimal_geometry(self, quanta: InformationQuanta, 
                               strategy: Optional[SelectionStrategy] = None) -> GeometryType:
        """
        Select the most efficient geometry for the given quanta
        
        Uses intelligent analysis to choose from existing geometries or
        determines if a new geometry should be created.
        """
        if strategy is None:
            strategy = self.selection_strategy
        
        # Analyze quanta with all geometries
        geometry_scores = {}
        
        for geom_type, engine in self.geometry_engines.items():
            analysis = engine.analyze_quanta(quanta)
            score = self._calculate_selection_score(geom_type, analysis, strategy)
            geometry_scores[geom_type] = score
        
        # Determine if new geometry is needed
        if self._should_create_new_geometry(quanta, geometry_scores):
            new_geometry = self._create_new_geometry(quanta)
            if new_geometry:
                return new_geometry
        
        # Select best existing geometry
        best_geometry = max(geometry_scores.keys(), key=lambda k: geometry_scores[k])
        
        # Update performance tracking
        self._record_selection(best_geometry, quanta)
        
        return best_geometry
    
    def _calculate_selection_score(self, geom_type: GeometryType, 
                                 analysis: Dict[str, Any], 
                                 strategy: SelectionStrategy) -> float:
        """Calculate selection score for a geometry"""
        profile = self.geometry_profiles[geom_type]
        complexity = analysis.get('complexity_assessment', 0.5)
        
        if strategy == SelectionStrategy.EFFICIENCY:
            # Prioritize computational efficiency
            return (profile.efficiency_score * 0.6 + 
                   profile.scalability_score * 0.3 + 
                   (1.0 - complexity) * 0.1)
        
        elif strategy == SelectionStrategy.ACCURACY:
            # Prioritize representation accuracy
            return (profile.accuracy_score * 0.6 + 
                   profile.theoretical_foundation * 0.3 + 
                   complexity * 0.1)
        
        elif strategy == SelectionStrategy.BALANCE:
            # Balance efficiency and accuracy
            return (profile.efficiency_score * 0.25 + 
                   profile.accuracy_score * 0.25 + 
                   profile.complexity_handling * 0.25 + 
                   profile.scalability_score * 0.25)
        
        elif strategy == SelectionStrategy.ADAPTIVE:
            # Adaptive based on quanta properties
            if complexity < 0.3:
                # Low complexity - prioritize efficiency
                return profile.efficiency_score * 0.8 + profile.accuracy_score * 0.2
            elif complexity < 0.7:
                # Medium complexity - balanced approach
                return (profile.efficiency_score + profile.accuracy_score + 
                       profile.complexity_handling) / 3.0
            else:
                # High complexity - prioritize complexity handling
                return profile.complexity_handling * 0.6 + profile.accuracy_score * 0.4
        
        else:  # THEORETICAL
            # Prioritize theoretical foundation
            return (profile.theoretical_foundation * 0.6 + 
                   profile.novelty_score * 0.3 + 
                   profile.accuracy_score * 0.1)
    
    def _should_create_new_geometry(self, quanta: InformationQuanta, 
                                   geometry_scores: Dict[GeometryType, float]) -> bool:
        """Determine if a new geometry should be created"""
        # Check if all existing geometries score poorly
        max_score = max(geometry_scores.values())
        
        if max_score < 0.6:  # Threshold for needing new geometry
            return True
        
        # Check for novel properties not well-handled by existing geometries
        novel_properties = self._detect_novel_properties(quanta)
        if novel_properties and max_score < 0.8:
            return True
        
        # Check theoretical requirements
        if quanta.properties.complexity > 0.9 and max_score < 0.7:
            return True
        
        return False
    
    def _detect_novel_properties(self, quanta: InformationQuanta) -> List[str]:
        """Detect novel properties that might require new geometries"""
        novel_properties = []
        
        # Check for extreme values
        if quanta.properties.complexity > 0.95:
            novel_properties.append("ultra_high_complexity")
        
        if quanta.properties.entropy > 0.95:
            novel_properties.append("maximum_entropy")
        
        if quanta.properties.dimensionality > 10:
            novel_properties.append("ultra_high_dimensionality")
        
        # Check for unusual data structures
        if isinstance(quanta.data, dict) and len(quanta.data) > 1000:
            novel_properties.append("massive_relational_structure")
        
        # Check for mathematical patterns
        if isinstance(quanta.data, (list, np.ndarray)):
            data = np.array(quanta.data, dtype=float)
            if data.size > 0:
                # Check for fractal patterns
                if self._has_fractal_properties(data):
                    novel_properties.append("fractal_structure")
                
                # Check for topological complexity
                if self._has_topological_complexity(data):
                    novel_properties.append("topological_complexity")
        
        return novel_properties
    
    def _has_fractal_properties(self, data: np.ndarray) -> bool:
        """Check if data has fractal properties"""
        if data.size < 10:
            return False
        
        # Simple fractal detection using self-similarity at different scales
        try:
            # Calculate box-counting dimension approximation
            scales = [2, 4, 8]
            counts = []
            
            for scale in scales:
                if data.size >= scale:
                    # Count non-empty boxes
                    boxes = np.histogram(data, bins=scale)[0]
                    count = np.sum(boxes > 0)
                    counts.append(count)
            
            if len(counts) >= 2:
                # Calculate fractal dimension
                log_scales = np.log(scales[:len(counts)])
                log_counts = np.log(counts)
                
                if len(log_scales) > 1:
                    # Simple linear regression
                    slope = (log_counts[-1] - log_counts[0]) / (log_scales[-1] - log_scales[0])
                    return 1.0 < abs(slope) < 2.0  # Typical fractal range
        
        except:
            pass
        
        return False
    
    def _has_topological_complexity(self, data: np.ndarray) -> bool:
        """Check if data has topological complexity"""
        # Simplified topological complexity detection
        if data.size < 20:
            return False
        
        # Check for high-dimensional connectivity patterns
        try:
            # Create simple connectivity graph
            threshold = np.std(data) * 0.5
            connections = 0
            
            for i in range(min(50, len(data))):
                for j in range(i+1, min(50, len(data))):
                    if abs(data[i] - data[j]) < threshold:
                        connections += 1
            
            # High connectivity suggests topological complexity
            max_connections = min(50, len(data)) * (min(50, len(data)) - 1) // 2
            if connections / max_connections > 0.3:
                return True
        
        except:
            pass
        
        return False
    
    def _create_new_geometry(self, quanta: InformationQuanta) -> Optional[GeometryType]:
        """Create a new geometry for novel situations"""
        novel_properties = self._detect_novel_properties(quanta)
        
        if not novel_properties:
            return None
        
        # Select theoretical foundation
        foundation = self._select_theoretical_foundation(quanta, novel_properties)
        
        # Create dynamic geometry
        geometry_name = f"dynamic_{len(self.dynamic_geometries)}_{foundation}"
        
        dynamic_geometry = DynamicGeometry(
            name=geometry_name,
            foundation=foundation,
            constraints={
                'novel_properties': novel_properties,
                'complexity': quanta.properties.complexity,
                'dimensionality': quanta.properties.dimensionality
            }
        )
        
        self.dynamic_geometries[geometry_name] = dynamic_geometry
        
        # Return as new geometry type (conceptual)
        # In practice, this would create a new engine class
        return GeometryType.RELATIONAL  # Fallback to relational for now
    
    def _select_theoretical_foundation(self, quanta: InformationQuanta, 
                                      novel_properties: List[str]) -> str:
        """Select appropriate theoretical foundation for new geometry"""
        # Match novel properties to theoretical foundations
        property_foundation_map = {
            "ultra_high_complexity": ["information_geometry", "category_theory_spaces"],
            "maximum_entropy": ["quantum_gravity_geometries", "information_geometry"],
            "ultra_high_dimensionality": ["hyperbolic_manifolds", "algebraic_geometry"],
            "massive_relational_structure": ["complex_network_geometries", "category_theory_spaces"],
            "fractal_structure": ["fractal_geometry"],
            "topological_complexity": ["topological_data_analysis"]
        }
        
        # Find matching foundations
        matching_foundations = set()
        for prop in novel_properties:
            if prop in property_foundation_map:
                matching_foundations.update(property_foundation_map[prop])
        
        # Select foundation based on quanta properties
        if matching_foundations:
            return list(matching_foundations)[0]
        else:
            # Default based on complexity
            if quanta.properties.complexity > 0.8:
                return "quantum_gravity_geometries"
            else:
                return "information_geometry"
    
    def _record_selection(self, geometry_type: GeometryType, quanta: InformationQuanta):
        """Record geometry selection for performance tracking"""
        # Create performance metrics for this selection
        metrics = GeometryMetrics()
        
        # Base metrics from profile
        profile = self.geometry_profiles[geometry_type]
        metrics.efficiency_score = profile.efficiency_score
        metrics.accuracy_score = profile.accuracy_score
        metrics.complexity_handling = profile.complexity_handling
        metrics.scalability_score = profile.scalability_score
        metrics.novelty_score = profile.novelty_score
        metrics.theoretical_foundation = profile.theoretical_foundation
        
        # Adjust based on actual performance
        complexity = quanta.properties.complexity
        if complexity > 0.8:
            metrics.complexity_handling = min(1.0, metrics.complexity_handling * 0.8)
        
        # Record performance
        self.performance_history[geometry_type].append(metrics)
        
        # Keep history manageable
        if len(self.performance_history[geometry_type]) > 100:
            self.performance_history[geometry_type] = self.performance_history[geometry_type][-50:]
    
    def generate_optimal_sphere(self, quanta: InformationQuanta, 
                               strategy: Optional[SelectionStrategy] = None) -> InformationSphere:
        """
        Generate optimal sphere using intelligent geometry selection
        
        Automatically selects the best geometry and generates the sphere.
        """
        # Select optimal geometry
        optimal_geometry = self.select_optimal_geometry(quanta, strategy)
        
        # Generate sphere using selected geometry
        engine = self.geometry_engines[optimal_geometry]
        sphere = engine.generate_sphere(quanta)
        
        # Add geometry factory metadata
        sphere.generation_metadata.update({
            'geometry_factory_selection': optimal_geometry.name,
            'selection_strategy': strategy.name if strategy else None,
            'geometry_factory_version': '1.0'
        })
        
        return sphere
    
    def analyze_geometry_performance(self) -> Dict[str, Any]:
        """Analyze performance of all geometries"""
        performance_analysis = {}
        
        for geom_type, history in self.performance_history.items():
            if history:
                # Calculate average metrics
                avg_metrics = GeometryMetrics()
                n = len(history)
                
                for metric in history:
                    avg_metrics.efficiency_score += metric.efficiency_score / n
                    avg_metrics.accuracy_score += metric.accuracy_score / n
                    avg_metrics.complexity_handling += metric.complexity_handling / n
                    avg_metrics.scalability_score += metric.scalability_score / n
                    avg_metrics.novelty_score += metric.novelty_score / n
                    avg_metrics.theoretical_foundation += metric.theoretical_foundation / n
                
                performance_analysis[geom_type.name] = {
                    'total_selections': len(history),
                    'average_metrics': avg_metrics.__dict__,
                    'selection_frequency': len(history) / max(1, sum(len(h) for h in self.performance_history.values()))
                }
        
        # Add dynamic geometries analysis
        if self.dynamic_geometries:
            performance_analysis['dynamic_geometries'] = {
                'total_created': len(self.dynamic_geometries),
                'foundations_used': list(set(g.foundation for g in self.dynamic_geometries.values())),
                'average_adaptations': np.mean([g.adaptation_count for g in self.dynamic_geometries.values()]) if self.dynamic_geometries else 0
            }
        
        return performance_analysis
    
    def update_geometry_profiles(self):
        """Update geometry profiles based on actual performance"""
        for geom_type, history in self.performance_history.items():
            if len(history) >= 5:  # Need sufficient data
                # Calculate updated profile
                profile = self.geometry_profiles[geom_type]
                
                # Update based on recent performance
                recent_metrics = history[-10:]  # Last 10 selections
                n = len(recent_metrics)
                
                # Weighted update (recent performance has more weight)
                for metric in recent_metrics:
                    weight = 0.1  # Learning rate
                    profile.efficiency_score = (1 - weight) * profile.efficiency_score + weight * metric.efficiency_score
                    profile.accuracy_score = (1 - weight) * profile.accuracy_score + weight * metric.accuracy_score
                    profile.complexity_handling = (1 - weight) * profile.complexity_handling + weight * metric.complexity_handling
                    profile.scalability_score = (1 - weight) * profile.scalability_score + weight * metric.scalability_score
                    profile.novelty_score = (1 - weight) * profile.novelty_score + weight * metric.novelty_score
                    profile.theoretical_foundation = (1 - weight) * profile.theoretical_foundation + weight * metric.theoretical_foundation
    
    def get_theoretical_geometry_blueprint(self, foundation: str, 
                                         constraints: Dict[str, Any]) -> Dict[str, Any]:
        """
        Get theoretical blueprint for creating new geometries
        
        Provides mathematical foundation and implementation guidance
        for theoretically sound new geometries.
        """
        blueprints = {
            "hyperbolic_manifolds": {
                "description": "Geometry with constant negative curvature",
                "mathematical_foundation": "Hyperbolic space H^n with metric ds² = dx₁² + ... + dx_n² / x_n²",
                "key_properties": ["exponential_growth", "negative_curvature", "tree_like_structure"],
                "coordinate_system": "Poincaré ball or half-space model",
                "applications": ["hierarchical_data", "network_analysis", "scale_invariant_structures"],
                "implementation_notes": "Use hyperbolic distance functions and exponential maps"
            },
            "fractal_geometry": {
                "description": "Self-similar geometric structures with non-integer dimensions",
                "mathematical_foundation": "Iterated function systems and Hausdorff dimension",
                "key_properties": ["self_similarity", "fractional_dimension", "scale_invariance"],
                "coordinate_system": "Affine transformations in fractal space",
                "applications": ["natural_phenomena", "chaotic_systems", "complex_patterns"],
                "implementation_notes": "Implement IFS with contraction mappings"
            },
            "topological_data_analysis": {
                "description": "Geometry based on topological invariants and persistent homology",
                "mathematical_foundation": "Simplicial complexes and homology groups",
                "key_properties": ["connectivity_preservation", "hole_detection", "multi_scale_analysis"],
                "coordinate_system": "Persistence diagrams and Morse complexes",
                "applications": ["shape_analysis", "feature_extraction", "data_classification"],
                "implementation_notes": "Use Vietoris-Rips complexes and persistent homology"
            },
            "information_geometry": {
                "description": "Geometry of statistical manifolds and information divergence",
                "mathematical_foundation": "Riemannian geometry with Fisher information metric",
                "key_properties": ["statistical_manifold", "information_divergence", "natural_gradient"],
                "coordinate_system": "Natural parameters of exponential families",
                "applications": ["machine_learning", "statistics", "optimization"],
                "implementation_notes": "Implement Fisher metric and Levi-Civita connection"
            },
            "quantum_gravity_geometries": {
                "description": "Quantum spacetime geometries at Planck scale",
                "mathematical_foundation": "Loop quantum gravity and spin networks",
                "key_properties": ["discrete_space", "quantum_geometry", "background_independence"],
                "coordinate_system": "Spin network states and quantum operators",
                "applications": ["fundamental_physics", "quantum_computation", "discrete_geometries"],
                "implementation_notes": "Use quantum states as geometric primitives"
            }
        }
        
        if foundation in blueprints:
            blueprint = blueprints[foundation].copy()
            blueprint["constraints"] = constraints
            blueprint["creation_timestamp"] = self._get_current_timestamp()
            return blueprint
        else:
            return {
                "error": f"Unknown theoretical foundation: {foundation}",
                "available_foundations": list(blueprints.keys())
            }
    
    def _get_current_timestamp(self) -> str:
        """Get current timestamp for record keeping"""
        import time
        return time.strftime("%Y-%m-%d %H:%M:%S")
    
    def set_selection_strategy(self, strategy: SelectionStrategy):
        """Set the geometry selection strategy"""
        self.selection_strategy = strategy
    
    def get_available_geometries(self) -> List[str]:
        """Get list of available geometry types"""
        return [geom_type.name for geom_type in GeometryType]
    
    def get_dynamic_geometries(self) -> Dict[str, Dict[str, Any]]:
        """Get information about dynamically created geometries"""
        return {
            name: {
                'foundation': geom.foundation,
                'constraints': geom.constraints,
                'performance_count': len(geom.performance_history),
                'adaptation_count': geom.adaptation_count
            }
            for name, geom in self.dynamic_geometries.items()
        }