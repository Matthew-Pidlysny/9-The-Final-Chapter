"""
Banachian Geometry Engine

Implements Banachian geometry based on complete normed vector spaces
with reciprocal adjacency relationships and metric space properties.
"""

import numpy as np
import math
from typing import Dict, List, Any, Optional, Tuple, Set
from dataclasses import dataclass, field

from ..core.geometry_base import GeometryEngine, GeometryType, InformationSphere, GenerationConstraints
from ..core.quanta import InformationQuanta, QuantaType
from ..core.coordinates import TysonCoordinate
from ..core.structures import StructureValidator, StructureOptimizer, OptimizationTarget, GeometricConstraints


@dataclass
class BanachianConstraints:
    """Specific constraints for Banachian geometry"""
    norm_type: str = "euclidean"  # euclidean, manhattan, supremum, custom
    completeness_threshold: float = 1e-8
    contraction_factor: float = 0.9
    reciprocal_depth: int = 3
    metric_properties: List[str] = field(default_factory=lambda: ["positivity", "symmetry", "triangle_inequality"])


class BanachianEngine(GeometryEngine):
    """
    Banachian Geometry Engine
    
    Implements geometric representation based on Banach space theory.
    Features complete normed vector spaces, reciprocal adjacency relationships,
    and strict adherence to metric space axioms.
    """
    
    def __init__(self):
        super().__init__(GeometryType.BANACHIAN)
        self.constraints = BanachianConstraints()
        self.validator = StructureValidator(GeometricConstraints())
        self.optimizer = StructureOptimizer()
        
        # Norm functions for different norm types
        self._init_norm_functions()
    
    def _init_norm_functions(self):
        """Initialize norm functions for different Banach space types"""
        self.norm_functions = {
            "euclidean": lambda x: np.linalg.norm(x, 2),
            "manhattan": lambda x: np.linalg.norm(x, 1),
            "supremum": lambda x: np.linalg.norm(x, np.inf),
            "p4": lambda x: np.linalg.norm(x, 4),
            "custom": lambda x: self._custom_norm(x)
        }
    
    def _custom_norm(self, x: np.ndarray) -> float:
        """Custom norm function combining multiple properties"""
        euclidean_norm = np.linalg.norm(x, 2)
        manhattan_norm = np.linalg.norm(x, 1)
        return 0.7 * euclidean_norm + 0.3 * manhattan_norm
    
    def analyze_quanta(self, quanta: InformationQuanta) -> Dict[str, Any]:
        """
        Analyze quanta for Banachian representation
        
        Focuses on metric properties, completeness, and vector space
        characteristics of the information.
        """
        analysis = {
            'recommended_dimensionality': self._determine_optimal_dimensionality(quanta),
            'complexity_assessment': quanta.properties.complexity,
            'metric_compatibility': 0.0,
            'completeness_score': 0.0,
            'optimal_norm': self.constraints.norm_type,
            'constraint_requirements': {},
            'optimization_opportunities': []
        }
        
        # Analyze data for metric compatibility
        if isinstance(quanta.data, (list, tuple, np.ndarray)):
            data = np.array(quanta.data, dtype=float)
            
            # Test different norms
            best_norm = None
            best_score = 0.0
            
            for norm_name, norm_func in self.norm_functions.items():
                if norm_name == "custom":
                    continue
                
                score = self._evaluate_norm_compatibility(data, norm_func)
                if score > best_score:
                    best_score = score
                    best_norm = norm_name
            
            analysis['metric_compatibility'] = best_score
            analysis['optimal_norm'] = best_norm
            
            # Calculate completeness score
            analysis['completeness_score'] = self._calculate_completeness_score(data)
        
        # Optimization suggestions
        if analysis['metric_compatibility'] > 0.8:
            analysis['optimization_opportunities'].append('metric_optimization')
        if analysis['completeness_score'] < 0.5:
            analysis['optimization_opportunities'].append('completion_extension')
        
        return analysis
    
    def _determine_optimal_dimensionality(self, quanta: InformationQuanta) -> int:
        """Determine optimal dimensionality for Banachian representation"""
        if isinstance(quanta.data, (list, tuple, np.ndarray)):
            data = np.array(quanta.data, dtype=float)
            
            if data.ndim == 1:
                # For 1D data, use information content to determine dimensionality
                information_content = quanta.properties.complexity * quanta.properties.dimensionality
                
                if information_content < 0.3:
                    return 2
                elif information_content < 0.7:
                    return 3
                else:
                    return min(5, max(2, int(math.ceil(information_content * 4))))
            else:
                return min(data.shape[-1], 5)
        
        return 2  # Default to 2D
    
    def _evaluate_norm_compatibility(self, data: np.ndarray, norm_func) -> float:
        """Evaluate how well a norm function fits the data"""
        if data.size < 2:
            return 0.0
        
        # Test metric properties
        positivity_violations = 0
        symmetry_violations = 0
        triangle_violations = 0
        
        # Test positivity: ||x|| >= 0, ||x|| = 0 iff x = 0
        for i in range(min(10, data.size)):
            x = data[i:i+1] if i+1 <= data.size else data[-1:]
            norm_value = norm_func(x)
            if norm_value < 0 or (np.allclose(x, 0) and not np.isclose(norm_value, 0)):
                positivity_violations += 1
        
        # Test symmetry: ||x - y|| = ||y - x||
        # Test triangle inequality: ||x - z|| <= ||x - y|| + ||y - z||
        for i in range(min(5, data.size - 2)):
            x = data[i:i+1] if i+1 <= data.size else data[-1:]
            y = data[i+1:i+2] if i+2 <= data.size else data[-1:]
            z = data[i+2:i+3] if i+3 <= data.size else data[-2:]
            
            dist_xy = norm_func(x - y)
            dist_yx = norm_func(y - x)
            dist_xz = norm_func(x - z)
            dist_xy_plus_yz = norm_func(x - y) + norm_func(y - z)
            
            if abs(dist_xy - dist_yx) > 1e-6:
                symmetry_violations += 1
            
            if dist_xz > dist_xy_plus_yz + 1e-6:
                triangle_violations += 1
        
        # Calculate compatibility score
        total_tests = positivity_violations + symmetry_violations + triangle_violations + 1
        violations = positivity_violations + symmetry_violations + triangle_violations
        
        compatibility = 1.0 - (violations / total_tests)
        return max(0.0, compatibility)
    
    def _calculate_completeness_score(self, data: np.ndarray) -> float:
        """Calculate how complete the data is for Banachian representation"""
        if data.size == 0:
            return 0.0
        
        # Check for missing values or NaN
        missing_ratio = np.sum(~np.isfinite(data)) / data.size
        
        # Check for sufficient coverage
        unique_values = len(np.unique(data[~np.isnan(data)]))
        coverage_score = min(1.0, unique_values / max(10, data.size))
        
        # Overall completeness
        completeness = (1.0 - missing_ratio) * coverage_score
        return completeness
    
    def generate_sphere(self, quanta: InformationQuanta, 
                       constraints: Optional[GenerationConstraints] = None) -> InformationSphere:
        """
        Generate Banachian sphere from information quanta
        
        Creates a complete normed vector space representation with
        reciprocal adjacency relationships.
        """
        if constraints is None:
            constraints = GenerationConstraints()
        
        # Analyze the quanta
        analysis = self.analyze_quanta(quanta)
        
        # Generate coordinates using Banach space principles
        coordinates = self._generate_banachian_coordinates(quanta, analysis, constraints)
        
        # Create reciprocal adjacency relationships
        coordinates = self._establish_reciprocal_adjacency(coordinates)
        
        # Create sphere properties
        sphere_properties = self._create_sphere_properties(coordinates, analysis)
        
        # Create the information sphere
        sphere = InformationSphere(
            geometry_type=self.geometry_type,
            coordinates=coordinates,
            properties=sphere_properties,
            quanta_source=quanta,
            generation_metadata={
                'engine': 'Banachian',
                'analysis': analysis,
                'constraints': constraints.__dict__ if constraints else {},
                'norm_type': analysis['optimal_norm']
            }
        )
        
        # Optimize if requested
        if constraints and constraints.optimization_goal != "none":
            sphere = self.optimize_representation(sphere, constraints.optimization_goal)
        
        return sphere
    
    def _generate_banachian_coordinates(self, quanta: InformationQuanta, 
                                       analysis: Dict[str, Any],
                                       constraints: GenerationConstraints) -> List[TysonCoordinate]:
        """Generate coordinates using Banach space principles"""
        coordinates = []
        norm_func = self.norm_functions[analysis['optimal_norm']]
        dimensionality = analysis['recommended_dimensionality']
        
        if isinstance(quanta.data, (int, float)):
            # Single value - create simple Banachian representation
            value = float(quanta.data)
            
            # Create coordinate system based on norm
            if analysis['optimal_norm'] == "euclidean":
                # Euclidean: place on sphere
                theta = 2 * math.pi * value
                for r in np.linspace(0.1, 1.0, 6):
                    x = r * math.cos(theta)
                    y = r * math.sin(theta)
                    if dimensionality >= 3:
                        z = r * math.sin(theta) * 0.5
                        pos = np.array([x, y, z])
                    else:
                        pos = np.array([x, y])
            else:
                # Non-Euclidean: create based on norm properties
                pos = np.zeros(dimensionality)
                pos[0] = value
                # Create other coordinates based on norm
                for i in range(1, min(dimensionality, 4)):
                    scale = 1.0 / (1.0 + i)
                    pos[i] = value * scale
            
            coord = TysonCoordinate(
                position=pos,
                geometry_type="banachian",
                metadata={'value': value, 'norm_type': analysis['optimal_norm']}
            )
            coordinates.append(coord)
        
        elif isinstance(quanta.data, (list, tuple, np.ndarray)):
            data = np.array(quanta.data, dtype=float)
            
            # Normalize data to unit ball in Banach space
            if data.size > 0:
                data_norm = norm_func(data)
                if data_norm > 0:
                    normalized_data = data / data_norm
                else:
                    normalized_data = data
            else:
                normalized_data = np.array([0.0])
            
            # Extend to optimal dimensionality
            if normalized_data.size < dimensionality:
                extended_data = np.zeros(dimensionality)
                extended_data[:normalized_data.size] = normalized_data
                normalized_data = extended_data
            elif normalized_data.size > dimensionality:
                # PCA reduction
                normalized_data = self._reduce_dimensionality(normalized_data, dimensionality)
            
            # Generate coordinates based on Banachian principles
            n_coords = min(20, max(5, int(len(data) * 0.3)))
            
            for i in range(n_coords):
                # Create linear combinations with Banachian constraints
                alpha = i / max(1, n_coords - 1)
                
                # Contraction mapping principle
                coord_data = normalized_data * (self.constraints.contraction_factor ** alpha)
                
                # Add small perturbation for completeness
                perturbation = np.random.normal(0, 0.01, coord_data.shape)
                coord_data = coord_data + perturbation
                
                # Renormalize if needed
                coord_norm = norm_func(coord_data)
                if coord_norm > constraints.max_radius:
                    coord_data = coord_data * (constraints.max_radius / coord_norm)
                
                coord = TysonCoordinate(
                    position=coord_data,
                    geometry_type="banachian",
                    metadata={
                        'index': i,
                        'alpha': alpha,
                        'norm_type': analysis['optimal_norm']
                    }
                )
                coordinates.append(coord)
        
        else:
            # Default representation for other data types
            data_hash = hash(str(quanta.data))
            seed = abs(data_hash) % 1000
            
            np.random.seed(seed)
            pos = np.random.normal(0, 1, dimensionality)
            
            # Normalize to unit ball
            pos_norm = norm_func(pos)
            if pos_norm > 0:
                pos = pos / pos_norm
            
            coord = TysonCoordinate(
                position=pos,
                geometry_type="banachian",
                metadata={'hash': data_hash, 'norm_type': analysis['optimal_norm']}
            )
            coordinates.append(coord)
        
        return coordinates
    
    def _reduce_dimensionality(self, data: np.ndarray, target_dim: int) -> np.ndarray:
        """Reduce dimensionality using PCA"""
        if data.size <= target_dim:
            return data
        
        # Reshape for PCA if needed
        if data.ndim == 1:
            data_2d = data.reshape(-1, 1)
        else:
            data_2d = data
        
        # Simple PCA using eigenvalue decomposition
        cov_matrix = np.cov(data_2d.T)
        eigenvalues, eigenvectors = np.linalg.eigh(cov_matrix)
        
        # Sort by eigenvalue magnitude
        idx = np.argsort(np.abs(eigenvalues))[::-1][:target_dim]
        selected_vectors = eigenvectors[:, idx]
        
        # Project data
        reduced_data = data_2d @ selected_vectors
        
        return reduced_data.flatten() if reduced_data.shape[1] == 1 else reduced_data
    
    def _establish_reciprocal_adjacency(self, coordinates: List[TysonCoordinate]) -> List[TysonCoordinate]:
        """Establish reciprocal adjacency relationships between coordinates"""
        if len(coordinates) < 2:
            return coordinates
        
        norm_func = self.norm_functions[self.constraints.norm_type]
        
        # Build adjacency graph
        adjacency = {}
        for i, coord1 in enumerate(coordinates):
            adjacency[i] = []
            for j, coord2 in enumerate(coordinates):
                if i != j:
                    distance = norm_func(coord1.position - coord2.position)
                    if distance < 1.0:  # Adjacency threshold
                        adjacency[i].append(j)
        
        # Enhance coordinates with adjacency information
        enhanced_coordinates = []
        
        for i, coord in enumerate(coordinates):
            enhanced_coord = TysonCoordinate(
                position=coord.position.copy(),
                geometry_type=coord.geometry_type,
                metadata={
                    **coord.metadata,
                    'adjacent_to': adjacency[i],
                    'adjacency_count': len(adjacency[i]),
                    'reciprocal_depth': self.constraints.reciprocal_depth
                }
            )
            enhanced_coordinates.append(enhanced_coord)
        
        return enhanced_coordinates
    
    def _create_sphere_properties(self, coordinates: List[TysonCoordinate], 
                                 analysis: Dict[str, Any]) -> 'SphereProperties':
        """Create sphere properties based on Banachian principles"""
        from ..core.geometry_base import SphereProperties
        
        if not coordinates:
            return SphereProperties()
        
        positions = np.array([coord.position for coord in coordinates])
        norm_func = self.norm_functions[self.constraints.norm_type]
        
        # Calculate Banachian-specific properties
        center = np.mean(positions, axis=0)
        distances = [norm_func(pos - center) for pos in positions]
        radius = max(distances) if distances else 1.0
        
        # Calculate curvature based on norm type
        if self.constraints.norm_type == "euclidean":
            curvature = 1.0 / radius if radius > 0 else 0.0
        else:
            curvature = 0.0  # Non-Euclidean spaces have different curvature
        
        # Calculate volume based on norm
        dimensionality = positions.shape[1]
        if self.constraints.norm_type == "euclidean":
            volume = (math.pi ** (dimensionality/2)) * (radius ** dimensionality) / math.gamma(dimensionality/2 + 1)
        else:
            # Approximate volume for non-Euclidean norms
            volume = radius ** dimensionality
        
        return SphereProperties(
            radius=radius,
            center=center,
            curvature=curvature,
            volume=volume,
            dimensionality=dimensionality,
            constraints={
                'norm_type': self.constraints.norm_type,
                'completeness_threshold': self.constraints.completeness_threshold,
                'metric_properties': self.constraints.metric_properties
            },
            metadata={
                'metric_compatibility': analysis['metric_compatibility'],
                'completeness_score': analysis['completeness_score']
            }
        )
    
    def calculate_distance(self, coord1: TysonCoordinate, coord2: TysonCoordinate) -> float:
        """Calculate distance using the specified Banach norm"""
        norm_func = self.norm_functions[self.constraints.norm_type]
        return norm_func(coord1.position - coord2.position)
    
    def optimize_representation(self, sphere: InformationSphere, 
                                goal: str = "balance") -> InformationSphere:
        """Optimize sphere representation for specific goal"""
        if goal == "accuracy":
            # Optimize for metric compliance
            optimized_coords = self._optimize_metric_compliance(sphere.coordinates)
        elif goal == "speed":
            # Reduce complexity while preserving Banachian properties
            optimized_coords = self._reduce_complexity(sphere.coordinates)
        else:  # balance
            # Balance optimization
            optimized_coords = self._balance_optimization(sphere.coordinates)
        
        # Create optimized sphere
        optimized_sphere = InformationSphere(
            geometry_type=sphere.geometry_type,
            coordinates=optimized_coords,
            properties=sphere.properties,
            quanta_source=sphere.quanta_source,
            generation_metadata={
                **sphere.generation_metadata,
                'optimization': goal,
                'original_coords': len(sphere.coordinates),
                'optimized_coords': len(optimized_coords)
            }
        )
        
        return optimized_sphere
    
    def _optimize_metric_compliance(self, coordinates: List[TysonCoordinate]) -> List[TysonCoordinate]:
        """Optimize coordinates for better metric compliance"""
        if len(coordinates) < 3:
            return coordinates
        
        norm_func = self.norm_functions[self.constraints.norm_type]
        
        # Use gradient descent to optimize for metric properties
        optimized = []
        
        for coord in coordinates:
            pos = coord.position.copy()
            
            # Simple gradient step to improve metric properties
            for _ in range(10):
                gradient = np.zeros_like(pos)
                
                # Calculate gradient based on metric violations
                for other in optimized:
                    diff = pos - other.position
                    dist = norm_func(diff)
                    
                    # Penalize metric violations
                    if dist < 1e-8 and not np.allclose(diff, 0):
                        gradient += diff / (dist + 1e-8)
                
                # Update position
                pos = pos - 0.01 * gradient
            
            optimized_coord = TysonCoordinate(
                position=pos,
                geometry_type=coord.geometry_type,
                metadata={**coord.metadata, 'metric_optimized': True}
            )
            optimized.append(optimized_coord)
        
        return optimized
    
    def _reduce_complexity(self, coordinates: List[TysonCoordinate]) -> List[TysonCoordinate]:
        """Reduce complexity while preserving Banachian properties"""
        if len(coordinates) <= 5:
            return coordinates
        
        # Select coordinates that best represent the space
        norm_func = self.norm_functions[self.constraints.norm_type]
        
        # Keep points that maximize coverage
        selected = [coordinates[0]]  # Always keep first point
        
        for coord in coordinates[1:]:
            # Check if this point adds significant coverage
            min_dist = min(norm_func(coord.position - sel.position) for sel in selected)
            
            if min_dist > 0.1:  # Threshold for significance
                selected.append(coord)
            
            if len(selected) >= 10:  # Limit total points
                break
        
        return selected
    
    def _balance_optimization(self, coordinates: List[TysonCoordinate]) -> List[TysonCoordinate]:
        """Balance between different optimization goals"""
        # Simple approach: keep every second coordinate
        return coordinates[::2] if len(coordinates) > 8 else coordinates
    
    def validate_constraints(self, sphere: InformationSphere) -> bool:
        """Validate Banachian specific constraints"""
        valid, errors = self.validator.validate_sphere(sphere.coordinates)
        
        if not valid:
            return False
        
        # Validate metric properties
        norm_func = self.norm_functions[self.constraints.norm_type]
        
        # Test metric axioms on sample points
        coords = sphere.coordinates[:min(5, len(sphere.coordinates))]
        
        for i in range(len(coords)):
            for j in range(i+1, len(coords)):
                # Test symmetry
                dist_ij = norm_func(coords[i].position - coords[j].position)
                dist_ji = norm_func(coords[j].position - coords[i].position)
                
                if abs(dist_ij - dist_ji) > self.constraints.completeness_threshold:
                    return False
        
        # Test triangle inequality
        for i in range(len(coords)):
            for j in range(i+1, len(coords)):
                for k in range(j+1, len(coords)):
                    dist_ik = norm_func(coords[i].position - coords[k].position)
                    dist_ij = norm_func(coords[i].position - coords[j].position)
                    dist_jk = norm_func(coords[j].position - coords[k].position)
                    
                    if dist_ik > dist_ij + dist_jk + self.constraints.completeness_threshold:
                        return False
        
        return True