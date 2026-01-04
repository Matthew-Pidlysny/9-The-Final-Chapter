#!/usr/bin/env python3
"""
Newspaper Workshop - A separate module for generating newspapers
Integrates with existing Falcon Press Office libraries without modifying core code
"""

import sys
import os
import json
import logging
from datetime import datetime, timezone
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, asdict
import asyncio
import aiohttp
import feedparser
from dataclasses import dataclass, asdict

# Import existing libraries (gentle integration)
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from enhanced_falcon_integration import EnhancedFalconIntegration
    from websters_dictionary_library import WebstersDictionaryManager
    from rogets_thesaurus_library import RogetsThesaurusManager
    from unconventional_news_sources_library import UnconventionalNewsSourcesManager
except ImportError as e:
    print(f"Warning: Could not import existing libraries: {e}")
    print("Newspaper Workshop will run in standalone mode")

@dataclass
class NewsArticle:
    """Represents a single news article"""
    title: str
    content: str
    source: str
    category: str
    timestamp: datetime
    url: Optional[str] = None
    author: Optional[str] = None
    word_count: int = 0
    sentiment_score: float = 0.0
    keywords: List[str] = None
    
    def __post_init__(self):
        if self.keywords is None:
            self.keywords = []
        if isinstance(self.timestamp, str):
            self.timestamp = datetime.fromisoformat(self.timestamp)
        self.word_count = len(self.content.split())

@dataclass
class NewspaperSection:
    """Represents a section of the newspaper"""
    name: str
    articles: List[NewsArticle]
    template: str = "default"
    
    def add_article(self, article: NewsArticle):
        """Add an article to this section"""
        self.articles.append(article)
    
    def get_word_count(self) -> int:
        """Get total word count for this section"""
        return sum(article.word_count for article in self.articles)

@dataclass
class NewspaperEdition:
    """Represents a complete newspaper edition"""
    title: str
    subtitle: str
    publication_date: datetime
    sections: Dict[str, NewspaperSection]
    editorial_note: str = ""
    
    def add_section(self, section: NewspaperSection):
        """Add a section to the newspaper"""
        self.sections[section.name] = section
    
    def get_total_articles(self) -> int:
        """Get total number of articles"""
        return sum(len(section.articles) for section in self.sections.values())
    
    def get_total_word_count(self) -> int:
        """Get total word count for entire newspaper"""
        return sum(section.get_word_count() for section in self.sections.values())

class NewspaperWorkshop:
    """Main Newspaper Workshop class"""
    
    def __init__(self, config_path: str = "newspaper_workshop/config.json"):
        self.config_path = config_path
        self.config = self.load_config()
        self.setup_logging()
        
        # Initialize existing libraries (if available)
        self.falcon_integration = None
        self.dictionary_manager = None
        self.thesaurus_manager = None
        self.news_sources_manager = None
        
        self.initialize_libraries()
        
        # Current edition being worked on
        self.current_edition = None
    
    def load_config(self) -> Dict[str, Any]:
        """Load workshop configuration"""
        default_config = {
            "newspaper_title": "The Falcon Press",
            "subtitle": "Global Perspectives, Unfiltered Truth",
            "default_sections": [
                "Headlines",
                "World News", 
                "Mathematics & Sciences",
                "Technology",
                "Culture & Society",
                "Opinions & Analysis"
            ],
            "max_articles_per_section": 10,
            "min_article_length": 200,
            "max_article_length": 2000,
            "export_formats": ["html", "pdf"],
            "latex_enabled": True,
            "consistency_checks": True
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
        log_dir = "newspaper_workshop/logs"
        os.makedirs(log_dir, exist_ok=True)
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(f"{log_dir}/workshop.log"),
                logging.StreamHandler(sys.stdout)
            ]
        )
        self.logger = logging.getLogger("NewspaperWorkshop")
    
    def initialize_libraries(self):
        """Gently initialize existing libraries"""
        try:
            self.falcon_integration = EnhancedFalconIntegration()
            self.logger.info("Enhanced Falcon Integration loaded successfully")
        except Exception as e:
            self.logger.warning(f"Could not load Enhanced Falcon Integration: {e}")
        
        try:
            self.dictionary_manager = WebstersDictionaryManager()
            self.logger.info("Dictionary Manager loaded successfully")
        except Exception as e:
            self.logger.warning(f"Could not load Dictionary Manager: {e}")
        
        try:
            self.thesaurus_manager = RogetsThesaurusManager()
            self.logger.info("Thesaurus Manager loaded successfully")
        except Exception as e:
            self.logger.warning(f"Could not load Thesaurus Manager: {e}")
        
        try:
            self.news_sources_manager = UnconventionalNewsSourcesManager()
            self.logger.info("News Sources Manager loaded successfully")
        except Exception as e:
            self.logger.warning(f"Could not load News Sources Manager: {e}")
    
    def create_new_edition(self, title: Optional[str] = None) -> NewspaperEdition:
        """Create a new newspaper edition"""
        if title is None:
            title = self.config["newspaper_title"]
        
        publication_date = datetime.now(timezone.utc)
        
        edition = NewspaperEdition(
            title=title,
            subtitle=self.config["subtitle"],
            publication_date=publication_date,
            sections={}
        )
        
        # Create default sections
        for section_name in self.config["default_sections"]:
            section = NewspaperSection(name=section_name, articles=[])
            edition.add_section(section)
        
        self.current_edition = edition
        self.logger.info(f"Created new edition: {title} - {publication_date}")
        
        return edition
    
    def log_error(self, message: str):
        """Log an error message"""
        print(f"ERROR: {message}")
    
    def get_status(self) -> Dict[str, Any]:
        """Get current workshop status"""
        status = {
            "workshop_ready": True,
            "libraries_loaded": {
                "falcon_integration": self.falcon_integration is not None,
                "dictionary": self.dictionary_manager is not None,
                "thesaurus": self.thesaurus_manager is not None,
                "news_sources": self.news_sources_manager is not None
            },
            "current_edition": None,
            "config": self.config
        }
        
        if self.current_edition:
            status["current_edition"] = {
                "title": self.current_edition.title,
                "publication_date": self.current_edition.publication_date.isoformat(),
                "total_articles": self.current_edition.get_total_articles(),
                "total_word_count": self.current_edition.get_total_word_count(),
                "sections": list(self.current_edition.sections.keys())
            }
        
        return status

def main():
    """Main function for testing"""
    workshop = NewspaperWorkshop()
    status = workshop.get_status()
    
    print("Newspaper Workshop Status:")
    print(json.dumps(status, indent=2, default=str))
    
    # Test creating a new edition
    edition = workshop.create_new_edition()
    print(f"\nCreated edition: {edition.title}")
    print(f"Sections: {list(edition.sections.keys())}")

if __name__ == "__main__":
    main()