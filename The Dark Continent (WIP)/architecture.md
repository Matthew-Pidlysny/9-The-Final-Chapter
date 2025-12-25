# Dark Continent C++ Architecture Design

## Module Structure (30kb+ modules goal):

### Core Engine Modules

1.  **GameEngine.cpp/h** (Main game loop, state management)
2.  **GameBoard.cpp/h** (World map, territories, coordinates)
3.  **PlayerManager.cpp/h** (Player turns, actions, validation)
4.  **ResourceManager.cpp/h** (Assets, cards, UI elements)

### Player System Modules

5.  **Player.cpp/h** (Base player class, common functionality)
6.  **UnitedStates.cpp/h** (US-specific mechanics, America cards)
7.  **Russia.cpp/h** (Russia-specific mechanics, Communism cards)
8.  **EuropeanUnion.cpp/h** (EU-specific mechanics, Influence cards)
9.  **SouthernAlliance.cpp/h** (Alliance-specific mechanics, Resource cards)
10.  **DarkContinent.cpp/h** (Devils, mischief cards, fragment spawning)

### Card System Modules

11.  **CardSystem.cpp/h** (Card base classes, deck management)
12.  **AmericaDeck.cpp/h** (US card effects, exact wording preservation)
13.  **CommunismDeck.cpp/h** (Russia card effects, exact wording preservation)
14.  **DivineWillDeck.cpp/h** (Shared card effects, exact wording preservation)
15.  **MischiefDeck.cpp/h** (Devil card effects, exact wording preservation)
16.  **EUInfluenceDeck.cpp/h** (EU card effects, political mechanics)
17.  **AllianceDeck.cpp/h** (Southern Alliance card effects, resource mechanics)

### Combat & Units Modules

18.  **CombatSystem.cpp/h** (Battle resolution, attack/defense calculations)
19.  **UnitManager.cpp/h** (Unit types, stats, upgrades, stacking)
20.  **FortificationSystem.cpp/h** (Buildings, defenses, special structures)
21.  **MovementSystem.cpp/h** (Unit movement, pathfinding, naval regions)

### Population & Economy Modules

22.  **PopulationCounter.cpp/h** (City populations, growth, overpopulation)
23.  **EconomySystem.cpp/h** (Currency, resources, income calculations)
24.  **InfluenceSystem.cpp/h** (Territory influence, political control)

### UI & Rendering Modules

25.  **Renderer.cpp/h** (OpenGL/SDL rendering pipeline)
26.  **UIManager.cpp/h** (Interface elements, menus, controls)
27.  **MapRenderer.cpp/h** (World map rendering, zoom functionality)
28.  **PieceRenderer.cpp/h** (Unit/fortification rendering, stacking visualization)
29.  **CardRenderer.cpp/h** (Card display, hand management)
30.  **AnimationSystem.cpp/h** (UI animations, transitions, effects)

### Network & Federation Modules

31.  **NetworkManager.cpp/h** (Asynchronous play, federation system)
32.  **SaveSystem.cpp/h** (Game state serialization, cloud saves)
33.  **EventManager.cpp/h** (Game events, triggers, callbacks)

### Utility & Support Modules

34.  **MathUtils.cpp/h** (Coordinates, calculations, helper functions)
35.  **FileUtils.cpp/h** (File I/O, asset loading)
36.  **StringUtils.cpp/h** (Text processing, card wording handling)
37.  **ConfigSystem.cpp/h** (Settings, game configuration)
38.  **Logger.cpp/h** (Debug logging, error tracking)
39.  **AudioManager.cpp/h** (Sound effects, music)
40.  **InputManager.cpp/h** (Mouse/keyboard input, touch support)

## Dependencies & Libraries:

### Graphics & UI:

-   **SFML 2.6** - Main graphics and window management
-   **ImGui 1.89** - Immediate mode GUI for game interfaces
-   **OpenGL 3.3** - Hardware acceleration for map rendering

### Audio:

-   **OpenAL Soft** - 3D positional audio
-   **libsndfile** - Audio file loading

### Network:

-   **Boost.Asio** - Asynchronous networking for federation play
-   **WebSocket++** - Real-time communication
-   **JSON for Modern C++** - Data serialization

### Utilities:

-   **SQLite3** - Local save data and caching
-   **zlib** - Compression for network transfers
-   **FreeType** - Font rendering for card text

### Build System:

-   **CMake 3.25+** - Cross-platform build configuration
-   **vcpkg** - Package management

## Federation/Asynchronous Play Architecture:

### Client-Server Model:

```
Federation Server (Cloud)
├── Game State Management
├── Player Action Queue  
├── Turn Validation
├── Save Synchronization
└── Conflict Resolution

Client Instances (Local)
├── Local Game State
├── Action Buffering
├── UI Responsiveness
└── Offline Mode Support
```

### Data Flow:

1.  Players submit actions locally (immediate UI feedback)
2.  Actions queued for federation validation
3.  Server validates and broadcasts confirmed actions
4.  Clients synchronize with authoritative game state
5.  Conflicts resolved using deterministic game logic

### Turn Management:

-   **Simultaneous Turns**: All players act within time window
-   **Action Lock-in**: Actions become immutable after deadline
-   **Conflict Resolution**: Server arbitrates timing conflicts
-   **Reconciliation**: Clients adjust to authoritative state

## Digital Stacking System:

### Piece Counting Algorithm:

```cpp
struct TerritoryPieces {
    std::map<PlayerID, std::map<UnitType, int>> units;
    std::map<PlayerID, std::map<FortType, int>> fortifications;
    bool hasMultiplePieces() const;
    int getTotalPieceCount() const;
};
```

### Zoom & Visualization:

-   **Level 0**: Territory overview with piece counts
-   **Level 1**: Territory with stacked piece indicators
-   **Level 2**: Expanded view showing individual pieces
-   **Level 3**: Detailed piece information and stats

### Rendering Pipeline:

1.  **Culling**: Only visible territories rendered
2.  **LOD System**: Different detail levels based on zoom
3.  **Instanced Rendering**: Efficient multiple piece rendering
4.  **UI Overlay**: Piece counts and controls

## Memory Management Strategy:

### Object Pooling:

-   Cards, units, and UI elements use object pools
-   Reduces allocation/deallocation overhead
-   Predictable memory usage patterns

### Smart Pointers:

-   std::shared\_ptr for shared resources
-   std::unique\_ptr for exclusive ownership
-   std::weak\_ptr for non-owning references

### Resource Loading:

-   Lazy loading of card graphics
-   Streaming for large map textures
-   Compression for card text data

## Performance Targets:

-   **60 FPS** during normal gameplay
-   **30 FPS** minimum during complex animations
-   **< 100ms** response time for player actions
-   **< 500MB** total memory usage
-   **< 2GB** disk space for complete game

## Cross-Platform Support:

-   **Windows 10/11** (Primary)
-   **macOS 12+** (Intel/Apple Silicon)
-   **Linux Ubuntu 22.04+** (Secondary)
-   **WebGL** (Future browser support)

## Development Tools Integration:

-   **Visual Studio 2022** (Windows)
-   **Xcode 14** (macOS)
-   **CLion/VSCode** (Linux)
-   **Git LFS** for large assets
-   **CI/CD pipeline** for automated builds