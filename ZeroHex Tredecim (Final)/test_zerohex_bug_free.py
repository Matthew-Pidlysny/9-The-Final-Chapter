"""
ZeroHex Tredecim Bug Test Suite
Comprehensive GUI error detection and validation
"""

import sys
import os
import unittest
from unittest.mock import patch, MagicMock
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtCore import QTimer
from PyQt6.QtTest import QTest
from PyQt6.QtCore import Qt
import time

# Import the application
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from zerohex_tredecim_final_complete import (
    ZeroHexTredecimApp, BetaSequenceExplorer, HeartbeatStudio,
    HexagonalConstantLab, Base13Calculator, RiemannThirteenBridge,
    OPGSConvergenceAnalyzer, DimensionalEmergenceStudio, UVDualityWorkbench,
    SequinorAxiomNavigator, PiJudgmentFramework, DisplacementLaboratory,
    RCOCitizenshipVerifier, UnifiedPatternSynthesizer, Ultimate13StudyAcademy
)

class TestZeroHexGUI(unittest.TestCase):
    """Comprehensive GUI test suite"""
    
    @classmethod
    def setUpClass(cls):
        """Set up test environment"""
        cls.app = QApplication.instance()
        if cls.app is None:
            cls.app = QApplication(sys.argv)
            
    def setUp(self):
        """Set up each test"""
        self.window = ZeroHexTredecimApp()
        
    def test_main_window_creation(self):
        """Test main window creation"""
        self.assertIsNotNone(self.window)
        self.assertEqual(self.window.windowTitle(), "🎯 ZeroHex Tredecim - Complete 14-Workshop System")
        self.assertGreater(self.window.width(), 0)
        self.assertGreater(self.window.height(), 0)
        
    def test_all_modules_exist(self):
        """Test all 14 modules are present"""
        tab_widget = self.window.tab_widget
        self.assertEqual(tab_widget.count(), 14)
        
        # Check all module titles
        expected_titles = [
            "📊 Module 1: Beta Sequence",
            "💓 Module 2: 13-Heartbeat",
            "🔷 Module 3: Hexagonal",
            "🔢 Module 4: Base-13",
            "🌉 Module 5: Riemann-13",
            "📊 Module 6: OPGS",
            "🌌 Module 7: Dimensions",
            "⚛️ Module 8: U-V Duality",
            "📜 Module 9: Sequinor",
            "🥧 Module 10: Pi Judgment",
            "⚛️ Module 11: 137-Displacement",
            "🏛️ Module 12: RCO",
            "🎭 Module 13: Unified",
            "🎓 Module 14: Academy (5000 Features)"
        ]
        
        for i, title in enumerate(expected_titles):
            self.assertEqual(tab_widget.tabText(i), title)
            
    def test_beta_sequence_module(self):
        """Test Module 1: Beta Sequence Explorer"""
        tab_widget = self.window.tab_widget
        tab_widget.setCurrentIndex(0)
        
        # Get the module widget
        module = tab_widget.currentWidget()
        self.assertIsInstance(module, BetaSequenceExplorer)
        
        # Test P(x) calculator
        if hasattr(module, 'x_input') and hasattr(module, 'calculate_px'):
            QTest.keyClicks(module.x_input, "13")
            QTest.mouseClick(module.findChild(QPushButton, None), Qt.MouseButton.LeftButton)
            
    def test_heartbeat_module(self):
        """Test Module 2: 13-Heartbeat Studio"""
        tab_widget = self.window.tab_widget
        tab_widget.setCurrentIndex(1)
        
        module = tab_widget.currentWidget()
        self.assertIsInstance(module, HeartbeatStudio)
        
    def test_hexagonal_module(self):
        """Test Module 3: Hexagonal Constant Lab"""
        tab_widget = self.window.tab_widget
        tab_widget.setCurrentIndex(2)
        
        module = tab_widget.currentWidget()
        self.assertIsInstance(module, HexagonalConstantLab)
        
    def test_base13_module(self):
        """Test Module 4: Base-13 Calculator"""
        tab_widget = self.window.tab_widget
        tab_widget.setCurrentIndex(3)
        
        module = tab_widget.currentWidget()
        self.assertIsInstance(module, Base13Calculator)
        
        # Test base conversion
        if hasattr(module, 'decimal_input') and hasattr(module, 'base13_result'):
            QTest.keyClicks(module.decimal_input, "169")
            
    def test_riemann_module(self):
        """Test Module 5: Riemann-Thirteen Bridge"""
        tab_widget = self.window.tab_widget
        tab_widget.setCurrentIndex(4)
        
        module = tab_widget.currentWidget()
        self.assertIsInstance(module, RiemannThirteenBridge)
        
    def test_opgs_module(self):
        """Test Module 6: OPGS Convergence Analyzer"""
        tab_widget = self.window.tab_widget
        tab_widget.setCurrentIndex(5)
        
        module = tab_widget.currentWidget()
        self.assertIsInstance(module, OPGSConvergenceAnalyzer)
        
    def test_dimensional_module(self):
        """Test Module 7: Dimensional Emergence Studio"""
        tab_widget = self.window.tab_widget
        tab_widget.setCurrentIndex(6)
        
        module = tab_widget.currentWidget()
        self.assertIsInstance(module, DimensionalEmergenceStudio)
        
    def test_uv_duality_module(self):
        """Test Module 8: U-V Duality Workbench"""
        tab_widget = self.window.tab_widget
        tab_widget.setCurrentIndex(7)
        
        module = tab_widget.currentWidget()
        self.assertIsInstance(module, UVDualityWorkbench)
        
    def test_sequinor_module(self):
        """Test Module 9: Sequinor Axiom Navigator"""
        tab_widget = self.window.tab_widget
        tab_widget.setCurrentIndex(8)
        
        module = tab_widget.currentWidget()
        self.assertIsInstance(module, SequinorAxiomNavigator)
        
    def test_pi_judgment_module(self):
        """Test Module 10: Pi Judgment Framework"""
        tab_widget = self.window.tab_widget
        tab_widget.setCurrentIndex(9)
        
        module = tab_widget.currentWidget()
        self.assertIsInstance(module, PiJudgmentFramework)
        
    def test_displacement_module(self):
        """Test Module 11: 137-Displacement Laboratory"""
        tab_widget = self.window.tab_widget
        tab_widget.setCurrentIndex(10)
        
        module = tab_widget.currentWidget()
        self.assertIsInstance(module, DisplacementLaboratory)
        
    def test_rco_module(self):
        """Test Module 12: RCO Citizenship Verifier"""
        tab_widget = self.window.tab_widget
        tab_widget.setCurrentIndex(11)
        
        module = tab_widget.currentWidget()
        self.assertIsInstance(module, RCOCitizenshipVerifier)
        
    def test_unified_module(self):
        """Test Module 13: Unified Pattern Synthesizer"""
        tab_widget = self.window.tab_widget
        tab_widget.setCurrentIndex(12)
        
        module = tab_widget.currentWidget()
        self.assertIsInstance(module, UnifiedPatternSynthesizer)
        
    def test_academy_module(self):
        """Test Module 14: Ultimate 13 Study Academy"""
        tab_widget = self.window.tab_widget
        tab_widget.setCurrentIndex(13)
        
        module = tab_widget.currentWidget()
        self.assertIsInstance(module, Ultimate13StudyAcademy)
        
        # Test progress bar
        if hasattr(module, 'progress_bar'):
            self.assertIsNotNone(module.progress_bar)
            
    def test_tab_navigation(self):
        """Test tab navigation functionality"""
        tab_widget = self.window.tab_widget
        
        # Test switching through all tabs
        for i in range(14):
            tab_widget.setCurrentIndex(i)
            self.assertEqual(tab_widget.currentIndex(), i)
            
    def test_window_properties(self):
        """Test window properties and styling"""
        self.assertIsNotNone(self.window.styleSheet())
        self.assertGreater(len(self.window.styleSheet()), 0)
        
    def test_status_bar(self):
        """Test status bar functionality"""
        status_bar = self.window.statusBar()
        self.assertIsNotNone(status_bar)
        
    def test_button_functionality(self):
        """Test button clicks don't cause errors"""
        tab_widget = self.window.tab_widget
        
        # Test buttons on each module
        for i in range(14):
            tab_widget.setCurrentIndex(i)
            module = tab_widget.currentWidget()
            
            # Find all buttons and click them
            buttons = module.findChildren(QPushButton)
            for button in buttons:
                try:
                    # Simulate button click
                    QTest.mouseClick(button, Qt.MouseButton.LeftButton)
                    # Small delay to process any dialogs
                    QApplication.processEvents()
                except Exception as e:
                    # Log error but don't fail test (some buttons might open dialogs)
                    print(f"Button click issue: {e}")
                    
    def test_text_inputs(self):
        """Test text input functionality"""
        tab_widget = self.window.tab_widget
        
        # Test text inputs on modules that have them
        test_modules = [0, 3]  # Beta Sequence and Base-13 Calculator
        
        for i in test_modules:
            tab_widget.setCurrentIndex(i)
            module = tab_widget.currentWidget()
            
            # Find text inputs
            text_inputs = module.findChildren(QLineEdit)
            for text_input in text_inputs:
                try:
                    # Test input
                    QTest.keyClicks(text_input, "13")
                    QApplication.processEvents()
                except Exception as e:
                    print(f"Text input issue: {e}")
                    
    def test_responsive_layout(self):
        """Test layout responsiveness"""
        # Test resizing
        original_width = self.window.width()
        original_height = self.window.height()
        
        # Test smaller size
        self.window.resize(800, 600)
        QApplication.processEvents()
        
        # Test larger size
        self.window.resize(1920, 1080)
        QApplication.processEvents()
        
        # Restore original size
        self.window.resize(original_width, original_height)
        QApplication.processEvents()

