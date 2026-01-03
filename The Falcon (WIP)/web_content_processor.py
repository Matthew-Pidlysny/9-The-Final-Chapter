"""
Web Content Processor for The Falcon Press Office
Ethical web scraping, content analysis, and library integration
"""

import requests
import re
import time
import hashlib
import base64
from urllib.parse import urljoin, urlparse, parse_qs
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import json
import sqlite3
import threading
import queue
from dataclasses import dataclass, asdict
from typing import List, Dict, Optional, Any
import warnings
warnings.filterwarnings('ignore')

# Import our components
from enhanced_visualizations import DataProcessor

@dataclass
class WebSource:
    """Web source configuration"""
    id: str
    name: str
    url: str
    category: str
    update_frequency: int  # minutes
    last_updated: str
    active: bool
    selectors: Dict[str, str]  # CSS selectors for content extraction
    headers: Dict[str, str]

@dataclass
class ProcessedContent:
    """Processed web content"""
    source_id: str
    url: str
    title: str
    content: str
    summary: str
    metadata: Dict[str, Any]
    analysis_results: Dict[str, Any]
    timestamp: str
    content_hash: str

class EthicalWebScraper:
    """Ethical web scraping with rate limiting and respect for robots.txt"""
    
    def __init__(self, user_agent="FalconPressOffice/1.0 (Educational Research Bot)"):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': user_agent,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        })
        
        self.rate_limits = {}
        self.last_requests = {}
        self.robots_cache = {}
        
        # Default rate limits (seconds between requests)
        self.default_rate_limit = 1
        self.max_retries = 3
        self.request_timeout = 30
        
    def check_robots_txt(self, domain, path):
        """Check if scraping is allowed by robots.txt"""
        if domain in self.robots_cache:
            return self.robots_cache[domain].get(path, True)
        
        try:
            robots_url = f"https://{domain}/robots.txt"
            response = self.session.get(robots_url, timeout=10)
            
            if response.status_code == 200:
                rules = {}
                for line in response.text.split('\n'):
                    if line.startswith('Disallow:'):
                        disallowed_path = line.split(':')[1].strip()
                        rules[disallowed_path] = False
                
                self.robots_cache[domain] = rules
                return rules.get(path, True)
            else:
                self.robots_cache[domain] = {}
                return True
                
        except Exception:
            self.robots_cache[domain] = {}
            return True
    
    def respect_rate_limit(self, domain):
        """Implement rate limiting"""
        rate_limit = self.rate_limits.get(domain, self.default_rate_limit)
        last_request = self.last_requests.get(domain, 0)
        
        current_time = time.time()
        time_since_last = current_time - last_request
        
        if time_since_last < rate_limit:
            sleep_time = rate_limit - time_since_last
            time.sleep(sleep_time)
        
        self.last_requests[domain] = time.time()
    
    def scrape_url(self, url, retries=0):
        """Scrape URL with ethical considerations"""
        try:
            parsed = urlparse(url)
            domain = parsed.netloc
            path = parsed.path
            
            # Check robots.txt
            if not self.check_robots_txt(domain, path):
                return {"error": "Scraping disallowed by robots.txt", "url": url}
            
            # Respect rate limiting
            self.respect_rate_limit(domain)
            
            # Make request
            response = self.session.get(url, timeout=self.request_timeout)
            response.raise_for_status()
            
            # Check content type
            content_type = response.headers.get('content-type', '').lower()
            if 'text/html' not in content_type:
                return {"error": f"Unsupported content type: {content_type}", "url": url}
            
            return {
                "url": url,
                "status_code": response.status_code,
                "content": response.text,
                "headers": dict(response.headers),
                "encoding": response.encoding
            }
            
        except requests.exceptions.RequestException as e:
            if retries < self.max_retries:
                wait_time = 2 ** retries  # Exponential backoff
                time.sleep(wait_time)
                return self.scrape_url(url, retries + 1)
            else:
                return {"error": f"Request failed after {self.max_retries} retries: {str(e)}", "url": url}
        except Exception as e:
            return {"error": f"Unexpected error: {str(e)}", "url": url}

