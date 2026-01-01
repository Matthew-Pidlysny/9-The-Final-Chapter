"""
Tyson Navigator

Core navigation system using Tyson Co-Ordinate operations for
universal navigation across all geometry types.
"""

import numpy as np
import math
from typing import List, Dict, Any, Optional, Tuple, Union, Callable
from dataclasses import dataclass, field
from enum import Enum, auto

from ..core.coordinates import TysonCoordinate, CoordinateOperation
from ..core.geometry_base import InformationSphere
from ..core.structures import NavigationPath, AdjacencyField


class NavigationMode(Enum):
    """Navigation modes for different purposes"""
    DIRECT = auto()           # Direct point-to-point navigation
    OPTIMAL = auto()          # Optimize for distance/efficiency
    ADAPTIVE = auto()         # Adaptive to geometry constraints
    EXPLORATORY = auto()      # Explore the space
    CONSTRAINT_AWARE = auto() # Respect geometric constraints


@dataclass
class NavigationConstraints:
    """Constraints for navigation planning"""
    max_distance: float = 100.0
    time_limit: Optional[float] = None
    forbidden_regions: List[Tuple[np.ndarray, float]] = field(default_factory=list)  # (center, radius)
    required_waypoints: List[TysonCoordinate] = field(default_factory=list)
    optimization_goal: str = "distance"  # "distance", "time", "energy"


