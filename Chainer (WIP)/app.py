"""
Chainer Web Application
Flask web application for mathematical simplicity analysis and education.
"""

from flask import Flask, render_template, request, jsonify, session
import json
import math
from datetime import datetime

# Import our mathematical engine
import sys
import os
sys.path.append(os.path.dirname(__file__))
from chainer_v2 import classifier

app = Flask(__name__)
app.secret_key = 'chainer_secret_key_2024'

# Game data and user progress
user_progress = {
    'level': 1,
    'score': 0,
    'achievements': [],
    'games_played': 0,
    'correct_answers': 0
}

@app.route('/')
def index():
    """Main dashboard with number input and analysis."""
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze_number():
    """Analyze a number and return classification results."""
    try:
        data = request.get_json()
        number = int(data.get('number', 0))
        base = int(data.get('base', 10))
        
        # Get comprehensive analysis
        classification = classifier.classify_number(number, base)
        
        # Add reciprocal expansion
        reciprocal = get_reciprocal_expansion(number, base)
        
        # Add interpretive analysis
        interpretive = get_interpretive_analysis(number, base)
        
        result = {
            'success': True,
            'classification': classification,
            'reciprocal': reciprocal,
            'interpretive': interpretive,
            'timestamp': datetime.now().isoformat()
        }
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

@app.route('/game/terminate_or_repeat')
def terminate_or_repeat():
    """Game 1: Terminate or Repeat speed quiz."""
    return render_template('games/terminate_or_repeat.html')

@app.route('/game/api/question')
def get_game_question():
    """API endpoint for game questions."""
    import random
    
    # Generate a random number for the game
    number = random.randint(2, 30)
    base = random.choice([10, 2, 3, 5, 7, 8, 12])
    
    classification = classifier.classify_number(number, base)
    
    question = {
        'number': number,
        'base': base,
        'question_type': 'terminate_or_repeat',
        'correct_answer': classification['is_simple'] and 'terminate' or 'repeat',
        'difficulty': calculate_difficulty(number, base)
    }
    
    return jsonify(question)

