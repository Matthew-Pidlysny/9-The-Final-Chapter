"""
Sharing Numbers Workshop
Workshop 2: Fractions and reciprocal concepts through sharing
"""

import random
import time
from typing import Dict, List

class SharingNumbersWorkshop:
    """Second workshop: Learning fractions and sharing concepts"""
    
    def __init__(self, printer, psychology, ai_helper):
        self.printer = printer
        self.psychology = psychology
        self.ai_helper = ai_helper
        self.name = "Sharing Numbers"
        self.activities = [
            self.sharing_stories,
            self.fraction_fun,
            self.reciprocal_introduction,
            self.sharing_games,
            self.pizza_math,
            self.candy_sharing,
            self.toy_sharing,
            self.fraction_art
        ]
    
    def get_name(self) -> str:
        """Get workshop name"""
        return self.name
    
    def run(self) -> bool:
        """Run the workshop"""
        try:
            self.printer.print_rainbow("\n" + "=" * 60)
            self.printer.print_rainbow("🍕 SHARING NUMBERS WORKSHOP - Fractions & Friendship! 🍕")
            self.printer.print_rainbow("=" * 60)
            
            self.printer.print_blue("\nWelcome to the wonderful world of sharing!")
            self.printer.print_green("Today we'll learn how numbers help us share fairly!")
            self.printer.print_purple("Sharing makes everyone happy, and numbers help us do it right!")
            
            # Introduction to sharing
            self.sharing_introduction()
            
            # Run activities
            for i, activity in enumerate(self.activities):
                self.printer.print_yellow(f"\n🎯 Activity {i + 1}: {activity.__name__.replace('_', ' ').title()}")
                
                if self.psychology.should_take_break():
                    self.psychology.suggest_break()
                
                activity()
                
                # Celebration every 2 activities
                if (i + 1) % 2 == 0:
                    self.psychology.celebrate_success()
            
            self.printer.print_rainbow("\n🎉 FANTASTIC! You're a sharing superstar!")
            self.printer.print_green("You've learned that fractions make sharing fair and fun!")
            self.printer.print_purple("You're becoming a mathematical genius! ⭐")
            
            return True
            
        except Exception as e:
            self.printer.print_red(f"Oh no! Something went wrong: {e}")
            self.printer.print_blue("But that's okay! Learning is all about trying!")
            return False
    
    def sharing_introduction(self):
        """Introduce the concept of sharing"""
        self.printer.print_blue("\n💝 Why Sharing is Amazing!")
        
        sharing_points = [
            "Sharing makes everyone feel happy and included!",
            "Fractions help us share things equally!",
            "When we share, everyone gets a fair amount!",
            "Numbers help us be kind and fair friends!",
            "Sharing is how we show we care about each other!"
        ]
        
        for point in sharing_points:
            self.printer.print_green(f"  💖 {point}")
            time.sleep(0.5)
    
    def sharing_stories(self):
        """Stories about sharing"""
        self.printer.print_nature("\n📖 Sharing Stories!")
        
        stories = [
            "Lily had 6 cookies and wanted to share with 2 friends. She gave each friend 3 cookies. Everyone got the same amount! 🍪",
            "Tom had 8 stickers and shared them with 4 classmates. Each person got 2 stickers. Everyone was happy! ⭐",
            "Maya had 10 crayons and shared them with 5 friends. Each friend got 2 crayons. Now everyone can color! 🎨",
            "Sam had 4 apples and shared them with his family of 4. Each person got 1 apple. Yummy! 🍎"
        ]
        
        for story in stories:
            self.printer.print_purple(story)
            time.sleep(1)
        
        self.printer.print_blue("\nSee how numbers help us share fairly?")
    
    def fraction_fun(self):
        """Introduction to fractions"""
        self.printer.print_yellow("\n🍰 Meet the Fraction Family!")
        
        self.printer.print_cyan("A fraction is like a piece of a whole thing!")
        self.printer.print_green("1/2 means 1 piece out of 2 equal pieces!")
        self.printer.print_blue("1/4 means 1 piece out of 4 equal pieces!")
        
        # Visual fraction examples
        fractions = [
            ("1/2", "Half of pizza", "🍕"),
            ("1/4", "Quarter of cake", "🎂"),
            ("1/3", "Third of chocolate", "🍫"),
            ("1/8", "Eighth of pie", "🥧")
        ]
        
        for fraction, description, emoji in fractions:
            self.printer.print_magenta(f"\n{fraction} = {description} {emoji}")
            time.sleep(0.5)
    
    def reciprocal_introduction(self):
        """Introduction to reciprocals in child-friendly way"""
        self.printer.print_pink("\n🤝 Reciprocal Numbers - Number Twins!")
        
        self.printer.print_blue("Reciprocal numbers are special number twins!")
        self.printer.print_green("When you multiply them together, you get 1!")
        
        examples = [
            ("2 and 1/2", "2 × 1/2 = 1"),
            ("3 and 1/3", "3 × 1/3 = 1"),
            ("4 and 1/4", "4 × 1/4 = 1"),
            ("5 and 1/5", "5 × 1/5 = 1")
        ]
        
        for pair, equation in examples:
            self.printer.print_purple(f"Twin numbers: {pair}")
            self.printer.print_cyan(f"  {equation}")
            self.printer.print_green("  They work together to make 1! 🎯")
            time.sleep(0.8)
    
    def sharing_games(self):
        """Interactive sharing games"""
        self.printer.print_rainbow("\n🎮 Sharing Games!")
        
        games = [
            {
                "total": 12,
                "people": 3,
                "item": "candies"
            },
            {
                "total": 15,
                "people": 5,
                "item": "stickers"
            },
            {
                "total": 20,
                "people": 4,
                "item": "toys"
            }
        ]
        
        for i, game in enumerate(games):
            self.printer.print_yellow(f"\nGame {i + 1}:")
            self.printer.print_blue(f"We have {game['total']} {game['item']} to share with {game['people']} people.")
            
            answer = game['total'] // game['people']
            
            self.printer.print_thinking("How many does each person get?")
            time.sleep(2)
            
            self.printer.print_green(f"🎉 Each person gets {answer} {game['item']}!")
            self.printer.print_purple(f"Check: {answer} × {game['people']} = {answer * game['people']} {game['item']}!")
            
            time.sleep(1)
    
    def pizza_math(self):
        """Pizza fraction activity"""
        self.printer.print_green("\n🍕 Pizza Party Math!")
        
        self.printer.print_blue("Imagine we have delicious pizzas to share!")
        
        pizza_scenarios = [
            ("1 pizza", "2 people", "1/2 pizza each"),
            ("1 pizza", "4 people", "1/4 pizza each"),
            ("2 pizzas", "4 people", "1/2 pizza each"),
            ("3 pizzas", "6 people", "1/2 pizza each")
        ]
        
        for pizzas, people, result in pizza_scenarios:
            self.printer.print_cyan(f"\n{pizzas} shared among {people}:")
            self.printer.print_green(f"  Each person gets {result} 🍕")
            time.sleep(1)
        
        self.printer.print_purple("\nFractions help us share pizza fairly!")
        self.printer.print_yellow("Everyone gets the right amount! 🎉")
    
    def candy_sharing(self):
        """Candy sharing activity"""
        self.printer.print_pink("\n🍬 Candy Sharing Adventure!")
        
        candy_types = ["gummy bears", "chocolates", "lollipops", "candy canes"]
        chosen_candy = random.choice(candy_types)
        
        total_candies = random.randint(8, 20)
        friends = random.randint(2, 5)
        
        self.printer.print_blue(f"We found {total_candies} {chosen_candy}!")
        self.printer.print_green(f"We want to share them with {friends} friends!")
        
        if total_candies % friends == 0:
            each_gets = total_candies // friends
            self.printer.print_rainbow(f"🎉 Perfect! Each friend gets {each_gets} {chosen_candy}!")
        else:
            each_gets = total_candies // friends
            remaining = total_candies % friends
            self.printer.print_yellow(f"Each friend gets {each_gets} {chosen_candy}")
            self.printer.print_cyan(f"There are {remaining} left over for sharing!")
        
        time.sleep(1)
    
    def toy_sharing(self):
        """Toy sharing activity"""
        self.printer.print_cyan("\n🧸 Toy Sharing Time!")
        
        toy_sharing_problems = [
            ("8 toy cars", "4 children", "2 cars each"),
            ("12 building blocks", "3 friends", "4 blocks each"),
            ("10 dolls", "5 kids", "2 dolls each"),
            ("16 puzzle pieces", "4 players", "4 pieces each")
        ]
        
        for toys, children, result in toy_sharing_problems:
            self.printer.print_blue(f"\n{toys} to share with {children}:")
            time.sleep(1)
            self.printer.print_green(f"  🎯 {result}")
            self.printer.print_purple("  Everyone gets the same amount! Fair sharing!")
    
    def fraction_art(self):
"""Create art with fractions"""
        self.printer.print_rainbow("\n🎨 Fraction Art Gallery!")
        
        self.printer.print_blue("Let's make art using fractions!")
        
        art_examples = [
            "1/2 🎨 + 1/2 🎨 = 1 whole beautiful painting!",
            "1/4 🌈 + 1/4 🌈 + 1/4 🌈 + 1/4 🌈 = 1 complete rainbow!",
            "1/3 ⭐ + 1/3 ⭐ + 1/3 ⭐ = 3 whole stars!",
            "1/2 ❤️ + 1/2 💛 = 1 heart full of love!"
        ]
        
        for art in art_examples:
            self.printer.print_magenta(f"\n{art}")
            time.sleep(0.8)
        
        self.printer.print_green("\nFractions help us create beautiful, balanced art!")
        self.printer.print_purple("Math and art are best friends! 🎨✨")