class ContentExtractor:
    """Advanced content extraction with multiple strategies"""
    
    def __init__(self):
        self.default_selectors = {
            'title': ['title', 'h1', '.headline', '.title'],
            'content': ['article', '.content', '.article-body', 'main', '.post-content'],
            'author': ['.author', '.byline', '[rel="author"]'],
            'date': ['.date', '.published', 'time', '[datetime]'],
            'summary': '.summary, .excerpt, .lead'
        }
    
    def extract_content(self, html, url, custom_selectors=None):
        """Extract structured content from HTML"""
        try:
            soup = BeautifulSoup(html, 'html.parser')
            
            # Remove unwanted elements
            for element in soup(['script', 'style', 'nav', 'footer', 'header', 'aside']):
                element.decompose()
            
            # Merge selectors
            if custom_selectors:
                selectors = {**self.default_selectors, **custom_selectors}
            else:
                selectors = self.default_selectors
            
            extracted = {}
            
            # Extract title
            extracted['title'] = self._extract_text(soup, selectors['title'])
            
            # Extract main content
            extracted['content'] = self._extract_main_content(soup, selectors['content'])
            
            # Extract metadata
            extracted['author'] = self._extract_text(soup, selectors['author'])
            extracted['date'] = self._extract_text(soup, selectors['date'])
            extracted['summary'] = self._extract_text(soup, selectors['summary'])
            
            # Extract meta tags
            extracted['meta'] = self._extract_meta_tags(soup)
            
            # Extract structured data
            extracted['structured_data'] = self._extract_structured_data(soup)
            
            # Calculate content metrics
            extracted['metrics'] = self._calculate_content_metrics(extracted)
            
            return extracted
            
        except Exception as e:
            return {"error": f"Content extraction failed: {str(e)}"}
    
    def _extract_text(self, soup, selectors):
        """Extract text using multiple selectors"""
        for selector in selectors:
            try:
                element = soup.select_one(selector)
                if element:
                    return element.get_text(strip=True)
            except Exception:
                continue
        return ""
    
    def _extract_main_content(self, soup, selectors):
        """Extract main content with fallback strategies"""
        # Try specified selectors first
        for selector in selectors:
            try:
                element = soup.select_one(selector)
                if element:
                    content = element.get_text(separator=' ', strip=True)
                    if len(content) > 200:  # Reasonable content length
                        return content
            except Exception:
                continue
        
        # Fallback: find largest text block
        text_blocks = []
        for element in soup.find_all(['p', 'div']):
            text = element.get_text(strip=True)
            if len(text) > 100:
                text_blocks.append((len(text), text))
        
        if text_blocks:
            text_blocks.sort(reverse=True)
            return text_blocks[0][1]
        
        # Final fallback: all text
        return soup.get_text(separator=' ', strip=True)
    
    def _extract_meta_tags(self, soup):
        """Extract meta tags"""
        meta = {}
        
        # Standard meta tags
        for tag in soup.find_all('meta'):
            name = tag.get('name') or tag.get('property')
            content = tag.get('content')
            if name and content:
                meta[name] = content
        
        # Open Graph tags
        for tag in soup.find_all('meta', property=True):
            prop = tag.get('property')
            content = tag.get('content')
            if prop and content:
                meta[f"og:{prop}"] = content
        
        return meta
    
    def _extract_structured_data(self, soup):
        """Extract structured data (JSON-LD, microdata)"""
        structured_data = []
        
        # JSON-LD
        for script in soup.find_all('script', type='application/ld+json'):
            try:
                import json
                data = json.loads(script.string)
                structured_data.append(data)
            except Exception:
                continue
        
        return structured_data
    
    def _calculate_content_metrics(self, extracted):
        """Calculate content quality metrics"""
        content = extracted.get('content', '')
        
        return {
            'word_count': len(content.split()),
            'character_count': len(content),
            'paragraph_count': len(content.split('\n\n')),
            'readability_score': self._calculate_readability(content),
            'has_images': bool(extracted.get('images', [])),
            'has_videos': bool(extracted.get('videos', []))
        }
    
    def _calculate_readability(self, text):
        """Simple readability calculation"""
        sentences = text.split('.')
        words = text.split()
        
        if not sentences or not words:
            return 0
        
        avg_sentence_length = len(words) / len(sentences)
        return max(0, 100 - (avg_sentence_length * 2))

