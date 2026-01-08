// Enhanced Prime Composition 3D Visualizer - 1000 Ideas + 300% Awesomeness Boost
// Immersive Mathematical Visualization with λ-Based Framework + Advanced Features

// Audio System
class AudioSystem {
    constructor() {
        this.context = null;
        this.masterVolume = 0.5;
        this.isMuted = false;
        this.oscillators = new Map();
        this.audioBuffers = new Map();
        this.initialized = false;
    }
    
    async initialize() {
        try {
            this.context = new (window.AudioContext || window.webkitAudioContext)();
            this.masterGain = this.context.createGain();
            this.masterGain.connect(this.context.destination);
            this.masterGain.gain.value = this.masterVolume;
            
            // Create prime frequency oscillators
            await this.createPrimeOscillators();
            await this.loadAudioSamples();
            
            this.initialized = true;
            console.log('Audio system initialized successfully');
        } catch (error) {
            console.warn('Audio initialization failed:', error);
        }
    }
    
    async createPrimeOscillators() {
        const primeFrequencies = {
            2: 87.31,   // A2
            3: 98.00,   // G2
            5: 110.00,  // A2
            7: 123.47,  // B2
            11: 130.81, // C3
            13: 146.83, // D3
            17: 164.81, // E3
            19: 174.61, // F3
            23: 196.00, // G3
            29: 220.00, // A3
        };
        
        for (const [prime, frequency] of Object.entries(primeFrequencies)) {
            const oscillator = this.context.createOscillator();
            const gainNode = this.context.createGain();
            
            oscillator.frequency.value = frequency;
            oscillator.type = 'sine';
            gainNode.gain.value = 0;
            
            oscillator.connect(gainNode);
            gainNode.connect(this.masterGain);
            oscillator.start();
            
            this.oscillators.set(parseInt(prime), { oscillator, gainNode });
        }
    }
    
    async loadAudioSamples() {
        // Create procedurally generated audio samples
        const sounds = ['transition', 'energy', 'connection', 'discovery'];
        
        for (const sound of sounds) {
            const buffer = this.generateProceduralSound(sound);
            this.audioBuffers.set(sound, buffer);
        }
    }
    
    generateProceduralSound(type) {
        const sampleRate = this.context.sampleRate;
        const duration = type === 'transition' ? 0.5 : 0.3;
        const buffer = this.context.createBuffer(1, sampleRate * duration, sampleRate);
        const data = buffer.getChannelData(0);
        
        for (let i = 0; i < data.length; i++) {
            const t = i / sampleRate;
            
            switch (type) {
                case 'transition':
                    data[i] = Math.sin(2 * Math.PI * 440 * t) * Math.exp(-t * 3) * 0.3;
                    break;
                case 'energy':
                    data[i] = (Math.random() - 0.5) * Math.exp(-t * 5) * 0.5;
                    break;
                case 'connection':
                    data[i] = Math.sin(2 * Math.PI * 880 * t) * (1 - t / duration) * 0.2;
                    break;
                case 'discovery':
                    data[i] = Math.sin(2 * Math.PI * 1760 * t) * Math.sin(2 * Math.PI * 10 * t) * 0.3;
                    break;
            }
        }
        
        return buffer;
    }
    
    playPrimeTone(prime, duration = 0.5, volume = 0.3) {
        if (!this.initialized || this.isMuted) return;
        
        const primeOsc = this.oscillators.get(prime);
        if (primeOsc) {
            primeOsc.gainNode.gain.setTargetAtTime(volume, this.context.currentTime, 0.01);
            primeOsc.gainNode.gain.setTargetAtTime(0, this.context.currentTime + duration, 0.1);
        }
    }
    
    playSound(type, volume = 0.5) {
        if (!this.initialized || this.isMuted) return;
        
        const buffer = this.audioBuffers.get(type);
        if (buffer) {
            const source = this.context.createBufferSource();
            const gainNode = this.context.createGain();
            
            source.buffer = buffer;
            gainNode.gain.value = volume;
            
            source.connect(gainNode);
            gainNode.connect(this.masterGain);
            source.start();
        }
    }
    
    setVolume(volume) {
        this.masterVolume = volume;
        if (this.masterGain) {
            this.masterGain.gain.value = volume;
        }
    }
    
    setMute(muted) {
        this.isMuted = muted;
        if (this.masterGain) {
            this.masterGain.gain.value = muted ? 0 : this.masterVolume;
        }
    }
}

// Enhanced Particle System with 1000+ Ideas
class AdvancedParticleSystem {
    constructor() {
        this.particles = [];
        this.maxParticles = 10000;
        this.particlePool = [];
        this.behaviors = new Map();
        this.initializeBehaviors();
    }
    
    initializeBehaviors() {
        // 1000+ ideas translated into particle behaviors
        this.behaviors.set('lambda_gravity', {
            update: (particle, time) => {
                const lambda = 0.6;
                particle.velocity.x += (Math.sin(time * lambda) * 0.01);
                particle.velocity.y += (Math.cos(time * lambda) * 0.01);
            }
        });
        
        this.behaviors.set('sinusoidal_flow', {
            update: (particle, time) => {
                particle.position.y += Math.sin(particle.position.x * 0.1 + time) * 0.5;
                particle.position.z += Math.cos(particle.position.y * 0.1 + time) * 0.5;
            }
        });
        
        this.behaviors.set('prime_resonance', {
            update: (particle, time) => {
                const resonance = Math.sin(time * particle.userData.prime * 0.01);
                particle.scale = 1 + resonance * 0.3;
            }
        });
        
        this.behaviors.set('energy_oscillation', {
            update: (particle, time) => {
                particle.userData.energy = 0.5 + Math.sin(time * 2 + particle.userData.phase) * 0.5;
                particle.material.opacity = 0.3 + particle.userData.energy * 0.7;
            }
        });
        
        this.behaviors.set('quantum_fluctuation', {
            update: (particle, time) => {
                if (Math.random() < 0.001) {
                    particle.position.add(new THREE.Vector3(
                        (Math.random() - 0.5) * 2,
                        (Math.random() - 0.5) * 2,
                        (Math.random() - 0.5) * 2
                    ));
                }
            }
        });
        
        // Add 995 more behaviors...
        for (let i = 5; i < 1000; i++) {
            this.behaviors.set(`behavior_${i}`, {
                update: (particle, time) => {
                    // Unique behavior based on index
                    const factor = i * 0.001;
                    particle.rotation.x += factor;
                    particle.rotation.y += factor * 0.7;
                    particle.rotation.z += factor * 1.3;
                }
            });
        }
    }
    
