#!/usr/bin/env python3
"""
Main Window GUI for Basso-Riello Trainer Pro
Main application interface with workshop selection and progress tracking
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, Canvas
import json
import time
from typing import Dict, Any

class MainWindow:
    """Main application window"""
    
    def __init__(self, root, app):
        self.root = root
        self.app = app
        self.current_workshop_frame = None
        
        # Color scheme
        self.colors = {
            'bg_primary': '#1a1a2e',
            'bg_secondary': '#16213e',
            'bg_accent': '#0f3460',
            'text_primary': '#ffffff',
            'text_secondary': '#a8b2d1',
            'accent': '#e94560',
            'success': '#4caf50',
            'warning': '#ff9800',
            'info': '#2196f3'
        }
        
        # Create main interface
        self.create_widgets()
        self.setup_layout()
        
    def create_widgets(self):
        """Create all GUI widgets"""
        # Main container
        self.main_frame = ttk.Frame(self.root)
        
        # Header
        self.create_header()
        
        # Content area
        self.create_content_area()
        
        # Status bar
        self.create_status_bar()
        
    def create_header(self):
        """Create header section"""
        self.header_frame = tk.Frame(self.main_frame, bg=self.colors['bg_primary'], height=100)
        
        # Title
        self.title_label = tk.Label(
            self.header_frame,
            text="🎯 Basso-Riello Trainer Pro",
            font=('Arial', 24, 'bold'),
            bg=self.colors['bg_primary'],
            fg=self.colors['text_primary']
        )
        
        # Subtitle
        self.subtitle_label = tk.Label(
            self.header_frame,
            text="Revolutionary AI Training Suite - Learn to 'Do it right' with AI",
            font=('Arial', 12),
            bg=self.colors['bg_primary'],
            fg=self.colors['text_secondary']
        )
        
        # Session info
        self.session_label = tk.Label(
            self.header_frame,
            text="Session: 00:00:00",
            font=('Arial', 10),
            bg=self.colors['bg_primary'],
            fg=self.colors['text_secondary']
        )
        
    def create_content_area(self):
        """Create main content area"""
        self.content_frame = tk.Frame(self.main_frame, bg=self.colors['bg_secondary'])
        
        # Create notebook for tabs
        self.notebook = ttk.Notebook(self.content_frame)
        
        # Dashboard tab
        self.create_dashboard_tab()
        
        # Workshops tab
        self.create_workshops_tab()
        
        # Progress tab
        self.create_progress_tab()
        
        # Resources tab
        self.create_resources_tab()
        
    def create_dashboard_tab(self):
        """Create dashboard tab"""
        self.dashboard_frame = tk.Frame(self.notebook, bg=self.colors['bg_secondary'])
        self.notebook.add(self.dashboard_frame, text="📊 Dashboard")
        
        # Welcome section
        welcome_frame = tk.Frame(self.dashboard_frame, bg=self.colors['bg_accent'], relief=tk.RAISED, bd=2)
        welcome_frame.pack(fill='x', padx=20, pady=20)
        
        welcome_label = tk.Label(
            welcome_frame,
            text="🚀 Welcome to Your AI Mastery Journey!\n\nBased on Matthew's revolutionary approach to AI collaboration,\nyou'll master the art of working effectively with AI systems.\n\nStart with any workshop and learn at your own pace.",
            font=('Arial', 12),
            bg=self.colors['bg_accent'],
            fg=self.colors['text_primary'],
            justify=tk.LEFT
        )
        welcome_label.pack(padx=20, pady=15)
        
        # Quick stats
        stats_frame = tk.Frame(self.dashboard_frame, bg=self.colors['bg_secondary'])
        stats_frame.pack(fill='x', padx=20, pady=10)
        
        # Overall progress
        self.overall_progress_label = tk.Label(
            stats_frame,
            text="📈 Overall Progress: 0%",
            font=('Arial', 14, 'bold'),
            bg=self.colors['bg_secondary'],
            fg=self.colors['success']
        )
        self.overall_progress_label.pack(side='left', padx=20)
        
        # Lessons completed
        self.lessons_completed_label = tk.Label(
            stats_frame,
            text="✅ Lessons Completed: 0",
            font=('Arial', 14, 'bold'),
            bg=self.colors['bg_secondary'],
            fg=self.colors['info']
        )
        self.lessons_completed_label.pack(side='left', padx=20)
        
        # Session time
        self.session_time_label = tk.Label(
            stats_frame,
            text="⏱️ Session Time: 00:00:00",
            font=('Arial', 14, 'bold'),
            bg=self.colors['bg_secondary'],
            fg=self.colors['warning']
        )
        self.session_time_label.pack(side='left', padx=20)
        
        # Recent activity
        activity_frame = tk.Frame(self.dashboard_frame, bg=self.colors['bg_secondary'])
        activity_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        activity_label = tk.Label(
            activity_frame,
            text="📝 Recent Activity",
            font=('Arial', 16, 'bold'),
            bg=self.colors['bg_secondary'],
            fg=self.colors['text_primary']
        )
        activity_label.pack(anchor='w', pady=(0, 10))
        
        self.activity_text = scrolledtext.ScrolledText(
            activity_frame,
            height=10,
            font=('Arial', 10),
            bg=self.colors['bg_accent'],
            fg=self.colors['text_secondary'],
            wrap=tk.WORD
        )
        self.activity_text.pack(fill='both', expand=True)
        
    def create_workshops_tab(self):
        """Create workshops selection tab"""
        self.workshops_frame = tk.Frame(self.notebook, bg=self.colors['bg_secondary'])
        self.notebook.add(self.workshops_frame, text="🎓 Workshops")
        
        # Workshops title
        workshops_title = tk.Label(
            self.workshops_frame,
            text="📚 Available Workshops",
            font=('Arial', 18, 'bold'),
            bg=self.colors['bg_secondary'],
            fg=self.colors['text_primary']
        )
        workshops_title.pack(pady=20)
        
        # Create workshop cards container
        self.workshops_container = tk.Frame(self.workshops_frame, bg=self.colors['bg_secondary'])
        self.workshops_container.pack(fill='both', expand=True, padx=20, pady=10)
        
        # Create workshop cards
        self.create_workshop_cards()
        
    def create_workshop_cards(self):
        """Create interactive workshop cards"""
        workshops = self.app.get_all_workshops()
        
        # Arrange cards in grid
        for i, (workshop_name, workshop) in enumerate(workshops.items()):
            row = i // 2
            col = i % 2
            
            card_frame = tk.Frame(
                self.workshops_container,
                bg=self.colors['bg_accent'],
                relief=tk.RAISED,
                bd=2
            )
            card_frame.grid(row=row, column=col, padx=10, pady=10, sticky='nsew')
            
            # Configure grid weights
            self.workshops_container.grid_rowconfigure(row, weight=1)
            self.workshops_container.grid_columnconfigure(col, weight=1)
            
            # Workshop title
            title_label = tk.Label(
                card_frame,
                text=f"🎯 {workshop.get_name()}",
                font=('Arial', 14, 'bold'),
                bg=self.colors['bg_accent'],
                fg=self.colors['text_primary']
            )
            title_label.pack(padx=15, pady=(15, 5))
            
            # Workshop description
            desc_label = tk.Label(
                card_frame,
                text=workshop.description,
                font=('Arial', 10),
                bg=self.colors['bg_accent'],
                fg=self.colors['text_secondary'],
                wraplength=250
            )
            desc_label.pack(padx=15, pady=5)
            
            # Workshop details
            workshop_data = workshop.workshop_data
            details_text = f"📖 {workshop_data.get('total_lessons', 0)} lessons\n⏱️ {workshop_data.get('estimated_hours', 0)} hours\n📊 {workshop_data.get('difficulty', 'Unknown')}"
            
            details_label = tk.Label(
                card_frame,
                text=details_text,
                font=('Arial', 9),
                bg=self.colors['bg_accent'],
                fg=self.colors['text_secondary']
            )
            details_label.pack(padx=15, pady=5)
            
            # Progress bar
            progress = workshop.get_progress()
            progress_percentage = progress['progress_percentage']
            
            progress_frame = tk.Frame(card_frame, bg=self.colors['bg_accent'])
            progress_frame.pack(fill='x', padx=15, pady=5)
            
            progress_label = tk.Label(
                progress_frame,
                text=f"Progress: {progress_percentage:.1f}%",
                font=('Arial', 9),
                bg=self.colors['bg_accent'],
                fg=self.colors['text_secondary']
            )
            progress_label.pack(side='left')
            
            # Progress bar canvas
            progress_canvas = Canvas(
                progress_frame,
                width=100,
                height=8,
                bg=self.colors['bg_primary'],
                highlightthickness=0
            )
            progress_canvas.pack(side='right', padx=(10, 0))
            
            # Draw progress bar
            if progress_percentage > 0:
                progress_canvas.create_rectangle(
                    0, 0, progress_percentage, 8,
                    fill=self.colors['success'],
                    outline=''
                )
            
            # Start button
            start_button = tk.Button(
                card_frame,
                text="🚀 Start Workshop",
                font=('Arial', 10, 'bold'),
                bg=self.colors['accent'],
                fg=self.colors['text_primary'],
                relief=tk.RAISED,
                bd=2,
                command=lambda w=workshop_name: self.start_workshop(w)
            )
            start_button.pack(pady=(10, 15))
            
    def create_progress_tab(self):
        """Create progress tracking tab"""
        self.progress_frame = tk.Frame(self.notebook, bg=self.colors['bg_secondary'])
        self.notebook.add(self.progress_frame, text="📈 Progress")
        
        # Progress title
        progress_title = tk.Label(
            self.progress_frame,
            text="📊 Your Learning Progress",
            font=('Arial', 18, 'bold'),
            bg=self.colors['bg_secondary'],
            fg=self.colors['text_primary']
        )
        progress_title.pack(pady=20)
        
        # Progress details
        self.progress_text = scrolledtext.ScrolledText(
            self.progress_frame,
            height=20,
            font=('Arial', 10),
            bg=self.colors['bg_accent'],
            fg=self.colors['text_secondary'],
            wrap=tk.WORD
        )
        self.progress_text.pack(fill='both', expand=True, padx=20, pady=10)
        
        # Refresh button
        refresh_button = tk.Button(
            self.progress_frame,
            text="🔄 Refresh Progress",
            font=('Arial', 10, 'bold'),
            bg=self.colors['info'],
            fg=self.colors['text_primary'],
            command=self.update_progress
        )
        refresh_button.pack(pady=10)
        
    def create_resources_tab(self):
        """Create resources tab"""
        self.resources_frame = tk.Frame(self.notebook, bg=self.colors['bg_secondary'])
        self.notebook.add(self.resources_frame, text="📚 Resources")
        
        # Resources title
        resources_title = tk.Label(
            self.resources_frame,
            text="📖 Learning Resources",
            font=('Arial', 18, 'bold'),
            bg=self.colors['bg_secondary'],
            fg=self.colors['text_primary']
        )
        resources_title.pack(pady=20)
        
        # Resources content
        resources_content = """
