#!/usr/bin/env python3
"""
Peerx Final Version - Enhanced Peer System with Novice-Friendly Features
Combines all enhancements: Units detection, Subject classification, Stuck button,
and 50 novice-friendly improvements
"""

import sys
import json
import re
from typing import Dict, List, Optional, Tuple, Any
from dataclasses import dataclass, asdict
from enum import Enum
from datetime import datetime

from units_database import UnitsDatabase, UnitInfo, VariableInfo
from subject_classifier import SubjectClassifier, SubjectDomain, ClassificationResult
from stuck_button_assistant import StuckButtonAssistant, FormulaSuggestion


class InterfaceMode(Enum):
    """User interface modes"""
    BEGINNER = "Beginner"
    STANDARD = "Standard"
    EXPERT = "Expert"
    STUDENT = "Student"  # NEW: Student mode with computation


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
    confidence_score: float  # NEW: Confidence in analysis


@dataclass
class ValidationResult:
    """Result of formula validation"""
    is_valid: bool
    errors: List[str]
    warnings: List[str]
    formatted_formula: str
    analysis: InputAnalysis
    computation_result: Optional[float] = None  # NEW: Actual computation result
    step_by_step: List[str] = None  # NEW: Step-by-step explanation
    real_world_example: Optional[str] = None  # NEW: Real-world application