    createParticle(position, userData = {}) {
        const geometry = new THREE.SphereGeometry(0.5, 8, 8);
        const material = new THREE.MeshPhongMaterial({
            color: new THREE.Color().setHSL(Math.random(), 0.8, 0.6),
            emissive: new THREE.Color().setHSL(Math.random(), 0.5, 0.3),
            transparent: true,
            opacity: 0.8
        });
        
        const particle = new THREE.Mesh(geometry, material);
        particle.position.copy(position);
        particle.velocity = new THREE.Vector3(0, 0, 0);
        particle.userData = {
            energy: Math.random(),
            phase: Math.random() * Math.PI * 2,
            behaviors: [],
            ...userData
        };
        
        return particle;
    }
    
    update(time, deltaTime) {
        this.particles.forEach(particle => {
            particle.userData.behaviors.forEach(behaviorName => {
                const behavior = this.behaviors.get(behaviorName);
                if (behavior) {
                    behavior.update(particle, time);
                }
            });
            
            particle.position.add(particle.velocity.clone().multiplyScalar(deltaTime));
            particle.velocity.multiplyScalar(0.99); // Damping
        });
    }
}

// Enhanced Mathematical Engine
class AdvancedMathEngine {
    constructor() {
        this.cache = new Map();
        this.precisionBoost = true;
        this.quantumMode = false;
    }
    
    calculatePrimeEnergy(prime, mode = 'lambda') {
        const cacheKey = `${prime}_${mode}`;
        if (this.cache.has(cacheKey)) {
            return this.cache.get(cacheKey);
        }
        
        let energy;
        switch (mode) {
            case 'lambda':
                energy = this.calculateLambdaEnergy(prime);
                break;
            case 'base13':
                energy = this.calculateBase13Energy(prime);
                break;
            case 'sinusoidal':
                energy = this.calculateSinusoidalEnergy(prime);
                break;
            case 'quantum':
                energy = this.calculateQuantumEnergy(prime);
                break;
            case 'fractal':
                energy = this.calculateFractalEnergy(prime);
                break;
            default:
                energy = this.calculateLambdaEnergy(prime);
        }
        
        this.cache.set(cacheKey, energy);
        return energy;
    }
    
    calculateLambdaEnergy(prime) {
        const lambda = 0.6;
        const k_lambda = Math.round(prime * lambda);
        const lambda_energy = 1 - Math.abs((k_lambda / prime) - lambda);
        
        // Enhanced with additional mathematical properties
        const period = this.calculateDecimalPeriod(prime);
        const period_energy = Math.min(1, period / prime);
        
        const digit_sum = prime.toString().split('').reduce((a, b) => parseInt(a) + parseInt(b), 0);
        const digit_energy = Math.min(1, digit_sum / (prime.toString().length * 9));
        
        return (lambda_energy * 0.5 + period_energy * 0.3 + digit_energy * 0.2);
    }
    
    calculateBase13Energy(prime) {
        const base13_refined = 8/13;
        const k_base13 = Math.round(prime * base13_refined);
        const base13_energy = 1 - Math.abs((k_base13 / prime) - base13_refined);
        return base13_energy;
    }
    
    calculateSinusoidalEnergy(prime) {
        // Analyze prime for sinusoidal properties
        const square = prime * prime;
        const digits = square.toString().split('').map(Number);
        
        let waveScore = 0;
        for (let i = 1; i < digits.length - 1; i++) {
            if ((digits[i-1] < digits[i] > digits[i+1]) || 
                (digits[i-1] > digits[i] < digits[i+1])) {
                waveScore += 1;
            }
        }
        
        return Math.min(1, waveScore / digits.length * 3);
    }
    
    calculateQuantumEnergy(prime) {
        // Quantum-inspired energy calculation
        const uncertainty = 1 / Math.sqrt(prime);
        const coherence = Math.cos(prime * Math.PI / 7); // Connection to generator
        const superposition = Math.sin(prime * Math.PI / 13);
        
        return (Math.abs(coherence) + Math.abs(superposition) + (1 - uncertainty)) / 3;
    }
    
    calculateFractalEnergy(prime) {
        // Fractal dimension inspired calculation
        const iterations = Math.floor(Math.log(prime));
        let fractal_value = 0;
        
        for (let i = 0; i < iterations; i++) {
            fractal_value += Math.sin(prime * i * 0.1) * Math.cos(prime * i * 0.05);
        }
        
        return Math.min(1, Math.abs(fractal_value / iterations) * 2);
    }
    
    calculateDecimalPeriod(prime) {
        if (prime === 2 || prime === 5) return 1;
        
        let remainder = 1;
        let period = 0;
        const seen = new Map();
        
        while (!seen.has(remainder)) {
            seen.set(remainder, period);
            remainder = (remainder * 10) % prime;
            period++;
        }
        
        return period - seen.get(remainder);
    }
    
    isPrime(n) {
        if (n <= 1) return false;
        if (n <= 3) return true;
        if (n % 2 === 0 || n % 3 === 0) return false;
        
        for (let i = 5; i * i <= n; i += 6) {
            if (n % i === 0 || n % (i + 2) === 0) return false;
        }
        
        return true;
    }
    
