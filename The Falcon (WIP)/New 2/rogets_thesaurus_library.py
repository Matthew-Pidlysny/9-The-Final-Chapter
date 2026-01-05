"""
ROGET'S THESAURUS LIBRARY - Falcon Press Office Compatible
Comprehensive database of English words organized by semantic relationships
Compliant with sphere conventions from Breath, Caelum, Space Balls, and Cradle repositories
"""

from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple, Set
import math
import json
from datetime import datetime
import hashlib
import numpy as np
import re

@dataclass
class ThesaurusEntry:
    """Thesaurus Entry dataclass following sphere conventions"""
    entry_id: str
    concept_number: str
    concept_name: str
    category: str
    subcategory: str
    synonyms: List[str]
    related_concepts: List[str]
    antonyms: List[str]
    semantic_class: str  # Abstract, Concrete, Action, Quality, etc.
    relationship_density: float  # 0-1 scale (how many connections)
    abstraction_level: float  # 0-1 scale (concrete to abstract)
    usage_context: List[str]  # Formal, Informal, Technical, etc.
    sphere_coordinates: Tuple[float, float, float]
    quantum_signature: str
    fuzzy_classification: str
    mathematical_properties: Dict
    metadata: Dict

class ThesaurusSphereProcessor:
    """Mathematical engine for thesaurus entry sphere generation"""
    
    def __init__(self):
        self.forbidden_angles = [30.0, 90.0, 150.0, 210.0, 270.0, 330.0]
        self.prime_sequences = [4, 7, 9, 11, 13, 17, 19, 23, 29, 31]
    
    def calculate_sphere_coordinates(self, concept_number: str, concept_name: str) -> Tuple[float, float, float]:
        """Generate sphere coordinates using 4-7-9 number theory with forbidden angle avoidance"""
        hash_input = f"{concept_number}_{concept_name}"
        hash_obj = hashlib.md5(hash_input.encode())
        hash_hex = hash_obj.hexdigest()
        
        base_values = [int(hash_hex[i:i+8], 16) for i in range(0, 32, 8)]
        
        x = (base_values[0] / 2**32) * 4 * math.pi
        y = (base_values[1] / 2**32) * 7 * math.pi
        z = (base_values[2] / 2**32) * 9 * math.pi
        
        # Check and avoid forbidden angles
        angle_degrees = math.degrees(x) % 360
        while any(abs(angle_degrees - forbidden) < 5.0 for forbidden in self.forbidden_angles):
            x += 0.1
            angle_degrees = math.degrees(x) % 360
        
        return (x, y, z)
    
    def generate_quantum_signature(self, entry_data: Dict) -> str:
        """Generate quantum signature using prime sequence mathematics"""
        signature_components = [
            len(entry_data.get('synonyms', [])),
            len(entry_data.get('related_concepts', [])),
            len(entry_data.get('antonyms', [])),
            self.prime_sequences[len(entry_data.get('concept_name', '')) % len(self.prime_sequences)]
        ]
        
        quantum_hash = hashlib.sha256(str(signature_components).encode()).hexdigest()[:16]
        return f"Q{quantum_hash.upper()}"
    
    def classify_fuzzy(self, entry: ThesaurusEntry) -> str:
        """Fuzzy classification based on semantic characteristics"""
        score = 0
        
        # Relationship density classification
        if entry.relationship_density > 0.8:
            score += 3
        elif entry.relationship_density > 0.6:
            score += 2
        elif entry.relationship_density > 0.4:
            score += 1
        
        # Abstraction level classification
        if entry.abstraction_level > 0.7:
            score += 3
        elif entry.abstraction_level > 0.5:
            score += 2
        elif entry.abstraction_level > 0.3:
            score += 1
        
        # Synonym count
        syn_count = len(entry.synonyms)
        if syn_count > 20:
            score += 2
        elif syn_count > 10:
            score += 1
        
        # Classification based on score
        if score >= 6:
            return "Rich"
        elif score >= 4:
            return "Developed"
        elif score >= 2:
            return "Standard"
        else:
            return "Basic"
    
    def calculate_mathematical_properties(self, entry: ThesaurusEntry) -> Dict:
        """Calculate mathematical properties for sphere compatibility"""
        coords = entry.sphere_coordinates
        
        # Calculate prime factors of synonym count
        prime_factors = self._get_prime_factors(len(entry.synonyms) + 1)
        
        return {
            'prime_factor_sum': sum(prime_factors),
            'coordinate_magnitude': math.sqrt(coords[0]**2 + coords[1]**2 + coords[2]**2),
            'angular_distribution': [
                math.degrees(coords[0]) % 360,
                math.degrees(coords[1]) % 360,
                math.degrees(coords[2]) % 360
            ],
            'geometric_entropy': math.log2(len(entry.synonyms) + len(entry.related_concepts) + len(entry.antonyms) + 1),
            'forbidden_angle_compliance': all(
                abs(math.degrees(coord) % 360 - forbidden) > 5.0 
                for coord in coords 
                for forbidden in self.forbidden_angles
            ),
            'semantic_connectivity': entry.relationship_density,
            'abstraction_measure': entry.abstraction_level
        }
    
    def _get_prime_factors(self, n: int) -> List[int]:
        """Get prime factors of a number"""
        if n <= 1:
            return [1]
        factors = []
        d = 2
        while d * d <= n:
            while n % d == 0:
                factors.append(d)
                n //= d
            d += 1
        if n > 1:
            factors.append(n)
        return factors if factors else [1]

