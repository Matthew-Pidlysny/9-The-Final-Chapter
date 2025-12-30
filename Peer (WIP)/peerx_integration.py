#!/usr/bin/env python3
"""
Peerx - Enhanced Peer System Integration
Combines all enhancements: Units detection, Subject classification, Stuck button, Multi-modal input
"""

import sys
import json
from typing import Dict, List, Optional, Tuple, Any
from dataclasses import dataclass, asdict
from enum import Enum

from units_database import UnitsDatabase, UnitInfo, VariableInfo
from subject_classifier import SubjectClassifier, SubjectDomain, ClassificationResult
from stuck_button_assistant import StuckButtonAssistant, FormulaSuggestion


class InterfaceMode(Enum):
    """User interface modes"""
    BASIC = "Basic"
    STANDARD = "Standard"
    EXPERT = "Expert"


@dataclass
class InputAnalysis:
    """Complete analysis of user input"""
    original_input: str
    classification: ClassificationResult
    variables_detected: Dict[str, VariableInfo]
    units_detected: Dict[str, UnitInfo]
    domain: str
    is_in_scope: bool
    warnings: List[str]
    suggestions: List[str]


@dataclass
class ValidationResult:
    """Result of formula validation"""
    is_valid: bool
    errors: List[str]
    warnings: List[str]
    formatted_formula: str
    analysis: InputAnalysis