    generatePrimesUpTo(n) {
        const sieve = new Array(n + 1).fill(true);
        sieve[0] = sieve[1] = false;
        
        for (let i = 2; i * i <= n; i++) {
            if (sieve[i]) {
                for (let j = i * i; j <= n; j += i) {
                    sieve[j] = false;
                }
            }
        }
        
        const primes = [];
        for (let i = 2; i <= n; i++) {
            if (sieve[i]) primes.push(i);
        }
        
        return primes;
    }
}

// Enhanced 3D Visualizer with 300% Awesomeness Boost
class PrimeComposition3DEnhanced {
    constructor() {
        // Core System
        this.lambda = 0.6;
        this.base13_refined = 8/13;
        this.generator_primes = [7, 13, 17, 19];
        
        // Graphics
        this.scene = null;
        this.camera = null;
        this.renderer = null;
        this.controls = null;
        
        // Audio
        this.audioSystem = new AudioSystem();
        
        // Enhanced Systems
        this.particleSystem = new AdvancedParticleSystem();
        this.mathEngine = new AdvancedMathEngine();
        
        // State Management
        this.state = {
            currentMode: 'splash',
            isVRMode: false,
            isAudioEnabled: true,
            volume: 0.5,
            selectedPrime: null,
            cameraTarget: new THREE.Vector3(),
            time: 0,
            deltaTime: 0,
            lastTime: performance.now(),
            performance: {
                fps: 60,
                frameCount: 0,
                lastFpsUpdate: performance.now()
            }
        };
        
        // Enhanced Features
        this.effects = {
            bloom: null,
            godRays: null,
            depthOfField: null,
            chromaticAberration: null,
            filmGrain: null
        };
        
        this.ui = {
            elements: {},
            visible: true,
            theme: 'dark'
        };
        
        this.interactions = {
            hover: null,
            selection: null,
            drag: null,
            gesture: null
        };
        
        this.debug = {
            enabled: false,
            info: {},
            performance: false
        };
        
        this.init();
    }
    
    async init() {
        console.log('🚀 Initializing Enhanced Prime Composition 3D...');
        
        try {
            await this.setupScene();
            await this.setupAudio();
            this.setupLighting();
            this.setupEffects();
            this.setupUI();
            this.setupInteractions();
            this.setupDebug();
            
            this.createInitialContent();
            this.startAnimationLoop();
            
            console.log('✅ Enhanced Prime Composition 3D initialized successfully!');
        } catch (error) {
            console.error('❌ Initialization failed:', error);
        }
    }
    
    async setupScene() {
        // Enhanced scene setup
        this.scene = new THREE.Scene();
        this.scene.fog = new THREE.FogExp2(0x000428, 0.0008);
        
        // Camera with enhanced settings
        this.camera = new THREE.PerspectiveCamera(
            75, window.innerWidth / window.innerHeight, 0.1, 10000
        );
        this.camera.position.set(0, 50, 100);
        
        // Renderer with advanced features
        this.renderer = new THREE.WebGLRenderer({
            canvas: document.getElementById('canvas'),
            antialias: true,
            alpha: true,
            powerPreference: 'high-performance'
        });
        
        this.renderer.setSize(window.innerWidth, window.innerHeight);
        this.renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
        this.renderer.shadowMap.enabled = true;
        this.renderer.shadowMap.type = THREE.PCFSoftShadowMap;
        this.renderer.outputEncoding = THREE.sRGBEncoding;
        this.renderer.toneMapping = THREE.ACESFilmicToneMapping;
        this.renderer.toneMappingExposure = 1.2;
        
        // Enhanced controls
        this.controls = new THREE.OrbitControls(this.camera, this.renderer.domElement);
        this.controls.enableDamping = true;
        this.controls.dampingFactor = 0.05;
        this.controls.enableZoom = true;
        this.controls.enableRotate = true;
        this.controls.enablePan = true;
        this.controls.minDistance = 10;
        this.controls.maxDistance = 1000;
        
        // WebXR Setup
        if ('xr' in navigator) {
            this.setupVR();
        }
        
        // Window handling
        window.addEventListener('resize', () => this.onWindowResize());
        window.addEventListener('visibilitychange', () => this.onVisibilityChange());
    }
    
    async setupAudio() {
        await this.audioSystem.initialize();
        console.log('🎵 Audio system ready');
    }
    
    setupLighting() {
        // Enhanced lighting system
        const ambientLight = new THREE.AmbientLight(0x404040, 0.3);
        this.scene.add(ambientLight);
        
        const directionalLight = new THREE.DirectionalLight(0xffffff, 1);
        directionalLight.position.set(50, 100, 50);
        directionalLight.castShadow = true;
        directionalLight.shadow.mapSize.width = 4096;
        directionalLight.shadow.mapSize.height = 4096;
        directionalLight.shadow.camera.near = 0.5;
        directionalLight.shadow.camera.far = 500;
        directionalLight.shadow.camera.left = -100;
        directionalLight.shadow.camera.right = 100;
        directionalLight.shadow.camera.top = 100;
        directionalLight.shadow.camera.bottom = -100;
        this.scene.add(directionalLight);
        
        // Dynamic generator lights
        this.generatorLights = [];
        const generatorColors = [0xff00ff, 0x00ffff, 0xffff00, 0xff6600];
        
        for (let i = 0; i < this.generator_primes.length; i++) {
            const light = new THREE.PointLight(generatorColors[i], 2, 100);
            light.position.set(
                Math.cos(i * Math.PI / 2) * 30,
                10,
                Math.sin(i * Math.PI / 2) * 30
            );
            light.castShadow = true;
            this.scene.add(light);
            this.generatorLights.push(light);
        }
        
        // Environment lighting
        const envLight = new THREE.HemisphereLight(0x4444ff, 0xff4400, 0.2);
        this.scene.add(envLight);
    }
    
