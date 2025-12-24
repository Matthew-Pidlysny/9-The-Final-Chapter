#!/usr/bin/env python3
"""
Basso-Riello Trainer Pro
Revolutionary AI Training Suite

Based on Matthew Pidlysny's Cradle methodology and "simple yet good" approach
Teaches people to collaborate effectively with AI and "Do it right"

Author: SuperNinja AI (with Matthew's guidance)
Mission: Create the ultimate AI training experience
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, filedialog
import sys
import os
import json
import time
from pathlib import Path

# Add src to path
sys.path.insert(0, os.path.dirname(__file__))

from gui.main_window import MainWindow
from core.progress_tracker import ProgressTracker
from content.content_manager import ContentManager
from workshops.variant_training import VariantTrainingWorkshop
from workshops.pseudolanguage_modeler import PseudolanguageModeler
from workshops.ai_playground import AIPlayground
from workshops.organizational_development import OrganizationalDevelopment
from workshops.advanced_integration import AdvancedIntegrationWorkshop

class BassoRielloTrainerPro:
    """Main application class for Basso-Riello Trainer Pro"""
    
    def __init__(self):
        self.app_name = "Basso-Riello Trainer Pro"
        self.version = "1.0.0"
        self.root = None
        self.main_window = None
        self.progress_tracker = ProgressTracker()
        self.content_manager = ContentManager()
        
        # Initialize workshops
        self.workshops = {
            'variant_training': VariantTrainingWorkshop(self.progress_tracker, self.content_manager),
            'pseudolanguage_modeler': PseudolanguageModeler(self.progress_tracker),
            'ai_playground': AIPlayground(self.progress_tracker),
            'organizational_development': OrganizationalDevelopment(self.progress_tracker),
            'advanced_integration': AdvancedIntegrationWorkshop(self.progress_tracker)
        }
        
        # Application state
        self.current_workshop = None
        self.user_data = {}
        self.session_start_time = time.time()
        
    def initialize(self):
        """Initialize the application"""
        try:
            print(f"🚀 Initializing {self.app_name} v{self.version}...")
            
            # Create main window
            self.root = tk.Tk()
            self.root.title(f"{self.app_name} v{self.version}")
            self.root.geometry("1400x900")
            self.root.configure(bg='#1a1a2e')
            
            # Create main window GUI
            self.main_window = MainWindow(self.root, self)
            
            # Initialize components
            self.progress_tracker.initialize()
            self.content_manager.initialize()
            
            # Load user data if exists
            self.load_user_data()
            
            print("✅ Initialization complete!")
            return True
            
        except Exception as e:
            print(f"❌ Initialization failed: {e}")
            return False
    
    def run(self):
        """Run the application"""
        try:
            if not self.initialize():
                messagebox.showerror("Error", f"Failed to initialize {self.app_name}")
                return
            
            print(f"🎯 Starting {self.app_name}...")
            self.root.mainloop()
            
        except KeyboardInterrupt:
            print("👋 Application interrupted by user")
        except Exception as e:
            print(f"💥 Application error: {e}")
            messagebox.showerror("Error", f"An error occurred: {e}")
        finally:
            self.cleanup()
    
    def start_workshop(self, workshop_name):
        """Start a specific workshop"""
        if workshop_name in self.workshops:
            self.current_workshop = self.workshops[workshop_name]
            self.current_workshop.start()
        else:
            messagebox.showerror("Error", f"Workshop '{workshop_name}' not found")
    
    def get_workshop(self, workshop_name):
        """Get a specific workshop"""
        return self.workshops.get(workshop_name)
    
    def get_all_workshops(self):
        """Get all available workshops"""
        return self.workshops
    
    def save_user_data(self):
        """Save user progress and data"""
        try:
            data = {
                'progress': self.progress_tracker.get_all_progress(),
                'session_time': time.time() - self.session_start_time,
                'completed_lessons': self.progress_tracker.get_completed_lessons(),
                'achievements': self.progress_tracker.get_achievements(),
                'workshop_progress': {name: ws.get_progress() for name, ws in self.workshops.items()}
            }
            
            with open('user_data.json', 'w') as f:
                json.dump(data, f, indent=2)
            
            print("💾 User data saved successfully")
            
        except Exception as e:
            print(f"❌ Failed to save user data: {e}")
    
    def load_user_data(self):
        """Load user progress and data"""
        try:
            if os.path.exists('user_data.json'):
                with open('user_data.json', 'r') as f:
                    data = json.load(f)
                
                self.progress_tracker.load_progress(data.get('progress', {}))
                self.user_data = data
                print("📂 User data loaded successfully")
            
        except Exception as e:
            print(f"❌ Failed to load user data: {e}")
    
    def get_session_stats(self):
        """Get current session statistics"""
        return {
            'session_time': time.time() - self.session_start_time,
            'total_progress': self.progress_tracker.get_overall_progress(),
            'completed_lessons': len(self.progress_tracker.get_completed_lessons()),
            'active_workshop': self.current_workshop.get_name() if self.current_workshop else None
        }
    
    def cleanup(self):
        """Clean up resources"""
        try:
            print("🧹 Cleaning up resources...")
            self.save_user_data()
            
            # Cleanup workshops
            for workshop in self.workshops.values():
                workshop.cleanup()
            
            # Cleanup components
            self.progress_tracker.cleanup()
            self.content_manager.cleanup()
            
            print("✅ Cleanup complete")
            
        except Exception as e:
            print(f"❌ Cleanup error: {e}")

def main():
    """Main entry point"""
    print("🌟 Welcome to Basso-Riello Trainer Pro!")
    print("🤖 The Ultimate AI Training Suite")
    print("📚 Based on Matthew's revolutionary AI collaboration methodology")
    print("=" * 60)
    print("🎯 Learning to 'Do it right' with AI...")
    print("🚀 Let's begin your AI mastery journey!")
    print("=" * 60)
    
    app = BassoRielloTrainerPro()
    app.run()

if __name__ == "__main__":
    main()