class ContentAnalyzer:
    """Advanced content analysis with AI integration"""
    
    def __init__(self):
        self.data_processor = DataProcessor()
        self.ai_summarizer = self._init_ai_summarizer()
    
    def _init_ai_summarizer(self):
        """Initialize AI summarization"""
        try:
            # Try to initialize local AI service
            return LocalAISummarizer()
        except Exception:
            return SimpleSummarizer()
    
    def analyze_content(self, extracted_content, url):
        """Comprehensive content analysis"""
        content = extracted_content.get('content', '')
        
        if not content:
            return {"error": "No content to analyze"}
        
        analysis = {
            'url': url,
            'timestamp': datetime.now().isoformat(),
            'basic_metrics': extracted_content.get('metrics', {}),
            'sentiment_analysis': self.data_processor.analyze_sentiment(content),
            'topic_extraction': self.data_processor.extract_topics(content),
            'entity_recognition': self.data_processor.extract_entities(content),
            'keyword_extraction': self.data_processor.extract_keywords(content),
            'language_detection': self.data_processor.detect_language(content),
            'readability_analysis': self.data_processor.analyze_readability(content),
            'ai_summary': self.ai_summarizer.summarize(content, max_length=150)
        }
        
        # Advanced analysis
        analysis.update({
            'content_quality': self._assess_content_quality(extracted_content),
            'credibility_indicators': self._assess_credibility(extracted_content),
            'bias_detection': self._detect_bias(content),
            'fact_checkability': self._assess_fact_checkability(extracted_content)
        })
        
        return analysis
    
    def _assess_content_quality(self, extracted_content):
        """Assess content quality"""
        metrics = extracted_content.get('metrics', {})
        
        quality_score = 0
        
        # Length indicators
        word_count = metrics.get('word_count', 0)
        if word_count > 300:
            quality_score += 20
        elif word_count > 100:
            quality_score += 10
        
        # Structure indicators
        if metrics.get('paragraph_count', 0) > 3:
            quality_score += 15
        
        # Media indicators
        if metrics.get('has_images'):
            quality_score += 10
        if metrics.get('has_videos'):
            quality_score += 10
        
        # Meta information
        if extracted_content.get('author'):
            quality_score += 15
        if extracted_content.get('date'):
            quality_score += 15
        if extracted_content.get('summary'):
            quality_score += 15
        
        return {
            'score': min(100, quality_score),
            'indicators': {
                'length': word_count,
                'structure': metrics.get('paragraph_count', 0),
                'media': metrics.get('has_images', False),
                'metadata': bool(extracted_content.get('author') and extracted_content.get('date'))
            }
        }
    
    def _assess_credibility(self, extracted_content):
        """Assess content credibility indicators"""
        indicators = {
            'has_author': bool(extracted_content.get('author')),
            'has_date': bool(extracted_content.get('date')),
            'has_sources': False,  # Would need more sophisticated analysis
            'has_citations': False,
            'structured_data': bool(extracted_content.get('structured_data')),
            'meta_description': bool(extracted_content.get('meta', {}).get('description'))
        }
        
        credibility_score = sum(indicators.values()) * 16.67  # 6 indicators = 100/6
        
        return {
            'score': credibility_score,
            'indicators': indicators
        }
    
    def _detect_bias(self, content):
        """Simple bias detection"""
        # This is a simplified implementation
        # Real implementation would use NLP models
        emotional_words = ['terrible', 'amazing', 'disgusting', 'perfect', 'worst', 'best']
        absolute_words = ['always', 'never', 'all', 'none', 'every', 'only']
        
        words = content.lower().split()
        
        emotional_count = sum(1 for word in words if word in emotional_words)
        absolute_count = sum(1 for word in words if word in absolute_words)
        total_words = len(words)
        
        if total_words == 0:
            bias_score = 0
        else:
            bias_score = ((emotional_count + absolute_count) / total_words) * 100
        
        return {
            'bias_score': min(100, bias_score),
            'emotional_language': emotional_count,
            'absolute_language': absolute_count,
            'total_words': total_words
        }
    
    def _assess_fact_checkability(self, extracted_content):
        """Assess how easily content can be fact-checked"""
        content = extracted_content.get('content', '')
        
        # Look for claims that could be fact-checked
        claim_indicators = ['according to', 'reported', 'claimed', 'stated', 'announced']
        number_indicators = re.findall(r'\d+(?:,\d{3})*(?:\.\d+)?%?', content)
        
        claims = sum(1 for indicator in claim_indicators if indicator in content.lower())
        
        return {
            'claims_found': claims,
            'numbers_found': len(number_indicators),
            'fact_checkable': claims > 0 or len(number_indicators) > 0,
            'score': min(100, (claims + len(number_indicators)) * 10)
        }

