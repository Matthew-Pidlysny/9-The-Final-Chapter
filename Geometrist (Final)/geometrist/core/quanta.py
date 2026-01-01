"""
Information Quanta System

Defines the fundamental units of information that can be represented
and processed by the Geometrist system.
"""

from enum import Enum, auto
from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass, field
import numpy as np
import json
from abc import ABC, abstractmethod


class QuantaType(Enum):
    """Types of information quanta based on their fundamental nature"""
    NUMERICAL = auto()      # Pure numerical data
    STRUCTURAL = auto()     # Structured patterns
    TEMPORAL = auto()       # Time-based sequences
    RELATIONAL = auto()     # Relationship-based information
    METAPHORICAL = auto()   # Abstract/metaphorical concepts
    QUANTUM = auto()        # Quantum state information
    HYPERCOMPLEX = auto()   # Beyond standard complexity


@dataclass
class QuantaProperties:
    """Properties that characterize an information quanta"""
    complexity: float = 0.0          # 0.0 to 1.0, information density
    stability: float = 1.0           # 0.0 to 1.0, resistance to change
    coherence: float = 1.0           # 0.0 to 1.0, internal consistency
    dimensionality: int = 1          # Number of dimensions needed
    symmetry: float = 0.0           # 0.0 to 1.0, degree of symmetry
    continuity: float = 1.0          # 0.0 to 1.0, continuous vs discrete
    entropy: float = 0.0            # Information entropy
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def validate(self) -> bool:
        """Validate that properties are within acceptable ranges"""
        return all(0.0 <= val <= 1.0 for val in [
            self.complexity, self.stability, self.coherence, 
            self.symmetry, self.continuity
        ]) and self.dimensionality > 0


class QuantaValidator(ABC):
    """Abstract base class for quanta validation strategies"""
    
    @abstractmethod
    def validate(self, data: Any, properties: QuantaProperties) -> bool:
        """Validate if data matches expected properties"""
        pass


class NumericalValidator(QuantaValidator):
    """Validator for numerical quanta"""
    
    def validate(self, data: Any, properties: QuantaProperties) -> bool:
        if not isinstance(data, (int, float, np.ndarray)):
            return False
        
        if isinstance(data, np.ndarray):
            return data.size > 0 and np.isfinite(data).all()
        
        return np.isfinite(data)


class StructuralValidator(QuantaValidator):
    """Validator for structural quanta"""
    
    def validate(self, data: Any, properties: QuantaProperties) -> bool:
        if isinstance(data, (list, tuple, dict)):
            return len(data) > 0
        return False


@dataclass
class InformationQuanta:
    """
    Fundamental unit of information in the Geometrist system
    
    Each quanta represents a discrete packet of information that can be
    analyzed, transformed, and embedded in geometric structures.
    """
    data: Any
    quanta_type: QuantaType
    properties: QuantaProperties
    id: str = field(default="")
    timestamp: float = field(default=0.0)
    
    def __post_init__(self):
        """Initialize derived properties"""
        if not self.id:
            import time
            self.id = f"quanta_{hash(str(self.data))}_{int(time.time() * 1000)}"
        
        if self.timestamp == 0.0:
            import time
            self.timestamp = time.time()
        
        # Auto-detect properties if not provided
        if self.properties.complexity == 0.0:
            self._analyze_properties()
    
    def _analyze_properties(self):
        """Analyze data to determine properties automatically"""
        data_str = str(self.data)
        data_size = len(data_str)
        
        # Basic complexity estimation based on data characteristics
        if isinstance(self.data, (int, float)):
            self.properties.complexity = 0.1
            self.properties.dimensionality = 1
        elif isinstance(self.data, np.ndarray):
            self.properties.complexity = min(0.8, 0.1 + 0.1 * self.data.ndim)
            self.properties.dimensionality = self.data.ndim
        elif isinstance(self.data, (list, tuple)):
            self.properties.complexity = min(0.7, 0.2 + 0.1 * len(str(self.data)) / 100)
            self.properties.dimensionality = 1
        elif isinstance(self.data, dict):
            self.properties.complexity = min(0.8, 0.3 + 0.1 * len(self.data))
            self.properties.dimensionality = len(self.data)
        else:
            self.properties.complexity = min(0.9, data_size / 1000)
            self.properties.dimensionality = 1
        
        # Calculate entropy (simplified)
        if data_size > 0:
            char_counts = {}
            for char in data_str:
                char_counts[char] = char_counts.get(char, 0) + 1
            
            total = sum(char_counts.values())
            entropy = 0.0
            for count in char_counts.values():
                p = count / total
                if p > 0:
                    entropy -= p * np.log2(p)
            
            self.properties.entropy = min(1.0, entropy / 8.0)  # Normalize to 0-1
    
    def validate(self) -> bool:
        """Validate the quanta's integrity"""
        validators = {
            QuantaType.NUMERICAL: NumericalValidator(),
            QuantaType.STRUCTURAL: StructuralValidator(),
            # Add more validators as needed
        }
        
        validator = validators.get(self.quanta_type)
        if validator:
            return validator.validate(self.data, self.properties)
        
        return self.properties.validate()
    
    def transform(self, transformation: str) -> 'InformationQuanta':
        """Apply a transformation to the quanta"""
        if transformation == "normalize":
            if isinstance(self.data, np.ndarray):
                normalized_data = (self.data - np.mean(self.data)) / (np.std(self.data) + 1e-8)
                return InformationQuanta(
                    data=normalized_data,
                    quanta_type=self.quanta_type,
                    properties=QuantaProperties(
                        complexity=self.properties.complexity * 0.9,
                        stability=self.properties.stability * 1.1,
                        coherence=self.properties.coherence,
                        dimensionality=self.properties.dimensionality
                    )
                )
        
        return self
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert quanta to dictionary representation"""
        return {
            'id': self.id,
            'data': self.data.tolist() if isinstance(self.data, np.ndarray) else self.data,
            'quanta_type': self.quanta_type.name,
            'properties': {
                'complexity': self.properties.complexity,
                'stability': self.properties.stability,
                'coherence': self.properties.coherence,
                'dimensionality': self.properties.dimensionality,
                'symmetry': self.properties.symmetry,
                'continuity': self.properties.continuity,
                'entropy': self.properties.entropy,
                'metadata': self.properties.metadata
            },
            'timestamp': self.timestamp
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'InformationQuanta':
        """Create quanta from dictionary representation"""
        properties = QuantaProperties(
            complexity=data['properties']['complexity'],
            stability=data['properties']['stability'],
            coherence=data['properties']['coherence'],
            dimensionality=data['properties']['dimensionality'],
            symmetry=data['properties']['symmetry'],
            continuity=data['properties']['continuity'],
            entropy=data['properties']['entropy'],
            metadata=data['properties']['metadata']
        )
        
        # Convert numpy arrays back
        quanta_data = data['data']
        if isinstance(quanta_data, list) and properties.dimensionality > 1:
            quanta_data = np.array(quanta_data)
        
        return cls(
            data=quanta_data,
            quanta_type=QuantaType[data['quanta_type']],
            properties=properties,
            id=data['id'],
            timestamp=data['timestamp']
        )
    
    def __str__(self) -> str:
        return f"InformationQuanta({self.quanta_type.name}, complexity={self.properties.complexity:.2f})"
    
    def __repr__(self) -> str:
        return self.__str__()