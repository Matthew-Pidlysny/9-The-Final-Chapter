#!/usr/bin/env python3
"""
Layout and Export Module for Newspaper Workshop
Handles newspaper layout design and PDF export with LaTeX support
"""

import os
import logging
from datetime import datetime
from typing import Dict, List, Any, Optional
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration
import base64

from newspaper_workshop import NewspaperEdition, NewspaperSection, NewsArticle

class NewspaperLayout:
    """Newspaper layout and design system"""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.logger = logging.getLogger("NewspaperLayout")
        self.font_config = FontConfiguration()
        
        # Layout settings
        self.layout_settings = config.get("layout", {
            "columns": 3,
            "font_family": "Times New Roman",
            "font_size": 12,
            "margin": "1 inch",
            "header_height": "2 inches"
        })
    
    def create_html_template(self, edition: NewspaperEdition) -> str:
        """Create HTML template for the newspaper"""
        
        # HTML structure with newspaper styling
        html_template = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{edition.title} - {edition.publication_date.strftime('%B %d, %Y')}</title>
    <style>
        /* Newspaper Styles */
        @page {{
            size: A4;
            margin: {self.layout_settings['margin']};
            @top-center {{
                content: "{edition.title}";
                font-size: 14px;
                font-weight: bold;
            }}
            @bottom-center {{
                content: "Page " counter(page);
                font-size: 10px;
            }}
        }}
        
        body {{
            font-family: '{self.layout_settings['font_family']}', serif;
            font-size: {self.layout_settings['font_size']}px;
            line-height: 1.4;
            color: #000;
            background: #fff;
        }}
        
        .newspaper {{
            width: 100%;
            max-width: 210mm; /* A4 width */
            margin: 0 auto;
        }}
        
        .header {{
            text-align: center;
            border-bottom: 3px double #000;
            padding-bottom: 10px;
            margin-bottom: 20px;
        }}
        
        .newspaper-title {{
            font-size: 48px;
            font-weight: bold;
            letter-spacing: 2px;
            margin: 0;
            text-transform: uppercase;
        }}
        
        .newspaper-subtitle {{
            font-size: 18px;
            font-style: italic;
            margin: 5px 0;
            color: #333;
        }}
        
        .publication-date {{
            font-size: 14px;
            margin: 10px 0;
        }}
        
        .content {{
            display: flex;
            flex-direction: column;
            gap: 30px;
        }}
        
        .section {{
            margin-bottom: 40px;
            page-break-inside: avoid;
        }}
        
        .section-header {{
            font-size: 24px;
            font-weight: bold;
            border-bottom: 2px solid #000;
            padding-bottom: 5px;
            margin-bottom: 15px;
            text-transform: uppercase;
        }}
        
        .articles-grid {{
            display: grid;
            grid-template-columns: repeat({self.layout_settings['columns']}, 1fr);
            gap: 20px;
        }}
        
        .article {{
            border: 1px solid #ccc;
            padding: 15px;
            break-inside: avoid-column;
            background: #fff;
        }}
        
        .article-title {{
            font-size: 16px;
            font-weight: bold;
            margin-bottom: 8px;
            line-height: 1.2;
        }}
        
        .article-meta {{
            font-size: 10px;
            color: #666;
            margin-bottom: 10px;
            font-style: italic;
        }}
        
        .article-content {{
            font-size: 11px;
            line-height: 1.4;
            text-align: justify;
        }}
        
        .math-section {{
            background: #f8f8f8;
            border-left: 4px solid #0066cc;
            padding: 15px;
            margin: 15px 0;
        }}
        
        .latex-formula {{
            font-family: 'Computer Modern', serif;
            font-style: italic;
            text-align: center;
            margin: 10px 0;
            padding: 10px;
            background: #f0f0f0;
            border: 1px solid #ddd;
        }}
        
        .editorial-note {{
            background: #f9f9f9;
            border: 1px solid #ddd;
            padding: 15px;
            font-style: italic;
            margin: 20px 0;
            text-align: center;
        }}
        
        /* Print-specific styles */
        @media print {{
            .section {{ page-break-inside: avoid; }}
            .article {{ break-inside: avoid-column; }}
        }}
    </style>
</head>
<body>
    <div class="newspaper">
        {self.generate_header_html(edition)}
        {self.generate_content_html(edition)}
    </div>
