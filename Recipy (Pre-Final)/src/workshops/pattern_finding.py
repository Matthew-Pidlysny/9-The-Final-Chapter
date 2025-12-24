"""
Pattern Finding Workshop
Workshop 4: Comprehensive pattern detection and creation
"""

import random

class PatternFindingWorkshop:
    def __init__(self, printer, psychology, ai_helper):
        self.printer = printer
        self.psychology = psychology
        self.ai_helper = ai_helper
        self.name = "Pattern Finding"
    
    def get_name(self) -> str:
        return self.name
    
    def run(self) -> bool:
        try:
            self.printer.print_rainbow("\n🔍 PATTERN FINDING WORKSHOP! 🔍")
            self.printer.print_blue("Let's discover amazing patterns!")
            
            self.number_patterns()
            self.shape_patterns()
            self.sound_patterns()
            
            self.printer.print_rainbow("🎉 Pattern master detected!")
            return True
        except Exception as e:
            self.printer.print_red(f"Oops: {e}")
            return False
    
    def number_patterns(self):
        self.printer.print_green("\n🔢 Number Patterns!")
        patterns = ["2, 4, 6, 8, ? (10!)", "1, 3, 5, 7, ? (9!)", "10, 20, 30, ? (40!)"]
        for pattern in patterns:
            self.printer.print_cyan(f"  {pattern}")
            
    def shape_patterns(self):
        self.printer.print_yellow("\n🔷 Shape Patterns!")
        self.printer.print_blue("Circle, Square, Circle, Square, ? (Circle!)")
        self.printer.print_purple("Triangle, Triangle, Square, Triangle, Triangle, ? (Square!)")
        
    def sound_patterns(self):
        self.printer.print_pink("\n🎵 Sound Patterns!")
        self.printer.print_green("Clap, Stomp, Clap, Stomp, ? (Clap!)")
        self.printer.print_cyan("High, Low, High, Low, ? (High!)")