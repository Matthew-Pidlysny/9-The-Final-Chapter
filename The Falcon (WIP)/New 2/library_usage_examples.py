"""
Usage Examples for Webster's Dictionary and Roget's Thesaurus Libraries
Demonstrates various ways to use the linguistic libraries with The Falcon Press Office
"""

from websters_dictionary_library import dictionary_library
from rogets_thesaurus_library import thesaurus_library
import json

def example_1_basic_dictionary_lookup():
    """Example 1: Basic dictionary word lookup"""
    print("\n" + "="*80)
    print("EXAMPLE 1: Basic Dictionary Lookup")
    print("="*80)
    
    # Look up a word
    word = "algorithm"
    entry = dictionary_library.get_entry_by_word(word)
    
    if entry:
        print(f"\nWord: {entry.word}")
        print(f"Part of Speech: {', '.join(entry.part_of_speech)}")
        print(f"\nDefinitions:")
        for i, defn in enumerate(entry.definitions, 1):
            print(f"  {i}. {defn}")
        print(f"\nEtymology: {entry.etymology}")
        print(f"Complexity Score: {entry.complexity_score:.2f}")
        print(f"Classification: {entry.fuzzy_classification}")
        print(f"Sphere Coordinates: {entry.sphere_coordinates}")
        print(f"Quantum Signature: {entry.quantum_signature}")
    else:
        print(f"Word '{word}' not found in dictionary")

def example_2_find_complex_words():
    """Example 2: Find complex words in the dictionary"""
    print("\n" + "="*80)
    print("EXAMPLE 2: Find Complex Words")
    print("="*80)
    
    complex_words = dictionary_library.get_complex_words()
    
    print(f"\nFound {len(complex_words)} complex words")
    print("\nSample complex words:")
    for entry in complex_words[:10]:
        print(f"  - {entry.word} (complexity: {entry.complexity_score:.2f}, length: {entry.word_length})")

def example_3_classification_analysis():
    """Example 3: Analyze words by classification"""
    print("\n" + "="*80)
    print("EXAMPLE 3: Classification Analysis")
    print("="*80)
    
    classifications = ["Simple", "Standard", "Advanced", "Complex"]
    
    for classification in classifications:
        entries = dictionary_library.get_entries_by_classification(classification)
        print(f"\n{classification} words: {len(entries)}")
        if entries:
            sample_words = [e.word for e in entries[:5]]
            print(f"  Sample: {', '.join(sample_words)}")

def example_4_thesaurus_synonyms():
    """Example 4: Find synonyms using thesaurus"""
    print("\n" + "="*80)
    print("EXAMPLE 4: Find Synonyms")
    print("="*80)
    
    words = ["happy", "sad", "big", "small"]
    
    for word in words:
        synonyms = thesaurus_library.find_synonyms(word)
        if synonyms:
            print(f"\nSynonyms for '{word}':")
            print(f"  {', '.join(synonyms[:15])}")
        else:
            print(f"\nNo synonyms found for '{word}'")

def example_5_thesaurus_antonyms():
    """Example 5: Find antonyms using thesaurus"""
    print("\n" + "="*80)
    print("EXAMPLE 5: Find Antonyms")
    print("="*80)
    
    words = ["good", "light", "hot", "fast"]
    
    for word in words:
        antonyms = thesaurus_library.find_antonyms(word)
        if antonyms:
            print(f"\nAntonyms for '{word}':")
            print(f"  {', '.join(antonyms[:10])}")
        else:
            print(f"\nNo antonyms found for '{word}'")

def example_6_semantic_categories():
    """Example 6: Explore semantic categories"""
    print("\n" + "="*80)
    print("EXAMPLE 6: Semantic Categories")
    print("="*80)
    
    categories = ["Abstract Relations", "Space", "Matter", "Intellect", "Volition", "Affections"]
    
    for category in categories:
        entries = thesaurus_library.get_entries_by_category(category)
        if entries:
            print(f"\n{category}: {len(entries)} concepts")
            sample_concepts = [e.concept_name for e in entries[:5]]
            print(f"  Sample: {', '.join(sample_concepts)}")