</body>
</html>
"""
        return html_template
    
    def generate_header_html(self, edition: NewspaperEdition) -> str:
        """Generate HTML for newspaper header"""
        return f"""
        <header class="header">
            <h1 class="newspaper-title">{edition.title}</h1>
            <div class="newspaper-subtitle">{edition.subtitle}</div>
            <div class="publication-date">{edition.publication_date.strftime('%A, %B %d, %Y')}</div>
        </header>
        """
    
    def generate_content_html(self, edition: NewspaperEdition) -> str:
        """Generate HTML for newspaper content"""
        content_html = '<main class="content">'
        
        # Add editorial note if present
        if edition.editorial_note:
            content_html += f'<div class="editorial-note">{edition.editorial_note}</div>'
        
        # Generate each section
        for section_name, section in edition.sections.items():
            if not section.articles:  # Skip empty sections
                continue
                
            content_html += self.generate_section_html(section)
        
        content_html += '</main>'
        return content_html
    
    def generate_section_html(self, section: NewspaperSection) -> str:
        """Generate HTML for a newspaper section"""
        section_html = f'''
        <section class="section">
            <h2 class="section-header">{section.name}</h2>
            <div class="articles-grid">
        '''
        
        for article in section.articles:
            section_html += self.generate_article_html(article)
        
        section_html += '''
            </div>
        </section>
        '''
        
        return section_html
    
    def generate_article_html(self, article: NewsArticle) -> str:
        """Generate HTML for a single article"""
        
        # Process content for LaTeX formulas
        processed_content = self.process_latex_formulas(article.content)
        
        return f'''
        <article class="article">
            <h3 class="article-title">{article.title}</h3>
            <div class="article-meta">
                By {article.author or article.source} | {article.timestamp.strftime('%H:%M')} | {article.word_count} words
            </div>
            <div class="article-content">
                {processed_content}
            </div>
        </article>
        '''
    
    def process_latex_formulas(self, content: str) -> str:
        """Process LaTeX formulas in content"""
        if not self.config.get("latex_enabled", True):
            return content
        
        # Simple LaTeX formula detection and conversion
        # Look for patterns like $formula$ or $$formula$$
        import re
        
        def replace_formula(match):
            formula = match.group(1).strip()
            # For now, we'll use a simple placeholder - in a real implementation,
            # this would convert LaTeX to MathML or use a LaTeX renderer
            return f'<div class="latex-formula">${formula}$</div>'
        
        # Replace inline formulas $...$
        content = re.sub(r'\$(.*?)\$', replace_formula, content)
        
        # Replace display formulas $$...$$
        content = re.sub(r'\$\$(.*?)\$\$', lambda m: f'<div class="latex-formula">${m.group(1)}$</div>', content, flags=re.DOTALL)
        
        return content

class PDFExporter:
    """PDF export functionality"""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.logger = logging.getLogger("PDFExporter")
        self.layout = NewspaperLayout(config)
    
    def export_to_pdf(self, edition: NewspaperEdition, output_path: str) -> bool:
        """Export newspaper edition to PDF"""
        try:
            self.logger.info(f"Exporting newspaper to PDF: {output_path}")
            
            # Generate HTML
            html_content = self.layout.create_html_template(edition)
            
            # Create output directory if it doesn't exist
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            
            # Generate PDF using WeasyPrint
            html_doc = HTML(string=html_content)
            css = CSS(string="""
                @page {
                    size: A4;
                    margin: 2.54cm; /* 1 inch in cm */
                }
            """)
            
            html_doc.write_pdf(output_path, stylesheets=[css])
            
            self.logger.info(f"PDF exported successfully: {output_path}")
            return True
            
        except Exception as e:
            self.logger.error(f"Error exporting PDF: {e}")
            return False
    
    def export_to_html(self, edition: NewspaperEdition, output_path: str) -> bool:
        """Export newspaper edition to HTML"""
        try:
            self.logger.info(f"Exporting newspaper to HTML: {output_path}")
            
            # Generate HTML
            html_content = self.layout.create_html_template(edition)
            
            # Create output directory if it doesn't exist
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            
            # Write HTML file
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(html_content)
            
            self.logger.info(f"HTML exported successfully: {output_path}")
            return True
            
        except Exception as e:
            self.logger.error(f"Error exporting HTML: {e}")
            return False
    
    def create_math_sample_article(self) -> NewsArticle:
        """Create a sample article with math formulas for testing"""
        content = """
Advanced Mathematics in Modern Computing

Mathematical principles form the foundation of modern computational systems. The elegant relationship between calculus and linear algebra enables us to solve complex problems that were once considered impossible.

Consider the fundamental theorem of calculus:
$$\\int_a^b f(x)\\,dx = F(b) - F(a)$$

This relationship connects differentiation and integration in a profound way. In machine learning applications, we frequently encounter optimization problems that require finding minima of complex functions using gradient descent:

$\\theta_{new} = \\theta_{old} - \\alpha \\nabla f(\\theta)$

The normal equation in linear regression provides a closed-form solution for finding optimal parameters:

$\\theta = (X^T X)^{-1} X^T y$

In probability theory, Bayes' theorem helps us update our beliefs based on new evidence:

$P(A|B) = \\frac{P(B|A) \\cdot P(A)}{P(B)}$

