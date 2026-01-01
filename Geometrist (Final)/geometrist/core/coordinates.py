"""
Tyson Co-Ordinate System

Universal navigation system for information spheres that works across
all geometry types through four fundamental operations.
"""

from enum import Enum, auto
from typing import List, Tuple, Optional, Union, Any, Dict
from dataclasses import dataclass, field
import numpy as np
import math
from abc import ABC, abstractmethod


class CoordinateOperation(Enum):
    """Four fundamental operations of Tyson Co-Ordinate system"""
    ADDITION = auto()       # Combine positions
    SUBTRACTION = auto()    # Find differences
    MULTIPLICATION = auto   # Scale positions
    RECIPROCAL = auto       # Invert positions


@dataclass
class TysonCoordinate:
    """
    Universal coordinate representation for navigation in information spheres
    
    Tyson coordinates provide a unified way to navigate across different
    geometry types through four fundamental operations.
    """
    position: np.ndarray
    geometry_type: str
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def __post_init__(self):
        """Initialize derived properties"""
        if isinstance(self.position, list):
            self.position = np.array(self.position, dtype=float)
        
        # Validate position
        if not isinstance(self.position, np.ndarray):
            raise ValueError("Position must be a numpy array")
        
        if self.position.size == 0:
            raise ValueError("Position cannot be empty")
    
    def addition(self, other: 'TysonCoordinate') -> 'TysonCoordinate':
        """
        ADDITION operation: Combine two positions
        
        Combines the geometric properties of both coordinates to create
        a new position that incorporates both informational states.
        """
        if self.geometry_type != other.geometry_type:
            raise ValueError("Cannot add coordinates from different geometry types")
        
        # Geometry-specific addition strategies
        if self.geometry_type == "banachian":
            # Banachian addition uses vector addition with norm preservation
            combined_position = self.position + other.position
            # Normalize to maintain Banachian space properties
            norm = np.linalg.norm(combined_position)
            if norm > 0:
                combined_position = combined_position / norm * min(norm, 1.0)
        
        elif self.geometry_type == "quantum":
            # Quantum addition uses superposition principles
            combined_position = self.position * 0.707 + other.position * 0.707
            # Normalize for quantum state
            norm = np.linalg.norm(combined_position)
            if norm > 0:
                combined_position = combined_position / norm
        
        elif self.geometry_type == "fuzzy":
            # Fuzzy addition uses weighted averaging
            combined_position = (self.position + other.position) / 2.0
        
        elif self.geometry_type == "hadwiger_nelson":
            # Hadwiger-Nelson addition maintains angular constraints
            combined_position = self._constrain_angle(self.position + other.position)
        
        else:  # relational or default
            combined_position = self.position + other.position
        
        return TysonCoordinate(
            position=combined_position,
            geometry_type=self.geometry_type,
            metadata={'operation': 'addition', 'sources': [self.metadata.get('id', ''), other.metadata.get('id', '')]}
        )
    
    def subtraction(self, other: 'TysonCoordinate') -> 'TysonCoordinate':
        """
        SUBTRACTION operation: Find the difference between positions
        
        Computes the informational distance and creates a coordinate
        representing the transition between states.
        """
        if self.geometry_type != other.geometry_type:
            raise ValueError("Cannot subtract coordinates from different geometry types")
        
        if self.geometry_type == "banachian":
            # Banachian subtraction uses metric space properties
            diff_position = self.position - other.position
            # Apply metric transformation
            diff_position = np.tanh(diff_position)  # Bound the difference
        
        elif self.geometry_type == "quantum":
            # Quantum subtraction uses inner product principles
            overlap = np.dot(self.position, other.position)
            diff_position = self.position - overlap * other.position
        
        elif self.geometry_type == "fuzzy":
            # Fuzzy subtraction uses fuzzy difference
            diff_position = np.abs(self.position - other.position)
        
        elif self.geometry_type == "hadwiger_nelson":
            # Hadwiger-Nelson subtraction maintains angular constraints
            diff_position = self._constrain_angle(self.position - other.position)
        
        else:  # relational or default
            diff_position = self.position - other.position
        
        return TysonCoordinate(
            position=diff_position,
            geometry_type=self.geometry_type,
            metadata={'operation': 'subtraction', 'sources': [self.metadata.get('id', ''), other.metadata.get('id', '')]}
        )
    
    def multiplication(self, scalar: Union[float, np.ndarray]) -> 'TysonCoordinate':
        """
        MULTIPLICATION operation: Scale position by scalar or vector
        
        Applies scaling transformation to expand or contract the
        informational space while maintaining geometry constraints.
        """
        if self.geometry_type == "banachian":
            # Banachian multiplication preserves norm properties
            scaled_position = self.position * scalar
            # Re-normalize to maintain Banachian space
            norm = np.linalg.norm(scaled_position)
            if norm > 0:
                scaled_position = scaled_position / norm * min(abs(scalar) * np.linalg.norm(self.position), 1.0)
        
        elif self.geometry_type == "quantum":
            # Quantum multiplication uses phase and amplitude
            if isinstance(scalar, (int, float)):
                scaled_position = self.position * scalar
                # Renormalize quantum state
                norm = np.linalg.norm(scaled_position)
                if norm > 0:
                    scaled_position = scaled_position / norm
            else:
                # Vector multiplication changes quantum state
                scaled_position = self.position * scalar
        
        elif self.geometry_type == "fuzzy":
            # Fuzzy multiplication uses fuzzy scaling
            scaled_position = self.position * scalar
            # Apply fuzzy membership constraints
            scaled_position = np.clip(scaled_position, 0, 1)
        
        elif self.geometry_type == "hadwiger_nelson":
            # Hadwiger-Nelson multiplication maintains angular constraints
            scaled_position = self._constrain_angle(self.position * scalar)
        
        else:  # relational or default
            scaled_position = self.position * scalar
        
        return TysonCoordinate(
            position=scaled_position,
            geometry_type=self.geometry_type,
            metadata={'operation': 'multiplication', 'scalar': scalar}
        )
    
    def reciprocal(self) -> 'TysonCoordinate':
        """
        RECIPROCAL operation: Invert the position
        
        Creates the complementary coordinate that represents the
        inverse informational state.
        """
        if self.geometry_type == "banachian":
            # Banachian reciprocal uses dual space
            norm = np.linalg.norm(self.position)
            if norm > 1e-8:
                reciprocal_position = self.position / (norm ** 2)
            else:
                reciprocal_position = np.zeros_like(self.position)
        
        elif self.geometry_type == "quantum":
            # Quantum reciprocal uses conjugate transpose
            reciprocal_position = np.conj(self.position)
        
        elif self.geometry_type == "fuzzy":
            # Fuzzy reciprocal uses complement
            reciprocal_position = 1.0 - self.position
            reciprocal_position = np.clip(reciprocal_position, 0, 1)
        
        elif self.geometry_type == "hadwiger_nelson":
            # Hadwiger-Nelson reciprocal reflects through origin
            reciprocal_position = self._constrain_angle(-self.position)
        
        else:  # relational or default
            # Safe reciprocal with handling of zeros
            reciprocal_position = np.where(
                np.abs(self.position) > 1e-8,
                1.0 / self.position,
                0.0
            )
        
        return TysonCoordinate(
            position=reciprocal_position,
            geometry_type=self.geometry_type,
            metadata={'operation': 'reciprocal'}
        )
    
    def _constrain_angle(self, position: np.ndarray) -> np.ndarray:
        """Apply Hadwiger-Nelson angular constraints"""
        if position.size >= 2:
            # Example constraint: avoid certain angles (simplified)
            x, y = position[0], position[1]
            angle = math.atan2(y, x)
            
            # Forbidden angles (simplified example)
            forbidden_angles = [math.pi/4, 3*math.pi/4, 5*math.pi/4, 7*math.pi/4]
            tolerance = 0.1
            
            for forbidden in forbidden_angles:
                if abs(angle - forbidden) < tolerance:
                    # Adjust angle to avoid forbidden region
                    angle += tolerance * np.sign(angle - forbidden)
            
            # Reconstruct position with constrained angle
            radius = math.sqrt(x**2 + y**2)
            position = np.array([radius * math.cos(angle), radius * math.sin(angle)])
            if self.position.size > 2:
                position = np.concatenate([position, position[2:]])
        
        return position
    
    def distance_to(self, other: 'TysonCoordinate') -> float:
        """Calculate distance to another coordinate"""
        if self.geometry_type != other.geometry_type:
            raise ValueError("Cannot calculate distance between different geometry types")
        
        if self.geometry_type == "banachian":
            return np.linalg.norm(self.position - other.position)
        
        elif self.geometry_type == "quantum":
            # Quantum distance uses inner product
            overlap = abs(np.dot(self.position, other.position))
            return math.acos(min(1.0, overlap))
        
        elif self.geometry_type == "fuzzy":
            # Fuzzy distance uses fuzzy metric
            return np.mean(np.abs(self.position - other.position))
        
        else:  # default Euclidean distance
            return np.linalg.norm(self.position - other.position)
    
    def interpolate(self, other: 'TysonCoordinate', t: float) -> 'TysonCoordinate':
        """Interpolate between this coordinate and another"""
        if self.geometry_type != other.geometry_type:
            raise ValueError("Cannot interpolate between different geometry types")
        
        if self.geometry_type == "quantum":
            # Quantum interpolation uses geodesic on unit sphere
            angle = self.distance_to(other)
            if angle < 1e-8:
                return self
            
            return TysonCoordinate(
                position=(math.sin((1-t)*angle)/math.sin(angle)) * self.position + 
                        (math.sin(t*angle)/math.sin(angle)) * other.position,
                geometry_type=self.geometry_type,
                metadata={'operation': 'interpolation', 't': t}
            )
        
        else:  # Linear interpolation for other geometries
            interpolated = (1-t) * self.position + t * other.position
            return TysonCoordinate(
                position=interpolated,
                geometry_type=self.geometry_type,
                metadata={'operation': 'interpolation', 't': t}
            )
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary representation"""
        return {
            'position': self.position.tolist(),
            'geometry_type': self.geometry_type,
            'metadata': self.metadata
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'TysonCoordinate':
        """Create from dictionary representation"""
        return cls(
            position=np.array(data['position']),
            geometry_type=data['geometry_type'],
            metadata=data['metadata']
        )
    
    def __str__(self) -> str:
        return f"TysonCoordinate({self.geometry_type}, pos={self.position})"
    
    def __repr__(self) -> str:
        return self.__str__()


class NavigationStrategy(ABC):
    """Abstract base class for navigation strategies"""
    
    @abstractmethod
    def plan_path(self, start: TysonCoordinate, goal: TysonCoordinate, 
                  constraints: Dict[str, Any]) -> List[TysonCoordinate]:
        """Plan a navigation path from start to goal"""
        pass


class DirectNavigation(NavigationStrategy):
    """Direct navigation using Tyson operations"""
    
    def plan_path(self, start: TysonCoordinate, goal: TysonCoordinate, 
                  constraints: Dict[str, Any]) -> List[TysonCoordinate]:
        """Plan direct path using Tyson operations"""
        steps = constraints.get('steps', 10)
        path = []
        
        for i in range(steps + 1):
            t = i / steps
            intermediate = start.interpolate(goal, t)
            path.append(intermediate)
        
        return path


class GreedyNavigation(NavigationStrategy):
    """Greedy navigation optimization"""
    
    def plan_path(self, start: TysonCoordinate, goal: TysonCoordinate, 
                  constraints: Dict[str, Any]) -> List[TysonCoordinate]:
        """Plan greedy optimized path"""
        path = [start]
        current = start
        max_iterations = constraints.get('max_iterations', 100)
        tolerance = constraints.get('tolerance', 0.01)
        
        for iteration in range(max_iterations):
            # Calculate direction to goal
            direction = current.subtraction(goal)
            
            # Take a step towards goal
            step_size = 0.1 * (1.0 - iteration / max_iterations)
            next_coord = current.addition(direction.multiplication(-step_size))
            
            path.append(next_coord)
            current = next_coord
            
            # Check if reached goal
            if current.distance_to(goal) < tolerance:
                path.append(goal)
                break
        
        return path