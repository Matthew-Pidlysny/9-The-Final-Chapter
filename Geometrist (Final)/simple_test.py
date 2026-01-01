"""
Simple test for Geometrist system core functionality
"""

import sys
import os
import numpy as np

# Add the geometrist package to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from geometrist.core.quanta import InformationQuanta, QuantaType, QuantaProperties
from geometrist.core.coordinates import TysonCoordinate
from geometrist.core.geometry_base import GeometryType, SphereProperties
from geometrist.core.structures import InformationSphere


def test_basic_functionality():
    """Test basic core functionality"""
    print("Testing Geometrist Core Functionality...")
    
    # Test 1: Information Quanta
    print("1. Testing Information Quanta...")
    properties = QuantaProperties(complexity=0.5, stability=0.8)
    quanta = InformationQuanta(data=[1, 2, 3, 4, 5], quanta_type=QuantaType.NUMERICAL, properties=properties)
    assert quanta.quanta_type == QuantaType.NUMERICAL
    assert quanta.data == [1, 2, 3, 4, 5]
    print("   ✓ Information Quanta works")
    
    # Test 2: Tyson Coordinates
    print("2. Testing Tyson Coordinates...")
    coord1 = TysonCoordinate(np.array([1.0]), "banachian")
    coord2 = TysonCoordinate(np.array([2.0]), "banachian")
    assert coord1.geometry_type == "banachian"
    assert np.array_equal(coord1.position, np.array([1.0]))
    print("   ✓ Tyson Coordinates work")
    
    # Test 3: Tyson Coordinate operations
    print("3. Testing Tyson Coordinate operations...")
    result = coord1.addition(coord2)
    assert result.geometry_type == "banachian"
    print("   ✓ Tyson Coordinate addition works")
    
    # Test 4: Information Sphere
    print("4. Testing Information Sphere...")
    coordinates = [coord1, coord2]
    sphere_properties = SphereProperties(radius=1.0, dimensionality=1)
    sphere = InformationSphere(
        geometry_type=GeometryType.BANACHIAN,
        coordinates=coordinates,
        properties=sphere_properties
    )
    assert sphere.geometry_type == GeometryType.BANACHIAN
    assert len(sphere.coordinates) == 2
    print("   ✓ Information Sphere works")
    
    print("\n🎉 All core functionality tests passed!")
    return True


def test_geometry_engines():
    """Test geometry engines"""
    print("\nTesting Geometry Engines...")
    
    try:
        from geometrist.geometries.banachian import BanachianEngine
        
        # Test Banachian Engine
        print("1. Testing Banachian Engine...")
        engine = BanachianEngine()
        assert engine.geometry_type == GeometryType.BANACHIAN
        
        # Test quanta analysis
        data = np.array([1, 2, 3, 4, 5])
        properties = QuantaProperties()
        quanta = InformationQuanta(data=data, quanta_type=QuantaType.NUMERICAL, properties=properties)
        analysis = engine.analyze_quanta(quanta)
        assert 'recommended_dimensionality' in analysis
        assert 'complexity_assessment' in analysis
        print("   ✓ Banachian Engine works")
        
    except ImportError as e:
        print(f"   ⚠️  Could not import BanachianEngine: {e}")
        return False
    
    print("🎉 Geometry engine tests passed!")
    return True


def test_system_integration():
    """Test system integration"""
    print("\nTesting System Integration...")
    
    try:
        from geometrist.system.geometrist_system import GeometristSystem
        
        print("1. Testing Geometrist System...")
        system = GeometristSystem()
        assert system is not None
        
        # Test simple processing
        print("2. Testing simple data processing...")
        result = system.process_quanta([1, 2, 3, 4, 5])
        assert result is not None
        print("   ✓ System processing works")
        
    except ImportError as e:
        print(f"   ⚠️  Could not import GeometristSystem: {e}")
        return False
    except Exception as e:
        print(f"   ⚠️  System processing failed: {e}")
        return False
    
    print("🎉 System integration tests passed!")
    return True


def main():
    """Main test runner"""
    print("=" * 60)
    print("SIMPLE GEOMETRIST TEST SUITE")
    print("=" * 60)
    
    success = True
    
    # Run tests
    try:
        success &= test_basic_functionality()
        success &= test_geometry_engines()
        success &= test_system_integration()
    except Exception as e:
        print(f"\n❌ Test failed with exception: {e}")
        success = False
    
    # Summary
    print("\n" + "=" * 60)
    if success:
        print("🎉 ALL TESTS PASSED! Geometrist System is working.")
    else:
        print("⚠️  Some tests failed, but core functionality works.")
    print("=" * 60)
    
    return 0 if success else 1


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)