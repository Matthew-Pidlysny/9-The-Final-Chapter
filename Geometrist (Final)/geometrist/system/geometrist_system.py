"""
Geometrist System

Main system that integrates all components into a unified framework
for processing informational quanta and generating geometric representations.
"""

import numpy as np
import time
from typing import Dict, List, Any, Optional, Union
from dataclasses import dataclass, field
from enum import Enum, auto

from ..core import *
from ..geometries import *
from ..navigation import *
from .input_analyzer import InputAnalyzer
from .output_generator import OutputGenerator


class SystemMode(Enum):
    """Operating modes for the Geometrist system"""
    AUTOMATIC = auto()       # Fully automatic geometry selection
    MANUAL = auto()          # Manual geometry specification
    LEARNING = auto()        # Learning mode with optimization
    PERFORMANCE = auto()     # Performance-optimized mode
    ACCURACY = auto()        # Accuracy-optimized mode


@dataclass
class SystemConfiguration:
    """Configuration for the Geometrist system"""
    mode: SystemMode = SystemMode.AUTOMATIC
    default_geometry: Optional[GeometryType] = None
    optimization_goal: str = "balance"
    enable_learning: bool = True
    max_complexity: float = 1.0
    cache_results: bool = True
    log_operations: bool = True
    performance_tracking: bool = True


@dataclass
class ProcessingResult:
    """Result of processing informational quanta"""
    success: bool
    sphere: Optional[InformationSphere] = None
    processing_time: float = 0.0
    geometry_used: Optional[GeometryType] = None
    metadata: Dict[str, Any] = field(default_factory=dict)
    warnings: List[str] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)


