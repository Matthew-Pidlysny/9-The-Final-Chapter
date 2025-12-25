#ifndef ASTRATECHNICA_WORLD_MAP_HPP
#define ASTRATECHNICA_WORLD_MAP_HPP

#include <string>
#include <map>
#include <vector>

namespace AstraTechnica {

    // Simple WorldMap placeholder class
    class WorldMap {
    public:
        WorldMap() = default;
        ~WorldMap() = default;
        
        void initialize() {}
        void update() {}
        void spawn_map(const std::string& map_type) {}
    };

} // namespace AstraTechnica

#endif // ASTRATECHNICA_WORLD_MAP_HPP