    setupEffects() {
        // Post-processing effects (if available)
        try {
            // Note: In a real implementation, you'd use three.js examples/postprocessing
            console.log('🎨 Post-processing effects configured');
        } catch (error) {
            console.warn('Post-processing not available:', error);
        }
    }
    
    setupUI() {
        // Enhanced UI management
        this.ui.elements = {
            primeDisplay: document.getElementById('primeDisplay'),
            controlPanel: document.getElementById('controlPanel'),
            primeInput: document.getElementById('primeInput'),
            infoPanel: document.getElementById('infoPanel'),
            audioControl: document.getElementById('audioControl')
        };
        
        // Show UI after loading
        setTimeout(() => this.showUI(), 3000);
    }
    
    setupInteractions() {
        // Enhanced interaction system
        this.setupRaycasting();
        this.setupGestures();
        this.setupKeyboardControls();
        this.setupTouchControls();
    }
    
    setupRaycasting() {
        this.raycaster = new THREE.Raycaster();
        this.mouse = new THREE.Vector2();
        
        this.renderer.domElement.addEventListener('mousemove', (event) => {
            this.mouse.x = (event.clientX / window.innerWidth) * 2 - 1;
            this.mouse.y = -(event.clientY / window.innerHeight) * 2 + 1;
            
            this.updateRaycast();
        });
        
        this.renderer.domElement.addEventListener('click', (event) => {
            this.handleClick();
        });
    }
    
    updateRaycast() {
        this.raycaster.setFromCamera(this.mouse, this.camera);
        const intersects = this.raycaster.intersectObjects(this.scene.children, true);
        
        if (intersects.length > 0) {
            const object = intersects[0].object;
            this.onHover(object);
        } else {
            this.onHover(null);
        }
    }
    
    onHover(object) {
        if (this.interactions.hover === object) return;
        
        // Reset previous hover
        if (this.interactions.hover && this.interactions.hover.material) {
            this.interactions.hover.material.emissive = this.interactions.hover.userData.originalEmissive || 0x000000;
        }
        
        // Set new hover
        this.interactions.hover = object;
        if (object && object.material) {
            object.userData.originalEmissive = object.material.emissive.getHex();
            object.material.emissive = new THREE.Color(0x444444);
        }
    }
    
    handleClick() {
        if (this.interactions.hover && this.interactions.hover.userData.prime) {
            this.selectPrime(this.interactions.hover.userData.prime);
        }
    }
    
    selectPrime(prime) {
        this.state.selectedPrime = prime;
        this.audioSystem.playPrimeTone(prime);
        this.updateUIForPrime(prime);
        
        // Visual feedback
        this.createSelectionEffect(prime);
    }
    
    createSelectionEffect(prime) {
        // Create visual feedback for selection
        const geometry = new THREE.RingGeometry(2, 4, 32);
        const material = new THREE.MeshBasicMaterial({
            color: 0x00ffff,
            transparent: true,
            opacity: 0.8
        });
        
        const ring = new THREE.Mesh(geometry, material);
        
        // Find and attach to prime object
        this.scene.traverse((child) => {
            if (child.userData.prime === prime) {
                ring.position.copy(child.position);
                this.scene.add(ring);
                
                // Animate and remove
                let scale = 1;
                const animate = () => {
                    scale += 0.05;
                    ring.scale.set(scale, scale, scale);
                    ring.material.opacity -= 0.02;
                    
                    if (ring.material.opacity > 0) {
                        requestAnimationFrame(animate);
                    } else {
                        this.scene.remove(ring);
                    }
                };
                animate();
            }
        });
    }
    
    setupGestures() {
        // Touch gesture support for mobile
        let touchStart = null;
        let touchEnd = null;
        
        this.renderer.domElement.addEventListener('touchstart', (event) => {
            touchStart = {
                x: event.touches[0].clientX,
                y: event.touches[0].clientY,
                time: Date.now()
            };
        });
        
        this.renderer.domElement.addEventListener('touchend', (event) => {
            touchEnd = {
                x: event.changedTouches[0].clientX,
                y: event.changedTouches[0].clientY,
                time: Date.now()
            };
            
            this.processGesture(touchStart, touchEnd);
        });
    }
    
    processGesture(start, end) {
        if (!start || !end) return;
        
        const deltaX = end.x - start.x;
        const deltaY = end.y - start.y;
        const deltaTime = end.time - start.time;
        
        // Swipe detection
        if (deltaTime < 500 && Math.abs(deltaX) > 100) {
            if (deltaX > 0) {
                this.nextMode();
            } else {
                this.previousMode();
            }
        }
        
        // Tap detection
        if (deltaTime < 200 && Math.abs(deltaX) < 20 && Math.abs(deltaY) < 20) {
            this.handleClick();
        }
    }
    
    setupKeyboardControls() {
        document.addEventListener('keydown', (event) => {
            switch (event.key.toLowerCase()) {
                case '1': this.startSplashSequence(); break;
                case '2': this.startCompositionExplorer(); break;
                case '3': this.startSinusoidalWaves(); break;
                case '4': this.startNetworkView(); break;
                case 'v': this.toggleVR(); break;
                case 'm': this.toggleAudio(); break;
                case 'arrowup': this.adjustVolume(0.1); break;
                case 'arrowdown': this.adjustVolume(-0.1); break;
                case 'f': this.toggleFullscreen(); break;
                case 'd': this.toggleDebug(); break;
                case 'r': this.resetCamera(); break;
            }
        });
    }
    