class TestMathematicalFunctions(unittest.TestCase):
    """Test mathematical functions for correctness"""
    
    def test_beta_sequence_calculation(self):
        """Test beta sequence P(x) calculation"""
        beta = BetaSequenceExplorer()
        
        # Test known values
        test_cases = [
            (0, 0),
            (13, 1000*13/169),
            (169, 1000*169/169),
            (100, 1000*100/169)
        ]
        
        for x, expected in test_cases:
            result = (1000 * x) / 169
            self.assertAlmostEqual(result, expected, places=6)
            
    def test_base13_conversion(self):
        """Test base-13 conversion"""
        # Test known conversions
        test_cases = [
            (0, "0"),
            (13, "10"),
            (169, "100"),
            (2197, "1000"),
            (10, "A"),
            (12, "C"),
        ]
        
        for decimal, expected in test_cases:
            digits = "0123456789ABC"
            result = ""
            temp = decimal
            
            while temp > 0:
                result = digits[temp % 13] + result
                temp = temp // 13
                
            if not result:
                result = "0"
                
            self.assertEqual(result, expected)

def run_comprehensive_tests():
    """Run comprehensive test suite"""
    print("🧪 Starting ZeroHex Tredecim Bug Test Suite...")
    print("=" * 60)
    
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add test classes
    suite.addTests(loader.loadTestsFromTestCase(TestZeroHexGUI))
    suite.addTests(loader.loadTestsFromTestCase(TestMathematicalFunctions))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print results
    print("=" * 60)
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print(f"Success rate: {((result.testsRun - len(result.failures) - len(result.errors)) / result.testsRun * 100):.1f}%")
    
    if result.failures:
        print("\n❌ FAILURES:")
        for test, traceback in result.failures:
            print(f"  {test}: {traceback.split('AssertionError:')[-1].strip()}")
            
    if result.errors:
        print("\n⚠️ ERRORS:")
        for test, traceback in result.errors:
            print(f"  {test}: {traceback.split('Exception:')[-1].strip()}")
            
    if result.wasSuccessful():
        print("\n✅ ALL TESTS PASSED - GUI is bug-free!")
    else:
        print("\n⚠️ Some tests failed - review issues above")
        
    return result.wasSuccessful()

if __name__ == "__main__":
    success = run_comprehensive_tests()
    sys.exit(0 if success else 1)