class SimpleSummarizer:
    """Simple extractive summarizer as fallback"""
    
    def summarize(self, text, max_length=150):
        """Create simple extractive summary"""
        sentences = re.split(r'[.!?]+', text)
        sentences = [s.strip() for s in sentences if len(s.strip()) > 20]
        
        if not sentences:
            return text[:max_length*5]
        
        # Score sentences by length and key terms
        key_terms = ['important', 'significant', 'major', 'key', 'critical', 'essential']
        scored_sentences = []
        
        for sentence in sentences:
            score = len(sentence)
            score += sum(5 for term in key_terms if term.lower() in sentence.lower())
            scored_sentences.append((score, sentence))
        
        # Select best sentences
        scored_sentences.sort(reverse=True)
        summary_sentences = [s[1] for s in scored_sentences[:3]]
        
        summary = '. '.join(summary_sentences)
        return summary[:max_length*5]

class LocalAISummarizer(SimpleSummarizer):
    """Local AI summarizer (would connect to local models)"""
    
    def summarize(self, text, max_length=150):
        """Summarize using local AI"""
        try:
            # Try to use Ollama or similar local service
            return self._summarize_with_local_ai(text, max_length)
        except Exception:
            # Fallback to simple summarizer
            return super().summarize(text, max_length)
    
    def _summarize_with_local_ai(self, text, max_length):
        """Summarize using local AI service"""
        # This would connect to local Ollama, Llama.cpp, or similar
        # For now, use fallback
        return super().summarize(text, max_length)

