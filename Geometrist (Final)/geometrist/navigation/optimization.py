"""
Navigation Optimization

Optimization strategies for improving navigation paths and
coordinates within information spheres.
"""

import numpy as np
from typing import List, Dict, Any, Optional, Tuple, Callable
from dataclasses import dataclass, field
from enum import Enum, auto

from ..core.coordinates import TysonCoordinate
from ..core.structures import NavigationPath, OptimizationTarget
from .path_planner import PlanningAlgorithm


class OptimizationStrategy(Enum):
    """Optimization strategies for navigation"""
    GRADIENT_DESCENT = auto()    # Gradient-based optimization
    SIMULATED_ANNEALING = auto() # Simulated annealing
    GENETIC = auto()            # Genetic algorithm
    PARTICLE_SWARM = auto()     # Particle swarm optimization
    BAYESIAN = auto()           # Bayesian optimization
    HYBRID = auto()             # Hybrid approach


@dataclass
class OptimizationParameters:
    """Parameters for optimization algorithms"""
    max_iterations: int = 1000
    convergence_threshold: float = 1e-6
    learning_rate: float = 0.01
    temperature: float = 100.0   # For simulated annealing
    population_size: int = 50    # For genetic/PSO
    mutation_rate: float = 0.1
    crossover_rate: float = 0.7


