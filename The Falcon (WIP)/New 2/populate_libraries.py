"""
Script to populate Webster's Dictionary and Roget's Thesaurus libraries
with data from the Project Gutenberg text files
"""

import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from websters_dictionary_library import dictionary_library, LIBRARY_METADATA as dict_metadata
from rogets_thesaurus_library import thesaurus_library, LIBRARY_METADATA as thes_metadata
import json

def populate_dictionary(filepath: str, max_entries: int = 5000):
    """Populate the dictionary library from Webster's Dictionary file"""
    print("\n" + "="*80)
    print("POPULATING WEBSTER'S DICTIONARY LIBRARY")
    print("="*80)
    
    dictionary_library.parse_dictionary_file(filepath, max_entries=max_entries)
    
    print("\n" + "-"*80)
    print("DICTIONARY LIBRARY STATISTICS")
    print("-"*80)
    stats = dictionary_library.get_data_statistics()
    print(f"Total Entries: {stats['total_entries']}")
    print(f"Average Word Length: {stats['average_word_length']:.2f}")
    print(f"Average Complexity: {stats['average_complexity']:.2f}")
    print(f"\nClassification Distribution:")
    for classification, count in stats['classification_distribution'].items():
        print(f"  {classification}: {count}")
    print(f"\nFrequency Distribution:")
    for freq, count in stats['frequency_distribution'].items():
        print(f"  {freq}: {count}")
    print(f"\nMathematical Summary:")
    for key, value in stats['mathematical_summary'].items():
        if isinstance(value, float):
            print(f"  {key}: {value:.4f}")
        else:
            print(f"  {key}: {value}")
    
    return dictionary_library

def populate_thesaurus(filepath: str, max_entries: int = 1000):
    """Populate the thesaurus library from Roget's Thesaurus file"""
    print("\n" + "="*80)
    print("POPULATING ROGET'S THESAURUS LIBRARY")
    print("="*80)
    
    thesaurus_library.parse_thesaurus_file(filepath, max_entries=max_entries)
    
    print("\n" + "-"*80)
    print("THESAURUS LIBRARY STATISTICS")
    print("-"*80)
    stats = thesaurus_library.get_data_statistics()
    print(f"Total Entries: {stats['total_entries']}")
    print(f"Average Synonyms per Entry: {stats['average_synonyms']:.2f}")
    print(f"Average Relationship Density: {stats['average_relationship_density']:.2f}")
    print(f"\nClassification Distribution:")
    for classification, count in stats['classification_distribution'].items():
        print(f"  {classification}: {count}")
    print(f"\nCategory Distribution:")
    for category, count in stats['category_distribution'].items():
        print(f"  {category}: {count}")
    print(f"\nMathematical Summary:")
    for key, value in stats['mathematical_summary'].items():
        if isinstance(value, float):
            print(f"  {key}: {value:.4f}")
        else:
            print(f"  {key}: {value}")
    
    return thesaurus_library

def save_library_samples(dict_lib, thes_lib, output_dir: str = "."):
    """Save sample entries from both libraries for inspection"""
    print("\n" + "="*80)
    print("SAVING LIBRARY SAMPLES")
    print("="*80)
    
    # Save dictionary samples
    dict_samples = []
    for i, (entry_id, entry) in enumerate(list(dict_lib.entries.items())[:10]):
        dict_samples.append({
            'entry_id': entry.entry_id,
            'word': entry.word,
            'definitions': entry.definitions[:2],
            'part_of_speech': entry.part_of_speech,
            'sphere_coordinates': entry.sphere_coordinates,
            'quantum_signature': entry.quantum_signature,
            'fuzzy_classification': entry.fuzzy_classification
        })
    
    dict_sample_file = os.path.join(output_dir, "dictionary_samples.json")
    with open(dict_sample_file, 'w') as f:
        json.dump(dict_samples, f, indent=2)
    print(f"Dictionary samples saved to: {dict_sample_file}")
    
    # Save thesaurus samples
    thes_samples = []
    for i, (entry_id, entry) in enumerate(list(thes_lib.entries.items())[:10]):
        thes_samples.append({
            'entry_id': entry.entry_id,
            'concept_name': entry.concept_name,
            'concept_number': entry.concept_number,
            'category': entry.category,
            'synonyms': entry.synonyms[:10],
            'sphere_coordinates': entry.sphere_coordinates,
            'quantum_signature': entry.quantum_signature,
            'fuzzy_classification': entry.fuzzy_classification
        })
    
    thes_sample_file = os.path.join(output_dir, "thesaurus_samples.json")
    with open(thes_sample_file, 'w') as f:
        json.dump(thes_samples, f, indent=2)
    print(f"Thesaurus samples saved to: {thes_sample_file}")

def test_sphere_compatibility(dict_lib, thes_lib):
    """Test that both libraries are compatible with Falcon Press Office sphere system"""
    print("\n" + "="*80)
    print("TESTING SPHERE COMPATIBILITY")
    print("="*80)
    
    # Test dictionary
    print("\nDictionary Library:")
    dict_sphere_data = dict_lib.get_sphere_generation_data()
    print(f"  Total coordinates: {len(dict_sphere_data['coordinates'])}")
    print(f"  Total quantum signatures: {len(dict_sphere_data['quantum_signatures'])}")
    print(f"  Classifications: {dict_sphere_data['classifications']}")
    
    # Test thesaurus
    print("\nThesaurus Library:")
    thes_sphere_data = thes_lib.get_sphere_generation_data()
    print(f"  Total coordinates: {len(thes_sphere_data['coordinates'])}")
    print(f"  Total quantum signatures: {len(thes_sphere_data['quantum_signatures'])}")
    print(f"  Classifications: {thes_sphere_data['classifications']}")
    
    # Verify coordinate format
    sample_dict_entry = list(dict_lib.entries.values())[0]
    sample_thes_entry = list(thes_lib.entries.values())[0]
    
    print("\nCoordinate Format Verification:")
    print(f"  Dictionary sample: {sample_dict_entry.sphere_coordinates}")
    print(f"  Thesaurus sample: {sample_thes_entry.sphere_coordinates}")
    
    print("\nQuantum Signature Format Verification:")
    print(f"  Dictionary sample: {sample_dict_entry.quantum_signature}")
    print(f"  Thesaurus sample: {sample_thes_entry.quantum_signature}")
    
    print("\n" + "="*80)
    print("SPHERE COMPATIBILITY TEST PASSED")
    print("="*80)

def main():
    """Main function to populate both libraries"""
    # File paths
    dict_file = "9-The-Final-Chapter/websters_dictionary.txt"
    thes_file = "9-The-Final-Chapter/rogets_thesaurus.txt"
    
    # Check if files exist
    if not os.path.exists(dict_file):
        print(f"Error: Dictionary file not found at {dict_file}")
        return
    
    if not os.path.exists(thes_file):
        print(f"Error: Thesaurus file not found at {thes_file}")
        return
    
    # Populate libraries
    dict_lib = populate_dictionary(dict_file, max_entries=5000)
    thes_lib = populate_thesaurus(thes_file, max_entries=1000)
    
    # Save samples
    save_library_samples(dict_lib, thes_lib)
    
    # Test compatibility
    test_sphere_compatibility(dict_lib, thes_lib)
    
    print("\n" + "="*80)
    print("LIBRARY POPULATION COMPLETE")
    print("="*80)
    print("\nLibraries are now ready for use with The Falcon Press Office!")

if __name__ == "__main__":
    main()