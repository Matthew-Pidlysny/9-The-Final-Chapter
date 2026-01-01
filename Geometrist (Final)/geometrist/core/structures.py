"""
Core Data Structures

Common data structures used throughout the Geometrist system
for representing information spheres, adjacency fields, and navigation paths.
"""

from typing import List, Dict, Any, Optional, Tuple, Set
from dataclasses import dataclass, field
import numpy as np
from enum import Enum, auto

from .quanta import InformationQuanta
from .coordinates import TysonCoordinate
from .geometry_base import GeometryType, SphereProperties


class StructureType(Enum):
    """Types of geometric structures"""
    SPHERE = auto()
    FIELD = auto()
    PATH = auto()
    NETWORK = auto()
    HYPERCOMPLEX = auto()


@dataclass
class GeometricConstraints:
    """Constraints that apply to geometric structures"""
    max_dimensionality: int = 10
    max_radius: float = 1000.0
    min_separation: float = 0.001
    symmetry_requirements: List[str] = field(default_factory=list)
    forbidden_configurations: List[str] = field(default_factory=list)
    continuity_requirements: bool = True
    smoothness_threshold: float = 0.1


@dataclass
class OptimizationTarget:
    """Target for optimization procedures"""
    metric: str  # "distance", "complexity", "density", "entropy"
    direction: str  # "minimize", "maximize"
    weight: float = 1.0
    constraints: Dict[str, Any] = field(default_factory=dict)


@dataclass
class InformationSphere:
    """Represents an information sphere with geometric properties"""
    geometry_type: GeometryType
    coordinates: List[TysonCoordinate]
    properties: SphereProperties
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def __post_init__(self):
        """Initialize derived properties"""
        if not self.coordinates:
            self.coordinates = []
        
        if not self.properties:
            self.properties = SphereProperties()
        
        # Calculate derived properties
        self._calculate_derived_properties()
    
    def _calculate_derived_properties(self):
        """Calculate derived properties from coordinates"""
        if not self.coordinates:
            return
        
        positions = np.array([coord.position for coord in self.coordinates])
        
        # Update center
        if positions.size > 0:
            self.properties.center = np.mean(positions, axis=0)
            
            # Update radius
            distances = [np.linalg.norm(pos - self.properties.center) for pos in positions]
            self.properties.radius = max(distances) if distances else 0.0
            
            # Update volume (simplified)
            self.properties.volume = self._calculate_volume()
            
            # Update surface area (simplified)
            self.properties.surface_area = self._calculate_surface_area()
    
    def _calculate_volume(self) -> float:
        """Calculate volume of the sphere"""
        if self.properties.dimensionality == 1:
            return 2 * self.properties.radius  # Length
        elif self.properties.dimensionality == 2:
            return np.pi * self.properties.radius ** 2  # Area
        elif self.properties.dimensionality == 3:
            return (4/3) * np.pi * self.properties.radius ** 3  # Volume
        else:
            # Higher dimensions (simplified)
            return self.properties.radius ** self.properties.dimensionality
    
    def _calculate_surface_area(self) -> float:
        """Calculate surface area of the sphere"""
        if self.properties.dimensionality == 1:
            return 2  # Two endpoints
        elif self.properties.dimensionality == 2:
            return 2 * np.pi * self.properties.radius  # Circumference
        elif self.properties.dimensionality == 3:
            return 4 * np.pi * self.properties.radius ** 2  # Surface area
        else:
            # Higher dimensions (simplified)
            return self.properties.radius ** (self.properties.dimensionality - 1)


@dataclass
class AdjacencyField:
    """Represents adjacency relationships between coordinates"""
    source_coordinate: TysonCoordinate
    adjacent_coordinates: List[TysonCoordinate]
    weights: List[float]
    field_type: str = "default"
    
    def __post_init__(self):
        """Initialize derived properties"""
        if len(self.adjacent_coordinates) != len(self.weights):
            # Default weights if not provided
            self.weights = [1.0] * len(self.adjacent_coordinates)


