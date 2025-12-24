"""
Child Psychology Manager
Optimizes learning experience based on child development principles
"""

import time
import random
from typing import List, Dict

class ChildPsychologyManager:
    """Manages child psychology aspects of learning"""
    
    def __init__(self):
        self.session_start_time = time.time()
        self.last_activity_time = time.time()
        self.activities_completed = 0
        self.attention_spans = []
        self.mood_state = "happy"
        self.encouragement_messages = [
            "You're doing amazing! Keep going!",
            "Your brain is growing stronger every second!",
            "I believe in you completely!",
            "You're discovering the secrets of the universe!",
            "Every great mathematician started exactly where you are!",
            "Your curiosity is your superpower!",
            "You're braver than you believe!",
            "Learning is an adventure, and you're the hero!"
        ]
        
        self.break_activities = [
            "Let's take three deep breaths together... in... out... beautiful!",
            "Time for a stretch! Reach for the stars! You can touch them!",
            "Let's wiggle our fingers and toes! Isn't our body amazing?",
            "Close your eyes and think of something that makes you happy...",
            "Let's count our blessings! 1... 2... 3... so many wonderful things!",
            "Time for a happy dance! Music in our hearts, joy in our steps!"
        ]
        
        self.attention_span_threshold = 15 * 60  # 15 minutes
        self.max_activity_time = 10 * 60  # 10 minutes per activity
    
    def should_take_break(self) -> bool:
        """Check if child should take a break"""
        current_time = time.time()
        session_duration = current_time - self.session_start_time
        time_since_last_activity = current_time - self.last_activity_time
        
        # Check total session time
        if session_duration > self.attention_span_threshold:
            return True
        
        # Check time since last activity
        if time_since_last_activity > self.max_activity_time:
            return True
        
        # Check mood state
        if self.mood_state == "tired":
            return True
        
        return False
    
    def suggest_break(self):
        """Suggest taking a break"""
        break_message = random.choice(self.break_activities)
        print(f"\n🌈 {break_message} 🌈")
        print("Taking breaks helps our brains learn even better!")
    
    def mindful_break(self):
        """Guide through a mindful break"""
        print("\n" + "💖" * 20)
        print("   LET'S TAKE A LOVING BREAK TOGETHER   ")
        print("💖" * 20)
        
        print("\n🧘‍♀️ Let's find our calm...")
        print("Close your eyes if you feel comfortable...")
        print("Take a deep breath in... and out... 🌬️")
        print("You are safe. You are loved. You are capable. 💕")
        print("Take one more deep breath... in... and out... ✨")
        print("\nReady to continue our adventure? You've got this!")
        print("💖" * 20)
        
        self.last_activity_time = time.time()
        self.mood_state = "refreshed"
    
    def celebrate_success(self):
        """Celebrate child's success"""
        celebrations = [
            "🎉 YOU DID IT! You're absolutely brilliant!",
            "⭐ SUPERSTAR! Your mind is amazing!",
            "🏆 CHAMPION! You've conquered this challenge!",
            "🌟 GENIUS! You're unlocking the secrets of math!",
            "🎊 HERO! You're brave enough to try and smart enough to succeed!"
        ]
        
        celebration = random.choice(celebrations)
        print(f"\n{celebration}")
        print("Your heart must be so proud! I know I am! 💖")
        
        self.activities_completed += 1
        self.last_activity_time = time.time()
    
    def encourage(self):
        """Provide encouragement"""
        message = random.choice(self.encouragement_messages)
        return message
    
    def adapt_difficulty(self, child_performance: str) -> Dict:
        """Adapt difficulty based on child's performance"""
        if child_performance == "struggling":
            return {
                "simplify": True,
                "more_examples": True,
                "extra_encouragement": True,
                "break_suggestion": True
            }
        elif child_performance == "excelling":
            return {
                "challenge_mode": True,
                "advanced_concepts": True,
                "less_guidance": True,
                "exploration_mode": True
            }
        else:
            return {
                "steady_pace": True,
                "balanced_support": True,
                "gradual_progression": True
            }
    
    def check_understanding(self, concept: str) -> bool:
        """Check if child understands the concept"""
        print(f"\n🤔 Let's make sure we understand {concept}!")
        print("Do you feel like you've got it, or would you like to explore it together?")
        
        while True:
            response = input("Type 'yes' if you understand, or 'explore' to learn more: ").lower()
            if response in ['yes', 'y', 'got it', 'understand']:
                print("🎉 Wonderful! You're doing great!")
                return True
            elif response in ['explore', 'more', 'help', 'no']:
                print("💖 That's perfectly okay! Learning takes time. Let's explore together!")
                return False
            else:
                print("Let's try again! Type 'yes' or 'explore'.")
    
    def track_attention_span(self, activity_duration: float):
        """Track child's attention span"""
        self.attention_spans.append(activity_duration)
        
        # Keep only last 10 attention spans
        if len(self.attention_spans) > 10:
            self.attention_spans.pop(0)
    
    def get_average_attention_span(self) -> float:
        """Get average attention span"""
        if not self.attention_spans:
            return 15.0  # Default 15 minutes
        return sum(self.attention_spans) / len(self.attention_spans)
    
    def update_mood_state(self, new_state: str):
        """Update child's mood state"""
        self.mood_state = new_state
    
    def should_celebrate(self) -> bool:
        """Check if we should celebrate"""
        # Celebrate every 3 activities or after significant achievement
        return self.activities_completed % 3 == 0
    
    def provide_emotional_support(self):
        """Provide emotional support"""
        print("\n" + "🫂" * 15)
        print("   REMEMBER: YOU ARE LOVED AND CAPABLE   ")
        print("🫂" * 15)
        print("\n💖 Every question is brilliant")
        print("💖 Every attempt is courageous")
        print("💖 Every moment is a chance to grow")
        print("💖 You are exactly where you need to be")
        print("💖 I'm here with you every step of the way")
        print("🫂" * 15 + "\n")