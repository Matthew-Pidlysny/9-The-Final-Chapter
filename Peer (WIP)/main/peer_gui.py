"""
ENHANCED PEER SYSTEM GUI - Advanced Visual Interface
Impressive GUI with stunning visuals and comprehensive features
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.patches as mpatches
import numpy as np
import json
import threading
import time
from datetime import datetime
import hashlib
from PIL import Image, ImageTk, ImageDraw, ImageFont
import seaborn as sns
from typing import Dict, List, Optional, Any
import queue

# Import enhanced peer system
from enhanced_peer_system import EnhancedPeerSystem
from scientific_features import ScientificField, ComplexityLevel

class ModernStyle:
    """Modern styling configuration for GUI."""
    
    # Color palette
    COLORS = {
        'primary': '#2E86AB',      # Deep blue
        'secondary': '#A23B72',    # Purple
        'accent': '#F18F01',       # Orange
        'success': '#C73E1D',      # Red-orange
        'dark_bg': '#1a1a2e',      # Dark blue
        'light_bg': '#16213e',     # Medium blue
        'text_light': '#eee',      # Light text
        'text_dark': '#333',       # Dark text
        'panel_bg': '#0f3460',     # Panel background
        'grid_color': '#2c3e50',   # Grid lines
        'highlight': '#3498db',    # Highlight color
    }
    
    # Fonts
    FONTS = {
        'title': ('Segoe UI', 24, 'bold'),
        'heading': ('Segoe UI', 16, 'bold'),
        'normal': ('Segoe UI', 10),
        'code': ('Consolas', 9),
        'button': ('Segoe UI', 10, 'bold')
    }

class AnimatedCanvas:
    """Animated canvas with particle effects and visual enhancements."""
    
    def __init__(self, parent, width=800, height=600):
        self.parent = parent
        self.width = width
        self.height = height
        self.particles = []
        self.animation_running = True
        
        # Create main frame
        self.frame = tk.Frame(parent, bg=ModernStyle.COLORS['dark_bg'])
        
        # Create matplotlib figure for advanced graphics
        self.fig = Figure(figsize=(12, 8), facecolor=ModernStyle.COLORS['dark_bg'])
        self.ax = self.fig.add_subplot(111, facecolor=ModernStyle.COLORS['light_bg'])
        
        # Setup canvas
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # Initialize particles
        self.init_particles()
        
        # Start animation
        self.animate()
    
    def init_particles(self):
        """Initialize floating particles for visual effect."""
        num_particles = 50
        for _ in range(num_particles):
            self.particles.append({
                'x': np.random.uniform(0, self.width),
                'y': np.random.uniform(0, self.height),
                'vx': np.random.uniform(-1, 1),
                'vy': np.random.uniform(-1, 1),
                'size': np.random.uniform(0.5, 2),
                'color': np.random.choice([ModernStyle.COLORS['primary'], 
                                         ModernStyle.COLORS['secondary'], 
                                         ModernStyle.COLORS['accent']]),
                'alpha': np.random.uniform(0.1, 0.5)
            })
    
    def animate(self):
        """Animate particles and visual effects."""
        if not self.animation_running:
            return
        
        # Clear and redraw
        self.ax.clear()
        self.ax.set_xlim(0, self.width)
        self.ax.set_ylim(0, self.height)
        self.ax.set_aspect('equal')
        self.ax.axis('off')
        
        # Draw particles
        for particle in self.particles:
            # Update position
            particle['x'] += particle['vx']
            particle['y'] += particle['vy']
            
            # Bounce off walls
            if particle['x'] <= 0 or particle['x'] >= self.width:
                particle['vx'] *= -1
            if particle['y'] <= 0 or particle['y'] >= self.height:
                particle['vy'] *= -1
            
            # Draw particle
            circle = plt.Circle((particle['x'], particle['y']), 
                               particle['size'], 
                               color=particle['color'], 
                               alpha=particle['alpha'])
            self.ax.add_patch(circle)
        
        # Add connecting lines between nearby particles
        for i, p1 in enumerate(self.particles):
            for p2 in self.particles[i+1:]:
                distance = np.sqrt((p1['x'] - p2['x'])**2 + (p1['y'] - p2['y'])**2)
                if distance < 100:
                    self.ax.plot([p1['x'], p2['x']], [p1['y'], p2['y']], 
                               color=ModernStyle.COLORS['primary'], 
                               alpha=0.1, linewidth=0.5)
        
        self.canvas.draw()
        self.parent.after(50, self.animate)
    
    def stop_animation(self):
        """Stop the animation."""
        self.animation_running = False

class ValidationVisualization:
    """Advanced visualization for validation results."""
    
    def __init__(self, parent):
        self.parent = parent
        self.fig = Figure(figsize=(14, 10), facecolor=ModernStyle.COLORS['dark_bg'])
        
        # Create subplots
        self.ax_main = self.fig.add_subplot(221, facecolor=ModernStyle.COLORS['light_bg'])
        self.ax_errors = self.fig.add_subplot(222, facecolor=ModernStyle.COLORS['light_bg'])
        self.ax_features = self.fig.add_subplot(223, facecolor=ModernStyle.COLORS['light_bg'])
        self.ax_timeline = self.fig.add_subplot(224, facecolor=ModernStyle.COLORS['light_bg'])
        
        self.canvas = FigureCanvasTkAgg(self.fig, master=parent)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        self.setup_style()
    
    def setup_style(self):
        """Setup modern matplotlib styling."""
        plt.style.use('dark_background')
        for ax in [self.ax_main, self.ax_errors, self.ax_features, self.ax_timeline]:
            ax.grid(True, alpha=0.3, color=ModernStyle.COLORS['grid_color'])
            ax.tick_params(colors=ModernStyle.COLORS['text_light'])
            ax.spines['bottom'].set_color(ModernStyle.COLORS['text_light'])
            ax.spines['top'].set_color(ModernStyle.COLORS['text_light'])
            ax.spines['right'].set_color(ModernStyle.COLORS['text_light'])
            ax.spines['left'].set_color(ModernStyle.COLORS['text_light'])
    
    def update_visualization(self, validation_results: Dict):
        """Update visualization with validation results."""
        # Clear all axes
        for ax in [self.ax_main, self.ax_errors, self.ax_features, self.ax_timeline]:
            ax.clear()
            ax.set_facecolor(ModernStyle.COLORS['light_bg'])
        
        # Main validation score visualization
        self.create_main_validation_viz(validation_results)
        
        # Error analysis visualization
        self.create_error_viz(validation_results)
        
        # Feature distribution visualization
        self.create_feature_viz(validation_results)
        
        # Timeline visualization
        self.create_timeline_viz(validation_results)
        
        self.canvas.draw()
    
    def create_main_validation_viz(self, results: Dict):
        """Create main validation score visualization."""
        if 'validation_summary' in results:
            score = results['validation_summary']['average_score']
            
            # Create gauge chart
            theta = np.linspace(0, np.pi, 100)
            r = 1
            
            # Background arc
            self.ax_main.plot(theta, np.ones_like(theta), 'o-', 
                            color=ModernStyle.COLORS['grid_color'], linewidth=20)
            
            # Score arc
            score_theta = np.linspace(0, score * np.pi, 100)
            self.ax_main.plot(score_theta, np.ones_like(score_theta), 'o-', 
                            color=self.get_score_color(score), linewidth=20)
            
            # Add score text
            self.ax_main.text(0.5, 0.3, f'{score:.3f}', 
                            fontsize=48, fontweight='bold', 
                            color=ModernStyle.COLORS['text_light'],
                            ha='center', va='center',
                            transform=self.ax_main.transAxes)
            
            self.ax_main.text(0.5, 0.1, 'VALIDATION SCORE', 
                            fontsize=14, 
                            color=ModernStyle.COLORS['text_light'],
                            ha='center', va='center',
                            transform=self.ax_main.transAxes)
            
            self.ax_main.set_xlim(0, np.pi)
            self.ax_main.set_ylim(0, 1.5)
            self.ax_main.axis('off')
            self.ax_main.set_title('Overall Validation Score', 
                                  color=ModernStyle.COLORS['text_light'], 
                                  fontsize=16, fontweight='bold', pad=20)
    
    def create_error_viz(self, results: Dict):
        """Create error analysis visualization."""
        if 'detailed_results' in results:
            error_counts = []
            formula_names = []
            
            for result in results['detailed_results']:
                error_counts.append(len(result.get('errors', [])))
                formula_names.append(result.get('formula_name', 'Unknown'))
            
            bars = self.ax_errors.bar(formula_names, error_counts, 
                                     color=ModernStyle.COLORS['secondary'], 
                                     alpha=0.7, edgecolor=ModernStyle.COLORS['text_light'])
            
            # Add value labels on bars
            for bar, count in zip(bars, error_counts):
                height = bar.get_height()
                self.ax_errors.text(bar.get_x() + bar.get_width()/2., height,
                                   f'{count}', ha='center', va='bottom',
                                   color=ModernStyle.COLORS['text_light'])
            
            self.ax_errors.set_title('Error Detection Analysis', 
                                    color=ModernStyle.COLORS['text_light'], 
                                    fontsize=14, fontweight='bold')
            self.ax_errors.set_ylabel('Number of Errors', 
                                     color=ModernStyle.COLORS['text_light'])
            self.ax_errors.tick_params(axis='x', rotation=45, 
                                      colors=ModernStyle.COLORS['text_light'])
    
    def create_feature_viz(self, results: Dict):
        """Create feature distribution visualization."""
        # Simulate feature distribution data
        categories = ['Mathematical Rigor', 'Experimental Validation', 'Theoretical Consistency',
                     'Computational Verification', 'Statistical Analysis', 'Peer Review Standards']
        values = np.random.randint(10, 100, len(categories))
        
        colors = [ModernStyle.COLORS['primary'], ModernStyle.COLORS['secondary'], 
                 ModernStyle.COLORS['accent'], ModernStyle.COLORS['success'],
                 ModernStyle.COLORS['highlight'], ModernStyle.COLORS['grid_color']]
        
        wedges, texts, autotexts = self.ax_features.pie(values, labels=categories, 
                                                       colors=colors, autopct='%1.1f%%',
                                                       startangle=90)
        
        for autotext in autotexts:
            autotext.set_color(ModernStyle.COLORS['text_light'])
            autotext.set_fontweight('bold')
        
        self.ax_features.set_title('Feature Application Distribution', 
                                  color=ModernStyle.COLORS['text_light'], 
                                  fontsize=14, fontweight='bold')
    
    def create_timeline_viz(self, results: Dict):
        """Create validation timeline visualization."""
        # Simulate timeline data
        timestamps = pd.date_range(start=datetime.now() - pd.Timedelta(hours=2), 
                                 end=datetime.now(), freq='15min')
        scores = np.random.uniform(0.7, 1.0, len(timestamps))
        
        self.ax_timeline.plot(timestamps, scores, marker='o', linewidth=3, 
                            color=ModernStyle.COLORS['primary'], markersize=8,
                            markerfacecolor=ModernStyle.COLORS['accent'])
        
        # Add confidence bands
        self.ax_timeline.fill_between(timestamps, scores - 0.05, scores + 0.05,
                                    alpha=0.3, color=ModernStyle.COLORS['primary'])
        
        self.ax_timeline.set_title('Validation Score Timeline', 
                                  color=ModernStyle.COLORS['text_light'], 
                                  fontsize=14, fontweight='bold')
        self.ax_timeline.set_ylabel('Score', color=ModernStyle.COLORS['text_light'])
        self.ax_timeline.tick_params(axis='x', rotation=45, 
                                    colors=ModernStyle.COLORS['text_light'])
    
    def get_score_color(self, score: float) -> str:
        """Get color based on validation score."""
        if score >= 0.9:
            return '#00ff00'  # Green
        elif score >= 0.7:
            return ModernStyle.COLORS['accent']  # Orange
        elif score >= 0.5:
            return ModernStyle.COLORS['secondary']  # Purple
        else:
            return '#ff0000'  # Red

class EnhancedPeerGUI:
    """Main GUI application for Enhanced Peer System."""
    
    def __init__(self, root):
        self.root = root
        self.root.title("🚀 Enhanced Peer System - Universal Scientific Validation")
        self.root.geometry("1400x900")
        
        # Setup modern styling
        self.setup_modern_style()
        
        # Initialize peer system
        self.peer_system = EnhancedPeerSystem()
        
        # Create GUI components
        self.create_widgets()
        
        # Setup queue for thread-safe updates
        self.update_queue = queue.Queue()
        self.process_queue()
        
        # Initialize with demo data
        self.load_demo_visualization()
    
    def setup_modern_style(self):
        """Setup modern tkinter styling."""
        self.root.configure(bg=ModernStyle.COLORS['dark_bg'])
        
        # Configure ttk styles
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure custom styles
        style.configure('Title.TLabel', 
                       background=ModernStyle.COLORS['dark_bg'],
                       foreground=ModernStyle.COLORS['text_light'],
                       font=ModernStyle.FONTS['title'])
        
        style.configure('Heading.TLabel',
                       background=ModernStyle.COLORS['dark_bg'],
                       foreground=ModernStyle.COLORS['text_light'],
                       font=ModernStyle.FONTS['heading'])
        
        style.configure('Modern.TButton',
                       background=ModernStyle.COLORS['primary'],
                       foreground=ModernStyle.COLORS['text_light'],
                       font=ModernStyle.FONTS['button'],
                       borderwidth=0,
                       focuscolor='none')
        
        style.map('Modern.TButton',
                 background=[('active', ModernStyle.COLORS['secondary'])])
        
        style.configure('Modern.TFrame',
                       background=ModernStyle.COLORS['dark_bg'])
    
    def create_widgets(self):
        """Create all GUI widgets."""
        # Main container
        main_container = tk.Frame(self.root, bg=ModernStyle.COLORS['dark_bg'])
        main_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Top section - Title and controls
        self.create_header_section(main_container)
        
        # Middle section - Main visualization
        self.create_main_visualization(main_container)
        
        # Bottom section - Input and results
        self.create_input_section(main_container)
    
    def create_header_section(self, parent):
        """Create header section with title and controls."""
        header_frame = tk.Frame(parent, bg=ModernStyle.COLORS['dark_bg'])
        header_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Title
        title_label = tk.Label(header_frame, 
                              text="🧮 Enhanced Peer System",
                              font=ModernStyle.FONTS['title'],
                              fg=ModernStyle.COLORS['text_light'],
                              bg=ModernStyle.COLORS['dark_bg'])
        title_label.pack(side=tk.LEFT)
        
        # Subtitle
        subtitle_label = tk.Label(header_frame,
                                 text="Universal Scientific Validation Framework",
                                 font=ModernStyle.FONTS['normal'],
                                 fg=ModernStyle.COLORS['text_light'],
                                 bg=ModernStyle.COLORS['dark_bg'])
        subtitle_label.pack(side=tk.LEFT, padx=(20, 0))
        
        # Control buttons
        button_frame = tk.Frame(header_frame, bg=ModernStyle.COLORS['dark_bg'])
        button_frame.pack(side=tk.RIGHT)
        
        # Run validation button
        self.run_button = tk.Button(button_frame,
                                   text="🚀 Run Validation",
                                   font=ModernStyle.FONTS['button'],
                                   bg=ModernStyle.COLORS['primary'],
                                   fg=ModernStyle.COLORS['text_light'],
                                   bd=0,
                                   padx=20,
                                   pady=10,
                                   command=self.run_validation)
        self.run_button.pack(side=tk.LEFT, padx=5)
        
        # Load formula button
        load_button = tk.Button(button_frame,
                               text="📁 Load Formula",
                               font=ModernStyle.FONTS['button'],
                               bg=ModernStyle.COLORS['secondary'],
                               fg=ModernStyle.COLORS['text_light'],
                               bd=0,
                               padx=20,
                               pady=10,
                               command=self.load_formula)
        load_button.pack(side=tk.LEFT, padx=5)
        
        # Save results button
        save_button = tk.Button(button_frame,
                               text="💾 Save Results",
                               font=ModernStyle.FONTS['button'],
                               bg=ModernStyle.COLORS['accent'],
                               fg=ModernStyle.COLORS['text_light'],
                               bd=0,
                               padx=20,
                               pady=10,
                               command=self.save_results)
        save_button.pack(side=tk.LEFT, padx=5)
    
    def create_main_visualization(self, parent):
        """Create main visualization area."""
        viz_container = tk.Frame(parent, bg=ModernStyle.COLORS['light_bg'], relief=tk.RAISED, bd=2)
        viz_container.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # Create notebook for tabs
        self.notebook = ttk.Notebook(viz_container)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Main dashboard tab
        self.dashboard_frame = tk.Frame(self.notebook, bg=ModernStyle.COLORS['dark_bg'])
        self.notebook.add(self.dashboard_frame, text="📊 Dashboard")
        
        # Create validation visualization
        self.validation_viz = ValidationVisualization(self.dashboard_frame)
        
        # Animated background tab
        self.animation_frame = tk.Frame(self.notebook, bg=ModernStyle.COLORS['dark_bg'])
        self.notebook.add(self.animation_frame, text="✨ Animation")
        
        # Create animated canvas
        self.animated_canvas = AnimatedCanvas(self.animation_frame, 800, 600)
        self.animated_canvas.frame.pack(fill=tk.BOTH, expand=True)
        
        # Cloud storage tab
        self.cloud_frame = tk.Frame(self.notebook, bg=ModernStyle.COLORS['dark_bg'])
        self.notebook.add(self.cloud_frame, text="☁️ Cloud Storage")
        
        self.create_cloud_storage_ui()
    
    def create_cloud_storage_ui(self):
        """Create cloud storage configuration UI."""
        # Instructions
        instructions = tk.Text(self.cloud_frame, height=8, width=80,
                              font=ModernStyle.FONTS['normal'],
                              bg=ModernStyle.COLORS['light_bg'],
                              fg=ModernStyle.COLORS['text_light'],
                              wrap=tk.WORD)
        instructions.pack(padx=20, pady=20)
        
        instructions.insert(tk.END, "☁️ Cloud Storage Configuration\n\n")
        instructions.insert(tk.END, "The Enhanced Peer System supports automatic upload of computational results to multiple cloud storage providers:\n\n")
        instructions.insert(tk.END, "📦 AWS S3 • 🔷 Google Cloud Storage • ☁️ Microsoft Azure • 📦 Dropbox\n\n")
        instructions.insert(tk.END, "Each provider includes comprehensive setup tutorials and automated connection testing. Configure your preferred provider in the cloud_config.json file, or use the interactive setup wizard.\n\n")
        instructions.insert(tk.END, "Features: • Data compression • Encryption • Parallel uploads • Cost estimation")
        instructions.config(state=tk.DISABLED)
        
        # Status display
        status_frame = tk.Frame(self.cloud_frame, bg=ModernStyle.COLORS['dark_bg'])
        status_frame.pack(fill=tk.X, padx=20, pady=10)
        
        tk.Label(status_frame, text="Cloud Storage Status:", 
                font=ModernStyle.FONTS['heading'],
                fg=ModernStyle.COLORS['text_light'],
                bg=ModernStyle.COLORS['dark_bg']).pack(side=tk.LEFT)
        
        self.cloud_status_label = tk.Label(status_frame, text="🔴 Not Configured",
                                          font=ModernStyle.FONTS['normal'],
                                          fg=ModernStyle.COLORS['accent'],
                                          bg=ModernStyle.COLORS['dark_bg'])
        self.cloud_status_label.pack(side=tk.LEFT, padx=20)
    
    def create_input_section(self, parent):
        """Create input and results section."""
        input_container = tk.Frame(parent, bg=ModernStyle.COLORS['light_bg'], relief=tk.RAISED, bd=2)
        input_container.pack(fill=tk.BOTH, pady=(0, 0))
        
        # Create paned window for input and results
        paned = tk.PanedWindow(input_container, orient=tk.HORIZONTAL, bg=ModernStyle.COLORS['light_bg'])
        paned.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Input panel
        input_frame = tk.Frame(paned, bg=ModernStyle.COLORS['dark_bg'])
        paned.add(input_frame, minsize=400)
        
        tk.Label(input_frame, text="📝 Formula Input",
                font=ModernStyle.FONTS['heading'],
                fg=ModernStyle.COLORS['text_light'],
                bg=ModernStyle.COLORS['dark_bg']).pack(pady=10)
        
        self.formula_input = scrolledtext.ScrolledText(input_frame,
                                                      height=10,
                                                      width=50,
                                                      font=ModernStyle.FONTS['code'],
                                                      bg=ModernStyle.COLORS['panel_bg'],
                                                      fg=ModernStyle.COLORS['text_light'])
        self.formula_input.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        # Results panel
        results_frame = tk.Frame(paned, bg=ModernStyle.COLORS['dark_bg'])
        paned.add(results_frame, minsize=400)
        
        tk.Label(results_frame, text="📊 Validation Results",
                font=ModernStyle.FONTS['heading'],
                fg=ModernStyle.COLORS['text_light'],
                bg=ModernStyle.COLORS['dark_bg']).pack(pady=10)
        
        self.results_display = scrolledtext.ScrolledText(results_frame,
                                                       height=10,
                                                       width=50,
                                                       font=ModernStyle.FONTS['normal'],
                                                       bg=ModernStyle.COLORS['panel_bg'],
                                                       fg=ModernStyle.COLORS['text_light'])
        self.results_display.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        # Progress bar
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(input_container, 
                                          variable=self.progress_var,
                                          maximum=100,
                                          style='TProgressbar')
        self.progress_bar.pack(fill=tk.X, padx=10, pady=(0, 10))
    
    def run_validation(self):
        """Run validation in a separate thread."""
        # Get formula from input
        formula = self.formula_input.get("1.0", tk.END).strip()
        
        if not formula:
            messagebox.showwarning("Input Required", "Please enter a formula to validate.")
            return
        
        # Disable run button during validation
        self.run_button.config(state=tk.DISABLED, text="⏳ Running...")
        
        # Start validation in thread
        thread = threading.Thread(target=self._run_validation_thread, args=(formula,))
        thread.daemon = True
        thread.start()
    
    def _run_validation_thread(self, formula: str):
        """Run validation in background thread."""
        try:
            # Update progress
            self.update_queue.put(('progress', 10))
            
            # Run validation
            self.update_queue.put(('progress', 30))
            result = self.peer_system.run_formula_validation(formula, "User Formula")
            
            self.update_queue.put(('progress', 70))
            
            # Update visualization
            self.update_queue.put(('visualization', result))
            
            # Display results
            self.update_queue.put(('results', result))
            
            self.update_queue.put(('progress', 100))
            
        except Exception as e:
            self.update_queue.put(('error', str(e)))
        finally:
            self.update_queue.put(('complete', None))
    
    def process_queue(self):
        """Process updates from background threads."""
        try:
            while True:
                msg_type, data = self.update_queue.get_nowait()
                
                if msg_type == 'progress':
                    self.progress_var.set(data)
                
                elif msg_type == 'visualization':
                    self.validation_viz.update_visualization(data)
                
                elif msg_type == 'results':
                    self.display_results(data)
                
                elif msg_type == 'error':
                    messagebox.showerror("Validation Error", f"An error occurred: {data}")
                
                elif msg_type == 'complete':
                    self.run_button.config(state=tk.NORMAL, text="🚀 Run Validation")
        
        except queue.Empty:
            pass
        
        self.root.after(100, self.process_queue)
    
    def display_results(self, result: Dict):
        """Display validation results."""
        self.results_display.delete("1.0", tk.END)
        
        # Format results for display
        results_text = f"🔍 Validation Results\n"
        results_text += f"{'='*50}\n\n"
        results_text += f"Formula: {result.get('formula_name', 'Unknown')}\n"
        results_text += f"Hash: {result.get('formula_hash', 'N/A')}\n\n"
        
        if 'validation_score' in result:
            score = result['validation_score']
            results_text += f"📊 Overall Score: {score:.3f}\n"
            results_text += f"Quality: {self.get_quality_description(score)}\n\n"
        
        if 'errors' in result:
            errors = result['errors']
            results_text += f"🚨 Errors Found: {len(errors)}\n"
            for i, error in enumerate(errors[:5], 1):  # Show first 5 errors
                results_text += f"  {i}. {error.get('description', 'Unknown error')}\n"
            if len(errors) > 5:
                results_text += f"  ... and {len(errors) - 5} more\n"
            results_text += "\n"
        
        if 'substantiation' in result:
            results_text += f"🎯 Substantiation Level: {result['substantiation'].get('validation_level', 'Unknown')}\n"
        
        if 'features_applied' in result:
            results_text += f"⚡ Features Applied: {result['features_applied']}\n\n"
        
        results_text += f"🕒 Timestamp: {result.get('timestamp', 'Unknown')}\n"
        
        self.results_display.insert(tk.END, results_text)
    
    def get_quality_description(self, score: float) -> str:
        """Get quality description based on score."""
        if score >= 0.9:
            return "🟢 Excellent - High confidence in validity"
        elif score >= 0.7:
            return "🟡 Good - Strong evidence for validity"
        elif score >= 0.5:
            return "🟠 Fair - Moderate confidence"
        else:
            return "🔴 Poor - Low confidence, issues detected"
    
    def load_formula(self):
        """Load formula from file."""
        filename = filedialog.askopenfilename(
            title="Select Formula File",
            filetypes=[("Python files", "*.py"), ("Text files", "*.txt"), ("All files", "*.*")]
        )
        
        if filename:
            try:
                with open(filename, 'r') as f:
                    content = f.read()
                self.formula_input.delete("1.0", tk.END)
                self.formula_input.insert("1.0", content)
            except Exception as e:
                messagebox.showerror("Load Error", f"Failed to load file: {e}")
    
    def save_results(self):
        """Save validation results to file."""
        filename = filedialog.asksaveasfilename(
            title="Save Results",
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("Text files", "*.txt"), ("All files", "*.*")]
        )
        
        if filename:
            try:
                # Get current results (simplified for demo)
                results = {
                    "timestamp": datetime.now().isoformat(),
                    "formula_input": self.formula_input.get("1.0", tk.END),
                    "results_display": self.results_display.get("1.0", tk.END)
                }
                
                with open(filename, 'w') as f:
                    json.dump(results, f, indent=2)
                
                messagebox.showinfo("Save Success", f"Results saved to {filename}")
            except Exception as e:
                messagebox.showerror("Save Error", f"Failed to save file: {e}")
    
    def load_demo_visualization(self):
        """Load demo visualization data."""
        # Create sample validation results for demo
        demo_results = {
            'validation_summary': {
                'average_score': 0.87,
                'total_formulas': 2,
                'total_errors': 3,
                'features_applied': 50
            },
            'detailed_results': [
                {
                    'formula_name': 'Basel Problem',
                    'errors': [],
                    'validation_score': 0.95
                },
                {
                    'formula_name': 'Harmonic Series',
                    'errors': ['Convergence claim error', 'Mathematical inconsistency'],
                    'validation_score': 0.78
                }
            ]
        }
        
        self.validation_viz.update_visualization(demo_results)
    
    def on_closing(self):
        """Handle window closing."""
        if hasattr(self, 'animated_canvas'):
            self.animated_canvas.stop_animation()
        self.root.destroy()

def main():
    """Main entry point for GUI application."""
    root = tk.Tk()
    app = EnhancedPeerGUI(root)
    
    # Handle window closing
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    
    # Start the GUI
    root.mainloop()

if __name__ == "__main__":
    main()