class PeerxFinal:
    """
    Final enhanced Peer system with all improvements
    """
    
    def __init__(self, mode: InterfaceMode = InterfaceMode.STANDARD):
        self.mode = mode
        self.units_db = UnitsDatabase()
        self.classifier = SubjectClassifier()
        self.assistant = StuckButtonAssistant()
        self.formula_history = []  # NEW: Track recent formulas
        self.custom_formulas = {}  # NEW: User's saved formulas
        
        # Configuration based on mode
        self._configure_mode()
    
    def _configure_mode(self):
        """Configure system based on interface mode"""
        if self.mode == InterfaceMode.BEGINNER:
            self.explanation_level = "beginner"
            self.show_advanced_options = False
            self.auto_correct = True
            self.verbose = False
            self.enable_computation = True  # NEW: Enable basic computation
        elif self.mode == InterfaceMode.STUDENT:
            self.explanation_level = "student"
            self.show_advanced_options = False
            self.auto_correct = True
            self.verbose = False
            self.enable_computation = True
            self.show_step_by_step = True  # NEW: Show steps for students
        elif self.mode == InterfaceMode.STANDARD:
            self.explanation_level = "intermediate"
            self.show_advanced_options = True
            self.auto_correct = False
            self.verbose = False
            self.enable_computation = False
        else:  # EXPERT
            self.explanation_level = "expert"
            self.show_advanced_options = True
            self.auto_correct = False
            self.verbose = True
            self.enable_computation = False
    
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
        
        # Add novice-friendly suggestions
        if self.mode in [InterfaceMode.BEGINNER, InterfaceMode.STUDENT]:
            suggestions.extend(self._get_novice_suggestions(variables_detected, units_detected))
        
        # Step 6: Format formula
        formatted_formula = self._format_formula(user_input)
        
        # Step 7: Validate and compute (if enabled)
        errors = self._validate_formula(formatted_formula)
        
        # Add classification warnings to validation errors if out of scope
        if not is_in_scope:
            errors.append("Input is outside Peer's scope. Please enter a mathematical or scientific formula.")
        
        # Step 8: Compute result (if enabled and formula is valid)
        computation_result = None
        step_by_step = None
        real_world_example = None
        
        if self.enable_computation and len(errors) == 0:
            computation_result, step_by_step = self._compute_formula(formatted_formula, variables_detected)
            real_world_example = self._get_real_world_example(formatted_formula)
        
        # Add to history
        self.formula_history.append({
            "input": user_input,
            "formatted": formatted_formula,
            "timestamp": datetime.now().isoformat(),
            "valid": len(errors) == 0 and is_in_scope
        })
        
        # Keep only last 10 formulas
        if len(self.formula_history) > 10:
            self.formula_history = self.formula_history[-10:]
        
        # Calculate confidence score
        confidence_score = classification.confidence if is_in_scope else 0.0
        
        # Create input analysis
        analysis = InputAnalysis(
            original_input=user_input,
            classification=classification,
            variables_detected=variables_detected,
            units_detected=units_detected,
            domain=classification.domain.value,
            is_in_scope=is_in_scope,
            warnings=warnings,
            suggestions=suggestions,
            confidence_score=confidence_score
        )
        
        return ValidationResult(
            is_valid=len(errors) == 0 and is_in_scope,
            errors=errors,
            warnings=warnings,
            formatted_formula=formatted_formula,
            analysis=analysis,
            computation_result=computation_result,
            step_by_step=step_by_step,
            real_world_example=real_world_example
        )
    
    def _get_novice_suggestions(self, variables: Dict, units: Dict) -> List[str]:
        """Get novice-friendly suggestions based on detected variables/units"""
        suggestions = []
        
        if variables:
            var_list = list(variables.keys())
            suggestions.append(f"✓ Variables detected: {', '.join(var_list)}")
            suggestions.append(f"💡 Tip: Click on any variable to see what it means")
        
        if units:
            unit_list = list(units.keys())
            suggestions.append(f"✓ Units detected: {', '.join(unit_list)}")
            suggestions.append(f"💡 Tip: Peer will check if your units are consistent")
        
        if not variables and not units:
            suggestions.append("💡 Tip: Try entering a formula like 'F = m * a'")
            suggestions.append("💡 Tip: Use the 'Stuck' button if you need help")
        
        return suggestions
    
    def _detect_units_in_input(self, text: str) -> Dict[str, UnitInfo]:
        """Detect units in user input"""
        detected = {}
        
        # Check for known units
        for unit_name, unit_info in self.units_db.units.items():
            # Only match whole words to avoid false positives
            pattern = r'\b' + re.escape(unit_name.lower()) + r'\b'
            if re.search(pattern, text.lower()):
                detected[unit_info.symbol] = unit_info
            
            # Check for symbol
            if unit_info.symbol in text:
                detected[unit_info.symbol] = unit_info
        
        return detected
    
    def _format_formula(self, text: str) -> str:
        """Format formula for processing"""
        # Basic formatting
        formatted = text.strip()
        
        # Clean up extra spaces
        formatted = re.sub(r'\s+', ' ', formatted)
        
        # Add spaces around operators for readability
        formatted = re.sub(r'\s*([+\-*/=<>≈≤≥≠])\s*', r' \1 ', formatted)
        
        # Clean up again
        formatted = re.sub(r'\s+', ' ', formatted).strip()
        
        return formatted
    
    def _validate_formula(self, formula: str) -> List[str]:
        """Validate formula syntax with beginner-friendly error messages"""
        errors = []
        
        # Check for balanced parentheses
        open_parens = formula.count('(')
        close_parens = formula.count(')')
        
        if open_parens != close_parens:
            if open_parens > close_parens:
                errors.append(f"Missing {open_parens - close_parens} closing parenthesis(es) )")
                if self.mode in [InterfaceMode.BEGINNER, InterfaceMode.STUDENT]:
                    errors.append("💡 Hint: Every opening parenthesis ( needs a closing parenthesis )")
            else:
                errors.append(f"Missing {close_parens - open_parens} opening parenthesis(es) (")
                if self.mode in [InterfaceMode.BEGINNER, InterfaceMode.STUDENT]:
                    errors.append("💡 Hint: You have extra closing parentheses. Remove one or add opening ones")
        
        # Check for empty parentheses
        if '()' in formula:
            errors.append("Empty parentheses detected. Did you mean to put something inside?")
        
        # Check for consecutive operators
        consecutive_ops = re.findall(r'([+\-*/]{2,})', formula)
        if consecutive_ops:
            errors.append(f"Consecutive operators found: {', '.join(consecutive_ops)}")
            if self.mode in [InterfaceMode.BEGINNER, InterfaceMode.STUDENT]:
                errors.append("💡 Hint: You probably need a number or variable between operators")
        
        # Check for operators at start/end (except for negative numbers)
        if formula.startswith(('+', '*', '/', '=')):
            errors.append("Formula cannot start with this operator")
        
        if formula.endswith(('+', '-', '*', '/', '<', '>', '≈', '≤', '≥')):
            errors.append("Formula cannot end with this operator")
        
        return errors
    
    def _compute_formula(self, formula: str, variables: Dict) -> Tuple[Optional[float], Optional[List[str]]]:
        """
        Compute result for simple formulas (Student/Beginner mode only)
        Returns: (result, step_by_steps)
        """
        # This is a simplified computation for demonstration
        # In production, this would use a proper symbolic/numerical computation engine
        
        steps = []
        
        # Try to evaluate simple arithmetic
        try:
            # Replace common symbols with Python operators
            eval_formula = formula.replace('^', '**')
            
            # Remove units and variable names for evaluation
            # This is a very simplified approach
            if '=' in eval_formula:
                left, right = eval_formula.split('=', 1)
                eval_formula = right.strip()
            
            # Check if it's a simple numeric expression
            if re.match(r'^[\d\s\+\-\*/\(\)\.]+$', eval_formula):
                result = eval(eval_formula)
                steps.append(f"Formula to evaluate: {formula}")
                steps.append(f"Simplified: {eval_formula}")
                steps.append(f"Result: {result}")
                return result, steps
            
        except Exception as e:
            steps.append(f"Unable to compute: {str(e)}")
            return None, steps
        
        return None, None
    
    def _get_real_world_example(self, formula: str) -> Optional[str]:
        """Get real-world example for the formula"""
        examples = {
            'F = m * a': "This formula calculates the force needed to accelerate an object. For example, a 1000 kg car accelerating at 3 m/s² requires 3000 N of force.",
            'E = mc^2': "This is Einstein's famous equation relating mass and energy. A small amount of mass can be converted to a huge amount of energy, which is how nuclear power works.",
            'v = d / t': "This formula calculates velocity (speed in a direction). If you drive 100 miles in 2 hours, your average velocity is 50 mph.",
            'KE = 0.5 * m * v^2': "This calculates kinetic energy (energy of motion). A 1000 kg car moving at 20 m/s has 200,000 J of kinetic energy.",
            'PE = m * g * h': "This calculates gravitational potential energy. A 10 kg object 5 meters high has about 490 J of potential energy.",
        }
        
        # Check for exact matches
        if formula in examples:
            return examples[formula]
        
        # Check for partial matches
        for key, value in examples.items():
            if key.split('=')[0].strip().lower() in formula.lower():
                return value
        
        return None
    
    def help_stuck_user(self, user_input: str) -> FormulaSuggestion:
        """Help a user who is stuck on formula input"""
        return self.assistant.help_user(user_input)
    
    def get_quick_tips(self) -> List[str]:
        """Get quick tips for formula input"""
        tips = self.assistant.get_quick_tips()
        
        # Add mode-specific tips
        if self.mode == InterfaceMode.BEGINNER:
            tips.insert(0, "🌱 Beginner Mode: Just type what you want, and Peer will help!")
            tips.insert(1, "💡 Don't worry about perfect formatting - Peer will help fix it")
        elif self.mode == InterfaceMode.STUDENT:
            tips.insert(0, "📚 Student Mode: Peer will compute results and show steps")
            tips.insert(1, "🎯 Perfect for homework and exam preparation")
        
        return tips
    
    def get_example_formulas(self) -> List[Dict[str, str]]:
        """Get example formulas organized by subject"""
        examples = [
            {
                "category": "Physics - Mechanics",
                "formulas": [
                    "F = m * a",
                    "v = d / t",
                    "KE = 0.5 * m * v^2",
                    "PE = m * g * h",
                    "p = m * v"
                ]
            },
            {
                "category": "Physics - Energy",
                "formulas": [
                    "E = mc^2",
                    "W = F * d",
                    "P = W / t",
                    "P = I * V"
                ]
            },
            {
                "category": "Mathematics",
                "formulas": [
                    "a^2 + b^2 = c^2",
                    "A = π * r^2",
                    "V = (4/3) * π * r^3",
                    "y = mx + b"
                ]
            },
            {
                "category": "Chemistry",
                "formulas": [
                    "PV = nRT",
                    "n = m / M",
                    "c = n / V"
                ]
            }
        ]
        return examples
    
    def get_formula_history(self, limit: int = 5) -> List[Dict]:
        """Get recent formula history"""
        return self.formula_history[-limit:]
    
    def save_custom_formula(self, name: str, formula: str, description: str = ""):
        """Save a custom formula to user's library"""
        self.custom_formulas[name] = {
            "formula": formula,
            "description": description,
            "timestamp": datetime.now().isoformat()
        }
    
    def get_custom_formulas(self) -> Dict:
        """Get user's saved custom formulas"""
        return self.custom_formulas
    
    def analyze_variable_with_units(self, variable: str, unit_str: str) -> Dict[str, Any]:
        """Analyze a variable with its associated units"""
        var_info = self.units_db.detect_variable(variable)
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
            "enable_computation": self.enable_computation,
            "units_in_database": self.units_db.get_total_units_count(),
            "variables_in_database": self.units_db.get_total_variables_count(),
            "supported_domains": [d.value for d in SubjectDomain if d not in 
                               [SubjectDomain.HUMANITIES, SubjectDomain.EVERYDAY, SubjectDomain.UNKNOWN]],
            "formulas_in_history": len(self.formula_history),
            "custom_formulas_saved": len(self.custom_formulas)
        }


