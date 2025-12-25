# Dark Continent 5-Player Game

A massive C++ implementation of the Dark Continent strategy game, enhanced for 5-player gameplay with federation support and digital features.

## Overview

Dark Continent is a geopolitical strategy game where five major powers compete for global dominance while dealing with the emergence of the mysterious Dark Continent. This C++ implementation features:

- **5-Player Support**: United States, Russia, European Union, Southern Alliance, and Dark Continent
- **Federation Play**: Asynchronous multiplayer with cloud synchronization
- **Digital Features**: Zoom system, piece stacking, and advanced UI
- **Exact Card Preservation**: All original card wording maintained
- **Modular Architecture**: 40+ C++ modules for maintainability

## Players

### 1. United States
- **Starting Position**: North America
- **Focus**: Military technology and global influence
- **Cards**: America, Divine Will, Technology

### 2. Russia  
- **Starting Position**: Eastern Europe
- **Focus**: Population growth and nuclear development
- **Cards**: Communism, Divine Will, Technology, Population Counter

### 3. European Union
- **Starting Position**: Western Europe
- **Focus**: Diplomatic influence and alliances
- **Cards**: EU Influence, Divine Will

### 4. Southern Hemisphere Alliance
- **Starting Position**: South America, Africa, Oceania, Antarctica
- **Focus**: Resource extraction and territorial development
- **Cards**: Alliance, Divine Will

### 5. Dark Continent
- **Starting Position**: Spawns during game
- **Focus**: World federation through chaos and influence
- **Cards**: Mischief, Divine Will

## Features

### Core Gameplay
- **48 Territories**: Complete world map with naval regions
- **Population Counter**: City levels 0-5 with growth mechanics
- **Combat System**: Dice-based with modifiers and special abilities
- **Card System**: 150+ cards with exact original wording
- **Victory Conditions**: Multiple paths to victory

### Digital Enhancements
- **5-Level Zoom**: From world view to unit inspection
- **Piece Stacking**: Efficient display of multiple units
- **Federation Mode**: Asynchronous play for busy schedules
- **Auto-Save**: Continuous game state preservation
- **Replay System**: Save and review games

### Technical Features
- **C++20**: Modern C++ with advanced features
- **OpenGL Rendering**: Hardware-accelerated graphics
- **SFML Framework**: Cross-platform multimedia
- **Modular Design**: Clean, maintainable architecture
- **Network Support**: Real-time and asynchronous multiplayer

## Requirements

### System Requirements
- **OS**: Windows 10+, macOS 10.14+, or Linux (Ubuntu 18.04+)
- **CPU**: Dual-core 2.0 GHz or better
- **Memory**: 4 GB RAM minimum, 8 GB recommended
- **Graphics**: OpenGL 3.3 compatible GPU
- **Storage**: 2 GB available space
- **Network**: Broadband connection for federation play

### Development Dependencies
- **CMake 3.25+**
- **C++20 compatible compiler**
- **SFML 2.6**
- **OpenGL 3.3**
- **Boost.Asio** (for networking)

## Installation

### Building from Source

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-org/DarkContinent.git
   cd DarkContinent
   ```

2. **Install dependencies**:
   ```bash
   # Ubuntu/Debian
   sudo apt-get install cmake build-essential libsfml-dev libopengl-dev
   
   # macOS (with Homebrew)
   brew install cmake sfml
   
   # Windows
   # Use vcpkg or download pre-built libraries
   ```

3. **Configure and build**:
   ```bash
   mkdir build
   cd build
   cmake ..
   make -j$(nproc)  # or use Visual Studio on Windows
   ```

4. **Run the game**:
   ```bash
   ./DarkContinent
   ```

### Package Installation

#### Windows
- Download `DarkContinent-1.0.0-win64.exe`
- Run installer and follow prompts

#### macOS
- Download `DarkContinent-1.0.0-macos.dmg`
- Mount and drag to Applications folder

#### Linux (Ubuntu/Debian)
- Download `darkcontinent_1.0.0_amd64.deb`
- Install with: `sudo dpkg -i darkcontinent_1.0.0_amd64.deb`

## Quick Start

### Single Player Game
1. Launch Dark Continent
2. Select "New Game"
3. Choose 5-player mode
4. Set up player positions (AI or human)
5. Start playing!

### Federation Game
1. Select "Federation Mode"
2. Create or join a game room
3. Take turns when notified
4. Game synchronizes automatically

### Basic Controls
- **Mouse**: Navigate interface, select units/cards
- **Scroll Wheel**: Zoom in/out
- **Arrow Keys**: Pan map
- **Space**: End turn
- **Escape**: Open menu

## Game Rules

Complete rules are available in `Game_Rules.md` and in-game through the Help menu.

### Quick Rules Summary
- **Goal**: Achieve one of the victory conditions
- **Turn**: Income → Actions → End Phase
- **Combat**: Roll dice, apply modifiers, resolve
- **Cards**: Pay costs, resolve effects
- **Victory**: Domination, Influence, Shimarra, Federation, or Time

## Development

### Architecture
The game uses a modular architecture with 40+ C++ modules:

```
src/
├── Core/           # Game engine, board, player management
├── Cards/          # Card systems and effects
├── Combat/         # Battle resolution and units
├── UI/             # User interface and rendering
├── Network/        # Federation and multiplayer
├── Utils/          # Utilities and helpers
└── Data/           # Game data and resources
```

### Contributing
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

### Code Style
- Follow C++ Core Guidelines
- Use clang-format for code formatting
- Include comprehensive comments
- Write unit tests for new features

## Testing

### Running Tests
```bash
# Build and run unit tests
cd build
make test

# Run game simulation
./DarkContinent --test-simulation

# Memory leak check (Linux/macOS)
valgrind --leak-check=full ./DarkContinent
```

### Test Coverage
- Unit tests for all major systems
- Integration tests for game flow
- Performance tests for rendering
- Network tests for federation play

## Documentation

- **Game Rules**: `Game_Rules.md`
- **API Documentation**: Generated with Doxygen
- **Architecture**: `architecture.md`
- **Design Documents**: `game_design.md`

## Support

### Bug Reports
- File issues on GitHub
- Include system information
- Provide reproduction steps
- Attach error logs

### Community
- Discord server: [link]
- Reddit: r/DarkContinentGame
- Forums: forums.darkcontinent.game

### Contact
- Email: support@darkcontinent.game
- Website: darkcontinent.game

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Credits

### Original Game
- Original Dark Continent concept and rules
- Card design and balance

### 5-Player Implementation
- NinjaTech AI Development Team
- C++ architecture and programming
- Federation system design

### Special Thanks
- Beta testers and community feedback
- Open source contributors
- Strategy game enthusiasts

---

**Version**: 1.0.0  
**Build**: C++20, SFML 2.6, OpenGL 3.3  
**Platform**: Windows, macOS, Linux  
**License**: MIT

Enjoy playing Dark Continent! 🌍