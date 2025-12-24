"""
Recipy Main Application
Python Implementation of Revolutionary Educational Framework
"""

import os
import sys
import time
import random
from typing import Dict, List, Optional
from pathlib import Path

from utils.colorful_printer import ColorfulPrinter
from utils.child_psychology import ChildPsychologyManager
from utils.ai_helper import AIHelper
from workshops.hello_numbers import HelloNumbersWorkshop
from workshops.sharing_numbers import SharingNumbersWorkshop
from workshops.long_number_adventures import LongNumberAdventuresWorkshop
from workshops.pattern_finding import PatternFindingWorkshop
from workshops.number_families import NumberFamiliesWorkshop
from workshops.information_magic import InformationMagicWorkshop
from workshops.number_secrets import NumberSecretsWorkshop
from workshops.shape_numbers import ShapeNumbersWorkshop
from workshops.number_games import NumberGamesWorkshop
from workshops.big_ideas import BigIdeasWorkshop

class RecipyApp:
    """Main application class for Recipy educational framework"""
    
    def __init__(self):
        self.printer = ColorfulPrinter()
        self.psychology = ChildPsychologyManager()
        self.ai_helper = AIHelper()
        self.current_workshop = None
        self.achievements = []
        self.session_start_time = time.time()
        
        # Initialize all workshops
        self.workshops = {
            1: HelloNumbersWorkshop(self.printer, self.psychology, self.ai_helper),
            2: SharingNumbersWorkshop(self.printer, self.psychology, self.ai_helper),
            3: LongNumberAdventuresWorkshop(self.printer, self.psychology, self.ai_helper),
            4: PatternFindingWorkshop(self.printer, self.psychology, self.ai_helper),
            5: NumberFamiliesWorkshop(self.printer, self.psychology, self.ai_helper),
            6: InformationMagicWorkshop(self.printer, self.psychology, self.ai_helper),
            7: NumberSecretsWorkshop(self.printer, self.psychology, self.ai_helper),
            8: ShapeNumbersWorkshop(self.printer, self.psychology, self.ai_helper),
            9: NumberGamesWorkshop(self.printer, self.psychology, self.ai_helper),
            10: BigIdeasWorkshop(self.printer, self.psychology, self.ai_helper)
        }
    
    def display_welcome(self):
        """Display beautiful welcome screen"""
        self.printer.print_rainbow("""
        ╔══════════════════════════════════════════════════════════════╗
        ║                                                              ║
        ║           🌟 WELCOME TO RECIpy MATH ADVENTURES! 🌟           ║
        ║                                                              ║
        ║            Where Every Number is Your Best Friend!           ║
        ║                                                              ║
        ╚══════════════════════════════════════════════════════════════╝
        """)
        
        self.printer.print_green("\nHello, amazing mathematician!")
        self.printer.print_blue("I'm so excited to explore numbers with you!")
        self.printer.print_purple("Are you ready for an incredible adventure?")
        
        # Check attention span
        if self.psychology.should_take_break():
            self.psychology.suggest_break()
    
    def display_menu(self):
        """Display workshop selection menu"""
        self.printer.print_yellow("\n" + "=" * 50)
        self.printer.print_rainbow("Choose Your Math Adventure!")
        self.printer.print_yellow("=" * 50)
        
        workshop_info = {
            1: "Hello Numbers - Make friends with numbers!",
            2: "Sharing Numbers - Learn about fractions and sharing!",
            3: "Long Number Adventures - Explore big, beautiful numbers!",
            4: "Pattern Finding - Discover amazing patterns!",
            5: "Number Families - Meet number families and their stories!",
            6: "Information Magic - The magic of information and patterns!",
            7: "Number Secrets - Unlock mathematical mysteries!",
            8: "Shape Numbers - Numbers in shapes and spaces!",
            9: "Number Games - Play and learn with number games!",
            10: "Big Ideas - Connect math to the real world!"
        }
        
        for num, description in workshop_info.items():
            self.printer.print_cyan(f"  {num}. {description}")
        
        self.printer.print_green("\n11. 🎉 Show my achievements!")
        self.printer.print_blue("12. 💝 Take a mindful break")
        self.printer.print_purple("0. 👋 Say goodbye for now")
        
        self.printer.print_yellow("\nWhich adventure would you like to choose? (0-12)")
    
    def handle_user_choice(self, choice: int) -> bool:
        """Handle user's menu choice"""
        if choice == 0:
            return False
        
        if choice == 11:
            self.show_achievements()
            return True
        
        if choice == 12:
            self.psychology.mindful_break()
            return True
        
        if 1 <= choice <= 10:
            self.run_workshop(choice)
            return True
        
        self.printer.print_red("Oops! That's not a valid choice. Let's try again!")
        return True
    
    def run_workshop(self, workshop_num: int):
        """Run a specific workshop"""
        if workshop_num in self.workshops:
            self.current_workshop = self.workshops[workshop_num]
            self.printer.print_green(f"\n🚀 Starting Workshop {workshop_num}: {self.current_workshop.get_name()}")
            
            # Run workshop
            success = self.current_workshop.run()
            
            if success:
                self.achievements.append(f"Completed {self.current_workshop.get_name()}")
                self.celebrate_completion()
            else:
                self.printer.print_blue("No worries! Learning takes time. You're doing great!")
    
    def celebrate_completion(self):
        """Celebrate workshop completion"""
        celebrations = [
            "🎉 AMAZING WORK! You're a math superstar!",
            "⭐ INCREDIBLE! Your brain is growing stronger!",
            "🌟 WOW! You're unlocking the secrets of the universe!",
            "🏆 FANTASTIC! You're becoming a mathematical wizard!",
            "💫 BRILLIANT! You've discovered something amazing!"
        ]
        
        celebration = random.choice(celebrations)
        self.printer.print_rainbow(f"\n{celebration}")
        
        # Check if attention span management needed
        if self.psychology.should_celebrate():
            self.psychology.celebrate_success()
    
    def show_achievements(self):
        """Display user achievements"""
        self.printer.print_rainbow("\n🏆 Your Amazing Achievements! 🏆")
        
        if not self.achievements:
            self.printer.print_blue("You're just getting started! Every journey begins with a single step!")
        else:
            for i, achievement in enumerate(self.achievements, 1):
                self.printer.print_green(f"  {i}. {achievement}")
        
        session_time = int(time.time() - self.session_start_time)
        minutes = session_time // 60
        seconds = session_time % 60
        
        self.printer.print_purple(f"\nLearning time: {minutes} minutes, {seconds} seconds")
        self.printer.print_yellow("You're doing AMAZING! Keep up the great work!")
    
    def run(self):
        """Main application loop"""
        self.display_welcome()
        
        running = True
        while running:
            try:
                self.display_menu()
                choice_input = input("\n> ")
                
                try:
                    choice = int(choice_input)
                    running = self.handle_user_choice(choice)
                except ValueError:
                    self.printer.print_red("Please enter a number. Let's try again!")
                
            except KeyboardInterrupt:
                self.printer.print_blue("\nTaking a little break... Press Enter to continue!")
                input()
            
            # Attention span management
            if self.psychology.should_take_break():
                self.psychology.suggest_break()
                if input("Would you like to take a break? (y/n): ").lower() == 'y':
                    self.psychology.mindful_break()
        
        self.printer.print_rainbow("\nThank you for learning with Recipy!")
        self.printer.print_green("You're amazing! Come back soon for more math adventures!")