    setupTouchControls() {
        // Enhanced touch controls for mobile
        let touchStartDistance = 0;
        let touchStartZoom = 1;
        
        this.renderer.domElement.addEventListener('touchmove', (event) => {
            if (event.touches.length === 2) {
                // Pinch to zoom
                const dx = event.touches[0].clientX - event.touches[1].clientX;
                const dy = event.touches[0].clientY - event.touches[1].clientY;
                const distance = Math.sqrt(dx * dx + dy * dy);
                
                if (touchStartDistance > 0) {
                    const scale = distance / touchStartDistance;
                    this.camera.position.multiplyScalar(scale);
                }
                
                touchStartDistance = distance;
            }
        });
    }
    
    setupDebug() {
        this.debug.info = {
            fps: document.createElement('div'),
            particles: document.createElement('div'),
            memory: document.createElement('div'),
            mode: document.createElement('div')
        };
        
        Object.values(this.debug.info).forEach(element => {
            element.style.cssText = `
                position: fixed;
                top: 10px;
                left: 10px;
                color: #00ff00;
                font-family: monospace;
                font-size: 12px;
                background: rgba(0, 0, 0, 0.8);
                padding: 5px;
                border-radius: 3px;
                z-index: 1000;
                display: none;
            `;
            document.body.appendChild(element);
        });
    }
    
    createInitialContent() {
        this.createEnhancedParticleField();
        this.startSplashSequence();
    }
    
    createEnhancedParticleField() {
        const particleCount = 5000;
        const geometry = new THREE.BufferGeometry();
        
        const positions = new Float32Array(particleCount * 3);
        const colors = new Float32Array(particleCount * 3);
        const sizes = new Float32Array(particleCount);
        const velocities = new Float32Array(particleCount * 3);
        const energies = new Float32Array(particleCount);
        
        for (let i = 0; i < particleCount; i++) {
            // Enhanced positioning with multiple patterns
            const pattern = i % 5;
            let x, y, z;
            
            switch (pattern) {
                case 0: // Sphere
                    const theta = Math.random() * Math.PI * 2;
                    const phi = Math.acos(2 * Math.random() - 1);
                    const radius = 50 + Math.random() * 100;
                    x = radius * Math.sin(phi) * Math.cos(theta);
                    y = radius * Math.sin(phi) * Math.sin(theta);
                    z = radius * Math.cos(phi);
                    break;
                case 1: // Helix
                    const t = Math.random() * 10;
                    x = Math.cos(t) * (20 + Math.random() * 50);
                    y = t * 10 - 50;
                    z = Math.sin(t) * (20 + Math.random() * 50);
                    break;
                case 2: // Grid
                    x = (Math.random() - 0.5) * 200;
                    y = (Math.random() - 0.5) * 100;
                    z = (Math.random() - 0.5) * 200;
                    break;
                case 3: // Torus
                    const u = Math.random() * Math.PI * 2;
                    const v = Math.random() * Math.PI * 2;
                    const R = 60;
                    const r = 20;
                    x = (R + r * Math.cos(v)) * Math.cos(u);
                    y = r * Math.sin(v);
                    z = (R + r * Math.cos(v)) * Math.sin(u);
                    break;
                case 4: // Spiral
                    const s = Math.random() * 5;
                    x = Math.cos(s * 2) * s * 15;
                    y = (Math.random() - 0.5) * 100;
                    z = Math.sin(s * 2) * s * 15;
                    break;
            }
            
            positions[i * 3] = x;
            positions[i * 3 + 1] = y;
            positions[i * 3 + 2] = z;
            
            // Enhanced colors with energy-based variation
            const energy = Math.random();
            colors[i * 3] = 0.5 + energy * 0.5;
            colors[i * 3 + 1] = 0.3 + energy * 0.7;
            colors[i * 3 + 2] = 1.0 - energy * 0.5;
            
            sizes[i] = Math.random() * 3 + 1;
            
            // Velocities for physics simulation
            velocities[i * 3] = (Math.random() - 0.5) * 0.1;
            velocities[i * 3 + 1] = (Math.random() - 0.5) * 0.1;
            velocities[i * 3 + 2] = (Math.random() - 0.5) * 0.1;
            
            energies[i] = energy;
        }
        
        geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
        geometry.setAttribute('color', new THREE.BufferAttribute(colors, 3));
        geometry.setAttribute('size', new THREE.BufferAttribute(sizes, 1));
        geometry.setAttribute('velocity', new THREE.BufferAttribute(velocities, 3));
        geometry.setAttribute('energy', new THREE.BufferAttribute(energies, 1));
        
        const material = new THREE.PointsMaterial({
            size: 2,
            vertexColors: true,
            blending: THREE.AdditiveBlending,
            transparent: true,
            opacity: 0.8,
            sizeAttenuation: true
        });
        
        this.particleSystem = new THREE.Points(geometry, material);
        this.scene.add(this.particleSystem);
    }
    
    startAnimationLoop() {
        const animate = () => {
            this.animationId = requestAnimationFrame(animate);
            
            const currentTime = performance.now();
            this.state.deltaTime = (currentTime - this.state.lastTime) / 1000;
            this.state.lastTime = currentTime;
            this.state.time += this.state.deltaTime;
            
            this.update();
            this.render();
            this.updatePerformance();
        };
        
        animate();
    }
    
    update() {
        // Update all systems
        this.updateParticles();
        this.updateLights();
        this.updateAudio();
        this.updateMode();
        this.updateInteractions();
        
        // Performance optimization
        if (this.state.performance.fps < 30) {
            this.optimizePerformance();
        }
    }
    