@dataclass
class NavigationPath:
    """Represents a navigation path through coordinates"""
    coordinates: List[TysonCoordinate]
    total_distance: float = 0.0
    path_type: str = "default"
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def __post_init__(self):
        """Calculate total distance if not provided"""
        if self.total_distance == 0.0 and len(self.coordinates) > 1:
            self.total_distance = self._calculate_total_distance()
    
    def _calculate_total_distance(self) -> float:
        """Calculate total distance of the path"""
        if len(self.coordinates) < 2:
            return 0.0
        
        total = 0.0
        for i in range(len(self.coordinates) - 1):
            if hasattr(self.coordinates[i], 'distance_to'):
                total += self.coordinates[i].distance_to(self.coordinates[i + 1])
            else:
                total += np.linalg.norm(self.coordinates[i].position - self.coordinates[i + 1].position)
        
        return total


class StructureValidator:
    """Validates geometric structures against constraints"""
    
    def __init__(self, constraints: GeometricConstraints):
        self.constraints = constraints
    
    def validate_sphere(self, coordinates: List[TysonCoordinate]) -> Tuple[bool, List[str]]:
        """Validate a sphere structure"""
        errors = []
        
        if not coordinates:
            errors.append("Sphere has no coordinates")
            return False, errors
        
        # Check dimensionality
        dims = [coord.position.size for coord in coordinates]
        if max(dims) > self.constraints.max_dimensionality:
            errors.append(f"Dimensionality {max(dims)} exceeds maximum {self.constraints.max_dimensionality}")
        
        # Check radius
        positions = np.array([coord.position for coord in coordinates])
        center = np.mean(positions, axis=0)
        radii = [np.linalg.norm(pos - center) for pos in positions]
        if max(radii) > self.constraints.max_radius:
            errors.append(f"Maximum radius {max(radii)} exceeds limit {self.constraints.max_radius}")
        
        # Check minimum separation
        for i, coord1 in enumerate(coordinates):
            for coord2 in coordinates[i+1:]:
                if hasattr(coord1, 'distance_to'):
                    if coord1.distance_to(coord2) < self.constraints.min_separation:
                        errors.append(f"Coordinates too close: {coord1.distance_to(coord2)} < {self.constraints.min_separation}")
                else:
                    distance = np.linalg.norm(coord1.position - coord2.position)
                    if distance < self.constraints.min_separation:
                        errors.append(f"Coordinates too close: {distance} < {self.constraints.min_separation}")
        
        return len(errors) == 0, errors
    
    def validate_path(self, path: List[TysonCoordinate]) -> Tuple[bool, List[str]]:
        """Validate a navigation path"""
        errors = []
        
        if len(path) < 2:
            errors.append("Path must have at least 2 coordinates")
            return False, errors
        
        # Check continuity
        for i in range(len(path) - 1):
            if path[i].geometry_type != path[i+1].geometry_type:
                errors.append(f"Geometry type mismatch at segment {i}")
        
        # Check smoothness if required
        if self.constraints.continuity_requirements:
            for i in range(1, len(path) - 1):
                # Calculate angle at each point
                v1 = path[i].position - path[i-1].position
                v2 = path[i+1].position - path[i].position
                
                if np.linalg.norm(v1) > 0 and np.linalg.norm(v2) > 0:
                    cos_angle = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
                    angle = np.arccos(np.clip(cos_angle, -1, 1))
                    
                    if angle < np.pi - self.constraints.smoothness_threshold:
                        errors.append(f"Path too sharp at segment {i}: angle {angle:.2f} < threshold {np.pi - self.constraints.smoothness_threshold:.2f}")
        
        return len(errors) == 0, errors


class StructureOptimizer:
    """Optimizes geometric structures for various objectives"""
    
    def __init__(self):
        self.optimization_history = []
    
    def optimize_sphere(self, coordinates: List[TysonCoordinate], 
                       targets: List[OptimizationTarget]) -> List[TysonCoordinate]:
        """Optimize sphere coordinates for multiple targets"""
        optimized_coords = coordinates.copy()
        
        # Simple optimization - could be more sophisticated
        for target in targets:
            if target.metric == "distance":
                optimized_coords = self._optimize_distance(optimized_coords, target)
            elif target.metric == "complexity":
                optimized_coords = self._optimize_complexity(optimized_coords, target)
        
        return optimized_coords
    
    def _optimize_distance(self, coordinates: List[TysonCoordinate], 
                          target: OptimizationTarget) -> List[TysonCoordinate]:
        """Optimize for minimal distance"""
        # Simple implementation - could use gradient descent
        return coordinates
    
    def _optimize_complexity(self, coordinates: List[TysonCoordinate], 
                            target: OptimizationTarget) -> List[TysonCoordinate]:
        """Optimize for complexity"""
        # Simple implementation
        return coordinates