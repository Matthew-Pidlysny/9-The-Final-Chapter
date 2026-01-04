#!/usr/bin/env python3
"""
Newspaper Workshop Orchestrator
Main controller that coordinates all newspaper generation components
"""

import asyncio
import json
import logging
import os
from datetime import datetime, timezone
from typing import Dict, List, Any, Optional

from newspaper_workshop import NewspaperWorkshop, NewspaperEdition, NewspaperSection, NewsArticle
from news_aggregator import NewsAggregator
from ai_article_generator import AIArticleGenerator
from layout_export import PDFExporter, ConsistencyValidator

class NewspaperWorkshopOrchestrator:
    """Main orchestrator for the Newspaper Workshop"""
    
    def __init__(self, config_path: str = "newspaper_workshop/config.json"):
        self.config_path = config_path
        self.config = self.load_config()
        self.setup_logging()
        
        # Initialize components
        self.workshop = NewspaperWorkshop(config_path)
        self.news_aggregator = None
        self.ai_generator = None
        self.pdf_exporter = None
        self.validator = None
        
        self.logger = logging.getLogger("WorkshopOrchestrator")
    
    def load_config(self) -> Dict[str, Any]:
        """Load configuration"""
        if os.path.exists(self.config_path):
            with open(self.config_path, 'r') as f:
                return json.load(f)
        return {}
    
    def setup_logging(self):
        """Setup logging"""
        log_dir = "newspaper_workshop/logs"
        os.makedirs(log_dir, exist_ok=True)
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(f"{log_dir}/orchestrator.log"),
                logging.StreamHandler()
            ]
        )
    
    async def initialize_components(self):
        """Initialize all workshop components"""
        self.logger.info("Initializing Newspaper Workshop components...")
        
        # Initialize components
        self.ai_generator = AIArticleGenerator(self.config)
        self.pdf_exporter = PDFExporter(self.config)
        self.validator = ConsistencyValidator(self.config)
        
        self.logger.info("All components initialized successfully")
    
    async def generate_complete_newspaper(self, 
                                        include_real_news: bool = True,
                                        include_ai_articles: bool = True,
                                        articles_per_section: int = 3) -> NewspaperEdition:
        """Generate a complete newspaper with both real and AI-generated content"""
        
        self.logger.info("Starting complete newspaper generation...")
        
        # Create new edition
        edition = self.workshop.create_new_edition()
        
        # Add editorial note
        edition.editorial_note = (
            "Welcome to The Falcon Press. This newspaper is generated using advanced AI technology "
            "and aggregated from multiple international news sources. We strive to provide balanced, "
            "factual reporting while avoiding loaded language and maintaining respect for all perspectives."
        )
        
        if include_real_news:
            await self.add_real_news(edition)
        
        if include_ai_articles:
            await self.add_ai_articles(edition, articles_per_section)
        
        # Add mathematics section with LaTeX content
        await self.add_mathematics_section(edition)
        
        self.logger.info(f"Newspaper generation completed: {edition.get_total_articles()} articles")
        return edition
    
    async def add_real_news(self, edition: NewspaperEdition):
        """Add real news articles to the newspaper"""
        self.logger.info("Fetching real news articles...")
        
        async with NewsAggregator(self.config) as aggregator:
            real_articles = await aggregator.fetch_all_news()
            
            # Distribute articles across sections
            for article in real_articles:
                if article.category in edition.sections:
                    section = edition.sections[article.category]
                    if len(section.articles) < self.config.get("max_articles_per_section", 10):
                        section.add_article(article)
        
        self.logger.info(f"Added {len(real_articles)} real news articles")
    
    async def add_ai_articles(self, edition: NewspaperEdition, articles_per_section: int):
        """Add AI-generated articles to fill out sections"""
        self.logger.info("Generating AI articles...")
        
        # Determine which sections need articles
        sections_to_fill = {}
        for section_name, section in edition.sections.items():
            needed = max(0, articles_per_section - len(section.articles))
            if needed > 0:
                sections_to_fill[section_name] = needed
        
        # Generate AI articles
        ai_articles = self.ai_generator.generate_articles_for_sections(sections_to_fill)
        
        # Add articles to sections
        for section_name, articles in ai_articles.items():
            section = edition.sections[section_name]
            for article in articles:
                section.add_article(article)
        
        self.logger.info(f"Generated AI articles for {len(sections_to_fill)} sections")
    
    async def add_mathematics_section(self, edition: NewspaperEdition):
        """Add mathematics section with LaTeX content"""
        self.logger.info("Adding mathematics section with LaTeX content...")
        
        # Create sample math articles with formulas
        math_articles = [
            self.create_calculus_article(),
            self.create_linear_algebra_article(),
            self.create_probability_article()
        ]
        
        math_section = edition.sections.get("Mathematics & Sciences")
        if math_section:
            for article in math_articles:
                math_section.add_article(article)
        
        self.logger.info(f"Added {len(math_articles)} mathematics articles")
    
    def create_calculus_article(self) -> NewsArticle:
        """Create calculus article with LaTeX formulas"""
        content = """
Fundamental Theorem of Calculus in Modern Applications

The fundamental theorem of calculus represents one of the most elegant connections in mathematics, linking the seemingly unrelated concepts of differentiation and integration.

The theorem states that if $f$ is continuous on $[a,b]$ and $F$ is an antiderivative of $f$, then:
$$\\int_a^b f(x)\\,dx = F(b) - F(a)$$

This relationship has profound implications in physics, engineering, and economics. In physics, it allows us to calculate work done by variable forces, while in economics it helps model accumulated changes over time.

The proof of this theorem involves understanding the concept of the definite integral as the limit of Riemann sums:
$$\\int_a^b f(x)\\,dx = \\lim_{n \\to \\infty} \\sum_{i=1}^{n} f(x_i^*) \\Delta x$$

Modern applications include optimization problems in machine learning, where gradient-based methods use the fundamental theorem to minimize loss functions by finding critical points where the derivative equals zero.
        """
        
        return NewsArticle(
            title="The Beauty of Integration: From Theory to Practice",
            content=content,
            source="Mathematics Department",
            category="Mathematics & Sciences",
            timestamp=datetime.now(timezone.utc),
            author="Prof. Sarah Chen",
            keywords=["calculus", "integration", "fundamental theorem", "applications"]
        )
    
    def create_linear_algebra_article(self) -> NewsArticle:
        """Create linear algebra article with LaTeX formulas"""
        content = """
Linear Algebra: The Foundation of Data Science

Linear algebra provides the mathematical framework for understanding and manipulating multidimensional data, making it essential for modern data science and machine learning.

At its core, linear algebra studies vector spaces and linear mappings between them. A system of linear equations can be represented in matrix form:
$$A\\mathbf{x} = \\mathbf{b}$$

Where $A$ is an $m \\times n$ matrix, $\\mathbf{x}$ is an $n \\times 1$ vector of unknowns, and $\\mathbf{b}$ is an $m \\times 1$ vector of constants.

The solution exists and is unique if and only if $\\text{rank}(A) = \\text{rank}([A|\\mathbf{b}]) = n$, where $[A|\\mathbf{b}]$ represents the augmented matrix.

Eigenvalues and eigenvectors play a crucial role in many applications. For a square matrix $A$, the eigenvalue equation is:
$$A\\mathbf{v} = \\lambda \\mathbf{v}$$

This concept underlies principal component analysis (PCA), where we find the directions of maximum variance in data by computing the eigenvectors of the covariance matrix:
$$\\Sigma = \\frac{1}{n-1} \\sum_{i=1}^{n} (\\mathbf{x}_i - \\bar{\\mathbf{x}})(\\mathbf{x}_i - \\bar{\\mathbf{x}})^T$$

These mathematical tools enable us to reduce dimensionality, identify patterns, and build predictive models that power modern artificial intelligence systems.
        """
        
        return NewsArticle(
            title="Matrix Transformations: Unlocking Multidimensional Insights",
            content=content,
            source="Applied Mathematics",
            category="Mathematics & Sciences",
            timestamp=datetime.now(timezone.utc),
            author="Dr. Michael Rodriguez",
            keywords=["linear algebra", "matrices", "eigenvalues", "data science"]
        )
    
    def create_probability_article(self) -> NewsArticle:
        """Create probability article with LaTeX formulas"""
        content = """
Probability Theory: Quantifying Uncertainty

Probability theory provides the mathematical framework for quantifying uncertainty and making informed decisions under incomplete information.

The probability of an event $A$ is defined as:
$$P(A) = \\frac{\\text{Number of favorable outcomes}}{\\text{Total number of possible outcomes}}$$

For two events $A$ and $B$, the probability of their union is given by:
$$P(A \\cup B) = P(A) + P(B) - P(A \\cap B)$$

Conditional probability, introduced by Bayes, allows us to update our beliefs based on new information:
$$P(A|B) = \\frac{P(B|A) \\cdot P(A)}{P(B)}$$

The concept of expected value provides a measure of the center of a probability distribution. For a discrete random variable $X$ with probability mass function $p(x)$:
$$E[X] = \\sum_{x} x \\cdot p(x)$$

In the continuous case, with probability density function $f(x)$:
$$E[X] = \\int_{-\\infty}^{\\infty} x f(x)\\,dx$$

The central limit theorem states that the sum of independent, identically distributed random variables approaches a normal distribution:
$$\\frac{\\bar{X}_n - \\mu}{\\sigma/\\sqrt{n}} \\xrightarrow{d} N(0,1)$$

This fundamental result enables hypothesis testing, confidence intervals, and many other statistical procedures that form the backbone of modern scientific research and data analysis.
        """
        
        return NewsArticle(
            title="The Mathematics of Chance: From Dice to Data Analytics",
            content=content,
            source="Statistics Department",
            category="Mathematics & Sciences",
            timestamp=datetime.now(timezone.utc),
            author="Dr. Lisa Thompson",
            keywords=["probability", "statistics", "bayes", "expected value"]
        )
    
    async def export_newspaper(self, edition: NewspaperEdition, 
                             output_dir: str = "newspaper_workshop/output",
                             formats: List[str] = None) -> Dict[str, bool]:
        """Export newspaper to specified formats"""
        
        if formats is None:
            formats = self.config.get("export_formats", ["html", "pdf"])
        
        results = {}
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        os.makedirs(output_dir, exist_ok=True)
        
        # Validate before export
        if self.config.get("consistency_checks", True):
            validation = self.validator.validate_edition(edition)
            if not validation["is_valid"]:
                self.logger.error("Newspaper validation failed. Export aborted.")
                return {"validation_failed": True}
            
            self.logger.info(f"Newspaper validation passed: {validation['statistics']}")
        
        # Export to each format
        base_filename = f"falcon_press_{timestamp}"
        
        for format_type in formats:
            try:
                if format_type.lower() == "html":
                    output_path = os.path.join(output_dir, f"{base_filename}.html")
                    success = self.pdf_exporter.export_to_html(edition, output_path)
                    results["html"] = success
                    
                elif format_type.lower() == "pdf":
                    output_path = os.path.join(output_dir, f"{base_filename}.pdf")
                    success = self.pdf_exporter.export_to_pdf(edition, output_path)
                    results["pdf"] = success
                    
                else:
                    self.logger.warning(f"Unsupported export format: {format_type}")
                    results[format_type] = False
                    
            except Exception as e:
                self.logger.error(f"Error exporting to {format_type}: {e}")
                results[format_type] = False
        
        return results
    
    async def run_complete_workflow(self, 
                                  include_real_news: bool = True,
                                  include_ai_articles: bool = True,
                                  articles_per_section: int = 3,
                                  export_formats: List[str] = None) -> Dict[str, Any]:
        """Run the complete newspaper generation workflow"""
        
        self.logger.info("Starting complete Newspaper Workshop workflow...")
        
        try:
            # Initialize components
            await self.initialize_components()
            
            # Generate newspaper
            edition = await self.generate_complete_newspaper(
                include_real_news=include_real_news,
                include_ai_articles=include_ai_articles,
                articles_per_section=articles_per_section
            )
            
            # Export newspaper
            export_results = await self.export_newspaper(edition, formats=export_formats)
            
            # Prepare results
            results = {
                "success": True,
                "edition_info": {
                    "title": edition.title,
                    "publication_date": edition.publication_date.isoformat(),
                    "total_articles": edition.get_total_articles(),
                    "total_words": edition.get_total_word_count(),
                    "sections": {name: len(section.articles) for name, section in edition.sections.items()}
                },
                "export_results": export_results
            }
            
            self.logger.info(f"Workflow completed successfully: {edition.get_total_articles()} articles generated")
            return results
            
        except Exception as e:
            self.logger.error(f"Workflow failed: {e}")
            return {
                "success": False,
                "error": str(e)
            }

async def main():
    """Main function to run the Newspaper Workshop"""
    orchestrator = NewspaperWorkshopOrchestrator()
    
    # Run complete workflow
    results = await orchestrator.run_complete_workflow(
        include_real_news=False,  # Set to False for testing without internet
        include_ai_articles=True,
        articles_per_section=2,
        export_formats=["html", "pdf"]
    )
    
    print("\nNewspaper Workshop Results:")
    print(json.dumps(results, indent=2, default=str))

if __name__ == "__main__":
    asyncio.run(main())