class PeerxSystem:
    """
    Enhanced Peer system with all improvements
    """
    
    def __init__(self, mode: InterfaceMode = InterfaceMode.STANDARD):
        self.mode = mode
        self.units_db = UnitsDatabase()
        self.classifier = SubjectClassifier()
        self.assistant = StuckButtonAssistant()
        
        # Configuration based on mode
        self._configure_mode()
    
    def _configure_mode(self):
        """Configure system based on interface mode"""
        if self.mode == InterfaceMode.BASIC:
            self.explanation_level = "beginner"
            self.show_advanced_options = False
            self.auto_correct = True
            self.verbose = False
        elif self.mode == InterfaceMode.STANDARD:
            self.explanation_level = "intermediate"
            self.show_advanced_options = True
            self.auto_correct = False
            self.verbose = False
        else:  # EXPERT
            self.explanation_level = "expert"
            self.show_advanced_options = True
            self.auto_correct = False
            self.verbose = True
    
    def process_input(self, user_input: str, max_length: int = 2000) -> ValidationResult:
        """
        Process user input through complete pipeline
        
        Args:
            user_input: User's formula or description
            max_length: Maximum length for stuck button assistant
            
        Returns:
            ValidationResult with complete analysis
        """
        # Step 1: Classify subject matter
        classification = self.classifier.classify(user_input)
        
        # Step 2: Detect variables
        variables_detected = self.units_db.analyze_formula_variables(user_input)
        
        # Step 3: Detect units
        units_detected = self._detect_units_in_input(user_input)
        
        # Step 4: Determine if in scope
        is_in_scope = classification.domain not in [SubjectDomain.HUMANITIES, 
                                                   SubjectDomain.EVERYDAY]
        
        # Step 5: Generate warnings and suggestions
        warnings = []
        suggestions = []
        
        if not is_in_scope:
            warnings.append(classification.warning_message or "Input is outside Peer's scope")
            suggestions.extend(classification.suggestions or [])
        
        # Add variable/unit warnings
        if variables_detected and self.mode == InterfaceMode.EXPERT:
            suggestions.append(f"Variables detected: {', '.join(variables_detected.keys())}")
        
        if units_detected and self.mode in [InterfaceMode.STANDARD, InterfaceMode.EXPERT]:
            suggestions.append(f"Units detected: {', '.join(units_detected.keys())}")
        
        # Step 6: Format formula
        formatted_formula = self._format_formula(user_input)
        
        # Create input analysis
        analysis = InputAnalysis(
            original_input=user_input,
            classification=classification,
            variables_detected=variables_detected,
            units_detected=units_detected,
            domain=classification.domain.value,
            is_in_scope=is_in_scope,
            warnings=warnings,
            suggestions=suggestions
        )
        
        # Step 7: Validate
        errors = self._validate_formula(formatted_formula)
        
        # Add classification warnings to validation errors if out of scope
        if not is_in_scope:
            errors.append("Input is outside Peer's scope. Please enter a mathematical or scientific formula.")
        
        return ValidationResult(
            is_valid=len(errors) == 0 and is_in_scope,
            errors=errors,
            warnings=warnings,
            formatted_formula=formatted_formula,
            analysis=analysis
        )
    
    def _detect_units_in_input(self, text: str) -> Dict[str, UnitInfo]:
        """Detect units in user input"""
        detected = {}
        
        # Check for known units
        for unit_name, unit_info in self.units_db.units.items():
            if unit_name.lower() in text.lower() or unit_info.symbol.lower() in text.lower():
                detected[unit_info.symbol] = unit_info
        
        return detected
    
    def _format_formula(self, text: str) -> str:
        """Format formula for processing"""
        # Basic formatting
        formatted = text.strip()
        
        # Clean up extra spaces
        import re
        formatted = re.sub(r'\s+', ' ', formatted)
        formatted = re.sub(r'\s*([+\-*/=<>≈≤≥≠])\s*', r' \1 ', formatted)
        formatted = re.sub(r'\s+', ' ', formatted).strip()
        
        return formatted
    
    def _validate_formula(self, formula: str) -> List[str]:
        """Validate formula syntax"""
        errors = []
        
        # Check for balanced parentheses
        if formula.count('(') != formula.count(')'):
            errors.append("Unbalanced parentheses")
        
        # Check for valid operators
        valid_operators = ['+', '-', '*', '/', '^', '=', '<', '>', '≈', '≤', '≥', '≠']
        # This is a simplified check - actual validation would be more complex
        # For now, we'll just check if there's at least one operator or equals sign
        has_operator = any(op in formula for op in valid_operators)
        has_equals = '=' in formula
        
        if not (has_operator or has_equals):
            # Could still be valid if it's just a variable or number
            pass
        
        # Check for common syntax errors
        if formula.endswith(' ') and len(formula) > 1:
            pass  # Trailing space is okay
        
        return errors
    
    def help_stuck_user(self, user_input: str) -> FormulaSuggestion:
        """
        Help a user who is stuck on formula input
        Uses the stuck button assistant
        
        Args:
            user_input: User's description of what they want to enter
            
        Returns:
            FormulaSuggestion with formatting help
        """
        return self.assistant.help_user(user_input)
    
    def get_quick_tips(self) -> List[str]:
        """Get quick tips for formula input"""
        return self.assistant.get_quick_tips()
    
    def analyze_variable_with_units(self, variable: str, unit_str: str) -> Dict[str, Any]:
        """
        Analyze a variable with its associated units
        
        Args:
            variable: Variable name (e.g., 'v', 'gamma')
            unit_str: Unit string (e.g., 'm/s', 'meters per second')
            
        Returns:
            Dictionary with analysis results
        """
        # Detect variable info
        var_info = self.units_db.detect_variable(variable)
        
        # Detect unit info
        unit_info = self.units_db.detect_unit(unit_str)
        
        result = {
            "variable": variable,
            "unit": unit_str,
            "variable_meanings": var_info.common_meanings if var_info else [],
            "variable_domains": var_info.typical_domains if var_info else [],
            "unit_category": unit_info.category.value if unit_info else None,
            "unit_description": unit_info.description if unit_info else None,
            "is_valid": unit_info is not None
        }
        
        return result
    
    def set_mode(self, mode: InterfaceMode):
        """Change interface mode"""
        self.mode = mode
        self._configure_mode()
    
    def get_system_info(self) -> Dict[str, Any]:
        """Get system information"""
        return {
            "mode": self.mode.value,
            "explanation_level": self.explanation_level,
            "show_advanced_options": self.show_advanced_options,
            "auto_correct": self.auto_correct,
            "units_in_database": self.units_db.get_total_units_count(),
            "variables_in_database": self.units_db.get_total_variables_count(),
            "supported_domains": [d.value for d in SubjectDomain if d not in 
                               [SubjectDomain.HUMANITIES, SubjectDomain.EVERYDAY, SubjectDomain.UNKNOWN]]
        }


