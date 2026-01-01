"""
Base Geometry Engine Interface

Provides the abstract foundation for all geometry engines in the
Geometrist system, defining common interfaces and behaviors.
"""

from abc import ABC, abstractmethod
from enum import Enum, auto
from typing import Any, Dict, List, Optional, Tuple, Union
from dataclasses import dataclass, field
import numpy as np

from .quanta import InformationQuanta
from .coordinates import TysonCoordinate


class GeometryType(Enum):
    """Supported geometry types in the Geometrist system"""
    HADWIGER_NELSON = auto()    # Trigonometric polynomials with forbidden angles
    BANACHIAN = auto()          # Complete normed vector space
    FUZZY = auto()              # Quantum angular momentum states
    QUANTUM = auto()            # q-deformed classical sphere (Podleś)
    RELATIONAL = auto()         # Meta-sphere synthesizing all four


@dataclass
class SphereProperties:
    """Properties that characterize an information sphere"""
    radius: float = 1.0
    center: np.ndarray = field(default_factory=lambda: np.array([0.0]))
    curvature: float = 0.0       # Gaussian curvature
    volume: float = 0.0          # n-dimensional volume
    surface_area: float = 0.0    # Surface area/volume ratio
    density: float = 1.0         # Information density
    dimensionality: int = 1
    constraints: Dict[str, Any] = field(default_factory=dict)
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class GenerationConstraints:
    """Constraints for sphere generation"""
    max_radius: float = 100.0
    min_radius: float = 0.001
    max_complexity: float = 1.0
    target_dimensions: Optional[int] = None
    optimization_goal: str = "balance"  # "speed", "accuracy", "balance"
    memory_limit: Optional[int] = None
    time_limit: Optional[float] = None


class GeometryEngine(ABC):
    """
    Abstract base class for all geometry engines
    
    Each geometry engine implements specific mathematical rules for
    representing and navigating information in its geometric space.
    """
    
    def __init__(self, geometry_type: GeometryType):
        self.geometry_type = geometry_type
        self.constraints = {}
        self.optimization_cache = {}
    
    @abstractmethod
    def analyze_quanta(self, quanta: InformationQuanta) -> Dict[str, Any]:
        """
        Analyze information quanta to determine geometric representation needs
        
        Returns analysis results including:
        - Recommended dimensionality
        - Complexity assessment
        - Constraint requirements
        - Optimization opportunities
        """
        pass
    
    @abstractmethod
    def generate_sphere(self, quanta: InformationQuanta, 
                       constraints: Optional[GenerationConstraints] = None) -> 'InformationSphere':
        """
        Generate an information sphere from the given quanta
        
        Creates the optimal geometric representation for the information
        within the specified constraints.
        """
        pass
    
    @abstractmethod
    def calculate_distance(self, coord1: TysonCoordinate, 
                          coord2: TysonCoordinate) -> float:
        """Calculate distance between two coordinates in this geometry"""
        pass
    
    @abstractmethod
    def optimize_representation(self, sphere: 'InformationSphere', 
                                goal: str = "balance") -> 'InformationSphere':
        """
        Optimize the sphere representation for a specific goal
        
        Goals:
        - "speed": Optimize for fast computation
        - "accuracy": Optimize for precision
        - "balance": Balance between speed and accuracy
        """
        pass
    
    @abstractmethod
    def validate_constraints(self, sphere: 'InformationSphere') -> bool:
        """Validate that a sphere satisfies all geometric constraints"""
        pass
    
    def get_geometry_info(self) -> Dict[str, Any]:
        """Get information about this geometry engine"""
        return {
            'type': self.geometry_type.name,
            'description': self.__doc__,
            'constraints': self.constraints,
            'optimization_cache_size': len(self.optimization_cache)
        }
    
    def clear_cache(self):
        """Clear optimization cache"""
        self.optimization_cache.clear()


