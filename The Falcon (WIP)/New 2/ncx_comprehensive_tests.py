#!/usr/bin/env python3
"""
Comprehensive Testing Suite for NCX Magazine
"""

import asyncio
import json
import os
import sys
from datetime import datetime

sys.path.append('ncx_magazine')

class NCXComprehensiveTester:
    """Comprehensive testing for NCX Magazine"""
    
    def __init__(self):
        self.test_results = {}
        self.performance_metrics = {}
    
    def print_test_header(self, test_name: str):
        """Print test header"""
        print(f"\n{'='*60}")
        print(f"🎸 {test_name}")
        print(f"{'='*60}")
    
    def print_test_result(self, test_name: str, success: bool, details: str = ""):
        """Print test result"""
        status = "✅ PASSED" if success else "❌ FAILED"
        print(f"{status}: {test_name}")
        if details:
            print(f"   Details: {details}")
    
    async def test_linguistic_analyzer(self):
        """Test linguistic analysis system"""
        self.print_test_header("Linguistic Analyzer Tests")
        
        try:
            from linguistic_analyzer import LinguisticAnalyzer
            
            config = {
                "minimum_evidence_score": 0.6,
                "minimum_punk_rating": 3,
                "tracked_organizations": ["Freemasons", "Lucis Trust"]
            }
            
            analyzer = LinguisticAnalyzer(config)
            
            # Test text with patterns
            test_text = """
            Behind closed doors, executives met with Freemasons to discuss 
            a sudden philanthropic initiative. Despite ongoing investigations, 
            they operate with apparent immunity. Sources say this cannot be verified.
            """
            
            results = analyzer.analyze_text(test_text)
            
            success = (
                results['evidence_strength'] > 0 and
                results['punk_rating'] > 0 and
                len(results['detected_patterns']) > 0
            )
            
            self.test_results["linguistic_analyzer"] = success
            self.print_test_result(
                "Linguistic Analyzer",
                success,
                f"Evidence: {results['evidence_strength']:.2f}, Patterns: {len(results['detected_patterns'])}"
            )
            
        except Exception as e:
            self.test_results["linguistic_analyzer"] = False
            self.print_test_result("Linguistic Analyzer", False, str(e))
    
    async def test_ncx_magazine_core(self):
        """Test NCX Magazine core functionality"""
        self.print_test_header("NCX Magazine Core Tests")
        
        try:
            from ncx_magazine import NCXMagazine
            
            magazine = NCXMagazine()
            edition = magazine.create_new_edition()
            
            success = (
                edition is not None and
                edition.title == "NCX Magazine" and
                len(edition.editorial_note) > 0
            )
            
            self.test_results["ncx_core"] = success
            self.print_test_result(
                "NCX Magazine Core",
                success,
                f"Edition created: {edition.title}"
            )
            
        except Exception as e:
            self.test_results["ncx_core"] = False
            self.print_test_result("NCX Magazine Core", False, str(e))
    
    async def test_ncx_orchestrator(self):
        """Test NCX orchestrator"""
        self.print_test_header("NCX Orchestrator Tests")
        
        try:
            from ncx_orchestrator import NCXOrchestrator
            
            orchestrator = NCXOrchestrator()
            results = await orchestrator.run_complete_workflow(
                scrape_news=False,
                generate_synthetic=True
            )
            
            success = (
                results['success'] and
                results['edition_info']['total_articles'] > 0
            )
            
            self.test_results["ncx_orchestrator"] = success
            self.performance_metrics["standard"] = results.get('performance', {})
            
            self.print_test_result(
                "NCX Orchestrator",
                success,
                f"Articles: {results['edition_info']['total_articles']}"
            )
            
        except Exception as e:
            self.test_results["ncx_orchestrator"] = False
            self.print_test_result("NCX Orchestrator", False, str(e))
    
    async def test_optimized_orchestrator(self):
        """Test optimized NCX orchestrator"""
        self.print_test_header("Optimized NCX Orchestrator Tests")
        
        try:
            from optimized_ncx_orchestrator import OptimizedNCXOrchestrator
            
            orchestrator = OptimizedNCXOrchestrator()
            results = await orchestrator.run_complete_workflow_optimized(
                scrape_news=False,
                generate_synthetic=True
            )
            
            success = (
                results['success'] and
                results['edition_info']['total_articles'] > 0 and
                results['performance']['optimization_score'] >= 200
            )
            
            self.test_results["optimized_orchestrator"] = success
            self.performance_metrics["optimized"] = results.get('performance', {})
            
            self.print_test_result(
                "Optimized NCX Orchestrator",
                success,
                f"Score: {results['performance']['optimization_score']}, Articles: {results['edition_info']['total_articles']}"
            )
            
        except Exception as e:
            self.test_results["optimized_orchestrator"] = False
            self.print_test_result("Optimized NCX Orchestrator", False, str(e))
    
    def test_file_integrity(self):
        """Test file integrity"""
        self.print_test_header("File Integrity Tests")
        
        required_files = [
            "ncx_magazine/ncx_magazine.py",
            "ncx_magazine/config.json",
            "ncx_magazine/linguistic_analyzer.py",
            "ncx_magazine/ncx_news_scraper.py",
            "ncx_magazine/ncx_orchestrator.py",
            "ncx_magazine/optimized_ncx_orchestrator.py"
        ]
        
        missing_files = []
        for file_path in required_files:
            if os.path.exists(file_path):
                self.print_test_result(f"File: {os.path.basename(file_path)}", True)
            else:
                missing_files.append(file_path)
                self.print_test_result(f"File: {os.path.basename(file_path)}", False, "Missing")
        
        self.test_results["file_integrity"] = len(missing_files) == 0
    
    def test_output_quality(self):
        """Test output quality"""
        self.print_test_header("Output Quality Tests")
        
        try:
            output_dir = "ncx_magazine/output"
            if os.path.exists(output_dir):
                html_files = [f for f in os.listdir(output_dir) if f.endswith('.html')]
                json_files = [f for f in os.listdir(output_dir) if f.endswith('.json')]
                
                has_html = len(html_files) > 0
                has_json = len(json_files) > 0
                
                if has_html:
                    latest_html = max(html_files, key=lambda f: os.path.getmtime(os.path.join(output_dir, f)))
                    html_path = os.path.join(output_dir, latest_html)
                    
                    with open(html_path, 'r') as f:
                        content = f.read()
                    
                    has_title = "NCX Magazine" in content
                    has_punk = "💀" in content or "🎸" in content
                    has_articles = "article" in content.lower()
                    
                    quality_score = sum([has_title, has_punk, has_articles])
                    
                    self.print_test_result("HTML Output", quality_score >= 2, f"Score: {quality_score}/3")
                    self.test_results["html_quality"] = quality_score >= 2
                else:
                    self.print_test_result("HTML Output", False, "No HTML files")
                    self.test_results["html_quality"] = False
                
                if has_json:
                    self.print_test_result("JSON Output", True, f"{len(json_files)} files")
                    self.test_results["json_quality"] = True
                else:
                    self.print_test_result("JSON Output", False, "No JSON files")
                    self.test_results["json_quality"] = False
            else:
                self.print_test_result("Output Directory", False, "Not found")
                self.test_results["html_quality"] = False
                self.test_results["json_quality"] = False
                
        except Exception as e:
            self.print_test_result("Output Quality", False, str(e))
            self.test_results["html_quality"] = False
            self.test_results["json_quality"] = False
    
    def generate_test_report(self):
        """Generate comprehensive test report"""
        self.print_test_header("NCX Magazine Test Report")
        
        total_tests = len(self.test_results)
        passed_tests = sum(1 for result in self.test_results.values() if result)
        success_rate = (passed_tests / total_tests * 100) if total_tests > 0 else 0
        
        print(f"\n📊 Test Summary:")
        print(f"   Total Tests: {total_tests}")
        print(f"   Passed: {passed_tests}")
        print(f"   Failed: {total_tests - passed_tests}")
        print(f"   Success Rate: {success_rate:.1f}%")
        
        if self.performance_metrics:
            print(f"\n⚡ Performance Comparison:")
            
            if "standard" in self.performance_metrics:
                std = self.performance_metrics["standard"]
                print(f"   Standard:")
                print(f"      Time: {std.get('total_time', 0):.3f}s")
                print(f"      Articles/sec: {std.get('articles_per_second', 0):.1f}")
            
            if "optimized" in self.performance_metrics:
                opt = self.performance_metrics["optimized"]
                print(f"   Optimized:")
                print(f"      Time: {opt.get('total_time', 0):.3f}s")
                print(f"      Articles/sec: {opt.get('articles_per_second', 0):.1f}")
                print(f"      Optimization Score: {opt.get('optimization_score', 0)}")
                print(f"      Efficiency Gain: {opt.get('efficiency_gain', 0)}%")
        
        if success_rate >= 90:
            print(f"\n🎸 OVERALL ASSESSMENT: PUNK AS FUCK")
            print(f"   NCX Magazine is ready to expose the hidden foes!")
        elif success_rate >= 80:
            print(f"\n✅ OVERALL ASSESSMENT: SOLID")
            print(f"   System is functional with minor issues.")
        else:
            print(f"\n⚠️  OVERALL ASSESSMENT: NEEDS WORK")
            print(f"   Some issues need attention.")
        
        return {
            "success_rate": success_rate,
            "total_tests": total_tests,
            "passed_tests": passed_tests,
            "ready_for_production": success_rate >= 90
        }
    
    async def run_all_tests(self):
        """Run all comprehensive tests"""
        print("🎸 Starting NCX Magazine Comprehensive Test Suite...")
        print("=" * 60)
        
        # Run all test categories
        await self.test_linguistic_analyzer()
        await self.test_ncx_magazine_core()
        await self.test_ncx_orchestrator()
        await self.test_optimized_orchestrator()
        self.test_file_integrity()
        self.test_output_quality()
        
        # Generate final report
        return self.generate_test_report()

async def main():
    """Main testing function"""
    tester = NCXComprehensiveTester()
    report = await tester.run_all_tests()
    
    # Save test report
    with open("ncx_test_report.json", "w") as f:
        json.dump(report, f, indent=2)
    
    print(f"\n📄 Test report saved to: ncx_test_report.json")
    
    return report["ready_for_production"]

if __name__ == "__main__":
    ready = asyncio.run(main())
    sys.exit(0 if ready else 1)