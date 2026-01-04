#!/usr/bin/env python3
"""
Newspaper Workshop User Interface
Command-line interface for the Newspaper Workshop
"""

import asyncio
import argparse
import json
import sys
from datetime import datetime
from typing import Dict, Any, List

from workshop_orchestrator import NewspaperWorkshopOrchestrator

class NewspaperWorkshopUI:
    """User interface for the Newspaper Workshop"""
    
    def __init__(self):
        self.orchestrator = None
    
    def print_banner(self):
        """Print workshop banner"""
        banner = """
╔══════════════════════════════════════════════════════════════╗
║                    NEWSPAPER WORKSHOP                        ║
║                 Advanced Newspaper Generation                 ║
║                                                              ║
║  📰 Generate complete newspapers with AI and real news       ║
║  🧮 Include mathematics section with LaTeX formulas          ║
║  🌐 Multiple export formats (HTML, PDF)                     ║
║  ✅ Consistency validation and quality checks               ║
╚══════════════════════════════════════════════════════════════╝
        """
        print(banner)
    
    def print_menu(self):
        """Print main menu"""
        menu = """
Main Menu:
────────────────────────────────────────────────────────────────
1. 📰 Generate Complete Newspaper
2. ⚙️  Configure Workshop Settings
3. 📊 View Workshop Status
4. 📤 Export Existing Newspaper
5. 🧪 Test Individual Components
6. 📖 View Help & Documentation
7. 🚪 Exit
────────────────────────────────────────────────────────────────
        """
        print(menu)
    
    async def interactive_mode(self):
        """Run interactive mode"""
        self.print_banner()
        
        while True:
            self.print_menu()
            choice = input("\nEnter your choice (1-7): ").strip()
            
            try:
                if choice == "1":
                    await self.interactive_newspaper_generation()
                elif choice == "2":
                    await self.configure_settings()
                elif choice == "3":
                    await self.view_status()
                elif choice == "4":
                    await self.export_newspaper()
                elif choice == "5":
                    await self.test_components()
                elif choice == "6":
                    self.show_help()
                elif choice == "7":
                    print("\n👋 Thank you for using Newspaper Workshop!")
                    break
                else:
                    print("❌ Invalid choice. Please enter a number between 1-7.")
            
            except KeyboardInterrupt:
                print("\n\n👋 Goodbye!")
                break
            except Exception as e:
                print(f"❌ Error: {e}")
            
            input("\nPress Enter to continue...")
    
    async def interactive_newspaper_generation(self):
        """Interactive newspaper generation"""
        print("\n📰 Newspaper Generation Configuration")
        print("─" * 50)
        
        # Get user preferences
        include_real_news = self.get_yes_no("Include real news from RSS feeds? (y/n): ", default=False)
        include_ai_articles = self.get_yes_no("Include AI-generated articles? (y/n): ", default=True)
        
        if include_ai_articles:
            articles_per_section = self.get_int("Articles per section (1-10): ", 1, 10, default=3)
        else:
            articles_per_section = 0
        
        export_formats = self.get_export_formats()
        
        print("\n🔄 Generating newspaper...")
        
        # Initialize orchestrator and generate
        self.orchestrator = NewspaperWorkshopOrchestrator()
        results = await self.orchestrator.run_complete_workflow(
            include_real_news=include_real_news,
            include_ai_articles=include_ai_articles,
            articles_per_section=articles_per_section,
            export_formats=export_formats
        )
        
        self.display_results(results)
    
    def get_yes_no(self, prompt: str, default: bool = True) -> bool:
        """Get yes/no input from user"""
        while True:
            response = input(prompt).strip().lower()
            if not response:
                return default
            if response in ['y', 'yes']:
                return True
            elif response in ['n', 'no']:
                return False
            else:
                print("Please enter 'y' or 'n'")
    
    def get_int(self, prompt: str, min_val: int, max_val: int, default: int = None) -> int:
        """Get integer input from user"""
        while True:
            try:
                response = input(prompt).strip()
                if not response and default is not None:
                    return default
                value = int(response)
                if min_val <= value <= max_val:
                    return value
                else:
                    print(f"Please enter a number between {min_val} and {max_val}")
            except ValueError:
                print("Please enter a valid number")
    
    def get_export_formats(self) -> List[str]:
        """Get export format choices from user"""
        print("\nExport Formats:")
        print("1. HTML")
        print("2. PDF")
        print("3. Both HTML and PDF")
        
        while True:
            choice = input("Choose export format (1-3): ").strip()
            if choice == "1":
                return ["html"]
            elif choice == "2":
                return ["pdf"]
            elif choice == "3":
                return ["html", "pdf"]
            else:
                print("Please enter 1, 2, or 3")
    
    def display_results(self, results: Dict[str, Any]):
        """Display generation results"""
        print("\n📊 Generation Results")
        print("─" * 30)
        
        if results["success"]:
            info = results["edition_info"]
            print(f"✅ Newspaper generated successfully!")
            print(f"📰 Title: {info['title']}")
            print(f"📅 Date: {info['publication_date'][:10]}")
            print(f"📄 Articles: {info['total_articles']}")
            print(f"📝 Words: {info['total_words']}")
            
            print("\n📋 Sections:")
            for section, count in info["sections"].items():
                print(f"  • {section}: {count} articles")
            
            print("\n📤 Export Results:")
            for format_type, success in results["export_results"].items():
                status = "✅" if success else "❌"
                print(f"  {status} {format_type.upper()}")
        else:
            print(f"❌ Generation failed: {results.get('error', 'Unknown error')}")
    
    async def configure_settings(self):
        """Configure workshop settings"""
        print("\n⚙️ Workshop Configuration")
        print("─" * 30)
        
        # Load current config
        try:
            with open("newspaper_workshop/config.json", 'r') as f:
                config = json.load(f)
            print("✅ Configuration loaded successfully")
        except Exception as e:
            print(f"❌ Error loading configuration: {e}")
            return
        
        print(f"\nCurrent configuration:")
        print(f"Newspaper Title: {config.get('newspaper_title', 'N/A')}")
        print(f"Max Articles per Section: {config.get('max_articles_per_section', 'N/A')}")
        print(f"LaTeX Enabled: {config.get('latex_enabled', 'N/A')}")
        print(f"Export Formats: {', '.join(config.get('export_formats', []))}")
        
        print("\n⚠️  Configuration editing not implemented in this demo")
        print("   To modify settings, edit: newspaper_workshop/config.json")
    
    async def view_status(self):
        """View workshop status"""
        print("\n📊 Workshop Status")
        print("─" * 25)
        
        if not self.orchestrator:
            self.orchestrator = NewspaperWorkshopOrchestrator()
        
        status = self.orchestrator.workshop.get_status()
        
        print(f"Workshop Ready: {'✅' if status['workshop_ready'] else '❌'}")
        print(f"\n📚 Libraries Status:")
        for lib_name, loaded in status["libraries_loaded"].items():
            status_icon = "✅" if loaded else "❌"
            print(f"  {status_icon} {lib_name.replace('_', ' ').title()}")
        
        if status["current_edition"]:
            edition = status["current_edition"]
            print(f"\n📰 Current Edition:")
            print(f"  Title: {edition['title']}")
            print(f"  Date: {edition['publication_date'][:10]}")
            print(f"  Articles: {edition['total_articles']}")
            print(f"  Word Count: {edition['total_word_count']}")
    
    async def export_newspaper(self):
        """Export existing newspaper"""
        print("\n📤 Export Newspaper")
        print("─" * 22)
        print("This feature requires an existing generated newspaper.")
        print("Please generate a newspaper first using option 1.")
    
    async def test_components(self):
        """Test individual components"""
        print("\n🧪 Component Testing")
        print("─" * 23)
        
        print("Available tests:")
        print("1. News Aggregator")
        print("2. AI Article Generator")
        print("3. Layout System")
        print("4. PDF Export")
        
        choice = input("Choose component to test (1-4): ").strip()
        
        if choice == "1":
            await self.test_news_aggregator()
        elif choice == "2":
            self.test_ai_generator()
        elif choice == "3":
            self.test_layout_system()
        elif choice == "4":
            self.test_pdf_export()
        else:
            print("❌ Invalid choice")
    
    async def test_news_aggregator(self):
        """Test news aggregator"""
        print("\n📡 Testing News Aggregator...")
        try:
            from news_aggregator import test_news_aggregator
            await test_news_aggregator()
        except Exception as e:
            print(f"❌ Test failed: {e}")
    
    def test_ai_generator(self):
        """Test AI article generator"""
        print("\n🤖 Testing AI Article Generator...")
        try:
            from ai_article_generator import test_ai_generator
            test_ai_generator()
        except Exception as e:
            print(f"❌ Test failed: {e}")
    
    def test_layout_system(self):
        """Test layout system"""
        print("\n🎨 Testing Layout System...")
        try:
            from layout_export import test_layout_export
            test_layout_export()
        except Exception as e:
            print(f"❌ Test failed: {e}")
    
    def test_pdf_export(self):
        """Test PDF export"""
        print("\n📄 Testing PDF Export...")
        try:
            from layout_export import test_layout_export
            test_layout_export()
        except Exception as e:
            print(f"❌ Test failed: {e}")
    
    def show_help(self):
        """Show help and documentation"""
        help_text = """
📖 Newspaper Workshop Help
────────────────────────────────────────────────────────────────

OVERVIEW:
The Newspaper Workshop is a complete system for generating newspapers
with both real news aggregation and AI-generated content. It includes
mathematics sections with LaTeX formula support and can export to
multiple formats.

KEY FEATURES:
• Real news aggregation from RSS feeds
• AI-powered article generation
• Mathematics section with LaTeX formulas
• HTML and PDF export capabilities
• Consistency validation and quality checks
• Modular, extensible architecture

COMPONENTS:
1. News Aggregator - Fetches real news from RSS feeds
2. AI Article Generator - Creates articles using AI models
3. Layout System - Designs newspaper layout with styling
4. PDF Exporter - Exports to PDF with proper formatting
5. Consistency Validator - Checks content quality and consistency

CONFIGURATION:
Edit newspaper_workshop/config.json to customize:
• Newspaper title and sections
• RSS feed sources
• AI generation settings
• Export formats
• Layout preferences

OUTPUT FILES:
Generated newspapers are saved to:
• newspaper_workshop/output/ (HTML and PDF files)
• newspaper_workshop/logs/ (activity logs)

TROUBLESHOOTING:
• For PDF export issues, ensure all dependencies are installed
• Network errors may affect RSS feed fetching
• AI generation quality depends on available models

For more information, see the project documentation.
        """
        print(help_text)

