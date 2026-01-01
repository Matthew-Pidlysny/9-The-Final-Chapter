"""
Path Planner

Advanced path planning algorithms for navigation in information spheres
using various strategies and optimization techniques.
"""

import numpy as np
import heapq
from typing import List, Dict, Any, Optional, Tuple, Set, Callable
from dataclasses import dataclass, field
from enum import Enum, auto

from ..core.coordinates import TysonCoordinate, NavigationStrategy
from ..core.structures import NavigationPath, AdjacencyField


class PlanningAlgorithm(Enum):
    """Path planning algorithms"""
    ASTAR = auto()           # A* search algorithm
    DIJKSTRA = auto()        # Dijkstra's algorithm
    GREEDY_BEST = auto()     # Greedy best-first search
    RRT = auto()             # Rapidly-exploring Random Trees
    GENETIC = auto()         # Genetic algorithm
    HYBRID = auto()          # Hybrid approach


@dataclass
class PathPlanningConstraints:
    """Constraints for path planning"""
    max_path_length: float = 100.0
    max_waypoints: int = 50
    forbidden_regions: List[Tuple[np.ndarray, float]] = field(default_factory=list)
    required_waypoints: List[TysonCoordinate] = field(default_factory=list)
    optimization_weight: float = 0.5  # 0.0 = fastest, 1.0 = shortest


