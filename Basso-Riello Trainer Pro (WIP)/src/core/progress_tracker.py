"""
Progress Tracker for Basso-Riello Trainer Pro
Tracks user progress, achievements, and learning metrics
"""

import json
import time
from typing import Dict, List, Set
from datetime import datetime

class ProgressTracker:
    """Comprehensive progress tracking system"""
    
    def __init__(self):
        self.progress_data = {}
        self.completed_lessons = set()
        self.achievements = []
        self.session_start = time.time()
        self.learning_metrics = {
            'total_time_spent': 0,
            'lessons_completed': 0,
            'exercises_attempted': 0,
            'exercises_completed': 0,
            'workshops_started': set(),
            'workshops_completed': set(),
            'skill_levels': {},
            'streak_days': 0,
            'last_activity': None
        }
    
    def initialize(self):
        """Initialize the progress tracker"""
        self.load_progress()
    
    def mark_lesson_completed(self, workshop_name: str, lesson_id: str, lesson_title: str):
        """Mark a lesson as completed"""
        lesson_key = f"{workshop_name}_{lesson_id}"
        
        if lesson_key not in self.completed_lessons:
            self.completed_lessons.add(lesson_key)
            self.learning_metrics['lessons_completed'] += 1
            
            # Update workshop progress
            if workshop_name not in self.progress_data:
                self.progress_data[workshop_name] = {'completed_lessons': [], 'total_lessons': 0, 'progress_percent': 0}
            
            self.progress_data[workshop_name]['completed_lessons'].append({
                'id': lesson_id,
                'title': lesson_title,
                'completed_at': datetime.now().isoformat(),
                'time_spent': 0
            })
            
            self._update_workshop_progress(workshop_name)
            self._check_achievements()
            
            print(f"✅ Lesson completed: {lesson_title}")
            return True
        
        return False
    
    def _update_workshop_progress(self, workshop_name: str):
        """Update workshop progress percentage"""
        if workshop_name in self.progress_data:
            completed = len(self.progress_data[workshop_name]['completed_lessons'])
            total = self.progress_data[workshop_name]['total_lessons']
            
            if total > 0:
                progress = (completed / total) * 100
                self.progress_data[workshop_name]['progress_percent'] = progress
                
                # Check if workshop is completed
                if progress >= 100:
                    self.learning_metrics['workshops_completed'].add(workshop_name)
                    print(f"🎉 Workshop completed: {workshop_name}")
    
    def set_workshop_total_lessons(self, workshop_name: str, total_lessons: int):
        """Set total number of lessons for a workshop"""
        if workshop_name not in self.progress_data:
            self.progress_data[workshop_name] = {'completed_lessons': [], 'total_lessons': 0, 'progress_percent': 0}
        
        self.progress_data[workshop_name]['total_lessons'] = total_lessons
        self._update_workshop_progress(workshop_name)
    
    def mark_exercise_attempt(self, workshop_name: str, exercise_id: str):
        """Mark that user attempted an exercise"""
        self.learning_metrics['exercises_attempted'] += 1
        self.learning_metrics['workshops_started'].add(workshop_name)
    
    def mark_exercise_completed(self, workshop_name: str, exercise_id: str, score: float = None):
        """Mark that user completed an exercise successfully"""
        self.learning_metrics['exercises_completed'] += 1
        
        if score is not None:
            self._update_skill_level(workshop_name, score)
    
    def _update_skill_level(self, workshop_name: str, score: float):
        """Update skill level based on exercise performance"""
        if workshop_name not in self.learning_metrics['skill_levels']:
            self.learning_metrics['skill_levels'][workshop_name] = []
        
        self.learning_metrics['skill_levels'][workshop_name].append(score)
        
        # Calculate average skill level
        scores = self.learning_metrics['skill_levels'][workshop_name]
        avg_score = sum(scores) / len(scores) if scores else 0
        
        # Update skill level classification
        if avg_score >= 0.9:
            level = "Expert"
        elif avg_score >= 0.8:
            level = "Advanced"
        elif avg_score >= 0.7:
            level = "Intermediate"
        elif avg_score >= 0.6:
            level = "Competent"
        else:
            level = "Beginner"
        
        self.learning_metrics['skill_levels'][f"{workshop_name}_level"] = level
    
    def _check_achievements(self):
        """Check for new achievements"""
        total_completed = len(self.completed_lessons)
        
        # Lesson count achievements
        lesson_milestones = [1, 5, 10, 25, 50, 100]
        for milestone in lesson_milestones:
            if total_completed >= milestone and f"lessons_{milestone}" not in [a['id'] for a in self.achievements]:
                self.achievements.append({
                    'id': f"lessons_{milestone}",
                    'title': f"{milestone} Lessons Completed",
                    'description': f"You've completed {milestone} lessons!",
                    'earned_at': datetime.now().isoformat()
                })
        
        # Workshop achievements
        if len(self.learning_metrics['workshops_completed']) >= 1 and "first_workshop" not in [a['id'] for a in self.achievements]:
            self.achievements.append({
                'id': "first_workshop",
                'title': "First Workshop Completed",
                'description': "You've completed your first workshop!",
                'earned_at': datetime.now().isoformat()
            })
    
    def get_workshop_progress(self, workshop_name: str) -> Dict:
        """Get progress for a specific workshop"""
        return self.progress_data.get(workshop_name, {'completed_lessons': [], 'total_lessons': 0, 'progress_percent': 0})
    
    def get_overall_progress(self) -> float:
        """Get overall progress across all workshops"""
        if not self.progress_data:
            return 0.0
        
        total_progress = sum(data.get('progress_percent', 0) for data in self.progress_data.values())
        return total_progress / len(self.progress_data)
    
    def get_completed_lessons(self) -> Set[str]:
        """Get set of completed lesson keys"""
        return self.completed_lessons.copy()
    
    def get_achievements(self) -> List[Dict]:
        """Get list of earned achievements"""
        return self.achievements.copy()
    
    def get_learning_metrics(self) -> Dict:
        """Get comprehensive learning metrics"""
        current_time = time.time()
        session_time = current_time - self.session_start
        
        return {
            **self.learning_metrics,
            'current_session_time': session_time,
            'total_time_spent': self.learning_metrics['total_time_spent'] + session_time,
            'completion_rate': self.learning_metrics['exercises_completed'] / max(1, self.learning_metrics['exercises_attempted']),
            'lessons_per_hour': self.learning_metrics['lessons_completed'] / max(1, session_time / 3600)
        }
    
    def get_all_progress(self) -> Dict:
        """Get all progress data"""
        return {
            'progress_data': self.progress_data,
            'completed_lessons': list(self.completed_lessons),
            'achievements': self.achievements,
            'learning_metrics': self.get_learning_metrics(),
            'last_updated': datetime.now().isoformat()
        }
    
    def load_progress(self, data: Dict = None):
        """Load progress from data"""
        if data:
            self.progress_data = data.get('progress_data', {})
            self.completed_lessons = set(data.get('completed_lessons', []))
            self.achievements = data.get('achievements', [])
            self.learning_metrics.update(data.get('learning_metrics', {}))
    
    def save_progress(self) -> Dict:
        """Save current progress data"""
        return self.get_all_progress()
    
    def cleanup(self):
        """Clean up resources"""
        # Update last activity
        self.learning_metrics['last_activity'] = datetime.now().isoformat()
        self.learning_metrics['total_time_spent'] += time.time() - self.session_start