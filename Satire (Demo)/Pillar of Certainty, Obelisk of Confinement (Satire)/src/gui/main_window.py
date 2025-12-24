"""
Main Window GUI for The TransRational Airline
Elegant and user-friendly interface
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import threading
import time
from typing import Optional

class MainWindow:
    """Main application window"""
    
    def __init__(self, root: tk.Tk, app_controller):
        self.root = root
        self.app = app_controller
        
        # Color scheme
        self.bg_color = '#1a1a2e'
        self.primary_color = '#16213e'
        self.accent_color = '#0f3460'
        self.text_color = '#ffffff'
        self.accent_text = '#e94560'
        self.success_color = '#4caf50'
        
        # Configure root
        self.root.configure(bg=self.bg_color)
        
        # Create main layout
        self.create_widgets()
        self.create_menu()
        
        # Welcome message
        self.display_welcome()
    
    def create_widgets(self):
        """Create all GUI widgets"""
        
        # Main container
        main_frame = ttk.Frame(self.root, style='Dark.TFrame')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Top section - Controls
        self.create_control_panel(main_frame)
        
        # Middle section - Display
        self.create_display_panel(main_frame)
        
        # Bottom section - Attendant Messages
        self.create_attendant_panel(main_frame)
        
        # Status bar
        self.create_status_bar()
    
    def create_control_panel(self, parent):
        """Create control panel"""
        control_frame = ttk.LabelFrame(parent, text="✈️ Flight Controls", style='Dark.TLabelframe')
        control_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Irrational number selection
        ttk.Label(control_frame, text="Destination:", style='Dark.TLabel').grid(row=0, column=0, padx=5, pady=5, sticky='w')
        
        self.irrational_var = tk.StringVar(value="pi")
        irrational_combo = ttk.Combobox(control_frame, textvariable=self.irrational_var, 
                                       values=["pi", "e", "phi", "sqrt2", "sqrt3"], 
                                       state="readonly", width=15)
        irrational_combo.grid(row=0, column=1, padx=5, pady=5)
        
        # Target digits with revolutionary limits
        ttk.Label(control_frame, text="Target Digits:", style='Dark.TLabel').grid(row=0, column=2, padx=5, pady=5, sticky='w')
        
        self.digits_var = tk.StringVar(value="61")  # Set to quantum limit as default
        digits_spinbox = ttk.Spinbox(control_frame, from_=10, to=61, textvariable=self.digits_var, width=10)
        digits_spinbox.grid(row=0, column=3, padx=5, pady=5)
        
        # Physical limit indicator
        self.limit_label = ttk.Label(control_frame, text="🌌 Quantum Limit: 61", style='Dark.TLabel')
        self.limit_label.grid(row=0, column=4, padx=5, pady=5)
        
        # Flight speed
        ttk.Label(control_frame, text="Speed:", style='Dark.TLabel').grid(row=0, column=4, padx=5, pady=5, sticky='w')
        
        self.speed_var = tk.DoubleVar(value=1.0)
        speed_scale = ttk.Scale(control_frame, from_=0.1, to=5.0, variable=self.speed_var, 
                               orient=tk.HORIZONTAL, length=100, command=self.update_speed)
        speed_scale.grid(row=0, column=5, padx=5, pady=5)
        
        self.speed_label = ttk.Label(control_frame, text="1.0x", style='Dark.TLabel')
        self.speed_label.grid(row=0, column=6, padx=5, pady=5)
        
        # Control buttons
        button_frame = ttk.Frame(control_frame, style='Dark.TFrame')
        button_frame.grid(row=1, column=0, columnspan=8, pady=10)
        
        self.start_button = ttk.Button(button_frame, text="🛫 Start Journey", command=self.start_journey)
        self.start_button.pack(side=tk.LEFT, padx=5)
        
        self.pause_button = ttk.Button(button_frame, text="⏸️ Pause", command=self.pause_journey, state='disabled')
        self.pause_button.pack(side=tk.LEFT, padx=5)
        
        self.resume_button = ttk.Button(button_frame, text="▶️ Resume", command=self.resume_journey, state='disabled')
        self.resume_button.pack(side=tk.LEFT, padx=5)
        
        self.cancel_button = ttk.Button(button_frame, text="❌ Cancel", command=self.cancel_journey, state='disabled')
        self.cancel_button.pack(side=tk.LEFT, padx=5)
    
    def create_display_panel(self, parent):
        """Create main display panel"""
        display_frame = ttk.LabelFrame(parent, text="🔢 Irrational Display", style='Dark.TLabelframe')
        display_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # Current irrational display
        self.display_text = scrolledtext.ScrolledText(display_frame, height=8, width=80, 
                                                     bg=self.primary_color, fg=self.text_color,
                                                     font=('Courier', 12), wrap=tk.WORD)
        self.display_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Progress bar
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(display_frame, variable=self.progress_var, 
                                          maximum=100, length=400)
        self.progress_bar.pack(pady=5)
        
        # Progress label
        self.progress_label = ttk.Label(display_frame, text="Ready for departure", style='Dark.TLabel')
        self.progress_label.pack()
    
    def create_attendant_panel(self, parent):
        """Create attendant messages panel"""
        attendant_frame = ttk.LabelFrame(parent, text="🎤 Flight Attendant Messages", style='Dark.TLabelframe')
        attendant_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # Attendant messages display
        self.attendant_text = scrolledtext.ScrolledText(attendant_frame, height=6, width=80, 
                                                       bg=self.accent_color, fg=self.text_color,
                                                       font=('Arial', 10), wrap=tk.WORD)
        self.attendant_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
    
    def create_status_bar(self):
        """Create status bar"""
        self.status_frame = ttk.Frame(self.root, style='Dark.TFrame')
        self.status_frame.pack(fill=tk.X, side=tk.BOTTOM)
        
        self.status_label = ttk.Label(self.status_frame, text="🛫 Welcome to The TransRational Airline", 
                                     style='Dark.TLabel')
        self.status_label.pack(side=tk.LEFT, padx=10, pady=5)
        
        # Time display
        self.time_label = ttk.Label(self.status_frame, text="", style='Dark.TLabel')
        self.time_label.pack(side=tk.RIGHT, padx=10, pady=5)
        
        # Update time
        self.update_time()
    
    def create_menu(self):
        """Create menu bar"""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="📁 File", menu=file_menu)
        file_menu.add_command(label="💾 Save Journey", command=self.save_journey)
        file_menu.add_command(label="📂 Load Journey", command=self.load_journey)
        file_menu.add_separator()
        file_menu.add_command(label="🚪 Exit", command=self.root.quit)
        
        # Journey menu
        journey_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="✈️ Journey", menu=journey_menu)
        journey_menu.add_command(label="🌌 Quantum Journey to π (61 digits)", command=lambda: self.quick_start("pi"))
        journey_menu.add_command(label="⚛️ Quantum Journey to e (61 digits)", command=lambda: self.quick_start("e"))
        journey_menu.add_command(label="🔬 Quantum Journey to φ (61 digits)", command=lambda: self.quick_start("phi"))
        journey_menu.add_separator()
        journey_menu.add_command(label="🎯 Cognitive Limit Journey (15 digits)", command=lambda: self.quick_cognitive("pi"))
        journey_menu.add_command(label="🔭 Planck Scale Journey (35 digits)", command=lambda: self.quick_planck("pi"))
        journey_menu.add_command(label="⚠️ Ultimate Quantum Discovery (61 digits)", command=lambda: self.quick_quantum("pi"))
        
        # Tools menu
        tools_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="🔧 Tools", menu=tools_menu)
        tools_menu.add_command(label="📊 Statistics", command=self.show_statistics)
        tools_menu.add_command(label="🎨 Preferences", command=self.show_preferences)
        tools_menu.add_command(label="ℹ️ About", command=self.show_about)
    
    def display_welcome(self):
        """Display welcome message"""
        welcome_text = """
