"""
AI Helper for Adaptive Learning
Provides personalized learning assistance
"""

import random
import time
from typing import Dict, List, Any

class AIHelper:
    """AI helper for personalized learning experience"""
    
    def __init__(self):
        self.user_preferences = {
            "learning_style": "visual",  # visual, auditory, kinesthetic
            "difficulty_preference": "gradual",
            "encouragement_level": "high",
            "pace": "moderate"
        }
        
        self.learning_progress = {
            "concepts_mastered": [],
            "struggling_areas": [],
            "strength_areas": [],
            "questions_asked": 0,
            "hints_needed": 0
        }
        
        self.personalized_encouragement = {
            "visual_learner": [
                "Can you picture that in your mind? Your imagination is powerful!",
                "Let's draw this concept! Your mind creates beautiful patterns!",
                "I bet you can see the pattern now! Your eyes are amazing!"
            ],
            "auditory_learner": [
                "Let's say this out loud together! Your voice is powerful!",
                "Does that sound right to you? Your ears are brilliant!",
                "Let's count rhythmically! Math has its own music!"
            ],
            "kinesthetic_learner": [
                "Let's use our hands to understand this! Your fingers are smart!",
                "Can you feel the pattern? Your body understands too!",
                "Let's move with the numbers! Your whole body can learn!"
            ]
        }
    
    def assess_learning_style(self) -> str:
        """Assess user's preferred learning style"""
        print("\n🎯 Let's discover how you learn best!")
        print("Everyone learns differently, and that's wonderful!")
        print("\nChoose your favorite way to learn:")
        print("1. 🎨 Looking at pictures and colors (Visual)")
        print("2. 🎵 Hearing explanations and sounds (Auditory)")
        print("3. 🤸 Moving and touching things (Kinesthetic)")
        
        while True:
            choice = input("\nWhich feels most like you? (1/2/3): ").strip()
            if choice == '1':
                self.user_preferences["learning_style"] = "visual"
                return "visual"
            elif choice == '2':
                self.user_preferences["learning_style"] = "auditory"
                return "auditory"
            elif choice == '3':
                self.user_preferences["learning_style"] = "kinesthetic"
                return "kinesthetic"
            else:
                print("Let's try again! Type 1, 2, or 3.")
    
    def provide_personalized_hint(self, concept: str, difficulty_level: int) -> str:
        """Provide personalized hint based on learning style"""
        learning_style = self.user_preferences["learning_style"]
        
        hints = {
            "visual": [
                f"Imagine {concept} as a beautiful picture in your mind!",
                f"Look for patterns in {concept} - they're like hidden treasures!",
                f"Can you see how {concept} fits together like puzzle pieces?"
            ],
            "auditory": [
                f"Let's say {concept} out loud and listen to how it sounds!",
                f"Does {concept} have a rhythm? Count it out loud!",
                f"Listen carefully to the pattern in {concept}!"
            ],
            "kinesthetic": [
                f"Let's use our fingers to count {concept}!",
                f"Can you feel the shape of {concept} with your hands?",
                f"Let's move with the idea of {concept}!"
            ]
        }
        
        hint_list = hints.get(learning_style, hints["visual"])
        base_hint = random.choice(hint_list)
        
        # Adjust based on difficulty
        if difficulty_level <= 2:
            return f"{base_hint} Here's a little help: "
        elif difficulty_level <= 4:
            return f"{base_hint} Think about: "
        else:
            return f"{base_hint} Advanced tip: "
    
    def adapt_pace(self, performance: str):
        """Adapt learning pace based on performance"""
        if performance == "excelling":
            if self.user_preferences["pace"] != "fast":
                self.user_preferences["pace"] = "fast"
                return "🚀 You're doing so well! Let's speed up a bit!"
        elif performance == "struggling":
            if self.user_preferences["pace"] != "slow":
                self.user_preferences["pace"] = "slow"
                return "🐢 No rush at all! Let's take our time and enjoy learning!"
        else:
            if self.user_preferences["pace"] != "moderate":
                self.user_preferences["pace"] = "moderate"
                return "⚖️ Perfect pace! Let's keep this rhythm!"
    
    def suggest_activity_variant(self, base_activity: str) -> str:
        """Suggest activity variant based on learning style"""
        style = self.user_preferences["learning_style"]
        
        variants = {
            "visual": f"Let's make {base_activity} colorful and visual!",
            "auditory": f"Let's explore {base_activity} with sounds and rhythm!",
            "kinesthetic": f"Let's experience {base_activity} with movement and touch!"
        }
        
        return variants.get(style, variants["visual"])
    
    def track_progress(self, concept: str, mastery_level: float):
        """Track learning progress"""
        if mastery_level >= 0.8:
            if concept not in self.learning_progress["concepts_mastered"]:
                self.learning_progress["concepts_mastered"].append(concept)
                if concept in self.learning_progress["struggling_areas"]:
                    self.learning_progress["struggling_areas"].remove(concept)
        elif mastery_level <= 0.4:
            if concept not in self.learning_progress["struggling_areas"]:
                self.learning_progress["struggling_areas"].append(concept)
        elif mastery_level >= 0.6:
            if concept not in self.learning_progress["strength_areas"]:
                self.learning_progress["strength_areas"].append(concept)
    
    def provide_encouragement(self) -> str:
        """Provide personalized encouragement"""
        learning_style = self.user_preferences["learning_style"]
        encouragement_list = self.personalized_encouragement.get(
            learning_style, 
            self.personalized_encouragement["visual"]
        )
        return random.choice(encouragement_list)
    
    def suggest_review_concepts(self) -> List[str]:
        """Suggest concepts that need review"""
        return self.learning_progress["struggling_areas"].copy()
    
    def celebrate_milestone(self, milestone: str):
        """Celebrate learning milestone"""
        celebrations = [
            f"🎉 MILESTONE REACHED: {milestone}!",
            f"⭐ ACHIEVEMENT UNLOCKED: {milestone}!",
            f"🏆 VICTORY: You've mastered {milestone}!",
            f"🌟 BREAKTHROUGH: {milestone} is now yours!"
        ]
        
        print(f"\n{random.choice(celebrations)}")
        print("Your dedication is paying off! This is HUGE! 🎊")
    
    def generate_personalized_challenge(self, concept: str) -> Dict[str, Any]:
        """Generate personalized challenge based on progress"""
        if concept in self.learning_progress["strength_areas"]:
            return {
                "type": "advanced",
                "description": f"Since you're amazing at {concept}, let's try something extra challenging!",
                "difficulty_boost": 2
            }
        elif concept in self.learning_progress["struggling_areas"]:
            return {
                "type": "reinforcement",
                "description": f"Let's practice {concept} together until it feels easy!",
                "difficulty_reduction": 1
            }
        else:
            return {
                "type": "standard",
                "description": f"Perfect time to explore {concept}!",
                "difficulty": "moderate"
            }
    
    def answer_question(self, question: str) -> str:
        """Simulate AI answering a question"""
        self.learning_progress["questions_asked"] += 1
        
        # Simple keyword-based responses
        question_lower = question.lower()
        
        if "why" in question_lower:
            return "That's a wonderful 'why' question! The reason is that numbers follow beautiful patterns that help us understand the world."
        elif "how" in question_lower:
            return "Great 'how' question! We can figure this out step by step together. Let's start with the first piece..."
        elif "what" in question_lower:
            return "Excellent 'what' question! This is all about understanding the amazing world of numbers and their relationships."
        else:
            return "That's a brilliant question! Every question helps us understand math better. Let's explore this together!"
    
    def get_learning_summary(self) -> Dict[str, Any]:
        """Get summary of learning progress"""
        return {
            "concepts_mastered": len(self.learning_progress["concepts_mastered"]),
            "strength_areas": len(self.learning_progress["strength_areas"]),
            "areas_to_work_on": self.learning_progress["struggling_areas"],
            "questions_asked": self.learning_progress["questions_asked"],
            "learning_style": self.user_preferences["learning_style"],
            "current_pace": self.user_preferences["pace"]
        }