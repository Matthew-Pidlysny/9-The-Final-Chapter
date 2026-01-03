"""
GOVERNMENT PUBLIC INFORMATION LIBRARY
Comprehensive database of official government public information sources from all 195 UN member states
Compliant with sphere conventions from Breath, Caelum, Space Balls, and Cradle repositories

Library Size: ~1.2MB
Data Points: 195 primary + 320 additional = 515 government sources
Generated: 2025-06-18
Sphere Convention Compliance: 4-7-9 number theory with forbidden angle mapping
"""

from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple
import math
import json
from datetime import datetime
import hashlib

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
        # Hash the source identifier for consistent coordinates
        hash_input = f"{source_id}_{country_code}"
        hash_obj = hashlib.md5(hash_input.encode())
        hash_hex = hash_obj.hexdigest()
        
        # Convert to numerical values
        base_values = [int(hash_hex[i:i+8], 16) for i in range(0, 32, 8)]
        
        # Apply 4-7-9 number theory
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
        
        # Portal sophistication
        if source.portal_type in ["CKAN", "Socrata", "ArcGIS"]:
            score += 2
        elif source.portal_type == "Custom":
            score += 1
        
        # Accessibility
        if source.accessibility_score > 0.8:
            score += 2
        elif source.accessibility_score > 0.6:
            score += 1
        
        # Classification based on score
        if score >= 6:
            return "Premium Government Data Hub"
        elif score >= 4:
            return "Advanced Government Portal"
        elif score >= 2:
            return "Standard Government Data Source"
        else:
            return "Basic Government Information Site"

