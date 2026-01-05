#!/usr/bin/env python3
"""
NCX News Scraper
Scrapes business news and analyzes for hidden patterns
"""

import asyncio
import aiohttp
import feedparser
import logging
from datetime import datetime, timezone
from typing import Dict, List, Any, Optional
from dataclasses import asdict

from ncx_magazine import NCXArticle
from linguistic_analyzer import LinguisticAnalyzer

class NCXNewsScraper:
    """News scraper with linguistic analysis for NCX Magazine"""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.logger = logging.getLogger("NCXNewsScraper")
        self.session = None
        
        # Initialize linguistic analyzer
        self.analyzer = LinguisticAnalyzer(config)
        
        # Metrics
        self.metrics = {
            "articles_scraped": 0,
            "articles_analyzed": 0,
            "articles_published": 0,
            "patterns_detected": 0
        }
    
    async def __aenter__(self):
        """Async context manager entry"""
        self.session = aiohttp.ClientSession(
            timeout=aiohttp.ClientTimeout(total=30),
            headers={'User-Agent': 'NCX-Magazine/1.0 (Truth-Seeking Bot)'}
        )
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit"""
        if self.session:
            await self.session.close()
    
    async def scrape_news_sources(self) -> List[NCXArticle]:
        """Scrape and analyze news from configured sources"""
        self.logger.info("Starting NCX news scraping...")
        
        rss_feeds = self.config.get("news_sources", {}).get("rss_feeds", [])
        
        all_articles = []
        
        for feed_url in rss_feeds:
            try:
                articles = await self.scrape_rss_feed(feed_url)
                all_articles.extend(articles)
            except Exception as e:
                self.logger.error(f"Error scraping {feed_url}: {e}")
        
        # Filter for publishable articles only
        publishable = [a for a in all_articles if a.should_publish]
        
        self.logger.info(f"Scraped {len(all_articles)} articles, {len(publishable)} publishable")
        return publishable
    
    async def scrape_rss_feed(self, feed_url: str) -> List[NCXArticle]:
        """Scrape and analyze a single RSS feed"""
        try:
            async with self.session.get(feed_url) as response:
                if response.status == 200:
                    content = await response.text()
                    feed = feedparser.parse(content)
                    
                    articles = []
                    for entry in feed.entries[:20]:  # Limit to 20 per feed
                        article = await self.process_entry(entry, feed_url)
                        if article:
                            articles.append(article)
                    
                    return articles
                else:
                    self.logger.error(f"Failed to fetch {feed_url}: HTTP {response.status}")
                    return []
        
        except Exception as e:
            self.logger.error(f"Error fetching RSS feed {feed_url}: {e}")
            return []
    
    async def process_entry(self, entry: Any, source_url: str) -> Optional[NCXArticle]:
        """Process a single RSS entry with linguistic analysis"""
        try:
            self.metrics["articles_scraped"] += 1
            
            # Extract basic information
            title = getattr(entry, 'title', 'No Title')
            content = getattr(entry, 'description', '') or getattr(entry, 'summary', '')
            url = getattr(entry, 'link', '')
            
            # Clean content
            import re
            content = re.sub(r'<[^>]+>', '', content)
            content = content.strip()
            
            # Skip if too short
            if len(content.split()) < 50:
                return None
            
            # Combine title and content for analysis
            full_text = f"{title}\n\n{content}"
            
            # Perform linguistic analysis
            analysis = self.analyzer.analyze_text(full_text, url)
            self.metrics["articles_analyzed"] += 1
            
            # Only create article if it should be published
            if not analysis["should_publish"]:
                return None
            
            # Determine analysis type based on highest score
            scores = {
                "discretion": analysis["discretion_score"],
                "altruistic_conspiracy": analysis["altruistic_score"],
                "sovereignty": analysis["sovereignty_score"]
            }
            analysis_type = max(scores, key=scores.get)
            
            # Create NCX article
            article = NCXArticle(
                title=self.punkify_title(title),
                content=self.generate_ncx_content(title, content, analysis),
                analysis_type=analysis_type,
                evidence_score=analysis["evidence_strength"],
                source_urls=[url] if url else [],
                detected_patterns=analysis["detected_patterns"],
                organizations_mentioned=analysis["organization_mentions"],
                timestamp=datetime.now(timezone.utc),
                punk_rating=analysis["punk_rating"],
                should_publish=True,
                reasoning=analysis["reasoning"]
            )
            
            self.metrics["articles_published"] += 1
            self.metrics["patterns_detected"] += len(analysis["detected_patterns"])
            
            return article
        
        except Exception as e:
            self.logger.error(f"Error processing entry: {e}")
            return None
    
    def punkify_title(self, title: str) -> str:
        """Add punk zine flair to titles"""
        punk_prefixes = [
            "🎸 EXPOSED:",
            "💀 THEY DON'T WANT YOU TO KNOW:",
            "⚡ BREAKING THE VEIL:",
            "🔥 PATTERN DETECTED:",
            "👁️ SEEING THROUGH:",
            "🚨 ALERT:",
            "💣 UNCOVERED:"
        ]
        
        import random
        prefix = random.choice(punk_prefixes)
        return f"{prefix} {title}"
    
    def generate_ncx_content(self, title: str, original_content: str, 
                            analysis: Dict[str, Any]) -> str:
        """Generate NCX-style article content with analysis"""
        
        # Build the NCX article
        ncx_content = []
        
        # Opening hook
        ncx_content.append("🎸 **NCX ANALYSIS** 🎸\n")
        
        # Evidence rating
        skulls = "💀" * analysis["punk_rating"]
        ncx_content.append(f"**PUNK RATING:** {skulls} ({analysis['punk_rating']}/5)")
        ncx_content.append(f"**EVIDENCE STRENGTH:** {analysis['evidence_strength']:.0%}\n")
        
        # Original story summary
        ncx_content.append("**THE OFFICIAL STORY:**")
        ncx_content.append(f"{original_content[:300]}...\n")
        
        # What we detected
        ncx_content.append("**WHAT WE DETECTED:**")
        
        if analysis["discretion_score"] > 0.3:
            ncx_content.append(f"🔍 **Business Discretion Score:** {analysis['discretion_score']:.0%}")
            ncx_content.append("They're making moves behind closed doors. Classic power play.")
        
        if analysis["altruistic_score"] > 0.3:
            ncx_content.append(f"🎭 **Altruistic Conspiracy Score:** {analysis['altruistic_score']:.0%}")
            ncx_content.append("Sudden philanthropy? Image rehabilitation? We see you.")
        
        if analysis["sovereignty_score"] > 0.3:
            ncx_content.append(f"👑 **Sovereignty Score:** {analysis['sovereignty_score']:.0%}")
            ncx_content.append("Acting like they're above the law. Untouchable elite behavior.")
        
        if analysis["deception_score"] > 0.2:
            ncx_content.append(f"🚩 **Deception Indicators:** {analysis['deception_score']:.0%}")
            ncx_content.append("Vague language, misdirection, contradictions. Red flags everywhere.")
        
        # Organizations mentioned
        if analysis["organization_mentions"]:
            ncx_content.append(f"\n🏛️ **TRACKED ORGANIZATIONS MENTIONED:**")
            for org in analysis["organization_mentions"]:
                ncx_content.append(f"   • {org}")
        
        # Key patterns detected
        if analysis["detected_patterns"]:
            ncx_content.append(f"\n📋 **PATTERNS DETECTED:**")
            for pattern in analysis["detected_patterns"][:5]:  # Top 5
                ncx_content.append(f"   • {pattern}")
        
        # NCX commentary
        ncx_content.append("\n**NCX SAYS:**")
        ncx_content.append(self.generate_commentary(analysis))
        
        # Call to action
        ncx_content.append("\n**STAY SKEPTICAL. STAY AWARE. STAY PUNK.** 🎸")
        
        return "\n".join(ncx_content)
    
    def generate_commentary(self, analysis: Dict[str, Any]) -> str:
        """Generate punk zine commentary based on analysis"""
        evidence = analysis["evidence_strength"]
        
        if evidence >= 0.8:
            return ("This is the real deal, folks. Multiple patterns, solid evidence, "
                   "and they think we won't notice. But we do. We always do. "
                   "The hidden foes are getting sloppy, and that's when we strike.")
        
        elif evidence >= 0.7:
            return ("Strong indicators here. The patterns are clear if you know what "
                   "to look for. They operate in the shadows, but we've got the "
                   "flashlight. Keep your eyes open.")
        
        elif evidence >= 0.6:
            return ("Solid evidence of their games. They think the public won't "
                   "connect the dots, but that's what we're here for. Pattern "
                   "recognition is our weapon.")
        
        else:
            return ("Interesting patterns emerging. Not conclusive yet, but worth "
                   "watching. Remember: they count on us not paying attention. "
                   "Don't give them that satisfaction.")
    
    def get_metrics(self) -> Dict[str, Any]:
        """Get scraping metrics"""
        return {
            **self.metrics,
            "publish_rate": self.metrics["articles_published"] / max(1, self.metrics["articles_analyzed"]),
            "analyzer_metrics": self.analyzer.get_metrics()
        }

async def test_ncx_scraper():
    """Test the NCX news scraper"""
    config = {
        "minimum_evidence_score": 0.6,
        "minimum_punk_rating": 3,
        "tracked_organizations": [
            "Lucis Trust",
            "Theosophical Society",
            "Freemasons",
            "Bilderberg Group"
        ],
        "news_sources": {
            "rss_feeds": [
                "https://feeds.bbci.co.uk/news/business/rss.xml"
            ]
        }
    }
    
    print("🎸 Testing NCX News Scraper...")
    print("=" * 60)
    
    async with NCXNewsScraper(config) as scraper:
        articles = await scraper.scrape_news_sources()
        
        print(f"\n📊 Scraping Results:")
        print(f"   Articles found: {len(articles)}")
        
        if articles:
            print(f"\n📰 Sample Article:")
            article = articles[0]
            print(f"   Title: {article.title}")
            print(f"   Type: {article.analysis_type}")
            print(f"   Evidence: {article.evidence_score:.0%}")
            print(f"   Punk Rating: {'💀' * article.punk_rating}")
            print(f"   Patterns: {len(article.detected_patterns)}")
            print(f"   Organizations: {len(article.organizations_mentioned)}")
        
        metrics = scraper.get_metrics()
        print(f"\n📈 Metrics:")
        print(f"   Scraped: {metrics['articles_scraped']}")
        print(f"   Analyzed: {metrics['articles_analyzed']}")
        print(f"   Published: {metrics['articles_published']}")
        print(f"   Publish Rate: {metrics['publish_rate']:.1%}")

if __name__ == "__main__":
    asyncio.run(test_ncx_scraper())