"""
Hello Numbers Workshop
Workshop 1: Number recognition and confidence building
"""

import random
import time
from typing import Dict, List

class HelloNumbersWorkshop:
    """First workshop: Making friends with numbers"""
    
    def __init__(self, printer, psychology, ai_helper):
        self.printer = printer
        self.psychology = psychology
        self.ai_helper = ai_helper
        self.name = "Hello Numbers"
        self.activities = [
            self.number_friends_introduction,
            self.counting_adventure,
            self.number_recognition_game,
            self.number_stories,
            self.number_dance,
            self.number_hunt,
            self.number_songs,
            self.number_art
        ]
    
    def get_name(self) -> str:
        """Get workshop name"""
        return self.name
    
    def run(self) -> bool:
        """Run the workshop"""
        try:
            self.printer.print_rainbow("\n" + "=" * 60)
            self.printer.print_rainbow("🌟 HELLO NUMBERS WORKSHOP - Making Number Friends! 🌟")
            self.printer.print_rainbow("=" * 60)
            
            self.printer.print_blue("\nWelcome to the magical world of numbers!")
            self.printer.print_green("Today, we're going to make friends with numbers 1-10!")
            self.printer.print_purple("Each number has its own personality and story!")
            
            # Introduction to number friends
            self.number_friends_introduction()
            
            # Run main activities
            for i, activity in enumerate(self.activities[1:], 1):  # Skip introduction
                self.printer.print_yellow(f"\n🎯 Activity {i}: {activity.__name__.replace('_', ' ').title()}")
                
                if self.psychology.should_take_break():
                    self.psychology.suggest_break()
                
                activity()
                
                # Celebration
                if i % 2 == 0:
                    self.psychology.celebrate_success()
            
            self.printer.print_rainbow("\n🎉 AMAZING WORK! You've made so many number friends!")
            self.printer.print_green("Numbers are now your best friends forever!")
            self.printer.print_purple("You're absolutely brilliant! ⭐")
            
            return True
            
        except Exception as e:
            self.printer.print_red(f"Oh no! Something went wrong: {e}")
            self.printer.print_blue("But that's okay! Learning is all about trying!")
            return False
    
    def number_friends_introduction(self):
        """Introduce number characters"""
        self.printer.print_blue("\n📚 Meet Your Number Friends!")
        
        number_friends = {
            1: "One is brave and stands tall all alone!",
            2: "Two loves to pair up and dance with a friend!",
            3: "Three makes perfect triangles and loves counting!",
            4: "Four is steady like a square and loves order!",
            5: "Five loves high-fives and being in the middle!",
            6: "Six loves making hexagons and being even!",
            7: "Seven is lucky and loves rainbows!",
            8: "Eight looks like infinity and loves circles!",
            9: "Nine is the biggest single digit and loves helping!",
            10: "Ten is perfect and complete!"
        }
        
        for number, description in number_friends.items():
            self.printer.print_cyan(f"  {number}: {description}")
            time.sleep(0.5)
    
    def counting_adventure(self):
        """Interactive counting activity"""
        self.printer.print_green("\n🎪 Let's Count Together Adventure!")
        
        objects = ["stars", "flowers", "apples", "butterflies", "raindrops"]
        chosen_object = random.choice(objects)
        
        self.printer.print_blue(f"Today we're counting {chosen_object}! ✨")
        
        for i in range(1, 11):
            emoji = "⭐" * i
            self.printer.print_yellow(f"{i}: {emoji} {chosen_object}")
            time.sleep(0.3)
        
        self.printer.print_green(f"WOW! We counted all the way to 10 {chosen_object}!")
        
        # Check understanding
        self.psychology.check_understanding("counting to 10")
    
    def number_recognition_game(self):
        """Number recognition game"""
        self.printer.print_purple("\n🎮 Number Recognition Game!")
        self.printer.print_blue("I'll show you a number, you tell me what it is!")
        
        correct_answers = 0
        for round_num in range(5):
            number = random.randint(1, 10)
            self.printer.print_yellow(f"\nRound {round_num + 1}:")
            self.printer.print_cyan(f"What number is this? {number}")
            
            try:
                answer = int(input("Your answer: "))
                if answer == number:
                    self.printer.print_green("🎉 PERFECT! You're amazing!")
                    correct_answers += 1
                else:
                    self.printer.print_blue(f"Nice try! The number was {number}. You'll get it next time!")
            except ValueError:
                self.printer.print_purple("No worries! Let's try another one!")
        
        if correct_answers >= 3:
            self.printer.print_rainbow(f"\n🏆 SPECTACULAR! You got {correct_answers} out of 5!")
        else:
            self.printer.print_green(f"\n💪 GREAT JOB! You got {correct_answers} out of 5! Practice makes perfect!")
    
    def number_stories(self):
        """Create stories with numbers"""
        self.printer.print_nature("\n📖 Number Stories Time!")
        
        story_templates = [
            "Once upon a time, {} little rabbits found {} carrots. They shared them equally and each got {} carrots!",
            "In a garden, {} flowers bloomed. {} more flowers bloomed the next day. Now there are {} beautiful flowers!",
            "{} birds were singing. {} more birds joined them. Together they made {} beautiful sounds!"
        ]
        
        for i, template in enumerate(random.sample(story_templates, 2)):
            self.printer.print_blue(f"\nStory {i + 1}:")
            
            if i == 0:
                numbers = [3, 6, 2]  # 3 rabbits, 6 carrots, 2 each
            elif i == 1:
                numbers = [4, 5, 9]  # 4 flowers, 5 more, 9 total
            else:
                numbers = [2, 7, 9]  # 2 birds, 7 more, 9 total
            
            story = template.format(*numbers)
            self.printer.print_green(story)
            time.sleep(1)
    
    def number_dance(self):
        """Dance and count activity"""
        self.printer.print_yellow("\n💃 Number Dance Party!")
        self.printer.print_blue("Let's dance while we count! Stand up if you can!")
        
        dance_moves = [
            "Jump {} times like a happy frog!",
            "Clap {} hands like a seal!",
            "Spin around {} times!",
            "Stomp {} feet like an elephant!",
            "Wave {} arms like a tree in the wind!"
        ]
        
        for i in range(3):
            move = random.choice(dance_moves).format(i + 3)
            self.printer.print_purple(f"🎵 {move}")
            time.sleep(2)
        
        self.printer.print_green("🎉 Wonderful dancing! Your body loves numbers too!")
    
    def number_hunt(self):
        """Find numbers in the environment"""
        self.printer.print_cyan("\n🔍 Number Hunt Adventure!")
        self.printer.print_blue("Let's find numbers around us!")
        
        hunt_items = [
            "How many fingers on one hand?",
            "How many eyes do you have?",
            "How many legs does a chair have?",
            "How many wheels on a car?",
            "How many days in a week?"
        ]
        
        for item in random.sample(hunt_items, 3):
            self.printer.print_yellow(f"🤔 {item}")
            self.printer.print_blue("Take a moment to think...")
            time.sleep(2)
            
            # Provide answers
            answers = [5, 2, 4, 4, 7]
            if item == hunt_items[0]:
                self.printer.print_green(f"Answer: {answers[0]} fingers!")
            elif item == hunt_items[1]:
                self.printer.print_green(f"Answer: {answers[1]} eyes!")
            elif item == hunt_items[2]:
                self.printer.print_green(f"Answer: {answers[2]} legs!")
            elif item == hunt_items[3]:
                self.printer.print_green(f"Answer: {answers[3]} wheels!")
            else:
                self.printer.print_green(f"Answer: {answers[4]} days!")
    
    def number_songs(self):
        """Sing counting songs"""
        self.printer.print_pink("\n🎤 Number Songs!")
        self.printer.print_blue("Let's sing together!")
        
        songs = [
            "One, two, buckle my shoe!\nThree, four, knock at the door!\nFive, six, pick up sticks!\nSeven, eight, lay them straight!\nNine, ten, a big fat hen!",
            "One little, two little, three little numbers\nFour little, five little, six little numbers\nSeven little, eight little, nine little numbers\nTen little numbers in a row!"
        ]
        
        for song in songs:
            self.printer.print_green(f"\n🎵 {song}")
            self.printer.print_blue("La la la! Wasn't that fun?")
            time.sleep(1)
    
    def number_art(self):
        """Create art with numbers"""
        self.printer.print_rainbow("\n🎨 Number Art Gallery!")
        self.printer.print_blue("Let's make art using numbers!")
        
        art_examples = [
            "111111111111111111111111\n1                   1\n1     HELLO         1\n1     NUMBERS       1\n1                   1\n111111111111111111111111",
            "888      888      888\n888      888      888\n888888888888888888888\n888      888      888\n888      888      888",
            "333333333\n333    333\n333    333\n333    333\n333333333"
        ]
        
        for art in art_examples:
            self.printer.print_cyan(f"\n{art}")
            self.printer.print_purple("Isn't that beautiful? Numbers can make art!")
            time.sleep(1)