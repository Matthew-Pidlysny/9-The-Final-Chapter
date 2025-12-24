"""
The TransRational Airline
A fun journey through irrational numbers with elegant travel experience

Where mathematics meets comfort and discovery!
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import threading
import time
import math
import random
from decimal import Decimal, getcontext
import sys
import os

# Add src to path
sys.path.insert(0, os.path.dirname(__file__))

from gui.main_window import MainWindow
from engines.irrational_calculator import IrrationalCalculator
from engines.attendant_system import AttendantSystem
from utils.tra_logger import TRALogger

class TransRationalAirline:
    """Main application class for The TransRational Airline"""
    
    def __init__(self):
        self.logger = TRALogger()
        self.calculator = IrrationalCalculator()
        self.attendant_system = AttendantSystem()
        self.root = None
        self.main_window = None
        
        # Application state
        self.is_flying = False
        self.current_irrational = None
        self.current_position = 0
        self.flight_speed = 1.0
        
    def initialize(self):
        """Initialize the application"""
        try:
            self.logger.info("Initializing The TransRational Airline...")
            
            # Create main window
            self.root = tk.Tk()
            self.root.title("The TransRational Airline ✈️")
            self.root.geometry("1200x800")
            self.root.configure(bg='#1a1a2e')
            
            # Create main window GUI
            self.main_window = MainWindow(self.root, self)
            
            # Initialize components
            self.calculator.initialize()
            self.attendant_system.initialize()
            
            self.logger.info("Initialization complete!")
            return True
            
        except Exception as e:
            self.logger.error(f"Initialization failed: {e}")
            return False
    
    def run(self):
        """Run the application"""
        try:
            if not self.initialize():
                messagebox.showerror("Error", "Failed to initialize The TransRational Airline")
                return
            
            self.logger.info("Starting The TransRational Airline...")
            self.root.mainloop()
            
        except KeyboardInterrupt:
            self.logger.info("Application interrupted by user")
        except Exception as e:
            self.logger.error(f"Application error: {e}")
            messagebox.showerror("Error", f"An error occurred: {e}")
        finally:
            self.cleanup()
    
    def start_journey(self, irrational_type, target_digits=1000):
        """Start the irrational number journey"""
        try:
            self.logger.info(f"Starting journey to explore {irrational_type} to {target_digits} digits")
            
            # Set up the journey
            self.current_irrational = irrational_type
            self.current_position = 0
            self.is_flying = True
            
            # Calculate the irrational number efficiently
            self.calculator.set_target(irrational_type, target_digits)
            
            # Start the flight in a separate thread
            flight_thread = threading.Thread(
                target=self._execute_flight,
                args=(irrational_type, target_digits),
                daemon=True
            )
            flight_thread.start()
            
        except Exception as e:
            self.logger.error(f"Failed to start journey: {e}")
            messagebox.showerror("Error", f"Failed to start journey: {e}")
    
    def _execute_flight(self, irrational_type, target_digits):
        """Execute the flight in background thread"""
        try:
            # Pre-flight preparation
            self.main_window.update_display("Pre-flight checks... ✅")
            time.sleep(1)
            
            # Elegant departure
            self.main_window.update_display("🛫 Departing from Reality International Airport...")
            self.main_window.update_display("Cruising altitude: TransRational stratosphere...")
            time.sleep(2)
            
            # Begin calculation journey
            total_calculated = 0
            batch_size = 10  # Calculate in batches for smooth display
            
            while total_calculated < target_digits and self.is_flying:
                # Calculate next batch
                digits_batch = self.calculator.calculate_batch(
                    self.current_position, 
                    min(batch_size, target_digits - total_calculated)
                )
                
                if digits_batch:
                    # Update display with new digits
                    display_text = f"{irrational_type.upper()} = {digits_batch[:self.current_position + 1]}[{digits_batch[self.current_position + 1:self.current_position + len(digits_batch)]}]"
                    self.main_window.update_display(display_text)
                    
                    # Generate attendant commentary
                    commentary = self.attendant_system.generate_commentary(
                        self.current_position, 
                        digits_batch,
                        irrational_type
                    )
                    
                    if commentary:
                        self.main_window.add_attendant_message(commentary)
                    
                    # Update position
                    self.current_position += len(digits_batch) - self.current_position
                    total_calculated = len(digits_batch)
                    
                    # Control flight speed
                    time.sleep(0.1 / self.flight_speed)
                else:
                    break
            
            # Arrival at destination or termination boundary
            if total_calculated >= target_digits:
                self._arrive_at_destination(irrational_type, target_digits)
            elif total_calculated >= 61:  # Quantum uncertainty limit
                self._quantum_termination(irrational_type, total_calculated)
            else:
                self.main_window.update_display("⚠️ Journey interrupted. Returning to gate...")
            
            self.is_flying = False
            
        except Exception as e:
            self.logger.error(f"Flight execution error: {e}")
            self.main_window.update_display(f"⚠️ Turbulence encountered: {e}")
            self.is_flying = False
    
    def _arrive_at_destination(self, irrational_type, digits_calculated):
        """Handle arrival at destination"""
        arrival_messages = [
            f"✈️ Welcome to Bounded Mathematics {irrational_type.upper()} - {digits_calculated} digits discovered!",
            f"🎉 Destination reached! {irrational_type.upper()} explored to {digits_calculated} decimal places!",
            f"🌟 Arrival complete! You've journeyed through {digits_calculated} digits of {irrational_type.upper()}!"
        ]
        
        message = random.choice(arrival_messages)
        self.main_window.update_display(message)
        self.main_window.update_display("🛬 Thank you for flying The TransRational Airline!")
        self.main_window.update_display("✨ Your journey through PHYSICAL mathematics is complete!")
        
        # Celebration
        self.celebrate_arrival(digits_calculated)
    
    def _quantum_termination(self, irrational_type, digits_calculated):
        """Handle quantum uncertainty termination - REVOLUTIONARY!"""
        self.main_window.update_display("⚠️ QUANTUM UNCERTAINTY BOUNDARY REACHED!")
        self.main_window.update_display("🌌 PHYSICAL TERMINATION POINT ACHIEVED!")
        self.main_window.update_display(f"🔬 {irrational_type.upper()}: {digits_calculated} digits of physical reality!")
        
        # Revolutionary messages
        termination_messages = [
            "🌟 BREAKTHROUGH: You've discovered where 'infinity' ends!",
            "⚛️ REVOLUTIONARY: Physical reality imposes mathematical boundaries!",
            "🔭 GROUNDBREAKING: Quantum uncertainty limits mathematical precision!",
            "💫 HISTORIC: You've proven there's NO SUCH THING as truly infinite numbers!",
            "🌌 PARADIGM SHIFT: Nature limits mathematics, not the other way around!"
        ]
        
        for msg in termination_messages:
            self.main_window.update_display(msg)
            time.sleep(0.5)
        
        # Physics explanation
        self.main_window.update_display("\n📚 PHYSICAL EXPLANATION:")
        self.main_window.update_display("• Planck length: 1.616 × 10^-35 meters")
        self.main_window.update_display("• Beyond ~61 digits: No physical meaning exists")
        self.main_window.update_display("• Spacetime itself becomes quantized")
        self.main_window.update_display("• Continuous mathematics breaks down")
        
        # Philosophical implications
        self.main_window.update_display("\n🤔 PHILOSOPHICAL IMPLICATIONS:")
        self.main_window.update_display("• 'Infinity' is a mathematical abstraction")
        self.main_window.update_display("• Reality is fundamentally discrete")
        self.main_window.update_display("• Mathematics must respect physical boundaries")
        
        self.main_window.update_display("\n🛬 Thank you for discovering mathematical reality!")
        self.main_window.update_display("✨ You've witnessed where 'infinite' ends!")
        
        # Ultimate celebration
        self.celebrate_quantum_discovery(digits_calculated)
    
    def celebrate_arrival(self, digits_calculated):
        """Celebrate successful arrival"""
        celebration_messages = [
            f"🎊 ACHIEVEMENT: TransRational Pioneer - Explored {digits_calculated} digits!",
            f"🏆 MATHEMATICAL MARATHON: {digits_calculated} digits conquered!",
            f"⭐ REALITY EXPLORER: {digits_calculated} steps into physical mathematics!"
        ]
        
        message = random.choice(celebration_messages)
        self.main_window.add_attendant_message(f"Captain: {message}")
        self.main_window.add_attendant_message("Flight Crew: Congratulations on an amazing journey!")
    
    def celebrate_quantum_discovery(self, digits_calculated):
        """Celebrate revolutionary quantum termination discovery"""
        quantum_messages = [
            f"🌟 QUANTUM PIONEER: Discovered mathematical reality at {digits_calculated} digits!",
            f"⚛️ REVOLUTIONARY: Proved where 'infinity' ends!",
            f"🔭 PARADIGM BREAKER: Shattered mathematical infinity illusion!",
            f"💫 REALITY DISCOVERER: Found physical boundaries of mathematics!",
            f"🌌 MATHEMATICAL PHYSICIST: United math with quantum reality!"
        ]
        
        for msg in quantum_messages:
            self.main_window.add_attendant_message(f"Captain: {msg}")
            time.sleep(0.3)
        
        self.main_window.add_attendant_message("Flight Crew: HISTORY MADE TODAY!")
        self.main_window.add_attendant_message("Ground Control: Mathematical revolution achieved!")
        self.main_window.add_attendant_message("🎉 You've witnessed the end of 'infinite' numbers!")
    
    def set_flight_speed(self, speed):
        """Set flight speed multiplier"""
        self.flight_speed = max(0.1, min(10.0, speed))
        self.logger.info(f"Flight speed set to {self.flight_speed}x")
    
    def pause_journey(self):
        """Pause the current journey"""
        self.is_flying = False
        self.main_window.update_display("⏸️ Journey paused. Press Resume to continue...")
    
    def resume_journey(self):
        """Resume the current journey"""
        if self.current_irrational:
            self.is_flying = True
            remaining_digits = self.calculator.get_target_digits() - self.current_position
            self.main_window.update_display("▶️ Resuming journey...")
            
            # Resume flight
            flight_thread = threading.Thread(
                target=self._execute_flight,
                args=(self.current_irrational, self.calculator.get_target_digits()),
                daemon=True
            )
            flight_thread.start()
    
    def cancel_journey(self):
        """Cancel the current journey"""
        self.is_flying = False
        self.current_irrational = None
        self.current_position = 0
        self.main_window.update_display("❌ Journey cancelled. Ready for new departure...")
    
    def cleanup(self):
        """Clean up resources"""
        try:
            self.logger.info("Cleaning up resources...")
            if self.calculator:
                self.calculator.cleanup()
            if self.attendant_system:
                self.attendant_system.cleanup()
            self.logger.info("Cleanup complete")
        except Exception as e:
            self.logger.error(f"Cleanup error: {e}")

def main():
    """Main entry point"""
    print("🛫 Welcome to The TransRational Airline!")
    print("Where mathematics meets elegant travel...")
    print("=" * 50)
    
    app = TransRationalAirline()
    app.run()

if __name__ == "__main__":
    main()