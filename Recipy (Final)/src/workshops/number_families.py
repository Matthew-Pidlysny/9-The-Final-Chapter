"""
Number Families Workshop
Workshop 5: Number theory and relationships
"""

import random

class NumberFamiliesWorkshop:
    def __init__(self, printer, psychology, ai_helper):
        self.printer = printer
        self.psychology = psychology
        self.ai_helper = ai_helper
        self.name = "Number Families"
    
    def get_name(self) -> str:
        return self.name
    
    def run(self) -> bool:
        try:
            self.printer.print_rainbow("\n👨‍👩‍👧‍👦 NUMBER FAMILIES WORKSHOP! 👨‍👩‍👧‍👦")
            self.printer.print_blue("Numbers have families too!")
            
            self.addition_families()
            self.multiplication_families()
            self.number_friends()
            
            self.printer.print_rainbow("🎉 Number family expert!")
            return True
        except Exception as e:
            self.printer.print_red(f"Oops: {e}")
            return False
    
    def addition_families(self):
        self.printer.print_green("\n➕ Addition Families!")
        self.printer.print_cyan("2 + 3 = 5, 3 + 2 = 5 (Number family: 2, 3, 5)")
        self.printer.print_purple("4 + 1 = 5, 1 + 4 = 5 (Number family: 1, 4, 5)")
        
    def multiplication_families(self):
        self.printer.print_yellow("\n✖️ Multiplication Families!")
        self.printer.print_blue("2 × 3 = 6, 3 × 2 = 6 (Number family: 2, 3, 6)")
        self.printer.print_green("4 × 2 = 8, 2 × 4 = 8 (Number family: 2, 4, 8)")
        
    def number_friends(self):
        self.printer.print_pink("\n🤝 Number Friends!")
        self.printer.print_cyan("Even numbers: 2, 4, 6, 8, 10 (all have best friend 2)")
        self.printer.print_purple("Odd numbers: 1, 3, 5, 7, 9 (special unique numbers)")