"""
WEBSTER'S DICTIONARY LIBRARY - Falcon Press Office Compatible
Comprehensive database of English words and definitions from Webster's Unabridged Dictionary
Compliant with sphere conventions from Breath, Caelum, Space Balls, and Cradle repositories
"""

from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple
import math
import json
from datetime import datetime
import hashlib
import numpy as np
import re

@dataclass
class DictionaryEntry:
    """Dictionary Entry dataclass following sphere conventions"""
    entry_id: str
    word: str
    part_of_speech: List[str]
    definitions: List[str]
    etymology: str
    pronunciation: str
    usage_examples: List[str]
    word_length: int
    syllable_count: int
    complexity_score: float  # 0-1 scale
    frequency_estimate: str  # Common, Uncommon, Rare, Archaic
    sphere_coordinates: Tuple[float, float, float]
    quantum_signature: str
    fuzzy_classification: str
    mathematical_properties: Dict
    metadata: Dict

class DictionarySphereProcessor:
    """Mathematical engine for dictionary entry sphere generation"""
    
    def __init__(self):
        self.forbidden_angles = [30.0, 90.0, 150.0, 210.0, 270.0, 330.0]
        self.prime_sequences = [4, 7, 9, 11, 13, 17, 19, 23, 29, 31]
    
    def calculate_sphere_coordinates(self, word: str, entry_id: str) -> Tuple[float, float, float]:
        """Generate sphere coordinates using 4-7-9 number theory with forbidden angle avoidance"""
        hash_input = f"{word}_{entry_id}"
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
            len(entry_data.get('definitions', [])),
            entry_data.get('word_length', 0),
            len(entry_data.get('part_of_speech', [])),
            self.prime_sequences[entry_data.get('word_length', 0) % len(self.prime_sequences)]
        ]
        
        quantum_hash = hashlib.sha256(str(signature_components).encode()).hexdigest()[:16]
        return f"Q{quantum_hash.upper()}"
    
    def classify_fuzzy(self, entry: DictionaryEntry) -> str:
        """Fuzzy classification based on word characteristics"""
        score = 0
        
        # Word length classification
        if entry.word_length > 12:
            score += 3
        elif entry.word_length > 8:
            score += 2
        elif entry.word_length > 5:
            score += 1
        
        # Complexity classification
        if entry.complexity_score > 0.8:
            score += 3
        elif entry.complexity_score > 0.6:
            score += 2
        elif entry.complexity_score > 0.4:
            score += 1
        
        # Definition diversity
        def_count = len(entry.definitions)
        if def_count > 5:
            score += 2
        elif def_count > 2:
            score += 1
        
        # Classification based on score
        if score >= 6:
            return "Complex"
        elif score >= 4:
            return "Advanced"
        elif score >= 2:
            return "Standard"
        else:
            return "Simple"
    
    def calculate_mathematical_properties(self, entry: DictionaryEntry) -> Dict:
        """Calculate mathematical properties for sphere compatibility"""
        coords = entry.sphere_coordinates
        
        # Calculate prime factors of word length
        prime_factors = self._get_prime_factors(entry.word_length)
        
        return {
            'prime_factor_sum': sum(prime_factors),
            'coordinate_magnitude': math.sqrt(coords[0]**2 + coords[1]**2 + coords[2]**2),
            'angular_distribution': [
                math.degrees(coords[0]) % 360,
                math.degrees(coords[1]) % 360,
                math.degrees(coords[2]) % 360
            ],
            'geometric_entropy': math.log2(len(entry.word) + len(entry.definitions) + 1),
            'forbidden_angle_compliance': all(
                abs(math.degrees(coord) % 360 - forbidden) > 5.0 
                for coord in coords 
                for forbidden in self.forbidden_angles
            ),
            'definition_density': len(entry.definitions) / max(entry.word_length, 1),
            'linguistic_complexity': entry.complexity_score
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

class WebstersDictionaryLibrary:
    """Main library class for Webster's Dictionary entries"""
    
    def __init__(self):
        self.processor = DictionarySphereProcessor()
        self.entries = {}
        self._initialize_library()
    
    def _initialize_library(self):
        """Initialize library with sample entries (to be populated from file)"""
        # Sample entries demonstrating the structure
        sample_entries = self._create_sample_entries()
        for entry in sample_entries:
            self.add_entry(entry)
    
    def _create_sample_entries(self) -> List[DictionaryEntry]:
        """Create sample dictionary entries"""
        samples = []
        
        # Sample 1: Simple word
        entry_data = {
            'word': 'cat',
            'part_of_speech': ['noun'],
            'definitions': ['A small domesticated carnivorous mammal with soft fur, a short snout, and retractable claws.'],
            'etymology': 'Old English catt, of Germanic origin',
            'pronunciation': 'kat',
            'usage_examples': ['The cat sat on the mat.'],
            'word_length': 3,
            'syllable_count': 1,
            'complexity_score': 0.2,
            'frequency_estimate': 'Common'
        }
        samples.append(self._create_entry('DICT_001', entry_data))
        
        # Sample 2: Complex word
        entry_data = {
            'word': 'serendipity',
            'part_of_speech': ['noun'],
            'definitions': [
                'The occurrence and development of events by chance in a happy or beneficial way.',
                'The faculty of making fortunate discoveries by accident.'
            ],
            'etymology': 'Coined by Horace Walpole in 1754',
            'pronunciation': 'ser-en-dip-i-ty',
            'usage_examples': ['A fortunate stroke of serendipity brought the two old friends together.'],
            'word_length': 11,
            'syllable_count': 5,
            'complexity_score': 0.8,
            'frequency_estimate': 'Uncommon'
        }
        samples.append(self._create_entry('DICT_002', entry_data))
        
        # Sample 3: Technical word
        entry_data = {
            'word': 'algorithm',
            'part_of_speech': ['noun'],
            'definitions': [
                'A process or set of rules to be followed in calculations or other problem-solving operations.',
                'A step-by-step procedure for solving a problem or accomplishing a task.'
            ],
            'etymology': 'From Arabic al-Khwarizmi, Persian mathematician',
            'pronunciation': 'al-go-rith-m',
            'usage_examples': ['The sorting algorithm efficiently organized the data.'],
            'word_length': 9,
            'syllable_count': 4,
            'complexity_score': 0.7,
            'frequency_estimate': 'Common'
        }
        samples.append(self._create_entry('DICT_003', entry_data))
        
        return samples
    
    def _create_entry(self, entry_id: str, entry_data: Dict) -> DictionaryEntry:
        """Create a dictionary entry with all sphere properties"""
        word = entry_data['word']
        
        # Generate sphere coordinates
        coords = self.processor.calculate_sphere_coordinates(word, entry_id)
        
        # Generate quantum signature
        quantum_sig = self.processor.generate_quantum_signature(entry_data)
        
        # Create entry
        entry = DictionaryEntry(
            entry_id=entry_id,
            word=word,
            part_of_speech=entry_data['part_of_speech'],
            definitions=entry_data['definitions'],
            etymology=entry_data.get('etymology', ''),
            pronunciation=entry_data.get('pronunciation', ''),
            usage_examples=entry_data.get('usage_examples', []),
            word_length=entry_data['word_length'],
            syllable_count=entry_data.get('syllable_count', 1),
            complexity_score=entry_data['complexity_score'],
            frequency_estimate=entry_data['frequency_estimate'],
            sphere_coordinates=coords,
            quantum_signature=quantum_sig,
            fuzzy_classification='',
            mathematical_properties={},
            metadata={
                'source': 'Webster\'s Unabridged Dictionary',
                'language': 'English',
                'date_added': datetime.now().strftime('%Y-%m-%d')
            }
        )
        
        # Calculate fuzzy classification
        entry.fuzzy_classification = self.processor.classify_fuzzy(entry)
        
        # Calculate mathematical properties
        entry.mathematical_properties = self.processor.calculate_mathematical_properties(entry)
        
        return entry
    
    def add_entry(self, entry: DictionaryEntry):
        """Add a dictionary entry to the library"""
        self.entries[entry.entry_id] = entry
    
    def get_entry_by_word(self, word: str) -> Optional[DictionaryEntry]:
        """Get dictionary entry by word"""
        for entry in self.entries.values():
            if entry.word.lower() == word.lower():
                return entry
        return None
    
    def get_entries_by_classification(self, classification: str) -> List[DictionaryEntry]:
        """Get all entries with a specific fuzzy classification"""
        return [entry for entry in self.entries.values() 
                if entry.fuzzy_classification == classification]
    
    def get_complex_words(self) -> List[DictionaryEntry]:
        """Get entries with high complexity scores"""
        return [entry for entry in self.entries.values() 
                if entry.complexity_score > 0.7]
    
    def get_sphere_generation_data(self) -> Dict:
        """Get data ready for sphere generation"""
        return {
            'coordinates': {eid: e.sphere_coordinates for eid, e in self.entries.items()},
            'quantum_signatures': {eid: e.quantum_signature for eid, e in self.entries.items()},
            'mathematical_properties': {eid: e.mathematical_properties for eid, e in self.entries.items()},
            'total_entries': len(self.entries),
            'classifications': list(set(e.fuzzy_classification for e in self.entries.values())),
            'parts_of_speech': list(set(pos for e in self.entries.values() for pos in e.part_of_speech)),
            'frequency_distribution': self._analyze_frequency()
        }
    
    def get_data_statistics(self) -> Dict:
        """Get comprehensive statistics about the library"""
        return {
            'total_entries': len(self.entries),
            'average_word_length': sum(e.word_length for e in self.entries.values()) / len(self.entries),
            'average_complexity': sum(e.complexity_score for e in self.entries.values()) / len(self.entries),
            'classification_distribution': self._analyze_classifications(),
            'frequency_distribution': self._analyze_frequency(),
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
    
    def _analyze_frequency(self) -> Dict:
        """Analyze frequency distribution"""
        freq_counts = {}
        for entry in self.entries.values():
            freq = entry.frequency_estimate
            freq_counts[freq] = freq_counts.get(freq, 0) + 1
        return freq_counts
    
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
    
    def parse_dictionary_file(self, filepath: str, max_entries: int = None):
        """Parse Webster's Dictionary text file and populate library"""
        print(f"Parsing dictionary file: {filepath}")
        
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Find the start of actual dictionary content (after Project Gutenberg header)
        start_marker = "A\nA (named a in the English"
        start_pos = content.find(start_marker)
        if start_pos == -1:
            print("Could not find dictionary start marker")
            return
        
        content = content[start_pos:]
        
        # Split into entries - entries typically start with a word in CAPS followed by newline
        # Pattern: Word at start of line, followed by definition content
        entries_parsed = 0
        current_word = None
        current_content = []
        
        lines = content.split('\n')
        
        for i, line in enumerate(lines):
            line = line.strip()
            
            # Skip empty lines
            if not line:
                continue
            
            # Check if this line starts a new entry (all caps word, or caps word with punctuation)
            if line and line[0].isupper() and (len(line.split()) == 1 or ';' in line or ',' in line):
                # Save previous entry if exists
                if current_word and current_content:
                    entry_data = self._parse_entry_content(current_word, '\n'.join(current_content))
                    if entry_data:
                        entry_id = f"DICT_{entries_parsed+1:06d}"
                        try:
                            entry = self._create_entry(entry_id, entry_data)
                            self.add_entry(entry)
                            entries_parsed += 1
                            
                            if entries_parsed % 1000 == 0:
                                print(f"Parsed {entries_parsed} entries...")
                            
                            if max_entries and entries_parsed >= max_entries:
                                break
                        except Exception as e:
                            print(f"Error creating entry for '{current_word}': {e}")
                
                # Start new entry
                current_word = line.split()[0].strip('.,;:')
                current_content = [line]
            else:
                # Continue current entry
                if current_word:
                    current_content.append(line)
        
        # Don't forget the last entry
        if current_word and current_content and (not max_entries or entries_parsed < max_entries):
            entry_data = self._parse_entry_content(current_word, '\n'.join(current_content))
            if entry_data:
                entry_id = f"DICT_{entries_parsed+1:06d}"
                try:
                    entry = self._create_entry(entry_id, entry_data)
                    self.add_entry(entry)
                    entries_parsed += 1
                except Exception as e:
                    print(f"Error creating entry for '{current_word}': {e}")
        
        print(f"Successfully parsed {entries_parsed} dictionary entries")
    
    def _parse_entry_content(self, word: str, content: str) -> Optional[Dict]:
        """Parse the content of a dictionary entry"""
        try:
            # Extract definitions (lines starting with "Defn:")
            definitions = []
            defn_pattern = r'Defn:\s*(.+?)(?=\n\n|\nDefn:|\n[A-Z]|\Z)'
            defn_matches = re.findall(defn_pattern, content, re.DOTALL)
            for match in defn_matches:
                clean_def = match.strip().replace('\n', ' ').replace('\r', '')
                if clean_def:
                    definitions.append(clean_def)
            
            if not definitions:
                # Try to extract any text after the word as definition
                lines = content.split('\n')
                for line in lines[1:]:  # Skip first line (the word itself)
                    if line.strip() and not line.startswith('Etym:'):
                        definitions.append(line.strip())
                        break
            
            # Extract etymology (lines starting with "Etym:")
            etymology = ''
            etym_pattern = r'Etym:\s*(.+?)(?=\n\n|\nDefn:|\Z)'
            etym_match = re.search(etym_pattern, content, re.DOTALL)
            if etym_match:
                etymology = etym_match.group(1).strip().replace('\n', ' ')
            
            # Determine part of speech (look for common indicators)
            parts_of_speech = []
            pos_indicators = {
                'n.': 'noun',
                'v.': 'verb',
                'adj.': 'adjective',
                'adv.': 'adverb',
                'prep.': 'preposition',
                'conj.': 'conjunction',
                'pron.': 'pronoun',
                'interj.': 'interjection'
            }
            for indicator, pos in pos_indicators.items():
                if indicator in content.lower():
                    parts_of_speech.append(pos)
            
            if not parts_of_speech:
                parts_of_speech = ['unknown']
            
            # Calculate word properties
            word_length = len(word)
            syllable_count = max(1, word_length // 3)  # Rough estimate
            
            # Estimate complexity based on word length and definition count
            complexity_score = min(1.0, (word_length / 15.0) + (len(definitions) / 10.0))
            
            # Estimate frequency (simplified)
            if word_length <= 4:
                frequency = 'Common'
            elif word_length <= 8:
                frequency = 'Uncommon'
            else:
                frequency = 'Rare'
            
            return {
                'word': word.lower(),
                'part_of_speech': parts_of_speech,
                'definitions': definitions if definitions else ['No definition available'],
                'etymology': etymology,
                'pronunciation': '',
                'usage_examples': [],
                'word_length': word_length,
                'syllable_count': syllable_count,
                'complexity_score': complexity_score,
                'frequency_estimate': frequency
            }
        except Exception as e:
            print(f"Error parsing entry for '{word}': {e}")
            return None

# Library metadata
LIBRARY_METADATA = {
    "library_name": "Webster's Dictionary Library",
    "version": "1.0.0",
    "generation_date": datetime.now().strftime('%Y-%m-%d'),
    "source": "Webster's Unabridged Dictionary (Project Gutenberg)",
    "sphere_convention": "Breath-Caelum-Space Balls-Cradle compliant",
    "mathematical_engine": "4-7-9 number theory with forbidden angle mapping",
    "assessment_relay_ready": True,
    "sphere_generation_compatible": True
}

# Export main library instance
dictionary_library = WebstersDictionaryLibrary()

if __name__ == "__main__":
    print("Webster's Dictionary Library Loaded")
    print(f"Total Entries: {len(dictionary_library.entries)}")
    print(f"Sphere Generation Data: {dictionary_library.get_sphere_generation_data()}")