@dataclass
class InformationSphere:
    """Represents an information sphere in a specific geometry"""
    geometry_type: GeometryType
    coordinates: List[TysonCoordinate]
    properties: SphereProperties
    quanta_source: InformationQuanta
    generation_metadata: Dict[str, Any] = field(default_factory=dict)
    
    def __post_init__(self):
        """Initialize derived properties"""
        if not self.coordinates:
            self.coordinates = [TysonCoordinate(
                position=self.properties.center,
                geometry_type=self.geometry_type.name.lower()
            )]
        
        # Calculate derived properties
        self._calculate_derived_properties()
    
    def _calculate_derived_properties(self):
        """Calculate derived properties from coordinates"""
        if not self.coordinates:
            return
        
        # Calculate center of mass
        positions = np.array([coord.position for coord in self.coordinates])
        self.properties.center = np.mean(positions, axis=0)
        
        # Calculate maximum radius
        distances = [np.linalg.norm(coord.position - self.properties.center) 
                    for coord in self.coordinates]
        self.properties.radius = max(distances) if distances else 1.0
        
        # Calculate dimensionality
        if self.coordinates:
            self.properties.dimensionality = self.coordinates[0].position.size
        
        # Calculate density (information per unit volume)
        if self.properties.radius > 0:
            # Approximate volume in n-dimensions
            n = self.properties.dimensionality
            self.properties.volume = (np.pi ** (n/2)) * (self.properties.radius ** n) / np.gamma(n/2 + 1)
            self.properties.density = len(self.coordinates) / max(self.properties.volume, 1e-8)
    
    def add_coordinate(self, coordinate: TysonCoordinate):
        """Add a new coordinate to the sphere"""
        if coordinate.geometry_type.lower() != self.geometry_type.name.lower():
            raise ValueError(f"Coordinate geometry type mismatch: {coordinate.geometry_type} != {self.geometry_type}")
        
        self.coordinates.append(coordinate)
        self._calculate_derived_properties()
    
    def get_coordinate_at_index(self, index: int) -> Optional[TysonCoordinate]:
        """Get coordinate at specific index"""
        if 0 <= index < len(self.coordinates):
            return self.coordinates[index]
        return None
    
    def find_nearest_coordinate(self, target: TysonCoordinate) -> Tuple[TysonCoordinate, int]:
        """Find the nearest coordinate to target"""
        if not self.coordinates:
            raise ValueError("Sphere has no coordinates")
        
        distances = [(coord.distance_to(target), i) for i, coord in enumerate(self.coordinates)]
        min_dist, min_idx = min(distances)
        return self.coordinates[min_idx], min_idx
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert sphere to dictionary representation"""
        return {
            'geometry_type': self.geometry_type.name,
            'coordinates': [coord.to_dict() for coord in self.coordinates],
            'properties': {
                'radius': self.properties.radius,
                'center': self.properties.center.tolist(),
                'curvature': self.properties.curvature,
                'volume': self.properties.volume,
                'surface_area': self.properties.surface_area,
                'density': self.properties.density,
                'dimensionality': self.properties.dimensionality,
                'constraints': self.properties.constraints,
                'metadata': self.properties.metadata
            },
            'quanta_source': self.quanta_source.to_dict(),
            'generation_metadata': self.generation_metadata
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'InformationSphere':
        """Create sphere from dictionary representation"""
        from .quanta import InformationQuanta
        
        coordinates = [TysonCoordinate.from_dict(coord_data) 
                      for coord_data in data['coordinates']]
        
        properties = SphereProperties(
            radius=data['properties']['radius'],
            center=np.array(data['properties']['center']),
            curvature=data['properties']['curvature'],
            volume=data['properties']['volume'],
            surface_area=data['properties']['surface_area'],
            density=data['properties']['density'],
            dimensionality=data['properties']['dimensionality'],
            constraints=data['properties']['constraints'],
            metadata=data['properties']['metadata']
        )
        
        quanta_source = InformationQuanta.from_dict(data['quanta_source'])
        
        return cls(
            geometry_type=GeometryType[data['geometry_type']],
            coordinates=coordinates,
            properties=properties,
            quanta_source=quanta_source,
            generation_metadata=data['generation_metadata']
        )
    
    def __str__(self) -> str:
        return f"InformationSphere({self.geometry_type.name}, {len(self.coordinates)} points, r={self.properties.radius:.2f})"
    
    def __repr__(self) -> str:
        return self.__str__()


@dataclass
class AdjacencyField:
    """Represents adjacency relationships between coordinates"""
    source_coordinate: TysonCoordinate
    adjacent_coordinates: List[TysonCoordinate]
    weights: List[float]
    field_type: str = "reciprocal"
    
    def __post_init__(self):
        """Initialize derived properties"""
        if len(self.adjacent_coordinates) != len(self.weights):
            # Default to equal weights
            self.weights = [1.0 / len(self.adjacent_coordinates)] * len(self.adjacent_coordinates)
    
    def get_weighted_average(self) -> TysonCoordinate:
        """Calculate weighted average of adjacent coordinates"""
        if not self.adjacent_coordinates:
            return self.source_coordinate
        
        weighted_sum = np.zeros_like(self.source_coordinate.position)
        for coord, weight in zip(self.adjacent_coordinates, self.weights):
            weighted_sum += coord.position * weight
        
        return TysonCoordinate(
            position=weighted_sum,
            geometry_type=self.source_coordinate.geometry_type,
            metadata={'operation': 'weighted_average', 'field_type': self.field_type}
        )


@dataclass
class NavigationPath:
    """Represents a navigation path through coordinates"""
    coordinates: List[TysonCoordinate]
    path_type: str = "optimal"
    total_distance: float = 0.0
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def __post_init__(self):
        """Calculate total distance"""
        if len(self.coordinates) > 1:
            self.total_distance = sum(
                self.coordinates[i].distance_to(self.coordinates[i+1])
                for i in range(len(self.coordinates)-1)
            )
    
    def interpolate_position(self, t: float) -> Optional[TysonCoordinate]:
        """Get position at parameter t (0 to 1) along path"""
        if not self.coordinates:
            return None
        
        if t <= 0.0:
            return self.coordinates[0]
        if t >= 1.0:
            return self.coordinates[-1]
        
        # Find segment and interpolate
        segment_length = len(self.coordinates) - 1
        segment_pos = t * segment_length
        segment_idx = int(segment_pos)
        local_t = segment_pos - segment_idx
        
        if segment_idx >= segment_length:
            return self.coordinates[-1]
        
        return self.coordinates[segment_idx].interpolate(
            self.coordinates[segment_idx + 1], local_t
        )