class PathPlanner:
    """
    Advanced path planner for navigation in information spheres
    
    Features:
    - Multiple planning algorithms
    - Constraint-aware planning
    - Optimization for different goals
    - Real-time replanning capabilities
    """
    
    def __init__(self, sphere: 'InformationSphere'):
        self.sphere = sphere
        self.constraints = PathPlanningConstraints()
        
        # Planning algorithms
        self.algorithms = {
            PlanningAlgorithm.ASTAR: self._astar_plan,
            PlanningAlgorithm.DIJKSTRA: self._dijkstra_plan,
            PlanningAlgorithm.GREEDY_BEST: self._greedy_best_plan,
            PlanningAlgorithm.RRT: self._rrt_plan,
            PlanningAlgorithm.GENETIC: self._genetic_plan,
            PlanningAlgorithm.HYBRID: self._hybrid_plan
        }
        
        # Heuristic functions
        self.heuristics = {
            'euclidean': self._euclidean_heuristic,
            'manhattan': self._manhattan_heuristic,
            'tyson_distance': self._tyson_distance_heuristic,
            'adaptive': self._adaptive_heuristic
        }
        
        # Planning statistics
        self.planning_history = []
        self.performance_metrics = {}
    
    def plan_path(self, start: TysonCoordinate, goal: TysonCoordinate,
                  algorithm: PlanningAlgorithm = PlanningAlgorithm.ASTAR,
                  heuristic: str = 'euclidean',
                  constraints: Optional[PathPlanningConstraints] = None) -> NavigationPath:
        """
        Plan optimal path from start to goal coordinate
        
        Uses the specified algorithm with constraints and heuristics.
        """
        if constraints:
            self.constraints = constraints
        
        # Validate inputs
        if not self._validate_inputs(start, goal):
            raise ValueError("Invalid start or goal coordinates")
        
        # Plan path using selected algorithm
        plan_function = self.algorithms.get(algorithm, self._astar_plan)
        path = plan_function(start, goal, heuristic)
        
        # Post-process path
        path = self._post_process_path(path)
        
        # Record planning statistics
        self._record_planning_stats(algorithm, len(path.coordinates), path.total_distance)
        
        return path
    
    def _validate_inputs(self, start: TysonCoordinate, goal: TysonCoordinate) -> bool:
        """Validate start and goal coordinates"""
        return (start is not None and goal is not None and
                isinstance(start, TysonCoordinate) and isinstance(goal, TysonCoordinate))
    
    def _astar_plan(self, start: TysonCoordinate, goal: TysonCoordinate, heuristic: str) -> NavigationPath:
        """A* search algorithm for path planning"""
        open_set = []
        heapq.heappush(open_set, (0, 0, start))
        
        came_from = {}
        g_score = {str(start.position): 0}
        f_score = {str(start.position): self._heuristic_cost(start, goal, heuristic)}
        
        visited = set()
        
        while open_set:
            current_f, _, current = heapq.heappop(open_set)
            
            if str(current.position) in visited:
                continue
            
            visited.add(str(current.position))
            
            # Check if goal reached
            if self._is_goal_reached(current, goal):
                return self._reconstruct_path(came_from, current)
            
            # Explore neighbors
            neighbors = self._get_neighbors(current)
            
            for neighbor in neighbors:
                if str(neighbor.position) in visited:
                    continue
                
                # Calculate tentative g_score
                tentative_g = g_score[str(current.position)] + self._calculate_step_cost(current, neighbor)
                
                if str(neighbor.position) not in g_score or tentative_g < g_score[str(neighbor.position)]:
                    came_from[str(neighbor.position)] = current
                    g_score[str(neighbor.position)] = tentative_g
                    f_score[str(neighbor.position)] = tentative_g + self._heuristic_cost(neighbor, goal, heuristic)
                    
                    heapq.heappush(open_set, (f_score[str(neighbor.position)], len(open_set), neighbor))
        
        # No path found
        return NavigationPath(coordinates=[start, goal], total_distance=self._calculate_distance(start, goal))
    
    def _dijkstra_plan(self, start: TysonCoordinate, goal: TysonCoordinate, heuristic: str) -> NavigationPath:
        """Dijkstra's algorithm for shortest path"""
        distances = {str(start.position): 0}
        previous = {}
        unvisited = [(0, start)]
        
        visited = set()
        
        while unvisited:
            current_dist, current = heapq.heappop(unvisited)
            
            if str(current.position) in visited:
                continue
            
            visited.add(str(current.position))
            
            # Check if goal reached
            if self._is_goal_reached(current, goal):
                return self._reconstruct_path(previous, current)
            
            # Explore neighbors
            neighbors = self._get_neighbors(current)
            
            for neighbor in neighbors:
                if str(neighbor.position) in visited:
                    continue
                
                distance = current_dist + self._calculate_step_cost(current, neighbor)
                
                if str(neighbor.position) not in distances or distance < distances[str(neighbor.position)]:
                    distances[str(neighbor.position)] = distance
                    previous[str(neighbor.position)] = current
                    heapq.heappush(unvisited, (distance, neighbor))
        
        # No path found
        return NavigationPath(coordinates=[start, goal], total_distance=self._calculate_distance(start, goal))
    
    def _greedy_best_plan(self, start: TysonCoordinate, goal: TysonCoordinate, heuristic: str) -> NavigationPath:
        """Greedy best-first search algorithm"""
        open_set = [(self._heuristic_cost(start, goal, heuristic), start)]
        came_from = {}
        visited = set()
        
        while open_set:
            _, current = heapq.heappop(open_set)
            
            if str(current.position) in visited:
                continue
            
            visited.add(str(current.position))
            
            # Check if goal reached
            if self._is_goal_reached(current, goal):
                return self._reconstruct_path(came_from, current)
            
            # Explore neighbors
            neighbors = self._get_neighbors(current)
            
            for neighbor in neighbors:
                if str(neighbor.position) not in visited:
                    came_from[str(neighbor.position)] = current
                    priority = self._heuristic_cost(neighbor, goal, heuristic)
                    heapq.heappush(open_set, (priority, neighbor))
        
        # No path found
        return NavigationPath(coordinates=[start, goal], total_distance=self._calculate_distance(start, goal))
    
    def _rrt_plan(self, start: TysonCoordinate, goal: TysonCoordinate, heuristic: str) -> NavigationPath:
        """Rapidly-exploring Random Trees algorithm"""
        max_iterations = 1000
        step_size = 1.0
        goal_tolerance = 0.1
        
        # Initialize tree with start node
        tree_nodes = [start]
        tree_edges = {start: None}
        
        for iteration in range(max_iterations):
            # Sample random point
            if np.random.random() < 0.1:  # 10% chance to sample goal
                random_point = goal
            else:
                random_point = self._sample_random_point()
            
            # Find nearest node in tree
            nearest_node = min(tree_nodes, key=lambda node: self._calculate_distance(node, random_point))
            
            # Steer towards random point
            new_node = self._steer(nearest_node, random_point, step_size)
            
            # Check if new node is valid
            if self._is_valid_node(new_node):
                tree_nodes.append(new_node)
                tree_edges[new_node] = nearest_node
                
                # Check if goal reached
                if self._calculate_distance(new_node, goal) < goal_tolerance:
                    # Reconstruct path
                    path_coords = []
                    current = new_node
                    while current is not None:
                        path_coords.append(current)
                        current = tree_edges[current]
                    
                    path_coords.reverse()
                    total_distance = sum(self._calculate_distance(path_coords[i], path_coords[i+1]) 
                                       for i in range(len(path_coords)-1))
                    
                    return NavigationPath(coordinates=path_coords, total_distance=total_distance)
        
        # No path found within iterations
        return NavigationPath(coordinates=[start, goal], total_distance=self._calculate_distance(start, goal))
    
    def _genetic_plan(self, start: TysonCoordinate, goal: TysonCoordinate, heuristic: str) -> NavigationPath:
        """Genetic algorithm for path planning"""
        population_size = 50
        max_generations = 100
        mutation_rate = 0.1
        crossover_rate = 0.7
        
        # Initialize population
        population = self._initialize_population(start, goal, population_size)
        
        for generation in range(max_generations):
            # Evaluate fitness
            fitness_scores = [self._evaluate_fitness(path, goal) for path in population]
            
            # Check for convergence
            best_fitness = max(fitness_scores)
            if best_fitness > 0.95:
                best_path = population[fitness_scores.index(best_fitness)]
                return best_path
            
            # Selection
            selected = self._tournament_selection(population, fitness_scores)
            
            # Crossover and mutation
            new_population = []
            for i in range(0, len(selected), 2):
                if i+1 < len(selected):
                    parent1, parent2 = selected[i], selected[i+1]
                    
                    if np.random.random() < crossover_rate:
                        child1, child2 = self._crossover(parent1, parent2)
                    else:
                        child1, child2 = parent1, parent2
                    
                    if np.random.random() < mutation_rate:
                        child1 = self._mutate(child1, start, goal)
                        child2 = self._mutate(child2, start, goal)
                    
                    new_population.extend([child1, child2])
                else:
                    new_population.append(selected[i])
            
            population = new_population
        
        # Return best path found
        fitness_scores = [self._evaluate_fitness(path, goal) for path in population]
        best_path = population[fitness_scores.index(max(fitness_scores))]
        return best_path
    
    def _hybrid_plan(self, start: TysonCoordinate, goal: TysonCoordinate, heuristic: str) -> NavigationPath:
        """Hybrid approach combining multiple algorithms"""
        # Try A* first
        astar_path = self._astar_plan(start, goal, heuristic)
        
        # If path is too long, try RRT for faster result
        if len(astar_path.coordinates) > self.constraints.max_waypoints:
            rrt_path = self._rrt_plan(start, goal, heuristic)
            
            # Choose shorter path
            if rrt_path.total_distance < astar_path.total_distance:
                return rrt_path
        
        return astar_path
    
    def _get_neighbors(self, coordinate: TysonCoordinate) -> List[TysonCoordinate]:
        """Get neighboring coordinates"""
        neighbors = []
        
        # Find coordinates in adjacency field
        for coord in self.sphere.coordinates:
            if coord != coordinate:
                distance = self._calculate_distance(coordinate, coord)
                if distance < 2.0:  # Neighbor threshold
                    neighbors.append(coord)
        
        return neighbors
    
    def _heuristic_cost(self, current: TysonCoordinate, goal: TysonCoordinate, heuristic: str) -> float:
        """Calculate heuristic cost for path planning"""
        heuristic_func = self.heuristics.get(heuristic, self._euclidean_heuristic)
        return heuristic_func(current, goal)
    
    def _euclidean_heuristic(self, current: TysonCoordinate, goal: TysonCoordinate) -> float:
        """Euclidean distance heuristic"""
        return np.linalg.norm(current.position - goal.position)
    
    def _manhattan_heuristic(self, current: TysonCoordinate, goal: TysonCoordinate) -> float:
        """Manhattan distance heuristic"""
        return np.sum(np.abs(current.position - goal.position))
    
    def _tyson_distance_heuristic(self, current: TysonCoordinate, goal: TysonCoordinate) -> float:
        """Tyson Co-Ordinate distance heuristic"""
        if hasattr(current, 'distance_to'):
            return current.distance_to(goal)
        return self._euclidean_heuristic(current, goal)
    
    def _adaptive_heuristic(self, current: TysonCoordinate, goal: TysonCoordinate) -> float:
        """Adaptive heuristic based on geometry type"""
        if current.geometry_type == "quantum":
            return self._tyson_distance_heuristic(current, goal)
        elif current.geometry_type == "fuzzy":
            return 0.5 * self._euclidean_heuristic(current, goal) + 0.5 * self._manhattan_heuristic(current, goal)
        else:
            return self._euclidean_heuristic(current, goal)
    
    def _calculate_step_cost(self, from_coord: TysonCoordinate, to_coord: TysonCoordinate) -> float:
        """Calculate cost of moving from one coordinate to another"""
        base_cost = self._calculate_distance(from_coord, to_coord)
        
        # Add penalty for crossing forbidden regions
        for center, radius in self.constraints.forbidden_regions:
            midpoint = (from_coord.position + to_coord.position) / 2
            if np.linalg.norm(midpoint - center) < radius:
                base_cost *= 10.0  # Large penalty
        
        return base_cost
    
    def _calculate_distance(self, coord1: TysonCoordinate, coord2: TysonCoordinate) -> float:
        """Calculate distance between two coordinates"""
        if hasattr(coord1, 'distance_to'):
            return coord1.distance_to(coord2)
        return np.linalg.norm(coord1.position - coord2.position)
    
    def _is_goal_reached(self, current: TysonCoordinate, goal: TysonCoordinate) -> bool:
        """Check if goal coordinate is reached"""
        return self._calculate_distance(current, goal) < 0.1
    
    def _reconstruct_path(self, came_from: Dict[str, TysonCoordinate], current: TysonCoordinate) -> NavigationPath:
        """Reconstruct path from search results"""
        path_coords = [current]
        
        while str(current.position) in came_from:
            current = came_from[str(current.position)]
            path_coords.append(current)
        
        path_coords.reverse()
        
        # Calculate total distance
        total_distance = sum(self._calculate_distance(path_coords[i], path_coords[i+1]) 
                           for i in range(len(path_coords)-1))
        
        return NavigationPath(coordinates=path_coords, total_distance=total_distance)
    
    def _sample_random_point(self) -> TysonCoordinate:
        """Sample a random point in the space"""
        if self.sphere.coordinates:
            positions = np.array([coord.position for coord in self.sphere.coordinates])
            min_bounds = positions.min(axis=0)
            max_bounds = positions.max(axis=0)
            
            random_position = np.random.uniform(min_bounds, max_bounds)
            return TysonCoordinate(random_position, self.sphere.geometry_type.name.lower())
        
        return TysonCoordinate(np.array([0.0]), self.sphere.geometry_type.name.lower())
    
    def _steer(self, from_coord: TysonCoordinate, to_coord: TysonCoordinate, step_size: float) -> TysonCoordinate:
        """Steer from one coordinate towards another"""
        direction = to_coord.position - from_coord.position
        distance = np.linalg.norm(direction)
        
        if distance <= step_size:
            return to_coord
        
        unit_direction = direction / distance
        new_position = from_coord.position + unit_direction * step_size
        
        return TysonCoordinate(new_position, from_coord.geometry_type)
    
    def _is_valid_node(self, node: TysonCoordinate) -> bool:
        """Check if a node is valid (not in forbidden regions)"""
        for center, radius in self.constraints.forbidden_regions:
            if np.linalg.norm(node.position - center) < radius:
                return False
        return True
    
    def _initialize_population(self, start: TysonCoordinate, goal: TysonCoordinate, size: int) -> List[NavigationPath]:
        """Initialize population for genetic algorithm"""
        population = []
        
        for _ in range(size):
            # Generate random path
            path_length = np.random.randint(3, 10)
            coordinates = [start]
            
            current = start
            for _ in range(path_length - 2):
                # Random intermediate point
                intermediate = self._sample_random_point()
                coordinates.append(intermediate)
                current = intermediate
            
            coordinates.append(goal)
            
            # Calculate total distance
            total_distance = sum(self._calculate_distance(coordinates[i], coordinates[i+1]) 
                               for i in range(len(coordinates)-1))
            
            population.append(NavigationPath(coordinates=coordinates, total_distance=total_distance))
        
        return population
    
    def _evaluate_fitness(self, path: NavigationPath, goal: TysonCoordinate) -> float:
        """Evaluate fitness of a path"""
        # Fitness based on path length and reaching goal
        last_coord = path.coordinates[-1]
        distance_to_goal = self._calculate_distance(last_coord, goal)
        
        # Normalize fitness (0 to 1, higher is better)
        fitness = 1.0 / (1.0 + distance_to_goal + path.total_distance)
        
        return fitness
    
    def _tournament_selection(self, population: List[NavigationPath], fitness_scores: List[float], tournament_size: int = 3) -> List[NavigationPath]:
        """Tournament selection for genetic algorithm"""
        selected = []
        
        for _ in range(len(population)):
            # Select random individuals for tournament
            tournament_indices = np.random.choice(len(population), tournament_size, replace=False)
            tournament_fitness = [fitness_scores[i] for i in tournament_indices]
            
            # Select winner
            winner_index = tournament_indices[np.argmax(tournament_fitness)]
            selected.append(population[winner_index])
        
        return selected
    
    def _crossover(self, parent1: NavigationPath, parent2: NavigationPath) -> Tuple[NavigationPath, NavigationPath]:
        """Crossover operation for genetic algorithm"""
        # Find common midpoint
        mid1 = len(parent1.coordinates) // 2
        mid2 = len(parent2.coordinates) // 2
        
        # Create children by combining paths
        child1_coords = parent1.coordinates[:mid1] + parent2.coordinates[mid2:]
        child2_coords = parent2.coordinates[:mid2] + parent1.coordinates[mid1:]
        
        # Calculate distances
        def calculate_total_distance(coords):
            return sum(self._calculate_distance(coords[i], coords[i+1]) for i in range(len(coords)-1))
        
        child1 = NavigationPath(coordinates=child1_coords, total_distance=calculate_total_distance(child1_coords))
        child2 = NavigationPath(coordinates=child2_coords, total_distance=calculate_total_distance(child2_coords))
        
        return child1, child2
    
    def _mutate(self, path: NavigationPath, start: TysonCoordinate, goal: TysonCoordinate) -> NavigationPath:
        """Mutation operation for genetic algorithm"""
        if len(path.coordinates) <= 2:
            return path
        
        # Randomly select a mutation point
        mutation_point = np.random.randint(1, len(path.coordinates) - 1)
        
        # Create new path with mutated segment
        new_coords = path.coordinates[:mutation_point]
        
        # Add random intermediate points
        num_new_points = np.random.randint(1, 4)
        for _ in range(num_new_points):
            new_coords.append(self._sample_random_point())
        
        new_coords.append(goal)
        
        # Calculate new distance
        total_distance = sum(self._calculate_distance(new_coords[i], new_coords[i+1]) 
                           for i in range(len(new_coords)-1))
        
        return NavigationPath(coordinates=new_coords, total_distance=total_distance)
    
    def _post_process_path(self, path: NavigationPath) -> NavigationPath:
        """Post-process path to remove unnecessary waypoints"""
        if len(path.coordinates) <= 2:
            return path
        
        # Remove waypoints that are too close
        filtered_coords = [path.coordinates[0]]
        
        for coord in path.coordinates[1:]:
            if self._calculate_distance(filtered_coords[-1], coord) > 0.01:
                filtered_coords.append(coord)
        
        # Recalculate distance
        total_distance = sum(self._calculate_distance(filtered_coords[i], filtered_coords[i+1]) 
                           for i in range(len(filtered_coords)-1))
        
        return NavigationPath(coordinates=filtered_coords, total_distance=total_distance)
    
    def _record_planning_stats(self, algorithm: PlanningAlgorithm, path_length: int, total_distance: float):
        """Record planning statistics"""
        stats = {
            'algorithm': algorithm.name,
            'path_length': path_length,
            'total_distance': total_distance,
            'timestamp': np.datetime64('now').astype(str)
        }
        
        self.planning_history.append(stats)
        
        # Update performance metrics
        if algorithm not in self.performance_metrics:
            self.performance_metrics[algorithm] = {
                'count': 0,
                'avg_path_length': 0.0,
                'avg_distance': 0.0
            }
        
        metrics = self.performance_metrics[algorithm]
        metrics['count'] += 1
        metrics['avg_path_length'] = (metrics['avg_path_length'] * (metrics['count'] - 1) + path_length) / metrics['count']
        metrics['avg_distance'] = (metrics['avg_distance'] * (metrics['count'] - 1) + total_distance) / metrics['count']
    
    def get_performance_metrics(self) -> Dict[str, Any]:
        """Get performance metrics for all algorithms"""
        return self.performance_metrics.copy()
    
    def get_planning_history(self) -> List[Dict[str, Any]]:
        """Get planning history"""
        return self.planning_history.copy()