def main():
    """Main function"""
    parser = argparse.ArgumentParser(description="Newspaper Workshop - Advanced Newspaper Generation")
    parser.add_argument("--interactive", "-i", action="store_true", 
                       help="Run in interactive mode")
    parser.add_argument("--generate", "-g", action="store_true",
                       help="Generate a newspaper with default settings")
    parser.add_argument("--config", "-c", type=str,
                       help="Path to configuration file")
    parser.add_argument("--output", "-o", type=str,
                       help="Output directory")
    parser.add_argument("--formats", type=str, nargs="+", choices=["html", "pdf"],
                       help="Export formats (html, pdf)")
    
    args = parser.parse_args()
    
    ui = NewspaperWorkshopUI()
    
    if args.interactive or len(sys.argv) == 1:
        # Run interactive mode
        asyncio.run(ui.interactive_mode())
    elif args.generate:
        # Run generation with defaults
        asyncio.run(run_default_generation(ui, args))
    else:
        parser.print_help()

async def run_default_generation(ui: NewspaperWorkshopUI, args):
    """Run newspaper generation with default settings"""
    print("🔄 Generating newspaper with default settings...")
    
    config_path = args.config if args.config else "newspaper_workshop/config.json"
    orchestrator = NewspaperWorkshopOrchestrator(config_path)
    results = await orchestrator.run_complete_workflow(
        include_real_news=False,  # Conservative default
        include_ai_articles=True,
        articles_per_section=2,
        export_formats=args.formats or ["html"]
    )
    
    ui.display_results(results)

if __name__ == "__main__":
    main()