def example_7_rich_concepts():
    """Example 7: Find semantically rich concepts"""
    print("\n" + "="*80)
    print("EXAMPLE 7: Semantically Rich Concepts")
    print("="*80)
    
    rich_concepts = thesaurus_library.get_rich_concepts()
    
    print(f"\nFound {len(rich_concepts)} rich concepts (high relationship density)")
    print("\nTop 10 richest concepts:")
    
    # Sort by relationship density
    sorted_concepts = sorted(rich_concepts, key=lambda x: x.relationship_density, reverse=True)
    
    for entry in sorted_concepts[:10]:
        print(f"  - {entry.concept_name}")
        print(f"    Density: {entry.relationship_density:.2f}, Synonyms: {len(entry.synonyms)}")

def example_8_sphere_data_extraction():
    """Example 8: Extract sphere generation data"""
    print("\n" + "="*80)
    print("EXAMPLE 8: Sphere Generation Data")
    print("="*80)
    
    # Dictionary sphere data
    dict_data = dictionary_library.get_sphere_generation_data()
    print("\nDictionary Sphere Data:")
    print(f"  Total Coordinates: {len(dict_data['coordinates'])}")
    print(f"  Total Quantum Signatures: {len(dict_data['quantum_signatures'])}")
    print(f"  Classifications: {dict_data['classifications']}")
    print(f"  Parts of Speech: {dict_data['parts_of_speech']}")
    
    # Thesaurus sphere data
    thes_data = thesaurus_library.get_sphere_generation_data()
    print("\nThesaurus Sphere Data:")
    print(f"  Total Coordinates: {len(thes_data['coordinates'])}")
    print(f"  Total Quantum Signatures: {len(thes_data['quantum_signatures'])}")
    print(f"  Classifications: {thes_data['classifications']}")
    print(f"  Categories: {thes_data['categories']}")

def example_9_mathematical_properties():
    """Example 9: Examine mathematical properties"""
    print("\n" + "="*80)
    print("EXAMPLE 9: Mathematical Properties")
    print("="*80)
    
    # Get a sample dictionary entry
    sample_dict = list(dictionary_library.entries.values())[0]
    print("\nDictionary Entry Mathematical Properties:")
    print(f"  Word: {sample_dict.word}")
    for key, value in sample_dict.mathematical_properties.items():
        if isinstance(value, float):
            print(f"  {key}: {value:.4f}")
        elif isinstance(value, list):
            print(f"  {key}: {[f'{v:.2f}' for v in value]}")
        else:
            print(f"  {key}: {value}")
    
    # Get a sample thesaurus entry
    sample_thes = list(thesaurus_library.entries.values())[0]
    print("\nThesaurus Entry Mathematical Properties:")
    print(f"  Concept: {sample_thes.concept_name}")
    for key, value in sample_thes.mathematical_properties.items():
        if isinstance(value, float):
            print(f"  {key}: {value:.4f}")
        elif isinstance(value, list):
            print(f"  {key}: {[f'{v:.2f}' for v in value]}")
        else:
            print(f"  {key}: {value}")

def example_10_combined_analysis():
    """Example 10: Combined dictionary and thesaurus analysis"""
    print("\n" + "="*80)
    print("EXAMPLE 10: Combined Analysis")
    print("="*80)
    
    word = "happy"
    
    # Dictionary lookup
    dict_entry = dictionary_library.get_entry_by_word(word)
    if dict_entry:
        print(f"\nDictionary Entry for '{word}':")
        print(f"  Definitions: {len(dict_entry.definitions)}")
        print(f"  Complexity: {dict_entry.complexity_score:.2f}")
        print(f"  Classification: {dict_entry.fuzzy_classification}")
    
    # Thesaurus lookup
    synonyms = thesaurus_library.find_synonyms(word)
    antonyms = thesaurus_library.find_antonyms(word)
    
    print(f"\nThesaurus Data for '{word}':")
    print(f"  Synonyms found: {len(synonyms)}")
    if synonyms:
        print(f"  Sample synonyms: {', '.join(synonyms[:10])}")
    print(f"  Antonyms found: {len(antonyms)}")
    if antonyms:
        print(f"  Sample antonyms: {', '.join(antonyms[:10])}")