class TysonNavigator:
    """
    Universal navigator using Tyson Co-Ordinate operations
    
    Provides navigation capabilities across all geometry types using the
    four fundamental operations: addition, subtraction, multiplication,
    and reciprocal.
    """
    
    def __init__(self, sphere: InformationSphere):
        self.sphere = sphere
        self.navigation_mode = NavigationMode.ADAPTIVE
        self.constraints = NavigationConstraints()
        
        # Navigation history and learning
        self.navigation_history = []
        self.performance_metrics = {}
        
        # Adjacency field for efficient navigation
        self.adjacency_field = self._build_adjacency_field()
        
        # Initialize navigation strategies
        self._init_navigation_strategies()
    
    def _init_navigation_strategies(self):
        """Initialize navigation strategies"""
        self.strategies = {
            'direct': self._direct_navigation,
            'optimal': self._optimal_navigation,
            'adaptive': self._adaptive_navigation,
            'exploratory': self._exploratory_navigation,
            'constraint_aware': self._constraint_aware_navigation
        }
    
    def _build_adjacency_field(self) -> AdjacencyField:
        """Build adjacency field for efficient navigation"""
        if not self.sphere.coordinates:
            return AdjacencyField(
                source_coordinate=TysonCoordinate(np.array([0.0]), self.sphere.geometry_type.name.lower()),
                adjacent_coordinates=[],
                weights=[]
            )
        
        # Build adjacency graph based on distances
        source = self.sphere.coordinates[0]
        adjacent = []
        weights = []
        
        for coord in self.sphere.coordinates[1:]:
            distance = self._calculate_tyson_distance(source, coord)
            if distance < 2.0:  # Adjacency threshold
                adjacent.append(coord)
                # Weight based on inverse distance (closer = stronger connection)
                weight = 1.0 / (distance + 1e-8)
                weights.append(weight)
        
        return AdjacencyField(
            source_coordinate=source,
            adjacent_coordinates=adjacent,
            weights=weights,
            field_type="tyson_reciprocal"
        )
    
    def navigate_to(self, target: TysonCoordinate, 
                   mode: Optional[NavigationMode] = None,
                   constraints: Optional[NavigationConstraints] = None) -> NavigationPath:
        """
        Navigate from current position to target coordinate
        
        Uses Tyson operations to plan and execute navigation path.
        """
        if mode is None:
            mode = self.navigation_mode
        if constraints is None:
            constraints = self.constraints
        
        # Get current position (start from first coordinate or center)
        current_pos = self._get_current_position()
        
        # Plan navigation path
        path = self._plan_navigation_path(current_pos, target, mode, constraints)
        
        # Record navigation
        self._record_navigation(current_pos, target, path)
        
        return path
    
    def _get_current_position(self) -> TysonCoordinate:
        """Get current navigation position"""
        if not self.sphere.coordinates:
            # Default to origin
            return TysonCoordinate(
                np.array([0.0] * self.sphere.properties.dimensionality),
                self.sphere.geometry_type.name.lower()
            )
        
        # Return first coordinate as current position
        return self.sphere.coordinates[0]
    
    def _plan_navigation_path(self, start: TysonCoordinate, target: TysonCoordinate,
                             mode: NavigationMode, 
                             constraints: NavigationConstraints) -> NavigationPath:
        """Plan navigation path using specified mode"""
        strategy_name = mode.name.lower()
        
        if strategy_name in self.strategies:
            path_coords = self.strategies[strategy_name](start, target, constraints)
        else:
            # Default to adaptive
            path_coords = self.strategies['adaptive'](start, target, constraints)
        
        return NavigationPath(
            coordinates=path_coords,
            path_type=strategy_name,
            metadata={
                'mode': mode.name,
                'start_id': start.metadata.get('id', ''),
                'target_id': target.metadata.get('id', ''),
                'constraints': constraints.__dict__
            }
        )
    
    def _direct_navigation(self, start: TysonCoordinate, target: TysonCoordinate,
                          constraints: NavigationConstraints) -> List[TysonCoordinate]:
        """Direct navigation using Tyson operations"""
        # Calculate direction using subtraction
        direction = start.subtraction(target)
        
        # Calculate number of steps based on distance
        distance = start.distance_to(target)
        steps = max(2, min(20, int(distance * 10)))
        
        path = [start]
        current = start
        
        for i in range(1, steps):
            # Move towards target using addition and multiplication
            step_size = i / steps
            
            # Interpolate using Tyson operations
            # intermediate = start.addition(direction.multiplication(-step_size))
            intermediate = start.interpolate(target, step_size)
            
            path.append(intermediate)
            current = intermediate
        
        path.append(target)
        return path
    
    def _optimal_navigation(self, start: TysonCoordinate, target: TysonCoordinate,
                           constraints: NavigationConstraints) -> List[TysonCoordinate]:
        """Optimal navigation minimizing distance"""
        # Use A* algorithm with Tyson distance metric
        return self._a_star_navigation(start, target, constraints)
    
    def _a_star_navigation(self, start: TysonCoordinate, target: TysonCoordinate,
                          constraints: NavigationConstraints) -> List[TysonCoordinate]:
        """A* pathfinding using Tyson operations"""
        # Simplified A* implementation
        open_set = [(0, start)]
        came_from = {}
        g_score = {self._coord_key(start): 0}
        f_score = {self._coord_key(start): self._heuristic_distance(start, target)}
        
        while open_set:
            # Get node with lowest f_score
            current_f, current = min(open_set, key=lambda x: x[0])
            open_set.remove((current_f, current))
            
            # Check if reached target
            if current.distance_to(target) < 0.1:
                # Reconstruct path
                path = []
                while self._coord_key(current) in came_from:
                    path.append(current)
                    current = came_from[self._coord_key(current)]
                path.append(start)
                path.reverse()
                path.append(target)
                return path
            
            # Explore neighbors
            neighbors = self._get_tyson_neighbors(current)
            
            for neighbor in neighbors:
                tentative_g = g_score[self._coord_key(current)] + current.distance_to(neighbor)
                
                if self._coord_key(neighbor) not in g_score or tentative_g < g_score[self._coord_key(neighbor)]:
                    came_from[self._coord_key(neighbor)] = current
                    g_score[self._coord_key(neighbor)] = tentative_g
                    f_score[self._coord_key(neighbor)] = tentative_g + self._heuristic_distance(neighbor, target)
                    
                    if neighbor not in [item[1] for item in open_set]:
                        open_set.append((f_score[self._coord_key(neighbor)], neighbor))
        
        # Fallback to direct navigation if no path found
        return self._direct_navigation(start, target, constraints)
    
    def _adaptive_navigation(self, start: TysonCoordinate, target: TysonCoordinate,
                            constraints: NavigationConstraints) -> List[TysonCoordinate]:
        """Adaptive navigation based on geometry type"""
        geometry_type = self.sphere.geometry_type.name.lower()
        
        if geometry_type == "banachian":
            # Use metric space properties
            return self._banachian_adaptive_navigation(start, target, constraints)
        elif geometry_type == "quantum":
            # Use quantum superposition
            return self._quantum_adaptive_navigation(start, target, constraints)
        elif geometry_type == "fuzzy":
            # Use fuzzy membership
            return self._fuzzy_adaptive_navigation(start, target, constraints)
        elif geometry_type == "hadwiger_nelson":
            # Use angular constraints
            return self._hadwiger_nelson_adaptive_navigation(start, target, constraints)
        else:
            # Default adaptive
            return self._direct_navigation(start, target, constraints)
    
    def _banachian_adaptive_navigation(self, start: TysonCoordinate, target: TysonCoordinate,
                                      constraints: NavigationConstraints) -> List[TysonCoordinate]:
        """Adaptive navigation for Banachian geometry"""
        # Use contraction mapping principle
        path = [start]
        current = start
        
        for i in range(10):
            # Apply contraction towards target
            direction = current.subtraction(target)
            contraction_factor = 0.5 ** (i + 1)
            
            step = direction.multiplication(-contraction_factor)
            current = current.addition(step)
            path.append(current)
            
            if current.distance_to(target) < 0.1:
                break
        
        path.append(target)
        return path
    
    def _quantum_adaptive_navigation(self, start: TysonCoordinate, target: TysonCoordinate,
                                    constraints: NavigationConstraints) -> List[TysonCoordinate]:
        """Adaptive navigation for quantum geometry"""
        # Use quantum superposition of paths
        path = []
        
        # Generate multiple quantum paths
        n_paths = 3
        all_paths = []
        
        for path_idx in range(n_paths):
            quantum_path = self._quantum_path_generation(start, target, path_idx)
            all_paths.append(quantum_path)
        
        # Superpose paths
        max_length = max(len(p) for p in all_paths)
        
        for i in range(max_length):
            superposed_position = np.zeros(start.position.shape)
            weight = 1.0 / n_paths
            
            for path_idx, quantum_path in enumerate(all_paths):
                if i < len(quantum_path):
                    superposed_position += weight * quantum_path[i].position
            
            superposed_coord = TysonCoordinate(
                position=superposed_position,
                geometry_type=start.geometry_type,
                metadata={'superposed': True, 'path_index': i}
            )
            path.append(superposed_coord)
        
        return path
    
    def _quantum_path_generation(self, start: TysonCoordinate, target: TysonCoordinate,
                                path_index: int) -> List[TysonCoordinate]:
        """Generate individual quantum path"""
        path = [start]
        
        # Quantum random walk towards target
        current = start
        
        for i in range(8):
            # Quantum step
            direction = current.subtraction(target)
            
            # Add quantum uncertainty
            quantum_noise = np.random.normal(0, 0.1, current.position.shape)
            
            step = direction.multiplication(-0.2)
            step.position += quantum_noise
            
            current = current.addition(step)
            path.append(current)
        
        path.append(target)
        return path
    
    def _fuzzy_adaptive_navigation(self, start: TysonCoordinate, target: TysonCoordinate,
                                  constraints: NavigationConstraints) -> List[TysonCoordinate]:
        """Adaptive navigation for fuzzy geometry"""
        # Use fuzzy membership to guide navigation
        path = [start]
        current = start
        
        for i in range(10):
            # Calculate fuzzy direction
            direction = current.subtraction(target)
            
            # Apply fuzzy membership-based weighting
            membership = current.metadata.get('membership_value', 0.5)
            fuzzy_weight = 0.5 + 0.5 * membership
            
            step = direction.multiplication(-fuzzy_weight * 0.2)
            current = current.addition(step)
            path.append(current)
            
            if current.distance_to(target) < 0.1:
                break
        
        path.append(target)
        return path
    
    def _hadwiger_nelson_adaptive_navigation(self, start: TysonCoordinate, target: TysonCoordinate,
                                           constraints: NavigationConstraints) -> List[TysonCoordinate]:
        """Adaptive navigation for Hadwiger-Nelson geometry"""
        # Navigate avoiding forbidden angles
        path = [start]
        current = start
        
        for i in range(12):
            # Calculate direction
            direction = current.subtraction(target)
            
            # Step towards target
            step_size = 0.1
            step = direction.multiplication(-step_size)
            next_pos = current.addition(step)
            
            # Check for forbidden angles and adjust if needed
            if self._has_forbidden_angle(next_pos):
                # Adjust angle to avoid forbidden configuration
                adjusted_pos = self._adjust_forbidden_angle(next_pos)
                next_pos = adjusted_pos
            
            current = next_pos
            path.append(current)
            
            if current.distance_to(target) < 0.1:
                break
        
        path.append(target)
        return path
    
    def _exploratory_navigation(self, start: TysonCoordinate, target: TysonCoordinate,
                               constraints: NavigationConstraints) -> List[TysonCoordinate]:
        """Exploratory navigation that discovers new paths"""
        path = [start]
        current = start
        
        # Explore space while generally moving towards target
        exploration_radius = 2.0
        steps = 15
        
        for i in range(steps):
            # Calculate direction to target
            target_direction = current.subtraction(target)
            
            # Add exploration component
            exploration_angle = np.random.uniform(0, 2 * math.pi)
            exploration_magnitude = exploration_radius * (1.0 - i / steps)
            
            if current.position.size >= 2:
                exploration_component = np.array([
                    exploration_magnitude * math.cos(exploration_angle),
                    exploration_magnitude * math.sin(exploration_angle)
                ])
                
                if current.position.size > 2:
                    exploration_component = np.concatenate([
                        exploration_component,
                        np.zeros(current.position.size - 2)
                    ])
                
                # Combine target direction with exploration
                target_weight = 0.7 * (i / steps)  # Increase target focus over time
                exploration_weight = 1.0 - target_weight
                
                step = target_direction.multiplication(-target_weight * 0.1)
                step.position = step.position + exploration_weight * exploration_component
                
                current = current.addition(step)
                path.append(current)
        
        # Final approach to target
        final_approach = self._direct_navigation(current, target, constraints)
        path.extend(final_approach[1:])
        
        return path
    
    def _constraint_aware_navigation(self, start: TysonCoordinate, target: TysonCoordinate,
                                    constraints: NavigationConstraints) -> List[TysonCoordinate]:
        """Navigation that respects geometric constraints"""
        # Check for forbidden regions
        if constraints.forbidden_regions:
            return self._avoid_forbidden_regions(start, target, constraints)
        
        # Check required waypoints
        if constraints.required_waypoints:
            return self._navigate_with_waypoints(start, target, constraints)
        
        # Default to optimal navigation
        return self._optimal_navigation(start, target, constraints)
    
    def _avoid_forbidden_regions(self, start: TysonCoordinate, target: TysonCoordinate,
                                constraints: NavigationConstraints) -> List[TysonCoordinate]:
        """Navigate avoiding forbidden regions"""
        # Simple implementation: add waypoints around forbidden regions
        path = [start]
        current = start
        
        # Check direct path
        if self._path_is_clear(current, target, constraints):
            return self._direct_navigation(start, target, constraints)
        
        # Find waypoints around obstacles
        waypoints = self._find_waypoints_around_obstacles(current, target, constraints)
        
        # Navigate to each waypoint
        for waypoint in waypoints:
            segment = self._direct_navigation(current, waypoint, constraints)
            path.extend(segment[1:])
            current = waypoint
        
        # Final segment to target
        final_segment = self._direct_navigation(current, target, constraints)
        path.extend(final_segment[1:])
        
        return path
    
    def _navigate_with_waypoints(self, start: TysonCoordinate, target: TysonCoordinate,
                                constraints: NavigationConstraints) -> List[TysonCoordinate]:
        """Navigate through required waypoints"""
        path = [start]
        current = start
        
        # Add waypoints in order
        for waypoint in constraints.required_waypoints:
            segment = self._direct_navigation(current, waypoint, constraints)
            path.extend(segment[1:])
            current = waypoint
        
        # Final segment to target
        final_segment = self._direct_navigation(current, target, constraints)
        path.extend(final_segment[1:])
        
        return path
    
    def _get_tyson_neighbors(self, coordinate: TysonCoordinate) -> List[TysonCoordinate]:
        """Get neighboring coordinates using Tyson operations"""
        neighbors = []
        
        # Generate neighbors using Tyson operations
        operations = [
            lambda c: c.addition(TysonCoordinate(np.array([0.1, 0.0]), c.geometry_type)),
            lambda c: c.addition(TysonCoordinate(np.array([-0.1, 0.0]), c.geometry_type)),
            lambda c: c.addition(TysonCoordinate(np.array([0.0, 0.1]), c.geometry_type)),
            lambda c: c.addition(TysonCoordinate(np.array([0.0, -0.1]), c.geometry_type))
        ]
        
        for operation in operations:
            try:
                neighbor = operation(coordinate)
                neighbors.append(neighbor)
            except:
                continue
        
        return neighbors
    
    def _heuristic_distance(self, coord1: TysonCoordinate, coord2: TysonCoordinate) -> float:
        """Heuristic distance for pathfinding"""
        return coord1.distance_to(coord2)
    
    def _coord_key(self, coordinate: TysonCoordinate) -> str:
        """Get hashable key for coordinate"""
        return str(coordinate.position.tobytes())
    
    def _calculate_tyson_distance(self, coord1: TysonCoordinate, coord2: TysonCoordinate) -> float:
        """Calculate distance using Tyson-specific metric"""
        return coord1.distance_to(coord2)
    
    def _path_is_clear(self, start: TysonCoordinate, target: TysonCoordinate,
                      constraints: NavigationConstraints) -> bool:
        """Check if path avoids forbidden regions"""
        if not constraints.forbidden_regions:
            return True
        
        # Sample points along path
        n_samples = 10
        for i in range(n_samples + 1):
            t = i / n_samples
            sample_pos = start.interpolate(target, t)
            
            # Check if sample is in forbidden region
            for center, radius in constraints.forbidden_regions:
                if np.linalg.norm(sample_pos.position - center) < radius:
                    return False
        
        return True
    
    def _find_waypoints_around_obstacles(self, start: TysonCoordinate, target: TysonCoordinate,
                                        constraints: NavigationConstraints) -> List[TysonCoordinate]:
        """Find waypoints around forbidden regions"""
        waypoints = []
        
        # Simple implementation: add waypoints at circumnavigation points
        for center, radius in constraints.forbidden_regions:
            # Calculate circumnavigation points
            direction = target.position - start.position
            if np.linalg.norm(direction) > 0:
                direction = direction / np.linalg.norm(direction)
                
                # Perpendicular directions
                if direction.size >= 2:
                    perp1 = np.array([-direction[1], direction[0]])
                    perp2 = np.array([direction[1], -direction[0]])
                    
                    # Waypoints at safe distance
                    safe_distance = radius * 1.5
                    waypoint1_pos = center + perp1 * safe_distance
                    waypoint2_pos = center + perp2 * safe_distance
                    
                    waypoint1 = TysonCoordinate(waypoint1_pos, start.geometry_type)
                    waypoint2 = TysonCoordinate(waypoint2_pos, start.geometry_type)
                    
                    waypoints.append(waypoint1)
                    waypoints.append(waypoint2)
        
        return waypoints
    
    def _has_forbidden_angle(self, coordinate: TysonCoordinate) -> bool:
        """Check if coordinate has forbidden angle (Hadwiger-Nelson)"""
        if coordinate.position.size < 2:
            return False
        
        angle = math.atan2(coordinate.position[1], coordinate.position[0])
        forbidden_angles = [math.pi/4, 3*math.pi/4, 5*math.pi/4, 7*math.pi/4]
        tolerance = 0.1
        
        for forbidden in forbidden_angles:
            if abs(angle - forbidden) < tolerance:
                return True
        
        return False
    
    def _adjust_forbidden_angle(self, coordinate: TysonCoordinate) -> TysonCoordinate:
        """Adjust coordinate to avoid forbidden angles"""
        if coordinate.position.size < 2:
            return coordinate
        
        pos = coordinate.position.copy()
        angle = math.atan2(pos[1], pos[0])
        forbidden_angles = [math.pi/4, 3*math.pi/4, 5*math.pi/4, 7*math.pi/4]
        tolerance = 0.1
        
        for forbidden in forbidden_angles:
            if abs(angle - forbidden) < tolerance:
                # Adjust angle
                if angle < forbidden:
                    angle -= tolerance
                else:
                    angle += tolerance
                
                # Reconstruct position
                r = math.sqrt(pos[0]**2 + pos[1]**2)
                pos[0] = r * math.cos(angle)
                pos[1] = r * math.sin(angle)
                break
        
        return TysonCoordinate(pos, coordinate.geometry_type, coordinate.metadata)
    
    def _record_navigation(self, start: TysonCoordinate, target: TysonCoordinate, path: NavigationPath):
        """Record navigation for learning and optimization"""
        navigation_record = {
            'timestamp': self._get_timestamp(),
            'start': start.to_dict(),
            'target': target.to_dict(),
            'path': path.to_dict(),
            'mode': self.navigation_mode.name,
            'distance': path.total_distance,
            'steps': len(path.coordinates)
        }
        
        self.navigation_history.append(navigation_record)
        
        # Keep history manageable
        if len(self.navigation_history) > 1000:
            self.navigation_history = self.navigation_history[-500:]
    
    def _get_timestamp(self) -> float:
        """Get current timestamp"""
        import time
        return time.time()
    
    def optimize_navigation(self, goal: str = "efficiency") -> Dict[str, Any]:
        """Optimize navigation parameters based on history"""
        if not self.navigation_history:
            return {"message": "No navigation history available for optimization"}
        
        # Analyze navigation patterns
        distances = [nav['distance'] for nav in self.navigation_history]
        steps = [nav['steps'] for nav in self.navigation_history]
        
        optimization_results = {
            'total_navigations': len(self.navigation_history),
            'average_distance': np.mean(distances),
            'average_steps': np.mean(steps),
            'efficiency_score': np.mean(distances) / np.mean(steps) if np.mean(steps) > 0 else 0,
            'optimizations': []
        }
        
        # Suggest optimizations based on patterns
        if optimization_results['efficiency_score'] > 0.5:
            optimization_results['optimizations'].append("Consider using direct navigation for better efficiency")
        
        if np.std(distances) > np.mean(distances):
            optimization_results['optimizations'].append("High variance in distances - consider adaptive mode")
        
        return optimization_results
    
    def set_navigation_mode(self, mode: NavigationMode):
        """Set navigation mode"""
        self.navigation_mode = mode
    
    def set_constraints(self, constraints: NavigationConstraints):
        """Set navigation constraints"""
        self.constraints = constraints
    
    def get_navigation_statistics(self) -> Dict[str, Any]:
        """Get navigation performance statistics"""
        if not self.navigation_history:
            return {"message": "No navigation history available"}
        
        return {
            'total_navigations': len(self.navigation_history),
            'modes_used': list(set(nav['mode'] for nav in self.navigation_history)),
            'average_distance': np.mean([nav['distance'] for nav in self.navigation_history]),
            'average_steps': np.mean([nav['steps'] for nav in self.navigation_history]),
            'most_used_mode': max(set(nav['mode'] for nav in self.navigation_history), 
                                 key=lambda x: [nav['mode'] for nav in self.navigation_history].count(x))
        }