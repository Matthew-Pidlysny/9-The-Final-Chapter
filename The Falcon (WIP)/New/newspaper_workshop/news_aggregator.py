#!/usr/bin/env python3
"""
News Aggregator Module for Newspaper Workshop
Handles fetching news from RSS feeds and other sources
"""

import asyncio
import aiohttp
import feedparser
import json
import logging
from datetime import datetime, timezone
from typing import List, Dict, Any, Optional
from dataclasses import asdict

from newspaper_workshop import NewsArticle

class NewsAggregator:
    """News aggregation system"""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.logger = logging.getLogger("NewsAggregator")
        self.session = None
        
    async def __aenter__(self):
        """Async context manager entry"""
        self.session = aiohttp.ClientSession(
            timeout=aiohttp.ClientTimeout(total=30),
            headers={'User-Agent': 'Newspaper-Workshop/1.0'}
        )
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit"""
        if self.session:
            await self.session.close()
    
    async def fetch_rss_feed(self, feed_url: str) -> List[NewsArticle]:
        """Fetch articles from an RSS feed"""
        try:
            async with self.session.get(feed_url) as response:
                if response.status == 200:
                    content = await response.text()
                    feed = feedparser.parse(content)
                    
                    articles = []
                    for entry in feed.entries[:self.config.get("max_articles_per_section", 10)]:
                        article = self.parse_rss_entry(entry, feed_url)
                        if article:
                            articles.append(article)
                    
                    self.logger.info(f"Fetched {len(articles)} articles from {feed_url}")
                    return articles
                else:
                    self.logger.error(f"Failed to fetch {feed_url}: HTTP {response.status}")
                    return []
        
        except Exception as e:
            self.logger.error(f"Error fetching RSS feed {feed_url}: {e}")
            return []
    
    def parse_rss_entry(self, entry: Any, source_url: str) -> Optional[NewsArticle]:
        """Parse a single RSS entry into a NewsArticle"""
        try:
            # Extract basic information
            title = getattr(entry, 'title', 'No Title')
            content = getattr(entry, 'description', '') or getattr(entry, 'summary', '')
            
            # Clean content
            if content:
                # Remove HTML tags (basic cleaning)
                import re
                content = re.sub(r'<[^>]+>', '', content)
                content = content.strip()
            
            # Skip if too short
            if len(content.split()) < self.config.get("min_article_length", 200) // 10:
                return None
            
            # Extract publication date
            published = getattr(entry, 'published', None)
            if published:
                try:
                    timestamp = datetime(*entry.published_parsed[:6], tzinfo=timezone.utc)
                except:
                    timestamp = datetime.now(timezone.utc)
            else:
                timestamp = datetime.now(timezone.utc)
            
            # Extract author
            author = getattr(entry, 'author', None)
            
            # Extract URL
            url = getattr(entry, 'link', None)
            
            # Determine category (basic categorization)
            category = self.categorize_article(title, content)
            
            # Extract keywords (basic)
            keywords = self.extract_keywords(title + " " + content)
            
            return NewsArticle(
                title=title,
                content=content,
                source=self.extract_source_name(source_url),
                category=category,
                timestamp=timestamp,
                url=url,
                author=author,
                keywords=keywords
            )
        
        except Exception as e:
            self.logger.error(f"Error parsing RSS entry: {e}")
            return None
    
    def extract_source_name(self, url: str) -> str:
        """Extract source name from URL"""
        try:
            from urllib.parse import urlparse
            domain = urlparse(url).netloc
            return domain.replace('www.', '').split('.')[0].title()
        except:
            return "Unknown Source"
    
    def categorize_article(self, title: str, content: str) -> str:
        """Basic categorization based on keywords"""
        text = (title + " " + content).lower()
        
        # Define category keywords
        categories = {
            "World News": ["world", "international", "global", "foreign", "country", "nation"],
            "Technology": ["tech", "technology", "software", "hardware", "computer", "internet", "digital"],
            "Mathematics & Sciences": ["science", "research", "study", "mathematics", "physics", "chemistry", "biology"],
            "Culture & Society": ["culture", "society", "arts", "entertainment", "lifestyle", "people"],
            "Opinions & Analysis": ["opinion", "analysis", "editorial", "commentary", "perspective"],
            "Headlines": ["breaking", "urgent", "major", "important", "news"]
        }
        
        # Score each category
        scores = {}
        for category, keywords in categories.items():
            score = sum(1 for keyword in keywords if keyword in text)
            scores[category] = score
        
        # Return category with highest score, or "Headlines" if no matches
        if max(scores.values()) == 0:
            return "Headlines"
        
        return max(scores, key=scores.get)
    
    def extract_keywords(self, text: str) -> List[str]:
        """Extract basic keywords from text"""
        # Simple keyword extraction - just get common words
        words = text.lower().split()
        # Filter out common stop words
        stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'is', 'are', 'was', 'were', 'be', 'been', 'have', 'has', 'had', 'will', 'would', 'could', 'should'}
        
        keywords = [word for word in words if word not in stop_words and len(word) > 3]
        
        # Return top 10 most common words
        from collections import Counter
        word_counts = Counter(keywords)
        return [word for word, count in word_counts.most_common(10)]
    
    async def fetch_all_news(self) -> List[NewsArticle]:
        """Fetch news from all configured sources"""
        all_articles = []
        
        # Fetch from RSS feeds
        rss_feeds = self.config.get("news_sources", {}).get("rss_feeds", [])
        
        tasks = [self.fetch_rss_feed(feed_url) for feed_url in rss_feeds]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        for result in results:
            if isinstance(result, list):
                all_articles.extend(result)
            elif isinstance(result, Exception):
                self.logger.error(f"Error in news aggregation: {result}")
        
        # Remove duplicates based on title similarity
        unique_articles = self.remove_duplicates(all_articles)
        
        self.logger.info(f"Fetched {len(unique_articles)} unique articles total")
        return unique_articles
    
    def remove_duplicates(self, articles: List[NewsArticle]) -> List[NewsArticle]:
        """Remove duplicate articles based on title similarity"""
        seen_titles = set()
        unique_articles = []
        
        for article in articles:
            # Simple duplicate detection - exact title match
            title_key = article.title.lower().strip()
            if title_key not in seen_titles:
                seen_titles.add(title_key)
                unique_articles.append(article)
        
        return unique_articles

async def test_news_aggregator():
    """Test function for news aggregator"""
    config = {
        "max_articles_per_section": 5,
        "min_article_length": 100,
        "news_sources": {
            "rss_feeds": [
                "https://rss.cnn.com/rss/edition.rss",
                "https://feeds.bbci.co.uk/news/rss.xml"
            ]
        }
    }
    
    async with NewsAggregator(config) as aggregator:
        articles = await aggregator.fetch_all_news()
        
        print(f"Fetched {len(articles)} articles:")
        for i, article in enumerate(articles[:3]):  # Show first 3
            print(f"\n{i+1}. {article.title}")
            print(f"   Source: {article.source}")
            print(f"   Category: {article.category}")
            print(f"   Words: {article.word_count}")
            print(f"   Keywords: {', '.join(article.keywords[:5])}")

if __name__ == "__main__":
    asyncio.run(test_news_aggregator())