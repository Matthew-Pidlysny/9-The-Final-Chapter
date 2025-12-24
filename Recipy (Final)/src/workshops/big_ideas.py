"""
Big Ideas Workshop
Workshop 10: Real-world connections and future possibilities
"""

import random

class BigIdeasWorkshop:
    def __init__(self, printer, psychology, ai_helper):
        self.printer = printer
        self.psychology = psychology
        self.ai_helper = ai_helper
        self.name = "Big Ideas"
    
    def get_name(self) -> str:
        return self.name
    
    def run(self) -> bool:
        try:
            self.printer.print_rainbow("\n🌍 BIG IDEAS WORKSHOP! 🌍")
            self.printer.print_blue("Math connects to everything!")
            
            self.real_world_math()
            self.future_dreams()
            self.math_heroes()
            
            self.printer.print_rainbow("🎉 Big ideas explorer!")
            return True
        except Exception as e:
            self.printer.print_red(f"Oops: {e}")
            return False
    
    def real_world_math(self):
        self.printer.print_green("\n🏠 Math in Real Life!")
        self.printer.print_cyan("Baking: Measuring ingredients with numbers!")
        self.printer.print_purple("Shopping: Counting money and making change!")
        self.printer.print_blue("Building: Measuring and counting materials!")
        
    def future_dreams(self):
        self.printer.print_yellow("\n🚀 Math and Your Future!")
        self.printer.print_green("Scientists use math to discover new things!")
        self.printer.print_cyan("Engineers use math to build amazing things!")
        self.printer.print_purple("Doctors use math to help people stay healthy!")
        
    def math_heroes(self):
        self.printer.print_pink("\n🦸‍♀️ Math Heroes!")
        self.printer.print_blue("You can be a math hero too!")
        self.printer.print_purple("Every time you learn math, you become stronger!")
        self.printer.print_green("Math gives you superpowers to solve problems!")