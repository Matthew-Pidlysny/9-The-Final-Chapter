"""
Flight Attendant System
Generates context-aware commentary during the irrational number journey
"""

import random
import time
import math
from typing import List, Dict, Tuple

class AttendantSystem:
    """Flight attendant commentary system for engaging journey experience"""
    
    def __init__(self):
        self.commentary_history = []
        self.position_markers = []
        self.current_irrational = None
        
        # Commentary templates
        self.general_commentary = [
            "We're now cruising through the mathematical stratosphere...",
            "The view from here is absolutely irrational! 🌟",
            "Ladies and gentlemen, we're experiencing some beautiful numerical turbulence...",
            "Fasten your seatbelts as we explore deeper into the physical boundaries...",
            "The captain has turned on the physical reality discovery light...",
            "We're flying through regions where numbers have physical meaning!",
            "Welcome to the QUANTUM-BOUND zone of mathematical wonder!",
            "The mathematical landscape below has physical limits...",
            "We've now reached the region where reality meets mathematics...",
            "Cruising altitude: Physical mathematics!"
        ]
        
        self.milestone_commentary = {
            10: [
                "🎉 We've reached our first double-digit milestone!",
                "✨ Two digits of physical mathematics explored!",
                "🌟 Welcome to the double-digit club of reality explorers!"
            ],
            15: [
                "⚠️ COGNITIVE TERMINATION REACHED! 15 digits!",
                "🧠 Beyond this, human perception cannot distinguish!",
                "👁️ You've hit the human comprehension boundary!"
            ],
            25: [
                "🎊 A quarter-century of digits discovered!",
                "💫 25 steps into the physical reality journey!",
                "⭐ You've reached 25 digits of mathematical wonder!"
            ],
            35: [
                "🌌 PLANCK SCALE MILESTONE! 35 digits!",
                "🔬 Beyond this, spacetime itself breaks down!",
                "⚛️ You've reached quantum foam territory!"
            ],
            50: [
                "🏆 Half-century milestone achieved!",
                "🎯 50 digits of irrational beauty explored!",
                "🌈 You've journeyed through 50 decimal places of reality!"
            ],
            61: [
                "🌟 QUANTUM UNCERTAINTY LIMIT! 61 digits!",
                "⚠️ PHYSICAL REALITY TERMINATION POINT!",
                "🔭 Beyond this: NO PHYSICAL MEANING EXISTS!",
                "💫 CONGRATULATIONS! You've reached the ABSOLUTE boundary!",
                "🌌 You've discovered where 'infinity' ends!"
            ],
            100: [
                "📊 THEORETICAL CENTURY (beyond physical meaning)!",
                "💯 Exploring mathematical concepts beyond reality...",
                "🌟 100 digits of abstract mathematics!"
            ]
        }
        
        self.pattern_commentary = {
            'pi': [
                "Ah, the beauty of π! The most famous TERMINABLE number!",
                "π appears everywhere - from circles to probability theory!",
                "REVOLUTIONARY: π terminates at 61 digits (quantum limit)!",
                "We're following in the footsteps of Archimedes himself!",
                "π day is March 14th (3/14) - celebrate the TERMINATION!"
            ],
            'e': [
                "The number e! Euler's constant, the base of natural logarithms!",
                "e appears in compound interest, population growth, and more!",
                "BREAKTHROUGH: e terminates at quantum uncertainty limit!",
                "Leonhard Euler would be amazed by physical termination!",
                "This is the number that makes calculus POSSIBLE and TERMINABLE!"
            ],
            'phi': [
                "The Golden Ratio! Found in art, nature, and architecture!",
                "φ = (1 + √5) / 2 - the most beautiful TERMINABLE number!",
                "DISCOVERY: φ terminates at physical boundaries!",
                "Leonardo da Vinci would love this termination finding!",
                "This is the divine proportion with REAL physical limits!"
            ],
            'sqrt2': [
                "√2! The diagonal of a unit square, the first TERMINABLE irrational!",
                "The Pythagoreans were shocked when they discovered this number!",
                "REVOLUTION: Even √2 has physical termination!",
                "√2 appears in paper sizes, construction, and more!",
                "The first step into the BOUNDED world of irrational numbers!"
            ],
            'sqrt3': [
                "√3! The height of an equilateral triangle with side length 2!",
                "This number appears in trigonometry and geometry!",
                "BREAKTHROUGH: √3 terminates at Planck scale!",
                "From 60-degree angles to hexagonal patterns with LIMITS!",
                "Another beautiful irrational with PHYSICAL boundaries!"
            ]
        }
        
        self.special_patterns = {
            'repeating_digits': [
                "✨ Look! We have repeating digits - a momentary pattern in infinity!",
                "🎯 Repetition alert! Even in irrational numbers, beauty repeats!",
                "🌟 Temporary pattern detected! Mathematical poetry in motion!"
            ],
            'ascending_sequence': [
                "📈 Ascending digits detected! The number is climbing!",
                "🚀 Upward sequence! Mathematical ascent in progress!",
                "⬆️ Rising pattern! Even infinity has its ups and downs!"
            ],
            'descending_sequence': [
                "📉 Descending digits! The number is cascading down!",
                "🏔️ Downward slope! Mathematical valley exploration!",
                "⬇️ Falling sequence! Gravity in the numerical world!"
            ],
            'palindrome': [
                "🔄 Palindromic pattern! Reads the same forwards and backwards!",
                "🪞 Mirror digits! Mathematical reflection symmetry!",
                "⚖️ Balanced beauty! Perfect numerical harmony!"
            ]
        }
    
    def initialize(self):
        """Initialize the attendant system"""
        self.commentary_history = []
        self.position_markers = []
        
    def generate_commentary(self, position: int, digits: str, irrational_type: str) -> str:
        """Generate contextual commentary for current position"""
        
        # Check for milestones
        milestone_commentary = self._check_milestones(position)
        if milestone_commentary:
            return milestone_commentary
        
        # Check for patterns
        pattern_commentary = self._detect_patterns(position, digits)
        if pattern_commentary:
            return pattern_commentary
        
        # General position-based commentary
        general_comment = self._generate_position_commentary(position, irrational_type)
        
        # Educational commentary about the irrational number
        educational_comment = self._get_educational_commentary(irrational_type, position)
        
        # Choose one based on frequency
        commentary_choice = random.random()
        
        if commentary_choice < 0.3 and milestone_commentary:
            return milestone_commentary
        elif commentary_choice < 0.5 and pattern_commentary:
            return pattern_commentary
        elif commentary_choice < 0.7:
            return educational_comment
        else:
            return general_comment
    
    def _check_milestones(self, position: int) -> str:
        """Check if position is a milestone"""
        for milestone, comments in self.milestone_commentary.items():
            if position == milestone:
                return random.choice(comments)
        return None
    
    def _detect_patterns(self, position: int, digits: str) -> str:
        """Detect interesting patterns in the digits"""
        if position < 3 or position >= len(digits):
            return None
        
        # Get recent digits for pattern detection
        recent_digits = digits[max(0, position-5):position+1]
        
        # Check for repeating digits
        if len(recent_digits) >= 3 and len(set(recent_digits[-3:])) == 1:
            return random.choice(self.special_patterns['repeating_digits'])
        
        # Check for ascending sequence
        if len(recent_digits) >= 3:
            ascending = True
            for i in range(len(recent_digits)-2, len(recent_digits)-1):
                if i >= 0 and int(recent_digits[i+1]) <= int(recent_digits[i]):
                    ascending = False
                    break
            if ascending and len(recent_digits) >= 3:
                return random.choice(self.special_patterns['ascending_sequence'])
        
        # Check for descending sequence
        if len(recent_digits) >= 3:
            descending = True
            for i in range(len(recent_digits)-2, len(recent_digits)-1):
                if i >= 0 and int(recent_digits[i+1]) >= int(recent_digits[i]):
                    descending = False
                    break
            if descending and len(recent_digits) >= 3:
                return random.choice(self.special_patterns['descending_sequence'])
        
        # Check for small palindrome
        if len(recent_digits) >= 3:
            last_three = recent_digits[-3:]
            if last_three == last_three[::-1]:
                return random.choice(self.special_patterns['palindrome'])
        
        return None
    
    def _generate_position_commentary(self, position: int, irrational_type: str) -> str:
        """Generate general commentary based on position"""
        base_commentary = self.general_commentary.copy()
        
        # Add position-specific flair
        if position % 50 == 0:
            base_commentary.append(f"📍 Position {position}: We're making excellent progress through {irrational_type.upper()}!")
        elif position % 25 == 0:
            base_commentary.append(f"🎯 Decimal place {position}: Another milestone in our {irrational_type.upper()} journey!")
        elif position % 10 == 0:
            base_commentary.append(f"📍 Digit {position}: Continuing our exploration of {irrational_type.upper()}!")
        
        return random.choice(base_commentary)
    
    def _get_educational_commentary(self, irrational_type: str, position: int) -> str:
        """Get educational commentary about the irrational number"""
        if irrational_type in self.pattern_commentary:
            comments = self.pattern_commentary[irrational_type].copy()
            
            # Add position-specific educational content
            if position < 50:
                comments.append(f"Fun fact: {irrational_type.upper()} is irrational, meaning it never repeats or terminates!")
            elif position < 100:
                comments.append(f"Amazing fact: We're seeing digits that no human had seen until computers were invented!")
            else:
                comments.append(f"Incredible: You're exploring territory that required supercomputers to discover!")
            
            return random.choice(comments)
        
        return random.choice(self.general_commentary)
    
    def get_captain_announcement(self, phase: str) -> str:
        """Get captain's announcement for different flight phases"""
        announcements = {
            'departure': [
                "🛫 Captain speaking: Welcome aboard The TransRational Airline!",
                "✈️ Captain: Prepare for departure into the world of PHYSICAL mathematics!",
                "🎯 Captain: Your journey through BOUNDED irrational numbers begins now!"
            ],
            'cruising': [
                "🌟 Captain: We've reached our cruising altitude in the REALITY stratosphere!",
                "✨ Captain: All systems nominal for PHYSICAL exploration!",
                "🔭 Captain: The mathematical landscape below has physical limits!"
            ],
            'quantum_boundary': [
                "⚠️ Captain: Approaching QUANTUM UNCERTAINTY boundary!",
                "🌌 Captain: This is where physics meets mathematics!",
                "🔬 Captain: Beyond this, spacetime itself breaks down!"
            ],
            'arrival': [
                "🛬 Captain: Beginning our descent after reaching physical limits!",
                "🎊 Captain: Thank you for exploring REALITY with us!",
                "🌈 Captain: Welcome back! You've discovered where 'infinity' ends!"
            ],
            'termination': [
                "🌟 Captain: PHYSICAL TERMINATION POINT REACHED!",
                "⚛️ Captain: You've found where 'infinite' numbers end!",
                "🔭 Captain: Reality imposes boundaries on mathematics!"
            ]
        }
        
        if phase in announcements:
            return random.choice(announcements[phase])
        return "🎯 Captain: Continuing our journey through mathematical wonders!"
    
    def get_safety_briefing(self) -> str:
        """Get safety briefing"""
        briefing = (
            "🛡️ REVOLUTIONARY Safety Briefing:\n"
            "• Please keep your PHYSICAL REALITY awareness secured at all times\n"
            "• In case of quantum boundary approach, prepare for reality breakdown\n"
            "• Emergency exits are located at cognitive limits (15 digits)\n"
            "• Ultimate termination: 61 digits (quantum uncertainty limit)\n"
            "• Enjoy the BOUNDED journey through physical mathematics!"
        )
        return briefing
    
    def add_commentary_to_history(self, position: int, commentary: str):
        """Add commentary to history"""
        self.commentary_history.append({
            'position': position,
            'commentary': commentary,
            'timestamp': time.time()
        })
        
        # Keep history manageable
        if len(self.commentary_history) > 1000:
            self.commentary_history = self.commentary_history[-500:]
    
    def get_commentary_statistics(self) -> Dict:
        """Get statistics about commentary generated"""
        if not self.commentary_history:
            return {}
        
        return {
            'total_commentary': len(self.commentary_history),
            'average_frequency': len(self.commentary_history) / max(1, self.commentary_history[-1]['position']),
            'most_recent_position': self.commentary_history[-1]['position'],
            'session_duration': time.time() - self.commentary_history[0]['timestamp'] if self.commentary_history else 0
        }
    
    def cleanup(self):
        """Clean up resources"""
        self.commentary_history = []
        self.position_markers = []