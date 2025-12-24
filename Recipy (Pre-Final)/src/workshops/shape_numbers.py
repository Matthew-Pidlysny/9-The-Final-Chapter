"""
Shape Numbers Workshop
Workshop 8: Geometry and spatial reasoning
"""

import random

class ShapeNumbersWorkshop:
    def __init__(self, printer, psychology, ai_helper):
        self.printer = printer
        self.psychology = psychology
        self.ai_helper = ai_helper
        self.name = "Shape Numbers"
    
    def get_name(self) -> str:
        return self.name
    
    def run(self) -> bool:
        try:
            self.printer.print_rainbow("\n🔷 SHAPE NUMBERS WORKSHOP! 🔷")
            self.printer.print_blue("Numbers in shapes and spaces!")
            
            self.geometry_fun()
            self.shape_counting()
            self.spatial_games()
            
            self.printer.print_rainbow("🎉 Geometry genius!")
            return True
        except Exception as e:
            self.printer.print_red(f"Oops: {e}")
            return False
    
    def geometry_fun(self):
        self.printer.print_green("\n📐 Geometry Adventures!")
        self.printer.print_cyan("Triangle has 3 sides and 3 corners!")
        self.printer.print_purple("Square has 4 equal sides and 4 corners!")
        self.printer.print_blue("Circle has no corners but is perfectly round!")
        
    def shape_counting(self):
        self.printer.print_yellow("\n🔢 Counting Shapes!")
        self.printer.print_green("How many triangles can you see? Count the corners!")
        self.printer.print_cyan("How many squares? Look for 4 equal sides!")
        
    def spatial_games(self):
        self.printer.print_pink("\n🎮 Spatial Games!")
        self.printer.print_blue("Build with blocks! Count how many you use!")
        self.printer.print_purple("Make patterns with shapes! What comes next?")