class NavigationOptimizer:
    """
    Optimizer for navigation paths and coordinates
    
    Features:
    - Multiple optimization strategies
    - Multi-objective optimization
    - Constraint handling
    - Real-time optimization
    """
    
    def __init__(self, sphere: 'InformationSphere'):
        self.sphere = sphere
        self.parameters = OptimizationParameters()
        
        # Optimization strategies
        self.strategies = {
            OptimizationStrategy.GRADIENT_DESCENT: self._gradient_descent_optimize,
            OptimizationStrategy.SIMULATED_ANNEALING: self._simulated_annealing_optimize,
            OptimizationStrategy.GENETIC: self._genetic_optimize,
            OptimizationStrategy.PARTICLE_SWARM: self._particle_swarm_optimize,
            OptimizationStrategy.BAYESIAN: self._bayesian_optimize,
            OptimizationStrategy.HYBRID: self._hybrid_optimize
        }
        
        # Optimization history
        self.optimization_history = []
        self.performance_metrics = {}
    
    def optimize_path(self, path: NavigationPath, 
                     target: OptimizationTarget,
                     strategy: OptimizationStrategy = OptimizationStrategy.GRADIENT_DESCENT,
                     parameters: Optional[OptimizationParameters] = None) -> NavigationPath:
        """
        Optimize navigation path for specified target
        
        Args:
            path: Initial path to optimize
            target: Optimization target (distance, complexity, etc.)
            strategy: Optimization strategy to use
            parameters: Optimization parameters
        
        Returns:
            Optimized path
        """
        if parameters:
            self.parameters = parameters
        
        # Select optimization strategy
        optimize_function = self.strategies.get(strategy, self._gradient_descent_optimize)
        
        # Optimize path
        optimized_path = optimize_function(path, target)
        
        # Record optimization
        self._record_optimization(strategy, target, path, optimized_path)
        
        return optimized_path
    
    def optimize_coordinates(self, coordinates: List[TysonCoordinate],
                           target: OptimizationTarget,
                           strategy: OptimizationStrategy = OptimizationStrategy.GRADIENT_DESCENT) -> List[TysonCoordinate]:
        """
        Optimize coordinate positions for specified target
        
        Args:
            coordinates: List of coordinates to optimize
            target: Optimization target
            strategy: Optimization strategy
        
        Returns:
            Optimized coordinates
        """
        # Create path from coordinates for optimization
        path = NavigationPath(coordinates=coordinates, total_distance=0.0)
        
        # Optimize path
        optimized_path = self.optimize_path(path, target, strategy)
        
        return optimized_path.coordinates
    
    def _gradient_descent_optimize(self, path: NavigationPath, target: OptimizationTarget) -> NavigationPath:
        """Gradient descent optimization"""
        coordinates = path.coordinates.copy()
        learning_rate = self.parameters.learning_rate
        
        for iteration in range(self.parameters.max_iterations):
            # Calculate gradients for each coordinate
            gradients = self._calculate_gradients(coordinates, target)
            
            # Update coordinates
            for i, coord in enumerate(coordinates):
                if i == 0 or i == len(coordinates) - 1:
                    continue  # Don't move start/end points
                
                # Apply gradient update
                new_position = coord.position - learning_rate * gradients[i]
                
                # Ensure new position is valid
                new_position = self._project_to_valid_space(new_position)
                
                coordinates[i] = TysonCoordinate(new_position, coord.geometry_type, coord.metadata)
            
            # Check convergence
            gradient_norm = np.linalg.norm(np.concatenate([g for g in gradients if g is not None]))
            if gradient_norm < self.parameters.convergence_threshold:
                break
        
        # Recalculate path distance
        total_distance = self._calculate_path_distance(coordinates)
        
        return NavigationPath(coordinates=coordinates, total_distance=total_distance)
    
    def _simulated_annealing_optimize(self, path: NavigationPath, target: OptimizationTarget) -> NavigationPath:
        """Simulated annealing optimization"""
        coordinates = path.coordinates.copy()
        current_cost = self._evaluate_target(coordinates, target)
        best_coordinates = coordinates.copy()
        best_cost = current_cost
        
        temperature = self.parameters.temperature
        
        for iteration in range(self.parameters.max_iterations):
            # Cool down
            temperature *= 0.99
            
            # Generate neighbor solution
            new_coordinates = self._generate_neighbor(coordinates)
            new_cost = self._evaluate_target(new_coordinates, target)
            
            # Accept or reject
            delta_cost = new_cost - current_cost
            
            if delta_cost < 0 or np.random.random() < np.exp(-delta_cost / max(temperature, 0.01)):
                coordinates = new_coordinates
                current_cost = new_cost
                
                if current_cost < best_cost:
                    best_coordinates = coordinates.copy()
                    best_cost = current_cost
        
        total_distance = self._calculate_path_distance(best_coordinates)
        return NavigationPath(coordinates=best_coordinates, total_distance=total_distance)
    
    def _genetic_optimize(self, path: NavigationPath, target: OptimizationTarget) -> NavigationPath:
        """Genetic algorithm optimization"""
        population_size = self.parameters.population_size
        max_generations = self.parameters.max_iterations // 10
        
        # Initialize population
        population = self._initialize_population(path, population_size)
        
        for generation in range(max_generations):
            # Evaluate fitness
            fitness_scores = [self._calculate_fitness(individual, target) for individual in population]
            
            # Selection
            selected = self._tournament_selection(population, fitness_scores)
            
            # Crossover and mutation
            new_population = []
            for i in range(0, len(selected), 2):
                if i + 1 < len(selected):
                    parent1, parent2 = selected[i], selected[i + 1]
                    
                    if np.random.random() < self.parameters.crossover_rate:
                        child1, child2 = self._crossover(parent1, parent2)
                    else:
                        child1, child2 = parent1, parent2
                    
                    if np.random.random() < self.parameters.mutation_rate:
                        child1 = self._mutate(child1)
                        child2 = self._mutate(child2)
                    
                    new_population.extend([child1, child2])
                else:
                    new_population.append(selected[i])
            
            population = new_population
        
        # Return best individual
        fitness_scores = [self._calculate_fitness(individual, target) for individual in population]
        best_path = population[fitness_scores.index(max(fitness_scores))]
        
        return best_path
    
    def _particle_swarm_optimize(self, path: NavigationPath, target: OptimizationTarget) -> NavigationPath:
        """Particle swarm optimization"""
        swarm_size = self.parameters.population_size
        max_iterations = self.parameters.max_iterations
        
        # Initialize swarm
        particles = self._initialize_swarm(path, swarm_size)
        velocities = [self._initialize_velocities(p.coordinates) for p in particles]
        
        # Personal and global bests
        personal_best = particles.copy()
        personal_best_costs = [self._evaluate_target(p.coordinates, target) for p in personal_best]
        global_best = personal_best[personal_best_costs.index(min(personal_best_costs))]
        global_best_cost = min(personal_best_costs)
        
        w = 0.7  # Inertia weight
        c1 = 1.5  # Cognitive coefficient
        c2 = 1.5  # Social coefficient
        
        for iteration in range(max_iterations):
            for i, particle in enumerate(particles):
                # Update velocity
                r1, r2 = np.random.random(), np.random.random()
                
                for j in range(len(velocities[i])):
                    if velocities[i][j] is not None:
                        # Personal influence
                        personal_diff = personal_best[i].coordinates[j].position - particle.coordinates[j].position
                        # Social influence
                        global_diff = global_best.coordinates[j].position - particle.coordinates[j].position
                        
                        velocities[i][j] = (w * velocities[i][j] + 
                                          c1 * r1 * personal_diff + 
                                          c2 * r2 * global_diff)
                        
                        # Update position
                        new_position = particle.coordinates[j].position + velocities[i][j]
                        new_position = self._project_to_valid_space(new_position)
                        
                        particle.coordinates[j] = TysonCoordinate(
                            new_position, 
                            particle.coordinates[j].geometry_type,
                            particle.coordinates[j].metadata
                        )
            
            # Update personal and global bests
            for i, particle in enumerate(particles):
                cost = self._evaluate_target(particle.coordinates, target)
                if cost < personal_best_costs[i]:
                    personal_best[i] = NavigationPath(
                        coordinates=particle.coordinates.copy(),
                        total_distance=self._calculate_path_distance(particle.coordinates)
                    )
                    personal_best_costs[i] = cost
                    
                    if cost < global_best_cost:
                        global_best = NavigationPath(
                            coordinates=particle.coordinates.copy(),
                            total_distance=self._calculate_path_distance(particle.coordinates)
                        )
                        global_best_cost = cost
        
        return global_best
    
    def _bayesian_optimize(self, path: NavigationPath, target: OptimizationTarget) -> NavigationPath:
        """Bayesian optimization (simplified implementation)"""
        # Simplified Bayesian optimization using random sampling with improvement criteria
        coordinates = path.coordinates.copy()
        best_coordinates = coordinates.copy()
        best_cost = self._evaluate_target(coordinates, target)
        
        for iteration in range(self.parameters.max_iterations):
            # Generate candidate solutions
            candidates = []
            for _ in range(10):
                candidate = self._generate_neighbor(best_coordinates)
                cost = self._evaluate_target(candidate, target)
                candidates.append((candidate, cost))
            
            # Select best candidate
            candidates.sort(key=lambda x: x[1])
            if candidates[0][1] < best_cost:
                best_coordinates = candidates[0][0].copy()
                best_cost = candidates[0][1]
        
        total_distance = self._calculate_path_distance(best_coordinates)
        return NavigationPath(coordinates=best_coordinates, total_distance=total_distance)
    
    def _hybrid_optimize(self, path: NavigationPath, target: OptimizationTarget) -> NavigationPath:
        """Hybrid optimization combining multiple strategies"""
        # Start with gradient descent for fast convergence
        path1 = self._gradient_descent_optimize(path, target)
        
        # Refine with simulated annealing
        path2 = self._simulated_annealing_optimize(path1, target)
        
        # Final refinement with particle swarm
        path3 = self._particle_swarm_optimize(path2, target)
        
        return path3
    
    def _calculate_gradients(self, coordinates: List[TysonCoordinate], target: OptimizationTarget) -> List[np.ndarray]:
        """Calculate gradients for coordinate optimization"""
        gradients = []
        epsilon = 1e-6
        
        for i, coord in enumerate(coordinates):
            if i == 0 or i == len(coordinates) - 1:
                gradients.append(None)
                continue
            
            grad = np.zeros_like(coord.position)
            
            # Numerical gradient calculation
            for j in range(len(coord.position)):
                # Forward difference
                coord_plus = TysonCoordinate(
                    coord.position.copy(), 
                    coord.geometry_type, 
                    coord.metadata
                )
                coord_plus.position[j] += epsilon
                
                temp_coords = coordinates.copy()
                temp_coords[i] = coord_plus
                
                cost_plus = self._evaluate_target(temp_coords, target)
                cost_original = self._evaluate_target(coordinates, target)
                
                grad[j] = (cost_plus - cost_original) / epsilon
            
            gradients.append(grad)
        
        return gradients
    
    def _evaluate_target(self, coordinates: List[TysonCoordinate], target: OptimizationTarget) -> float:
        """Evaluate optimization target for given coordinates"""
        if target.metric == "distance":
            return self._calculate_path_distance(coordinates)
        elif target.metric == "complexity":
            return self._calculate_path_complexity(coordinates)
        elif target.metric == "smoothness":
            return self._calculate_path_smoothness(coordinates)
        elif target.metric == "energy":
            return self._calculate_path_energy(coordinates)
        else:
            return self._calculate_path_distance(coordinates)
    
    def _calculate_path_distance(self, coordinates: List[TysonCoordinate]) -> float:
        """Calculate total path distance"""
        total_distance = 0.0
        for i in range(len(coordinates) - 1):
            if hasattr(coordinates[i], 'distance_to'):
                total_distance += coordinates[i].distance_to(coordinates[i + 1])
            else:
                total_distance += np.linalg.norm(coordinates[i].position - coordinates[i + 1].position)
        return total_distance
    
    def _calculate_path_complexity(self, coordinates: List[TysonCoordinate]) -> float:
        """Calculate path complexity"""
        if len(coordinates) < 3:
            return 0.0
        
        # Complexity based on turning angles and coordinate variations
        total_turn = 0.0
        for i in range(1, len(coordinates) - 1):
            v1 = coordinates[i].position - coordinates[i - 1].position
            v2 = coordinates[i + 1].position - coordinates[i].position
            
            if np.linalg.norm(v1) > 0 and np.linalg.norm(v2) > 0:
                cos_angle = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
                cos_angle = np.clip(cos_angle, -1, 1)
                angle = np.arccos(cos_angle)
                total_turn += angle
        
        return total_turn / (len(coordinates) - 2)
    
    def _calculate_path_smoothness(self, coordinates: List[TysonCoordinate]) -> float:
        """Calculate path smoothness (lower is better)"""
        if len(coordinates) < 3:
            return 0.0
        
        # Smoothness based on acceleration
        total_acceleration = 0.0
        for i in range(1, len(coordinates) - 1):
            v1 = coordinates[i].position - coordinates[i - 1].position
            v2 = coordinates[i + 1].position - coordinates[i].position
            acceleration = np.linalg.norm(v2 - v1)
            total_acceleration += acceleration
        
        return total_acceleration / (len(coordinates) - 2)
    
    def _calculate_path_energy(self, coordinates: List[TysonCoordinate]) -> float:
        """Calculate path energy"""
        # Energy based on distance and curvature
        distance = self._calculate_path_distance(coordinates)
        curvature = self._calculate_path_complexity(coordinates)
        
        return distance + 0.1 * curvature
    
    def _generate_neighbor(self, coordinates: List[TysonCoordinate]) -> List[TysonCoordinate]:
        """Generate neighbor solution by random perturbation"""
        new_coordinates = coordinates.copy()
        
        if len(coordinates) > 2:
            # Randomly select a coordinate to perturb
            idx = np.random.randint(1, len(coordinates) - 1)
            coord = coordinates[idx]
            
            # Add random perturbation
            perturbation = np.random.normal(0, 0.1, coord.position.shape)
            new_position = coord.position + perturbation
            new_position = self._project_to_valid_space(new_position)
            
            new_coordinates[idx] = TysonCoordinate(new_position, coord.geometry_type, coord.metadata)
        
        return new_coordinates
    
    def _initialize_population(self, initial_path: NavigationPath, size: int) -> List[NavigationPath]:
        """Initialize population for genetic algorithm"""
        population = [initial_path]
        
        for _ in range(size - 1):
            # Generate random variation of initial path
            coordinates = initial_path.coordinates.copy()
            
            # Add random perturbations
            for i in range(1, len(coordinates) - 1):
                perturbation = np.random.normal(0, 0.05, coordinates[i].position.shape)
                new_position = coordinates[i].position + perturbation
                new_position = self._project_to_valid_space(new_position)
                coordinates[i] = TysonCoordinate(new_position, coordinates[i].geometry_type, coordinates[i].metadata)
            
            total_distance = self._calculate_path_distance(coordinates)
            population.append(NavigationPath(coordinates=coordinates, total_distance=total_distance))
        
        return population
    
    def _initialize_swarm(self, initial_path: NavigationPath, size: int) -> List[NavigationPath]:
        """Initialize particle swarm"""
        return self._initialize_population(initial_path, size)
    
    def _initialize_velocities(self, coordinates: List[TysonCoordinate]) -> List[np.ndarray]:
        """Initialize velocities for particle swarm"""
        velocities = []
        for coord in coordinates:
            if coord is not None:
                velocities.append(np.random.normal(0, 0.01, coord.position.shape))
            else:
                velocities.append(None)
        return velocities
    
    def _calculate_fitness(self, path: NavigationPath, target: OptimizationTarget) -> float:
        """Calculate fitness for genetic algorithm"""
        cost = self._evaluate_target(path.coordinates, target)
        
        # Convert cost to fitness (higher is better)
        if target.direction == "minimize":
            fitness = 1.0 / (1.0 + cost)
        else:
            fitness = cost
        
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
        # Single point crossover
        if len(parent1.coordinates) < 2 or len(parent2.coordinates) < 2:
            return parent1, parent2
        
        crossover_point = min(len(parent1.coordinates), len(parent2.coordinates)) // 2
        
        child1_coords = parent1.coordinates[:crossover_point] + parent2.coordinates[crossover_point:]
        child2_coords = parent2.coordinates[:crossover_point] + parent1.coordinates[crossover_point:]
        
        # Ensure minimum path structure
        if len(child1_coords) < 2:
            child1_coords = [parent1.coordinates[0], parent2.coordinates[-1]]
        if len(child2_coords) < 2:
            child2_coords = [parent2.coordinates[0], parent1.coordinates[-1]]
        
        total_distance1 = self._calculate_path_distance(child1_coords)
        total_distance2 = self._calculate_path_distance(child2_coords)
        
        return (NavigationPath(coordinates=child1_coords, total_distance=total_distance1),
                NavigationPath(coordinates=child2_coords, total_distance=total_distance2))
    
    def _mutate(self, path: NavigationPath) -> NavigationPath:
        """Mutation operation for genetic algorithm"""
        coordinates = path.coordinates.copy()
        
        if len(coordinates) > 2:
            # Random mutation
            mutation_type = np.random.choice(['perturb', 'add', 'remove'])
            
            if mutation_type == 'perturb' and len(coordinates) > 2:
                # Perturb a random coordinate
                idx = np.random.randint(1, len(coordinates) - 1)
                coord = coordinates[idx]
                
                perturbation = np.random.normal(0, 0.1, coord.position.shape)
                new_position = coord.position + perturbation
                new_position = self._project_to_valid_space(new_position)
                
                coordinates[idx] = TysonCoordinate(new_position, coord.geometry_type, coord.metadata)
            
            elif mutation_type == 'add' and len(coordinates) < 20:
                # Add a new coordinate
                idx = np.random.randint(1, len(coordinates))
                new_coord = self._generate_intermediate_coordinate(coordinates[idx - 1], coordinates[idx])
                coordinates.insert(idx, new_coord)
            
            elif mutation_type == 'remove' and len(coordinates) > 3:
                # Remove a coordinate
                idx = np.random.randint(1, len(coordinates) - 1)
                coordinates.pop(idx)
        
        total_distance = self._calculate_path_distance(coordinates)
        return NavigationPath(coordinates=coordinates, total_distance=total_distance)
    
    def _generate_intermediate_coordinate(self, coord1: TysonCoordinate, coord2: TysonCoordinate) -> TysonCoordinate:
        """Generate intermediate coordinate between two coordinates"""
        t = np.random.random()  # Random interpolation parameter
        new_position = (1 - t) * coord1.position + t * coord2.position
        new_position = self._project_to_valid_space(new_position)
        
        return TysonCoordinate(new_position, coord1.geometry_type)
    
    def _project_to_valid_space(self, position: np.ndarray) -> np.ndarray:
        """Project position to valid space"""
        # Simple bounds checking
        if hasattr(self.sphere, 'coordinates') and self.sphere.coordinates:
            positions = np.array([coord.position for coord in self.sphere.coordinates])
            min_bounds = positions.min(axis=0) - 1.0
            max_bounds = positions.max(axis=0) + 1.0
            
            position = np.clip(position, min_bounds, max_bounds)
        
        return position
    
    def _record_optimization(self, strategy: OptimizationStrategy, target: OptimizationTarget, 
                           original_path: NavigationPath, optimized_path: NavigationPath):
        """Record optimization statistics"""
        stats = {
            'strategy': strategy.name,
            'target_metric': target.metric,
            'target_direction': target.direction,
            'original_cost': self._evaluate_target(original_path.coordinates, target),
            'optimized_cost': self._evaluate_target(optimized_path.coordinates, target),
            'improvement': self._evaluate_target(original_path.coordinates, target) - self._evaluate_target(optimized_path.coordinates, target),
            'timestamp': np.datetime64('now').astype(str)
        }
        
        self.optimization_history.append(stats)
        
        # Update performance metrics
        key = f"{strategy.name}_{target.metric}"
        if key not in self.performance_metrics:
            self.performance_metrics[key] = {
                'count': 0,
                'avg_improvement': 0.0,
                'success_rate': 0.0
            }
        
        metrics = self.performance_metrics[key]
        metrics['count'] += 1
        metrics['avg_improvement'] = (metrics['avg_improvement'] * (metrics['count'] - 1) + stats['improvement']) / metrics['count']
        
        if stats['improvement'] > 0:
            metrics['success_rate'] = (metrics['success_rate'] * (metrics['count'] - 1) + 1.0) / metrics['count']
        else:
            metrics['success_rate'] = (metrics['success_rate'] * (metrics['count'] - 1)) / metrics['count']
    
    def get_performance_metrics(self) -> Dict[str, Any]:
        """Get optimization performance metrics"""
        return self.performance_metrics.copy()
    
    def get_optimization_history(self) -> List[Dict[str, Any]]:
        """Get optimization history"""
        return self.optimization_history.copy()