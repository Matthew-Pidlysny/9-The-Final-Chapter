"""
GEOMETRIST - Universal Information Sphere System

A comprehensive framework for representing and navigating informational quanta
through optimized geometric structures with Tyson Co-Ordinate navigation.

This system supports 5 core geometries with intelligent selection and dynamic
creation capabilities for handling maximum informational complexity.
"""

__version__ = "1.0.0"
__author__ = "Geometrist Framework Team"

from .core import *
from .geometries import *
from .navigation import *
from .system import *

__all__ = [
    'InformationQuanta',
    'TysonCoordinate', 
    'GeometryEngine',
    'GeometristSystem'
]