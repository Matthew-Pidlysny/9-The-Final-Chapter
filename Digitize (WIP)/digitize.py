#!/usr/bin/env python3
"""
DIGITIZE - The Decimal Space Explorer
An innovative educational program revealing the hidden architecture of numbers

Core Concept: Decimal Space Metric (Base-10 Lattice Metric)
The systematic study of how all numbers are constructed from the fundamental 
partnership of 2 and 5 in base-10 arithmetic.

Designed for Grade 1 learners with respect for their natural learning abilities.
No curriculum - just experience-driven understanding of number construction.
"""

import tkinter as tk
from tkinter import ttk, messagebox, font
import math
import random
from collections import defaultdict
import time

class DigitizeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Digitize - The Decimal Space Explorer")
        self.root.geometry("1400x900")
        self.root.configure(bg='#f0f8ff')
        
        # Core mathematical knowledge
        self.prime_factors_cache = {}
        self.decimal_space_metric = "Decimal Space Metric"
        self.base_10_lattice = "Base-10 Lattice Metric"
        
        # Learning state
        self.current_number = 1
        self.exploration_history = []
        self.achievement_count = 0
        
        # Color scheme - warm and inviting
        self.colors = {
            'bg': '#f0f8ff',
            'panel': '#e6f3ff',
            'button': '#4a90e2',
            'button_hover': '#357abd',
            'text': '#2c3e50',
            'highlight': '#e74c3c',
            'success': '#27ae60',
            'number_2': '#9b59b6',
            'number_5': '#f39c12',
            'number_balanced': '#16a085'
        }
        
        self.setup_gui()
        self.welcome_message()
        
    def setup_gui(self):
        """Setup the main GUI layout"""
        # Main container
        main_frame = tk.Frame(self.root, bg=self.colors['bg'])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Title area
        self.create_title_area(main_frame)
        
        # Middle section with panels
        middle_frame = tk.Frame(main_frame, bg=self.colors['bg'])
        middle_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Left panel - Number Construction
        self.create_construction_panel(middle_frame)
        
        # Center panel - Decimal Space Visualization
        self.create_visualization_panel(middle_frame)
        
        # Right panel - Pattern Discovery
        self.create_discovery_panel(middle_frame)
        
        # Bottom area - Interactive controls
        self.create_control_area(main_frame)
        
        # Achievement bar
        self.create_achievement_bar(main_frame)
        
    def create_title_area(self, parent):
        """Create the title and explanation area"""
        title_frame = tk.Frame(parent, bg=self.colors['bg'])
        title_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Main title
        title_font = font.Font(family="Arial", size=28, weight="bold")
        title_label = tk.Label(
            title_frame, 
            text="🌟 DIGITIZE 🌟",
            font=title_font,
            bg=self.colors['bg'],
            fg=self.colors['text']
        )
        title_label.pack()
        
        # Subtitle
        subtitle_font = font.Font(family="Arial", size=16)
        subtitle_label = tk.Label(
            title_frame,
            text="The Decimal Space Explorer - Discover How Numbers Are Built!",
            font=subtitle_font,
            bg=self.colors['bg'],
            fg=self.colors['button']
        )
        subtitle_label.pack()
        
        # Metric explanation
        metric_font = font.Font(family="Arial", size=12, italic=True)
        metric_label = tk.Label(
            title_frame,
            text=f"Using the {self.decimal_space_metric} - every number has a special story!",
            font=metric_font,
            bg=self.colors['bg'],
            fg=self.colors['text']
        )
        metric_label.pack()
        
    def create_construction_panel(self, parent):
        """Create the number construction panel"""
        panel = tk.LabelFrame(
            parent,
            text="🏗️ Number Construction",
            font=("Arial", 14, "bold"),
            bg=self.colors['panel'],
            fg=self.colors['text'],
            relief=tk.RAISED,
            borderwidth=3
        )
        panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        
        # Number selector
        select_frame = tk.Frame(panel, bg=self.colors['panel'])
        select_frame.pack(fill=tk.X, padx=15, pady=10)
        
        tk.Label(
            select_frame,
            text="Choose a number to explore:",
            font=("Arial", 12),
            bg=self.colors['panel']
        ).pack(side=tk.LEFT)
        
        self.number_entry = tk.Entry(
            select_frame,
            font=("Arial", 14, "bold"),
            width=10,
            bg='white'
        )
        self.number_entry.pack(side=tk.LEFT, padx=10)
        self.number_entry.insert(0, "39")
        
        explore_btn = tk.Button(
            select_frame,
            text="Explore! 🔍",
            command=self.explore_number,
            font=("Arial", 12, "bold"),
            bg=self.colors['button'],
            fg='white',
            relief=tk.RAISED,
            borderwidth=2,
            cursor="hand2"
        )
        explore_btn.pack(side=tk.LEFT)
        
        # Construction display
        self.construction_text = tk.Text(
            panel,
            height=15,
            width=35,
            font=("Arial", 11),
            bg='white',
            relief=tk.SUNKEN,
            borderwidth=2,
            wrap=tk.WORD
        )
        self.construction_text.pack(padx=15, pady=10, fill=tk.BOTH, expand=True)
        
        # Quick buttons for small numbers
        quick_frame = tk.Frame(panel, bg=self.colors['panel'])
        quick_frame.pack(fill=tk.X, padx=15, pady=5)
        
        for num in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 39, 100]:
            btn = tk.Button(
                quick_frame,
                text=str(num),
                command=lambda n=num: self.quick_explore(n),
                font=("Arial", 10, "bold"),
                bg=self.colors['button_hover'],
                fg='white',
                width=3,
                cursor="hand2"
            )
            btn.pack(side=tk.LEFT, padx=2)
            
    def create_visualization_panel(self, parent):
        """Create the decimal space visualization panel"""
        panel = tk.LabelFrame(
            parent,
            text="🎨 Decimal Space Visualization",
            font=("Arial", 14, "bold"),
            bg=self.colors['panel'],
            fg=self.colors['text'],
            relief=tk.RAISED,
            borderwidth=3
        )
        panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10)
        
        # Canvas for visualization
        self.viz_canvas = tk.Canvas(
            panel,
            width=400,
            height=400,
            bg='white',
            relief=tk.SUNKEN,
            borderwidth=2
        )
        self.viz_canvas.pack(padx=15, pady=10)
        
        # Legend
        legend_frame = tk.Frame(panel, bg=self.colors['panel'])
        legend_frame.pack(fill=tk.X, padx=15)
        
        legends = [
            ("⬜ Power of 2", self.colors['number_2']),
            ("⬛ Power of 5", self.colors['number_5']),
            ("🟦 Balanced (2×5)", self.colors['number_balanced'])
        ]
        
        for text, color in legends:
            label = tk.Label(
                legend_frame,
                text=text,
                font=("Arial", 10),
                bg=self.colors['panel'],
                fg=color
            )
            label.pack(side=tk.LEFT, padx=10)
            
        # Info display
        self.viz_info = tk.Text(
            panel,
            height=8,
            width=40,
            font=("Arial", 10),
            bg='white',
            relief=tk.SUNKEN,
            borderwidth=2,
            wrap=tk.WORD
        )
        self.viz_info.pack(padx=15, pady=5, fill=tk.X)
        
        # Draw initial space
        self.draw_decimal_space()
        
    def create_discovery_panel(self, parent):
        """Create the pattern discovery panel"""
        panel = tk.LabelFrame(
            parent,
            text="🔍 Pattern Discovery",
            font=("Arial", 14, "bold"),
            bg=self.colors['panel'],
            fg=self.colors['text'],
            relief=tk.RAISED,
            borderwidth=3
        )
        panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(10, 0))
        
        # Pattern type selector
        pattern_frame = tk.Frame(panel, bg=self.colors['panel'])
        pattern_frame.pack(fill=tk.X, padx=15, pady=10)
        
        tk.Label(
            pattern_frame,
            text="Discover patterns:",
            font=("Arial", 12),
            bg=self.colors['panel']
        ).pack(side=tk.LEFT)
        
        self.pattern_var = tk.StringVar(value="terminating")
        patterns = [
            ("🔚 Terminating", "terminating"),
            ("🔄 Repeating", "repeating"),
            ("⭐ Special", "special"),
            ("🎯 Balanced", "balanced")
        ]
        
        for text, value in patterns:
            rb = tk.Radiobutton(
                pattern_frame,
                text=text,
                variable=self.pattern_var,
                value=value,
                command=self.show_pattern,
                font=("Arial", 10),
                bg=self.colors['panel'],
                fg=self.colors['text'],
                selectcolor=self.colors['button']
            )
            rb.pack(side=tk.LEFT, padx=5)
            
        # Discovery display
        self.discovery_text = tk.Text(
            panel,
            height=12,
            width=35,
            font=("Arial", 11),
            bg='white',
            relief=tk.SUNKEN,
            borderwidth=2,
            wrap=tk.WORD
        )
        self.discovery_text.pack(padx=15, pady=10, fill=tk.BOTH, expand=True)
        
        # Fun fact button
        fun_fact_btn = tk.Button(
            panel,
            text="🎲 Surprise Me! (Random Fun Fact)",
            command=self.show_fun_fact,
            font=("Arial", 12, "bold"),
            bg=self.colors['success'],
            fg='white',
            relief=tk.RAISED,
            borderwidth=2,
            cursor="hand2"
        )
        fun_fact_btn.pack(pady=10)
        
    def create_control_area(self, parent):
        """Create interactive control area"""
        control_frame = tk.Frame(parent, bg=self.colors['bg'])
        control_frame.pack(fill=tk.X, pady=10)
        
        # Interactive exercises
        exercise_frame = tk.Frame(control_frame, bg=self.colors['bg'])
        exercise_frame.pack(side=tk.LEFT, padx=20)
        
        tk.Label(
            exercise_frame,
            text="🎯 Try These Fun Challenges:",
            font=("Arial", 12, "bold"),
            bg=self.colors['bg']
        ).pack()
        
        challenges = [
            ("Find the Magic 10", self.challenge_magic_10),
            ("Build a Perfect Decimal", self.challenge_perfect_decimal),
            ("Discover the Pattern", self.challenge_discover_pattern),
            ("Explore Reciprocal", self.challenge_reciprocal)
        ]
        
        for text, command in challenges:
            btn = tk.Button(
                exercise_frame,
                text=text,
                command=command,
                font=("Arial", 11),
                bg=self.colors['highlight'],
                fg='white',
                relief=tk.RAISED,
                borderwidth=2,
                cursor="hand2"
            )
            btn.pack(side=tk.LEFT, padx=5)
            
        # Help section
        help_frame = tk.Frame(control_frame, bg=self.colors['bg'])
        help_frame.pack(side=tk.RIGHT, padx=20)
        
        help_btn = tk.Button(
            help_frame,
            text="❓ How It Works",
            command=self.show_help,
            font=("Arial", 12, "bold"),
            bg=self.colors['button'],
            fg='white',
            relief=tk.RAISED,
            borderwidth=2,
            cursor="hand2"
        )
        help_btn.pack(side=tk.RIGHT, padx=5)
        
        reset_btn = tk.Button(
            help_frame,
            text="🔄 Start Over",
            command=self.reset_all,
            font=("Arial", 12),
            bg=self.colors['text'],
            fg='white',
            relief=tk.RAISED,
            borderwidth=2,
            cursor="hand2"
        )
        reset_btn.pack(side=tk.RIGHT, padx=5)
        
    def create_achievement_bar(self, parent):
        """Create the achievement progress bar"""
        achievement_frame = tk.Frame(parent, bg=self.colors['bg'])
        achievement_frame.pack(fill=tk.X, pady=(10, 0))
        
        tk.Label(
            achievement_frame,
            text="🏆 Your Discovery Journey:",
            font=("Arial", 12, "bold"),
            bg=self.colors['bg']
        ).pack(side=tk.LEFT, padx=10)
        
        self.progress_bar = ttk.Progressbar(
            achievement_frame,
            length=300,
            mode='determinate',
            maximum=100
        )
        self.progress_bar.pack(side=tk.LEFT, padx=10)
        
        self.progress_label = tk.Label(
            achievement_frame,
            text="0 discoveries made",
            font=("Arial", 11),
            bg=self.colors['bg']
        )
        self.progress_label.pack(side=tk.LEFT)
        
    def prime_factorization(self, n):
        """Get prime factorization of n"""
        if n in self.prime_factors_cache:
            return self.prime_factors_cache[n]
            
        if n <= 1:
            return {}
            
        original_n = n
        factors = {}
        d = 2
        while d * d <= n:
            while n % d == 0:
                factors[d] = factors.get(d, 0) + 1
                n //= d
            d += 1
        if n > 1:
            factors[n] = factors.get(n, 0) + 1
            
        self.prime_factors_cache[original_n] = factors.copy()
        return factors
        
    def classify_number(self, n):
        """Classify number according to decimal space metric"""
        factors = self.prime_factorization(n)
        
        # Check if only 2s and 5s (terminating decimal)
        if all(p in [2, 5] for p in factors.keys()):
            return {
                'type': 'SIMPLE',
                'description': 'This number makes a nice ending decimal!',
                'color': self.colors['success'],
                'factors': factors
            }
        
        # Check if prime
        if len(factors) == 1 and list(factors.values())[0] == 1:
            prime = list(factors.keys())[0]
            return {
                'type': 'PRIME_BASE',
                'description': f'This is prime number {prime} - it makes a repeating pattern!',
                'color': self.colors['highlight'],
                'factors': factors
            }
        
        # Otherwise wild
        return {
            'type': 'WILD',
            'description': 'This number has a special repeating pattern!',
            'color': self.colors['button'],
            'factors': factors
        }
        
    def explore_number(self):
        """Main exploration function"""
        try:
            num = int(self.number_entry.get())
            if num <= 0 or num > 10000:
                messagebox.showwarning("Oops!", "Please choose a number between 1 and 10,000!")
                return
                
            self.current_number = num
            self.show_number_construction(num)
            self.visualize_number_in_space(num)
            self.add_to_progress()
            
        except ValueError:
            messagebox.showwarning("Oops!", "Please type a whole number!")
            
    def quick_explore(self, n):
        """Quick exploration for preset numbers"""
        self.number_entry.delete(0, tk.END)
        self.number_entry.insert(0, str(n))
        self.explore_number()
        
    def show_number_construction(self, n):
        """Show how number is constructed"""
        self.construction_text.delete(1.0, tk.END)
        
        factors = self.prime_factorization(n)
        classification = self.classify_number(n)
        
        # Friendly explanation
        self.construction_text.insert(tk.END, f"🌟 Exploring Number {n}! 🌟\n\n", "title")
        
        # Basic info
        self.construction_text.insert(tk.END, f"Type: {classification['type']}\n", "type")
        self.construction_text.insert(tk.END, f"{classification['description']}\n\n", "desc")
        
        # Factor analysis
        self.construction_text.insert(tk.END, "🏗️ How it's built:\n", "subtitle")
        self.construction_text.insert(tk.END, "Prime factors: ", "normal")
        
        factor_parts = []
        for p, exp in factors.items():
            if exp == 1:
                factor_parts.append(str(p))
            else:
                factor_parts.append(f"{p}^{exp}")
        
        if factor_parts:
            self.construction_text.insert(tk.END, " × ".join(factor_parts), "factors")
            self.construction_text.insert(tk.END, f"\n\n", "normal")
        else:
            self.construction_text.insert(tk.END, "None (this is 1!)\n\n", "normal")
        
        # Decimal space analysis
        self.construction_text.insert(tk.END, "🔍 Decimal Space Analysis:\n", "subtitle")
        
        count_2 = factors.get(2, 0)
        count_5 = factors.get(5, 0)
        other_factors = [p for p in factors.keys() if p not in [2, 5]]
        
        if count_2 > 0:
            self.construction_text.insert(tk.END, f"• Has {count_2} power(s) of 2", self.colors['number_2'])
            self.construction_text.insert(tk.END, "\n", "normal")
        
        if count_5 > 0:
            self.construction_text.insert(tk.END, f"• Has {count_5} power(s) of 5", self.colors['number_5'])
            self.construction_text.insert(tk.END, "\n", "normal")
        
        if count_2 == count_5 and count_2 > 0:
            self.construction_text.insert(tk.END, "🎯 Perfect balance! This equals 10^" + str(count_2), self.colors['number_balanced'])
            self.construction_text.insert(tk.END, "\n", "normal")
        
        if other_factors:
            self.construction_text.insert(tk.END, f"• Also has: {', '.join(map(str, other_factors))}", "highlight")
            self.construction_text.insert(tk.END, "\n", "normal")
        
        # Special insights for specific numbers
        if n == 39:
            self.construction_text.insert(tk.END, "\n🌟 SPECIAL: 39 = 3 × 13\n", "special")
            self.construction_text.insert(tk.END, "Both 3 and 13 create repeating decimals!\n", "special")
            self.construction_text.insert(tk.END, "1/39 = 0.025641... (repeating)\n", "special")
        
        # Configure text tags
        self.construction_text.tag_config("title", font=("Arial", 14, "bold"), justify="center")
        self.construction_text.tag_config("type", font=("Arial", 12, "bold"), foreground=classification['color'])
        self.construction_text.tag_config("desc", font=("Arial", 11, "italic"))
        self.construction_text.tag_config("subtitle", font=("Arial", 11, "bold"))
        self.construction_text.tag_config("factors", font=("Arial", 11, "bold"), foreground=self.colors['highlight'])
        self.construction_text.tag_config("special", font=("Arial", 11, "bold"), foreground=self.colors['highlight'])
        self.construction_text.tag_config("normal", font=("Arial", 10))
        
    def draw_decimal_space(self, highlight_n=None):
        """Draw the decimal space lattice"""
        self.viz_canvas.delete("all")
        
        # Grid parameters
        canvas_size = 400
        center = canvas_size // 2
        grid_size = 7
        
        # Draw grid
        for i in range(-grid_size, grid_size + 1):
            for j in range(-grid_size, grid_size + 1):
                x = center + i * 25
                y = center - j * 25  # Negative for proper orientation
                
                # Calculate number at this position
                num = (2 ** i) * (5 ** j)
                
                # Determine color based on type
                if i == 0 and j == 0:
                    color = self.colors['highlight']  # 1 is special
                    size = 8
                elif i == j and i != 0:
                    color = self.colors['number_balanced']  # Balanced (powers of 10)
                    size = 6
                elif i == 0 and j != 0:
                    color = self.colors['number_5']  # Pure power of 5
                    size = 6
                elif j == 0 and i != 0:
                    color = self.colors['number_2']  # Pure power of 2
                    size = 6
                else:
                    color = self.colors['button']  # Mixed
                    size = 4
                
                # Highlight if this is our number
                if highlight_n and abs(num - highlight_n) < 0.001:
                    color = self.colors['highlight']
                    size = 10
                
                # Draw point
                if abs(num) < 1000000:  # Only draw reasonable numbers
                    self.viz_canvas.create_oval(
                        x - size, y - size, x + size, y + size,
                        fill=color, outline='white'
                    )
                    
                    # Label important points
                    if size >= 6 and abs(num) < 1000:
                        self.viz_canvas.create_text(
                            x, y - 15,
                            text=str(num),
                            font=("Arial", 8),
                            fill=self.colors['text']
                        )
        
        # Draw axes
        self.viz_canvas.create_line(0, center, canvas_size, center, fill='gray', dash=(2, 2))
        self.viz_canvas.create_line(center, 0, center, canvas_size, fill='gray', dash=(2, 2))
        
        # Labels
        self.viz_canvas.create_text(
            canvas_size - 30, center - 10,
            text="Power of 2 →",
            font=("Arial", 10),
            fill=self.colors['number_2']
        )
        self.viz_canvas.create_text(
            center + 30, 20,
            text="↑ Power of 5",
            font=("Arial", 10),
            fill=self.colors['number_5']
        )
        
    def visualize_number_in_space(self, n):
        """Visualize specific number in decimal space"""
        self.draw_decimal_space(highlight_n=n)
        
        # Update info
        self.viz_info.delete(1.0, tk.END)
        self.viz_info.insert(tk.END, f"📍 Number {n} in Decimal Space:\n\n", "title")
        
        factors = self.prime_factorization(n)
        count_2 = factors.get(2, 0)
        count_5 = factors.get(5, 0)
        
        # Explain position
        self.viz_info.insert(tk.END, f"Position: (2^{count_2}, 5^{count_5})\n", "position")
        
        # Explain what this means
        if count_2 > 0 or count_5 > 0:
            self.viz_info.insert(tk.END, f"\n🔍 This number is {count_2} steps right", "normal")
            if count_5 > 0:
                self.viz_info.insert(tk.END, f" and {count_5} steps up", "normal")
            self.viz_info.insert(tk.END, " in the space!\n", "normal")
        
        # Special insights
        if count_2 == count_5 and count_2 > 0:
            self.viz_info.insert(tk.END, f"\n⭐ Perfect balance! This equals 10^{count_2}\n", "balanced")
            self.viz_info.insert(tk.END, "That's why it's a perfect decimal!\n", "balanced")
        
        # Configure tags
        self.viz_info.tag_config("title", font=("Arial", 12, "bold"))
        self.viz_info.tag_config("position", font=("Arial", 11, "bold"))
        self.viz_info.tag_config("balanced", font=("Arial", 10, "bold"), foreground=self.colors['number_balanced'])
        self.viz_info.tag_config("normal", font=("Arial", 10))
        
    def show_pattern(self):
        """Show selected pattern type"""
        pattern_type = self.pattern_var.get()
        self.discovery_text.delete(1.0, tk.END)
        
        patterns = {
            'terminating': {
                'title': '🔚 Terminating Decimals',
                'content': '''These numbers have a special superpower!
                
When you divide 1 by them, the decimal ends nicely.

Rule: Numbers made only from 2s and 5s!

Examples:
1/2 = 0.5 (ends!)
1/4 = 0.25 (ends!)
1/5 = 0.2 (ends!)
1/8 = 0.125 (ends!)
1/10 = 0.1 (ends!)

Why? Because 10 = 2 × 5!
These numbers can divide a power of 10 perfectly.

Try exploring: 2, 4, 5, 8, 10, 16, 20, 25, 40, 50, 100'''
            },
            'repeating': {
                'title': '🔄 Repeating Decimals',
                'content': '''These numbers make beautiful patterns!
                
When you divide 1 by them, the decimal repeats forever.

Rule: Numbers with primes other than 2 and 5!

Examples:
1/3 = 0.333... (repeats 3)
1/6 = 0.1666... (repeats 6)
1/7 = 0.142857... (repeats 142857)
1/9 = 0.111... (repeats 1)
1/11 = 0.0909... (repeats 09)

Why? They create cycles based on modular arithmetic!
Each prime creates its own special pattern length.

Try exploring: 3, 6, 7, 9, 11, 12, 13, 14, 15, 17, 19'''
            },
            'special': {
                'title': '⭐ Special Numbers',
                'content': '''These numbers have unique properties!
                
They surprise us with special behaviors.

Full Reptend Primes:
Use ALL possible digits in their cycle!
1/7 = 0.142857 (uses 1,4,2,8,5,7)
1/17 = 0.0588235294117647 (16 different digits!)

Perfect Powers:
1/4 = 0.25 (2²)
1/8 = 0.125 (2³)
1/16 = 0.0625 (2⁴)

1/25 = 0.04 (5²)
1/125 = 0.008 (5³)

Mystery Numbers:
39 = 3 × 13 (both create repeating patterns!)
1/39 = 0.025641... (repeats 025641)

Try exploring: 7, 13, 17, 19, 39, 73, 97'''
            },
            'balanced': {
                'title': '🎯 Balanced Numbers',
                'content': '''These numbers are perfectly balanced!
                
They have equal powers of 2 and 5.

Rule: n = 2^k × 5^k = 10^k

Examples:
10 = 2¹ × 5¹ = 10¹
100 = 2² × 5² = 10²  
1000 = 2³ × 5³ = 10³

Why special?
Their reciprocals are perfect decimals:
1/10 = 0.1 (1 place)
1/100 = 0.01 (2 places)
1/1000 = 0.001 (3 places)

The number of decimal places equals the power!
This is the perfect "half" balance.

Try exploring: 10, 100, 1000, 10000'''
            }
        }
        
        pattern = patterns.get(pattern_type, patterns['terminating'])
        self.discovery_text.insert(tk.END, f"{pattern['title']}\n\n", "title")
        self.discovery_text.insert(tk.END, pattern['content'], "content")
        
        self.discovery_text.tag_config("title", font=("Arial", 12, "bold"))
        self.discovery_text.tag_config("content", font=("Arial", 10))
        
    def show_fun_fact(self):
        """Show a random fun fact about numbers"""
        fun_facts = [
            '''🌟 DID YOU KNOW?
            
The number 7 is magic!
1/7 = 0.142857142857...

The pattern 142857 repeats forever.
Multiply it by 2, 3, 4, 5, or 6:
142857 × 2 = 285714
142857 × 3 = 428571
142857 × 4 = 571428
142857 × 5 = 714285  
142857 × 6 = 857142

The digits just rotate! Amazing!''',
            
            '''🎯 COOL PATTERN!
            
Look at powers of 5:
5¹ = 5
5² = 25  
5³ = 125
5⁴ = 625
5⁵ = 3125
5⁶ = 15625

The last digit is always 5!
And 1/5 = 0.2, 1/25 = 0.04
Each power adds one more decimal place!''',
            
            '''🔍 NUMBER SECRET!
            
39 is mysterious:
39 = 3 × 13
1/39 = 0.025641...

The pattern has 6 digits: 025641
That's because both 3 and 13 create patterns!

1/3 = 0.3... (1 digit pattern)
1/13 = 0.076923... (6 digit pattern)
1/39 combines their magic!''',
            
            '''⚡ LIGHTNING FAST!
            
Powers of 2 double each time:
2¹ = 2
2² = 4
2³ = 8
2⁴ = 16
2⁵ = 32
2⁶ = 64

In decimals:
1/2 = 0.5
1/4 = 0.25
1/8 = 0.125
1/16 = 0.0625

Each power adds to the pattern!''',
            
            '''🎨 PERFECT SHAPES!
            
The decimal space is like a grid!
Every number has coordinates (2^a, 5^b).

Moving right = multiply by 2
Moving up = multiply by 5  
Moving left = divide by 2
Moving down = divide by 5

Diagonal (where a=b) = powers of 10!
This creates perfect balance!'''
        ]
        
        fact = random.choice(fun_facts)
        self.discovery_text.delete(1.0, tk.END)
        self.discovery_text.insert(tk.END, fact, "fun_fact")
        self.discovery_text.tag_config("fun_fact", font=("Arial", 10), justify="center")
        
    def challenge_magic_10(self):
        """Challenge: Find the magic of 10"""
        messagebox.showinfo(
            "🎯 Challenge: Magic of 10",
            """Try to find numbers that equal powers of 10!

Hint: Look for numbers with equal powers of 2 and 5.

Examples to try:
• 10 = 2¹ × 5¹
• 100 = 2² × 5²
• 40 = 2³ × 5¹

Why are these special?
Their reciprocals are perfect decimals!

1/10 = 0.1 (1 place)
1/100 = 0.01 (2 places)

Can you find more?"""
        )
        
    def challenge_perfect_decimal(self):
        """Challenge: Build perfect decimal"""
        messagebox.showinfo(
            "🎯 Challenge: Perfect Decimal",
            """Find numbers that make perfect ending decimals!

Rule: Use ONLY 2s and 5s in construction.

Start with these:
• 2 (0.5)
• 4 (0.25)  
• 5 (0.2)
• 8 (0.125)
• 10 (0.1)

Try combining them:
• 20 = 2² × 5¹ (0.05)
• 50 = 2¹ × 5² (0.02)
• 40 = 2³ × 5¹ (0.025)

What pattern do you see?"""
        )
        
    def challenge_discover_pattern(self):
        """Challenge: Discover the pattern"""
        messagebox.showinfo(
            "🎯 Challenge: Pattern Detective",
            """Be a pattern detective!

Try these number sequences:

Sequence 1: 2, 4, 8, 16, 32, 64...
What's the pattern? (×2 each time!)

Sequence 2: 5, 25, 125, 625, 3125...
What's the pattern? (×5 each time!)

Sequence 3: 10, 100, 1000, 10000...
What's the pattern? (×10 each time!)

Now try their reciprocals:
1/2 = 0.5
1/4 = 0.25
1/8 = 0.125

See how the decimal grows?"""
        )
        
    def challenge_reciprocal(self):
        """Challenge: Explore reciprocals"""
        messagebox.showinfo(
            "🎯 Challenge: Reciprocal Explorer",
            """Explore the hidden world of reciprocals!

Try dividing 1 by different numbers:

Simple numbers (ending decimals):
1/2 = 0.5
1/4 = 0.25
1/5 = 0.2
1/8 = 0.125

Pattern numbers (repeating):
1/3 = 0.333...
1/6 = 0.1666...
1/7 = 0.142857...
1/9 = 0.111...

Question: Why do some end and others repeat?
Hint: Look at the prime factors!"""
        )
        
    def show_help(self):
        """Show help information"""
        help_text = f"""
🌟 Welcome to DIGITIZE! 🌟

The {self.decimal_space_metric} helps us understand
how every number is constructed!

🏗️ NUMBER CONSTRUCTION:
• Every number is built from prime factors
• The primes 2 and 5 are special in base-10
• They create our decimal system!

🎨 DECIMAL SPACE:
• Think of a grid where you can move:
  → Right = multiply by 2
  → Up = multiply by 5
  → Left = divide by 2
  → Down = divide by 5

🔍 TYPES OF NUMBERS:
• SIMPLES: Only 2s and 5s → Perfect endings
• PRIMES: Other primes → Repeating patterns  
• WILDS: Mixed factors → Complex patterns

🎯 HOW TO EXPLORE:
1. Type any number (1-10000)
2. Click "Explore!" to see how it's built
3. Look at the visualization to see its place
4. Try the challenges to learn more!

Remember: Every number tells a story!
"""
        
        messagebox.showinfo("How Digitize Works", help_text)
        
    def reset_all(self):
        """Reset the entire application"""
        self.current_number = 1
        self.exploration_history = []
        self.number_entry.delete(0, tk.END)
        self.number_entry.insert(0, "1")
        
        self.construction_text.delete(1.0, tk.END)
        self.discovery_text.delete(1.0, tk.END)
        self.viz_info.delete(1.0, tk.END)
        
        self.draw_decimal_space()
        self.welcome_message()
        
        messagebox.showinfo("Reset", "Welcome back! Ready to explore numbers again!")
        
    def add_to_progress(self):
        """Add to progress and update"""
        self.achievement_count += 1
        self.exploration_history.append(self.current_number)
        
        # Update progress bar
        progress = min(self.achievement_count * 5, 100)
        self.progress_bar['value'] = progress
        self.progress_label.config(text=f"{self.achievement_count} discoveries made")
        
        # Celebration for milestones
        if self.achievement_count in [5, 10, 20, 50, 100]:
            self.celebrate_milestone()
            
    def celebrate_milestone(self):
        """Celebrate achievement milestone"""
        celebration_window = tk.Toplevel(self.root)
        celebration_window.title("🎉 Milestone Reached!")
        celebration_window.geometry("400x300")
        celebration_window.configure(bg=self.colors['bg'])
        
        tk.Label(
            celebration_window,
            text="🎉 AMAZING! 🎉",
            font=("Arial", 24, "bold"),
            bg=self.colors['bg'],
            fg=self.colors['highlight']
        ).pack(pady=20)
        
        tk.Label(
            celebration_window,
            text=f"You've made {self.achievement_count} discoveries!",
            font=("Arial", 16),
            bg=self.colors['bg'],
            fg=self.colors['text']
        ).pack(pady=10)
        
        tk.Label(
            celebration_window,
            text="You're becoming a Number Expert!",
            font=("Arial", 14, "italic"),
            bg=self.colors['bg'],
            fg=self.colors['success']
        ).pack(pady=10)
        
        tk.Button(
            celebration_window,
            text="Keep Exploring!",
            command=celebration_window.destroy,
            font=("Arial", 12, "bold"),
            bg=self.colors['success'],
            fg='white',
            relief=tk.RAISED,
            borderwidth=3
        ).pack(pady=20)
        
    def welcome_message(self):
        """Show welcome message in construction panel"""
        self.construction_text.delete(1.0, tk.END)
        welcome = '''🌟 Welcome to DIGITIZE! 🌟

I'm here to help you discover the amazing
hidden world of numbers!

Every number has a special story to tell
about how it's constructed.

✨ Try typing a number above!
✨ Or click the quick number buttons!
✨ Explore the challenges on the bottom!

Let's discover the magic of numbers together!

Ready? Let's start exploring! 🚀'''
        
        self.construction_text.insert(tk.END, welcome, "welcome")
        self.construction_text.tag_config("welcome", font=("Arial", 12), justify="center")
        
        # Also show initial pattern
        self.show_pattern()


def main():
    """Main entry point"""
    root = tk.Tk()
    app = DigitizeApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()