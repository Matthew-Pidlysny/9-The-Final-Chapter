"""
Fuzzy Geometry Engine

Implements fuzzy geometry based on quantum angular momentum states
and fuzzy set theory with graded membership functions.
"""

import numpy as np
import math
from typing import Dict, List, Any, Optional, Tuple, Union
from dataclasses import dataclass, field

from ..core.geometry_base import GeometryEngine, GeometryType, InformationSphere, GenerationConstraints
from ..core.quanta import InformationQuanta, QuantaType
from ..core.coordinates import TysonCoordinate
from ..core.structures import StructureValidator, StructureOptimizer, OptimizationTarget, GeometricConstraints


@dataclass
class FuzzyConstraints:
    """Specific constraints for fuzzy geometry"""
    membership_function: str = "gaussian"  # gaussian, triangular, trapezoidal, sigmoid
    fuzziness_parameter: float = 0.5       # 0.0 (crisp) to 1.0 (maximally fuzzy)
    angular_momentum_quantum: int = 1      # Quantum number for angular momentum
    uncertainty_principle: bool = True
    fuzzy_overlap_threshold: float = 0.3   # Minimum overlap for membership
    quantum_coherence: float = 0.8         # Degree of quantum coherence


class FuzzyEngine(GeometryEngine):
    """
    Fuzzy Geometry Engine
    
    Implements geometric representation based on fuzzy set theory and
    quantum angular momentum states. Features graded membership functions,
    uncertainty principles, and fuzzy spatial relationships.
    """
    
    def __init__(self):
        super().__init__(GeometryType.FUZZY)
        self.constraints = FuzzyConstraints()
        self.validator = StructureValidator(GeometricConstraints())
        self.optimizer = StructureOptimizer()
        
        # Membership functions
        self._init_membership_functions()
        
        # Quantum angular momentum states
        self._init_quantum_states()
    
    def _init_membership_functions(self):
        """Initialize different membership function types"""
        self.membership_functions = {
            "gaussian": lambda x, mu, sigma: np.exp(-((x - mu) ** 2) / (2 * sigma ** 2)),
            "triangular": lambda x, a, b, c: np.maximum(0, np.minimum((x - a) / (b - a), (c - x) / (c - b))),
            "trapezoidal": lambda x, a, b, c, d: np.maximum(0, np.minimum(np.minimum((x - a) / (b - a), 1.0), (d - x) / (d - c))),
            "sigmoid": lambda x, a, b: 1.0 / (1.0 + np.exp(-a * (x - b)))
        }
    
    def _init_quantum_states(self):
        """Initialize quantum angular momentum states"""
        self.quantum_states = {}
        for l in range(5):  # l = 0, 1, 2, 3, 4
            states = []
            for m in range(-l, l + 1):
                # Spherical harmonic Y_l^m at theta=0 (simplified)
                states.append({
                    'l': l,
                    'm': m,
                    'amplitude': self._spherical_harmonic_amplitude(l, m)
                })
            self.quantum_states[l] = states
    
    def _spherical_harmonic_amplitude(self, l: int, m: int) -> float:
        """Calculate simplified spherical harmonic amplitude"""
        # Simplified calculation for demonstration
        if m == 0:
            return math.sqrt((2 * l + 1) / (4 * math.pi))
        else:
            return math.sqrt((2 * l + 1) / (4 * math.pi) * math.factorial(l - abs(m)) / math.factorial(l + abs(m)))
    
    def analyze_quanta(self, quanta: InformationQuanta) -> Dict[str, Any]:
        """
        Analyze quanta for fuzzy representation
        
        Focuses on uncertainty, graded membership properties, and
        quantum angular momentum characteristics.
        """
        analysis = {
            'recommended_dimensionality': self._determine_quantum_dimensionality(quanta),
            'complexity_assessment': quanta.properties.complexity,
            'fuzziness_level': 0.0,
            'uncertainty_score': 0.0,
            'optimal_membership': self.constraints.membership_function,
            'quantum_number': self.constraints.angular_momentum_quantum,
            'constraint_requirements': {},
            'optimization_opportunities': []
        }
        
        # Analyze data for fuzzy properties
        if isinstance(quanta.data, (list, tuple, np.ndarray)):
            data = np.array(quanta.data, dtype=float)
            
            # Calculate fuzziness level
            analysis['fuzziness_level'] = self._calculate_fuzziness_level(data)
            
            # Calculate uncertainty score
            analysis['uncertainty_score'] = self._calculate_uncertainty_score(data)
            
            # Determine optimal membership function
            best_membership = self._select_optimal_membership_function(data)
            analysis['optimal_membership'] = best_membership
            
            # Determine quantum number
            analysis['quantum_number'] = self._determine_quantum_number(data, quanta.properties.complexity)
        
        # Optimization suggestions
        if analysis['fuzziness_level'] > 0.7:
            analysis['optimization_opportunities'].append('fuzzy_clustering')
        if analysis['uncertainty_score'] > 0.5:
            analysis['optimization_opportunities'].append('uncertainty_reduction')
        if analysis['quantum_number'] > 2:
            analysis['optimization_opportunities'].append('quantum_optimization')
        
        return analysis
    
    def _determine_quantum_dimensionality(self, quanta: InformationQuanta) -> int:
        """Determine dimensionality based on quantum angular momentum"""
        # Fuzzy geometry often uses 3D for spherical harmonics
        base_dim = 3
        
        # Adjust based on complexity
        complexity_factor = quanta.properties.complexity
        
        if complexity_factor < 0.3:
            return 2  # 2D fuzzy representation
        elif complexity_factor < 0.7:
            return 3  # 3D spherical representation
        else:
            return min(5, base_dim + int(math.ceil(complexity_factor * 2)))
    
    def _calculate_fuzziness_level(self, data: np.ndarray) -> float:
        """Calculate how fuzzy the data is"""
        if data.size < 2:
            return 0.0
        
        # Calculate variance as a measure of fuzziness
        variance = np.var(data)
        max_variance = np.max(data) - np.min(data) if data.size > 0 else 1.0
        
        # Normalize fuzziness level
        fuzziness = min(1.0, variance / (max_variance ** 2 + 1e-8))
        
        # Consider data distribution
        if data.size > 10:
            # Check for overlapping regions (indicator of fuzziness)
            hist, _ = np.histogram(data, bins=10)
            non_empty_bins = np.sum(hist > 0)
            overlap_score = 1.0 - (non_empty_bins / 10.0)
            fuzziness = (fuzziness + overlap_score) / 2.0
        
        return fuzziness
    
    def _calculate_uncertainty_score(self, data: np.ndarray) -> float:
        """Calculate uncertainty score using entropy-based measures"""
        if data.size < 2:
            return 0.0
        
        # Calculate Shannon entropy
        hist, _ = np.histogram(data, bins=20)
        hist = hist[hist > 0]  # Remove zero probabilities
        probabilities = hist / np.sum(hist)
        
        if len(probabilities) > 0:
            entropy = -np.sum(probabilities * np.log2(probabilities + 1e-8))
            max_entropy = np.log2(len(probabilities))
            uncertainty = entropy / max_entropy if max_entropy > 0 else 0.0
        else:
            uncertainty = 0.0
        
        return uncertainty
    
    def _select_optimal_membership_function(self, data: np.ndarray) -> str:
        """Select the best membership function for the data"""
        if data.size < 3:
            return "gaussian"
        
        scores = {}
        
        # Test each membership function
        for func_name in ["gaussian", "triangular", "sigmoid"]:
            score = self._evaluate_membership_function(data, func_name)
            scores[func_name] = score
        
        # Return the function with highest score
        return max(scores.keys(), key=lambda k: scores[k])
    
    def _evaluate_membership_function(self, data: np.ndarray, func_name: str) -> float:
        """Evaluate how well a membership function fits the data"""
        if data.size < 3:
            return 0.0
        
        try:
            data_min, data_max = np.min(data), np.max(data)
            
            if func_name == "gaussian":
                # Fit Gaussian parameters
                mu = np.mean(data)
                sigma = np.std(data)
                
                # Calculate fit quality (R²-like measure)
                membership = self.membership_functions["gaussian"](data, mu, sigma)
                
            elif func_name == "triangular":
                # Fit triangular parameters
                a, b, c = data_min, np.mean(data), data_max
                
                membership = self.membership_functions["triangular"](data, a, b, c)
                
            elif func_name == "sigmoid":
                # Fit sigmoid parameters
                b = np.mean(data)
                a = 1.0 / (np.std(data) + 1e-8)
                
                membership = self.membership_functions["sigmoid"](data, a, b)
            
            # Calculate fit quality
            if np.var(data) > 0:
                correlation = np.corrcoef(data, membership)[0, 1]
                return max(0.0, correlation)
            else:
                return 0.5
                
        except:
            return 0.0
    
    def _determine_quantum_number(self, data: np.ndarray, complexity: float) -> int:
        """Determine optimal angular momentum quantum number"""
        # Base quantum number on complexity and data characteristics
        if complexity < 0.2:
            return 0  # s-orbital (spherical)
        elif complexity < 0.5:
            return 1  # p-orbital
        elif complexity < 0.8:
            return 2  # d-orbital
        else:
            return 3  # f-orbital
    
    def generate_sphere(self, quanta: InformationQuanta, 
                       constraints: Optional[GenerationConstraints] = None) -> InformationSphere:
        """
        Generate fuzzy sphere from information quanta
        
        Creates a representation using fuzzy membership functions and
        quantum angular momentum states.
        """
        if constraints is None:
            constraints = GenerationConstraints()
        
        # Analyze the quanta
        analysis = self.analyze_quanta(quanta)
        
        # Generate coordinates using fuzzy quantum principles
        coordinates = self._generate_fuzzy_coordinates(quanta, analysis, constraints)
        
        # Apply fuzzy membership functions
        coordinates = self._apply_fuzzy_membership(coordinates, analysis)
        
        # Create sphere properties
        sphere_properties = self._create_sphere_properties(coordinates, analysis)
        
        # Create the information sphere
        sphere = InformationSphere(
            geometry_type=self.geometry_type,
            coordinates=coordinates,
            properties=sphere_properties,
            quanta_source=quanta,
            generation_metadata={
                'engine': 'Fuzzy',
                'analysis': analysis,
                'constraints': constraints.__dict__ if constraints else {},
                'membership_function': analysis['optimal_membership']
            }
        )
        
        # Optimize if requested
        if constraints and constraints.optimization_goal != "none":
            sphere = self.optimize_representation(sphere, constraints.optimization_goal)
        
        return sphere
    
    def _generate_fuzzy_coordinates(self, quanta: InformationQuanta, 
                                   analysis: Dict[str, Any],
                                   constraints: GenerationConstraints) -> List[TysonCoordinate]:
        """Generate coordinates using fuzzy quantum principles"""
        coordinates = []
        dimensionality = analysis['recommended_dimensionality']
        quantum_number = analysis['quantum_number']
        
        if isinstance(quanta.data, (int, float)):
            # Single value - create fuzzy quantum representation
            value = float(quanta.data)
            
            # Generate points based on quantum angular momentum
            if quantum_number in self.quantum_states:
                states = self.quantum_states[quantum_number]
                
                for i, state in enumerate(states):
                    # Convert quantum state to spatial coordinates
                    theta = math.pi * i / max(1, len(states) - 1) if len(states) > 1 else 0
                    phi = 2 * math.pi * value / max(1, abs(value))
                    
                    # Convert spherical to Cartesian
                    r = state['amplitude']
                    x = r * math.sin(theta) * math.cos(phi)
                    y = r * math.sin(theta) * math.sin(phi)
                    z = r * math.cos(theta)
                    
                    if dimensionality == 2:
                        pos = np.array([x, y])
                    else:
                        pos = np.array([x, y, z])
                    
                    coord = TysonCoordinate(
                        position=pos,
                        geometry_type="fuzzy",
                        metadata={
                            'value': value,
                            'quantum_state': f"l={state['l']}, m={state['m']}",
                            'amplitude': state['amplitude']
                        }
                    )
                    coordinates.append(coord)
        
        elif isinstance(quanta.data, (list, tuple, np.ndarray)):
            data = np.array(quanta.data, dtype=float)
            
            # Generate fuzzy cloud based on data distribution
            n_points = min(30, max(10, int(len(data) * 0.5)))
            
            # Calculate fuzzy parameters
            mu = np.mean(data)
            sigma = np.std(data) + 1e-8
            
            for i in range(n_points):
                # Sample from fuzzy distribution
                if analysis['optimal_membership'] == "gaussian":
                    fuzzy_value = np.random.normal(mu, sigma)
                else:
                    # Uniform sampling with fuzzy bounds
                    fuzzy_value = mu + (np.random.random() - 0.5) * 2 * sigma
                
                # Map to quantum angular momentum coordinates
                theta = math.pi * i / max(1, n_points - 1) if n_points > 1 else 0
                phi = 2 * math.pi * fuzzy_value / max(1, abs(fuzzy_value))
                
                r = 1.0 + 0.1 * np.sin(quantum_number * theta)  # Modulate radius with quantum number
                
                if dimensionality >= 3:
                    x = r * math.sin(theta) * math.cos(phi)
                    y = r * math.sin(theta) * math.sin(phi)
                    z = r * math.cos(theta)
                    pos = np.array([x, y, z])
                else:
                    x = r * math.cos(phi)
                    y = r * math.sin(phi)
                    pos = np.array([x, y])
                
                coord = TysonCoordinate(
                    position=pos,
                    geometry_type="fuzzy",
                    metadata={
                        'sample': i,
                        'fuzzy_value': fuzzy_value,
                        'quantum_number': quantum_number
                    }
                )
                coordinates.append(coord)
        
        else:
            # Default representation for other data types
            data_hash = hash(str(quanta.data))
            seed = abs(data_hash) % 1000
            
            np.random.seed(seed)
            
            # Create fuzzy cloud based on hash
            for i in range(12):
                angle = 2 * math.pi * i / 12
                r = np.random.normal(1.0, 0.2)
                
                if dimensionality >= 3:
                    theta = np.random.uniform(0, math.pi)
                    x = r * math.sin(theta) * math.cos(angle)
                    y = r * math.sin(theta) * math.sin(angle)
                    z = r * math.cos(theta)
                    pos = np.array([x, y, z])
                else:
                    x = r * math.cos(angle)
                    y = r * math.sin(angle)
                    pos = np.array([x, y])
                
                coord = TysonCoordinate(
                    position=pos,
                    geometry_type="fuzzy",
                    metadata={'hash': data_hash, 'index': i}
                )
                coordinates.append(coord)
        
        return coordinates
    
    def _apply_fuzzy_membership(self, coordinates: List[TysonCoordinate], 
                               analysis: Dict[str, Any]) -> List[TysonCoordinate]:
        """Apply fuzzy membership functions to coordinates"""
        if not coordinates:
            return coordinates
        
        membership_func = self.membership_functions[analysis['optimal_membership']]
        fuzziness_param = self.constraints.fuzziness_parameter
        
        # Calculate membership values for each coordinate
        positions = np.array([coord.position for coord in coordinates])
        
        # Apply membership function based on distance from origin
        distances = np.linalg.norm(positions, axis=1)
        
        if analysis['optimal_membership'] == "gaussian":
            mu = np.mean(distances)
            sigma = np.std(distances) + 1e-8
            membership_values = membership_func(distances, mu, sigma * fuzziness_param)
            
        elif analysis['optimal_membership'] == "triangular":
            a, b, c = np.min(distances), np.mean(distances), np.max(distances)
            membership_values = membership_func(distances, a, b, c)
            
        elif analysis['optimal_membership'] == "sigmoid":
            b = np.mean(distances)
            a = 1.0 / (np.std(distances) + 1e-8) * fuzziness_param
            membership_values = membership_func(distances, a, b)
        
        else:
            membership_values = np.ones_like(distances) * 0.5  # Default fuzzy value
        
        # Update coordinates with membership information
        fuzzy_coordinates = []
        
        for i, coord in enumerate(coordinates):
            fuzzy_coord = TysonCoordinate(
                position=coord.position.copy(),
                geometry_type=coord.geometry_type,
                metadata={
                    **coord.metadata,
                    'membership_value': membership_values[i],
                    'fuzziness_parameter': fuzziness_param,
                    'membership_function': analysis['optimal_membership']
                }
            )
            fuzzy_coordinates.append(fuzzy_coord)
        
        return fuzzy_coordinates
    
    def _create_sphere_properties(self, coordinates: List[TysonCoordinate], 
                                 analysis: Dict[str, Any]) -> 'SphereProperties':
        """Create sphere properties based on fuzzy quantum principles"""
        from ..core.geometry_base import SphereProperties
        
        if not coordinates:
            return SphereProperties()
        
        positions = np.array([coord.position for coord in coordinates])
        
        # Calculate fuzzy-specific properties
        center = np.mean(positions, axis=0)
        distances = np.linalg.norm(positions - center, axis=1)
        radius = np.max(distances) if len(distances) > 0 else 1.0
        
        # Calculate fuzzy density based on membership values
        membership_values = [coord.metadata.get('membership_value', 0.5) for coord in coordinates]
        fuzzy_density = np.mean(membership_values)
        
        # Calculate curvature (fuzzy spaces have variable curvature)
        curvature = self.constraints.fuzziness_parameter * 0.5
        
        # Calculate volume with fuzzy boundaries
        dimensionality = positions.shape[1]
        effective_radius = radius * (1.0 + self.constraints.fuzziness_parameter)
        volume = (math.pi ** (dimensionality/2)) * (effective_radius ** dimensionality) / math.gamma(dimensionality/2 + 1)
        
        return SphereProperties(
            radius=radius,
            center=center,
            curvature=curvature,
            volume=volume,
            density=fuzzy_density,
            dimensionality=dimensionality,
            constraints={
                'membership_function': analysis['optimal_membership'],
                'fuzziness_parameter': self.constraints.fuzziness_parameter,
                'quantum_number': analysis['quantum_number'],
                'uncertainty_principle': self.constraints.uncertainty_principle
            },
            metadata={
                'fuzziness_level': analysis['fuzziness_level'],
                'uncertainty_score': analysis['uncertainty_score'],
                'quantum_coherence': self.constraints.quantum_coherence
            }
        )
    
    def calculate_distance(self, coord1: TysonCoordinate, coord2: TysonCoordinate) -> float:
        """Calculate fuzzy distance with uncertainty considerations"""
        # Standard Euclidean distance
        euclidean_dist = np.linalg.norm(coord1.position - coord2.position)
        
        # Apply fuzzy membership-based modification
        membership1 = coord1.metadata.get('membership_value', 0.5)
        membership2 = coord2.metadata.get('membership_value', 0.5)
        
        # Fuzzy distance is modified by membership values
        fuzzy_factor = 1.0 + (1.0 - membership1) * (1.0 - membership2) * self.constraints.fuzziness_parameter
        
        return euclidean_dist * fuzzy_factor
    
    def optimize_representation(self, sphere: InformationSphere, 
                                goal: str = "balance") -> InformationSphere:
        """Optimize sphere representation for specific goal"""
        if goal == "accuracy":
            # Optimize for fuzzy membership accuracy
            optimized_coords = self._optimize_fuzzy_membership(sphere.coordinates)
        elif goal == "speed":
            # Reduce fuzzy complexity
            optimized_coords = self._reduce_fuzzy_complexity(sphere.coordinates)
        else:  # balance
            optimized_coords = self._balance_fuzzy_optimization(sphere.coordinates)
        
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
    
    def _optimize_fuzzy_membership(self, coordinates: List[TysonCoordinate]) -> List[TysonCoordinate]:
        """Optimize for better fuzzy membership distribution"""
        if len(coordinates) < 3:
            return coordinates
        
        # Adjust positions to improve membership distribution
        optimized = []
        membership_values = [coord.metadata.get('membership_value', 0.5) for coord in coordinates]
        
        for i, coord in enumerate(coordinates):
            pos = coord.position.copy()
            
            # Move points with low membership toward center
            if membership_values[i] < 0.3:
                center = np.mean([c.position for c in coordinates], axis=0)
                direction = center - pos
                pos = pos + 0.1 * direction
            
            optimized_coord = TysonCoordinate(
                position=pos,
                geometry_type=coord.geometry_type,
                metadata={**coord.metadata, 'membership_optimized': True}
            )
            optimized.append(optimized_coord)
        
        return optimized
    
    def _reduce_fuzzy_complexity(self, coordinates: List[TysonCoordinate]) -> List[TysonCoordinate]:
        """Reduce fuzzy complexity while preserving essential features"""
        if len(coordinates) <= 8:
            return coordinates
        
        # Keep points with highest membership values
        membership_values = [(coord.metadata.get('membership_value', 0.5), i, coord) 
                            for i, coord in enumerate(coordinates)]
        membership_values.sort(reverse=True)
        
        # Select top points
        selected = [item[2] for item in membership_values[:12]]
        
        return selected
    
    def _balance_fuzzy_optimization(self, coordinates: List[TysonCoordinate]) -> List[TysonCoordinate]:
        """Balance fuzzy optimization goals"""
        target_count = max(8, min(16, len(coordinates)))
        
        if len(coordinates) <= target_count:
            return coordinates
        
        # Select points evenly distributed in membership space
        membership_values = [coord.metadata.get('membership_value', 0.5) for coord in coordinates]
        indices = np.argsort(membership_values)
        
        # Select evenly spaced indices
        step = len(coordinates) // target_count
        selected_indices = indices[::step][:target_count]
        
        return [coordinates[i] for i in selected_indices]
    
    def validate_constraints(self, sphere: InformationSphere) -> bool:
        """Validate fuzzy specific constraints"""
        valid, errors = self.validator.validate_sphere(sphere.coordinates)
        
        if not valid:
            return False
        
        # Validate membership values are in valid range
        for coord in sphere.coordinates:
            membership = coord.metadata.get('membership_value', 0.5)
            if not (0.0 <= membership <= 1.0):
                return False
        
        # Check uncertainty principle if required
        if self.constraints.uncertainty_principle:
            positions = np.array([coord.position for coord in sphere.coordinates])
            if positions.shape[0] > 1:
                # Calculate position and momentum uncertainty (simplified)
                pos_uncertainty = np.std(positions)
                
                # Simplified momentum uncertainty based on position differences
                momentum_uncertainty = 0.0
                for i in range(len(positions) - 1):
                    momentum_uncertainty += np.linalg.norm(positions[i+1] - positions[i])
                momentum_uncertainty /= max(1, len(positions) - 1)
                
                # Uncertainty principle: σ_x * σ_p ≥ ℏ/2 (simplified)
                if pos_uncertainty * momentum_uncertainty < 0.1:  # Simplified threshold
                    return False
        
        return True