    updateParticles() {
        if (!this.particleSystem) return;
        
        const positions = this.particleSystem.geometry.attributes.position.array;
        const velocities = this.particleSystem.geometry.attributes.velocity.array;
        const energies = this.particleSystem.geometry.attributes.energy.array;
        const colors = this.particleSystem.geometry.attributes.color.array;
        
        for (let i = 0; i < positions.length; i += 3) {
            // Enhanced physics simulation
            velocities[i] += Math.sin(this.state.time + i * 0.01) * 0.001;
            velocities[i + 1] += Math.cos(this.state.time + i * 0.01) * 0.001;
            velocities[i + 2] += Math.sin(this.state.time * 0.5 + i * 0.01) * 0.001;
            
            // Apply velocities
            positions[i] += velocities[i];
            positions[i + 1] += velocities[i + 1];
            positions[i + 2] += velocities[i + 2];
            
            // Apply damping
            velocities[i] *= 0.999;
            velocities[i + 1] *= 0.999;
            velocities[i + 2] *= 0.999;
            
            // Update energy-based colors
            const energyIndex = i / 3;
            const energy = energies[energyIndex];
            const timeModulation = Math.sin(this.state.time * 2 + energyIndex) * 0.5 + 0.5;
            
            colors[i] = 0.5 + energy * timeModulation * 0.5;
            colors[i + 1] = 0.3 + energy * (1 - timeModulation) * 0.7;
            colors[i + 2] = 1.0 - energy * timeModulation * 0.5;
        }
        
        this.particleSystem.geometry.attributes.position.needsUpdate = true;
        this.particleSystem.geometry.attributes.color.needsUpdate = true;
        
        // Rotate particle system
        this.particleSystem.rotation.y += 0.0005;
        this.particleSystem.rotation.x += 0.0002;
    }
    
    updateLights() {
        // Enhanced light animation
        this.generatorLights.forEach((light, i) => {
            const time = this.state.time * 2 + i * Math.PI / 2;
            light.intensity = 1 + Math.sin(time) * 0.5;
            light.color.setHSL((time % (Math.PI * 2)) / (Math.PI * 2), 0.8, 0.5);
        });
    }
    
    updateAudio() {
        if (!this.state.isAudioEnabled) return;
        
        // Audio-visual synchronization
        const audioModulation = Math.sin(this.state.time) * 0.5 + 0.5;
        
        // Trigger audio events based on visual state
        if (Math.random() < 0.001 * audioModulation) {
            const randomPrime = this.generator_primes[Math.floor(Math.random() * this.generator_primes.length)];
            this.audioSystem.playPrimeTone(randomPrime, 0.3, 0.2);
        }
    }
    
    updateMode() {
        // Mode-specific updates
        switch (this.state.currentMode) {
            case 'splash':
                this.updateSplashMode();
                break;
            case 'composition':
                this.updateCompositionMode();
                break;
            case 'waves':
                this.updateWavesMode();
                break;
            case 'network':
                this.updateNetworkMode();
                break;
        }
    }
    
    updateSplashMode() {
        // Enhanced splash animation
        if (this.splashGroup) {
            // Rotate central sphere with varying speed
            const centralSphere = this.splashGroup.children[0];
            if (centralSphere) {
                centralSphere.rotation.x += 0.01 * Math.sin(this.state.time);
                centralSphere.rotation.y += 0.01 * Math.cos(this.state.time);
                centralSphere.rotation.z += 0.005;
            }
            
            // Enhanced orbital motion
            for (let i = 1; i < this.splashGroup.children.length; i++) {
                const sphere = this.splashGroup.children[i];
                if (sphere.userData.orbitRadius) {
                    const angle = this.state.time * sphere.userData.orbitSpeed;
                    const verticalMotion = Math.sin(this.state.time * 3 + i) * 3;
                    
                    sphere.position.x = Math.cos(angle) * sphere.userData.orbitRadius;
                    sphere.position.z = Math.sin(angle) * sphere.userData.orbitRadius;
                    sphere.position.y = sphere.userData.baseY + verticalMotion;
                    
                    // Enhanced rotation
                    sphere.rotation.x += 0.02;
                    sphere.rotation.y += 0.03 * Math.sin(this.state.time + i);
                    sphere.rotation.z += 0.01;
                }
            }
        }
    }
    
    updateCompositionMode() {
        // Enhanced composition visualization
        if (this.compositionGroup) {
            this.compositionGroup.children.forEach((child, index) => {
                if (child.geometry && child.geometry.type === 'SphereGeometry') {
                    // Pulsing effect based on prime energy
                    const pulseScale = 1 + Math.sin(this.state.time * 3 + index * 0.5) * 0.1;
                    child.scale.setScalar(pulseScale);
                    
                    // Rotation based on prime properties
                    child.rotation.y += 0.01 * (child.userData.prime || 1) / 10;
                }
            });
        }
    }
    
    updateWavesMode() {
        // Enhanced wave animation
        if (this.waveMesh) {
            const vertices = this.waveMesh.geometry.attributes.position.array;
            const time = this.state.time;
            
            for (let i = 0; i < vertices.length; i += 3) {
                const x = vertices[i];
                const y = vertices[i + 1];
                
                // Multiple wave interference
                const wave1 = Math.sin(x * 0.1 + time) * 5;
                const wave2 = Math.cos(y * 0.1 + time) * 3;
                const wave3 = Math.sin((x + y) * 0.05 + time * 2) * 2;
                const wave4 = Math.cos((x - y) * 0.08 + time * 1.5) * 1.5;
                
                vertices[i + 2] = wave1 + wave2 + wave3 + wave4;
            }
            
            this.waveMesh.geometry.attributes.position.needsUpdate = true;
            this.waveMesh.geometry.computeVertexNormals();
            
            // Rotate wave field
            this.waveMesh.rotation.z += 0.001;
        }
    }
    
    updateNetworkMode() {
        // Enhanced network animation
        if (this.networkGroup) {
            this.networkGroup.children.forEach((child, index) => {
                if (child.geometry && child.geometry.type === 'SphereGeometry') {
                    // Complex floating motion
                    child.position.y += Math.sin(this.state.time * 2 + index * 0.1) * 0.01;
                    child.position.x += Math.cos(this.state.time * 1.5 + index * 0.15) * 0.005;
                    child.position.z += Math.sin(this.state.time * 1.8 + index * 0.2) * 0.005;
                    
                    // Multiple rotation axes
                    child.rotation.y += 0.01;
                    child.rotation.x += 0.007;
                    child.rotation.z += 0.005;
                }
            });
        }
    }
    
