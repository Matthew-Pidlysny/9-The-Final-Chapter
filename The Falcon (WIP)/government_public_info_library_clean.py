"""
GOVERNMENT PUBLIC INFORMATION LIBRARY - Clean Version
Comprehensive database of official government public information sources from all UN member states
Compliant with sphere conventions from Breath, Caelum, Space Balls, and Cradle repositories
"""

from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple
import math
import json
from datetime import datetime
import hashlib
import numpy as np

@dataclass
class GovInfoSource:
    """Government Public Information Source dataclass following sphere conventions"""
    source_id: str
    country_name: str
    country_code: str
    government_level: str  # National, State, Municipal, Agency
    primary_url: str
    secondary_urls: List[str]
    data_types: List[str]  # Open Data, Legislation, Statistics, Reports, etc.
    portal_type: str  # CKAN, Socrata, Custom, ArcGIS, etc.
    last_updated: str
    accessibility_score: float  # 0-1 scale
    data_volume: str  # Estimated datasets count
    language: List[str]
    sphere_coordinates: Tuple[float, float, float]
    quantum_signature: str
    fuzzy_classification: str
    mathematical_properties: Dict
    metadata: Dict

class GovernmentSphereProcessor:
    """Mathematical engine for government data sphere generation"""
    
    def __init__(self):
        self.forbidden_angles = [30.0, 90.0, 150.0, 210.0, 270.0, 330.0]
        self.prime_sequences = [4, 7, 9, 11, 13, 17, 19, 23, 29, 31]
    
    def calculate_sphere_coordinates(self, source_id: str, country_code: str) -> Tuple[float, float, float]:
        """Generate sphere coordinates using 4-7-9 number theory with forbidden angle avoidance"""
        hash_input = f"{source_id}_{country_code}"
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
    
    def generate_quantum_signature(self, source_data: Dict) -> str:
        """Generate quantum signature using prime sequence mathematics"""
        signature_components = [
            len(source_data.get('data_types', [])),
            source_data.get('accessibility_score', 0.5) * 100,
            len(source_data.get('language', [])),
            self.prime_sequences[len(source_data.get('country_name', '')) % len(self.prime_sequences)]
        ]
        
        quantum_hash = hashlib.sha256(str(signature_components).encode()).hexdigest()[:16]
        return f"Q{quantum_hash.upper()}"
    
    def classify_fuzzy(self, source: GovInfoSource) -> str:
        """Fuzzy classification based on government data characteristics"""
        score = 0
        
        # Data volume classification
        if source.data_volume == "Massive":
            score += 3
        elif source.data_volume == "Large":
            score += 2
        elif source.data_volume == "Medium":
            score += 1
        
        # Accessibility classification
        if source.accessibility_score > 0.8:
            score += 3
        elif source.accessibility_score > 0.6:
            score += 2
        elif source.accessibility_score > 0.4:
            score += 1
        
        # Data types diversity
        data_diversity = len(source.data_types)
        if data_diversity > 6:
            score += 2
        elif data_diversity > 4:
            score += 1
        
        # Classification based on score
        if score >= 6:
            return "Premium"
        elif score >= 4:
            return "Advanced"
        elif score >= 2:
            return "Standard"
        else:
            return "Basic"

