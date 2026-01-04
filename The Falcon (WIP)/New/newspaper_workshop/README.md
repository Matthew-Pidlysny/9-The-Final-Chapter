# 📰 Newspaper Workshop

A complete, modular newspaper generation system that integrates with The Falcon Press Office without modifying the core codebase.

## 🎯 Overview

The Newspaper Workshop is a separate, self-contained module that generates complete newspapers with:
- **Real News Aggregation** from RSS feeds
- **AI-Powered Article Generation** for diverse content
- **Mathematics & Sciences Section** with LaTeX formula support
- **Multiple Export Formats** (HTML, PDF)
- **Consistency Validation** and quality checks
- **Interactive & Command-Line Interfaces**

## 🚀 Quick Start

### Installation

```bash
# Install required dependencies
pip install aiohttp feedparser weasyprint

# Navigate to the workshop directory
cd newspaper_workshop
```

### Generate Your First Newspaper

```bash
# Interactive mode (recommended for beginners)
python workshop_ui.py --interactive

# Quick generation with defaults
python workshop_ui.py --generate --formats html pdf

# Command line with options
python workshop_ui.py --generate --formats html --output ./my_newspaper
```

## 📁 Project Structure

```
newspaper_workshop/
├── 📄 README.md                 # This file
├── 📄 config.json               # Configuration settings
├── 📄 newspaper_workshop.py     # Core workshop classes
├── 📄 news_aggregator.py        # RSS news fetching
├── 📄 ai_article_generator.py   # AI article generation
├── 📄 layout_export.py          # Layout design & PDF export
├── 📄 workshop_orchestrator.py  # Main workflow controller
├── 📄 workshop_ui.py            # User interfaces
├── 📁 output/                   # Generated newspapers
├── 📁 logs/                     # Activity logs
└── 📁 tests/                    # Test files
```

## ⚙️ Configuration

Edit `config.json` to customize your newspaper:

```json
{
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
    "latex_enabled": true,
    "consistency_checks": true,
    "export_formats": ["html", "pdf"],
    "layout": {
        "columns": 3,
        "font_family": "Times New Roman",
        "font_size": 12,
        "margin": "1 inch"
    }
}
```

## 🔧 Features

### 1. News Aggregation
- Fetches from multiple RSS feeds simultaneously
- Automatic categorization and keyword extraction
- Duplicate detection and content filtering
- Support for custom news sources

### 2. AI Article Generation
- Context-aware article creation
- Multiple writing styles (factual, analytical, engaging)
- Topic-specific content generation
- Integration with linguistic libraries

### 3. Mathematics Section
- LaTeX formula support for proper mathematical notation
- Sample articles covering calculus, linear algebra, probability
- Automatic formula detection and formatting
- Math-ready PDF export

### 4. Layout & Design
- Professional newspaper-style layout
- Multi-column designs
- Responsive HTML output
- Print-ready PDF generation

### 5. Quality Assurance
- Content consistency validation
- Word count and quality checks
- LaTeX formula validation
- Export format verification

## 📖 Usage Examples

### Interactive Mode
```bash
python workshop_ui.py --interactive
```
Provides a menu-driven interface for all features.

### Command Line Generation
```bash
# Generate with AI articles only
python workshop_ui.py --generate --formats html

# Include real news from RSS feeds
python workshop_orchestrator.py
```

### Programmatic Usage
```python
import asyncio
from workshop_orchestrator import NewspaperWorkshopOrchestrator

async def generate_newspaper():
    orchestrator = NewspaperWorkshopOrchestrator()
    results = await orchestrator.run_complete_workflow(
        include_real_news=True,
        include_ai_articles=True,
        articles_per_section=3,
        export_formats=["html", "pdf"]
    )
    return results

# Run the generation
results = asyncio.run(generate_newspaper())
```

## 🧮 Mathematics & LaTeX Support

The workshop includes specialized support for mathematical content:

### Featured Mathematics Articles:
- **Calculus**: Fundamental theorem of calculus with integral notation
- **Linear Algebra**: Matrix operations and eigenvalue problems
- **Probability Theory**: Bayes' theorem and expected value calculations

### LaTeX Formula Examples:
```
Inline: $E[X] = \sum_{x} x \cdot p(x)$
Display: $$\int_a^b f(x)\,dx = F(b) - F(a)$$
```

All formulas are properly formatted in both HTML and PDF outputs.

## 📊 Output Formats

### HTML Output
- Responsive design for web viewing
- Interactive navigation
- Embedded CSS styling
- Mobile-friendly layout

### PDF Output
- Print-ready A4 format
- Professional newspaper styling
- Proper page breaks and headers
- Embedded LaTeX formula rendering

## 🎨 Customization

### Adding Custom Sections
```python
# In your configuration
"default_sections": [
    "Headlines",
    "Custom Section",
    "Technology"
]
```

### Custom RSS Sources
```json
"news_sources": {
    "rss_feeds": [
        "https://your-news-source.com/rss.xml"
    ]
}
```

### Custom Layout
```json
"layout": {
    "columns": 2,
    "font_family": "Georgia",
    "font_size": 11
}
```

## 🧪 Testing

Run component tests:
```bash
# Test news aggregator
python news_aggregator.py

# Test AI generator
python ai_article_generator.py

# Test layout system
python layout_export.py

# Test complete workflow
python workshop_orchestrator.py
```

## 🔍 Troubleshooting

### Common Issues

1. **PDF Export Fails**
   ```bash
   # Ensure WeasyPrint dependencies are installed
   pip install weasyprint
   ```

2. **RSS Feed Errors**
   - Check network connectivity
   - Verify RSS feed URLs are accessible
   - Some feeds may require user-agent headers

3. **Import Errors**
   - The workshop can run standalone without existing Falcon Press libraries
   - Install missing dependencies with pip

### Logs
Check activity logs in `newspaper_workshop/logs/` for detailed error information.

## 🔗 Integration with Falcon Press Office

The workshop is designed to integrate gently with the existing system:

- **Non-Invasive**: Doesn't modify any existing code
- **Optional Libraries**: Works with or without Falcon Press libraries
- **Modular Design**: Can be used independently or as part of the larger system
- **Shared Standards**: Follows the same editorial principles and quality standards

## 📋 Requirements

- Python 3.11+
- aiohttp
- feedparser
- weasyprint
- numpy (optional, for mathematical operations)

## 📄 License

This workshop is part of The Falcon Press Office project and follows the same licensing terms.

## 🤝 Contributing

To contribute to the Newspaper Workshop:

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Ensure all tests pass
5. Submit a pull request

## 📞 Support

For issues and questions:
- Check the logs in `newspaper_workshop/logs/`
- Review the troubleshooting section above
- Test individual components to isolate problems

---

**Newspaper Workshop** - Empowering quality journalism through AI and automation 🚀