"""
Output Generator

Generates various output formats from information spheres for
different use cases and interfaces.
"""

import numpy as np
import json
import matplotlib.pyplot as plt
from typing import Any, Dict, List, Optional, Union, Tuple
from dataclasses import dataclass, field
from enum import Enum, auto

from ..core.geometry_base import InformationSphere
from ..core.coordinates import TysonCoordinate
from ..core.structures import NavigationPath


class OutputFormat(Enum):
    """Supported output formats"""
    JSON = auto()
    VISUALIZATION = auto()
    ANALYTICS = auto()
    NAVIGATION_DATA = auto()
    REPORT = auto()
    COORDINATES = auto()
    METADATA = auto()


@dataclass
class OutputOptions:
    """Options for output generation"""
    format: OutputFormat = OutputFormat.JSON
    include_metadata: bool = True
    include_coordinates: bool = True
    precision: int = 6
    pretty_print: bool = True
    visualization_options: Dict[str, Any] = field(default_factory=dict)


class OutputGenerator:
    """
    Generates various output formats from information spheres
    
    Features:
    - Multiple output formats (JSON, visualization, analytics)
    - Configurable output options
    - Efficient data serialization
    - Visualization capabilities
    """
    
    def __init__(self):
        self.output_history = []
        
        # Visualization defaults
        self.default_viz_options = {
            'figsize': (10, 8),
            'dpi': 100,
            'style': 'seaborn-v0_8',
            'colormap': 'viridis',
            'show_grid': True,
            'show_axes': True
        }
    
    def generate_output(self, sphere: InformationSphere, 
                       options: Optional[OutputOptions] = None) -> Dict[str, Any]:
        """
        Generate output in the specified format
        
        Returns a dictionary with the output data and metadata.
        """
        if options is None:
            options = OutputOptions()
        
        # Generate output based on format
        if options.format == OutputFormat.JSON:
            output_data = self._generate_json_output(sphere, options)
        elif options.format == OutputFormat.VISUALIZATION:
            output_data = self._generate_visualization(sphere, options)
        elif options.format == OutputFormat.ANALYTICS:
            output_data = self._generate_analytics(sphere, options)
        elif options.format == OutputFormat.NAVIGATION_DATA:
            output_data = self._generate_navigation_output(sphere, options)
        elif options.format == OutputFormat.REPORT:
            output_data = self._generate_report(sphere, options)
        elif options.format == OutputFormat.COORDINATES:
            output_data = self._generate_coordinates_output(sphere, options)
        elif options.format == OutputFormat.METADATA:
            output_data = self._generate_metadata_output(sphere, options)
        else:
            raise ValueError(f"Unsupported output format: {options.format}")
        
        # Add output metadata
        result = {
            'data': output_data,
            'format': options.format.name,
            'timestamp': np.datetime64('now').astype(str),
            'sphere_info': {
                'geometry_type': sphere.geometry_type.name,
                'coordinate_count': len(sphere.coordinates),
                'properties': sphere.properties.__dict__ if sphere.properties else {}
            }
        }
        
        # Record output
        self.output_history.append(result)
        
        return result
    
    def _generate_json_output(self, sphere: InformationSphere, options: OutputOptions) -> Dict[str, Any]:
        """Generate JSON format output"""
        data = {
            'geometry_type': sphere.geometry_type.name,
            'properties': sphere.properties.__dict__ if sphere.properties else {}
        }
        
        if options.include_coordinates:
            data['coordinates'] = []
            for coord in sphere.coordinates:
                coord_data = {
                    'position': coord.position.tolist(),
                    'geometry_type': coord.geometry_type,
                    'metadata': coord.metadata
                }
                data['coordinates'].append(coord_data)
        
        if options.include_metadata:
            data['metadata'] = {
                'generation_timestamp': sphere.metadata.get('generation_timestamp', ''),
                'optimization_applied': sphere.metadata.get('optimization_applied', False),
                'processing_time': sphere.metadata.get('processing_time', 0.0)
            }
        
        return data
    
    def _generate_visualization(self, sphere: InformationSphere, options: OutputOptions) -> Dict[str, Any]:
        """Generate visualization output"""
        viz_options = {**self.default_viz_options, **options.visualization_options}
        
        # Create figure
        fig, axes = plt.subplots(figsize=viz_options['figsize'], dpi=viz_options['dpi'])
        
        # Plot coordinates
        if sphere.coordinates:
            positions = np.array([coord.position for coord in sphere.coordinates])
            
            if positions.shape[1] == 1:
                # 1D plot
                axes.scatter(positions[:, 0], np.zeros_like(positions[:, 0]), 
                          c=range(len(positions)), cmap=viz_options['colormap'])
                axes.set_xlabel('Position')
                axes.set_title(f'{sphere.geometry_type.name} Sphere (1D)')
            elif positions.shape[1] == 2:
                # 2D plot
                axes.scatter(positions[:, 0], positions[:, 1], 
                          c=range(len(positions)), cmap=viz_options['colormap'])
                axes.set_xlabel('X')
                axes.set_ylabel('Y')
                axes.set_title(f'{sphere.geometry_type.name} Sphere (2D)')
            elif positions.shape[1] >= 3:
                # 3D plot (project to 2D)
                axes.scatter(positions[:, 0], positions[:, 1], 
                          c=positions[:, 2], cmap=viz_options['colormap'])
                axes.set_xlabel('X')
                axes.set_ylabel('Y')
                axes.set_title(f'{sphere.geometry_type.name} Sphere (3D projected to 2D)')
            
            if viz_options['show_grid']:
                axes.grid(True, alpha=0.3)
        
        # Save figure
        import io
        import base64
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png', bbox_inches='tight')
        buffer.seek(0)
        image_base64 = base64.b64encode(buffer.read()).decode()
        plt.close()
        
        return {
            'image_data': image_base64,
            'format': 'base64_png',
            'visualization_options': viz_options
        }
    
    def _generate_analytics(self, sphere: InformationSphere, options: OutputOptions) -> Dict[str, Any]:
        """Generate analytics output"""
        analytics = {
            'sphere_statistics': {},
            'coordinate_analysis': {},
            'geometry_metrics': {}
        }
        
        if sphere.coordinates:
            positions = np.array([coord.position for coord in sphere.coordinates])
            
            # Sphere statistics
            analytics['sphere_statistics'] = {
                'coordinate_count': len(sphere.coordinates),
                'dimensionality': positions.shape[1],
                'center': np.mean(positions, axis=0).tolist(),
                'spread': np.std(positions, axis=0).tolist(),
                'bounds': {
                    'min': positions.min(axis=0).tolist(),
                    'max': positions.max(axis=0).tolist()
                }
            }
            
            # Coordinate analysis
            distances = []
            for i, coord1 in enumerate(sphere.coordinates):
                for coord2 in sphere.coordinates[i+1:]:
                    if hasattr(coord1, 'distance_to'):
                        distances.append(coord1.distance_to(coord2))
            
            if distances:
                analytics['coordinate_analysis'] = {
                    'mean_distance': np.mean(distances),
                    'min_distance': np.min(distances),
                    'max_distance': np.max(distances),
                    'std_distance': np.std(distances)
                }
            
            # Geometry-specific metrics
            analytics['geometry_metrics'] = self._calculate_geometry_metrics(sphere)
        
        return analytics
    
    def _generate_navigation_output(self, sphere: InformationSphere, options: OutputOptions) -> Dict[str, Any]:
        """Generate navigation-specific output"""
        nav_data = {
            'navigation_grid': {},
            'adjacency_matrix': [],
            'path_suggestions': []
        }
        
        if sphere.coordinates:
            # Generate adjacency matrix
            n = len(sphere.coordinates)
            adjacency_matrix = np.zeros((n, n))
            
            for i, coord1 in enumerate(sphere.coordinates):
                for j, coord2 in enumerate(sphere.coordinates):
                    if i != j:
                        if hasattr(coord1, 'distance_to'):
                            distance = coord1.distance_to(coord2)
                            adjacency_matrix[i, j] = 1.0 / (distance + 1.0)  # Inverse distance
            
            nav_data['adjacency_matrix'] = adjacency_matrix.tolist()
            
            # Generate navigation grid (simplified)
            positions = np.array([coord.position for coord in sphere.coordinates])
            if positions.shape[1] <= 3:  # Only for low dimensions
                grid_points = self._generate_navigation_grid(positions, resolution=10)
                nav_data['navigation_grid'] = {
                    'points': grid_points.tolist(),
                    'resolution': 10
                }
        
        return nav_data
    
    def _generate_report(self, sphere: InformationSphere, options: OutputOptions) -> Dict[str, Any]:
        """Generate comprehensive report"""
        report = {
            'summary': '',
            'detailed_analysis': {},
            'recommendations': []
        }
        
        # Generate summary
        summary_parts = [
            f"Information Sphere Report",
            f"Geometry Type: {sphere.geometry_type.name}",
            f"Coordinate Count: {len(sphere.coordinates)}",
            f"Generated: {sphere.metadata.get('generation_timestamp', 'Unknown')}"
        ]
        
        report['summary'] = '\n'.join(summary_parts)
        
        # Detailed analysis
        report['detailed_analysis'] = self._generate_analytics(sphere, options)
        
        # Recommendations
        report['recommendations'] = self._generate_recommendations(sphere)
        
        return report
    
    def _generate_coordinates_output(self, sphere: InformationSphere, options: OutputOptions) -> Dict[str, Any]:
        """Generate coordinates-only output"""
        coords_data = []
        
        for i, coord in enumerate(sphere.coordinates):
            coord_data = {
                'index': i,
                'position': coord.position.round(options.precision).tolist(),
                'geometry_type': coord.geometry_type
            }
            
            if options.include_metadata:
                coord_data['metadata'] = coord.metadata
            
            coords_data.append(coord_data)
        
        return {
            'coordinates': coords_data,
            'count': len(coords_data),
            'dimensionality': len(sphere.coordinates[0].position) if sphere.coordinates else 0
        }
    
    def _generate_metadata_output(self, sphere: InformationSphere, options: OutputOptions) -> Dict[str, Any]:
        """Generate metadata-only output"""
        metadata = {
            'sphere_metadata': sphere.metadata,
            'geometry_type': sphere.geometry_type.name,
            'coordinate_count': len(sphere.coordinates),
            'properties': sphere.properties.__dict__ if sphere.properties else {}
        }
        
        if sphere.properties:
            metadata['property_analysis'] = {
                'radius': sphere.properties.radius,
                'curvature': sphere.properties.curvature,
                'volume': sphere.properties.volume,
                'surface_area': sphere.properties.surface_area,
                'density': sphere.properties.density,
                'dimensionality': sphere.properties.dimensionality
            }
        
        return metadata
    
    def _calculate_geometry_metrics(self, sphere: InformationSphere) -> Dict[str, Any]:
        """Calculate geometry-specific metrics"""
        metrics = {}
        
        if sphere.geometry_type.name == "BANACHIAN":
            metrics['banachian_norm_type'] = sphere.metadata.get('norm_type', 'euclidean')
            metrics['completeness_score'] = sphere.metadata.get('completeness_score', 0.0)
        
        elif sphere.geometry_type.name == "QUANTUM":
            metrics['deformation_parameter'] = sphere.metadata.get('deformation_parameter', 0.7)
            metrics['quantum_coherence'] = sphere.metadata.get('quantum_coherence', 0.8)
        
        elif sphere.geometry_type.name == "FUZZY":
            metrics['fuzziness_parameter'] = sphere.metadata.get('fuzziness_parameter', 0.5)
            metrics['membership_function'] = sphere.metadata.get('membership_function', 'gaussian')
        
        elif sphere.geometry_type.name == "HADWIGER_NELSON":
            metrics['chromatic_number'] = sphere.metadata.get('chromatic_number', 7)
            metrics['angular_content'] = sphere.metadata.get('angular_content', 0.0)
        
        elif sphere.geometry_type.name == "RELATIONAL":
            metrics['synthesis_strategy'] = sphere.metadata.get('synthesis_strategy', 'adaptive')
            metrics['geometry_weights'] = sphere.metadata.get('geometry_weights', {})
        
        return metrics
    
    def _generate_navigation_grid(self, positions: np.ndarray, resolution: int = 10) -> np.ndarray:
        """Generate navigation grid points"""
        if positions.shape[1] == 1:
            # 1D grid
            min_val, max_val = positions.min(), positions.max()
            return np.linspace(min_val, max_val, resolution).reshape(-1, 1)
        
        elif positions.shape[1] == 2:
            # 2D grid
            x_min, x_max = positions[:, 0].min(), positions[:, 0].max()
            y_min, y_max = positions[:, 1].min(), positions[:, 1].max()
            
            x = np.linspace(x_min, x_max, resolution)
            y = np.linspace(y_min, y_max, resolution)
            
            xx, yy = np.meshgrid(x, y)
            return np.column_stack([xx.ravel(), yy.ravel()])
        
        elif positions.shape[1] == 3:
            # 3D grid (lower resolution)
            x_min, x_max = positions[:, 0].min(), positions[:, 0].max()
            y_min, y_max = positions[:, 1].min(), positions[:, 1].max()
            z_min, z_max = positions[:, 2].min(), positions[:, 2].max()
            
            x = np.linspace(x_min, x_max, resolution // 2)
            y = np.linspace(y_min, y_max, resolution // 2)
            z = np.linspace(z_min, z_max, resolution // 2)
            
            xx, yy, zz = np.meshgrid(x, y, z)
            return np.column_stack([xx.ravel(), yy.ravel(), zz.ravel()])
        
        return np.array([[0.0]])
    
    def _generate_recommendations(self, sphere: InformationSphere) -> List[str]:
        """Generate recommendations based on sphere analysis"""
        recommendations = []
        
        if len(sphere.coordinates) < 10:
            recommendations.append("Consider adding more coordinates for better representation")
        
        if sphere.properties and sphere.properties.complexity > 0.8:
            recommendations.append("High complexity sphere - consider optimization")
        
        if sphere.geometry_type.name == "RELATIONAL":
            recommendations.append("RELATIONAL geometry provides comprehensive representation")
        
        return recommendations
    
    def save_output(self, output_data: Dict[str, Any], filename: str) -> bool:
        """Save output to file"""
        try:
            if isinstance(output_data['data'], dict):
                with open(filename, 'w') as f:
                    json.dump(output_data['data'], f, indent=2 if output_data.get('pretty_print', True) else None)
            return True
        except Exception as e:
            print(f"Error saving output: {e}")
            return False
    
    def get_output_history(self) -> List[Dict[str, Any]]:
        """Get history of generated outputs"""
        return self.output_history.copy()