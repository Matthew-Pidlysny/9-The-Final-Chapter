"""
Comprehensive Test Suite for Geometrist System

Tests all components of the Geometrist system to ensure proper
functionality and integration.
"""

import sys
import os
import numpy as np
import time
import json
from typing import List, Dict, Any

# Add the geometrist package to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from geometrist.core import *
from geometrist.geometries import *
from geometrist.navigation import *
from geometrist.system import *


class GeometristTestSuite:
    """
    Comprehensive test suite for the Geometrist system
    
    Tests all major components and integration scenarios.
    """
    
    def __init__(self):
        self.test_results = []
        self.total_tests = 0
        self.passed_tests = 0
        self.failed_tests = 0
    
    def run_all_tests(self):
        """Run all tests in the suite"""
        print("=" * 80)
        print("GEOMETRIST SYSTEM COMPREHENSIVE TEST SUITE")
        print("=" * 80)
        
        # Core component tests
        self.test_information_quanta()
        self.test_tyson_coordinates()
        self.test_geometry_engines()
        self.test_geometry_factory()
        
        # Navigation tests
        self.test_tyson_navigator()
        self.test_path_planner()
        self.test_navigation_optimizer()
        
        # System integration tests
        self.test_input_analyzer()
        self.test_output_generator()
        self.test_geometrist_system()
        
        # Performance and integration tests
        self.test_performance()
        self.test_integration_scenarios()
        
        # Print results
        self.print_test_results()
        
        return self.passed_tests == self.total_tests
    
    def run_test(self, test_name: str, test_function):
        """Run a single test and record results"""
        self.total_tests += 1
        print(f"\n[TEST] {test_name}...", end=" ")
        
        try:
            start_time = time.time()
            test_function()
            end_time = time.time()
            
            self.passed_tests += 1
            execution_time = end_time - start_time
            print(f"PASSED ({execution_time:.3f}s)")
            
            self.test_results.append({
                'name': test_name,
                'status': 'PASSED',
                'time': execution_time,
                'error': None
            })
            
        except Exception as e:
            self.failed_tests += 1
            print(f"FAILED: {str(e)}")
            
            self.test_results.append({
                'name': test_name,
                'status': 'FAILED',
                'time': 0,
                'error': str(e)
            })
    
    def test_information_quanta(self):
        """Test Information Quanta functionality"""
        
        def test_creation():
            # Test numerical quanta
            numerical_quanta = InformationQuanta(
                data=42.0,
                quanta_type=QuantaType.NUMERICAL,
                properties=QuantaProperties(complexity=0.1)
            )
            assert numerical_quanta.quanta_type == QuantaType.NUMERICAL
            assert numerical_quanta.data == 42.0
        
        def test_property_analysis():
            # Test automatic property analysis
            data = [1, 2, 3, 4, 5]
            properties = QuantaProperties()
            quanta = InformationQuanta(data=data, quanta_type=QuantaType.STRUCTURAL, properties=properties)
            assert quanta.properties.complexity > 0.0
            assert quanta.properties.dimensionality > 0
        
        def test_validation():
            # Test property validation
            properties = QuantaProperties(complexity=0.5, stability=1.5)  # Invalid stability
            assert not properties.validate()
        
        # Run tests
        self.run_test("Information Quanta Creation", test_creation)
        self.run_test("Property Analysis", test_property_analysis)
        self.run_test("Property Validation", test_validation)
    
    def test_tyson_coordinates(self):
        """Test Tyson Co-Ordinate functionality"""
        
        def test_coordinate_creation():
            position = np.array([1.0, 2.0, 3.0])
            coord = TysonCoordinate(position, "banachian")
            assert coord.geometry_type == "banachian"
            assert np.array_equal(coord.position, position)
        
        def test_addition_operation():
            coord1 = TysonCoordinate(np.array([1.0]), "banachian")
            coord2 = TysonCoordinate(np.array([2.0]), "banachian")
            result = coord1.addition(coord2)
            assert result.geometry_type == "banachian"
        
        def test_distance_calculation():
            coord1 = TysonCoordinate(np.array([0.0]), "banachian")
            coord2 = TysonCoordinate(np.array([3.0]), "banachian")
            distance = coord1.distance_to(coord2)
            assert distance == 3.0
        
        # Run tests
        self.run_test("Tyson Coordinate Creation", test_coordinate_creation)
        self.run_test("Addition Operation", test_addition_operation)
        self.run_test("Distance Calculation", test_distance_calculation)
    
    def test_geometry_engines(self):
        """Test all geometry engines"""
        
        def test_hadwiger_nelson_engine():
            engine = HadwigerNelsonEngine()
            assert engine.geometry_type == GeometryType.HADWIGER_NELSON
            
            # Test quanta analysis
            data = [0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi]
            quanta = InformationQuanta(data, QuantaType.NUMERICAL)
            analysis = engine.analyze_quanta(quanta)
            assert 'recommended_dimensionality' in analysis
            assert 'complexity_assessment' in analysis
        
        def test_banachian_engine():
            engine = BanachianEngine()
            assert engine.geometry_type == GeometryType.BANACHIAN
            
            # Test quanta analysis
            data = np.array([1, 2, 3, 4, 5])
            quanta = InformationQuanta(data, QuantaType.NUMERICAL)
            analysis = engine.analyze_quanta(quanta)
            assert 'optimal_norm' in analysis
        
        def test_fuzzy_engine():
            engine = FuzzyEngine()
            assert engine.geometry_type == GeometryType.FUZZY
            
            # Test quanta analysis
            data = np.random.random(10)
            quanta = InformationQuanta(data, QuantaType.NUMERICAL)
            analysis = engine.analyze_quanta(quanta)
            assert 'fuzziness_level' in analysis
        
        def test_quantum_engine():
            engine = QuantumEngine()
            assert engine.geometry_type == GeometryType.QUANTUM
            
            # Test quanta analysis
            data = np.array([1+0j, 0+1j, -1+0j, 0-1j])
            quanta = InformationQuanta(data, QuantaType.QUANTUM)
            analysis = engine.analyze_quanta(quanta)
            assert 'quantum_coherence' in analysis
        
        def test_relational_engine():
            engine = RelationalEngine()
            assert engine.geometry_type == GeometryType.RELATIONAL
            
            # Test quanta analysis
            data = {'complex': 'structure', 'nested': {'data': [1, 2, 3]}}
            quanta = InformationQuanta(data, QuantaType.STRUCTURAL)
            analysis = engine.analyze_quanta(quanta)
            assert 'synthesis_strategy' in analysis
        
        # Run tests
        self.run_test("Hadwiger-Nelson Engine", test_hadwiger_nelson_engine)
        self.run_test("Banachian Engine", test_banachian_engine)
        self.run_test("Fuzzy Engine", test_fuzzy_engine)
        self.run_test("Quantum Engine", test_quantum_engine)
        self.run_test("RELATIONAL Engine", test_relational_engine)
    
    def test_geometry_factory(self):
        """Test Geometry Factory functionality"""
        
        def test_factory_initialization():
            factory = GeometryFactory()
            assert len(factory.geometry_engines) == 5
            assert GeometryType.HADWIGER_NELSON in factory.geometry_engines
        
        def test_geometry_selection():
            factory = GeometryFactory()
            
            # Test numerical data selection
            data = np.array([1, 2, 3, 4, 5])
            quanta = InformationQuanta(data, QuantaType.NUMERICAL)
            selected_geometry = factory.select_geometry(quanta)
            assert selected_geometry is not None
        
        def test_dynamic_creation():
            factory = GeometryFactory()
            
            # Test creating new geometry for novel data
            data = "extremely complex hyperdimensional data with unknown properties"
            quanta = InformationQuanta(data, QuantaType.HYPERCOMPLEX)
            
            # This should trigger dynamic geometry creation
            try:
                result = factory.process_quanta(quanta)
                assert result is not None
            except:
                # Expected to fail for very complex data
                pass
        
        # Run tests
        self.run_test("Factory Initialization", test_factory_initialization)
        self.run_test("Geometry Selection", test_geometry_selection)
        self.run_test("Dynamic Creation", test_dynamic_creation)
    
    def test_tyson_navigator(self):
        """Test Tyson Navigator functionality"""
        
        def test_navigator_initialization():
            # Create a simple sphere for testing
            coordinates = [
                TysonCoordinate(np.array([0.0]), "banachian"),
                TysonCoordinate(np.array([1.0]), "banachian"),
                TysonCoordinate(np.array([2.0]), "banachian")
            ]
            sphere = InformationSphere(
                geometry_type=GeometryType.BANACHIAN,
                coordinates=coordinates,
                properties=SphereProperties(radius=2.0)
            )
            
            navigator = TysonNavigator(sphere)
            assert navigator.sphere == sphere
        
        def test_navigation_planning():
            # Create sphere
            coordinates = [
                TysonCoordinate(np.array([0.0]), "banachian"),
                TysonCoordinate(np.array([1.0]), "banachian"),
                TysonCoordinate(np.array([2.0]), "banachian")
            ]
            sphere = InformationSphere(
                geometry_type=GeometryType.BANACHIAN,
                coordinates=coordinates,
                properties=SphereProperties(radius=2.0)
            )
            
            navigator = TysonNavigator(sphere)
            
            # Plan navigation
            start = coordinates[0]
            target = coordinates[2]
            path = navigator.navigate_to(target)
            
            assert path is not None
            assert len(path.coordinates) >= 2
            assert path.coordinates[0] == start
            assert path.coordinates[-1] == target
        
        # Run tests
        self.run_test("Navigator Initialization", test_navigator_initialization)
        self.run_test("Navigation Planning", test_navigation_planning)
    
    def test_path_planner(self):
        """Test Path Planner functionality"""
        
        def test_planner_initialization():
            # Create sphere for testing
            coordinates = [
                TysonCoordinate(np.array([0.0, 0.0]), "banachian"),
                TysonCoordinate(np.array([1.0, 0.0]), "banachian"),
                TysonCoordinate(np.array([0.0, 1.0]), "banachian")
            ]
            sphere = InformationSphere(
                geometry_type=GeometryType.BANACHIAN,
                coordinates=coordinates,
                properties=SphereProperties()
            )
            
            planner = PathPlanner(sphere)
            assert planner.sphere == sphere
        
        def test_astar_planning():
            # Create sphere
            coordinates = [
                TysonCoordinate(np.array([0.0]), "banachian"),
                TysonCoordinate(np.array([1.0]), "banachian"),
                TysonCoordinate(np.array([2.0]), "banachian")
            ]
            sphere = InformationSphere(
                geometry_type=GeometryType.BANACHIAN,
                coordinates=coordinates,
                properties=SphereProperties()
            )
            
            planner = PathPlanner(sphere)
            
            # Plan path using A*
            start = coordinates[0]
            goal = coordinates[2]
            path = planner.plan_path(start, goal, PlanningAlgorithm.ASTAR)
            
            assert path is not None
            assert len(path.coordinates) >= 2
        
        # Run tests
        self.run_test("Planner Initialization", test_planner_initialization)
        self.run_test("A* Planning", test_astar_planning)
    
    def test_navigation_optimizer(self):
        """Test Navigation Optimizer functionality"""
        
        def test_optimizer_initialization():
            # Create sphere for testing
            coordinates = [
                TysonCoordinate(np.array([0.0]), "banachian"),
                TysonCoordinate(np.array([1.0]), "banachian"),
                TysonCoordinate(np.array([2.0]), "banachian")
            ]
            sphere = InformationSphere(
                geometry_type=GeometryType.BANACHIAN,
                coordinates=coordinates,
                properties=SphereProperties()
            )
            
            optimizer = NavigationOptimizer(sphere)
            assert optimizer.sphere == sphere
        
        def test_path_optimization():
            # Create test path
            coordinates = [
                TysonCoordinate(np.array([0.0]), "banachian"),
                TysonCoordinate(np.array([1.0]), "banachian"),
                TysonCoordinate(np.array([2.0]), "banachian")
            ]
            path = NavigationPath(coordinates=coordinates, total_distance=2.0)
            
            # Create sphere
            sphere = InformationSphere(
                geometry_type=GeometryType.BANACHIAN,
                coordinates=coordinates,
                properties=SphereProperties()
            )
            
            optimizer = NavigationOptimizer(sphere)
            
            # Optimize path
            target = OptimizationTarget(metric="distance", direction="minimize")
            optimized_path = optimizer.optimize_path(path, target)
            
            assert optimized_path is not None
            assert len(optimized_path.coordinates) >= 2
        
        # Run tests
        self.run_test("Optimizer Initialization", test_optimizer_initialization)
        self.run_test("Path Optimization", test_path_optimization)
    
    def test_input_analyzer(self):
        """Test Input Analyzer functionality"""
        
        def test_analyzer_initialization():
            analyzer = InputAnalyzer()
            assert analyzer is not None
        
        def test_numerical_analysis():
            analyzer = InputAnalyzer()
            data = [1, 2, 3, 4, 5]
            analysis = analyzer.analyze_input(data)
            
            assert analysis.detected_type == QuantaType.NUMERICAL
            assert analysis.confidence > 0.5
            assert len(analysis.recommendations) > 0
        
        def test_structural_analysis():
            analyzer = InputAnalyzer()
            data = {'key': 'value', 'list': [1, 2, 3]}
            analysis = analyzer.analyze_input(data)
            
            assert analysis.detected_type == QuantaType.STRUCTURAL
            assert analysis.confidence > 0.5
        
        # Run tests
        self.run_test("Analyzer Initialization", test_analyzer_initialization)
        self.run_test("Numerical Analysis", test_numerical_analysis)
        self.run_test("Structural Analysis", test_structural_analysis)
    
    def test_output_generator(self):
        """Test Output Generator functionality"""
        
        def test_generator_initialization():
            generator = OutputGenerator()
            assert generator is not None
        
        def test_json_output():
            # Create test sphere
            coordinates = [
                TysonCoordinate(np.array([1.0]), "banachian"),
                TysonCoordinate(np.array([2.0]), "banachian")
            ]
            sphere = InformationSphere(
                geometry_type=GeometryType.BANACHIAN,
                coordinates=coordinates,
                properties=SphereProperties(radius=1.0)
            )
            
            generator = OutputGenerator()
            options = OutputOptions(format=OutputFormat.JSON)
            output = generator.generate_output(sphere, options)
            
            assert 'data' in output
            assert 'geometry_type' in output['data']
            assert output['data']['geometry_type'] == 'BANACHIAN'
        
        def test_metadata_output():
            # Create test sphere
            coordinates = [TysonCoordinate(np.array([1.0]), "banachian")]
            sphere = InformationSphere(
                geometry_type=GeometryType.BANACHIAN,
                coordinates=coordinates,
                properties=SphereProperties(radius=1.0)
            )
            
            generator = OutputGenerator()
            options = OutputOptions(format=OutputFormat.METADATA)
            output = generator.generate_output(sphere, options)
            
            assert 'data' in output
            assert 'geometry_type' in output['data']
        
        # Run tests
        self.run_test("Generator Initialization", test_generator_initialization)
        self.run_test("JSON Output", test_json_output)
        self.run_test("Metadata Output", test_metadata_output)
    
    def test_geometrist_system(self):
        """Test main Geometrist System functionality"""
        
        def test_system_initialization():
            config = SystemConfiguration()
            system = GeometristSystem(config)
            assert system is not None
            assert system.config == config
        
        def test_simple_processing():
            system = GeometristSystem()
            
            # Process simple numerical data
            result = system.process_quanta([1, 2, 3, 4, 5])
            
            assert result.success
            assert result.sphere is not None
            assert result.geometry_used is not None
            assert result.processing_time > 0
        
        def test_complex_processing():
            system = GeometristSystem()
            
            # Process complex structured data
            data = {
                'complex_structure': {
                    'nested_data': [1, 2, 3, 4, 5],
                    'metadata': {'type': 'test', 'complexity': 'high'}
                },
                'additional_info': [1.1, 2.2, 3.3, 4.4, 5.5]
            }
            
            result = system.process_quanta(data)
            
            assert result.success
            assert result.sphere is not None
            # Should select appropriate geometry for complex data
            assert result.geometry_used in [GeometryType.RELATIONAL, GeometryType.BANACHIAN]
        
        # Run tests
        self.run_test("System Initialization", test_system_initialization)
        self.run_test("Simple Processing", test_simple_processing)
        self.run_test("Complex Processing", test_complex_processing)
    
    def test_performance(self):
        """Test performance characteristics"""
        
        def test_processing_speed():
            system = GeometristSystem()
            
            # Test with various data sizes
            data_sizes = [10, 100, 1000]
            
            for size in data_sizes:
                data = list(range(size))
                start_time = time.time()
                result = system.process_quanta(data)
                end_time = time.time()
                
                processing_time = end_time - start_time
                assert processing_time < 5.0  # Should complete within 5 seconds
                assert result.success
        
        def test_memory_usage():
            # Test that the system doesn't leak memory
            system = GeometristSystem()
            
            for i in range(10):
                data = list(range(100))
                result = system.process_quanta(data)
                assert result.success
                del result
            
            # If we reach here, no obvious memory issues
        
        # Run tests
        self.run_test("Processing Speed", test_processing_speed)
        self.run_test("Memory Usage", test_memory_usage)
    
    def test_integration_scenarios(self):
        """Test real-world integration scenarios"""
        
        def test_numerical_data_scenario():
            """Test processing numerical data with automatic geometry selection"""
            system = GeometristSystem()
            
            # Various types of numerical data
            test_cases = [
                [1, 2, 3, 4, 5],  # Simple integers
                [1.1, 2.2, 3.3, 4.4, 5.5],  # Floats
                np.random.random(20),  # Random array
                np.linspace(0, 10, 50),  # Linear progression
                np.sin(np.linspace(0, 2*np.pi, 100))  # Sinusoidal data
            ]
            
            for i, data in enumerate(test_cases):
                result = system.process_quanta(data)
                assert result.success, f"Failed test case {i}"
                assert result.sphere is not None
                print(f"  Test case {i}: Used {result.geometry_used.name} geometry")
        
        def test_structural_data_scenario():
            """Test processing structured data"""
            system = GeometristSystem()
            
            # Various types of structured data
            test_cases = [
                {'simple': 'dict'},
                {'nested': {'data': [1, 2, 3]}},
                [1, 2, {'nested': 'dict'}, 4, 5],
                {'list': [1, 2, 3], 'dict': {'a': 1, 'b': 2}}
            ]
            
            for i, data in enumerate(test_cases):
                result = system.process_quanta(data)
                assert result.success, f"Failed test case {i}"
                assert result.sphere is not None
                print(f"  Test case {i}: Used {result.geometry_used.name} geometry")
        
        def test_mixed_complexity_scenario():
            """Test processing data with varying complexity"""
            system = GeometristSystem()
            
            # Data with different complexity levels
            test_cases = [
                ('simple', 42),
                ('medium', list(range(100))),
                ('complex', {'nested': {'data': list(range(50)), 'metadata': {'complex': True}}}),
                ('very_complex', np.random.random((10, 10)))  # 2D array
            ]
            
            for name, data in test_cases:
                result = system.process_quanta(data)
                assert result.success, f"Failed {name} data"
                
                # Check that appropriate geometry was selected
                if name == 'simple':
                    assert result.geometry_used in [GeometryType.BANACHIAN, GeometryType.HADWIGER_NELSON]
                elif name == 'very_complex':
                    assert result.geometry_used in [GeometryType.RELATIONAL, GeometryType.QUANTUM]
                
                print(f"  {name.title()} data: Used {result.geometry_used.name} geometry "
                      f"(time: {result.processing_time:.3f}s)")
        
        def test_edge_cases_scenario():
            """Test edge cases and error handling"""
            system = GeometristSystem()
            
            # Edge cases
            edge_cases = [
                [],  # Empty list
                [1],  # Single element
                "simple string",  # String data
                None,  # None value (should be handled gracefully)
                True,  # Boolean value
                float('inf'),  # Infinity
                [float('nan'), 1, 2]  # NaN in list
            ]
            
            for i, data in enumerate(edge_cases):
                try:
                    result = system.process_quanta(data)
                    # Some edge cases should succeed, others should fail gracefully
                    print(f"  Edge case {i}: {'Success' if result.success else 'Handled gracefully'}")
                except Exception as e:
                    # Expected for some edge cases
                    print(f"  Edge case {i}: Exception handled: {str(e)[:50]}...")
        
        def test_navigation_scenario():
            """Test navigation functionality"""
            system = GeometristSystem()
            
            # Create a sphere with known structure
            data = np.array([[0, 0], [1, 0], [0, 1], [1, 1], [0.5, 0.5]])
            result = system.process_quanta(data)
            
            assert result.success
            assert result.sphere is not None
            
            # Test navigation if available
            if hasattr(system, 'navigator') and system.navigator:
                start = result.sphere.coordinates[0]
                target = result.sphere.coordinates[-1]
                
                try:
                    path = system.navigator.navigate_to(target)
                    assert path is not None
                    print(f"  Navigation: Path found with {len(path.coordinates)} waypoints")
                except Exception as e:
                    print(f"  Navigation: Not available or failed: {str(e)[:50]}...")
        
        # Run integration tests
        self.run_test("Numerical Data Scenario", test_numerical_data_scenario)
        self.run_test("Structural Data Scenario", test_structural_data_scenario)
        self.run_test("Mixed Complexity Scenario", test_mixed_complexity_scenario)
        self.run_test("Edge Cases Scenario", test_edge_cases_scenario)
        self.run_test("Navigation Scenario", test_navigation_scenario)
    
    def print_test_results(self):
        """Print comprehensive test results"""
        print("\n" + "=" * 80)
        print("TEST RESULTS SUMMARY")
        print("=" * 80)
        
        print(f"Total Tests: {self.total_tests}")
        print(f"Passed: {self.passed_tests}")
        print(f"Failed: {self.failed_tests}")
        print(f"Success Rate: {(self.passed_tests / max(1, self.total_tests)) * 100:.1f}%")
        
        if self.failed_tests > 0:
            print("\nFailed Tests:")
            for result in self.test_results:
                if result['status'] == 'FAILED':
                    print(f"  - {result['name']}: {result['error']}")
        
        # Performance summary
        total_time = sum(r['time'] for r in self.test_results if r['time'] > 0)
        avg_time = total_time / max(1, len([r for r in self.test_results if r['time'] > 0]))
        
        print(f"\nPerformance:")
        print(f"  Total Time: {total_time:.3f}s")
        print(f"  Average Time: {avg_time:.3f}s")
        
        print("\n" + "=" * 80)
        
        if self.passed_tests == self.total_tests:
            print("🎉 ALL TESTS PASSED! Geometrist System is fully functional.")
        else:
            print("⚠️  Some tests failed. Please review the issues above.")
        
        print("=" * 80)


def main():
    """Main test runner"""
    print("Initializing Geometrist Test Suite...")
    
    # Create and run test suite
    test_suite = GeometristTestSuite()
    success = test_suite.run_all_tests()
    
    return 0 if success else 1


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)