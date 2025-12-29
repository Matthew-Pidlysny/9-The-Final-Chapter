"""
Solver Program - 11 Workshops for Universal Problem Solving
================================================================
A comprehensive problem-solving framework approaching Type V capabilities.
"""

__version__ = "1.0.0"
__author__ = "SuperNinja AI"

# Import all workshops
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from .workshop1_foundations import Workshop1_Foundations
from .workshop2_number_theory import Workshop2_NumberTheory
from .workshop3_algebra import Workshop3_Algebra
from .workshop4_analysis import Workshop4_Analysis
from .workshop5_geometry import Workshop5_Geometry
from .workshop6_11 import Workshop6_Topology, Workshop7_Combinatorics, Workshop8_Probability, Workshop9_Physics, Workshop10_Computational, Workshop11_Advanced

# Export all workshop classes
__all__ = [
    'Workshop1_Foundations',
    'Workshop2_NumberTheory',
    'Workshop3_Algebra',
    'Workshop4_Analysis',
    'Workshop5_Geometry',
    'Workshop6_Topology',
    'Workshop7_Combinatorics',
    'Workshop8_Probability',
    'Workshop9_Physics',
    'Workshop10_Computational',
    'Workshop11_Advanced'
]