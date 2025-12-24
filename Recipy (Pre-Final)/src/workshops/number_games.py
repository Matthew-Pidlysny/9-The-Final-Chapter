"""
Number Games Workshop
Workshop 9: Learning through engaging games
"""

import random

class NumberGamesWorkshop:
    def __init__(self, printer, psychology, ai_helper):
        self.printer = printer
        self.psychology = psychology
        self.ai_helper = ai_helper
        self.name = "Number Games"
    
    def get_name(self) -> str:
        return self.name
    
    def run(self) -> bool:
        try:
            self.printer.print_rainbow("\n🎮 NUMBER GAMES WORKSHOP! 🎮")
            self.printer.print_blue("Play and learn with numbers!")
            
            self.math_games()
            self.number_puzzles()
            self.quick_challenges()
            
            self.printer.print_rainbow("🎉 Game champion!")
            return True
        except Exception as e:
            self.printer.print_red(f"Oops: {e}")
            return False
    
    def math_games(self):
        self.printer.print_green("\n🎲 Math Dice Games!")
        self.printer.print_cyan("Roll dice and add the numbers!")
        self.printer.print_purple("Roll again and see who gets the higher total!")
        
    def number_puzzles(self):
        self.printer.print_yellow("\n🧩 Number Puzzles!")
        self.printer.print_blue("Fill in the missing number: 2, 4, ?, 8 (6!)")
        self.printer.print_green("What comes next: 10, 20, 30, ? (40!)")
        
    def quick_challenges(self):
        self.printer.print_pink("\n⚡ Quick Math Challenges!")
        self.printer.print_cyan("How fast can you count to 20?")
        self.printer.print_purple("Can you say the 2 times table?")