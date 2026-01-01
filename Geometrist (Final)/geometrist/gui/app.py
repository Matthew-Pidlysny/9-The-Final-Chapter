"""
Main Geometrist GUI Application

Flask-based web application with advanced visualization and interactive controls.
"""

from flask import Flask, render_template, jsonify, request, send_file
import json
import numpy as np
import base64
import io
from datetime import datetime
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from geometrist.core import *
from geometrist.geometries import *
from geometrist.navigation import *
from geometrist.system import *


class GeometristApp:
    """Main GUI application for Geometrist system"""
    
    def __init__(self, host='0.0.0.0', port=8080, debug=False):
        self.host = host
        self.port = port
        self.debug = debug
        
        # Initialize Flask app
        self.app = Flask(__name__)
        self.app.config['SECRET_KEY'] = 'geometrist_advanced_gui_2024'
        
        # Initialize Geometrist system
        self.geometrist = GeometristSystem()
        
        # Session management
        self.sessions = {}
        self.session_counter = 0
        
        # Setup routes
        self.setup_routes()
        
        # Performance tracking
        self.performance_history = []
        self.test_results = []
    
    def setup_routes(self):
        """Setup Flask routes"""
        
        @self.app.route('/')
        def index():
            """Main dashboard"""
            return render_template('dashboard.html')
        
        @self.app.route('/analyzer')
        def analyzer():
            """Data analyzer page"""
            return render_template('analyzer.html')
        
        @self.app.route('/visualizer')
        def visualizer():
            """Geometry visualizer page"""
            return render_template('visualizer.html')
        
        @self.app.route('/navigator')
        def navigator():
            """Navigation simulator page"""
            return render_template('navigator.html')
        
        @self.app.route('/testing')
        def testing():
            """Advanced testing page"""
            return render_template('testing.html')
        
        @self.app.route('/api/analyze', methods=['POST'])
        def api_analyze():
            """Analyze input data"""
            try:
                data = request.get_json()
                input_data = data.get('data', [])
                data_type = data.get('type', 'auto')
                
                # Create session
                session_id = self.create_session()
                
                # Process data
                result = self.geometrist.process_quanta(input_data)
                
                # Store result
                self.sessions[session_id]['result'] = result
                self.sessions[session_id]['input_data'] = input_data
                
                # Prepare response
                response = {
                    'session_id': session_id,
                    'success': result.success,
                    'geometry_used': result.geometry_used.name if result.geometry_used else None,
                    'processing_time': result.processing_time,
                    'coordinate_count': len(result.sphere.coordinates) if result.sphere else 0,
                    'analysis': self.analyze_result(result),
                    'recommendations': self.generate_recommendations(result)
                }
                
                return jsonify(response)
                
            except Exception as e:
                return jsonify({'error': str(e)}), 500
        
        @self.app.route('/api/visualize', methods=['POST'])
        def api_visualize():
            """Generate visualization"""
            try:
                data = request.get_json()
                session_id = data.get('session_id')
                viz_type = data.get('type', '3d')
                
                if session_id not in self.sessions:
                    return jsonify({'error': 'Invalid session'}), 400
                
                result = self.sessions[session_id]['result']
                
                if not result.success or not result.sphere:
                    return jsonify({'error': 'No valid sphere to visualize'}), 400
                
                # Generate visualization
                viz_data = self.generate_visualization(result.sphere, viz_type)
                
                return jsonify({
                    'visualization': viz_data,
                    'metadata': {
                        'geometry_type': result.geometry_type.name,
                        'coordinate_count': len(result.sphere.coordinates),
                        'sphere_properties': result.sphere.properties.__dict__
                    }
                })
                
            except Exception as e:
                return jsonify({'error': str(e)}), 500
        
        @self.app.route('/api/navigate', methods=['POST'])
        def api_navigate():
            """Generate navigation path"""
            try:
                data = request.get_json()
                session_id = data.get('session_id')
                start_idx = data.get('start', 0)
                end_idx = data.get('end', -1)
                algorithm = data.get('algorithm', 'astar')
                
                if session_id not in self.sessions:
                    return jsonify({'error': 'Invalid session'}), 400
                
                result = self.sessions[session_id]['result']
                
                if not result.success or not result.sphere:
                    return jsonify({'error': 'No valid sphere for navigation'}), 400
                
                # Generate navigation path
                path_data = self.generate_navigation_path(result.sphere, start_idx, end_idx, algorithm)
                
                return jsonify(path_data)
                
            except Exception as e:
                return jsonify({'error': str(e)}), 500
        
        @self.app.route('/api/test', methods=['POST'])
        def api_test():
            """Run comprehensive tests"""
            try:
                data = request.get_json()
                test_type = data.get('type', 'comprehensive')
                intensity = data.get('intensity', 'medium')
                
                # Run tests
                test_results = self.run_comprehensive_tests(test_type, intensity)
                
                return jsonify({
                    'results': test_results,
                    'summary': self.generate_test_summary(test_results),
                    'timestamp': datetime.now().isoformat()
                })
                
            except Exception as e:
                return jsonify({'error': str(e)}), 500
        
        @self.app.route('/api/export', methods=['POST'])
        def api_export():
            """Export results"""
            try:
                data = request.get_json()
                session_id = data.get('session_id')
                format_type = data.get('format', 'json')
                
                if session_id not in self.sessions:
                    return jsonify({'error': 'Invalid session'}), 400
                
                result = self.sessions[session_id]['result']
                
                # Export data
                export_data = self.export_result(result, format_type)
                
                return jsonify(export_data)
                
            except Exception as e:
                return jsonify({'error': str(e)}), 500
        
        @self.app.route('/api/performance')
        def api_performance():
            """Get performance metrics"""
            return jsonify({
                'history': self.performance_history,
                'summary': self.generate_performance_summary(),
                'test_results': self.test_results[-10:]  # Last 10 test results
            })
    
    def create_session(self):
        """Create new session"""
        self.session_counter += 1
        session_id = f"session_{self.session_counter}_{datetime.now().timestamp()}"
        self.sessions[session_id] = {
            'created_at': datetime.now(),
            'result': None,
            'input_data': None
        }
        return session_id
    
    def analyze_result(self, result):
        """Analyze processing result"""
        if not result.success:
            return {'error': 'Processing failed'}
        
        analysis = {
            'geometry_optimization': self.assess_geometry_optimization(result),
            'complexity_handling': self.assess_complexity_handling(result),
            'efficiency_score': self.calculate_efficiency_score(result),
            'accuracy_score': self.calculate_accuracy_score(result)
        }
        
        return analysis
    
    def assess_geometry_optimization(self, result):
        """Assess if the chosen geometry was optimal"""
        # Simplified assessment
        if result.geometry_used == GeometryType.RELATIONAL:
            return {'score': 0.9, 'reason': 'RELATIONAL chosen for complex data'}
        elif result.geometry_used == GeometryType.BANACHIAN:
            return {'score': 0.8, 'reason': 'Banachian optimal for numerical data'}
        else:
            return {'score': 0.7, 'reason': 'Specialized geometry applied'}
    
    def assess_complexity_handling(self, result):
        """Assess complexity handling"""
        processing_time = result.processing_time
        if processing_time < 0.1:
            score = 0.95
        elif processing_time < 0.5:
            score = 0.8
        elif processing_time < 2.0:
            score = 0.6
        else:
            score = 0.4
        
        return {'score': score, 'time': processing_time}
    
    def calculate_efficiency_score(self, result):
        """Calculate efficiency score"""
        time_score = 1.0 / (1.0 + result.processing_time)
        complexity_score = 1.0 - result.processing_time / 10.0  # Normalize
        
        return (time_score + complexity_score) / 2.0
    
    def calculate_accuracy_score(self, result):
        """Calculate accuracy score"""
        # Simplified accuracy based on coordinate count and geometry type
        if not result.sphere:
            return 0.5
        
        coord_count = len(result.sphere.coordinates)
        if coord_count > 10:
            return 0.9
        elif coord_count > 5:
            return 0.8
        else:
            return 0.6
    
    def generate_recommendations(self, result):
        """Generate recommendations based on result"""
        recommendations = []
        
        if result.processing_time > 1.0:
            recommendations.append("Consider data preprocessing for better performance")
        
        if result.geometry_used == GeometryType.BANACHIAN:
            recommendations.append("Banachian geometry suggests structured numerical data")
        
        if result.geometry_used == GeometryType.QUANTUM:
            recommendations.append("Quantum geometry indicates quantum-like properties")
        
        if not result.success:
            recommendations.append("Try simplifying input data or check data format")
        
        return recommendations
    
    def generate_visualization(self, sphere, viz_type):
        """Generate visualization data"""
        if not sphere or not sphere.coordinates:
            return {'error': 'No coordinates to visualize'}
        
        positions = np.array([coord.position for coord in sphere.coordinates])
        
        if viz_type == '3d':
            # 3D visualization
            viz_data = {
                'type': '3d',
                'coordinates': positions.tolist() if positions.ndim <= 3 else positions[:, :3].tolist(),
                'colors': self.generate_color_map(len(sphere.coordinates)),
                'labels': [f"Point {i+1}" for i in range(len(sphere.coordinates))],
                'sphere_properties': sphere.properties.__dict__
            }
        elif viz_type == '2d':
            # 2D projection
            if positions.shape[1] >= 2:
                coords_2d = positions[:, :2].tolist()
            else:
                coords_2d = [[pos[0], 0] for pos in positions]
            
            viz_data = {
                'type': '2d',
                'coordinates': coords_2d,
                'colors': self.generate_color_map(len(sphere.coordinates)),
                'labels': [f"Point {i+1}" for i in range(len(sphere.coordinates))]
            }
        elif viz_type == 'network':
            # Network visualization
            viz_data = {
                'type': 'network',
                'nodes': [{'id': i, 'x': float(pos[0]), 'y': float(pos[1] if len(pos) > 1 else 0)} 
                         for i, pos in enumerate(positions)],
                'edges': self.generate_network_edges(positions),
                'colors': self.generate_color_map(len(sphere.coordinates))
            }
        else:
            viz_data = {'error': 'Unknown visualization type'}
        
        return viz_data
    
    def generate_color_map(self, n_points):
        """Generate color map for points"""
        colors = []
        for i in range(n_points):
            hue = i / max(1, n_points - 1)
            # Convert HSV to RGB (simplified)
            r = abs(hue * 6 - 3) - 1
            g = 2 - abs(hue * 6 - 2)
            b = 2 - abs(hue * 6 - 4)
            colors.append([max(0, min(1, r)), max(0, min(1, g)), max(0, min(1, b))])
        return colors
    
    def generate_network_edges(self, positions):
        """Generate edges for network visualization"""
        edges = []
        threshold = np.mean(np.linalg.norm(positions - np.mean(positions, axis=0), axis=1))
        
        for i, pos1 in enumerate(positions):
            for j, pos2 in enumerate(positions[i+1:], i+1):
                distance = np.linalg.norm(pos1 - pos2)
                if distance < threshold * 1.5:  # Connect nearby points
                    edges.append({'source': i, 'target': j, 'weight': float(distance)})
        
        return edges
    
    def generate_navigation_path(self, sphere, start_idx, end_idx, algorithm):
        """Generate navigation path"""
        try:
            from geometrist.navigation.tyson_navigator import TysonNavigator
            from geometrist.navigation.path_planner import PathPlanner, PlanningAlgorithm
            
            if not sphere or len(sphere.coordinates) < 2:
                return {'error': 'Insufficient coordinates for navigation'}
            
            # Create navigator
            navigator = TysonNavigator(sphere)
            
            # Get start and end coordinates
            start_coord = sphere.coordinates[min(start_idx, len(sphere.coordinates)-1)]
            end_coord = sphere.coordinates[min(end_idx, len(sphere.coordinates)-1)]
            
            # Generate path
            path = navigator.navigate_to(end_coord)
            
            # Prepare response
            path_data = {
                'coordinates': [coord.position.tolist() for coord in path.coordinates],
                'total_distance': path.total_distance,
                'waypoint_count': len(path.coordinates),
                'algorithm': algorithm,
                'start_index': start_idx,
                'end_index': end_idx,
                'path_properties': {
                    'optimization_level': 'high' if len(path.coordinates) < 10 else 'medium',
                    'smoothness': self.calculate_path_smoothness(path)
                }
            }
            
            return path_data
            
        except Exception as e:
            return {'error': f'Navigation failed: {str(e)}'}
    
    def calculate_path_smoothness(self, path):
        """Calculate path smoothness"""
        if len(path.coordinates) < 3:
            return 1.0
        
        total_turn = 0.0
        for i in range(1, len(path.coordinates) - 1):
            v1 = path.coordinates[i].position - path.coordinates[i-1].position
            v2 = path.coordinates[i+1].position - path.coordinates[i].position
            
            if np.linalg.norm(v1) > 0 and np.linalg.norm(v2) > 0:
                cos_angle = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
                cos_angle = np.clip(cos_angle, -1, 1)
                angle = np.arccos(cos_angle)
                total_turn += angle
        
        avg_turn = total_turn / (len(path.coordinates) - 2)
        return max(0.0, 1.0 - avg_turn / np.pi)
    
    def run_comprehensive_tests(self, test_type, intensity):
        """Run comprehensive tests with varied data"""
        test_results = []
        
        # Generate test datasets based on intensity
        if intensity == 'light':
            datasets = self.generate_light_test_datasets()
        elif intensity == 'medium':
            datasets = self.generate_medium_test_datasets()
        elif intensity == 'heavy':
            datasets = self.generate_heavy_test_datasets()
        else:  # extreme
            datasets = self.generate_extreme_test_datasets()
        
        # Run tests on each dataset
        for i, (name, data, expected_properties) in enumerate(datasets):
            print(f"Running test {i+1}/{len(datasets)}: {name}")
            
            try:
                start_time = datetime.now()
                result = self.geometrist.process_quanta(data)
                end_time = datetime.now()
                
                test_result = {
                    'test_name': name,
                    'success': result.success,
                    'processing_time': result.processing_time,
                    'geometry_used': result.geometry_used.name if result.geometry_used else None,
                    'coordinate_count': len(result.sphere.coordinates) if result.sphere else 0,
                    'expected_complexity': expected_properties.get('complexity', 'unknown'),
                    'actual_performance': self.assess_test_performance(result, expected_properties),
                    'anomalies': self.detect_anomalies(result, expected_properties),
                    'timestamp': start_time.isoformat()
                }
                
                test_results.append(test_result)
                
            except Exception as e:
                test_results.append({
                    'test_name': name,
                    'success': False,
                    'error': str(e),
                    'timestamp': datetime.now().isoformat()
                })
        
        # Store test results
        self.test_results.extend(test_results)
        
        return test_results
    
    def generate_light_test_datasets(self):
        """Generate light test datasets"""
        return [
            ("Simple Integers", [1, 2, 3, 4, 5], {'complexity': 'low', 'type': 'numerical'}),
            ("Simple Floats", [1.1, 2.2, 3.3, 4.4, 5.5], {'complexity': 'low', 'type': 'numerical'}),
            ("Short String", "hello world", {'complexity': 'low', 'type': 'textual'}),
            ("Small Dict", {"a": 1, "b": 2}, {'complexity': 'low', 'type': 'structural'}),
        ]
    
    def generate_medium_test_datasets(self):
        """Generate medium test datasets"""
        np.random.seed(42)
        return [
            ("Medium Array", np.random.random(50).tolist(), {'complexity': 'medium', 'type': 'numerical'}),
            ("Sinusoidal Data", np.sin(np.linspace(0, 10, 100)).tolist(), {'complexity': 'medium', 'type': 'periodic'}),
            ("Nested Structure", {"data": list(range(20)), "meta": {"level": 2}}, {'complexity': 'medium', 'type': 'structural'}),
            ("Complex Numbers", [complex(i, i+1) for i in range(10)], {'complexity': 'medium', 'type': 'quantum'}),
        ]
    
    def generate_heavy_test_datasets(self):
        """Generate heavy test datasets"""
        np.random.seed(42)
        return [
            ("Large Array", np.random.random(1000).tolist(), {'complexity': 'high', 'type': 'numerical'}),
            ("2D Matrix", np.random.random((50, 50)).flatten().tolist(), {'complexity': 'high', 'type': 'matrix'}),
            ("Deep Structure", self.generate_deep_structure(5, 10), {'complexity': 'high', 'type': 'hierarchical'}),
            ("Mixed Data Types", self.generate_mixed_data(100), {'complexity': 'high', 'type': 'heterogeneous'}),
        ]
    
    def generate_extreme_test_datasets(self):
        """Generate extreme test datasets with rule-breaking properties"""
        np.random.seed(42)
        return [
            ("Hypercomplex Nested", self.generate_hypercomplex_structure(), {'complexity': 'extreme', 'type': 'hypercomplex'}),
            ("Infinite Regression", self.generate_infinite_regression(10), {'complexity': 'extreme', 'type': 'recursive'}),
            ("Quantum Superposition", self.generate_quantum_superposition(50), {'complexity': 'extreme', 'type': 'quantum'}),
            ("Fractal Data", self.generate_fractal_data(5, 100), {'complexity': 'extreme', 'type': 'fractal'}),
            ("Self-Referential", self.generate_self_referential_data(), {'complexity': 'extreme', 'type': 'paradoxical'}),
        ]
    
    def generate_deep_structure(self, depth, breadth):
        """Generate deeply nested structure"""
        if depth == 0:
            return list(range(breadth))
        return {f"level_{depth}": self.generate_deep_structure(depth-1, breadth)}
    
    def generate_mixed_data(self, size):
        """Generate mixed data types"""
        data = []
        for i in range(size):
            if i % 4 == 0:
                data.append(i)  # Integer
            elif i % 4 == 1:
                data.append(float(i) + 0.5)  # Float
            elif i % 4 == 2:
                data.append(f"item_{i}")  # String
            else:
                data.append({"value": i, "type": "object"})  # Dict
        return data
    
    def generate_hypercomplex_structure(self):
        """Generate hypercomplex structure that breaks normal rules"""
        return {
            "quantum_states": [complex(np.random.random(), np.random.random()) for _ in range(20)],
            "fuzzy_memberships": [np.random.random() for _ in range(20)],
            "recursive_depth": self.generate_deep_structure(8, 5),
            "temporal_layers": [list(np.random.random(10)) for _ in range(5)],
            "meta_properties": {
                "complexity": "infinite",
                "dimensionality": "transfinite",
                "symmetry": "broken",
                "causality": "violated"
            }
        }
    
    def generate_infinite_regression(self, depth):
        """Generate infinite regression structure"""
        if depth == 0:
            return "base"
        return {"contains": self.generate_infinite_regression(depth-1), "level": depth}
    
    def generate_quantum_superposition(self, n_states):
        """Generate quantum superposition states"""
        states = []
        for i in range(n_states):
            amplitude = complex(np.random.random(), np.random.random())
            phase = np.random.random() * 2 * np.pi
            states.append(amplitude * np.exp(1j * phase))
        return states
    
    def generate_fractal_data(self, iterations, points):
        """Generate fractal data pattern"""
        data = []
        x, y = 0, 0
        for _ in range(points):
            data.extend([x, y])
            # Fractal transformation
            r = np.random.random()
            if r < 0.25:
                x, y = 0.5 * x - 0.5 * y, 0.5 * x + 0.5 * y
            elif r < 0.5:
                x, y = -0.5 * x + 0.5 * y, -0.5 * x - 0.5 * y
            elif r < 0.75:
                x, y = 0.5 * x + 0.5 * y, -0.5 * x + 0.5 * y
            else:
                x, y = 0, 0.5 * y
        return data
    
    def generate_self_referential_data(self):
        """Generate self-referential paradoxical data"""
        data = {"this_dict": None}
        data["this_dict"] = data  # Self-reference
        data.update({
            "liar_paradox": "This statement is false",
            "set_paradox": {"contains_itself": None},
            "infinite_loop": lambda: "infinite",
            "quantum_uncertainty": {"position": "unknown", "momentum": "unknown"}
        })
        data["set_paradox"]["contains_itself"] = data["set_paradox"]
        return data
    
    def assess_test_performance(self, result, expected):
        """Assess test performance against expectations"""
        if not result.success:
            return {'score': 0.0, 'assessment': 'failed'}
        
        score = 0.5  # Base score for success
        
        # Check processing time
        if result.processing_time < 0.1:
            score += 0.2
        elif result.processing_time < 1.0:
            score += 0.1
        
        # Check geometry selection
        expected_complexity = expected.get('complexity', 'medium')
        if expected_complexity == 'high' and result.geometry_type == GeometryType.RELATIONAL:
            score += 0.2
        elif expected_complexity == 'medium' and result.geometry_type in [GeometryType.BANACHIAN, GeometryType.QUANTUM]:
            score += 0.2
        elif expected_complexity == 'low' and result.geometry_type in [GeometryType.HADWIGER_NELSON, GeometryType.BANACHIAN]:
            score += 0.2
        
        # Check coordinate count
        if result.sphere and len(result.sphere.coordinates) > 0:
            score += 0.1
        
        return {
            'score': min(1.0, score),
            'assessment': 'excellent' if score > 0.9 else 'good' if score > 0.7 else 'acceptable'
        }
    
    def detect_anomalies(self, result, expected):
        """Detect anomalies in test results"""
        anomalies = []
        
        if not result.success:
            anomalies.append('processing_failed')
        
        if result.processing_time > 5.0:
            anomalies.append('slow_processing')
        
        if result.sphere and len(result.sphere.coordinates) == 0:
            anomalies.append('no_coordinates_generated')
        
        if result.geometry_used == GeometryType.RELATIONAL and expected.get('complexity') == 'low':
            anomalies.append('overkill_geometry')
        
        if result.geometry_used != GeometryType.RELATIONAL and expected.get('complexity') == 'extreme':
            anomalies.append('insufficient_geometry')
        
        return anomalies
    
    def generate_test_summary(self, test_results):
        """Generate test summary"""
        total_tests = len(test_results)
        successful_tests = sum(1 for r in test_results if r.get('success', False))
        
        avg_performance = 0.0
        if successful_tests > 0:
            performances = [r.get('actual_performance', {}).get('score', 0) for r in test_results if r.get('success', False)]
            avg_performance = sum(performances) / len(performances) if performances else 0
        
        geometry_usage = {}
        for result in test_results:
            if result.get('geometry_used'):
                geometry = result['geometry_used']
                geometry_usage[geometry] = geometry_usage.get(geometry, 0) + 1
        
        return {
            'total_tests': total_tests,
            'successful_tests': successful_tests,
            'success_rate': successful_tests / total_tests if total_tests > 0 else 0,
            'average_performance': avg_performance,
            'geometry_usage': geometry_usage,
            'anomaly_count': sum(len(r.get('anomalies', [])) for r in test_results)
        }
    
    def export_result(self, result, format_type):
        """Export result in specified format"""
        if format_type == 'json':
            return self.export_as_json(result)
        elif format_type == 'csv':
            return self.export_as_csv(result)
        elif format_type == 'xml':
            return self.export_as_xml(result)
        else:
            return {'error': 'Unsupported export format'}
    
    def export_as_json(self, result):
        """Export result as JSON"""
        export_data = {
            'timestamp': datetime.now().isoformat(),
            'success': result.success,
            'geometry_used': result.geometry_type.name if result.geometry_type else None,
            'processing_time': result.processing_time,
            'coordinate_count': len(result.sphere.coordinates) if result.sphere else 0,
            'sphere_properties': result.sphere.properties.__dict__ if result.sphere else None,
            'coordinates': [coord.position.tolist() for coord in result.sphere.coordinates] if result.sphere else []
        }
        
        return {
            'format': 'json',
            'data': export_data,
            'filename': f'geometrist_result_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json'
        }
    
    def export_as_csv(self, result):
        """Export result as CSV"""
        if not result.sphere or not result.sphere.coordinates:
            return {'error': 'No coordinates to export'}
        
        csv_lines = ['index,x,y,z,geometry_type']
        for i, coord in enumerate(result.sphere.coordinates):
            pos = coord.position.tolist()
            # Ensure 3D coordinates
            while len(pos) < 3:
                pos.append(0.0)
            csv_lines.append(f"{i},{pos[0]},{pos[1]},{pos[2]},{coord.geometry_type}")
        
        csv_data = '\n'.join(csv_lines)
        
        return {
            'format': 'csv',
            'data': csv_data,
            'filename': f'geometrist_coordinates_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'
        }
    
    def export_as_xml(self, result):
        """Export result as XML"""
        xml_lines = ['<?xml version="1.0" encoding="UTF-8"?>']
        xml_lines.append('<geometrist_result>')
        xml_lines.append(f'  <timestamp>{datetime.now().isoformat()}</timestamp>')
        xml_lines.append(f'  <success>{result.success}</success>')
        xml_lines.append(f'  <geometry_used>{result.geometry_type.name if result.geometry_type else "None"}</geometry_used>')
        xml_lines.append(f'  <processing_time>{result.processing_time}</processing_time>')
        xml_lines.append('  <coordinates>')
        
        if result.sphere:
            for i, coord in enumerate(result.sphere.coordinates):
                xml_lines.append(f'    <coordinate index="{i}">')
                xml_lines.append(f'      <position>{coord.position.tolist()}</position>')
                xml_lines.append(f'      <geometry_type>{coord.geometry_type}</geometry_type>')
                xml_lines.append(f'    </coordinate>')
        
        xml_lines.append('  </coordinates>')
        xml_lines.append('</geometrist_result>')
        
        xml_data = '\n'.join(xml_lines)
        
        return {
            'format': 'xml',
            'data': xml_data,
            'filename': f'geometrist_result_{datetime.now().strftime("%Y%m%d_%H%M%S")}.xml'
        }
    
    def generate_performance_summary(self):
        """Generate performance summary"""
        if not self.performance_history:
            return {'status': 'no_data'}
        
        recent_data = self.performance_history[-100:]  # Last 100 entries
        
        avg_processing_time = sum(r.get('processing_time', 0) for r in recent_data) / len(recent_data)
        success_rate = sum(1 for r in recent_data if r.get('success', False)) / len(recent_data)
        
        return {
            'total_requests': len(self.performance_history),
            'average_processing_time': avg_processing_time,
            'success_rate': success_rate,
            'most_used_geometry': self.get_most_used_geometry(recent_data),
            'peak_performance': max(r.get('efficiency_score', 0) for r in recent_data)
        }
    
    def get_most_used_geometry(self, data):
        """Get most used geometry from performance data"""
        geometry_counts = {}
        for record in data:
            geometry = record.get('geometry_used')
            if geometry:
                geometry_counts[geometry] = geometry_counts.get(geometry, 0) + 1
        
        if geometry_counts:
            return max(geometry_counts.keys(), key=lambda k: geometry_counts[k])
        return None
    
    def run(self):
        """Run the Flask application"""
        print(f"🌐 Starting Geometrist GUI Server...")
        print(f"📍 Access at: http://{self.host}:{self.port}")
        print(f"🎯 Features: Advanced Visualization, Navigation, Testing")
        
        self.app.run(host=self.host, port=self.port, debug=self.debug)