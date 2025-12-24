"""
Information Magic Workshop
Workshop 6: Information theory and Shannon entropy
"""

import random

class InformationMagicWorkshop:
    def __init__(self, printer, psychology, ai_helper):
        self.printer = printer
        self.psychology = psychology
        self.ai_helper = ai_helper
        self.name = "Information Magic"
    
    def get_name(self) -> str:
        return self.name
    
    def run(self) -> bool:
        try:
            self.printer.print_rainbow("\n📡 INFORMATION MAGIC WORKSHOP! 📡")
            self.printer.print_blue("Magic of information and patterns!")
            
            self.information_basics()
            self.pattern_magic()
            self.communication_fun()
            
            self.printer.print_rainbow("🎉 Information wizard!")
            return True
        except Exception as e:
            self.printer.print_red(f"Oops: {e}")
            return False
    
    def information_basics(self):
        self.printer.print_green("\n💡 What is Information?")
        self.printer.print_cyan("Information is like secret messages!")
        self.printer.print_purple("Numbers help us send and understand information!")
        
    def pattern_magic(self):
        self.printer.print_yellow("\n🔮 Pattern Magic!")
        self.printer.print_blue("A-B-A-B pattern tells us what comes next!")
        self.printer.print_green("1-2-1-2 pattern helps us guess!")
        
    def communication_fun(self):
        self.printer.print_pink("\n📢 Communication Fun!")
        self.printer.print_cyan("Math helps us share ideas clearly!")
        self.printer.print_purple("Numbers are a universal language!")