These mathematical tools, combined with computational power, enable breakthroughs in artificial intelligence, data science, and engineering. The interplay between pure mathematics and applied computation continues to drive innovation across multiple disciplines.

Researchers are now exploring quantum computing applications where quantum entanglement and superposition principles could revolutionize how we process information, potentially solving problems that would take classical computers millions of years to complete.
        """
        
        return NewsArticle(
            title="Mathematics: The Language of Innovation",
            content=content,
            source="Science Desk",
            category="Mathematics & Sciences",
            timestamp=datetime.now(),
            author="Dr. Mathematics Editor",
            keywords=["mathematics", "calculus", "algebra", "probability", "quantum"]
        )

class ConsistencyValidator:
    """Validates newspaper consistency and quality"""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.logger = logging.getLogger("ConsistencyValidator")
    
    def validate_edition(self, edition: NewspaperEdition) -> Dict[str, Any]:
        """Validate newspaper edition for consistency and quality"""
        validation_results = {
            "is_valid": True,
            "errors": [],
            "warnings": [],
            "statistics": {}
        }
        
        try:
            # Basic statistics
            total_articles = edition.get_total_articles()
            total_words = edition.get_total_word_count()
            
            validation_results["statistics"] = {
                "total_articles": total_articles,
                "total_words": total_words,
                "sections_count": len(edition.sections),
                "publication_date": edition.publication_date.isoformat()
            }
            
            # Validate minimum requirements
            if total_articles == 0:
                validation_results["errors"].append("No articles found in newspaper")
                validation_results["is_valid"] = False
            
            if total_words < 1000:
                validation_results["warnings"].append("Newspaper has very low word count")
            
            # Validate each section
            for section_name, section in edition.sections.items():
                if not section.articles:
                    validation_results["warnings"].append(f"Section '{section_name}' is empty")
                    continue
                
                # Validate articles in section
                for i, article in enumerate(section.articles):
                    if not article.title or len(article.title.strip()) < 5:
                        validation_results["errors"].append(f"Article {i+1} in {section_name} has invalid title")
                        validation_results["is_valid"] = False
                    
                    if article.word_count < self.config.get("min_article_length", 50):
                        validation_results["warnings"].append(f"Article '{article.title}' is too short")
                    
                    if not article.content or len(article.content.strip()) < 100:
                        validation_results["errors"].append(f"Article '{article.title}' has insufficient content")
                        validation_results["is_valid"] = False
            
            # Check for LaTeX consistency if enabled
            if self.config.get("latex_enabled", True):
                self._validate_latex_consistency(edition, validation_results)
            
            self.logger.info(f"Validation completed: {'PASSED' if validation_results['is_valid'] else 'FAILED'}")
            
        except Exception as e:
            validation_results["errors"].append(f"Validation error: {e}")
            validation_results["is_valid"] = False
            self.logger.error(f"Error during validation: {e}")
        
        return validation_results
    
    def _validate_latex_consistency(self, edition: NewspaperEdition, results: Dict[str, Any]):
        """Validate LaTeX formula consistency"""
        import re
        
        latex_count = 0
        for section in edition.sections.values():
            for article in section.articles:
                # Count LaTeX formulas
                inline_formulas = len(re.findall(r'\$[^$]+\$', article.content))
                display_formulas = len(re.findall(r'\$\$[^$]+\$\$', article.content))
                latex_count += inline_formulas + display_formulas
        
        if latex_count > 0:
            results["statistics"]["latex_formulas"] = latex_count
            self.logger.info(f"Found {latex_count} LaTeX formulas in newspaper")

def test_layout_export():
    """Test function for layout and export"""
    config = {
        "layout": {
            "columns": 2,
            "font_family": "Times New Roman",
            "font_size": 12,
            "margin": "1 inch"
        },
        "latex_enabled": True
    }
    
    # Create test edition
    from newspaper_workshop import NewspaperEdition, NewspaperSection
    
    test_edition = NewspaperEdition(
        title="Test Newspaper",
        subtitle="Testing Layout System",
        publication_date=datetime.now(),
        sections={}
    )
    
    # Add test sections
    exporter = PDFExporter(config)
    
    # Add math section
    math_section = NewspaperSection(name="Mathematics & Sciences", articles=[])
    math_article = exporter.create_math_sample_article()
    math_section.add_article(math_article)
    test_edition.add_section(math_section)
    
    # Validate
    validator = ConsistencyValidator(config)
    validation = validator.validate_edition(test_edition)
    
    import json
    print("Validation Results:")
    print(json.dumps(validation, indent=2, default=str))
    
    # Export to HTML for testing
    os.makedirs("newspaper_workshop/output", exist_ok=True)
    success = exporter.export_to_html(test_edition, "newspaper_workshop/output/test_newspaper.html")
    print(f"HTML Export: {'SUCCESS' if success else 'FAILED'}")

if __name__ == "__main__":
    import json
    from datetime import datetime
    test_layout_export()