"""
Hadwiger-Nelson Geometry Engine

Implements the Hadwiger-Nelson problem geometry using trigonometric
polynomials with forbidden angular configurations.
"""

import numpy as np
import math
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass

from ..core.geometry_base import GeometryEngine, GeometryType, InformationSphere, GenerationConstraints
from ..core.quanta import InformationQuanta, QuantaType
from ..core.coordinates import TysonCoordinate
from ..core.structures import StructureValidator, StructureOptimizer, OptimizationTarget, GeometricConstraints


@dataclass
class HadwigerNelsonConstraints:
    """Specific constraints for Hadwiger-Nelson geometry"""
    forbidden_angles: List[float] = None
    angle_tolerance: float = 0.1
    polynomial_degree: int = 3
    chromatic_number: int = 7  # Current best upper bound
    
    def __post_init__(self):
        if self.forbidden_angles is None:
            # Classic forbidden angles from Hadwiger-Nelson problem
            self.forbidden_angles = [
                math.pi / 3,      # 60 degrees
                math.pi / 6,      # 30 degrees  
                math.pi / 2       # 90 degrees
            ]


class HadwigerNelsonEngine(GeometryEngine):
    """
    Hadwiger-Nelson Geometry Engine
    
    Implements geometric representation based on the Hadwiger-Nelson problem,
    which deals with coloring the plane such that no two points at distance 1
    have the same color. This engine uses trigonometric polynomials and
    angular constraints to represent information.
    """
    
    def __init__(self):
        super().__init__(GeometryType.HADWIGER_NELSON)
        self.constraints = HadwigerNelsonConstraints()
        self.validator = StructureValidator(GeometricConstraints())
        self.optimizer = StructureOptimizer()
        
        # Pre-computed trigonometric basis functions
        self._init_basis_functions()
    
    def _init_basis_functions(self):
        """Initialize trigonometric basis functions for polynomial generation"""
        self.basis_functions = []
        for n in range(self.constraints.polynomial_degree + 1):
            # sin(nx) and cos(nx) basis functions
            self.basis_functions.append(('sin', n))
            self.basis_functions.append(('cos', n))
    
    def analyze_quanta(self, quanta: InformationQuanta) -> Dict[str, Any]:
        """
        Analyze quanta for Hadwiger-Nelson representation
        
        Focuses on angular relationships, periodic patterns, and
        chromatic properties of the information.
        """
        analysis = {
            'recommended_dimensionality': 2,  # Planar geometry
            'complexity_assessment': quanta.properties.complexity,
            'angular_content': 0.0,
            'periodicity': 0.0,
            'chromatic_requirements': 1,
            'constraint_requirements': {},
            'optimization_opportunities': []
        }
        
        # Analyze data for angular content
        if isinstance(quanta.data, (list, tuple, np.ndarray)):
            data = np.array(quanta.data, dtype=float)
            
            if data.size >= 2:
                # Extract angular relationships
                angles = self._extract_angles(data)
                analysis['angular_content'] = self._calculate_angular_content(angles)
                analysis['periodicity'] = self._calculate_periodicity(data)
                
                # Determine chromatic requirements based on complexity
                if analysis['complexity_assessment'] < 0.3:
                    analysis['chromatic_requirements'] = 2
                elif analysis['complexity_assessment'] < 0.6:
                    analysis['chromatic_requirements'] = 4
                else:
                    analysis['chromatic_requirements'] = min(7, self.constraints.chromatic_number)
        
        # Optimization suggestions
        if analysis['angular_content'] > 0.7:
            analysis['optimization_opportunities'].append('angular_basis')
        if analysis['periodicity'] > 0.5:
            analysis['optimization_opportunities'].append('frequency_decomposition')
        
        return analysis
    
    def generate_sphere(self, quanta: InformationQuanta, 
                       constraints: Optional[GenerationConstraints] = None) -> InformationSphere:
        """
        Generate Hadwiger-Nelson sphere from information quanta
        
        Creates a planar representation with angular constraints based on
        trigonometric polynomial interpolation.
        """
        if constraints is None:
            constraints = GenerationConstraints()
        
        # Analyze the quanta
        analysis = self.analyze_quanta(quanta)
        
        # Generate coordinates based on analysis
        coordinates = self._generate_coordinates_from_quanta(quanta, analysis, constraints)
        
        # Create sphere properties
        sphere_properties = self._create_sphere_properties(coordinates, analysis)
        
        # Create the information sphere
        sphere = InformationSphere(
            geometry_type=self.geometry_type,
            coordinates=coordinates,
            properties=sphere_properties,
            quanta_source=quanta,
            generation_metadata={
                'engine': 'HadwigerNelson',
                'analysis': analysis,
                'constraints': constraints.__dict__ if constraints else {}
            }
        )
        
        # Optimize if requested
        if constraints and constraints.optimization_goal != "none":
            sphere = self.optimize_representation(sphere, constraints.optimization_goal)
        
        return sphere
    
    def _extract_angles(self, data: np.ndarray) -> List[float]:
        """Extract angular relationships from data"""
        angles = []
        
        if data.size >= 2:
            # Treat consecutive pairs as vectors
            for i in range(data.size - 1):
                if i + 1 < data.size:
                    v1 = np.array([data[i], data[i+1]])
                    if i + 3 < data.size:
                        v2 = np.array([data[i+2], data[i+3]])
                        
                        # Calculate angle between vectors
                        norm1 = np.linalg.norm(v1)
                        norm2 = np.linalg.norm(v2)
                        
                        if norm1 > 0 and norm2 > 0:
                            cos_angle = np.dot(v1, v2) / (norm1 * norm2)
                            angle = math.acos(np.clip(cos_angle, -1, 1))
                            angles.append(angle)
        
        return angles
    
    def _calculate_angular_content(self, angles: List[float]) -> float:
        """Calculate how much angular content the data has"""
        if not angles:
            return 0.0
        
        # Check for forbidden angles
        forbidden_count = 0
        for angle in angles:
            for forbidden in self.constraints.forbidden_angles:
                if abs(angle - forbidden) < self.constraints.angle_tolerance:
                    forbidden_count += 1
                    break
        
        # Normalize angular content
        total_content = len(angles) / max(len(angles), 1)
        forbidden_ratio = forbidden_count / max(len(angles), 1)
        
        return min(1.0, total_content + forbidden_ratio)
    
    def _calculate_periodicity(self, data: np.ndarray) -> float:
        """Calculate periodicity in the data"""
        if data.size < 4:
            return 0.0
        
        # Use autocorrelation to detect periodicity
        autocorr = np.correlate(data, data, mode='full')
        autocorr = autocorr[autocorr.size // 2:]
        
        # Find peaks in autocorrelation
        peaks = []
        for i in range(1, len(autocorr) - 1):
            if autocorr[i] > autocorr[i-1] and autocorr[i] > autocorr[i+1]:
                peaks.append(i)
        
        if len(peaks) < 2:
            return 0.0
        
        # Calculate periodicity from peak spacing
        spacings = [peaks[i+1] - peaks[i] for i in range(len(peaks)-1)]
        avg_spacing = np.mean(spacings)
        spacing_variance = np.var(spacings)
        
        # Higher periodicity = more regular spacing
        periodicity = 1.0 - min(1.0, spacing_variance / (avg_spacing ** 2))
        return periodicity
    
    def _generate_coordinates_from_quanta(self, quanta: InformationQuanta, 
                                         analysis: Dict[str, Any],
                                         constraints: GenerationConstraints) -> List[TysonCoordinate]:
        """Generate coordinates from quanta using trigonometric polynomials"""
        coordinates = []
        
        if isinstance(quanta.data, (int, float)):
            # Single value - create simple representation
            value = float(quanta.data)
            angle = 2 * math.pi * value / (constraints.max_radius if constraints else 1.0)
            
            for r in np.linspace(0.1, 1.0, 5):
                x = r * math.cos(angle)
                y = r * math.sin(angle)
                pos = np.array([x, y])
                
                coord = TysonCoordinate(
                    position=pos,
                    geometry_type="hadwiger_nelson",
                    metadata={'value': value, 'angle': angle}
                )
                coordinates.append(coord)
        
        elif isinstance(quanta.data, (list, tuple, np.ndarray)):
            data = np.array(quanta.data, dtype=float)
            
            if data.size >= 2:
                # Use data to generate trigonometric polynomial
                polynomial_coeffs = self._fit_trigonometric_polynomial(data)
                
                # Sample polynomial to generate coordinates
                n_samples = min(len(data), 20)
                for i in range(n_samples):
                    t = 2 * math.pi * i / n_samples
                    x, y = self._evaluate_polynomial(polynomial_coeffs, t)
                    
                    # Ensure no forbidden angles
                    angle = math.atan2(y, x)
                    angle = self._avoid_forbidden_angles(angle)
                    
                    r = math.sqrt(x**2 + y**2)
                    x = r * math.cos(angle)
                    y = r * math.sin(angle)
                    
                    pos = np.array([x, y])
                    coord = TysonCoordinate(
                        position=pos,
                        geometry_type="hadwiger_nelson",
                        metadata={'sample': i, 'angle': angle}
                    )
                    coordinates.append(coord)
        
        else:
            # Default representation for other data types
            data_hash = hash(str(quanta.data))
            angle = (data_hash % 1000) / 1000.0 * 2 * math.pi
            angle = self._avoid_forbidden_angles(angle)
            
            for r in np.linspace(0.1, 1.0, 8):
                x = r * math.cos(angle)
                y = r * math.sin(angle)
                pos = np.array([x, y])
                
                coord = TysonCoordinate(
                    position=pos,
                    geometry_type="hadwiger_nelson",
                    metadata={'hash': data_hash}
                )
                coordinates.append(coord)
        
        return coordinates
    
    def _fit_trigonometric_polynomial(self, data: np.ndarray) -> Dict[str, List[float]]:
        """Fit trigonometric polynomial to data"""
        n_points = len(data)
        degree = min(self.constraints.polynomial_degree, n_points // 2)
        
        # Initialize coefficients
        sin_coeffs = []
        cos_coeffs = []
        
        # Simple fitting using least squares
        t_values = np.linspace(0, 2*math.pi, n_points)
        
        for n in range(degree + 1):
            # Fit sin(nx) coefficient
            sin_basis = np.sin(n * t_values)
            sin_coeff = np.dot(data, sin_basis) / np.dot(sin_basis, sin_basis)
            sin_coeffs.append(sin_coeff)
            
            # Fit cos(nx) coefficient
            cos_basis = np.cos(n * t_values)
            cos_coeff = np.dot(data, cos_basis) / np.dot(cos_basis, cos_basis)
            cos_coeffs.append(cos_coeff)
        
        return {'sin': sin_coeffs, 'cos': cos_coeffs}
    
    def _evaluate_polynomial(self, coeffs: Dict[str, List[float]], t: float) -> Tuple[float, float]:
        """Evaluate trigonometric polynomial at parameter t"""
        sin_coeffs = coeffs['sin']
        cos_coeffs = coeffs['cos']
        
        x = sum(cos_coeffs[n] * math.cos(n * t) for n in range(len(cos_coeffs)))
        y = sum(sin_coeffs[n] * math.sin(n * t) for n in range(len(sin_coeffs)))
        
        return x, y
    
    def _avoid_forbidden_angles(self, angle: float) -> float:
        """Adjust angle to avoid forbidden configurations"""
        for forbidden in self.constraints.forbidden_angles:
            if abs(angle - forbidden) < self.constraints.angle_tolerance:
                # Shift angle away from forbidden region
                if angle < forbidden:
                    angle -= self.constraints.angle_tolerance
                else:
                    angle += self.constraints.angle_tolerance
                
                # Wrap to [0, 2π]
                angle = angle % (2 * math.pi)
        
        return angle
    
    def _create_sphere_properties(self, coordinates: List[TysonCoordinate], 
                                 analysis: Dict[str, Any]) -> 'SphereProperties':
        """Create sphere properties based on coordinates and analysis"""
        from ..core.geometry_base import SphereProperties
        
        if not coordinates:
            return SphereProperties()
        
        positions = np.array([coord.position for coord in coordinates])
        
        # Calculate geometric properties
        center = np.mean(positions, axis=0)
        distances = [np.linalg.norm(pos - center) for pos in positions]
        radius = max(distances) if distances else 1.0
        
        # Calculate curvature (approximate for planar geometry)
        curvature = 0.0 if len(coordinates) < 3 else 0.1
        
        return SphereProperties(
            radius=radius,
            center=center,
            curvature=curvature,
            dimensionality=2,  # Hadwiger-Nelson is inherently planar
            constraints={
                'forbidden_angles': self.constraints.forbidden_angles,
                'chromatic_number': analysis['chromatic_requirements']
            },
            metadata={
                'angular_content': analysis['angular_content'],
                'periodicity': analysis['periodicity']
            }
        )
    
    def calculate_distance(self, coord1: TysonCoordinate, coord2: TysonCoordinate) -> float:
        """Calculate distance respecting Hadwiger-Nelson constraints"""
        # Basic Euclidean distance with angular penalty
        euclidean_dist = np.linalg.norm(coord1.position - coord2.position)
        
        # Add penalty for forbidden angle configurations
        angle1 = math.atan2(coord1.position[1], coord1.position[0]) if coord1.position.size >= 2 else 0
        angle2 = math.atan2(coord2.position[1], coord2.position[0]) if coord2.position.size >= 2 else 0
        angle_diff = abs(angle1 - angle2)
        
        penalty = 0.0
        for forbidden in self.constraints.forbidden_angles:
            if abs(angle_diff - forbidden) < self.constraints.angle_tolerance:
                penalty = 10.0  # Large penalty for forbidden configurations
                break
        
        return euclidean_dist + penalty
    
    def optimize_representation(self, sphere: InformationSphere, 
                                goal: str = "balance") -> InformationSphere:
        """Optimize sphere representation for specific goal"""
        if goal == "accuracy":
            # Refine angular resolution
            optimized_coords = self._refine_angular_resolution(sphere.coordinates)
        elif goal == "speed":
            # Reduce coordinate count while preserving structure
            optimized_coords = self._reduce_coordinate_count(sphere.coordinates)
        else:  # balance
            # Moderate optimization
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
    
    def _refine_angular_resolution(self, coordinates: List[TysonCoordinate]) -> List[TysonCoordinate]:
        """Refine angular resolution for better accuracy"""
        refined = []
        
        for coord in coordinates:
            refined.append(coord)
            
            # Add intermediate points for higher resolution
            if len(refined) > 1:
                prev_coord = refined[-2]
                intermediate = prev_coord.interpolate(coord, 0.5)
                refined.append(intermediate)
        
        return refined
    
    def _reduce_coordinate_count(self, coordinates: List[TysonCoordinate]) -> List[TysonCoordinate]:
        """Reduce coordinate count for speed"""
        if len(coordinates) <= 5:
            return coordinates
        
        # Keep every nth coordinate
        step = max(1, len(coordinates) // 5)
        reduced = coordinates[::step]
        
        return reduced
    
    def _balance_optimization(self, coordinates: List[TysonCoordinate]) -> List[TysonCoordinate]:
        """Balance between accuracy and speed"""
        target_count = max(8, min(15, len(coordinates)))
        
        if len(coordinates) <= target_count:
            return coordinates
        
        # Uniform sampling
        step = len(coordinates) // target_count
        balanced = coordinates[::step]
        
        return balanced
    
    def validate_constraints(self, sphere: InformationSphere) -> bool:
        """Validate Hadwiger-Nelson specific constraints"""
        valid, errors = self.validator.validate_sphere(sphere.coordinates)
        
        if not valid:
            return False
        
        # Check angular constraints
        for coord in sphere.coordinates:
            if coord.position.size >= 2:
                angle = math.atan2(coord.position[1], coord.position[0])
                
                for forbidden in self.constraints.forbidden_angles:
                    if abs(angle - forbidden) < self.constraints.angle_tolerance:
                        return False
        
        return True