class WebContentManager:
    """Main manager for web content processing"""
    
    def __init__(self):
        self.scraper = EthicalWebScraper()
        self.extractor = ContentExtractor()
        self.analyzer = ContentAnalyzer()
        self.sources = {}
        self.processed_content = []
        self.database_path = "falcon_content.db"
        self._init_database()
    
    def _init_database(self):
        """Initialize SQLite database for content storage"""
        conn = sqlite3.connect(self.database_path)
        cursor = conn.cursor()
        
        # Create tables
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS web_sources (
                id TEXT PRIMARY KEY,
                name TEXT,
                url TEXT,
                category TEXT,
                update_frequency INTEGER,
                last_updated TEXT,
                active BOOLEAN,
                selectors TEXT,
                headers TEXT
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS processed_content (
                id TEXT PRIMARY KEY,
                source_id TEXT,
                url TEXT,
                title TEXT,
                content TEXT,
                summary TEXT,
                metadata TEXT,
                analysis_results TEXT,
                timestamp TEXT,
                content_hash TEXT
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def add_source(self, name, url, category="general", update_frequency=60, 
                  selectors=None, headers=None):
        """Add a web source"""
        source_id = hashlib.md5(f"{name}_{url}".encode()).hexdigest()[:12]
        
        source = WebSource(
            id=source_id,
            name=name,
            url=url,
            category=category,
            update_frequency=update_frequency,
            last_updated="",
            active=True,
            selectors=selectors or {},
            headers=headers or {}
        )
        
        self.sources[source_id] = source
        
        # Save to database
        conn = sqlite3.connect(self.database_path)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT OR REPLACE INTO web_sources 
            (id, name, url, category, update_frequency, last_updated, active, selectors, headers)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            source.id, source.name, source.url, source.category,
            source.update_frequency, source.last_updated, source.active,
            json.dumps(source.selectors), json.dumps(source.headers)
        ))
        conn.commit()
        conn.close()
        
        return source_id
    
    def process_source(self, source_id):
        """Process a single web source"""
        if source_id not in self.sources:
            return {"error": "Source not found"}
        
        source = self.sources[source_id]
        
        # Scrape content
        scrape_result = self.scraper.scrape_url(source.url)
        
        if "error" in scrape_result:
            return scrape_result
        
        # Extract content
        extracted = self.extractor.extract_content(
            scrape_result['content'], 
            source.url, 
            source.selectors
        )
        
        if "error" in extracted:
            return extracted
        
        # Analyze content
        analysis = self.analyzer.analyze_content(extracted, source.url)
        
        # Create processed content object
        processed = ProcessedContent(
            source_id=source_id,
            url=source.url,
            title=extracted.get('title', ''),
            content=extracted.get('content', ''),
            summary=analysis.get('ai_summary', ''),
            metadata=extracted,
            analysis_results=analysis,
            timestamp=datetime.now().isoformat(),
            content_hash=hashlib.md5(extracted.get('content', '').encode()).hexdigest()
        )
        
        # Save to database
        self._save_processed_content(processed)
        
        # Update source
        source.last_updated = processed.timestamp
        self._update_source(source)
        
        return asdict(processed)
    
    def _save_processed_content(self, processed):
        """Save processed content to database"""
        conn = sqlite3.connect(self.database_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT OR REPLACE INTO processed_content
            (id, source_id, url, title, content, summary, metadata, analysis_results, timestamp, content_hash)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            hashlib.md5(f"{processed.url}_{processed.timestamp}".encode()).hexdigest(),
            processed.source_id, processed.url, processed.title, processed.content,
            processed.summary, json.dumps(processed.metadata), 
            json.dumps(processed.analysis_results), processed.timestamp, processed.content_hash
        ))
        
        conn.commit()
        conn.close()
    
    def _update_source(self, source):
        """Update source in database"""
        conn = sqlite3.connect(self.database_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            UPDATE web_sources SET last_updated = ? WHERE id = ?
        ''', (source.last_updated, source.id))
        
        conn.commit()
        conn.close()
    
    def get_sources(self):
        """Get all web sources"""
        return list(self.sources.values())
    
    def get_processed_content(self, limit=100):
        """Get recent processed content"""
        conn = sqlite3.connect(self.database_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT * FROM processed_content 
            ORDER BY timestamp DESC 
            LIMIT ?
        ''', (limit,))
        
        rows = cursor.fetchall()
        conn.close()
        
        # Convert to dictionaries
        columns = ['id', 'source_id', 'url', 'title', 'content', 'summary', 
                  'metadata', 'analysis_results', 'timestamp', 'content_hash']
        
        return [dict(zip(columns, row)) for row in rows]
    
    def create_custom_library(self, content_ids):
        """Create custom library from selected content"""
        library = {
            "library_id": f"custom_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            "created_at": datetime.now().isoformat(),
            "content_count": len(content_ids),
            "contents": []
        }
        
        conn = sqlite3.connect(self.database_path)
        cursor = conn.cursor()
        
        for content_id in content_ids:
            cursor.execute('SELECT * FROM processed_content WHERE id = ?', (content_id,))
            row = cursor.fetchone()
            if row:
                columns = ['id', 'source_id', 'url', 'title', 'content', 'summary', 
                          'metadata', 'analysis_results', 'timestamp', 'content_hash']
                content = dict(zip(columns, row))
                library["contents"].append(content)
        
        conn.close()
        
        return library

# Default web sources for The Falcon Press Office
DEFAULT_SOURCES = [
    {
        "name": "BBC News",
        "url": "https://www.bbc.com/news",
        "category": "mainstream",
        "update_frequency": 30,
        "selectors": {
            "title": "h1",
            "content": "[data-component='text-block']",
            "author": "[data-component='byline-block']"
        }
    },
    {
        "name": "Reuters",
        "url": "https://www.reuters.com",
        "category": "agency",
        "update_frequency": 15,
        "selectors": {
            "title": "h1",
            "content": ".ArticleBodyWrapper",
            "author": ".AuthorInfoBody"
        }
    },
    {
        "name": "Associated Press",
        "url": "https://apnews.com",
        "category": "agency",
        "update_frequency": 20,
        "selectors": {
            "title": "h1",
            "content": ".Article",
            "author": ".Component"
        }
    },
    {
        "name": "Al Jazeera",
        "url": "https://www.aljazeera.com",
        "category": "international",
        "update_frequency": 25,
        "selectors": {
            "title": "h1",
            "content": ".wysiwyg",
            "author": ".author-name"
        }
    },
    {
        "name": "CNN",
        "url": "https://www.cnn.com",
        "category": "mainstream",
        "update_frequency": 30,
        "selectors": {
            "title": "h1",
            "content": ".l-container",
            "author": ".byline"
        }
    }
]