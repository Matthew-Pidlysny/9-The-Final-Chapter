#!/usr/bin/env python3
"""
'Stuck' Button AI Assistant
Helps users when they can't input their formula properly
Provides ONLY technical formatting help - does NOT solve problems
"""

import re
from typing import Dict, List, Optional
from dataclasses import dataclass


@dataclass
class FormulaSuggestion:
    """Suggestion for formula formatting"""
    original_input: str
    suggested_format: str
    explanation: str
    variables_identified: List[str]
    units_suggested: List[str]


class StuckButtonAssistant:
    """
    AI assistant for users stuck on formula input
    Provides formatting guidance but does NOT solve problems
    """
    
    def __init__(self):
        self.common_patterns = self._init_common_patterns()
        self.operator_mappings = self._init_operator_mappings()
        self.function_mappings = self._init_function_mappings()
    
    def _init_common_patterns(self) -> Dict[str, str]:
        """Common natural language patterns and their mathematical equivalents"""
        return {
            # Basic operations
            r'(\w+)\s*plus\s*(\w+)': r'\1 + \2',
            r'(\w+)\s*minus\s*(\w+)': r'\1 - \2',
            r'(\w+)\s*times\s*(\w+)': r'\1 * \2',
            r'(\w+)\s*divided by\s*(\w+)': r'\1 / \2',
            r'(\w+)\s*multiply by\s*(\w+)': r'\1 * \2',
            r'(\w+)\s*over\s*(\w+)': r'\1 / \2',
            r'(\w+)\s*divided\s+into\s*(\w+)': r'\2 / \1',
            
            # Powers and roots
            r'(\w+)\s*squared': r'\1^2',
            r'(\w+)\s*cubed': r'\1^3',
            r'(\w+)\s*to the power of\s*(\d+)': r'\1^\2',
            r'(\w+)\s*raised to the\s*(\d+)\w* power': r'\1^\2',
            r'square root of\s*(\w+)': r'sqrt(\1)',
            r'cube root of\s*(\w+)': r'\1^(1/3)',
            r'(\w+)\w*\s*root of\s*(\w+)': r'\2^(1/\1)',
            
            # Fractions
            r'(\d+)\s*over\s*(\d+)': r'\1/\2',
            r'(\d+)\s*slash\s*(\d+)': r'\1/\2',
            r'(\d+)\s*divided by\s*(\d+)': r'\1/\2',
            
            # Trigonometric
            r'sine of\s*(\w+)': r'sin(\1)',
            r'cosine of\s*(\w+)': r'cos(\1)',
            r'tangent of\s*(\w+)': r'tan(\1)',
            r'sin of\s*(\w+)': r'sin(\1)',
            r'cos of\s*(\w+)': r'cos(\1)',
            r'tan of\s*(\w+)': r'tan(\1)',
            
            # Logarithms
            r'log of\s*(\w+)': r'log(\1)',
            r'log base\s*(\d+)\s*of\s*(\w+)': r'log_\1(\2)',
            r'natural log of\s*(\w+)': r'ln(\1)',
            r'ln of\s*(\w+)': r'ln(\1)',
            
            # Sums and products
            r'sum of\s*(\w+)\s*from\s*(\d+)\s*to\s*(\d+)': r'∑_{\2}^{\3} \1',
            r'product of\s*(\w+)\s*from\s*(\d+)\s*to\s*(\d+)': r'∏_{\2}^{\3} \1',
            r'integral of\s*(\w+)': r'∫ \1',
            r'derivative of\s*(\w+)': r'd/dx \1',
            r'd(\w+)/d(\w+)': r'd\1/d\2',
            
            # Common physics formulas
            r'force equals mass times acceleration': r'F = m * a',
            r'energy equals mass times speed of light squared': r'E = m * c^2',
            r'kinetic energy': r'KE = 1/2 * m * v^2',
            r'potential energy': r'PE = m * g * h',
            r'momentum equals mass times velocity': r'p = m * v',
            r'work equals force times distance': r'W = F * d',
            r'power equals work over time': r'P = W / t',
            r'voltage equals current times resistance': r'V = I * R',
            r'ohm[\']?s law': r'V = I * R',
            
            # Percentage
            r'(\d+)\s*percent': r'\1%',
            r'(\d+)\s*percent of\s*(\w+)': r'(\1/100) * \2',
        }
    
    def _init_operator_mappings(self) -> Dict[str, str]:
        """Natural language to operator mappings"""
        return {
            'plus': '+',
            'minus': '-',
            'times': '*',
            'multiplied by': '*',
            'divided by': '/',
            'over': '/',
            'equals': '=',
            'is equal to': '=',
            'is': '=',
            'approximately': '≈',
            'less than': '<',
            'greater than': '>',
            'less than or equal to': '≤',
            'greater than or equal to': '≥',
            'not equal to': '≠',
        }
    
    def _init_function_mappings(self) -> Dict[str, str]:
        """Natural language to function mappings"""
        return {
            'square root': 'sqrt',
            'cube root': 'cbrt',
            'absolute value': 'abs',
            'natural logarithm': 'ln',
            'logarithm': 'log',
            'exponential': 'exp',
            'sine': 'sin',
            'cosine': 'cos',
            'tangent': 'tan',
            'cotangent': 'cot',
            'secant': 'sec',
            'cosecant': 'csc',
            'arcsine': 'asin',
            'arccosine': 'acos',
            'arctangent': 'atan',
        }
    
    def help_user(self, user_input: str, max_length: int = 2000) -> FormulaSuggestion:
        """
        Provide help for a user stuck on formula input
        
        Args:
            user_input: The user's description of what they want to enter
            max_length: Maximum length of input to process
            
        Returns:
            FormulaSuggestion with formatted formula and explanation
        """
        # Truncate input if too long
        if len(user_input) > max_length:
            user_input = user_input[:max_length]
        
        # Normalize input
        normalized = user_input.lower().strip()
        
        # Try to match common patterns
        suggested_format = self._apply_patterns(normalized)
        
        # Identify potential variables
        variables = self._identify_variables(normalized)
        
        # Identify potential units
        units = self._identify_units(normalized)
        
        # Generate explanation
        explanation = self._generate_explanation(normalized, suggested_format, variables, units)
        
        return FormulaSuggestion(
            original_input=user_input,
            suggested_format=suggested_format,
            explanation=explanation,
            variables_identified=variables,
            units_suggested=units
        )
    
    def _apply_patterns(self, text: str) -> str:
        """Apply pattern matching to convert natural language to formula"""
        result = text
        
        # Try each pattern in order
        for pattern, replacement in self.common_patterns.items():
            try:
                new_result = re.sub(pattern, replacement, result, flags=re.IGNORECASE)
                if new_result != result:
                    result = new_result
                    break  # Use first successful match
            except:
                continue
        
        # Apply operator mappings
        for phrase, operator in self.operator_mappings.items():
            result = re.sub(r'\b' + phrase + r'\b', operator, result, flags=re.IGNORECASE)
        
        # Apply function mappings
        for phrase, func in self.function_mappings.items():
            result = re.sub(r'\b' + phrase + r'\b', func, result, flags=re.IGNORECASE)
        
        # Clean up extra spaces around operators
        result = re.sub(r'\s*([+\-*/=<>≈≤≥≠])\s*', r' \1 ', result)
        result = re.sub(r'\s+', ' ', result).strip()
        
        return result
    
    def _identify_variables(self, text: str) -> List[str]:
        """Identify potential variables in the input"""
        # Find single letters that might be variables
        variables = list(set(re.findall(r'\b[a-z]\b', text, re.IGNORECASE)))
        
        # Find words that might be variable names
        potential_vars = [
            'velocity', 'speed', 'force', 'mass', 'acceleration',
            'energy', 'power', 'voltage', 'current', 'resistance',
            'time', 'distance', 'height', 'width', 'length',
            'temperature', 'pressure', 'volume', 'density',
            'angle', 'frequency', 'wavelength', 'amplitude'
        ]
        
        for var in potential_vars:
            if var in text.lower():
                variables.append(var[0].upper())  # Add first letter as variable
        
        return sorted(list(set(variables)))
    
    def _identify_units(self, text: str) -> List[str]:
        """Identify potential units in the input"""
        units = []
        
        unit_patterns = {
            'meters': 'm',
            'meter': 'm',
            'metre': 'm',
            'metres': 'm',
            'm': 'm',
            'kilometers': 'km',
            'kilometer': 'km',
            'km': 'km',
            'seconds': 's',
            'second': 's',
            's': 's',
            'hours': 'h',
            'hour': 'h',
            'h': 'h',
            'minutes': 'min',
            'minute': 'min',
            'min': 'min',
            'kilograms': 'kg',
            'kilogram': 'kg',
            'kg': 'kg',
            'grams': 'g',
            'gram': 'g',
            'g': 'g',
            'newtons': 'N',
            'newton': 'N',
            'joules': 'J',
            'joule': 'J',
            'watts': 'W',
            'watt': 'W',
            'volts': 'V',
            'volt': 'V',
            'amperes': 'A',
            'ampere': 'A',
            'amps': 'A',
            'amp': 'A',
            'meters per second': 'm/s',
            'm/s': 'm/s',
            'miles per hour': 'mph',
            'mph': 'mph',
            'kilometers per hour': 'km/h',
            'km/h': 'km/h',
            'meters per second squared': 'm/s²',
            'm/s^2': 'm/s²',
            'degrees': '°',
            'degree': '°',
            'radians': 'rad',
            'radian': 'rad',
            'hertz': 'Hz',
            'hz': 'Hz',
        }
        
        for unit_name, symbol in unit_patterns.items():
            if unit_name in text.lower() or symbol in text:
                if symbol not in units:
                    units.append(symbol)
        
        return units
    
    def _generate_explanation(self, original: str, suggested: str, 
                            variables: List[str], units: List[str]) -> str:
        """Generate explanation for the user"""
        explanation = []
        
        explanation.append("Based on your description, here's a suggested format for your formula:")
        explanation.append(f"\n**Suggested Formula:** `{suggested}`")
        explanation.append("\n**What I did:**")
        
        if original != suggested:
            explanation.append("- Converted natural language to mathematical notation")
            explanation.append("- Applied standard mathematical operators and functions")
        
        if variables:
            explanation.append(f"\n**Variables I identified:** {', '.join(f'`{v}`' for v in variables)}")
        
        if units:
            explanation.append(f"\n**Units I identified:** {', '.join(f'`{u}`' for u in units)}")
        
        explanation.append("\n**Important:**")
        explanation.append("- Review the suggested formula to make sure it matches what you intended")
        explanation.append("- You can copy this formula directly into the input field")
        explanation.append("- If this isn't correct, please provide more details about your formula")
        explanation.append("- This assistant only helps with formatting - it does not solve problems")
        
        return '\n'.join(explanation)
    
    def get_quick_tips(self) -> List[str]:
        """Get quick tips for formula input"""
        return [
            "Use standard mathematical notation: `+`, `-`, `*`, `/` for operations",
            "Use `^` for powers: `x^2` means x squared",
            "Use parentheses to group operations: `(a + b) * c`",
            "Common functions: `sin(x)`, `cos(x)`, `sqrt(x)`, `log(x)`, `exp(x)`",
            "Use `=` for equations: `a + b = c`",
            "Greek letters: `alpha`, `beta`, `gamma`, `delta`, etc.",
            "Derivatives: `dy/dx` or `d/dx f(x)`",
            "Integrals: `∫ f(x) dx`",
            "Sums: `∑_{i=1}^{n} x_i`",
            "Products: `∏_{i=1}^{n} x_i`",
            "Square roots: `sqrt(x)` or `x^(1/2)`",
            "Logarithms: `log(x)` for base 10, `ln(x)` for natural log",
        ]


if __name__ == "__main__":
    # Test the assistant
    assistant = StuckButtonAssistant()
    
    print("Stuck Button Assistant Tests")
    print("=" * 60)
    
    test_inputs = [
        "velocity plus acceleration times time",
        "force equals mass times acceleration",
        "I want to calculate energy which is mass times speed of light squared",
        "square root of x plus y",
        "sine of theta equals opposite over hypotenuse",
        "the sum of i squared from 1 to n",
        "kinetic energy equals half mass velocity squared",
        "a plus b divided by gamma equals z where a is velocity b is vector metric",
    ]
    
    for user_input in test_inputs:
        print(f"\n{'=' * 60}")
        print(f"User Input: {user_input}")
        print(f"{'=' * 60}")
        
        suggestion = assistant.help_user(user_input)
        
        print(f"\n{suggestion.explanation}")