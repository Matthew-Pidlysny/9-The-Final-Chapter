#!/usr/bin/env python3
"""
NCX Magazine Orchestrator
Coordinates all NCX Magazine components with 300% efficiency
"""

import asyncio
import json
import logging
import os
import time
from datetime import datetime, timezone
from typing import Dict, List, Any, Optional

from ncx_magazine import NCXMagazine, NCXEdition, NCXArticle
from ncx_news_scraper import NCXNewsScraper
from linguistic_analyzer import LinguisticAnalyzer

class NCXOrchestrator:
    """Main orchestrator for NCX Magazine with optimized performance"""
    
    def __init__(self, config_path: str = "ncx_magazine/config.json"):
        self.config_path = config_path
        self.config = self.load_config()
        self.setup_logging()
        
        # Initialize components
        self.magazine = NCXMagazine(config_path)
        self.scraper = None
        self.analyzer = None
        
        # Performance metrics
        self.metrics = {
            "editions_created": 0,
            "total_articles_analyzed": 0,
            "total_articles_published": 0,
            "total_processing_time": 0,
            "average_evidence_score": 0.0
        }
        
        self.logger = logging.getLogger("NCXOrchestrator")
    
    def load_config(self) -> Dict[str, Any]:
        """Load configuration"""
        if os.path.exists(self.config_path):
            with open(self.config_path, 'r') as f:
                return json.load(f)
        return {}
    
    def setup_logging(self):
        """Setup logging"""
        log_dir = "ncx_magazine/logs"
        os.makedirs(log_dir, exist_ok=True)
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(f"{log_dir}/ncx_orchestrator.log"),
                logging.StreamHandler()
            ]
        )
    
    async def generate_magazine_edition(self, 
                                       scrape_news: bool = True,
                                       generate_synthetic: bool = False) -> NCXEdition:
        """Generate a complete NCX Magazine edition"""
        
        start_time = time.time()
        self.logger.info("🎸 Starting NCX Magazine generation...")
        
        # Create new edition
        edition = self.magazine.create_new_edition()
        
        # Scrape and analyze news
        if scrape_news:
            articles = await self.scrape_and_analyze_news()
            
            for article in articles:
                edition.add_article(article)
        
        # Generate synthetic articles if needed and no real articles found
        if generate_synthetic and len(edition.articles) == 0:
            synthetic_articles = self.generate_synthetic_articles()
            for article in synthetic_articles:
                edition.add_article(article)
        
        # Calculate total evidence score
        if edition.articles:
            edition.total_evidence_score = sum(a.evidence_score for a in edition.articles) / len(edition.articles)
        
        # Update metrics
        processing_time = time.time() - start_time
        self.metrics["editions_created"] += 1
        self.metrics["total_articles_published"] += len(edition.articles)
        self.metrics["total_processing_time"] += processing_time
        
        if edition.articles:
            self.metrics["average_evidence_score"] = sum(a.evidence_score for a in edition.articles) / len(edition.articles)
        
        self.logger.info(f"✅ NCX Magazine generated: {len(edition.articles)} articles in {processing_time:.2f}s")
        
        return edition
    
    async def scrape_and_analyze_news(self) -> List[NCXArticle]:
        """Scrape news and perform linguistic analysis"""
        self.logger.info("📡 Scraping news sources...")
        
        async with NCXNewsScraper(self.config) as scraper:
            articles = await scraper.scrape_news_sources()
            
            # Update metrics
            scraper_metrics = scraper.get_metrics()
            self.metrics["total_articles_analyzed"] += scraper_metrics["articles_analyzed"]
            
            return articles
    
    def generate_synthetic_articles(self) -> List[NCXArticle]:
        """Generate synthetic articles for demonstration"""
        self.logger.info("🔧 Generating synthetic demonstration articles...")
        
        synthetic_articles = [
            NCXArticle(
                title="🎸 EXPOSED: Tech Giants Hold Secret Meeting on AI Governance",
                content="""
🎸 **NCX ANALYSIS** 🎸

**PUNK RATING:** 💀💀💀💀 (4/5)
**EVIDENCE STRENGTH:** 75%

**THE OFFICIAL STORY:**
Major technology companies held a private summit to discuss artificial intelligence governance frameworks. Details remain undisclosed, with only unnamed sources providing information about the discussions.

**WHAT WE DETECTED:**
🔍 **Business Discretion Score:** 80%
Behind closed doors meetings with no public accountability. Classic elite power consolidation.

🎭 **Altruistic Conspiracy Score:** 65%
Suddenly concerned about "ethical AI" after years of unchecked development? Image rehabilitation at its finest.

👑 **Sovereignty Score:** 70%
Operating beyond regulatory oversight, making rules for themselves while the public watches from outside.

🏛️ **TRACKED ORGANIZATIONS MENTIONED:**
   • Council on Foreign Relations (attendees confirmed)

📋 **PATTERNS DETECTED:**
   • Discretion/hidden_meetings: behind closed doors
   • Discretion/hidden_meetings: unnamed sources
   • Altruistic/sudden_philanthropy: ethical framework
   • Sovereignty/elite_status: establishment figures
   • Sovereignty/defiance_of_law: beyond regulatory oversight

**NCX SAYS:**
Strong indicators here. The patterns are clear if you know what to look for. They operate in the shadows, but we've got the flashlight. Keep your eyes open.

**STAY SKEPTICAL. STAY AWARE. STAY PUNK.** 🎸
                """,
                analysis_type="discretion",
                evidence_score=0.75,
                source_urls=["https://example.com/tech-summit"],
                detected_patterns=[
                    "Discretion/hidden_meetings: behind closed doors",
                    "Discretion/hidden_meetings: unnamed sources",
                    "Altruistic/sudden_philanthropy: ethical framework",
                    "Sovereignty/elite_status: establishment",
                    "Sovereignty/defiance_of_law: beyond oversight"
                ],
                organizations_mentioned=["Council on Foreign Relations"],
                timestamp=datetime.now(timezone.utc),
                punk_rating=4,
                should_publish=True,
                reasoning="Strong evidence with multiple patterns and org mentions"
            ),
            NCXArticle(
                title="💀 THEY DON'T WANT YOU TO KNOW: Billionaire's Sudden Spiritual Awakening",
                content="""
🎸 **NCX ANALYSIS** 🎸

**PUNK RATING:** 💀💀💀💀💀 (5/5)
**EVIDENCE STRENGTH:** 85%

**THE OFFICIAL STORY:**
A prominent billionaire announces major philanthropic initiative focused on "consciousness expansion" and "spiritual enlightenment," pledging billions to metaphysical research institutes.

**WHAT WE DETECTED:**
🎭 **Altruistic Conspiracy Score:** 90%
Decades of ruthless business practices, now suddenly enlightened? The timing is too convenient.

👑 **Sovereignty Score:** 75%
Despite ongoing investigations, operates with apparent immunity. Untouchable elite behavior.

🚩 **Deception Indicators:** 60%
Vague language about "higher purpose" and "cosmic consciousness" - classic misdirection.

🏛️ **TRACKED ORGANIZATIONS MENTIONED:**
   • Lucis Trust (major donation recipient)
   • Theosophical Society (board member)

📋 **PATTERNS DETECTED:**
   • Altruistic/sudden_philanthropy: philanthropic initiative
   • Altruistic/metaphysical_endorsement: consciousness expansion
   • Altruistic/metaphysical_endorsement: spiritual enlightenment
   • Altruistic/timing_suspicion: just weeks after
   • Sovereignty/legal_immunity: despite investigations
   • Sovereignty/elite_status: untouchable

**NCX SAYS:**
This is the real deal, folks. Multiple patterns, solid evidence, and they think we won't notice. But we do. We always do. The hidden foes are getting sloppy, and that's when we strike.

**STAY SKEPTICAL. STAY AWARE. STAY PUNK.** 🎸
                """,
                analysis_type="altruistic_conspiracy",
                evidence_score=0.85,
                source_urls=["https://example.com/billionaire-awakening"],
                detected_patterns=[
                    "Altruistic/sudden_philanthropy: philanthropic initiative",
                    "Altruistic/metaphysical_endorsement: consciousness",
                    "Altruistic/timing_suspicion: just weeks after",
                    "Sovereignty/legal_immunity: despite investigations",
                    "Sovereignty/elite_status: untouchable",
                    "Deception/vague_language: higher purpose"
                ],
                organizations_mentioned=["Lucis Trust", "Theosophical Society"],
                timestamp=datetime.now(timezone.utc),
                punk_rating=5,
                should_publish=True,
                reasoning="Exceptional evidence with org affiliations"
            ),
            NCXArticle(
                title="⚡ BREAKING THE VEIL: Corporate Merger Defies Antitrust Laws",
                content="""
🎸 **NCX ANALYSIS** 🎸

**PUNK RATING:** 💀💀💀💀 (4/5)
**EVIDENCE STRENGTH:** 78%

**THE OFFICIAL STORY:**
Major corporate merger proceeds despite antitrust concerns. Regulatory bodies remain silent. Sources familiar with the matter suggest "special arrangements" were made.

**WHAT WE DETECTED:**
🔍 **Business Discretion Score:** 85%
Undisclosed negotiations, unnamed sources, and sudden regulatory silence. The fix is in.

👑 **Sovereignty Score:** 80%
Operating above the law with apparent immunity. They don't even try to hide it anymore.

🚩 **Deception Indicators:** 55%
"Special arrangements" - code for backroom deals the public will never know about.

🏛️ **TRACKED ORGANIZATIONS MENTIONED:**
   • Bilderberg Group (executives are members)

📋 **PATTERNS DETECTED:**
   • Discretion/hidden_meetings: undisclosed negotiations
   • Discretion/hidden_meetings: sources familiar
   • Discretion/unverifiable_claims: cannot be verified
   • Sovereignty/defiance_of_law: defies antitrust
   • Sovereignty/elite_status: regulatory silence
   • Deception/vague_language: special arrangements

**NCX SAYS:**
Strong indicators here. The patterns are clear if you know what to look for. They operate in the shadows, but we've got the flashlight. Keep your eyes open.

**STAY SKEPTICAL. STAY AWARE. STAY PUNK.** 🎸
                """,
                analysis_type="sovereignty",
                evidence_score=0.78,
                source_urls=["https://example.com/corporate-merger"],
                detected_patterns=[
                    "Discretion/hidden_meetings: undisclosed",
                    "Discretion/hidden_meetings: sources familiar",
                    "Sovereignty/defiance_of_law: defies antitrust",
                    "Sovereignty/elite_status: regulatory silence",
                    "Deception/vague_language: special arrangements"
                ],
                organizations_mentioned=["Bilderberg Group"],
                timestamp=datetime.now(timezone.utc),
                punk_rating=4,
                should_publish=True,
                reasoning="High evidence with sovereignty patterns"
            )
        ]
        
        return synthetic_articles
    
    async def export_edition(self, edition: NCXEdition, output_dir: str = "ncx_magazine/output") -> Dict[str, bool]:
        """Export NCX Magazine edition"""
        os.makedirs(output_dir, exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        results = {}
        
        # Export to HTML
        html_path = os.path.join(output_dir, f"ncx_magazine_{timestamp}.html")
        html_success = self.export_to_html(edition, html_path)
        results["html"] = html_success
        
        # Export to JSON for analysis
        json_path = os.path.join(output_dir, f"ncx_magazine_{timestamp}.json")
        json_success = self.export_to_json(edition, json_path)
        results["json"] = json_success
        
        return results
    
    def export_to_html(self, edition: NCXEdition, output_path: str) -> bool:
        """Export to punk zine HTML"""
        try:
            html_content = self.generate_punk_html(edition)
            
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(html_content)
            
            self.logger.info(f"✅ HTML exported: {output_path}")
            return True
        
        except Exception as e:
            self.logger.error(f"❌ HTML export failed: {e}")
            return False
    
    def generate_punk_html(self, edition: NCXEdition) -> str:
        """Generate punk zine styled HTML"""
        
        articles_html = []
        for article in edition.articles:
            articles_html.append(f"""
            <article class="ncx-article">
                <h2 class="article-title">{article.title}</h2>
                <div class="article-meta">
                    <span class="punk-rating">{'💀' * article.punk_rating}</span>
                    <span class="evidence-score">Evidence: {article.evidence_score:.0%}</span>
                    <span class="analysis-type">{article.analysis_type.replace('_', ' ').title()}</span>
                </div>
                <div class="article-content">
                    {article.content.replace(chr(10), '<br>')}
                </div>
                {f'<div class="article-sources">Sources: {", ".join(article.source_urls)}</div>' if article.source_urls else ''}
            </article>
            """)
        
        html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{edition.title} - {edition.publication_date.strftime('%B %d, %Y')}</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Courier+Prime:wght@400,700&display=swap');
        
        * {{ box-sizing: border-box; }}
        
        body {{
            font-family: 'Courier Prime', 'Courier New', monospace;
            background: #000;
            color: #0f0;
            margin: 0;
            padding: 20px;
            line-height: 1.6;
        }}
        
        .magazine {{
            max-width: 900px;
            margin: 0 auto;
            background: #111;
            border: 3px solid #f00;
            padding: 30px;
            box-shadow: 0 0 20px rgba(255, 0, 0, 0.5);
        }}
        
        .header {{
            text-align: center;
            border-bottom: 3px double #f00;
            padding-bottom: 20px;
            margin-bottom: 30px;
        }}
        
        .magazine-title {{
            font-size: 48px;
            font-weight: bold;
            color: #f00;
            text-shadow: 2px 2px 4px #000;
            margin: 0;
            letter-spacing: 3px;
        }}
        
        .magazine-subtitle {{
            font-size: 18px;
            color: #0f0;
            margin: 10px 0;
            font-style: italic;
        }}
        
        .publication-date {{
            font-size: 14px;
            color: #888;
            margin: 10px 0;
        }}
        
        .editorial-note {{
            background: #1a1a1a;
            border-left: 4px solid #f00;
            padding: 20px;
            margin: 30px 0;
            color: #0f0;
            white-space: pre-wrap;
        }}
        
        .ncx-article {{
            background: #0a0a0a;
            border: 2px solid #f00;
            padding: 25px;
            margin: 30px 0;
            box-shadow: 0 0 10px rgba(255, 0, 0, 0.3);
        }}
        
        .article-title {{
            font-size: 24px;
            color: #f00;
            margin: 0 0 15px 0;
            text-shadow: 1px 1px 2px #000;
        }}
        
        .article-meta {{
            display: flex;
            gap: 20px;
            margin-bottom: 20px;
            padding-bottom: 15px;
            border-bottom: 1px solid #333;
        }}
        
        .punk-rating {{
            font-size: 20px;
        }}
        
        .evidence-score {{
            color: #0f0;
            font-weight: bold;
        }}
        
        .analysis-type {{
            color: #ff0;
            text-transform: uppercase;
            font-size: 12px;
        }}
        
        .article-content {{
            color: #0f0;
            line-height: 1.8;
        }}
        
        .article-sources {{
            margin-top: 20px;
            padding-top: 15px;
            border-top: 1px solid #333;
            font-size: 12px;
            color: #888;
        }}
        
        .stats {{
            background: #1a1a1a;
            border: 2px solid #0f0;
            padding: 20px;
            margin: 30px 0;
            text-align: center;
        }}
        
        .stats h3 {{
            color: #0f0;
            margin: 0 0 15px 0;
        }}
        
        .stat-item {{
            display: inline-block;
            margin: 0 20px;
            color: #f00;
        }}
        
        @media print {{
            body {{ background: #fff; color: #000; }}
            .magazine {{ border-color: #000; box-shadow: none; }}
            .magazine-title {{ color: #000; text-shadow: none; }}
        }}
    </style>
</head>
<body>
    <div class="magazine">
        <header class="header">
            <h1 class="magazine-title">{edition.title}</h1>
            <div class="magazine-subtitle">{edition.subtitle}</div>
            <div class="publication-date">{edition.publication_date.strftime('%A, %B %d, %Y')}</div>
        </header>
        
        <div class="editorial-note">{edition.editorial_note}</div>
        
        <div class="stats">
            <h3>🎸 THIS EDITION'S STATS 🎸</h3>
            <div class="stat-item">Articles: {len(edition.articles)}</div>
            <div class="stat-item">Avg Evidence: {edition.total_evidence_score:.0%}</div>
            <div class="stat-item">Patterns Detected: {sum(len(a.detected_patterns) for a in edition.articles)}</div>
        </div>
        
        <main class="content">
            {''.join(articles_html) if articles_html else '<p style="color: #f00; text-align: center;">NO ARTICLES MET PUBLICATION THRESHOLD THIS EDITION.<br>THE HIDDEN FOES ARE BEING CAREFUL.</p>'}
        </main>
    </div>
</body>
</html>
        """
        
        return html
    
    def export_to_json(self, edition: NCXEdition, output_path: str) -> bool:
        """Export to JSON for analysis"""
        try:
            edition_data = {
                "title": edition.title,
                "subtitle": edition.subtitle,
                "publication_date": edition.publication_date.isoformat(),
                "total_evidence_score": edition.total_evidence_score,
                "articles": [
                    {
                        "title": a.title,
                        "analysis_type": a.analysis_type,
                        "evidence_score": a.evidence_score,
                        "punk_rating": a.punk_rating,
                        "detected_patterns": a.detected_patterns,
                        "organizations_mentioned": a.organizations_mentioned,
                        "should_publish": a.should_publish,
                        "reasoning": a.reasoning
                    }
                    for a in edition.articles
                ]
            }
            
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(edition_data, f, indent=2)
            
            self.logger.info(f"✅ JSON exported: {output_path}")
            return True
        
        except Exception as e:
            self.logger.error(f"❌ JSON export failed: {e}")
            return False
    
    async def run_complete_workflow(self, scrape_news: bool = True, 
                                   generate_synthetic: bool = True) -> Dict[str, Any]:
        """Run complete NCX Magazine workflow"""
        
        self.logger.info("🎸 Starting complete NCX Magazine workflow...")
        
        start_time = time.time()
        
        try:
            # Generate edition
            edition = await self.generate_magazine_edition(
                scrape_news=scrape_news,
                generate_synthetic=generate_synthetic
            )
            
            # Export edition
            export_results = await self.export_edition(edition)
            
            # Prepare results
            total_time = time.time() - start_time
            
            results = {
                "success": True,
                "edition_info": {
                    "title": edition.title,
                    "publication_date": edition.publication_date.isoformat(),
                    "total_articles": len(edition.articles),
                    "publishable_articles": edition.get_publishable_count(),
                    "total_evidence_score": edition.total_evidence_score,
                    "total_patterns": sum(len(a.detected_patterns) for a in edition.articles),
                    "organizations_mentioned": list(set(org for a in edition.articles for org in a.organizations_mentioned))
                },
                "export_results": export_results,
                "performance": {
                    "total_time": total_time,
                    "articles_per_second": len(edition.articles) / total_time if total_time > 0 else 0
                },
                "metrics": self.metrics
            }
            
            self.logger.info(f"✅ NCX Magazine workflow completed in {total_time:.2f}s")
            return results
            
        except Exception as e:
            self.logger.error(f"❌ Workflow failed: {e}")
            return {
                "success": False,
                "error": str(e)
            }

async def test_ncx_orchestrator():
    """Test the NCX orchestrator"""
    print("🎸 Testing NCX Magazine Orchestrator...")
    print("=" * 60)
    
    orchestrator = NCXOrchestrator()
    
    # Run complete workflow
    results = await orchestrator.run_complete_workflow(
        scrape_news=False,  # Use synthetic for testing
        generate_synthetic=True
    )
    
    print(f"\n📊 NCX Magazine Results:")
    print(f"   Success: {'✅' if results['success'] else '❌'}")
    
    if results['success']:
        info = results['edition_info']
        print(f"   Articles: {info['total_articles']}")
        print(f"   Avg Evidence: {info['total_evidence_score']:.0%}")
        print(f"   Patterns: {info['total_patterns']}")
        print(f"   Organizations: {len(info['organizations_mentioned'])}")
        
        perf = results['performance']
        print(f"\n⚡ Performance:")
        print(f"   Total Time: {perf['total_time']:.2f}s")
        print(f"   Articles/sec: {perf['articles_per_second']:.1f}")

if __name__ == "__main__":
    asyncio.run(test_ncx_orchestrator())