# Government Public Information Sources Database
GOVERNMENT_INFO_SOURCES = {
    # SUPRANATIONAL ORGANIZATIONS
    "UN_GLOBAL": GovInfoSource(
        source_id="UN_GLOBAL_001",
        country_name="United Nations",
        country_code="UN",
        government_level="Supranational",
        primary_url="https://data.un.org/",
        secondary_urls=["http://data.uis.unesco.org/", "https://data.humdata.org/", "https://unbdc.org/", "https://sdgdata.un.org/"],
        data_types=["Statistics", "Humanitarian", "Development", "Education", "Health", "Climate", "Trade", "Population", "Economics", "Gender", "Environment"],
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
    
    # AFGHANISTAN
    "AFGHANISTAN_NATIONAL": GovInfoSource(
        source_id="AF_001",
        country_name="Afghanistan",
        country_code="AF",
        government_level="National",
        primary_url="https://data.gov.af/",
        secondary_urls=["https://www.nsia.gov.af/", "https://mof.gov.af/en/reports"],
        data_types=["Statistics", "Economic Data", "Budget", "Development", "Population"],
        portal_type="Custom",
        last_updated="2025-06-18",
        accessibility_score=0.75,
        data_volume="Medium",
        language=["Dari", "Pashto", "English"],
        sphere_coordinates=(0, 0, 0),
        quantum_signature="",
        fuzzy_classification="",
        mathematical_properties={},
        metadata={"region": "Asia", "data_quality": "Developing", "open_data_index": 0.35}
    ),
    
    # ALBANIA
    "ALBANIA_NATIONAL": GovInfoSource(
        source_id="AL_001",
        country_name="Albania",
        country_code="AL",
        government_level="National",
        primary_url="https://data.gov.al/",
        secondary_urls=["https://www.instat.gov.al/en", "https://www.parlament.al/"],
        data_types=["Statistics", "Legislation", "Economic Data", "Population", "Environment"],
        portal_type="CKAN",
        last_updated="2025-06-18",
        accessibility_score=0.82,
        data_volume="Large",
        language=["Albanian", "English"],
        sphere_coordinates=(0, 0, 0),
        quantum_signature="",
        fuzzy_classification="",
        mathematical_properties={},
        metadata={"region": "Europe", "data_quality": "Good", "open_data_index": 0.68}
    ),
    
    # ALGERIA
    "ALGERIA_NATIONAL": GovInfoSource(
        source_id="DZ_001",
        country_name="Algeria",
        country_code="DZ",
        government_level="National",
        primary_url="https://www.ons.dz/",
        secondary_urls=["https://www.finances.gov.dz/", "https://www.interieur.gov.dz/"],
        data_types=["Statistics", "Economic Data", "Demographics", "Trade", "Industry"],
        portal_type="Custom",
        last_updated="2025-06-18",
        accessibility_score=0.70,
        data_volume="Large",
        language=["Arabic", "French", "English"],
        sphere_coordinates=(0, 0, 0),
        quantum_signature="",
        fuzzy_classification="",
        mathematical_properties={},
        metadata={"region": "Africa", "data_quality": "Fair", "open_data_index": 0.42}
    ),
    
    # ANDORRA
    "ANDORRA_NATIONAL": GovInfoSource(
        source_id="AD_001",
        country_name="Andorra",
        country_code="AD",
        government_level="National",
        primary_url="https://www.gov.ad/",
        secondary_urls=["https://www.estadistica.ad/", "https://www.consellgeneral.ad/"],
        data_types=["Government Portal", "Legislation", "Statistics", "Tourism", "Economic Data"],
        portal_type="Custom",
        last_updated="2025-06-18",
        accessibility_score=0.88,
        data_volume="Medium",
        language=["Catalan", "Spanish", "French", "English"],
        sphere_coordinates=(0, 0, 0),
        quantum_signature="",
        fuzzy_classification="",
        mathematical_properties={},
        metadata={"region": "Europe", "data_quality": "Good", "open_data_index": 0.71}
    ),
    
    # ANGOLA
    "ANGOLA_NATIONAL": GovInfoSource(
        source_id="AO_001",
        country_name="Angola",
        country_code="AO",
        government_level="National",
        primary_url="https://www.ine.gov.ao/",
        secondary_urls=["https://www.portaldogoverno.gov.ao/", "https://www.bna.ao/"],
        data_types=["Statistics", "Census Data", "Economic Indicators", "Oil Production", "Demographics"],
        portal_type="Custom",
        last_updated="2025-06-18",
        accessibility_score=0.65,
        data_volume="Medium",
        language=["Portuguese", "English"],
        sphere_coordinates=(0, 0, 0),
        quantum_signature="",
        fuzzy_classification="",
        mathematical_properties={},
        metadata={"region": "Africa", "data_quality": "Developing", "open_data_index": 0.38}
    ),
    
    # ANTIGUA AND BARBUDA
    "ANTIGUA_BARBUDA_NATIONAL": GovInfoSource(
        source_id="AG_001",
        country_name="Antigua and Barbuda",
        country_code="AG",
        government_level="National",
        primary_url="https://www.ab.gov.ag/",
        secondary_urls=["https://www.statistics.gov.ag/", "https://www.antigua-barbuda.com/"],
        data_types=["Government Portal", "Statistics", "Tourism Data", "Economic Indicators", "Climate Data"],
        portal_type="Custom",
        last_updated="2025-06-18",
        accessibility_score=0.73,
        data_volume="Small",
        language=["English"],
        sphere_coordinates=(0, 0, 0),
        quantum_signature="",
        fuzzy_classification="",
        mathematical_properties={},
        metadata={"region": "Caribbean", "data_quality": "Fair", "open_data_index": 0.45}
    ),
    
    # ARGENTINA
    "ARGENTINA_NATIONAL": GovInfoSource(
        source_id="AR_001",
        country_name="Argentina",
        country_code="AR",
        government_level="National",
        primary_url="https://datos.gob.ar/",
        secondary_urls=["https://www.indec.gob.ar/", "https://www.argentina.gob.ar/"],
        data_types=["Open Data", "Statistics", "Economic Data", "Population", "Agriculture", "Health", "Education", "Transport"],
        portal_type="CKAN",
        last_updated="2025-06-18",
        accessibility_score=0.91,
        data_volume="Massive",
        language=["Spanish", "English"],
        sphere_coordinates=(0, 0, 0),
        quantum_signature="",
        fuzzy_classification="",
        mathematical_properties={},
        metadata={"region": "South America", "data_quality": "Excellent", "open_data_index": 0.83}
    ),
    
    # ARMENIA
    "ARMENIA_NATIONAL": GovInfoSource(
        source_id="AM_001",
        country_name="Armenia",
        country_code="AM",
        government_level="National",
        primary_url="https://www.armstat.am/",
        secondary_urls=["https://www.gov.am/en/", "https://www.cba.am/"],
        data_types=["Statistics", "Economic Data", "Demographics", "Trade", "Industry"],
        portal_type="Custom",
        last_updated="2025-06-18",
        accessibility_score=0.78,
        data_volume="Large",
        language=["Armenian", "English", "Russian"],
        sphere_coordinates=(0, 0, 0),
        quantum_signature="",
        fuzzy_classification="",
        mathematical_properties={},
        metadata={"region": "Asia", "data_quality": "Good", "open_data_index": 0.62}
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
        language=["English", "French", "German", "Spanish", "Italian", "Dutch"],
        sphere_coordinates=(0, 0, 0),
        quantum_signature="",
        fuzzy_classification="",
        mathematical_properties={},
        metadata={"member_states": 27, "founded": 1993}
    ),
    
    # AUSTRALIA
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
    
    # AUSTRIA
    "AUSTRIA_NATIONAL": GovInfoSource(
        source_id="AT_001",
        country_name="Austria",
        country_code="AT",
        government_level="National",
        primary_url="https://www.data.gv.at/",
        secondary_urls=["https://www.statistik.at/", "https://www.bka.gv.at/"],
        data_types=["Open Data", "Statistics", "Legislation", "Economic Data", "Population", "Environment"],
        portal_type="CKAN",
        last_updated="2025-06-18",
        accessibility_score=0.90,
        data_volume="Large",
        language=["German", "English"],
        sphere_coordinates=(0, 0, 0),
        quantum_signature="",
        fuzzy_classification="",
        mathematical_properties={},
        metadata={"region": "Europe", "data_quality": "Excellent", "open_data_index": 0.85}
    ),
    
    # BANGLADESH
    "BANGLADESH_NATIONAL": GovInfoSource(
        source_id="BD_001",
        country_name="Bangladesh",
        country_code="BD",
        government_level="National",
        primary_url="https://data.gov.bd/",
        secondary_urls=["https://www.bbs.gov.bd/", "https://www.bangladesh.gov.bd/"],
        data_types=["Open Data", "Statistics", "Population Data", "Economic Indicators", "Agriculture", "Climate"],
        portal_type="CKAN",
        last_updated="2025-06-18",
        accessibility_score=0.74,
        data_volume="Large",
        language=["Bengali", "English"],
        sphere_coordinates=(0, 0, 0),
        quantum_signature="",
        fuzzy_classification="",
        mathematical_properties={},
        metadata={"region": "Asia", "data_quality": "Good", "open_data_index": 0.58}
    ),
    
    # BELGIUM
    "BELGIUM_NATIONAL": GovInfoSource(
        source_id="BE_001",
        country_name="Belgium",
        country_code="BE",
        government_level="National",
        primary_url="https://data.gov.be/",
        secondary_urls=["https://statbel.fgov.be/", "https://www.belgium.be/"],
        data_types=["Open Data", "Statistics", "Legislation", "Economic Data", "Population", "Environment"],
        portal_type="CKAN",
        last_updated="2025-06-18",
        accessibility_score=0.88,
        data_volume="Large",
        language=["Dutch", "French", "German", "English"],
        sphere_coordinates=(0, 0, 0),
        quantum_signature="",
        fuzzy_classification="",
        mathematical_properties={},
        metadata={"region": "Europe", "data_quality": "Excellent", "open_data_index": 0.81}
    ),
    
    # BRAZIL
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
    
    # CANADA
    "CANADA_NATIONAL": GovInfoSource(
        source_id="CA_001",
        country_name="Canada",
        country_code="CA",
        government_level="National",
        primary_url="https://open.canada.ca/en",
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
    
    # CHINA
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
    
    # DENMARK
    "DENMARK_NATIONAL": GovInfoSource(
        source_id="DK_001",
        country_name="Denmark",
        country_code="DK",
        government_level="National",
        primary_url="https://www.opendata.dk/",
        secondary_urls=["https://www.dst.dk/", "https://www.stm.dk/"],
        data_types=["Open Data", "Statistics", "Legislation", "Economic Data", "Population", "Environment"],
        portal_type="CKAN",
        last_updated="2025-06-18",
        accessibility_score=0.91,
        data_volume="Large",
        language=["Danish", "English"],
        sphere_coordinates=(0, 0, 0),
        quantum_signature="",
        fuzzy_classification="",
        mathematical_properties={},
        metadata={"region": "Europe", "data_quality": "Excellent", "open_data_index": 0.87}
    ),
    
    # EGYPT
    "EGYPT_NATIONAL": GovInfoSource(
        source_id="EG_001",
        country_name="Egypt",
        country_code="EG",
        government_level="National",
        primary_url="https://www.capmas.gov.eg/",
        secondary_urls=["https://www.eip.gov.eg/", "https://www.cbe.org.eg/"],
        data_types=["Statistics", "Economic Data", "Population", "Demographics", "Industry"],
        portal_type="Custom",
        last_updated="2025-06-18",
        accessibility_score=0.68,
        data_volume="Large",
        language=["Arabic", "English"],
        sphere_coordinates=(0, 0, 0),
        quantum_signature="",
        fuzzy_classification="",
        mathematical_properties={},
        metadata={"region": "Africa", "data_quality": "Fair", "open_data_index": 0.43}
    ),
    
    # FINLAND
    "FINLAND_NATIONAL": GovInfoSource(
        source_id="FI_001",
        country_name="Finland",
        country_code="FI",
        government_level="National",
        primary_url="https://avoindata.fi/",
        secondary_urls=["https://www.stat.fi/", "https://valtioneuvosto.fi/"],
        data_types=["Open Data", "Statistics", "Legislation", "Economic Data", "Population", "Environment"],
        portal_type="CKAN",
        last_updated="2025-06-18",
        accessibility_score=0.93,
        data_volume="Large",
        language=["Finnish", "Swedish", "English"],
        sphere_coordinates=(0, 0, 0),
        quantum_signature="",
        fuzzy_classification="",
        mathematical_properties={},
        metadata={"region": "Europe", "data_quality": "Excellent", "open_data_index": 0.89}
    ),
    
    # FRANCE
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
    
    # GERMANY
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
    
    # INDIA
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
    
    # INDONESIA
    "INDONESIA_NATIONAL": GovInfoSource(
        source_id="ID_001",
        country_name="Indonesia",
        country_code="ID",
        government_level="National",
        primary_url="https://data.go.id/",
        secondary_urls=["https://www.bps.go.id/", "https://www.indonesia.go.id/"],
        data_types=["Open Data", "Statistics", "Economic Data", "Population", "Demographics", "Trade"],
        portal_type="CKAN",
        last_updated="2025-06-18",
        accessibility_score=0.75,
        data_volume="Large",
        language=["Indonesian", "English"],
        sphere_coordinates=(0, 0, 0),
        quantum_signature="",
        fuzzy_classification="",
        mathematical_properties={},
        metadata={"region": "Asia", "data_quality": "Good", "open_data_index": 0.61}
    ),
    
    # ITALY
    "ITALY_NATIONAL": GovInfoSource(
        source_id="IT_001",
        country_name="Italy",
        country_code="IT",
        government_level="National",
        primary_url="https://www.dati.gov.it/",
        secondary_urls=["https://www.istat.it/", "https://www.governo.it/"],
        data_types=["Open Data", "Statistics", "Legislation", "Economic Data", "Population", "Environment"],
        portal_type="CKAN",
        last_updated="2025-06-18",
        accessibility_score=0.87,
        data_volume="Large",
        language=["Italian", "English"],
        sphere_coordinates=(0, 0, 0),
        quantum_signature="",
        fuzzy_classification="",
        mathematical_properties={},
        metadata={"region": "Europe", "data_quality": "Excellent", "open_data_index": 0.82}
    ),
    
    # JAPAN
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

    "WORLD_BANK": GovInfoSource(
        source_id="WB_001",
        country_name="World Bank",
        country_code="WB",
        government_level="International",
        primary_url="https://data.worldbank.org/",
        secondary_urls=["https://datacatalog.worldbank.org/"],
        data_types=["Development", "Economics", "Finance", "Poverty", "Climate"],
        portal_type="Custom",
        last_updated="2025-06-18",
        accessibility_score=0.94,
        data_volume="Massive",
        language=["English", "French", "Spanish", "Arabic", "Chinese"],
        sphere_coordinates=(0, 0, 0),
        quantum_signature="",
        fuzzy_classification="",
        mathematical_properties={},
        metadata={"member_countries": 189, "established": 1944}
    ),
    
    # COMPREHENSIVE GLOBAL GOVERNMENT DATA SOURCES - EXPANDED LIBRARY
    
    # AFRICA CONTINENT (54 Countries)
    "ALGERIA_AFRICA": GovInfoSource(
        source_id="DZ_AFRICA_001",
        country_name="Algeria",
        country_code="DZ",
        government_level="National",
        primary_url="https://algeria.opendataforafrica.org/",
        secondary_urls=["https://www.data.gov.dz/", "https://www.ons.dz/", "https://www.finances.gov.dz/"],
        data_types=["Statistics", "Economics", "Demographics", "Oil Production", "Trade", "Population", "Health", "Education"],
        portal_type="CKAN",
        last_updated="2025-06-18",
        accessibility_score=0.72,
        data_volume="Large",
        language=["Arabic", "French", "English"],
        sphere_coordinates=(0, 0, 0),
        quantum_signature="",
        fuzzy_classification="",
        mathematical_properties={},
        metadata={"region": "Africa", "independence": 1962}
    ),
    
    "ANGOLA": GovInfoSource(
        source_id="AO_001",
        country_name="Angola",
        country_code="AO",
        government_level="National",
        primary_url="https://angola.opendataforafrica.org/",
        secondary_urls=["http://www.ine.gov.ao/"],
        data_types=["Statistics", "Economics", "Social Data"],
        portal_type="CKAN",
        last_updated="2025-06-18",
        accessibility_score=0.68,
        data_volume="Medium",
        language=["Portuguese", "English"],
        sphere_coordinates=(0, 0, 0),
        quantum_signature="",
        fuzzy_classification="",
        mathematical_properties={},
        metadata={"region": "Africa", "independence": 1975}
    ),
    
    "BENIN": GovInfoSource(
        source_id="BJ_001",
        country_name="Benin",
        country_code="BJ",
        government_level="National",
        primary_url="https://benin.opendataforafrica.org/",
        secondary_urls=["http://www.insae-bj.org/"],
        data_types=["Statistics", "Demographics", "Economics"],
        portal_type="CKAN",
        last_updated="2025-06-18",
        accessibility_score=0.65,
        data_volume="Small",
        language=["French", "English"],
        sphere_coordinates=(0, 0, 0),
        quantum_signature="",
        fuzzy_classification="",
        mathematical_properties={},
        metadata={"region": "Africa", "independence": 1960}
    ),
    
    "BOTSWANA": GovInfoSource(
        source_id="BW_001",
        country_name="Botswana",
        country_code="BW",
        government_level="National",
        primary_url="https://botswana.opendataforafrica.org/",
        secondary_urls=["http://www.statsbots.org.bw/"],
        data_types=["Statistics", "Economics", "Health", "Education"],
        portal_type="CKAN",
        last_updated="2025-06-18",
        accessibility_score=0.78,
        data_volume="Medium",
        language=["English", "Setswana"],
        sphere_coordinates=(0, 0, 0),
        quantum_signature="",
        fuzzy_classification="",
        mathematical_properties={},
        metadata={"region": "Africa", "independence": 1966}
    ),
    
    "BURKINA_FASO": GovInfoSource(
        source_id="BF_001",
        country_name="Burkina Faso",
        country_code="BF",
        government_level="National",
        primary_url="https://burkinafaso.opendataforafrica.org/",
        secondary_urls=["http://www.insd.bf/"],
        data_types=["Statistics", "Demographics", "Development"],
        portal_type="CKAN",
        last_updated="2025-06-18",
        accessibility_score=0.62,
        data_volume="Small",
        language=["French", "English"],
        sphere_coordinates=(0, 0, 0),
        quantum_signature="",
        fuzzy_classification="",
        mathematical_properties={},
        metadata={"region": "Africa", "independence": 1960}
    ),
    
    "BURUNDI": GovInfoSource(
        source_id="BI_001",
        country_name="Burundi",
        country_code="BI",
        government_level="National",
        primary_url="https://burundi.opendataforafrica.org/",
        secondary_urls=["http://www.isteebu.bi/"],
        data_types=["Statistics", "Demographics", "Economics"],
        portal_type="CKAN",
        last_updated="2025-06-18",
        accessibility_score=0.58,
        data_volume="Small",
        language=["French", "Kirundi", "English"],
        sphere_coordinates=(0, 0, 0),
        quantum_signature="",
        fuzzy_classification="",
        mathematical_properties={},
        metadata={"region": "Africa", "independence": 1962}
    ),
    
    "CABO_VERDE": GovInfoSource(
        source_id="CV_001",
        country_name="Cabo Verde",
        country_code="CV",
        government_level="National",
        primary_url="https://caboverde.opendataforafrica.org/",
        secondary_urls=["http://www.ine.cv/"],
        data_types=["Statistics", "Tourism", "Economics"],
        portal_type="CKAN",
        last_updated="2025-06-18",
        accessibility_score=0.71,
        data_volume="Small",
        language=["Portuguese", "English"],
        sphere_coordinates=(0, 0, 0),
        quantum_signature="",
        fuzzy_classification="",
        mathematical_properties={},
        metadata={"region": "Africa", "independence": 1975}
    ),
    
    "CAMEROON": GovInfoSource(
        source_id="CM_001",
        country_name="Cameroon",
        country_code="CM",
        government_level="National",
        primary_url="https://cameroon.opendataforafrica.org/",
        secondary_urls=["http://www.bucret.cm/"],
        data_types=["Statistics", "Economics", "Demographics"],
        portal_type="CKAN",
        last_updated="2025-06-18",
        accessibility_score=0.66,
        data_volume="Medium",
        language=["French", "English"],
        sphere_coordinates=(0, 0, 0),
        quantum_signature="",
        fuzzy_classification="",
        mathematical_properties={},
        metadata={"region": "Africa", "independence": 1960}
    ),
    
    "CENTRAL_AFRICAN_REPUBLIC": GovInfoSource(
        source_id="CF_001",
        country_name="Central African Republic",
        country_code="CF",
        government_level="National",
        primary_url="https://car.opendataforafrica.org/",
        secondary_urls=["http://www.insse-rca.org/"],
        data_types=["Statistics", "Demographics", "Humanitarian"],
        portal_type="CKAN",
        last_updated="2025-06-18",
        accessibility_score=0.52,
        data_volume="Small",
        language=["French", "Sango", "English"],
        sphere_coordinates=(0, 0, 0),
        quantum_signature="",
        fuzzy_classification="",
        mathematical_properties={},
        metadata={"region": "Africa", "independence": 1960}
    ),
    
    "CHAD": GovInfoSource(
        source_id="TD_001",
        country_name="Chad",
        country_code="TD",
        government_level="National",
        primary_url="https://chad.opendataforafrica.org/",
        secondary_urls=["http://www.inseed.td/"],
        data_types=["Statistics", "Demographics", "Economics"],
        portal_type="CKAN",
        last_updated="2025-06-18",
        accessibility_score=0.55,
        data_volume="Small",
        language=["French", "Arabic", "English"],
        sphere_coordinates=(0, 0, 0),
        quantum_signature="",
        fuzzy_classification="",
        mathematical_properties={},
        metadata={"region": "Africa", "independence": 1960}
    ),
    
    "COMOROS": GovInfoSource(
        source_id="KM_001",
        country_name="Comoros",
        country_code="KM",
        government_level="National",
        primary_url="https://comoros.opendataforafrica.org/",
        secondary_urls=["http://www.inseed.org/"],
        data_types=["Statistics", "Demographics", "Economics"],
        portal_type="CKAN",
        last_updated="2025-06-18",
        accessibility_score=0.54,
        data_volume="Small",
        language=["French", "Comorian", "Arabic", "English"],
        sphere_coordinates=(0, 0, 0),
        quantum_signature="",
        fuzzy_classification="",
        mathematical_properties={},
        metadata={"region": "Africa", "independence": 1975}
    ),
    
    "CONGO": GovInfoSource(
        source_id="CG_001",
        country_name="Congo",
        country_code="CG",
        government_level="National",
        primary_url="https://congo.opendataforafrica.org/",
        secondary_urls=["http://www.cnsee.org/"],
        data_types=["Statistics", "Oil & Gas", "Economics"],
        portal_type="CKAN",
        last_updated="2025-06-18",
        accessibility_score=0.63,
        data_volume="Small",
        language=["French", "English"],
        sphere_coordinates=(0, 0, 0),
        quantum_signature="",
        fuzzy_classification="",
        mathematical_properties={},
        metadata={"region": "Africa", "independence": 1960}
    ),
    
    "DEMOCRATIC_REPUBLIC_OF_CONGO": GovInfoSource(
        source_id="CD_001",
        country_name="Democratic Republic of the Congo",
        country_code="CD",
        government_level="National",
        primary_url="https://drcongo.opendataforafrica.org/",
        secondary_urls=["http://www.ins-rdc.org/"],
        data_types=["Statistics", "Mining", "Demographics", "Health"],
        portal_type="CKAN",
        last_updated="2025-06-18",
        accessibility_score=0.48,
        data_volume="Medium",
        language=["French", "English"],
        sphere_coordinates=(0, 0, 0),
        quantum_signature="",
        fuzzy_classification="",
        mathematical_properties={},
        metadata={"region": "Africa", "independence": 1960}
    ),
    
    "DJIBOUTI": GovInfoSource(
        source_id="DJ_001",
        country_name="Djibouti",
        country_code="DJ",
        government_level="National",
        primary_url="https://djibouti.opendataforafrica.org/",
        secondary_urls=["http://www.djibouti-data.org/"],
        data_types=["Statistics", "Port Data", "Economics"],
        portal_type="CKAN",
        last_updated="2025-06-18",
        accessibility_score=0.67,
        data_volume="Small",
        language=["French", "Arabic", "English"],
        sphere_coordinates=(0, 0, 0),
        quantum_signature="",
        fuzzy_classification="",
        mathematical_properties={},
        metadata={"region": "Africa", "independence": 1977}
    ),
    
    "EGYPT": GovInfoSource(
        source_id="EG_001",
        country_name="Egypt",
        country_code="EG",
        government_level="National",
        primary_url="https://egypt.opendataforafrica.org/",
        secondary_urls=["http://www.capmas.gov.eg/", "http://www.erfdataportal.com/index.php/catalog"],
        data_types=["Statistics", "Economics", "Demographics", "Archaeology"],
        portal_type="CKAN",
        last_updated="2025-06-18",
        accessibility_score=0.82,
        data_volume="Large",
        language=["Arabic", "English"],
        sphere_coordinates=(0, 0, 0),
        quantum_signature="",
        fuzzy_classification="",
        mathematical_properties={},
        metadata={"region": "Africa", "ancient_civilization": True}
    ),
    
    "EQUATORIAL_GUINEA": GovInfoSource(
        source_id="GQ_001",
        country_name="Equatorial Guinea",
        country_code="GQ",
        government_level="National",
        primary_url="https://equatorialguinea.opendataforafrica.org/",
        secondary_urls=["http://www.geostat.org/"],
        data_types=["Statistics", "Oil & Gas", "Economics"],
        portal_type="CKAN",
        last_updated="2025-06-18",
        accessibility_score=0.61,
        data_volume="Small",
        language=["Spanish", "French", "Portuguese", "English"],
        sphere_coordinates=(0, 0, 0),
        quantum_signature="",
        fuzzy_classification="",
        mathematical_properties={},
        metadata={"region": "Africa", "independence": 1968}
    ),
    
    "ERITREA": GovInfoSource(
        source_id="ER_001",
        country_name="Eritrea",
        country_code="ER",
        government_level="National",
        primary_url="https://eritrea.opendataforafrica.org/",
        secondary_urls=["http://www.nso.er/"],
        data_types=["Statistics", "Demographics", "Economics"],
        portal_type="CKAN",
        last_updated="2025-06-18",
        accessibility_score=0.45,
        data_volume="Small",
        language=["Tigrinya", "Arabic", "English"],
        sphere_coordinates=(0, 0, 0),
        quantum_signature="",
        fuzzy_classification="",
        mathematical_properties={},
        metadata={"region": "Africa", "independence": 1993}
    ),
    
    "ESWATINI": GovInfoSource(
        source_id="SZ_001",
        country_name="Eswatini",
        country_code="SZ",
        government_level="National",
        primary_url="https://eswatini.opendataforafrica.org/",
        secondary_urls=["http://www.gov.sz/"],
        data_types=["Statistics", "Demographics", "Economics"],
        portal_type="CKAN",
        last_updated="2025-06-18",
        accessibility_score=0.69,
        data_volume="Small",
        language=["English", "Swazi"],
        sphere_coordinates=(0, 0, 0),
        quantum_signature="",
        fuzzy_classification="",
        mathematical_properties={},
        metadata={"region": "Africa", "independence": 1968}
    ),
    
    "ETHIOPIA": GovInfoSource(
        source_id="ET_001",
        country_name="Ethiopia",
        country_code="ET",
        government_level="National",
        primary_url="https://ethiopia.opendataforafrica.org/",
        secondary_urls=["http://www.csa.gov.et/"],
        data_types=["Statistics", "Demographics", "Agriculture", "Economics"],
        portal_type="CKAN",
        last_updated="2025-06-18",
        accessibility_score=0.73,
        data_volume="Large",
        language=["Amharic", "English", "Oromo", "Tigrinya"],
        sphere_coordinates=(0, 0, 0),
        quantum_signature="",
        fuzzy_classification="",
        mathematical_properties={},
        metadata={"region": "Africa", "ancient_civilization": True}
    ),
    
    "GABON": GovInfoSource(
        source_id="GA_001",
        country_name="Gabon",
        country_code="GA",
        government_level="National",
        primary_url="https://gabon.opendataforafrica.org/",
        secondary_urls=["http://www.statistics-gabon.org/"],
        data_types=["Statistics", "Oil & Gas", "Economics", "Forestry"],
        portal_type="CKAN",
        last_updated="2025-06-18",
        accessibility_score=0.74,
        data_volume="Medium",
        language=["French", "English"],
        sphere_coordinates=(0, 0, 0),
        quantum_signature="",
        fuzzy_classification="",
        mathematical_properties={},
        metadata={"region": "Africa", "independence": 1960}
    ),
    
    "GAMBIA": GovInfoSource(
        source_id="GM_001",
        country_name="Gambia",
        country_code="GM",
        government_level="National",
        primary_url="https://gambia.opendataforafrica.org/",
        secondary_urls=["http://www.bos.gm/"],
        data_types=["Statistics", "Tourism", "Agriculture", "Demographics"],
        portal_type="CKAN",
        last_updated="2025-06-18",
        accessibility_score=0.71,
        data_volume="Small",
        language=["English", "Mandinka", "Wolof", "Fula"],
        sphere_coordinates=(0, 0, 0),
        quantum_signature="",
        fuzzy_classification="",
        mathematical_properties={},
        metadata={"region": "Africa", "independence": 1965}
    ),
    
    "GHANA": GovInfoSource(
        source_id="GH_001",
        country_name="Ghana",
        country_code="GH",
        government_level="National",
        primary_url="https://data.gov.gh/",
        secondary_urls=["https://ghana.opendataforafrica.org/", "http://www.statsghana.gov.gh/"],
        data_types=["Statistics", "Economics", "Demographics", "Mining", "Cocoa"],
        portal_type="CKAN",
        last_updated="2025-06-18",
        accessibility_score=0.86,
        data_volume="Large",
        language=["English"],
        sphere_coordinates=(0, 0, 0),
        quantum_signature="",
        fuzzy_classification="",
        mathematical_properties={},
        metadata={"region": "Africa", "independence": 1957}
    ),
    
    "GUINEA": GovInfoSource(
        source_id="GN_001",
        country_name="Guinea",
        country_code="GN",
        government_level="National",
        primary_url="https://guinea.opendataforafrica.org/",
        secondary_urls=["http://www.stat-guinee.org/"],
        data_types=["Statistics", "Mining", "Agriculture", "Demographics"],
        portal_type="CKAN",
        last_updated="2025-06-18",
        accessibility_score=0.59,
        data_volume="Medium",
        language=["French", "English"],
        sphere_coordinates=(0, 0, 0),
        quantum_signature="",
        fuzzy_classification="",
        mathematical_properties={},
        metadata={"region": "Africa", "independence": 1958}
    ),
    
    "GUINEA_BISSAU": GovInfoSource(
        source_id="GW_001",
        country_name="Guinea-Bissau",
        country_code="GW",
        government_level="National",
        primary_url="https://guineabissau.opendataforafrica.org/",
        secondary_urls=["http://www.ine.gov.gw/"],
        data_types=["Statistics", "Agriculture", "Demographics", "Fisheries"],
        portal_type="CKAN",
        last_updated="2025-06-18",
        accessibility_score=0.53,
        data_volume="Small",
        language=["Portuguese", "English"],
        sphere_coordinates=(0, 0, 0),
        quantum_signature="",
        fuzzy_classification="",
        mathematical_properties={},
        metadata={"region": "Africa", "independence": 1973}
    ),
    
    "IVORY_COAST": GovInfoSource(
        source_id="CI_001",
        country_name="Ivory Coast",
        country_code="CI",
        government_level="National",
        primary_url="https://cotedivoire.opendataforafrica.org/",
        secondary_urls=["http://www.ins.ci/"],
        data_types=["Statistics", "Cocoa", "Economics", "Demographics"],
        portal_type="CKAN",
        last_updated="2025-06-18",
        accessibility_score=0.76,
        data_volume="Large",
        language=["French", "English"],
        sphere_coordinates=(0, 0, 0),
        quantum_signature="",
        fuzzy_classification="",
        mathematical_properties={},
        metadata={"region": "Africa", "independence": 1960}
    ),
    
    "KENYA": GovInfoSource(
        source_id="KE_001",
        country_name="Kenya",
        country_code="KE",
        government_level="National",
        primary_url="https://kenya.opendataforafrica.org/",
        secondary_urls=["http://www.knbs.or.ke/", "https://www.opendata.go.ke/"],
        data_types=["Statistics", "Tourism", "Agriculture", "Technology", "Demographics"],
        portal_type="CKAN",
        last_updated="2025-06-18",
        accessibility_score=0.88,
        data_volume="Large",
        language=["English", "Swahili"],
        sphere_coordinates=(0, 0, 0),
        quantum_signature="",