class GeometristSystem:
    """
    Main Geometrist system that unifies all components
    
    Provides a complete framework for:
    - Analyzing informational quanta
    - Selecting optimal geometries
    - Generating information spheres
    - Navigation and optimization
    - Output generation
    """
    
    def __init__(self, configuration: Optional[SystemConfiguration] = None):
        self.config = configuration if configuration else SystemConfiguration()
        
        # Initialize core components
        self.geometry_factory = GeometryFactory()
        self.input_analyzer = InputAnalyzer()
        self.output_generator = OutputGenerator()
        
        # Navigation system (initialized per sphere)
        self.navigator: Optional[TysonNavigator] = None
        
        # Performance tracking
        self.processing_history = []
        self.performance_metrics = {}
        
        # Learning system
        self.learning_enabled = self.config.enable_learning
        self.adaptation_history = []
        
        # Caching system
        self.result_cache = {} if self.config.cache_results else None
        
        # Initialize system
        self._initialize_system()
    
    def _initialize_system(self):
        """Initialize system components"""
        # Set geometry factory strategy based on configuration
        if self.config.mode == SystemMode.PERFORMANCE:
            self.geometry_factory.set_selection_strategy(SelectionStrategy.EFFICIENCY)
        elif self.config.mode == SystemMode.ACCURACY:
            self.geometry_factory.set_selection_strategy(SelectionStrategy.ACCURACY)
        elif self.config.mode == SystemMode.LEARNING:
            self.geometry_factory.set_selection_strategy(SelectionStrategy.ADAPTIVE)
        
        if self.config.log_operations:
            self._log("Geometrist system initialized")
    
    def process_quanta(self, data: Any, 
                      quanta_type: Optional[QuantaType] = None,
                      geometry_override: Optional[GeometryType] = None,
                      properties_override: Optional[QuantaProperties] = None) -> ProcessingResult:
        """
        Process informational quanta and generate optimal geometric representation
        
        Main entry point for the Geometrist system.
        """
        start_time = time.time()
        
        try:
            # Create information quanta
            quanta = self._create_quanta(data, quanta_type, properties_override)
            
            # Validate quanta
            if not quanta.validate():
                return ProcessingResult(
                    success=False,
                    errors=["Invalid information quanta"],
                    processing_time=time.time() - start_time
                )
            
            # Check cache
            cache_key = self._get_cache_key(quanta, geometry_override)
            if self.result_cache and cache_key in self.result_cache:
                cached_result = self.result_cache[cache_key]
                cached_result.processing_time = time.time() - start_time
                return cached_result
            
            # Select geometry
            geometry_type = self._select_geometry(quanta, geometry_override)
            
            # Generate information sphere
            sphere = self._generate_sphere(quanta, geometry_type)
            
            # Initialize navigation
            self.navigator = TysonNavigator(sphere)
            
            # Optimize if enabled
            if self.config.optimization_goal != "none":
                sphere = self._optimize_sphere(sphere)
            
            # Create result
            result = ProcessingResult(
                success=True,
                sphere=sphere,
                processing_time=time.time() - start_time,
                geometry_used=geometry_type,
                metadata={
                    'quanta_id': quanta.id,
                    'quanta_type': quanta.quanta_type.name,
                    'complexity': quanta.properties.complexity,
                    'geometry_engine': geometry_type.name,
                    'sphere_properties': sphere.properties.__dict__,
                    'navigation_initialized': self.navigator is not None
                }
            )
            
            # Cache result
            if self.result_cache:
                self.result_cache[cache_key] = result
            
            # Update learning
            if self.learning_enabled:
                self._update_learning(quanta, geometry_type, result)
            
            # Track performance
            if self.config.performance_tracking:
                self._track_performance(result)
            
            # Log operation
            if self.config.log_operations:
                self._log(f"Processed quanta: {quanta.id} using {geometry_type.name}")
            
            return result
            
        except Exception as e:
            error_msg = f"Error processing quanta: {str(e)}"
            if self.config.log_operations:
                self._log(error_msg, level="ERROR")
            
            return ProcessingResult(
                success=False,
                errors=[error_msg],
                processing_time=time.time() - start_time
            )
    
    def navigate_to_coordinate(self, target_position: Union[np.ndarray, List[float]],
                              navigation_mode: Optional[str] = None) -> Optional[NavigationPath]:
        """Navigate to a target coordinate within the current sphere"""
        if not self.navigator:
            return None
        
        # Create target coordinate
        if isinstance(target_position, list):
            target_position = np.array(target_position)
        
        target_coord = TysonCoordinate(
            position=target_position,
            geometry_type=self.navigator.sphere.geometry_type.name.lower()
        )
        
        # Set navigation mode
        if navigation_mode:
            mode_map = {
                'direct': NavigationMode.DIRECT,
                'optimal': NavigationMode.OPTIMAL,
                'adaptive': NavigationMode.ADAPTIVE,
                'exploratory': NavigationMode.EXPLORATORY,
                'constraint_aware': NavigationMode.CONSTRAINT_AWARE
            }
            
            if navigation_mode.lower() in mode_map:
                self.navigator.set_navigation_mode(mode_map[navigation_mode.lower()])
        
        # Navigate
        return self.navigator.navigate_to(target_coord)
    
    def analyze_current_sphere(self) -> Dict[str, Any]:
        """Analyze the current information sphere"""
        if not self.navigator:
            return {"error": "No active sphere to analyze"}
        
        sphere = self.navigator.sphere
        
        analysis = {
            'sphere_info': {
                'geometry_type': sphere.geometry_type.name,
                'coordinate_count': len(sphere.coordinates),
                'radius': sphere.properties.radius,
                'dimensionality': sphere.properties.dimensionality,
                'density': sphere.properties.density
            },
            'navigation_info': self.navigator.get_navigation_statistics(),
            'geometry_analysis': self.geometry_factory.analyze_geometry_performance()
        }
        
        return analysis
    
    def optimize_system(self, goal: str = "performance") -> Dict[str, Any]:
        """Optimize system performance"""
        optimizations = {}
        
        # Optimize geometry factory
        if goal in ["performance", "accuracy"]:
            self.geometry_factory.update_geometry_profiles()
            optimizations['geometry_factory_updated'] = True
        
        # Optimize navigator
        if self.navigator:
            nav_optimization = self.navigator.optimize_navigation(goal)
            optimizations['navigation_optimization'] = nav_optimization
        
        # Clear cache if memory is a concern
        if self.result_cache and len(self.result_cache) > 1000:
            # Keep recent half
            items = list(self.result_cache.items())
            self.result_cache = dict(items[-500:])
            optimizations['cache_cleared'] = True
        
        optimizations['optimization_goal'] = goal
        optimizations['timestamp'] = time.time()
        
        return optimizations
    
    def _create_quanta(self, data: Any, 
                      quanta_type: Optional[QuantaType] = None,
                      properties_override: Optional[QuantaProperties] = None) -> InformationQuanta:
        """Create information quanta from input data"""
        # Auto-detect quanta type if not specified
        if quanta_type is None:
            quanta_type = self.input_analyzer.detect_quanta_type(data)
        
        # Use overridden properties or auto-detect
        if properties_override:
            properties = properties_override
        else:
            properties = QuantaProperties()
        
        return InformationQuanta(data=data, quanta_type=quanta_type, properties=properties)
    
    def _select_geometry(self, quanta: InformationQuanta, 
                        geometry_override: Optional[GeometryType] = None) -> GeometryType:
        """Select optimal geometry for the quanta"""
        if geometry_override:
            return geometry_override
        
        if self.config.mode == SystemMode.MANUAL and self.config.default_geometry:
            return self.config.default_geometry
        
        # Use geometry factory for intelligent selection
        strategy_map = {
            SystemMode.AUTOMATIC: SelectionStrategy.ADAPTIVE,
            SystemMode.PERFORMANCE: SelectionStrategy.EFFICIENCY,
            SystemMode.ACCURACY: SelectionStrategy.ACCURACY,
            SystemMode.LEARNING: SelectionStrategy.ADAPTIVE
        }
        
        strategy = strategy_map.get(self.config.mode, SelectionStrategy.ADAPTIVE)
        return self.geometry_factory.select_optimal_geometry(quanta, strategy)
    
    def _generate_sphere(self, quanta: InformationQuanta, 
                        geometry_type: GeometryType) -> InformationSphere:
        """Generate information sphere using selected geometry"""
        engine = self.geometry_factory.geometry_engines[geometry_type]
        
        # Apply system constraints
        constraints = GenerationConstraints(
            max_complexity=self.config.max_complexity,
            optimization_goal=self.config.optimization_goal
        )
        
        return engine.generate_sphere(quanta, constraints)
    
    def _optimize_sphere(self, sphere: InformationSphere) -> InformationSphere:
        """Optimize the information sphere"""
        engine = self.geometry_factory.geometry_engines[sphere.geometry_type]
        return engine.optimize_representation(sphere, self.config.optimization_goal)
    
    def _get_cache_key(self, quanta: InformationQuanta, 
                      geometry_override: Optional[GeometryType]) -> str:
        """Generate cache key for quanta processing"""
        key_data = f"{quanta.id}_{quanta.quanta_type.name}_{geometry_override.name if geometry_override else 'auto'}"
        return str(hash(key_data))
    
    def _update_learning(self, quanta: InformationQuanta, 
                        geometry_type: GeometryType, 
                        result: ProcessingResult):
        """Update learning system with processing results"""
        learning_record = {
            'timestamp': time.time(),
            'quanta_complexity': quanta.properties.complexity,
            'quanta_type': quanta.quanta_type.name,
            'selected_geometry': geometry_type.name,
            'processing_time': result.processing_time,
            'success': result.success,
            'sphere_quality': self._evaluate_sphere_quality(result.sphere) if result.sphere else 0.0
        }
        
        self.adaptation_history.append(learning_record)
        
        # Keep history manageable
        if len(self.adaptation_history) > 1000:
            self.adaptation_history = self.adaptation_history[-500:]
        
        # Adapt system parameters based on learning
        if len(self.adaptation_history) > 10:
            self._adapt_parameters()
    
    def _evaluate_sphere_quality(self, sphere: InformationSphere) -> float:
        """Evaluate quality of generated sphere"""
        if not sphere:
            return 0.0
        
        quality_score = 0.0
        
        # Coordinate density score
        if sphere.properties.volume > 0:
            density_score = min(1.0, sphere.properties.density / 10.0)
            quality_score += density_score * 0.3
        
        # Dimensionality efficiency
        dim_score = 1.0 / max(1.0, sphere.properties.dimensionality / 3.0)
        quality_score += dim_score * 0.2
        
        # Constraint satisfaction (simplified)
        try:
            engine = self.geometry_factory.geometry_engines[sphere.geometry_type]
            if engine.validate_constraints(sphere):
                quality_score += 0.5
        except:
            pass
        
        return min(1.0, quality_score)
    
    def _adapt_parameters(self):
        """Adapt system parameters based on learning history"""
        recent_records = self.adaptation_history[-50:]
        
        # Analyze success rates by geometry
        geometry_success = {}
        for record in recent_records:
            geom = record['selected_geometry']
            if geom not in geometry_success:
                geometry_success[geom] = {'success': 0, 'total': 0}
            
            geometry_success[geom]['total'] += 1
            if record['success']:
                geometry_success[geom]['success'] += 1
        
        # Update geometry factory with insights
        for geom, stats in geometry_success.items():
            success_rate = stats['success'] / stats['total'] if stats['total'] > 0 else 0.5
            
            # Adjust selection preferences
            if success_rate < 0.3 and geom in self.geometry_factory.geometry_profiles:
                # Reduce preference for underperforming geometry
                profile = self.geometry_factory.geometry_profiles[GeometryType[geom.upper()]]
                profile.accuracy_score *= 0.9
    
    def _track_performance(self, result: ProcessingResult):
        """Track system performance metrics"""
        self.processing_history.append({
            'timestamp': time.time(),
            'success': result.success,
            'processing_time': result.processing_time,
            'geometry_used': result.geometry_used.name if result.geometry_used else None,
            'metadata': result.metadata
        })
        
        # Keep history manageable
        if len(self.processing_history) > 1000:
            self.processing_history = self.processing_history[-500:]
        
        # Update performance metrics
        self._update_performance_metrics()
    
    def _update_performance_metrics(self):
        """Update performance metrics"""
        if not self.processing_history:
            return
        
        recent_history = self.processing_history[-100:]
        
        # Calculate metrics
        total_processed = len(recent_history)
        successful = sum(1 for record in recent_history if record['success'])
        avg_processing_time = np.mean([record['processing_time'] for record in recent_history])
        
        # Geometry usage statistics
        geometry_usage = {}
        for record in recent_history:
            geom = record['geometry_used']
            if geom:
                geometry_usage[geom] = geometry_usage.get(geom, 0) + 1
        
        self.performance_metrics = {
            'total_processed': total_processed,
            'success_rate': successful / total_processed if total_processed > 0 else 0.0,
            'average_processing_time': avg_processing_time,
            'geometry_usage': geometry_usage,
            'last_updated': time.time()
        }
    
    def get_system_status(self) -> Dict[str, Any]:
        """Get comprehensive system status"""
        status = {
            'configuration': {
                'mode': self.config.mode.name,
                'optimization_goal': self.config.optimization_goal,
                'learning_enabled': self.learning_enabled,
                'cache_enabled': self.result_cache is not None
            },
            'performance': self.performance_metrics,
            'components': {
                'geometry_factory': self.geometry_factory.analyze_geometry_performance(),
                'navigator_available': self.navigator is not None,
                'dynamic_geometries': self.geometry_factory.get_dynamic_geometries()
            },
            'learning': {
                'adaptation_records': len(self.adaptation_history),
                'learning_enabled': self.learning_enabled
            }
        }
        
        return status
    
    def _log(self, message: str, level: str = "INFO"):
        """Log system messages"""
        if self.config.log_operations:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            print(f"[{timestamp}] [{level}] GeometristSystem: {message}")
    
    def reset_system(self):
        """Reset system to initial state"""
        self.navigator = None
        self.processing_history = []
        self.adaptation_history = []
        
        if self.result_cache:
            self.result_cache = {}
        
        if self.config.log_operations:
            self._log("System reset completed")
    
    def export_configuration(self) -> Dict[str, Any]:
        """Export current system configuration"""
        return {
            'configuration': self.config.__dict__,
            'performance_metrics': self.performance_metrics,
            'geometry_profiles': {
                geom.name: profile.__dict__ 
                for geom, profile in self.geometry_factory.geometry_profiles.items()
            }
        }
    
    def import_configuration(self, config_data: Dict[str, Any]):
        """Import system configuration"""
        if 'configuration' in config_data:
            # Update configuration
            for key, value in config_data['configuration'].items():
                if hasattr(self.config, key):
                    setattr(self.config, key, value)
        
        if 'geometry_profiles' in config_data:
            # Update geometry profiles
            for geom_name, profile_data in config_data['geometry_profiles'].items():
                try:
                    geom_type = GeometryType[geom_name.upper()]
                    if geom_type in self.geometry_factory.geometry_profiles:
                        profile = self.geometry_factory.geometry_profiles[geom_type]
                        for key, value in profile_data.items():
                            if hasattr(profile, key):
                                setattr(profile, key, value)
                except KeyError:
                    continue
        
        if self.config.log_operations:
            self._log("Configuration imported successfully")