#ifndef ASTRATECHNICA_GAME_APP_HPP
#define ASTRATECHNICA_GAME_APP_HPP

#include <string>
#include <map>
#include <vector>
#include <memory>
#include <functional>

namespace AstraTechnica {

    // Simple GameApp placeholder class
    class GameApp {
    public:
        GameApp() = default;
        ~GameApp() = default;
        
        void initialize() {}
        void shutdown() {}
        void update() {}
    };

} // namespace AstraTechnica

#endif // ASTRATECHNICA_GAME_APP_HPP