def print_result(result: ValidationResult, show_details: bool = True):
    """Pretty print validation result"""
    print("\n" + "=" * 70)
    print("PEERX VALIDATION RESULT")
    print("=" * 70)
    
    print(f"\n📝 Original Input: {result.analysis.original_input}")
    print(f"✏️  Formatted Formula: {result.formatted_formula}")
    print(f"🔬 Domain: {result.analysis.domain}")
    print(f"📊 Confidence: {result.analysis.confidence_score:.0%}")
    print(f"🎯 In Scope: {'✓ Yes' if result.analysis.is_in_scope else '✗ No'}")
    print(f"✅ Valid: {'✓ Yes' if result.is_valid else '✗ No'}")
    
    # Show computation result if available
    if result.computation_result is not None:
        print(f"\n🔢 Computation Result: {result.computation_result}")
    
    if show_details:
        if result.analysis.variables_detected:
            print(f"\n📊 Variables Detected:")
            for var, info in result.analysis.variables_detected.items():
                meanings = ', '.join(info.common_meanings[:3])
                print(f"  • {var}: {meanings}")
        
        if result.analysis.units_detected:
            print(f"\n📏 Units Detected:")
            for unit, info in result.analysis.units_detected.items():
                print(f"  • {unit}: {info.category.value}")
        
        if result.step_by_step:
            print(f"\n📝 Step-by-Step Explanation:")
            for i, step in enumerate(result.step_by_step, 1):
                print(f"  {i}. {step}")
        
        if result.real_world_example:
            print(f"\n🌍 Real-World Example:")
            print(f"  {result.real_world_example}")
        
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
                print(f"  {suggestion}")
    
    print("\n" + "=" * 70)