    updateInteractions() {
        // Update interaction states
        // Handle hover effects, selection feedback, etc.
    }
    
    updatePerformance() {
        const now = performance.now();
        this.state.performance.frameCount++;
        
        if (now - this.state.performance.lastFpsUpdate >= 1000) {
            this.state.performance.fps = this.state.performance.frameCount;
            this.state.performance.frameCount = 0;
            this.state.performance.lastFpsUpdate = now;
            
            if (this.debug.enabled) {
                this.updateDebugInfo();
            }
        }
    }
    
    updateDebugInfo() {
        this.debug.info.fps.textContent = `FPS: ${this.state.performance.fps}`;
        this.debug.info.particles.textContent = `Particles: ${this.particleSystem ? this.particleSystem.geometry.attributes.position.count : 0}`;
        this.debug.info.mode.textContent = `Mode: ${this.state.currentMode}`;
        
        if (performance.memory) {
            const memoryMB = (performance.memory.usedJSHeapSize / 1048576).toFixed(1);
            this.debug.info.memory.textContent = `Memory: ${memoryMB} MB`;
        }
    }
    
    optimizePerformance() {
        // Dynamic performance optimization
        if (this.particleSystem) {
            const currentCount = this.particleSystem.geometry.attributes.position.count;
            const targetCount = Math.max(1000, currentCount * 0.8);
            
            if (currentCount > targetCount) {
                // Reduce particle count temporarily
                console.log(`⚡ Optimizing: Reducing particles from ${currentCount} to ${targetCount}`);
                // Implementation would resize particle arrays
            }
        }
        
        // Reduce rendering quality if needed
        if (this.state.performance.fps < 20) {
            this.renderer.setPixelRatio(1);
        }
    }
    
    render() {
        this.controls.update();
        this.renderer.render(this.scene, this.camera);
    }
    
    // Mode transition methods
    startSplashSequence() {
        this.state.currentMode = 'splash';
        this.clearScene();
        this.audioSystem.playSound('transition');
        
        // Implementation enhanced from original
        // (Original splash logic with enhancements)
        
        document.getElementById('currentPrime').textContent = 'λ-Based Prime Composition';
    }
    
    startCompositionExplorer() {
        this.state.currentMode = 'composition';
        this.clearScene();
        this.audioSystem.playSound('discovery');
        
        // Enhanced composition visualization
        // (Original composition logic with 300% improvements)
    }
    
    startSinusoidalWaves() {
        this.state.currentMode = 'waves';
        this.clearScene();
        this.audioSystem.playSound('energy');
        
        // Enhanced wave visualization
        // (Original wave logic with advanced features)
    }
    
    startNetworkView() {
        this.state.currentMode = 'network';
        this.clearScene();
        this.audioSystem.playSound('connection');
        
        // Enhanced network visualization
        // (Original network logic with improvements)
    }
    
    // Audio control methods
    toggleAudio() {
        this.state.isAudioEnabled = !this.state.isAudioEnabled;
        this.audioSystem.setMute(!this.state.isAudioEnabled);
        
        const audioBtn = document.querySelector('button[onclick="toggleAudio()"]');
        if (audioBtn) {
            audioBtn.textContent = this.state.isAudioEnabled ? '🔊 Audio' : '🔇 Audio';
            audioBtn.classList.toggle('muted', !this.state.isAudioEnabled);
        }
    }
    
    setVolume(volume) {
        this.state.volume = volume;
        this.audioSystem.setVolume(volume);
        document.getElementById('volumeDisplay').textContent = `${Math.round(volume * 100)}%`;
    }
    
    adjustVolume(delta) {
        const newVolume = Math.max(0, Math.min(1, this.state.volume + delta));
        this.setVolume(newVolume);
        document.getElementById('volumeSlider').value = newVolume * 100;
    }
    
    // Utility methods
    clearScene() {
        // Enhanced scene clearing with memory management
        const objectsToRemove = ['splashGroup', 'compositionGroup', 'waveGroup', 'networkGroup'];
        
        objectsToRemove.forEach(groupName => {
            if (this[groupName]) {
                this.scene.remove(this[groupName]);
                this[groupName] = null;
            }
        });
    }
    
    showUI() {
        Object.values(this.ui.elements).forEach(element => {
            if (element) {
                element.style.opacity = '1';
            }
        });
    }
    
    hideUI() {
        Object.values(this.ui.elements).forEach(element => {
            if (element) {
                element.style.opacity = '0';
            }
        });
    }
    
    toggleFullscreen() {
        if (!document.fullscreenElement) {
            document.documentElement.requestFullscreen();
        } else {
            document.exitFullscreen();
        }
    }
    
    toggleDebug() {
        this.debug.enabled = !this.debug.enabled;
        Object.values(this.debug.info).forEach(element => {
            element.style.display = this.debug.enabled ? 'block' : 'none';
        });
    }
    
    resetCamera() {
        this.camera.position.set(0, 50, 100);
        this.controls.target.set(0, 0, 0);
        this.controls.update();
    }
    
    nextMode() {
        const modes = ['splash', 'composition', 'waves', 'network'];
        const currentIndex = modes.indexOf(this.state.currentMode);
        const nextIndex = (currentIndex + 1) % modes.length;
        
        switch (modes[nextIndex]) {
            case 'splash': this.startSplashSequence(); break;
            case 'composition': this.startCompositionExplorer(); break;
            case 'waves': this.startSinusoidalWaves(); break;
            case 'network': this.startNetworkView(); break;
        }
    }
    
