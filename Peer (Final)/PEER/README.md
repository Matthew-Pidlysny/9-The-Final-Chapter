# Peerx - Enhanced Peer System for Mathematical and Scientific Formulas

## Overview

Peerx is an enhanced version of the Peer system, designed to help users validate, understand, and work with mathematical and scientific formulas. Unlike simple calculators, Peerx provides intelligent analysis, context-aware assistance, and multi-level explanations suitable for everyone from high school students to professional researchers.

## Key Features

### 1. **Subject Matter Classification**
- Automatically detects whether input is within Peer's scope
- Identifies domain: Mathematics, Physics, Chemistry, Biology, Engineering, Computer Science, Statistics, Economics
- Provides helpful warnings for out-of-scope content (humanities, everyday topics)

### 2. **Variable Detection**
- Recognizes 50+ common variables and their meanings
- Identifies potential interpretations (e.g., "v" could be velocity, voltage, or volume)
- Shows typical domains where variables are used

### 3. **Unit Detection**
- Recognizes 476+ units across all scientific disciplines
- Identifies unit categories (Length, Time, Mass, Velocity, etc.)
- Helps ensure unit consistency in formulas

### 4. **"Stuck" Button AI Assistant**
- Helps users format natural language into mathematical notation
- Converts "force equals mass times acceleration" to "F = m * a"
- Provides formatting help without solving problems (encourages learning)

### 5. **Progressive Interface Modes**
- **Beginner Mode**: Simplified interface with auto-correction and gentle guidance
- **Student Mode**: Computation with step-by-step explanations and real-world examples
- **Standard Mode**: Balanced validation and analysis for general use
- **Expert Mode**: Full-featured validation with verbose output for professionals

### 6. **Enhanced Validation**
- Beginner-friendly error messages with explanations
- Visual highlighting of error locations
- Automatic suggestions for corrections
- Confidence scores for analysis

### 7. **Learning Features**
- Step-by-step explanations (Student mode)
- Real-world examples showing practical applications
- Related formulas suggestions
- Quick definitions for variables and units

### 8. **Productivity Features**
- Formula history tracking
- Custom formula library
- Example formulas organized by subject
- Quick tips and context-aware help

## Installation

### Prerequisites
- Python 3.11 or higher
- No external dependencies required (uses only standard library)

### Setup
```bash
# Clone or download the Peerx package
cd Peerx_Working

# Run the system
python peerx_final.py
```

## Usage Examples

### Example 1: Basic Formula Validation
```python
from peerx_final import PeerxFinal, InterfaceMode

# Initialize system
system = PeerxFinal(mode=InterfaceMode.STANDARD)

# Process a formula
result = system.process_input("E = mc^2")

# View results
print(f"Valid: {result.is_valid}")
print(f"Domain: {result.analysis.domain}")
print(f"Variables: {list(result.analysis.variables_detected.keys())}")
```

### Example 2: Student Mode with Computation
```python
# Use Student mode for computation and explanations
system = PeerxFinal(mode=InterfaceMode.STUDENT)

# Process Sarah's acceleration problem
result = system.process_input("(60 - 0) / 10")

print(f"Result: {result.computation_result}")  # 6.0
print("\nStep-by-Step:")
for step in result.step_by_step:
    print(f"  {step}")
```

### Example 3: Stuck Button Assistance
```python
# Help a user who is stuck
suggestion = system.help_stuck_user("I need to calculate force")

print(f"Suggested Formula: {suggestion.suggested_format}")
print(f"\nExplanation:")
print(suggestion.explanation)
```

### Example 4: Variable + Unit Analysis
```python
# Analyze a variable with its units
analysis = system.analyze_variable_with_units("v", "m/s")

print(f"Variable meanings: {analysis['variable_meanings']}")
print(f"Unit category: {analysis['unit_category']}")
```

## Interface Modes Explained

### Beginner Mode
- Auto-correction enabled
- Simplified error messages
- Helpful hints and tips
- Perfect for first-time users

### Student Mode
- Computation results included
- Step-by-step explanations
- Real-world examples
- Ideal for homework and learning

### Standard Mode
- Balanced features
- No auto-correction
- Detailed analysis
- Best for general use

### Expert Mode
- Full validation capabilities
- Verbose output
- Advanced options
- Designed for researchers and professionals

## File Structure

```
Peerx_Working/
├── peerx_final.py              # Main system file (use this!)
├── peerx_integration.py        # Integration system (alternative)
├── units_database.py           # Unit and variable database
├── subject_classifier.py       # Subject matter classification
├── stuck_button_assistant.py   # AI formatting assistant
├── original/                   # Backup of original Peer files
│   ├── peer.py
│   ├── peer_cpu.py
│   └── peer_validation.py
├── user_testing_letter.txt     # User feedback from testing
├── team_response.txt           # Team response to user feedback
├── 50_novice_friendly_ideas.md # List of improvement ideas
└── README.md                   # This file
```

## System Capabilities

### Supported Domains
- Mathematics (calculus, algebra, geometry, statistics)
- Physics (mechanics, thermodynamics, electromagnetism, quantum mechanics)
- Chemistry (organic, inorganic, physical, analytical)
- Biology (cellular, molecular, ecology, genetics)
- Engineering (mechanical, electrical, civil, chemical)
- Computer Science (algorithms, data structures, ML)
- Statistics (hypothesis testing, regression, probability)
- Economics (micro, macro, econometrics)

### Out-of-Scope Content
Peerx politely declines and provides helpful guidance for:
- Humanities (literature, history, philosophy, art)
- Everyday topics (cooking, travel, shopping, weather)
- Politics, law, and current events

## Testing

Run the comprehensive test suite:
```bash
python peerx_final.py
```

This will test:
- Subject classification
- Variable detection
- Unit detection
- Formula validation
- Stuck button assistance
- Computation (Student mode)
- All interface modes

## Future Enhancements

The following features are planned for future releases:
- Handwriting recognition
- Voice input
- Visual formula editor (WYSIWYG)
- Mobile app
- Collaborative features
- Advanced symbolic computation
- Integration with external computation engines

## User Feedback

Based on testing with high school students, we've implemented:
- ✓ Student mode with computation
- ✓ Beginner-friendly error messages
- ✓ Step-by-step explanations
- ✓ Real-world examples
- ✓ Auto-correction in Beginner mode
- ✓ Quick tips and helpful hints
- ✓ Example formulas library
- ✓ Formula history tracking

See `user_testing_letter.txt` and `team_response.txt` for detailed feedback and our commitment to continuous improvement.

## Contributing

This is the final deliverable for the Peer Enhancement Project. Future contributions should focus on:
1. Expanding the units database
2. Improving the classification accuracy
3. Adding more example formulas
4. Implementing future enhancements listed above

## License

This project is based on the original Peer system. See original files for licensing information.

## Contact

For questions, feedback, or support, please refer to the original Peer documentation.

## Acknowledgments

- Original Peer system development team
- Sarah Chen (high school student tester) for valuable feedback
- The 50 novice-friendly ideas that guided improvements
- All contributors to the scientific formula validation community

---

**Peerx: Making mathematical and scientific formulas accessible to everyone.**