if __name__ == "__main__":
    # Test the final system
    print("PEERX FINAL - Enhanced Peer System with Novice-Friendly Features")
    print("=" * 70)
    
    # Initialize system in Student mode
    system = PeerxFinal(mode=InterfaceMode.STUDENT)
    
    # Display system info
    print("\n📋 System Information:")
    info = system.get_system_info()
    for key, value in info.items():
        print(f"  {key}: {value}")
    
    # Test cases including Sarah's example
    test_inputs = [
        "a + b / [gamma] = z",
        "E = mc^2",
        "F = m * a",
        "(60 - 0) / 10",  # Sarah's acceleration calculation
        "What is the capital of France?",
        "velocity plus acceleration times time",
        "sin(theta) = opposite/hypotenuse",
        "Tell me about the history of Rome",
        "sqrt(x^2 + y^2)",
        "dy/dx = 2x",
        "How do I bake a cake?",
        "KE = 0.5 * m * v^2",  # Kinetic energy
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
    
    # Show example formulas
    print("\n" + "=" * 70)
    print("EXAMPLE FORMULAS")
    print("=" * 70)
    
    examples = system.get_example_formulas()
    for category in examples:
        print(f"\n{category['category']}:")
        for formula in category['formulas']:
            print(f"  • {formula}")
    
    # Show formula history
    print("\n" + "=" * 70)
    print("RECENT FORMULA HISTORY")
    print("=" * 70)
    
    history = system.get_formula_history()
    for item in history:
        print(f"  [{item['timestamp']}] {item['formatted']}")
    
    print("\n" + "=" * 70)
    print("QUICK TIPS")
    print("=" * 70)
    
    for i, tip in enumerate(system.get_quick_tips(), 1):
        print(f"{i}. {tip}")
    
    print("\n" + "=" * 70)
    print("TESTING COMPLETE")
    print("=" * 70)