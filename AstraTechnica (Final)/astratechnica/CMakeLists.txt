# AstraTechnica Source CMakeLists

# AstraTechnica Source CMakeLists

# Create include directories
include_directories(${CMAKE_CURRENT_SOURCE_DIR})

# Core library
add_library(astratechnica_core_lib STATIC
    core/game_engine.cpp
    core/game_engine.hpp
)

target_include_directories(astratechnica_core_lib PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
target_link_libraries(astratechnica_core_lib PUBLIC Threads::Threads)

# Character library
add_library(astratechnica_character_lib STATIC
    character/character_system.cpp
    character/character_system.hpp
)

target_include_directories(astratechnica_character_lib PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
target_link_libraries(astratechnica_character_lib PUBLIC astratechnica_core_lib)

# Phone integration library
add_library(astratechnica_phone_lib STATIC
    phone/phone_integration.cpp
    phone/phone_integration.hpp
)

target_include_directories(astratechnica_phone_lib PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
target_link_libraries(astratechnica_phone_lib PUBLIC astratechnica_core_lib)

# AI system library
add_library(astratechnica_ai_lib STATIC
    ai/ai_system.hpp
    # Note: ai_system.cpp not implemented yet to avoid build errors
)

target_include_directories(astratechnica_ai_lib PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
target_link_libraries(astratechnica_ai_lib PUBLIC astratechnica_core_lib)

# External dependencies for phone integration (if available)
if(CURL_FOUND)
    target_link_libraries(astratechnica_phone_lib PRIVATE ${CURL_LIBRARIES})
    target_include_directories(astratechnica_phone_lib PRIVATE ${CURL_INCLUDE_DIRS})
endif()

if(OPENSSL_FOUND)
    target_link_libraries(astratechnica_phone_lib PRIVATE OpenSSL::SSL OpenSSL::Crypto)
    target_include_directories(astratechnica_phone_lib PRIVATE ${OPENSSL_INCLUDE_DIR})
endif()

# External dependencies for AI system (if available)
if(TORCH_FOUND)
    target_link_libraries(astratechnica_ai_lib PRIVATE ${TORCH_LIBRARIES})
    target_include_directories(astratechnica_ai_lib PRIVATE ${TORCH_INCLUDE_DIRS})
endif()

if(MLPACK_FOUND)
    target_link_libraries(astratechnica_ai_lib PRIVATE ${MLPACK_LIBRARIES})
    target_include_directories(astratechnica_ai_lib PRIVATE ${MLPACK_INCLUDE_DIRS})
endif()

if(OpenCV_FOUND)
    target_link_libraries(astratechnica_ai_lib PRIVATE ${OpenCV_LIBS})
endif()

# Platform-specific linking
if(WIN32)
    target_link_libraries(astratechnica_phone_lib PRIVATE ws2_32 crypt32)
elseif(UNIX AND NOT APPLE)
    target_link_libraries(astratechnica_core_lib PRIVATE pthread)
    target_link_libraries(astratechnica_phone_lib PRIVATE pthread)
    target_link_libraries(astratechnica_ai_lib PRIVATE pthread)
endif()
# Kardashev Max library
add_library(astratechnica_kardashev_lib STATIC
    kardashev/kardashev_max_system.cpp
    kardashev/kardashev_max_system.hpp
    kardashev/kardashev_integration.cpp
    kardashev/kardashev_integration.hpp
)

target_include_directories(astratechnica_kardashev_lib PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
target_link_libraries(astratechnica_kardashev_lib PUBLIC astratechnica_core_lib Threads::Threads)

# Kardashev Max executable
add_executable(astratechnica_kardashev_max kardashev/astratechnica_kardashev_max.cpp)
target_link_libraries(astratechnica_kardashev_max PRIVATE 
    astratechnica_core_lib 
    astratechnica_character_lib 
    astratechnica_phone_lib 
    astratechnica_ai_lib
    astratechnica_kardashev_lib
)

