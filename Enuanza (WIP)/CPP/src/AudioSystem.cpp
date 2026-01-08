#include "PrimeComposition3D.h"
#include <iostream>
#include <cmath>
#include <algorithm>

namespace Enuanza {

AudioSystem::AudioSystem() 
    : m_device(nullptr), m_context(nullptr), m_source(0)
    , m_volume(0.5f), m_muted(false) {
}

AudioSystem::~AudioSystem() {
    cleanup();
}

bool AudioSystem::initialize() {
    if (!initializeOpenAL()) {
        return false;
    }
    
    generatePrimeFrequencies();
    std::cout << "Audio system initialized successfully" << std::endl;
    return true;
}

void AudioSystem::cleanup() {
    // Stop all sounds
    alSourceStop(m_source);
    
    // Delete buffers
    for (auto& [prime, buffer] : m_primeBuffers) {
        alDeleteBuffers(1, &buffer);
    }
    m_primeBuffers.clear();
    
    // Delete source
    if (m_source) {
        alDeleteSources(1, &m_source);
        m_source = 0;
    }
    
    // Destroy context
    if (m_context) {
        alcMakeContextCurrent(nullptr);
        alcDestroyContext(m_context);
        m_context = nullptr;
    }
    
    // Close device
    if (m_device) {
        alcCloseDevice(m_device);
        m_device = nullptr;
    }
}

void AudioSystem::setVolume(float volume) {
    m_volume = std::clamp(volume, 0.0f, 1.0f);
    if (!m_muted && m_source) {
        alSourcef(m_source, AL_GAIN, m_volume);
    }
}

void AudioSystem::setMuted(bool muted) {
    m_muted = muted;
    if (m_source) {
        alSourcef(m_source, AL_GAIN, m_muted ? 0.0f : m_volume);
    }
}

void AudioSystem::playPrimeFrequency(int prime) {
    if (m_muted || !m_source) return;
    
    auto it = m_primeBuffers.find(prime);
    if (it != m_primeBuffers.end()) {
        alSourcei(m_source, AL_BUFFER, it->second);
        alSourcePlay(m_source);
    }
}

void AudioSystem::stopPrimeFrequency(int prime) {
    if (m_source) {
        alSourceStop(m_source);
    }
}

void AudioSystem::playBackgroundMusic() {
    // Background music implementation would go here
}

void AudioSystem::stopBackgroundMusic() {
    // Stop background music implementation would go here
}

bool AudioSystem::initializeOpenAL() {
    // Open default device
    m_device = alcOpenDevice(nullptr);
    if (!m_device) {
        std::cerr << "Failed to open OpenAL device" << std::endl;
        return false;
    }
    
    // Create context
    m_context = alcCreateContext(m_device, nullptr);
    if (!m_context) {
        std::cerr << "Failed to create OpenAL context" << std::endl;
        alcCloseDevice(m_device);
        m_device = nullptr;
        return false;
    }
    
    // Make context current
    if (!alcMakeContextCurrent(m_context)) {
        std::cerr << "Failed to make OpenAL context current" << std::endl;
        alcDestroyContext(m_context);
        alcCloseDevice(m_device);
        m_context = nullptr;
        m_device = nullptr;
        return false;
    }
    
    // Generate source
    alGenSources(1, &m_source);
    if (alGetError() != AL_NO_ERROR) {
        std::cerr << "Failed to generate OpenAL source" << std::endl;
        cleanup();
        return false;
    }
    
    // Configure source
    alSourcef(m_source, AL_PITCH, 1.0f);
    alSourcef(m_source, AL_GAIN, m_volume);
    alSource3f(m_source, AL_POSITION, 0.0f, 0.0f, 0.0f);
    alSource3f(m_source, AL_VELOCITY, 0.0f, 0.0f, 0.0f);
    alSourcei(m_source, AL_LOOPING, AL_FALSE);
    
    return true;
}

void AudioSystem::generatePrimeFrequencies() {
    // Map primes to musical frequencies (Hz)
    std::map<int, float> primeFrequencies = {
        {2, 87.31f},   // A2
        {3, 98.00f},   // G2
        {5, 110.00f},  // A2
        {7, 123.47f},  // B2
        {11, 130.81f}, // C3
        {13, 146.83f}, // D3
        {17, 164.81f}, // E3
        {19, 174.61f}, // F3
        {23, 196.00f}, // G3
        {29, 220.00f}, // A3
        {31, 233.08f}, // A#3
        {37, 246.94f}, // B3
        {41, 261.63f}, // C4 (Middle C)
        {43, 277.18f}, // C#4
        {47, 293.66f}, // D4
        {53, 311.13f}, // D#4
        {59, 329.63f}, // E4
        {61, 349.23f}, // F4
        {67, 369.99f}, // F#4
        {71, 392.00f}, // G4
        {73, 415.30f}, // G#4
        {79, 440.00f}, // A4
        {83, 466.16f}, // A#4
        {89, 493.88f}, // B4
        {97, 523.25f}, // C5
    };
    
    // Generate audio buffers for each prime frequency
    for (const auto& [prime, frequency] : primeFrequencies) {
        ALuint buffer = generateToneBuffer(frequency, 1.0f); // 1 second duration
        if (buffer) {
            m_primeBuffers[prime] = buffer;
        }
    }
    
    // Generate frequencies for additional primes using mathematical formula
    for (int prime = 101; prime <= 997; prime += 2) {
        // Simple primality test
        bool isPrime = true;
        for (int i = 3; i * i <= prime; i += 2) {
            if (prime % i == 0) {
                isPrime = false;
                break;
            }
        }
        
        if (isPrime) {
            // Calculate frequency based on prime properties
            float frequency = 440.0f * pow(2.0f, (prime % 12) / 12.0f);
            frequency = std::clamp(frequency, 80.0f, 2000.0f);
            
            ALuint buffer = generateToneBuffer(frequency, 0.5f);
            if (buffer) {
                m_primeBuffers[prime] = buffer;
            }
        }
    }
}

ALuint AudioSystem::generateToneBuffer(float frequency, float duration) {
    const int sampleRate = 44100;
    const int numSamples = static_cast<int>(sampleRate * duration);
    
    std::vector<ALshort> samples(numSamples);
    
    // Generate sine wave
    for (int i = 0; i < numSamples; ++i) {
        float time = static_cast<float>(i) / sampleRate;
        float amplitude = 0.5f * sin(2.0f * M_PI * frequency * time);
        
        // Apply envelope for smoother sound
        float envelope = 1.0f;
        if (i < sampleRate * 0.01f) { // Attack
            envelope = i / (sampleRate * 0.01f);
        } else if (i > numSamples - sampleRate * 0.1f) { // Release
            envelope = (numSamples - i) / (sampleRate * 0.1f);
        }
        
        samples[i] = static_cast<ALshort>(amplitude * envelope * 32767);
    }
    
    // Create OpenAL buffer
    ALuint buffer;
    alGenBuffers(1, &buffer);
    if (alGetError() != AL_NO_ERROR) {
        return 0;
    }
    
    // Fill buffer
    alBufferData(buffer, AL_FORMAT_MONO16, samples.data(), 
                 static_cast<ALsizei>(samples.size() * sizeof(ALshort)), sampleRate);
    
    if (alGetError() != AL_NO_ERROR) {
        alDeleteBuffers(1, &buffer);
        return 0;
    }
    
    return buffer;
}

} // namespace Enuanza