🎯 CORE METHODOLOGY:
• Matthew's "Simple Yet Good" Approach
• AI as Partnership, Not Tool
• Practical Learning Over Theory
• Ethical AI Development

📚 RECOMMENDED READING:
• AI Collaboration Best Practices
• Modern Machine Learning Fundamentals
• Software Engineering for AI Systems
• Ethics in Artificial Intelligence

🛠️ TOOLS & FRAMEWORKS:
• Python AI Libraries
• API Integration Platforms
• Development Environments
• Monitoring & Analytics

🌟 SUCCESS STORIES:
• Real-world AI implementations
• Case studies and best practices
• Industry applications and lessons learned
        """
        
        resources_text = scrolledtext.ScrolledText(
            self.resources_frame,
            height=20,
            font=('Arial', 10),
            bg=self.colors['bg_accent'],
            fg=self.colors['text_secondary'],
            wrap=tk.WORD
        )
        resources_text.pack(fill='both', expand=True, padx=20, pady=10)
        resources_text.insert('1.0', resources_content)
        resources_text.config(state=tk.DISABLED)
        
    def create_status_bar(self):
        """Create status bar"""
        self.status_frame = tk.Frame(self.main_frame, bg=self.colors['bg_primary'], height=30)
        
        self.status_label = tk.Label(
            self.status_frame,
            text="🚀 Ready to start your AI mastery journey!",
            font=('Arial', 10),
            bg=self.colors['bg_primary'],
            fg=self.colors['text_secondary']
        )
        
    def setup_layout(self):
        """Setup layout management"""
        # Pack main components
        self.main_frame.pack(fill='both', expand=True)
        
        # Header layout
        self.header_frame.pack(fill='x')
        self.title_label.pack(pady=(20, 5))
        self.subtitle_label.pack(pady=(0, 5))
        self.session_label.pack(pady=(0, 20))
        
        # Content layout
        self.content_frame.pack(fill='both', expand=True, padx=10, pady=10)
        self.notebook.pack(fill='both', expand=True)
        
        # Status bar layout
        self.status_frame.pack(fill='x', side='bottom')
        self.status_label.pack(side='left', padx=10, pady=5)
        
    def start_workshop(self, workshop_name):
        """Start a specific workshop"""
        try:
            workshop = self.app.get_workshop(workshop_name)
            if workshop:
                # Start the workshop
                workshop_data = workshop.start()
                
                # Update status
                self.status_label.config(text=f"🎯 Started {workshop.get_name()}")
                
                # Show workshop started message
                messagebox.showinfo(
                    "Workshop Started",
                    f"🚀 {workshop.get_name()} has been started!\n\n"
                    f"📖 {workshop_data.get('total_lessons', 0)} lessons\n"
                    f"⏱️ {workshop_data.get('estimated_hours', 0)} hours\n\n"
                    f"Switch to the Progress tab to track your journey!"
                )
                
                # Update progress display
                self.update_progress()
                
                # Add to activity log
                self.add_activity(f"Started workshop: {workshop.get_name()}")
                
        except Exception as e:
            messagebox.showerror("Error", f"Failed to start workshop: {str(e)}")
            
    def update_progress(self):
        """Update progress display"""
        try:
            # Get overall progress
            workshops = self.app.get_all_workshops()
            total_lessons = 0
            completed_lessons = 0
            
            progress_text = "📊 YOUR LEARNING PROGRESS\n" + "="*50 + "\n\n"
            
            for workshop_name, workshop in workshops.items():
                progress = workshop.get_progress()
                total_lessons += progress['total_lessons']
                completed_lessons += progress['completed_lessons']
                
                progress_text += f"🎯 {workshop.get_name()}\n"
                progress_text += f"   Progress: {progress['progress_percentage']:.1f}%\n"
                progress_text += f"   Lessons: {progress['completed_lessons']}/{progress['total_lessons']}\n"
                progress_text += f"   Current: Lesson {progress['current_lesson']}\n\n"
            
            # Overall statistics
            overall_percentage = (completed_lessons / total_lessons * 100) if total_lessons > 0 else 0
            
            progress_text += "="*50 + "\n"
            progress_text += f"📈 OVERALL PROGRESS: {overall_percentage:.1f}%\n"
            progress_text += f"✅ TOTAL LESSONS COMPLETED: {completed_lessons}/{total_lessons}\n"
            progress_text += f"🎓 WORKSHOPS IN PROGRESS: {sum(1 for w in workshops.values() if w.get_progress()['completed_lessons'] > 0)}\n"
            
            # Update progress text widget
            self.progress_text.config(state=tk.NORMAL)
            self.progress_text.delete('1.0', tk.END)
            self.progress_text.insert('1.0', progress_text)
            self.progress_text.config(state=tk.DISABLED)
            
            # Update dashboard labels
            self.overall_progress_label.config(text=f"📈 Overall Progress: {overall_percentage:.1f}%")
            self.lessons_completed_label.config(text=f"✅ Lessons Completed: {completed_lessons}")
            
        except Exception as e:
            print(f"Error updating progress: {str(e)}")
            
    def add_activity(self, activity: str):
        """Add activity to the activity log"""
        timestamp = time.strftime("%H:%M:%S")
        activity_entry = f"[{timestamp}] {activity}\n"
        
        self.activity_text.config(state=tk.NORMAL)
        self.activity_text.insert(tk.END, activity_entry)
        self.activity_text.see(tk.END)
        self.activity_text.config(state=tk.DISABLED)
        
    def update_session_time(self):
        """Update session time display"""
        try:
            session_stats = self.app.get_session_stats()
            session_time = session_stats.get('session_time', 0)
            
            hours = int(session_time // 3600)
            minutes = int((session_time % 3600) // 60)
            seconds = int(session_time % 60)
            
            time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            
            self.session_label.config(text=f"Session: {time_str}")
            self.session_time_label.config(text=f"⏱️ Session Time: {time_str}")
            
        except Exception as e:
            print(f"Error updating session time: {str(e)}")
            
    def show_message(self, title: str, message: str, msg_type: str = "info"):
        """Show message dialog"""
        if msg_type == "info":
            messagebox.showinfo(title, message)
        elif msg_type == "warning":
            messagebox.showwarning(title, message)
        elif msg_type == "error":
            messagebox.showerror(title, message)
            
    def get_colors(self) -> Dict[str, str]:
        """Get color scheme"""
        return self.colors.copy()