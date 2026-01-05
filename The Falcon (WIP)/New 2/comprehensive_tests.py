#!/usr/bin/env python3
"""
Comprehensive Testing Suite for Newspaper Workshop
Bug testing, performance validation, and quality assurance
"""

import asyncio
import json
import os
import time
import sys
from datetime import datetime
from typing import Dict, List, Any

# Add newspaper workshop to path
sys.path.append('newspaper_workshop')

class ComprehensiveTester:
    """Comprehensive testing suite"""
    
    def __init__(self):
        self.test_results = {}
        self.performance_metrics = {}
        self.bugs_found = []
        self.warnings = []
        
    def print_test_header(self, test_name: str):
        """Print test header"""
        print(f"\n{'='*60}")
        print(f"🧪 {test_name}")
        print(f"{'='*60}")
    
    def print_test_result(self, test_name: str, success: bool, details: str = ""):
        """Print test result"""
        status = "✅ PASSED" if success else "❌ FAILED"
        print(f"{status}: {test_name}")
        if details:
            print(f"   Details: {details}")
    
    async def test_core_functionality(self):
        """Test core workshop functionality"""
        self.print_test_header("Core Functionality Tests")
        
        try:
            # Test original workshop
            from workshop_orchestrator import NewspaperWorkshopOrchestrator
            
            orchestrator = NewspaperWorkshopOrchestrator()
            results = await orchestrator.run_complete_workflow(
                include_real_news=False,
                include_ai_articles=True,
                articles_per_section=2,
                export_formats=["html"]
            )
            
            success = results.get("success", False)
            self.test_results["core_functionality"] = success
            
            if success:
                info = results["edition_info"]
                print(f"   Generated {info['total_articles']} articles")
                print(f"   Word count: {info['total_words']}")
                print(f"   Sections: {info['sections']}")
            
            self.print_test_result("Core Workshop Generation", success)
            
        except Exception as e:
            self.bugs_found.append(f"Core functionality error: {e}")
            self.print_test_result("Core Workshop Generation", False, str(e))
    
    async def test_optimized_functionality(self):
        """Test optimized workshop functionality"""
        self.print_test_header("Optimized Functionality Tests")
        
        try:
            from optimized_workshop_orchestrator import OptimizedWorkshopOrchestrator
            
            orchestrator = OptimizedWorkshopOrchestrator()
            results = await orchestrator.run_complete_workflow_optimized(
                include_real_news=False,
                include_ai_articles=True,
                articles_per_section=3,
                export_formats=["html", "pdf"],
                optimization_level="maximum"
            )
            
            success = results.get("success", False)
            self.test_results["optimized_functionality"] = success
            
            if success:
                perf = results["performance"]
                self.performance_metrics["optimized"] = perf
                print(f"   Optimization score: {perf['optimization_score']}%")
                print(f"   Efficiency gain: {perf['efficiency_gain']}%")
                print(f"   Total time: {perf['total_time']:.2f}s")
            
            self.print_test_result("Optimized Workshop Generation", success)
            
        except Exception as e:
            self.bugs_found.append(f"Optimized functionality error: {e}")
            self.print_test_result("Optimized Workshop Generation", False, str(e))
    
    async def test_news_aggregation(self):
        """Test news aggregation components"""
        self.print_test_header("News Aggregation Tests")
        
        # Test original aggregator
        try:
            from news_aggregator import test_news_aggregator
            print("   Testing original news aggregator...")
            await test_news_aggregator()
            self.print_test_result("Original News Aggregator", True)
            self.test_results["original_aggregator"] = True
        except Exception as e:
            self.bugs_found.append(f"Original aggregator error: {e}")
            self.print_test_result("Original News Aggregator", False, str(e))
            self.test_results["original_aggregator"] = False
        
        # Test optimized aggregator
        try:
            from optimized_news_aggregator import test_optimized_aggregator
            print("   Testing optimized news aggregator...")
            await test_optimized_aggregator()
            self.print_test_result("Optimized News Aggregator", True)
            self.test_results["optimized_aggregator"] = True
        except Exception as e:
            self.bugs_found.append(f"Optimized aggregator error: {e}")
            self.print_test_result("Optimized News Aggregator", False, str(e))
            self.test_results["optimized_aggregator"] = False
    
    def test_ai_generation(self):
        """Test AI article generation"""
        self.print_test_header("AI Article Generation Tests")
        
        # Test original AI generator
        try:
            from ai_article_generator import test_ai_generator
            print("   Testing original AI generator...")
            test_ai_generator()
            self.print_test_result("Original AI Generator", True)
            self.test_results["original_ai"] = True
        except Exception as e:
            self.bugs_found.append(f"Original AI generator error: {e}")
            self.print_test_result("Original AI Generator", False, str(e))
            self.test_results["original_ai"] = False
        
        # Test optimized AI generator
        try:
            from optimized_ai_generator import test_optimized_generator
            print("   Testing optimized AI generator...")
            # Create event loop if not running
            try:
                loop = asyncio.get_running_loop()
                loop.create_task(test_optimized_generator())
            except RuntimeError:
                asyncio.run(test_optimized_generator())
            self.print_test_result("Optimized AI Generator", True)
            self.test_results["optimized_ai"] = True
        except Exception as e:
            self.bugs_found.append(f"Optimized AI generator error: {e}")
            self.print_test_result("Optimized AI Generator", False, str(e))
            self.test_results["optimized_ai"] = False
    
    def test_layout_export(self):
        """Test layout and export functionality"""
        self.print_test_header("Layout & Export Tests")
        
        # Test original layout system
        try:
            from layout_export import test_layout_export
            print("   Testing original layout system...")
            test_layout_export()
            self.print_test_result("Original Layout System", True)
            self.test_results["original_layout"] = True
        except Exception as e:
            self.bugs_found.append(f"Original layout error: {e}")
            self.print_test_result("Original Layout System", False, str(e))
            self.test_results["original_layout"] = False
        
        # Test optimized layout system
        try:
            from optimized_layout_export import test_optimized_layout_export
            print("   Testing optimized layout system...")
            # Create event loop if not running
            try:
                loop = asyncio.get_running_loop()
                loop.create_task(test_optimized_layout_export())
            except RuntimeError:
                asyncio.run(test_optimized_layout_export())
            self.print_test_result("Optimized Layout System", True)
            self.test_results["optimized_layout"] = True
        except Exception as e:
            self.bugs_found.append(f"Optimized layout error: {e}")
            self.print_test_result("Optimized Layout System", False, str(e))
            self.test_results["optimized_layout"] = False
    
    def test_user_interfaces(self):
        """Test user interfaces"""
        self.print_test_header("User Interface Tests")
        
        try:
            # Test UI imports
            from workshop_ui import NewspaperWorkshopUI
            ui = NewspaperWorkshopUI()
            self.print_test_result("UI Class Initialization", True)
            self.test_results["ui_init"] = True
            
            # Test configuration loading
            if os.path.exists("newspaper_workshop/config.json"):
                with open("newspaper_workshop/config.json", 'r') as f:
                    config = json.load(f)
                self.print_test_result("Configuration Loading", True)
                self.test_results["config_loading"] = True
            else:
                self.warnings.append("Configuration file not found")
                self.print_test_result("Configuration Loading", False, "Config file missing")
                self.test_results["config_loading"] = False
                
        except Exception as e:
            self.bugs_found.append(f"UI error: {e}")
            self.print_test_result("User Interface", False, str(e))
            self.test_results["ui_init"] = False
    
    def test_file_integrity(self):
        """Test file integrity and structure"""
        self.print_test_header("File Integrity Tests")
        
        required_files = [
            "newspaper_workshop/newspaper_workshop.py",
            "newspaper_workshop/config.json",
            "newspaper_workshop/workshop_orchestrator.py",
            "newspaper_workshop/workshop_ui.py",
            "newspaper_workshop/news_aggregator.py",
            "newspaper_workshop/ai_article_generator.py",
            "newspaper_workshop/layout_export.py",
            "newspaper_workshop/optimized_news_aggregator.py",
            "newspaper_workshop/optimized_ai_generator.py",
            "newspaper_workshop/optimized_layout_export.py",
            "newspaper_workshop/optimized_workshop_orchestrator.py"
        ]
        
        missing_files = []
        for file_path in required_files:
            if os.path.exists(file_path):
                self.print_test_result(f"File: {os.path.basename(file_path)}", True)
            else:
                missing_files.append(file_path)
                self.print_test_result(f"File: {os.path.basename(file_path)}", False, "Missing")
        
        self.test_results["file_integrity"] = len(missing_files) == 0
        if missing_files:
            self.bugs_found.extend(f"Missing file: {f}" for f in missing_files)
    
    def test_output_quality(self):
        """Test output quality and content"""
        self.print_test_header("Output Quality Tests")
        
        try:
            output_dir = "newspaper_workshop/output"
            if os.path.exists(output_dir):
                html_files = [f for f in os.listdir(output_dir) if f.endswith('.html')]
                
                if html_files:
                    latest_html = max(html_files, key=lambda f: os.path.getmtime(os.path.join(output_dir, f)))
                    html_path = os.path.join(output_dir, latest_html)
                    
                    # Check HTML content
                    with open(html_path, 'r') as f:
                        content = f.read()
                    
                    # Quality checks
                    has_title = "The Falcon Press" in content
                    has_articles = "article" in content.lower()
                    has_latex = "$" in content and "$" in content
                    has_sections = "section" in content.lower()
                    
                    quality_score = sum([has_title, has_articles, has_latex, has_sections])
                    
                    print(f"   Latest output: {latest_html}")
                    print(f"   Contains title: {'✅' if has_title else '❌'}")
                    print(f"   Contains articles: {'✅' if has_articles else '❌'}")
                    print(f"   Contains LaTeX: {'✅' if has_latex else '❌'}")
                    print(f"   Contains sections: {'✅' if has_sections else '❌'}")
                    
                    self.test_results["output_quality"] = quality_score >= 3
                    self.print_test_result("Output Quality", quality_score >= 3, f"Score: {quality_score}/4")
                else:
                    self.warnings.append("No output files found")
                    self.print_test_result("Output Quality", False, "No output files")
                    self.test_results["output_quality"] = False
            else:
                self.warnings.append("Output directory not found")
                self.print_test_result("Output Quality", False, "No output directory")
                self.test_results["output_quality"] = False
                
        except Exception as e:
            self.bugs_found.append(f"Output quality test error: {e}")
            self.print_test_result("Output Quality", False, str(e))
            self.test_results["output_quality"] = False
    
    def generate_test_report(self):
        """Generate comprehensive test report"""
        self.print_test_header("Comprehensive Test Report")
        
        # Calculate success rate
        total_tests = len(self.test_results)
        passed_tests = sum(1 for result in self.test_results.values() if result)
        success_rate = (passed_tests / total_tests * 100) if total_tests > 0 else 0
        
        print(f"\n📊 Test Summary:")
        print(f"   Total Tests: {total_tests}")
        print(f"   Passed: {passed_tests}")
        print(f"   Failed: {total_tests - passed_tests}")
        print(f"   Success Rate: {success_rate:.1f}%")
        
        # Performance summary
        if self.performance_metrics.get("optimized"):
            perf = self.performance_metrics["optimized"]
            print(f"\n⚡ Performance Summary:")
            print(f"   Optimization Score: {perf.get('optimization_score', 0)}%")
            print(f"   Efficiency Gain: {perf.get('efficiency_gain', 0)}%")
            print(f"   Total Time: {perf.get('total_time', 0):.2f}s")
        
        # Issues found
        if self.bugs_found:
            print(f"\n🐛 Bugs Found ({len(self.bugs_found)}):")
            for i, bug in enumerate(self.bugs_found, 1):
                print(f"   {i}. {bug}")
        
        if self.warnings:
            print(f"\n⚠️  Warnings ({len(self.warnings)}):")
            for i, warning in enumerate(self.warnings, 1):
                print(f"   {i}. {warning}")
        
        # Overall assessment
        if success_rate >= 90 and len(self.bugs_found) == 0:
            print(f"\n🎉 OVERALL ASSESSMENT: EXCELLENT")
            print(f"   System is ready for production deployment!")
        elif success_rate >= 80 and len(self.bugs_found) <= 2:
            print(f"\n✅ OVERALL ASSESSMENT: GOOD")
            print(f"   System is functional with minor issues.")
        elif success_rate >= 70:
            print(f"\n⚠️  OVERALL ASSESSMENT: ACCEPTABLE")
            print(f"   System needs some attention before deployment.")
        else:
            print(f"\n❌ OVERALL ASSESSMENT: NEEDS WORK")
            print(f"   Significant issues need to be addressed.")
        
        return {
            "success_rate": success_rate,
            "total_tests": total_tests,
            "passed_tests": passed_tests,
            "bugs_count": len(self.bugs_found),
            "warnings_count": len(self.warnings),
            "ready_for_production": success_rate >= 90 and len(self.bugs_found) == 0
        }
    
    async def run_all_tests(self):
        """Run all comprehensive tests"""
        print("🚀 Starting Comprehensive Test Suite...")
        print("=" * 60)
        
        # Run all test categories
        await self.test_core_functionality()
        await self.test_optimized_functionality()
        await self.test_news_aggregation()
        self.test_ai_generation()
        self.test_layout_export()
        self.test_user_interfaces()
        self.test_file_integrity()
        self.test_output_quality()
        
        # Generate final report
        return self.generate_test_report()

async def main():
    """Main testing function"""
    tester = ComprehensiveTester()
    report = await tester.run_all_tests()
    
    # Save test report
    with open("test_report.json", "w") as f:
        json.dump(report, f, indent=2)
    
    print(f"\n📄 Test report saved to: test_report.json")
    
    return report["ready_for_production"]

if __name__ == "__main__":
    ready = asyncio.run(main())
    sys.exit(0 if ready else 1)