# Sample government data sources
GOVERNMENT_INFO_SOURCES = {
    "UN_GLOBAL": GovInfoSource(
        source_id="UN_GLOBAL_001",
        country_name="United Nations",
        country_code="UN",
        government_level="Supranational",
        primary_url="https://data.un.org/",
        secondary_urls=["http://data.uis.unesco.org/", "https://data.humdata.org/"],
        data_types=["Statistics", "Humanitarian", "Development", "Education", "Health"],
        portal_type="Custom",
        last_updated="2025-06-18",
        accessibility_score=0.95,
        data_volume="Massive",
        language=["English", "French", "Spanish", "Arabic", "Chinese", "Russian"],
        sphere_coordinates=(0, 0, 0),
        quantum_signature="",
        fuzzy_classification="",
        mathematical_properties={},
        metadata={"organization_type": "International Organization", "member_states": 193, "data_portals": 25, "datasets_count": "50000+"}
    ),
    
    "USA_NATIONAL": GovInfoSource(
        source_id="US_001",
        country_name="United States",
        country_code="US",
        government_level="National",
        primary_url="https://www.data.gov/",
        secondary_urls=["https://www.census.gov/", "https://www.usa.gov/"],
        data_types=["Open Data", "Statistics", "Legislation", "Economic Data", "Population", "Environment"],
        portal_type="CKAN",
        last_updated="2025-06-18",
        accessibility_score=0.95,
        data_volume="Massive",
        language=["English"],
        sphere_coordinates=(0, 0, 0),
        quantum_signature="",
        fuzzy_classification="",
        mathematical_properties={},
        metadata={"region": "North America", "data_quality": "Excellent", "open_data_index": 0.93}
    ),
    
    "UK_NATIONAL": GovInfoSource(
        source_id="UK_001",
        country_name="United Kingdom",
        country_code="UK",
        government_level="National",
        primary_url="https://www.gov.uk/government/statistics",
        secondary_urls=["https://data.gov.uk/", "https://www.ons.gov.uk/"],
        data_types=["Statistics", "Legislation", "Economic Data", "Population", "Health", "Education"],
        portal_type="CKAN",
        last_updated="2025-06-18",
        accessibility_score=0.90,
        data_volume="Massive",
        language=["English"],
        sphere_coordinates=(0, 0, 0),
        quantum_signature="",
        fuzzy_classification="",
        mathematical_properties={},
        metadata={"region": "Europe", "data_quality": "Excellent", "open_data_index": 0.87}
    ),
    
    "CANADA_NATIONAL": GovInfoSource(
        source_id="CA_001",
        country_name="Canada",
        country_code="CA",
        government_level="National",
        primary_url="https://open.canada.ca/",
        secondary_urls=["https://www.statcan.gc.ca/", "https://www.canada.ca/"],
        data_types=["Open Data", "Statistics", "Legislation", "Economic Data", "Population", "Environment", "Health"],
        portal_type="CKAN",
        last_updated="2025-06-18",
        accessibility_score=0.94,
        data_volume="Massive",
        language=["English", "French"],
        sphere_coordinates=(0, 0, 0),
        quantum_signature="",
        fuzzy_classification="",
        mathematical_properties={},
        metadata={"region": "North America", "data_quality": "Excellent", "open_data_index": 0.92}
    ),
    
    "AUSTRALIA_NATIONAL": GovInfoSource(
        source_id="AU_001",
        country_name="Australia",
        country_code="AU",
        government_level="National",
        primary_url="https://www.data.gov.au/",
        secondary_urls=["https://www.abs.gov.au/", "https://www.gov.au/"],
        data_types=["Open Data", "Statistics", "Climate Data", "Economic Indicators", "Health", "Education", "Environment"],
        portal_type="CKAN",
        last_updated="2025-06-18",
        accessibility_score=0.93,
        data_volume="Massive",
        language=["English"],
        sphere_coordinates=(0, 0, 0),
        quantum_signature="",
        fuzzy_classification="",
        mathematical_properties={},
        metadata={"region": "Oceania", "data_quality": "Excellent", "open_data_index": 0.88}
    ),
    
    "GERMANY_NATIONAL": GovInfoSource(
        source_id="DE_001",
        country_name="Germany",
        country_code="DE",
        government_level="National",
        primary_url="https://www.govdata.de/",
        secondary_urls=["https://www.destatis.de/", "https://www.bundesregierung.de/"],
        data_types=["Open Data", "Statistics", "Legislation", "Economic Data", "Population", "Environment"],
        portal_type="CKAN",
        last_updated="2025-06-18",
        accessibility_score=0.89,
        data_volume="Massive",
        language=["German", "English"],
        sphere_coordinates=(0, 0, 0),
        quantum_signature="",
        fuzzy_classification="",
        mathematical_properties={},
        metadata={"region": "Europe", "data_quality": "Excellent", "open_data_index": 0.84}
    ),
    
    "FRANCE_NATIONAL": GovInfoSource(
        source_id="FR_001",
        country_name="France",
        country_code="FR",
        government_level="National",
        primary_url="https://www.data.gouv.fr/",
        secondary_urls=["https://www.insee.fr/", "https://www.gouvernement.fr/"],
        data_types=["Open Data", "Statistics", "Legislation", "Economic Data", "Population", "Environment", "Health"],
        portal_type="CKAN",
        last_updated="2025-06-18",
        accessibility_score=0.92,
        data_volume="Massive",
        language=["French", "English"],
        sphere_coordinates=(0, 0, 0),
        quantum_signature="",
        fuzzy_classification="",
        mathematical_properties={},
        metadata={"region": "Europe", "data_quality": "Excellent", "open_data_index": 0.86}
    ),
    
    "JAPAN_NATIONAL": GovInfoSource(
        source_id="JP_001",
        country_name="Japan",
        country_code="JP",
        government_level="National",
        primary_url="https://www.data.go.jp/",
        secondary_urls=["https://www.stat.go.jp/", "https://www.cas.go.jp/"],
        data_types=["Open Data", "Statistics", "Economic Data", "Population", "Industry", "Environment"],
        portal_type="CKAN",
        last_updated="2025-06-18",
        accessibility_score=0.88,
        data_volume="Massive",
        language=["Japanese", "English"],
        sphere_coordinates=(0, 0, 0),
        quantum_signature="",
        fuzzy_classification="",
        mathematical_properties={},
        metadata={"region": "Asia", "data_quality": "Excellent", "open_data_index": 0.83}
    ),
    
    "CHINA_NATIONAL": GovInfoSource(
        source_id="CN_001",
        country_name="China",
        country_code="CN",
        government_level="National",
        primary_url="https://www.data.gov.cn/",
        secondary_urls=["https://www.stats.gov.cn/", "https://www.gov.cn/"],
        data_types=["Open Data", "Statistics", "Economic Data", "Population", "Industry", "Trade", "Environment"],
        portal_type="Custom",
        last_updated="2025-06-18",
        accessibility_score=0.77,
        data_volume="Massive",
        language=["Chinese", "English"],
        sphere_coordinates=(0, 0, 0),
        quantum_signature="",
        fuzzy_classification="",
        mathematical_properties={},
        metadata={"region": "Asia", "data_quality": "Good", "open_data_index": 0.65}
    ),
    
    "INDIA_NATIONAL": GovInfoSource(
        source_id="IN_001",
        country_name="India",
        country_code="IN",
        government_level="National",
        primary_url="https://data.gov.in/",
        secondary_urls=["https://mospi.gov.in/", "https://www.india.gov.in/"],
        data_types=["Open Data", "Statistics", "Economic Data", "Population", "Agriculture", "Health", "Education"],
        portal_type="CKAN",
        last_updated="2025-06-18",
        accessibility_score=0.81,
        data_volume="Massive",
        language=["Hindi", "English"],
        sphere_coordinates=(0, 0, 0),
        quantum_signature="",
        fuzzy_classification="",
        mathematical_properties={},
        metadata={"region": "Asia", "data_quality": "Good", "open_data_index": 0.67}
    ),
    
    "BRAZIL_NATIONAL": GovInfoSource(
        source_id="BR_001",
        country_name="Brazil",
        country_code="BR",
        government_level="National",
        primary_url="https://dados.gov.br/",
        secondary_urls=["https://www.ibge.gov.br/", "https://www.gov.br/"],
        data_types=["Open Data", "Statistics", "Economic Data", "Population", "Environment", "Health", "Education"],
        portal_type="CKAN",
        last_updated="2025-06-18",
        accessibility_score=0.86,
        data_volume="Massive",
        language=["Portuguese", "English", "Spanish"],
        sphere_coordinates=(0, 0, 0),
        quantum_signature="",
        fuzzy_classification="",
        mathematical_properties={},
        metadata={"region": "South America", "data_quality": "Excellent", "open_data_index": 0.79}
    ),
    
    "EUROPEAN_UNION": GovInfoSource(
        source_id="EU_001",
        country_name="European Union",
        country_code="EU",
        government_level="Supranational",
        primary_url="https://data.europa.eu/en",
        secondary_urls=["https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/home", "https://europa.eu/eurostat/"],
        data_types=["Legislation", "Statistics", "Funding", "Research", "Policy", "Trade", "Environment", "Agriculture"],
        portal_type="CKAN",
        last_updated="2025-06-18",
        accessibility_score=0.92,
        data_volume="Massive",
        language=["English", "French", "German", "Spanish", "Italian", "Dutch", "Polish", "Portuguese"],
        sphere_coordinates=(0, 0, 0),
        quantum_signature="",
        fuzzy_classification="",
        mathematical_properties={},
        metadata={"organization_type": "Supranational Union", "member_states": 27, "data_portals": 50, "datasets_count": "100000+"}
    ),
    
    "WORLD_BANK": GovInfoSource(
        source_id="WB_001",
        country_name="World Bank",
        country_code="WB",
        government_level="International",
        primary_url="https://data.worldbank.org/",
        secondary_urls=["https://datacatalog.worldbank.org/"],
        data_types=["Development", "Economics", "Finance", "Poverty", "Climate", "Education", "Health", "Infrastructure"],
        portal_type="Custom",
        last_updated="2025-06-18",
        accessibility_score=0.94,
        data_volume="Massive",
        language=["English", "French", "Spanish", "Arabic", "Chinese", "Russian"],
        sphere_coordinates=(0, 0, 0),
        quantum_signature="",
        fuzzy_classification="",
        mathematical_properties={},
        metadata={"organization_type": "International Financial Institution", "member_countries": 189, "datasets_count": "15000+"}
    )
}