def example_11_statistics():
    """Example 11: Library statistics"""
    print("\n" + "="*80)
    print("EXAMPLE 11: Library Statistics")
    print("="*80)
    
    # Dictionary statistics
    dict_stats = dictionary_library.get_data_statistics()
    print("\nDictionary Statistics:")
    print(f"  Total Entries: {dict_stats['total_entries']}")
    print(f"  Average Word Length: {dict_stats['average_word_length']:.2f}")
    print(f"  Average Complexity: {dict_stats['average_complexity']:.2f}")
    print(f"  Classification Distribution:")
    for classification, count in dict_stats['classification_distribution'].items():
        percentage = (count / dict_stats['total_entries']) * 100
        print(f"    {classification}: {count} ({percentage:.1f}%)")
    
    # Thesaurus statistics
    thes_stats = thesaurus_library.get_data_statistics()
    print("\nThesaurus Statistics:")
    print(f"  Total Entries: {thes_stats['total_entries']}")
    print(f"  Average Synonyms: {thes_stats['average_synonyms']:.2f}")
    print(f"  Average Relationship Density: {thes_stats['average_relationship_density']:.2f}")
    print(f"  Classification Distribution:")
    for classification, count in thes_stats['classification_distribution'].items():
        percentage = (count / thes_stats['total_entries']) * 100
        print(f"    {classification}: {count} ({percentage:.1f}%)")

def example_12_export_sample_data():
    """Example 12: Export sample data for inspection"""
    print("\n" + "="*80)
    print("EXAMPLE 12: Export Sample Data")
    print("="*80)
    
    # Export dictionary samples
    dict_samples = []
    for entry in list(dictionary_library.entries.values())[:5]:
        dict_samples.append({
            'word': entry.word,
            'definitions': entry.definitions,
            'complexity': entry.complexity_score,
            'classification': entry.fuzzy_classification,
            'sphere_coordinates': entry.sphere_coordinates,
            'quantum_signature': entry.quantum_signature
        })
    
    with open('dict_export_sample.json', 'w') as f:
        json.dump(dict_samples, f, indent=2)
    print("\nDictionary samples exported to: dict_export_sample.json")
    
    # Export thesaurus samples
    thes_samples = []
    for entry in list(thesaurus_library.entries.values())[:5]:
        thes_samples.append({
            'concept': entry.concept_name,
            'category': entry.category,
            'synonyms': entry.synonyms[:20],
            'relationship_density': entry.relationship_density,
            'classification': entry.fuzzy_classification,
            'sphere_coordinates': entry.sphere_coordinates,
            'quantum_signature': entry.quantum_signature
        })
    
    with open('thes_export_sample.json', 'w') as f:
        json.dump(thes_samples, f, indent=2)
    print("Thesaurus samples exported to: thes_export_sample.json")

def run_all_examples():
    """Run all examples"""
    print("\n" + "#"*80)
    print("# WEBSTER'S DICTIONARY & ROGET'S THESAURUS LIBRARY USAGE EXAMPLES")
    print("#"*80)
    
    example_1_basic_dictionary_lookup()
    example_2_find_complex_words()
    example_3_classification_analysis()
    example_4_thesaurus_synonyms()
    example_5_thesaurus_antonyms()
    example_6_semantic_categories()
    example_7_rich_concepts()
    example_8_sphere_data_extraction()
    example_9_mathematical_properties()
    example_10_combined_analysis()
    example_11_statistics()
    example_12_export_sample_data()
    
    print("\n" + "#"*80)
    print("# ALL EXAMPLES COMPLETED")
    print("#"*80)

if __name__ == "__main__":
    run_all_examples()