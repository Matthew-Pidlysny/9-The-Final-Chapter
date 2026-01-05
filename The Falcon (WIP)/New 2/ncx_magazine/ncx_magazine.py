#!/usr/bin/env python3
"""
NCX Magazine - Non-Conformist Xenophober Magazine
A punk zine analyzing hidden patterns in news and business

"We see what they don't want us to see. We say what they don't want us to say."
"""

import sys
import os
import json
import logging
from datetime import datetime, timezone
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, asdict
import re

# Import existing Falcon Press libraries (gentle integration)
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

@dataclass
class NCXArticle:
    """Represents an NCX Magazine article with analysis"""
    title: str
    content: str
    analysis_type: str  # discretion, altruistic_conspiracy, sovereignty, affiliation
    evidence_score: float  # 0.0 to 1.0
    source_urls: List[str]
    detected_patterns: List[str]
    organizations_mentioned: List[str]
    timestamp: datetime
    punk_rating: int  # 1-5 punk skulls 💀
    should_publish: bool
    reasoning: str
    
    def __post_init__(self):
        if isinstance(self.timestamp, str):
            self.timestamp = datetime.fromisoformat(self.timestamp)

@dataclass
class NCXEdition:
    """Represents a complete NCX Magazine edition"""
    title: str
    subtitle: str
    publication_date: datetime
    articles: List[NCXArticle]
    editorial_note: str
    total_evidence_score: float
    
    def add_article(self, article: NCXArticle):
        """Add an article to the edition"""
        if article.should_publish:
            self.articles.append(article)
    
    def get_publishable_count(self) -> int:
        """Get count of publishable articles"""
        return len([a for a in self.articles if a.should_publish])

class NCXMagazine:
    """Main NCX Magazine class"""
    
    def __init__(self, config_path: str = "ncx_magazine/config.json"):
        self.config_path = config_path
        self.config = self.load_config()
        self.setup_logging()
        
        # Initialize analysis systems
        self.pattern_analyzer = None
        self.linguistic_analyzer = None
        
        # Current edition
        self.current_edition = None
        
        # Tracked organizations (the hidden foes)
        self.tracked_organizations = [
            "Lucis Trust",
            "Theosophical Society",
            "Great White Brotherhood",
            "Jesuits",
            "Rosicrucians",
            "Roesa Crucis",
            "Illuminati",
            "Masons",
            "Freemasons",
            "Summit Lighthouse",
            "Church of Satan",
            "Temple of Set",
            "Ordo Templi Orientis",
            "Golden Dawn"
        ]
        
        # Pattern keywords for detection
        self.discretion_patterns = [
            "behind closed doors",
            "private meeting",
            "undisclosed",
            "unnamed sources",
            "off the record",
            "confidential",
            "insider information",
            "sources say",
            "according to sources",
            "leaked documents"
        ]
        
        self.altruistic_patterns = [
            "philanthropy",
            "charitable donation",
            "giving back",
            "social responsibility",
            "sustainability",
            "awareness campaign",
            "humanitarian",
            "consciousness",
            "spiritual awakening",
            "metaphysical"
        ]
        
        self.sovereignty_patterns = [
            "above the law",
            "untouchable",
            "immune",
            "diplomatic immunity",
            "sovereign",
            "beyond jurisdiction",
            "protected",
            "privileged",
            "elite",
            "establishment"
        ]
        
        self.logger = logging.getLogger("NCXMagazine")
    
    def load_config(self) -> Dict[str, Any]:
        """Load NCX configuration"""
        default_config = {
            "magazine_title": "NCX Magazine",
            "subtitle": "Non-Conformist Xenophober - Seeing Through The Veil",
            "punk_aesthetic": True,
            "minimum_evidence_score": 0.6,
            "minimum_punk_rating": 3,
            "analysis_depth": "deep",
            "editorial_principles": {
                "truth_seeking": True,
                "pattern_recognition": True,
                "skeptical_analysis": True,
                "punk_attitude": True,
                "no_bullshit": True
            }
        }
        
        if os.path.exists(self.config_path):
            try:
                with open(self.config_path, 'r') as f:
                    config = json.load(f)
                return {**default_config, **config}
            except Exception as e:
                self.log_error(f"Failed to load config: {e}")
        
        return default_config
    
    def setup_logging(self):
        """Setup logging configuration"""
        log_dir = "ncx_magazine/logs"
        os.makedirs(log_dir, exist_ok=True)
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(f"{log_dir}/ncx.log"),
                logging.StreamHandler(sys.stdout)
            ]
        )
        self.logger = logging.getLogger("NCXMagazine")
    
    def create_new_edition(self) -> NCXEdition:
        """Create a new NCX Magazine edition"""
        publication_date = datetime.now(timezone.utc)
        
        edition = NCXEdition(
            title=self.config["magazine_title"],
            subtitle=self.config["subtitle"],
            publication_date=publication_date,
            articles=[],
            editorial_note=self.generate_editorial_note(),
            total_evidence_score=0.0
        )
        
        self.current_edition = edition
        self.logger.info(f"Created new NCX edition: {publication_date}")
        
        return edition
    
    def generate_editorial_note(self) -> str:
        """Generate punk zine editorial note"""
        return """
🎸 EDITORIAL NOTE 🎸

Welcome to NCX Magazine - where we cut through the corporate bullshit and expose 
the patterns they don't want you to see.

We're not here to tell you what to think. We're here to show you what to LOOK FOR.
The business world operates on rules they never share with us regular folks. 
They make deals in the shadows, then preach enlightenment in the light.

This isn't your typical conspiracy rag. We use REAL linguistic analysis, 
REAL pattern detection, and REAL evidence scoring. If we can't back it up, 
we don't print it. That's the NCX way.

Stay skeptical. Stay punk. Stay aware.

- The NCX Collective
        """
    
    def log_error(self, message: str):
        """Log an error message"""
        print(f"ERROR: {message}")
    
    def get_status(self) -> Dict[str, Any]:
        """Get current magazine status"""
        status = {
            "magazine_ready": True,
            "current_edition": None,
            "tracked_organizations": len(self.tracked_organizations),
            "analysis_systems": {
                "pattern_analyzer": self.pattern_analyzer is not None,
                "linguistic_analyzer": self.linguistic_analyzer is not None
            },
            "config": self.config
        }
        
        if self.current_edition:
            status["current_edition"] = {
                "title": self.current_edition.title,
                "publication_date": self.current_edition.publication_date.isoformat(),
                "total_articles": len(self.current_edition.articles),
                "publishable_articles": self.current_edition.get_publishable_count(),
                "total_evidence_score": self.current_edition.total_evidence_score
            }
        
        return status

def main():
    """Main function for testing"""
    magazine = NCXMagazine()
    status = magazine.get_status()
    
    print("🎸 NCX Magazine Status:")
    print(json.dumps(status, indent=2, default=str))
    
    # Test creating a new edition
    edition = magazine.create_new_edition()
    print(f"\n📰 Created edition: {edition.title}")
    print(f"📅 Date: {edition.publication_date}")
    print(f"\n{edition.editorial_note}")

if __name__ == "__main__":
    main()