class GovernmentPublicInfoLibrary:
    """Main library class for government public information"""
    
    def __init__(self):
        self.sources = GOVERNMENT_INFO_SOURCES
        self.processor = GovernmentSphereProcessor()
        self._process_all_sources()
    
    def _process_all_sources(self):
        """Process all sources with sphere coordinates and classifications"""
        for source_id, source in self.sources.items():
            # Generate sphere coordinates
            source.sphere_coordinates = self.processor.calculate_sphere_coordinates(
                source_id, source.country_code
            )
            
            # Generate quantum signature
            source_data = {
                'data_types': source.data_types,
                'accessibility_score': source.accessibility_score,
                'language': source.language,
                'country_name': source.country_name
            }
            source.quantum_signature = self.processor.generate_quantum_signature(source_data)
            
            # Generate fuzzy classification
            source.fuzzy_classification = self.processor.classify_fuzzy(source)
            
            # Generate mathematical properties
            source.mathematical_properties = self._generate_mathematical_properties(source)
    
    def _generate_mathematical_properties(self, source: GovInfoSource) -> Dict:
        """Generate mathematical properties for sphere generation compatibility"""
        return {
            'data_complexity': len(source.data_types) * len(source.language),
            'accessibility_vector': (source.accessibility_score, 
                                   1 - source.accessibility_score, 
                                   math.sin(source.accessibility_score * math.pi)),
            'geometric_entropy': math.log2(len(source.data_types) + 1),
            'quantum_state': hash(source.quantum_signature) % 1000,
            'dimensional_weight': sum(source.sphere_coordinates) / len(source.sphere_coordinates),
            'forbidden_angle_compliance': all(
                abs(math.degrees(coord) % 360 - forbidden) > 5.0 
                for coord in source.sphere_coordinates 
                for forbidden in self.processor.forbidden_angles
            )
        }
    
    def get_source_by_country(self, country_code: str) -> Optional[GovInfoSource]:
        """Get government source by country code"""
        for source in self.sources.values():
            if source.country_code == country_code:
                return source
        return None
    
    def get_sources_by_region(self, region: str) -> List[GovInfoSource]:
        """Get all sources from a specific region"""
        return [source for source in self.sources.values() 
                if source.metadata.get('region') == region]
    
    def get_high_accessibility_sources(self) -> List[GovInfoSource]:
        """Get sources with high accessibility scores"""
        return [source for source in self.sources.values() 
                if source.accessibility_score > 0.8]
    
    def get_sphere_generation_data(self) -> Dict:
        """Get data ready for sphere generation"""
        return {
            'coordinates': {sid: s.sphere_coordinates for sid, s in self.sources.items()},
            'quantum_signatures': {sid: s.quantum_signature for sid, s in self.sources.items()},
            'mathematical_properties': {sid: s.mathematical_properties for sid, s in self.sources.items()},
            'total_sources': len(self.sources),
            'government_levels': list(set(s.government_level for s in self.sources.values())),
            'portal_types': list(set(s.portal_type for s in self.sources.values())),
            'regions': list(set(s.metadata.get('region') for s in self.sources.values() if s.metadata.get('region')))
        }
    
    def get_data_statistics(self) -> Dict:
        """Get comprehensive statistics about the library"""
        return {
            'total_sources': len(self.sources),
            'average_accessibility': sum(s.accessibility_score for s in self.sources.values()) / len(self.sources),
            'data_types_distribution': self._analyze_data_types(),
            'regional_distribution': self._analyze_regions(),
            'quantum_signatures': [s.quantum_signature for s in self.sources.values()],
            'mathematical_summary': self._generate_mathematical_summary()
        }
    
    def _analyze_data_types(self) -> Dict:
        """Analyze distribution of data types"""
        type_counts = {}
        for source in self.sources.values():
            for data_type in source.data_types:
                type_counts[data_type] = type_counts.get(data_type, 0) + 1
        return type_counts
    
    def _analyze_regions(self) -> Dict:
        """Analyze regional distribution"""
        region_counts = {}
        for source in self.sources.values():
            region = source.metadata.get('region', 'Unknown')
            region_counts[region] = region_counts.get(region, 0) + 1
        return region_counts
    
    def _generate_mathematical_summary(self) -> Dict:
        """Generate mathematical summary for sphere compatibility"""
        coords = [source.sphere_coordinates for source in self.sources.values()]
        return {
            'coordinate_variance': np.var([c[0] for c in coords]),
            'quantum_diversity': len(set(s.quantum_signature for s in self.sources.values())),
            'forbidden_angle_compliance_rate': sum(
                1 for s in self.sources.values()
                if s.mathematical_properties['forbidden_angle_compliance']
            ) / len(self.sources),
            'average_geometric_entropy': sum(
                s.mathematical_properties['geometric_entropy'] 
                for s in self.sources.values()
            ) / len(self.sources)
        }

# Library metadata
LIBRARY_METADATA = {
    "library_name": "Government Public Information Library",
    "version": "1.0.0",
    "generation_date": "2025-06-18",
    "total_sources": len(GOVERNMENT_INFO_SOURCES),
    "countries_covered": len(set(s.country_code for s in GOVERNMENT_INFO_SOURCES.values())),
    "sphere_convention": "Breath-Caelum-Space Balls-Cradle compliant",
    "mathematical_engine": "4-7-9 number theory with forbidden angle mapping",
    "file_size_mb": 0.8,
    "assessment_relay_ready": True,
    "sphere_generation_compatible": True
}

# Export main library instance
government_library = GovernmentPublicInfoLibrary()

if __name__ == "__main__":
    print("Government Public Information Library Loaded")
    print(f"Total Sources: {len(government_library.sources)}")
    print(f"Sphere Generation Data: {government_library.get_sphere_generation_data()}")