"""
Geometry Engine Implementations

Five specialized geometry engines for different types of information representation:
- Hadwiger-Nelson: Trigonometric polynomials with forbidden angles
- Banachian: Complete normed vector space
- Fuzzy: Quantum angular momentum states  
- Quantum (Podleś): q-deformed classical sphere
- RELATIONAL: Meta-sphere synthesizing all four
"""

from .hadwiger_nelson import HadwigerNelsonEngine
from .banachian import BanachianEngine
from .fuzzy import FuzzyEngine
from .quantum import QuantumEngine
from .relational import RelationalEngine
from .geometry_factory import GeometryFactory

__all__ = [
    'HadwigerNelsonEngine',
    'BanachianEngine', 
    'FuzzyEngine',
    'QuantumEngine',
    'RelationalEngine',
    'GeometryFactory'
]