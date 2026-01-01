"""
Input Analyzer

Analyzes input data to determine optimal processing parameters
and detect data characteristics for the Geometrist system.
"""

import numpy as np
from typing import Any, Dict, List, Optional, Union, Tuple
from dataclasses import dataclass
import json
import math

from ..core.quanta import InformationQuanta, QuantaType, QuantaProperties


@dataclass
class InputAnalysis:
    """Results of input analysis"""
    detected_type: QuantaType
    properties: QuantaProperties
    confidence: float
    recommendations: List[str]
    warnings: List[str]


class InputAnalyzer:
    """
    Analyzes input data to determine optimal processing parameters
    
    Features:
    - Automatic quanta type detection
    - Property estimation
    - Complexity assessment
    - Processing recommendations
    """
    
    def __init__(self):
        # Type detection patterns
        self.type_patterns = {
            QuantaType.NUMERICAL: self._is_numerical,
            QuantaType.STRUCTURAL: self._is_structural,
            QuantaType.TEMPORAL: self._is_temporal,
            QuantaType.RELATIONAL: self._is_relational,
            QuantaType.METAPHORICAL: self._is_metaphorical,
            QuantaType.QUANTUM: self._is_quantum,
            QuantaType.HYPERCOMPLEX: self._is_hypercomplex
        }
        
        # Analysis statistics
        self.analysis_history = []
    
    def analyze_input(self, data: Any) -> InputAnalysis:
        """
        Comprehensive analysis of input data
        
        Returns type detection, properties, and recommendations.
        """
        # Detect quanta type
        detected_type, confidence = self.detect_quanta_type_with_confidence(data)
        
        # Estimate properties
        properties = self.estimate_properties(data, detected_type)
        
        # Generate recommendations
        recommendations = self.generate_recommendations(data, detected_type, properties)
        
        # Generate warnings
        warnings = self.generate_warnings(data, detected_type, properties)
        
        analysis = InputAnalysis(
            detected_type=detected_type,
            properties=properties,
            confidence=confidence,
            recommendations=recommendations,
            warnings=warnings
        )
        
        # Record analysis
        self.analysis_history.append(analysis)
        
        return analysis
    
    def detect_quanta_type(self, data: Any) -> QuantaType:
        """Detect the most appropriate quanta type for the data"""
        detected_type, _ = self.detect_quanta_type_with_confidence(data)
        return detected_type
    
    def detect_quanta_type_with_confidence(self, data: Any) -> Tuple[QuantaType, float]:
        """Detect quanta type with confidence score"""
        type_scores = {}
        
        # Score each type
        for quanta_type, detector in self.type_patterns.items():
            score = detector(data)
            type_scores[quanta_type] = score
        
        # Find best match
        best_type = max(type_scores.keys(), key=lambda k: type_scores[k])
        best_score = type_scores[best_type]
        
        # Normalize confidence
        max_possible_score = max(type_scores.values())
        confidence = best_score / max_possible_score if max_possible_score > 0 else 0.5
        
        return best_type, confidence
    
    def estimate_properties(self, data: Any, quanta_type: QuantaType) -> QuantaProperties:
        """Estimate quanta properties from data"""
        properties = QuantaProperties()
        
        # Base complexity calculation
        properties.complexity = self._calculate_complexity(data)
        
        # Type-specific property estimation
        if quanta_type == QuantaType.NUMERICAL:
            properties = self._estimate_numerical_properties(data, properties)
        elif quanta_type == QuantaType.STRUCTURAL:
            properties = self._estimate_structural_properties(data, properties)
        elif quanta_type == QuantaType.TEMPORAL:
            properties = self._estimate_temporal_properties(data, properties)
        elif quanta_type == QuantaType.RELATIONAL:
            properties = self._estimate_relational_properties(data, properties)
        elif quanta_type == QuantaType.QUANTUM:
            properties = self._estimate_quantum_properties(data, properties)
        
        # General property calculations
        properties.dimensionality = self._estimate_dimensionality(data)
        properties.entropy = self._calculate_entropy(data)
        properties.stability = self._estimate_stability(data)
        properties.coherence = self._estimate_coherence(data)
        
        return properties
    
    def generate_recommendations(self, data: Any, quanta_type: QuantaType, 
                                properties: QuantaProperties) -> List[str]:
        """Generate processing recommendations based on analysis"""
        recommendations = []
        
        # Complexity-based recommendations
        if properties.complexity < 0.3:
            recommendations.append("Low complexity - consider efficiency-focused geometries")
        elif properties.complexity > 0.8:
            recommendations.append("High complexity - consider RELATIONAL or QUANTUM geometries")
        
        # Type-based recommendations
        if quanta_type == QuantaType.NUMERICAL:
            recommendations.append("Numerical data - Banachian or Quantum geometries recommended")
        elif quanta_type == QuantaType.STRUCTURAL:
            recommendations.append("Structural data - Hadwiger-Nelson or RELATIONAL geometries")
        elif quanta_type == QuantaType.TEMPORAL:
            recommendations.append("Temporal data - consider time-aware processing")
        elif quanta_type == QuantaType.RELATIONAL:
            recommendations.append("Relational data - RELATIONAL geometry highly recommended")
        elif quanta_type == QuantaType.QUANTUM:
            recommendations.append("Quantum data - Quantum geometry essential")
        
        # Dimensionality recommendations
        if properties.dimensionality > 5:
            recommendations.append("High dimensionality - consider dimensionality reduction")
        
        # Entropy-based recommendations
        if properties.entropy > 0.7:
            recommendations.append("High entropy - consider Fuzzy or Quantum geometries")
        
        # Stability recommendations
        if properties.stability < 0.3:
            recommendations.append("Low stability - consider adaptive optimization")
        
        return recommendations
    
    def generate_warnings(self, data: Any, quanta_type: QuantaType, 
                         properties: QuantaProperties) -> List[str]:
        """Generate warnings about potential processing issues"""
        warnings = []
        
        # Data size warnings
        if isinstance(data, (list, tuple, np.ndarray)):
            if len(data) > 10000:
                warnings.append("Large dataset - processing may be slow")
            elif len(data) < 3:
                warnings.append("Very small dataset - results may be unreliable")
        
        # Complexity warnings
        if properties.complexity > 0.95:
            warnings.append("Extreme complexity - may require specialized handling")
        
        # Type-specific warnings
        if quanta_type == QuantaType.QUANTUM and not self._has_quantum_properties(data):
            warnings.append("Data may not have true quantum properties")
        
        # Missing data warnings
        if self._has_missing_data(data):
            warnings.append("Data contains missing or null values")
        
        # Dimensionality warnings
        if properties.dimensionality > 10:
            warnings.append("Very high dimensionality - may cause computational issues")
        
        return warnings
    
    # Type detection methods
    def _is_numerical(self, data: Any) -> float:
        """Check if data is primarily numerical"""
        if isinstance(data, (int, float, complex)):
            return 1.0
        elif isinstance(data, np.ndarray):
            if np.issubdtype(data.dtype, np.number):
                return 0.9
            return 0.1
        elif isinstance(data, (list, tuple)):
            if all(isinstance(x, (int, float, complex)) for x in data):
                return 0.8
            elif sum(isinstance(x, (int, float, complex)) for x in data) / len(data) > 0.7:
                return 0.6
            return 0.2
        elif isinstance(data, str):
            # Try to parse as number
            try:
                float(data)
                return 0.3
            except:
                return 0.0
        return 0.0
    
    def _is_structural(self, data: Any) -> float:
        """Check if data has structural properties"""
        if isinstance(data, (list, tuple, dict)):
            return 0.8
        elif isinstance(data, str):
            # Check for structured patterns (JSON, XML, etc.)
            if data.startswith(('{', '[', '<')):
                return 0.6
            return 0.2
        elif isinstance(data, np.ndarray):
            if data.ndim > 1:
                return 0.7
            return 0.3
        return 0.1
    
    def _is_temporal(self, data: Any) -> float:
        """Check if data has temporal properties"""
        if isinstance(data, (list, tuple, np.ndarray)):
            # Check for time-like patterns
            if len(data) > 2:
                # Look for sequential patterns
                sequential_score = 0.0
                for i in range(len(data) - 1):
                    if isinstance(data[i], (int, float)) and isinstance(data[i+1], (int, float)):
                        # Check if roughly sequential
                        if abs(data[i+1] - data[i]) < 100:  # Reasonable time step
                            sequential_score += 1.0
                
                return min(1.0, sequential_score / max(1, len(data) - 1))
        
        # Check for timestamp strings
        if isinstance(data, str):
            import re
            timestamp_patterns = [
                r'\d{4}-\d{2}-\d{2}',  # Date format
                r'\d{2}:\d{2}:\d{2}',   # Time format
                r'T\d{2}:\d{2}:\d{2}'   # ISO format time
            ]
            
            for pattern in timestamp_patterns:
                if re.search(pattern, data):
                    return 0.7
        
        return 0.0
    
    def _is_relational(self, data: Any) -> float:
        """Check if data has relational properties"""
        if isinstance(data, dict):
            return 0.9
        elif isinstance(data, (list, tuple)):
            # Check for list of dicts (relational database-like)
            if all(isinstance(x, dict) for x in data):
                return 0.8
            # Check for nested structures
            elif any(isinstance(x, (list, tuple, dict)) for x in data):
                return 0.5
        elif isinstance(data, str):
            # Check for JSON-like structure
            try:
                parsed = json.loads(data)
                if isinstance(parsed, dict):
                    return 0.7
            except:
                pass
        
        return 0.0
    
    def _is_metaphorical(self, data: Any) -> float:
        """Check if data has metaphorical/abstract properties"""
        if isinstance(data, str):
            # Look for abstract language patterns
            abstract_indicators = [
                'concept', 'idea', 'theory', 'principle', 'metaphor',
                'symbol', 'meaning', 'abstract', 'philosophical'
            ]
            
            text_lower = data.lower()
            score = sum(1.0 for indicator in abstract_indicators if indicator in text_lower)
            return min(1.0, score / 3.0)
        
        return 0.0
    
    def _is_quantum(self, data: Any) -> float:
        """Check if data has quantum properties"""
        if isinstance(data, (list, tuple, np.ndarray)):
            # Look for complex numbers or quantum-like patterns
            if isinstance(data, np.ndarray):
                if np.iscomplexobj(data):
                    return 0.9
                # Look for quantum state vectors (normalized)
                if data.size > 0:
                    norm = np.linalg.norm(data)
                    if abs(norm - 1.0) < 0.1:  # Near-normalized
                        return 0.6
            
            # Check for complex numbers in list
            elif any(isinstance(x, complex) for x in data):
                return 0.7
        
        # Look for quantum terminology in strings
        if isinstance(data, str):
            quantum_terms = [
                'quantum', 'superposition', 'entanglement', 'qubit',
                'wavefunction', 'amplitude', 'phase', 'coherence'
            ]
            
            text_lower = data.lower()
            score = sum(1.0 for term in quantum_terms if term in text_lower)
            return min(1.0, score / 2.0)
        
        return 0.0
    
    def _is_hypercomplex(self, data: Any) -> float:
        """Check if data is hypercomplex (beyond normal complexity)"""
        complexity = self._calculate_complexity(data)
        
        if complexity > 0.9:
            return 0.8
        elif complexity > 0.7:
            return 0.5
        elif complexity > 0.5:
            return 0.2
        
        return 0.0
    
    # Property estimation methods
    def _calculate_complexity(self, data: Any) -> float:
        """Calculate complexity score for data"""
        if isinstance(data, (int, float)):
            return 0.1
        elif isinstance(data, complex):
            return 0.2
        elif isinstance(data, str):
            # Complexity based on length and content
            length_score = min(1.0, len(data) / 1000.0)
            content_score = len(set(data)) / max(1, len(data))
            return (length_score + content_score) / 2.0
        elif isinstance(data, (list, tuple)):
            # Complexity based on size and nesting
            size_score = min(1.0, len(data) / 100.0)
            nesting_score = self._calculate_nesting_complexity(data)
            return (size_score + nesting_score) / 2.0
        elif isinstance(data, dict):
            # Complexity based on number of keys and value complexity
            size_score = min(1.0, len(data) / 50.0)
            value_complexity = np.mean([self._calculate_complexity(v) for v in data.values()]) if data else 0
            return (size_score + value_complexity) / 2.0
        elif isinstance(data, np.ndarray):
            # Complexity based on size and dimensionality
            size_score = min(1.0, data.size / 1000.0)
            dim_score = min(1.0, data.ndim / 5.0)
            return (size_score + dim_score) / 2.0
        
        return 0.5  # Default medium complexity
    
    def _calculate_nesting_complexity(self, data: Union[list, tuple], depth: int = 0) -> float:
        """Calculate nesting complexity"""
        if depth > 5:  # Prevent infinite recursion
            return 1.0
        
        nested_count = 0
        for item in data:
            if isinstance(item, (list, tuple, dict)):
                nested_count += 1
                if isinstance(item, (list, tuple)):
                    nested_count += self._calculate_nesting_complexity(item, depth + 1)
        
        return min(1.0, nested_count / max(1, len(data)))
    
    def _estimate_numerical_properties(self, data: Any, properties: QuantaProperties) -> QuantaProperties:
        """Estimate properties for numerical data"""
        if isinstance(data, (int, float)):
            properties.dimensionality = 1
            properties.symmetry = 0.5
        elif isinstance(data, complex):
            properties.dimensionality = 2
            properties.symmetry = 0.8
        elif isinstance(data, np.ndarray):
            properties.dimensionality = data.ndim
            # Calculate symmetry (simplified)
            if data.ndim == 1 and data.size > 1:
                symmetry = abs(np.corrcoef(data)[0, 1]) if data.size > 1 else 0.0
                properties.symmetry = max(0.0, symmetry)
        
        return properties
    
    def _estimate_structural_properties(self, data: Any, properties: QuantaProperties) -> QuantaProperties:
        """Estimate properties for structural data"""
        if isinstance(data, dict):
            properties.dimensionality = len(data)
            # Symmetry based on key patterns
            keys = list(data.keys())
            properties.symmetry = len(set(keys)) / max(1, len(keys))
        elif isinstance(data, (list, tuple)):
            properties.dimensionality = 1
            # Continuity based on sequence patterns
            if len(data) > 1:
                continuity = 0.5  # Default
                if all(isinstance(x, (int, float)) for x in data):
                    # Check for sequences
                    diffs = [abs(data[i+1] - data[i]) for i in range(len(data)-1)]
                    if diffs and np.std(diffs) < np.mean(diffs):
                        continuity = 0.8
                properties.continuity = continuity
        
        return properties
    
    def _estimate_temporal_properties(self, data: Any, properties: QuantaProperties) -> QuantaProperties:
        """Estimate properties for temporal data"""
        properties.continuity = 0.8  # Temporal data is typically continuous
        properties.stability = 0.6  # Temporal data can change
        
        return properties
    
    def _estimate_relational_properties(self, data: Any, properties: QuantaProperties) -> QuantaProperties:
        """Estimate properties for relational data"""
        if isinstance(data, dict):
            properties.dimensionality = len(data)
        elif isinstance(data, list) and data and isinstance(data[0], dict):
            # List of records
            if data[0]:
                properties.dimensionality = len(data[0])
        
        properties.coherence = 0.7  # Relational data has internal coherence
        
        return properties
    
    def _estimate_quantum_properties(self, data: Any, properties: QuantaProperties) -> QuantaProperties:
        """Estimate properties for quantum data"""
        properties.symmetry = 0.9  # Quantum states often have symmetry
        properties.coherence = 0.8  # Coherence is important in quantum systems
        
        return properties
    
    def _estimate_dimensionality(self, data: Any) -> int:
        """Estimate data dimensionality"""
        if isinstance(data, (int, float, complex)):
            return 1
        elif isinstance(data, str):
            return 1
        elif isinstance(data, np.ndarray):
            return data.ndim
        elif isinstance(data, dict):
            return len(data)
        elif isinstance(data, (list, tuple)):
            if not data:
                return 1
            # Check if nested
            if any(isinstance(x, (list, tuple, dict)) for x in data):
                return max(self._estimate_dimensionality(x) for x in data)
            return 1
        
        return 1
    
    def _calculate_entropy(self, data: Any) -> float:
        """Calculate information entropy"""
        if isinstance(data, (int, float, complex)):
            return 0.0
        elif isinstance(data, str):
            # Shannon entropy of characters
            char_counts = {}
            for char in data:
                char_counts[char] = char_counts.get(char, 0) + 1
            
            if not char_counts:
                return 0.0
            
            total = sum(char_counts.values())
            entropy = 0.0
            for count in char_counts.values():
                p = count / total
                if p > 0:
                    entropy -= p * np.log2(p)
            
            return min(1.0, entropy / 8.0)  # Normalize
        
        elif isinstance(data, (list, tuple, np.ndarray)):
            # Discretize and calculate entropy
            try:
                data_array = np.array(data, dtype=float)
                if data_array.size == 0:
                    return 0.0
                
                # Create histogram
                hist, _ = np.histogram(data_array, bins=min(20, len(data_array)))
                hist = hist[hist > 0]
                
                if len(hist) == 0:
                    return 0.0
                
                probabilities = hist / np.sum(hist)
                entropy = -np.sum(probabilities * np.log2(probabilities))
                
                return min(1.0, entropy / np.log2(len(hist)))
            except:
                return 0.5
        
        return 0.5  # Default medium entropy
    
    def _estimate_stability(self, data: Any) -> float:
        """Estimate data stability"""
        if isinstance(data, (int, float, complex, str)):
            return 1.0  # Atomic data is stable
        elif isinstance(data, np.ndarray):
            # Stability based on variance
            if np.issubdtype(data.dtype, np.number):
                variance = np.var(data)
                max_var = (np.max(data) - np.min(data)) ** 2 if data.size > 1 else 1.0
                stability = 1.0 - min(1.0, variance / max_var) if max_var > 0 else 1.0
                return stability
        
        return 0.7  # Default moderate stability
    
    def _estimate_coherence(self, data: Any) -> float:
        """Estimate data coherence"""
        if isinstance(data, (int, float, complex, str)):
            return 1.0  # Atomic data is coherent
        elif isinstance(data, np.ndarray):
            # Coherence based on correlation
            if data.size > 1 and np.issubdtype(data.dtype, np.number):
                if data.ndim == 1:
                    # Auto-correlation
                    autocorr = np.correlate(data, data, mode='full')
                    autocorr = autocorr[len(autocorr)//2:]
                    if len(autocorr) > 1:
                        coherence = abs(autocorr[1]) / (abs(autocorr[0]) + 1e-8)
                        return min(1.0, coherence)
        
        return 0.6  # Default moderate coherence
    
    # Helper methods
    def _has_quantum_properties(self, data: Any) -> bool:
        """Check if data actually has quantum properties"""
        return self._is_quantum(data) > 0.5
    
    def _has_missing_data(self, data: Any) -> bool:
        """Check if data has missing values"""
        if isinstance(data, np.ndarray):
            return np.any(np.isnan(data)) or np.any(np.isinf(data))
        elif isinstance(data, (list, tuple)):
            return any(x is None for x in data)
        elif isinstance(data, dict):
            return any(v is None for v in data.values())
        
        return False
    
    def get_analysis_statistics(self) -> Dict[str, Any]:
        """Get statistics about analysis history"""
        if not self.analysis_history:
            return {"message": "No analysis history available"}
        
        type_counts = {}
        complexity_scores = []
        confidence_scores = []
        
        for analysis in self.analysis_history:
            type_name = analysis.detected_type.name
            type_counts[type_name] = type_counts.get(type_name, 0) + 1
            complexity_scores.append(analysis.properties.complexity)
            confidence_scores.append(analysis.confidence)
        
        return {
            'total_analyses': len(self.analysis_history),
            'type_distribution': type_counts,
            'average_complexity': np.mean(complexity_scores),
            'average_confidence': np.mean(confidence_scores),
            'most_common_type': max(type_counts.keys(), key=lambda k: type_counts[k]) if type_counts else None
        }