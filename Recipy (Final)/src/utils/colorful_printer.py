"""
Colorful Printer Utility for Child-Friendly Output
Makes learning fun and visually engaging!
"""

import random
import sys
from typing import Optional

class ColorfulPrinter:
    """Provides colorful, child-friendly printing functionality"""
    
    # ANSI color codes
    COLORS = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'magenta': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
        'pink': '\033[95m',
        'purple': '\033[94m',
        'orange': '\033[93m',
        'rainbow': 'rainbow',
        'bold': '\033[1m',
        'underline': '\033[4m',
        'end': '\033[0m'
    }
    
    def __init__(self):
        self.colorful_mode = True
        self.emoji_set = {
            'happy': ['😊', '😄', '🌟', '⭐', '💫', '🎉', '🎈', '🌈'],
            'thinking': ['🤔', '💭', '🧠', '💡', '🔍', '📚'],
            'success': ['🎉', '🏆', '⭐', '🌟', '💪', '👏', '🎊'],
            'love': ['💖', '💝', '💕', '💗', '💓', '❤️', '🫶'],
            'nature': ['🌸', '🌺', '🌻', '🌷', '🌹', '🌿', '🍃']
        }
    
    def _get_color_code(self, color: str) -> str:
        """Get ANSI color code for given color name"""
        return self.COLORS.get(color, '')
    
    def print_colored(self, text: str, color: str = 'white', end: str = '\n'):
        """Print text in specified color"""
        if not self.colorful_mode:
            print(text, end=end)
            return
        
        color_code = self._get_color_code(color)
        if color == 'rainbow':
            self.print_rainbow(text, end)
        else:
            print(f"{color_code}{text}{self.COLORS['end']}", end=end)
    
    def print_rainbow(self, text: str, end: str = '\n'):
        """Print text in rainbow colors"""
        if not self.colorful_mode:
            print(text, end=end)
            return
        
        colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']
        rainbow_text = ""
        
        for i, char in enumerate(text):
            if char == ' ' or char == '\n':
                rainbow_text += char
            else:
                color = colors[i % len(colors)]
                rainbow_text += f"{self._get_color_code(color)}{char}"
        
        print(f"{rainbow_text}{self.COLORS['end']}", end=end)
    
    def print_with_emoji(self, text: str, emoji_type: str = 'happy', color: str = 'white'):
        """Print text with appropriate emoji"""
        emoji = random.choice(self.emoji_set.get(emoji_type, ['😊']))
        self.print_colored(f"{emoji} {text}", color)
    
    def print_slowly(self, text: str, color: str = 'blue', delay: float = 0.03):
        """Print text slowly for dramatic effect"""
        if not self.colorful_mode:
            print(text)
            return
        
        color_code = self._get_color_code(color)
        for char in text:
            print(f"{color_code}{char}{self.COLORS['end']}", end='', flush=True)
            import time
            time.sleep(delay)
        print()
    
    def print_success(self, text: str):
        """Print success message"""
        self.print_with_emoji(text, 'success', 'green')
    
    def print_love(self, text: str):
        """Print loving message"""
        self.print_with_emoji(text, 'love', 'pink')
    
    def print_thinking(self, text: str):
        """Print thinking prompt"""
        self.print_with_emoji(text, 'thinking', 'purple')
    
    def print_nature(self, text: str):
        """Print nature-themed message"""
        self.print_with_emoji(text, 'nature', 'green')
    
    def print_red(self, text: str):
        """Print in red"""
        self.print_colored(text, 'red')
    
    def print_green(self, text: str):
        """Print in green"""
        self.print_colored(text, 'green')
    
    def print_yellow(self, text: str):
        """Print in yellow"""
        self.print_colored(text, 'yellow')
    
    def print_blue(self, text: str):
        """Print in blue"""
        self.print_colored(text, 'blue')
    
    def print_magenta(self, text: str):
        """Print in magenta"""
        self.print_colored(text, 'magenta')
    
    def print_cyan(self, text: str):
        """Print in cyan"""
        self.print_colored(text, 'cyan')
    
    def print_purple(self, text: str):
        """Print in purple"""
        self.print_colored(text, 'purple')
    
    def print_pink(self, text: str):
        """Print in pink"""
        self.print_colored(text, 'pink')
    
    def print_box(self, text: str, color: str = 'blue'):
        """Print text in a decorative box"""
        lines = text.split('\n')
        max_length = max(len(line) for line in lines)
        
        border = '+' + '-' * (max_length + 4) + '+'
        color_code = self._get_color_code(color)
        
        self.print_colored(border, color)
        for line in lines:
            padded_line = line.ljust(max_length)
            self.print_colored(f"| {padded_line} |", color)
        self.print_colored(border, color)
    
    def print_star_border(self, text: str, color: str = 'yellow'):
        """Print text with star borders"""
        self.print_colored("⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐", color)
        self.print_colored(f"⭐     {text}     ⭐", color)
        self.print_colored("⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐", color)
    
    def disable_colors(self):
        """Disable colorful output"""
        self.colorful_mode = False
    
    def enable_colors(self):
        """Enable colorful output"""
        self.colorful_mode = True
    
    def animate_thinking(self, duration: float = 2.0):
        """Show thinking animation"""
        import time
        symbols = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
        end_time = time.time() + duration
        
        while time.time() < end_time:
            for symbol in symbols:
                if time.time() >= end_time:
                    break
                print(f"\r{self.COLORS['blue']}{symbol} Thinking...{self.COLORS['end']}", end='', flush=True)
                time.sleep(0.1)
        
        print("\r" + " " * 20 + "\r", end='', flush=True)