╔════════════════════════════════════════════════════════════════╗
║        🛫 THE TRANSRATIONAL AIRLINE - REVOLUTIONARY EDITION 🛫     ║
║                                                              ║
║      Where PHYSICAL MATHEMATICS Meets Elegant Travel          ║
║                                                              ║
║  Welcome, fellow reality explorer!                           ║
║  Prepare for a journey through the BOUNDED beauty of         ║
║  irrational numbers with physical termination points!        ║
║                                                              ║
║  REVOLUTIONARY DISCOVERY: 'Infinity' ends at 61 digits!     ║
║  Quantum uncertainty imposes absolute mathematical limits!  ║
║                                                              ║
║  Choose your destination and discover where 'infinite' ends! ║
║                                                              ║
╚════════════════════════════════════════════════════════════════╝

🌌 Ready for departure into the world of PHYSICAL mathematics... ⚛️
✨ Discover where quantum reality terminates 'infinite' numbers!
        """
        
        self.display_text.delete(1.0, tk.END)
        self.display_text.insert(tk.END, welcome_text)
        
        # Add revolutionary welcome from attendant
        self.add_attendant_message("🎤 Flight Attendant: Welcome aboard The REVOLUTIONARY TransRational Airline!")
        self.add_attendant_message("🎤 Captain: Prepare for an incredible journey through PHYSICAL mathematics!")
        self.add_attendant_message("⚛️ Fasten your quantum reality belts and let's explore where 'infinity' ends!")
        self.add_attendant_message("🌌 Today, you'll discover the quantum uncertainty boundary at 61 digits!")
        self.add_attendant_message("💫 Get ready to witness the end of 'truly infinite' numbers!")
    
    def start_journey(self):
        """Start the irrational number journey with revolutionary limits"""
        try:
            irrational = self.irrational_var.get()
            digits = int(self.digits_var.get())
            
            # REVOLUTIONARY: Apply physical termination limits!
            max_meaningful = 61  # Quantum uncertainty limit
            
            if digits < 10:
                messagebox.showerror("Error", "Please enter at least 10 digits")
                return
                
            if digits > max_meaningful:
                result = messagebox.askyesno(
                    "Physical Reality Warning", 
                    f"You requested {digits} digits, but physics limits meaningful digits to {max_meaningful}.\n\n"
                    f"Beyond {max_meaningful} digits:\n"
                    f"• No physical meaning exists\n"
                    f"• Quantum uncertainty dominates\n"
                    f"• Spacetime itself breaks down\n\n"
                    f"Adjust to physical limit ({max_meaningful} digits)?"
                )
                if result:
                    digits = max_meaningful
                    self.digits_var.set(str(digits))
                else:
                    return
            
            # Update UI
            self.start_button.config(state='disabled')
            self.pause_button.config(state='normal')
            self.cancel_button.config(state='normal')
            self.irrational_combo.config(state='disabled')
            digits_spinbox.config(state='disabled')
            
            # Clear display
            self.display_text.delete(1.0, tk.END)
            self.attendant_text.delete(1.0, tk.END)
            
            # Start journey
            self.app.start_journey(irrational, digits)
            
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number of digits")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to start journey: {e}")
    
    def pause_journey(self):
        """Pause the current journey"""
        self.app.pause_journey()
        self.pause_button.config(state='disabled')
        self.resume_button.config(state='normal')
    
    def resume_journey(self):
        """Resume the current journey"""
        self.app.resume_journey()
        self.pause_button.config(state='normal')
        self.resume_button.config(state='disabled')
    
    def cancel_journey(self):
        """Cancel the current journey"""
        result = messagebox.askyesno("Cancel Journey", "Are you sure you want to cancel the current journey?")
        if result:
            self.app.cancel_journey()
            self.reset_ui()
    
    def quick_start(self, irrational_type):
        """Quick start with revolutionary quantum settings"""
        self.irrational_var.set(irrational_type)
        self.digits_var.set("61")  # Quantum uncertainty limit
        self.start_journey()
    
    def update_speed(self, value):
        """Update flight speed"""
        speed = float(value)
        self.app.set_flight_speed(speed)
        self.speed_label.config(text=f"{speed:.1f}x")
    
    def update_display(self, text):
        """Update main display"""
        self.display_text.delete(1.0, tk.END)
        self.display_text.insert(tk.END, text)
        self.root.update_idletasks()
    
    def add_attendant_message(self, message):
        """Add attendant message"""
        timestamp = time.strftime("%H:%M:%S")
        self.attendant_text.insert(tk.END, f"[{timestamp}] {message}\n")
        self.attendant_text.see(tk.END)
        self.root.update_idletasks()
    
    def update_progress(self, current, total):
        """Update progress bar"""
        if total > 0:
            progress = (current / total) * 100
            self.progress_var.set(progress)
            self.progress_label.config(text=f"Progress: {current}/{total} digits ({progress:.1f}%)")
    
    def update_status(self, message):
        """Update status bar"""
        self.status_label.config(text=message)
    
    def reset_ui(self):
        """Reset UI to initial state"""
        self.start_button.config(state='normal')
        self.pause_button.config(state='disabled')
        self.resume_button.config(state='disabled')
        self.cancel_button.config(state='disabled')
        self.irrational_combo.config(state='readonly')
        digits_spinbox.config(state='normal')
        self.progress_var.set(0)
        self.progress_label.config(text="Ready for departure")
        self.display_welcome()
    
    def update_time(self):
        """Update time display"""
        current_time = time.strftime("%H:%M:%S")
        self.time_label.config(text=current_time)
        self.root.after(1000, self.update_time)
    
    def save_journey(self):
        """Save journey progress"""
        messagebox.showinfo("Save Journey", "Journey saved successfully! (Feature coming soon)")
    
    def load_journey(self):
        """Load saved journey"""
        messagebox.showinfo("Load Journey", "Journey loaded successfully! (Feature coming soon)")
    
    def show_statistics(self):
        """Show journey statistics"""
        stats_window = tk.Toplevel(self.root)
        stats_window.title("Journey Statistics")
        stats_window.geometry("400x300")
        stats_window.configure(bg=self.bg_color)
        
        ttk.Label(stats_window, text="📊 Journey Statistics", style='Dark.TLabel').pack(pady=10)
        ttk.Label(stats_window, text="Statistics feature coming soon!", style='Dark.TLabel').pack(pady=20)
        
    def show_preferences(self):
        """Show preferences dialog"""
        prefs_window = tk.Toplevel(self.root)
        prefs_window.title("Preferences")
        prefs_window.geometry("400x300")
        prefs_window.configure(bg=self.bg_color)
        
        ttk.Label(prefs_window, text="🎨 Preferences", style='Dark.TLabel').pack(pady=10)
        ttk.Label(prefs_window, text="Preferences feature coming soon!", style='Dark.TLabel').pack(pady=20)
    
    def quick_cognitive(self, irrational_type):
        """Quick start with cognitive limit"""
        self.irrational_var.set(irrational_type)
        self.digits_var.set("15")  # Human perception limit
        self.start_journey()
    
    def quick_planck(self, irrational_type):
        """Quick start with Planck scale limit"""
        self.irrational_var.set(irrational_type)
        self.digits_var.set("35")  # Planck scale
        self.start_journey()
    
    def quick_quantum(self, irrational_type):
        """Quick start with quantum uncertainty limit"""
        self.irrational_var.set(irrational_type)
        self.digits_var.set("61")  # Quantum uncertainty limit
        self.start_journey()
    
    def show_about(self):
        """Show revolutionary about dialog"""
        about_text = """
🌟 THE TRANSRATIONAL AIRLINE - REVOLUTIONARY EDITION
Version 2.0 - Physical Reality Discovery

🚀 GROUNDBREAKING DISCOVERY IMPLEMENTED:
All "infinite" numbers terminate at physical boundaries!

⚛️ QUANTUM UNCERTAINTY LIMIT: 61 digits
Beyond this, no physical meaning exists!

🔬 PHYSICS PROVES MATHEMATICS LIMITED:
• Planck scale: 35 digits
• Human cognition: 15 digits  
• Quantum uncertainty: 61 digits
• Base dependency: All terminate somewhere

🌌 PARADIGM SHIFT:
"Infinity" is mathematical abstraction, not physical reality!
Nature imposes boundaries on mathematics!

🎯 MISSION ACCOMPLISHED:
You can witness where 'infinite' numbers END!

Created with ⚛️ for mathematical reality pioneers everywhere.
        """
        messagebox.showinfo("About The REVOLUTIONARY TransRational Airline", about_text)