@app.route('/game/api/answer', methods=['POST'])
def check_answer():
    """Check game answer and update score."""
    try:
        data = request.get_json()
        user_answer = data.get('answer')
        correct_answer = data.get('correct')
        time_taken = data.get('time', 0)
        
        is_correct = user_answer.lower() == correct_answer.lower()
        
        # Update user progress
        global user_progress
        user_progress['games_played'] += 1
        if is_correct:
            user_progress['correct_answers'] += 1
            # Calculate score based on difficulty and time
            base_score = 100
            time_bonus = max(0, 50 - time_taken)
            user_progress['score'] += base_score + time_bonus
        
        return jsonify({
            'correct': is_correct,
            'score': user_progress['score'],
            'progress': user_progress
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/learn')
def learn():
    """Learning module with tutorials and explanations."""
    return render_template('learn.html')

@app.route('/explore')
def explore():
    """Exploration module for cross-base analysis."""
    return render_template('explore.html')

@app.route('/api/cross_base/<int:number>')
def cross_base_analysis(number):
    """API for cross-base analysis of a number."""
    try:
        bases = [2, 3, 5, 7, 8, 10, 12, 16, 20, 60]
        analysis = {}
        
        for base in bases:
            classification = classifier.classify_number(number, base)
            reciprocal = get_reciprocal_expansion(number, base, max_digits=20)
            
            analysis[str(base)] = {
                'classification': classification,
                'reciprocal': reciprocal,
                'base_properties': {
                    'base': base,
                    'prime_factors': list(classifier.prime_factors(base)),
                    'base_type': classify_base_type(base)
                }
            }
        
        return jsonify({
            'success': True,
            'number': number,
            'analysis': analysis
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

def get_reciprocal_expansion(n: int, base: int = 10, max_digits: int = 50) -> dict:
    """Calculate reciprocal expansion of 1/n."""
    if n == 0:
        return {'error': 'Reciprocal of 0 is undefined'}
    
    try:
        if base == 10:
            # Use decimal expansion for base 10
            from decimal import Decimal, getcontext
            getcontext().prec = max_digits + 10
            
            decimal_value = Decimal(1) / Decimal(n)
            decimal_str = format(decimal_value, 'f')
            
            # Determine if terminating or repeating
            if '.' in decimal_str and len(decimal_str) <= max_digits:
                if len(decimal_str.split('.')[1]) <= max_digits - 5:
                    return {
                        'decimal': decimal_str,
                        'terminates': True,
                        'period': 0,
                        'type': 'terminating'
                    }
            
            return {
                'decimal': decimal_str[:max_digits] + ('...' if len(decimal_str) > max_digits else ''),
                'terminates': classifier.is_simple(n, base),
                'period': estimate_period(n, base),
                'type': classifier.is_simple(n, base) and 'terminating' or 'repeating'
            }
        else:
            return {'decimal': f'Base {base} conversion not implemented yet'}
            
    except Exception as e:
        return {'error': str(e)}

def estimate_period(n: int, base: int) -> int:
    """Estimate the repeating period of 1/n."""
    if classifier.is_simple(n, base):
        return 0
    
    # Simple estimation based on number theory
    if n < 100:
        return (n - 1) // len(classifier.prime_factors(n)) if n > 1 else 0
    return n // 10  # Rough estimate for larger numbers

def get_interpretive_analysis(n: int, base: int) -> dict:
    """Generate interpretive analysis of the number."""
    classification = classifier.classify_number(n, base)
    
    insights = []
    
    if classification['is_simple']:
        insights.append(f"{n} is Simple in base {base}")
        insights.append(f"All prime factors of {n} divide {base}")
        if len(classification['prime_factors']) == 1:
            insights.append(f"{n} is a pure power of {classification['prime_factors'][0]}")
    else:
        insights.append(f"{n} is Wild in base {base}")
        insights.append(f"{n} has prime factors not dividing {base}")
        insights.append(f"1/{n} will repeat infinitely in base {base}")
    
    if classification['is_factor']:
        insights.append(f"{n} is a Factor prime of base {base}")
    
    # Special properties for key numbers
    if n in [7, 13]:
        insights.append(f"{n} is a Prime Base number with special cyclic properties")
    if n == 0:
        insights.append("0 is the structural origin point")
    
    return {
        'insights': insights,
        'mathematical_significance': get_mathematical_significance(n),
        'educational_notes': get_educational_notes(n, base)
    }

def get_mathematical_significance(n: int) -> str:
    """Get mathematical significance of a number."""
    significance_map = {
        0: "The additive identity and structural origin",
        1: "The multiplicative identity, always Simple",
        2: "Smallest prime, factor of base 10",
        3: "First odd prime, creates repeating decimals",
        5: "Prime factor of base 10",
        7: "Prime Base, generates cyclic number 142857",
        10: "The decimal base itself",
        12: "Highly composite, good for fractions",
        13: "Prime Base, period 6 in base 10"
    }
    
    return significance_map.get(n, f"Integer {n} with unique properties")

def get_educational_notes(n: int, base: int) -> list:
    """Get educational notes about the number."""
    notes = []
    
    if classifier.is_simple(n, base):
        notes.append(f"In base {base}, 1/{n} terminates cleanly")
        notes.append(f"This happens because {n}'s factors align with base {base}'s structure")
    else:
        notes.append(f"In base {base}, 1/{n} creates an infinite repeating pattern")
        notes.append("This reveals the fundamental relationship between numbers and bases")
    
    if n <= 13:
        notes.append("This number is part of our foundational set (0-13)")
    
    return notes

def classify_base_type(base: int) -> str:
    """Classify a base by its mathematical properties."""
    factors = list(classifier.prime_factors(base))
    
    if len(factors) == 1:
        return f"Prime Base ({factors[0]})"
    elif len(factors) == 2:
        return f"Semi-prime Base ({factors[0]}×{factors[1]})"
    elif len(factors) > 3:
        return f"Highly Composite Base ({len(factors)} prime factors)"
    else:
        return f"Composite Base ({factors})"

def calculate_difficulty(number: int, base: int) -> str:
    """Calculate difficulty level for game questions."""
    if number <= 10:
        return "Easy"
    elif number <= 50:
        return "Medium"
    else:
        return "Hard"

@app.route('/api/progress')
def get_progress():
    """Get user progress data."""
    return jsonify(user_progress)

@app.route('/reset_progress')
def reset_progress():
    """Reset user progress."""
    global user_progress
    user_progress = {
        'level': 1,
        'score': 0,
        'achievements': [],
        'games_played': 0,
        'correct_answers': 0
    }
    return jsonify({'success': True, 'progress': user_progress})

if __name__ == '__main__':
    print("Starting Chainer Web Application...")
    print("Access the application at: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)