def print_result(result: ValidationResult, show_details: bool = True):
    """Pretty print validation result"""
    print("\n" + "=" * 70)
    print("PEERX VALIDATION RESULT")
    print("=" * 70)
    
    print(f"\nOriginal Input: {result.analysis.original_input}")
    print(f"Formatted Formula: {result.formatted_formula}")
    print(f"Domain: {result.analysis.domain}")
    print(f"In Scope: {'✓ Yes' if result.analysis.is_in_scope else '✗ No'}")
    print(f"Valid: {'✓ Yes' if result.is_valid else '✗ No'}")
    
    if show_details:
        if result.analysis.variables_detected:
            print(f"\nVariables Detected:")
            for var, info in result.analysis.variables_detected.items():
                print(f"  • {var}: {', '.join(info.common_meanings[:3])}")
        
        if result.analysis.units_detected:
            print(f"\nUnits Detected:")
            for unit, info in result.analysis.units_detected.items():
                print(f"  • {unit}: {info.category.value}")
        
        if result.errors:
            print(f"\n❌ Errors:")
            for error in result.errors:
                print(f"  • {error}")
        
        if result.warnings:
            print(f"\n⚠️  Warnings:")
            for warning in result.warnings:
                print(f"  • {warning}")
        
        if result.analysis.suggestions:
            print(f"\n💡 Suggestions:")
            for suggestion in result.analysis.suggestions:
                print(f"  • {suggestion}")
    
    print("\n" + "=" * 70)


if __name__ == "__main__":
    # Test the integrated system
    print("PEERX - Enhanced Peer System")
    print("=" * 70)
    
    # Initialize system
    system = PeerxSystem(mode=InterfaceMode.STANDARD)
    
    # Display system info
    print("\nSystem Information:")
    info = system.get_system_info()
    for key, value in info.items():
        print(f"  {key}: {value}")
    
    # Test cases
    test_inputs = [
        "a + b / [gamma] = z",
        "E = mc^2",
        "F = m * a",
        "What is the capital of France?",
        "velocity plus acceleration times time",
        "sin(theta) = opposite/hypotenuse",
        "Tell me about the history of Rome",
        "sqrt(x^2 + y^2)",
        "dy/dx = 2x",
        "How do I bake a cake?",
    ]
    
    print("\n" + "=" * 70)
    print("TESTING INPUTS")
    print("=" * 70)
    
    for test_input in test_inputs:
        result = system.process_input(test_input)
        print_result(result, show_details=True)
        
        # Test stuck button for ambiguous inputs
        if not result.is_valid and result.analysis.domain in ["Unknown", "Everyday Topics", "Humanities"]:
            print("\n🆘 Stuck Button Help:")
            suggestion = system.help_stuck_user(test_input)
            print(f"{suggestion.explanation}")
    
    # Test variable with units analysis
    print("\n" + "=" * 70)
    print("TESTING VARIABLE + UNIT ANALYSIS")
    print("=" * 70)
    
    test_var_units = [
        ("v", "m/s"),
        ("gamma", ""),
        ("E", "J"),
        ("a", "m/s^2"),
    ]
    
    for var, unit in test_var_units:
        analysis = system.analyze_variable_with_units(var, unit)
        print(f"\nVariable: {var} | Unit: {unit or 'None'}")
        if analysis["variable_meanings"]:
            print(f"  Meanings: {', '.join(analysis['variable_meanings'][:3])}")
        if analysis["unit_category"]:
            print(f"  Unit Category: {analysis['unit_category']}")
    
    print("\n" + "=" * 70)
    print("QUICK TIPS")
    print("=" * 70)
    
    for i, tip in enumerate(system.get_quick_tips(), 1):
        print(f"{i}. {tip}")
    
    print("\n" + "=" * 70)
    print("TESTING COMPLETE")
    print("=" * 70)