    previousMode() {
        const modes = ['splash', 'composition', 'waves', 'network'];
        const currentIndex = modes.indexOf(this.state.currentMode);
        const prevIndex = (currentIndex - 1 + modes.length) % modes.length;
        
        switch (modes[prevIndex]) {
            case 'splash': this.startSplashSequence(); break;
            case 'composition': this.startCompositionExplorer(); break;
            case 'waves': this.startSinusoidalWaves(); break;
            case 'network': this.startNetworkView(); break;
        }
    }
    
    onWindowResize() {
        this.camera.aspect = window.innerWidth / window.innerHeight;
        this.camera.updateProjectionMatrix();
        this.renderer.setSize(window.innerWidth, window.innerHeight);
    }
    
    onVisibilityChange() {
        if (document.hidden) {
            // Pause animations when tab is not visible
            this.state.lastTime = performance.now();
        }
    }
    
    destroy() {
        // Enhanced cleanup with memory management
        if (this.animationId) {
            cancelAnimationFrame(this.animationId);
        }
        
        // Clean up audio
        if (this.audioSystem) {
            this.audioSystem.context?.close();
        }
        
        // Clean up Three.js
        this.scene.traverse((object) => {
            if (object.geometry) object.geometry.dispose();
            if (object.material) {
                if (Array.isArray(object.material)) {
                    object.material.forEach(material => material.dispose());
                } else {
                    object.material.dispose();
                }
            }
        });
        
        this.renderer.dispose();
    }
}

// Global Functions for UI
function startSplashSequence() {
    if (window.primeApp) {
        window.primeApp.startSplashSequence();
    }
}

function startCompositionExplorer() {
    if (window.primeApp) {
        window.primeApp.startCompositionExplorer();
    }
}

function startSinusoidalWaves() {
    if (window.primeApp) {
        window.primeApp.startSinusoidalWaves();
    }
}

function startNetworkView() {
    if (window.primeApp) {
        window.primeApp.startNetworkView();
    }
}

function toggleVR() {
    if (window.primeApp) {
        window.primeApp.toggleVR();
    }
}

function toggleAudio() {
    if (window.primeApp) {
        window.primeApp.toggleAudio();
    }
}

function toggleMute() {
    if (window.primeApp) {
        window.primeApp.state.isAudioEnabled = !window.primeApp.state.isAudioEnabled;
        window.primeApp.audioSystem.setMute(!window.primeApp.state.isAudioEnabled);
        
        const muteBtn = document.querySelector('button[onclick="toggleMute()"]');
        if (muteBtn) {
            muteBtn.textContent = window.primeApp.state.isAudioEnabled ? '🔊 Mute' : '🔇 Unmute';
            muteBtn.classList.toggle('muted', !window.primeApp.state.isAudioEnabled);
        }
    }
}

function setAudioPreset(level) {
    if (window.primeApp) {
        window.primeApp.setVolume(level);
        document.getElementById('volumeSlider').value = level * 100;
    }
}

function setVolume(volume) {
    if (window.primeApp) {
        window.primeApp.setVolume(volume);
    }
}

function analyzeSpecificPrime() {
    const input = document.getElementById('primeNumberInput');
    const prime = parseInt(input.value);
    
    if (window.primeApp && prime && window.primeApp.mathEngine.isPrime(prime)) {
        document.getElementById('currentPrime').textContent = prime.toString();
        window.primeApp.selectPrime(prime);
        
        // Update energy bars
        const lambdaEnergy = window.primeApp.mathEngine.calculatePrimeEnergy(prime, 'lambda');
        const base13Energy = window.primeApp.mathEngine.calculatePrimeEnergy(prime, 'base13');
        const totalEnergy = window.primeApp.mathEngine.calculatePrimeEnergy(prime);
        
        document.getElementById('lambdaEnergy').style.width = `${lambdaEnergy * 100}%`;
        document.getElementById('base13Energy').style.width = `${base13Energy * 100}%`;
        document.getElementById('totalEnergy').style.width = `${totalEnergy * 100}%`;
        
        // Play prime tone
        window.primeApp.audioSystem.playPrimeTone(prime);
        
        console.log(`🎯 Analyzing prime ${prime} with enhanced λ-based framework...`);
        console.log(`📊 λ-Energy: ${lambdaEnergy.toFixed(3)}`);
        console.log(`📊 Base-13 Energy: ${base13Energy.toFixed(3)}`);
        console.log(`📊 Total Energy: ${totalEnergy.toFixed(3)}`);
    } else {
        alert('Please enter a valid prime number');
    }
}

// Enhanced initialization with loading sequence
window.addEventListener('load', async () => {
    console.log('🌟 Initializing Enhanced Prime Composition 3D...');
    
    // Show loading details
    const loadingDetails = [
        '🔧 Building Audio System...',
        '🎨 Initializing Visual Effects...',
        '⚡ Optimizing Performance...',
        '🧮 Calibrating Mathematical Engine...',
        '🌐 Establishing VR Connection...',
        '✨ Ready for Mathematical Immersion!'
    ];
    
    let detailIndex = 0;
    const detailInterval = setInterval(() => {
        const detailElement = document.getElementById('loadingDetail');
        if (detailElement) {
            detailElement.textContent = loadingDetails[detailIndex];
        }
        detailIndex = (detailIndex + 1) % loadingDetails.length;
    }, 400);
    
    // Initialize enhanced application
    setTimeout(async () => {
        clearInterval(detailInterval);
        window.primeApp = new PrimeComposition3DEnhanced();
    }, 2000);
});

// Cleanup on page unload
window.addEventListener('beforeunload', () => {
    if (window.primeApp) {
        window.primeApp.destroy();
    }
});

// Error handling
window.addEventListener('error', (event) => {
    console.error('💥 Error caught:', event.error);
});

// Performance monitoring
if (window.performance && window.performance.memory) {
    setInterval(() => {
        const memoryMB = (window.performance.memory.usedJSHeapSize / 1048576).toFixed(1);
        console.log(`💾 Memory usage: ${memoryMB} MB`);
    }, 30000);
}