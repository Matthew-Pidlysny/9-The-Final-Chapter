"""
Long Number Adventures Workshop
Workshop 3: 1200-decimal analysis and advanced patterns
"""

import random
import math

class LongNumberAdventuresWorkshop:
    def __init__(self, printer, psychology, ai_helper):
        self.printer = printer
        self.psychology = psychology
        self.ai_helper = ai_helper
        self.name = "Long Number Adventures"
    
    def get_name(self) -> str:
        return self.name
    
    def run(self) -> bool:
        try:
            self.printer.print_rainbow("\n🔢 LONG NUMBER ADVENTURES WORKSHOP! 🔢")
            self.printer.print_blue("Let's explore amazing big numbers!")
            
            # PI exploration
            self.explore_pi()
            self.explore_patterns()
            self.number_magic()
            
            self.printer.print_rainbow("🎉 You've conquered big numbers!")
            return True
        except Exception as e:
            self.printer.print_red(f"Oops: {e}")
            return False
    
    def explore_pi(self):
        self.printer.print_green("\n🥧 Meet Pi - The Magical Circle Number!")
        pi_digits = "3.14159265358979323846264338327950288419716939937510"
        self.printer.print_cyan(f"Pi starts with: {pi_digits[:20]}...")
        self.printer.print_purple("Pi goes on forever without repeating! Amazing!")
        
    def explore_patterns(self):
        self.printer.print_yellow("\n🔍 Pattern Discovery in Big Numbers!")
        patterns = [
            "123456789 - Counting up pattern",
            "987654321 - Counting down pattern", 
            "111111111 - Same number pattern",
            "121212121 - Repeating pattern"
        ]
        for pattern in patterns:
            self.printer.print_blue(f"  {pattern}")
            
    def number_magic(self):
        self.printer.print_pink("\n✨ Number Magic Tricks!")
        self.printer.print_green("2 × 2 = 4, 3 × 3 = 9, 4 × 4 = 16")
        self.printer.print_purple("These are called square numbers - they make perfect squares!")