class RogetsThesaurusLibrary:
    """Main library class for Roget's Thesaurus entries"""
    
    def __init__(self):
        self.processor = ThesaurusSphereProcessor()
        self.entries = {}
        self._initialize_library()
    
    def _initialize_library(self):
        """Initialize library with sample entries (to be populated from file)"""
        # Sample entries demonstrating the structure
        sample_entries = self._create_sample_entries()
        for entry in sample_entries:
            self.add_entry(entry)
    
    def _create_sample_entries(self) -> List[ThesaurusEntry]:
        """Create sample thesaurus entries"""
        samples = []
        
        # Sample 1: Abstract concept
        entry_data = {
            'concept_number': '1',
            'concept_name': 'Existence',
            'category': 'Abstract Relations',
            'subcategory': 'Existence',
            'synonyms': ['being', 'entity', 'subsistence', 'reality', 'actuality', 'presence'],
            'related_concepts': ['life', 'substance', 'essence', 'nature'],
            'antonyms': ['nonexistence', 'nothingness', 'nullity', 'nihility'],
            'semantic_class': 'Abstract',
            'relationship_density': 0.7,
            'abstraction_level': 0.9,
            'usage_context': ['Formal', 'Philosophical']
        }
        samples.append(self._create_entry('THES_001', entry_data))
        
        # Sample 2: Concrete concept
        entry_data = {
            'concept_number': '189',
            'concept_name': 'Abode',
            'category': 'Space',
            'subcategory': 'Place',
            'synonyms': ['dwelling', 'residence', 'domicile', 'habitation', 'home', 'house', 'lodging', 'quarters'],
            'related_concepts': ['shelter', 'accommodation', 'housing', 'nest'],
            'antonyms': [],
            'semantic_class': 'Concrete',
            'relationship_density': 0.6,
            'abstraction_level': 0.3,
            'usage_context': ['Formal', 'Common']
        }
        samples.append(self._create_entry('THES_002', entry_data))
        
        # Sample 3: Action concept
        entry_data = {
            'concept_number': '264',
            'concept_name': 'Motion',
            'category': 'Space',
            'subcategory': 'Motion',
            'synonyms': ['movement', 'move', 'mobility', 'motility', 'locomotion', 'action'],
            'related_concepts': ['progress', 'travel', 'journey', 'transit', 'passage'],
            'antonyms': ['rest', 'stillness', 'immobility', 'stagnation'],
            'semantic_class': 'Action',
            'relationship_density': 0.8,
            'abstraction_level': 0.5,
            'usage_context': ['Common', 'Technical']
        }
        samples.append(self._create_entry('THES_003', entry_data))
        
        return samples
    
    def _create_entry(self, entry_id: str, entry_data: Dict) -> ThesaurusEntry:
        """Create a thesaurus entry with all sphere properties"""
        concept_number = entry_data['concept_number']
        concept_name = entry_data['concept_name']
        
        # Generate sphere coordinates
        coords = self.processor.calculate_sphere_coordinates(concept_number, concept_name)
        
        # Generate quantum signature
        quantum_sig = self.processor.generate_quantum_signature(entry_data)
        
        # Create entry
        entry = ThesaurusEntry(
            entry_id=entry_id,
            concept_number=concept_number,
            concept_name=concept_name,
            category=entry_data['category'],
            subcategory=entry_data['subcategory'],
            synonyms=entry_data['synonyms'],
            related_concepts=entry_data.get('related_concepts', []),
            antonyms=entry_data.get('antonyms', []),
            semantic_class=entry_data['semantic_class'],
            relationship_density=entry_data['relationship_density'],
            abstraction_level=entry_data['abstraction_level'],
            usage_context=entry_data.get('usage_context', []),
            sphere_coordinates=coords,
            quantum_signature=quantum_sig,
            fuzzy_classification='',
            mathematical_properties={},
            metadata={
                'source': 'Roget\'s Thesaurus',
                'language': 'English',
                'date_added': datetime.now().strftime('%Y-%m-%d')
            }
        )
        
        # Calculate fuzzy classification
        entry.fuzzy_classification = self.processor.classify_fuzzy(entry)
        
        # Calculate mathematical properties
        entry.mathematical_properties = self.processor.calculate_mathematical_properties(entry)
        
        return entry
    
    def add_entry(self, entry: ThesaurusEntry):
        """Add a thesaurus entry to the library"""
        self.entries[entry.entry_id] = entry
    
    def get_entry_by_concept(self, concept_name: str) -> Optional[ThesaurusEntry]:
        """Get thesaurus entry by concept name"""
        for entry in self.entries.values():
            if entry.concept_name.lower() == concept_name.lower():
                return entry
        return None
    
    def get_entries_by_category(self, category: str) -> List[ThesaurusEntry]:
        """Get all entries in a specific category"""
        return [entry for entry in self.entries.values() 
                if entry.category == category]
    
    def get_entries_by_semantic_class(self, semantic_class: str) -> List[ThesaurusEntry]:
        """Get all entries of a specific semantic class"""
        return [entry for entry in self.entries.values() 
                if entry.semantic_class == semantic_class]
    
    def get_rich_concepts(self) -> List[ThesaurusEntry]:
        """Get entries with high relationship density"""
        return [entry for entry in self.entries.values() 
                if entry.relationship_density > 0.7]
    
    def find_synonyms(self, word: str) -> List[str]:
        """Find synonyms for a given word"""
        synonyms = set()
        for entry in self.entries.values():
            if word.lower() in [s.lower() for s in entry.synonyms]:
                synonyms.update(entry.synonyms)
        return list(synonyms)
    
    def find_antonyms(self, word: str) -> List[str]:
        """Find antonyms for a given word"""
        antonyms = set()
        for entry in self.entries.values():
            if word.lower() in [s.lower() for s in entry.synonyms]:
                antonyms.update(entry.antonyms)
        return list(antonyms)
    
    def get_sphere_generation_data(self) -> Dict:
        """Get data ready for sphere generation"""
        return {
            'coordinates': {eid: e.sphere_coordinates for eid, e in self.entries.items()},
            'quantum_signatures': {eid: e.quantum_signature for eid, e in self.entries.items()},
            'mathematical_properties': {eid: e.mathematical_properties for eid, e in self.entries.items()},
            'total_entries': len(self.entries),
            'classifications': list(set(e.fuzzy_classification for e in self.entries.values())),
            'categories': list(set(e.category for e in self.entries.values())),
            'semantic_classes': list(set(e.semantic_class for e in self.entries.values()))
        }
    
    def get_data_statistics(self) -> Dict:
        """Get comprehensive statistics about the library"""
        return {
            'total_entries': len(self.entries),
            'average_synonyms': sum(len(e.synonyms) for e in self.entries.values()) / len(self.entries) if self.entries else 0,
            'average_relationship_density': sum(e.relationship_density for e in self.entries.values()) / len(self.entries) if self.entries else 0,
            'classification_distribution': self._analyze_classifications(),
            'category_distribution': self._analyze_categories(),
            'quantum_signatures': [e.quantum_signature for e in self.entries.values()],
            'mathematical_summary': self._generate_mathematical_summary()
        }
    
    def _analyze_classifications(self) -> Dict:
        """Analyze distribution of fuzzy classifications"""
        class_counts = {}
        for entry in self.entries.values():
            classification = entry.fuzzy_classification
            class_counts[classification] = class_counts.get(classification, 0) + 1
        return class_counts
    
    def _analyze_categories(self) -> Dict:
        """Analyze category distribution"""
        cat_counts = {}
        for entry in self.entries.values():
            category = entry.category
            cat_counts[category] = cat_counts.get(category, 0) + 1
        return cat_counts
    
    def _generate_mathematical_summary(self) -> Dict:
        """Generate mathematical summary for sphere compatibility"""
        coords = [entry.sphere_coordinates for entry in self.entries.values()]
        return {
            'coordinate_variance': np.var([c[0] for c in coords]) if coords else 0,
            'quantum_diversity': len(set(e.quantum_signature for e in self.entries.values())),
            'forbidden_angle_compliance_rate': sum(
                1 for e in self.entries.values()
                if e.mathematical_properties['forbidden_angle_compliance']
            ) / len(self.entries) if self.entries else 0,
            'average_geometric_entropy': sum(
                e.mathematical_properties['geometric_entropy'] 
                for e in self.entries.values()
            ) / len(self.entries) if self.entries else 0
        }
    
    def parse_thesaurus_file(self, filepath: str, max_entries: int = None):
        """Parse Roget's Thesaurus text file and populate library"""
        print(f"Parsing thesaurus file: {filepath}")
        
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Find entries marked with #
        entry_pattern = r'#(\d+)\.\s+([^\n]+)\n(.*?)(?=#\d+\.|$)'
        matches = re.findall(entry_pattern, content, re.DOTALL)
        
        entries_parsed = 0
        
        for match in matches:
            concept_number = match[0]
            concept_name = match[1].strip()
            entry_content = match[2]
            
            # Parse the entry content
            entry_data = self._parse_thesaurus_entry(concept_number, concept_name, entry_content)
            
            if entry_data:
                entry_id = f"THES_{entries_parsed+1:06d}"
                try:
                    entry = self._create_entry(entry_id, entry_data)
                    self.add_entry(entry)
                    entries_parsed += 1
                    
                    if entries_parsed % 100 == 0:
                        print(f"Parsed {entries_parsed} entries...")
                    
                    if max_entries and entries_parsed >= max_entries:
                        break
                except Exception as e:
                    print(f"Error creating entry for concept '{concept_name}': {e}")
        
        print(f"Successfully parsed {entries_parsed} thesaurus entries")
    
    def _parse_thesaurus_entry(self, concept_number: str, concept_name: str, content: str) -> Optional[Dict]:
        """Parse the content of a thesaurus entry"""
        try:
            # Extract words/synonyms (typically comma-separated)
            # Clean up the content
            content = content.replace('\n', ' ').replace('\r', '')
            
            # Split by common delimiters
            words = []
            for part in content.split(';'):
                for word in part.split(','):
                    word = word.strip()
                    # Remove annotations like [obs3], |, etc.
                    word = re.sub(r'\[.*?\]', '', word)
                    word = re.sub(r'\|.*?$', '', word)
                    word = word.strip('.,;:!?')
                    if word and len(word) > 1 and word.isalpha():
                        words.append(word.lower())
            
            # Remove duplicates while preserving order
            synonyms = []
            seen = set()
            for word in words:
                if word not in seen:
                    synonyms.append(word)
                    seen.add(word)
            
            # Limit to reasonable number
            synonyms = synonyms[:50]
            
            # Determine category (simplified - would need more sophisticated parsing)
            category = self._determine_category(concept_name, content)
            
            # Determine semantic class
            semantic_class = self._determine_semantic_class(concept_name, synonyms)
            
            # Calculate relationship density based on synonym count
            relationship_density = min(1.0, len(synonyms) / 30.0)
            
            # Calculate abstraction level (simplified heuristic)
            abstraction_level = self._estimate_abstraction(concept_name, synonyms)
            
            return {
                'concept_number': concept_number,
                'concept_name': concept_name,
                'category': category,
                'subcategory': category,  # Simplified
                'synonyms': synonyms if synonyms else [concept_name.lower()],
                'related_concepts': [],
                'antonyms': [],
                'semantic_class': semantic_class,
                'relationship_density': relationship_density,
                'abstraction_level': abstraction_level,
                'usage_context': ['General']
            }
        except Exception as e:
            print(f"Error parsing thesaurus entry '{concept_name}': {e}")
            return None
    
    def _determine_category(self, concept_name: str, content: str) -> str:
        """Determine the category of a concept"""
        # Simplified categorization
        abstract_keywords = ['existence', 'relation', 'quantity', 'order', 'time', 'change', 'cause']
        space_keywords = ['space', 'dimension', 'form', 'motion', 'place', 'direction']
        matter_keywords = ['matter', 'material', 'organic', 'inorganic', 'body']
        intellect_keywords = ['intellect', 'thought', 'idea', 'reasoning', 'knowledge', 'communication']
        volition_keywords = ['volition', 'will', 'action', 'choice', 'intention']
        affection_keywords = ['affection', 'emotion', 'feeling', 'moral', 'sympathy']
        
        concept_lower = concept_name.lower()
        
        if any(kw in concept_lower for kw in abstract_keywords):
            return 'Abstract Relations'
        elif any(kw in concept_lower for kw in space_keywords):
            return 'Space'
        elif any(kw in concept_lower for kw in matter_keywords):
            return 'Matter'
        elif any(kw in concept_lower for kw in intellect_keywords):
            return 'Intellect'
        elif any(kw in concept_lower for kw in volition_keywords):
            return 'Volition'
        elif any(kw in concept_lower for kw in affection_keywords):
            return 'Affections'
        else:
            return 'General'
    
    def _determine_semantic_class(self, concept_name: str, synonyms: List[str]) -> str:
        """Determine the semantic class of a concept"""
        # Check for action words (verbs)
        action_indicators = ['tion', 'ment', 'ing', 'ance', 'ence']
        if any(concept_name.lower().endswith(ind) for ind in action_indicators):
            return 'Action'
        
        # Check for quality words (adjectives)
        quality_indicators = ['ness', 'ity', 'ty']
        if any(concept_name.lower().endswith(ind) for ind in quality_indicators):
            return 'Quality'
        
        # Check for concrete vs abstract
        concrete_keywords = ['place', 'object', 'thing', 'body', 'material']
        if any(kw in concept_name.lower() for kw in concrete_keywords):
            return 'Concrete'
        
        return 'Abstract'
    
    def _estimate_abstraction(self, concept_name: str, synonyms: List[str]) -> float:
        """Estimate the abstraction level of a concept"""
        # Simplified heuristic: longer words and philosophical terms tend to be more abstract
        avg_length = (len(concept_name) + sum(len(s) for s in synonyms[:10])) / (len(synonyms[:10]) + 1)
        
        abstract_keywords = ['essence', 'nature', 'quality', 'relation', 'existence', 'being']
        abstract_score = sum(1 for kw in abstract_keywords if kw in concept_name.lower())
        
        return min(1.0, (avg_length / 15.0) + (abstract_score * 0.2))

# Library metadata
LIBRARY_METADATA = {
    "library_name": "Roget's Thesaurus Library",
    "version": "1.0.0",
    "generation_date": datetime.now().strftime('%Y-%m-%d'),
    "source": "Roget's Thesaurus (Project Gutenberg)",
    "sphere_convention": "Breath-Caelum-Space Balls-Cradle compliant",
    "mathematical_engine": "4-7-9 number theory with forbidden angle mapping",
    "assessment_relay_ready": True,
    "sphere_generation_compatible": True
}

# Export main library instance
thesaurus_library = RogetsThesaurusLibrary()

if __name__ == "__main__":
    print("Roget's Thesaurus Library Loaded")
    print(f"Total Entries: {len(thesaurus_library.entries)}")
    print(f"Sphere Generation Data: {thesaurus_library.get_sphere_generation_data()}")