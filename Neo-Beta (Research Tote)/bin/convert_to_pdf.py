#!/usr/bin/env python3
"""
Convert the Peer research report from Markdown to PDF with proper formatting
"""

import markdown
from weasyprint import HTML, CSS
from pathlib import Path

def convert_markdown_to_pdf():
    """Convert the markdown report to a professionally formatted PDF"""
    
    # Read the markdown file
    md_file = Path("peer_research_report.md")
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # Convert markdown to HTML
    html_content = markdown.markdown(
        md_content,
        extensions=[
            'markdown.extensions.tables',
            'markdown.extensions.fenced_code',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
            'markdown.extensions.attr_list',
            'markdown.extensions.def_list',
            'markdown.extensions.footnotes',
            'markdown.extensions.meta',
            'markdown.extensions.sane_lists',
            'markdown.extensions.smarty',
        ]
    )
    
    # Create HTML template with styling
    html_template = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>PEER: Universal Scientific Formula Assessment System - Research Report</title>
        <style>
            @page {{
                size: letter;
                margin: 1in;
                @bottom-center {{
                    content: "Page " counter(page) " of " counter(pages);
                    font-size: 10pt;
                    font-family: 'Georgia', serif;
                }}
            }}
            
            body {{
                font-family: 'Georgia', serif;
                font-size: 12pt;
                line-height: 1.6;
                color: #333;
                max-width: 100%;
            }}
            
            h1 {{
                font-size: 24pt;
                font-weight: bold;
                color: #1a1a1a;
                margin-top: 24pt;
                margin-bottom: 12pt;
                page-break-after: avoid;
                border-bottom: 2pt solid #333;
                padding-bottom: 6pt;
            }}
            
            h2 {{
                font-size: 18pt;
                font-weight: bold;
                color: #2a2a2a;
                margin-top: 18pt;
                margin-bottom: 10pt;
                page-break-after: avoid;
            }}
            
            h3 {{
                font-size: 14pt;
                font-weight: bold;
                color: #3a3a3a;
                margin-top: 14pt;
                margin-bottom: 8pt;
                page-break-after: avoid;
            }}
            
            h4 {{
                font-size: 12pt;
                font-weight: bold;
                color: #4a4a4a;
                margin-top: 12pt;
                margin-bottom: 6pt;
                page-break-after: avoid;
            }}
            
            p {{
                margin-bottom: 10pt;
                text-align: justify;
            }}
            
            code {{
                font-family: 'Courier New', monospace;
                font-size: 10pt;
                background-color: #f5f5f5;
                padding: 2pt 4pt;
                border-radius: 3pt;
            }}
            
            pre {{
                font-family: 'Courier New', monospace;
                font-size: 10pt;
                background-color: #f5f5f5;
                padding: 10pt;
                border-left: 3pt solid #333;
                margin: 10pt 0;
                overflow-x: auto;
                page-break-inside: avoid;
            }}
            
            pre code {{
                background-color: transparent;
                padding: 0;
            }}
            
            ul, ol {{
                margin-bottom: 10pt;
                padding-left: 30pt;
            }}
            
            li {{
                margin-bottom: 4pt;
            }}
            
            table {{
                width: 100%;
                border-collapse: collapse;
                margin: 10pt 0;
                page-break-inside: avoid;
            }}
            
            th, td {{
                border: 1pt solid #ddd;
                padding: 8pt;
                text-align: left;
            }}
            
            th {{
                background-color: #f5f5f5;
                font-weight: bold;
            }}
            
            blockquote {{
                border-left: 3pt solid #ccc;
                padding-left: 15pt;
                margin-left: 0;
                font-style: italic;
                color: #666;
            }}
            
            hr {{
                border: none;
                border-top: 1pt solid #ccc;
                margin: 20pt 0;
            }}
            
            .page-break {{
                page-break-after: always;
            }}
            
            strong {{
                font-weight: bold;
            }}
            
            em {{
                font-style: italic;
            }}
        </style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """
    
    # Convert HTML to PDF
    output_file = Path("PEER_Research_Report.pdf")
    HTML(string=html_template).write_pdf(output_file)
    
    print(f"✓ PDF report generated: {output_file}")
    print(f"✓ File size: {output_file.stat().st_size / 1024 / 1024:.2f} MB")

if __name__ == "__main__":
    convert_markdown_to_pdf()