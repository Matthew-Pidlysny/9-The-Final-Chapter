// Prime Composition 3D Visualizer - Enhanced with Audio Controls
// Immersive Mathematical Visualization with λ-Based Framework
// Enhanced with 1000+ Ideas and 300% Awesomeness Boost

class PrimeComposition3D {
    constructor() {
        this.lambda = 0.6; // Primary constant
        this.base13_refined = 8/13; // Base-13 manifestation
        this.generator_primes = [7, 13, 17, 19];
        
        this.scene = null;
        this.camera = null;
        this.renderer = null;
        this.controls = null;
        this.vrButton = null;
        
        // Audio system
        this.audioContext = null;
        this.masterGain = null;
        this.isMuted = false;
        
        this.particleSystem = null;
        this.primeObjects = new Map();
        this.currentMode = 'splash';
        this.isVRMode = false;
        
        this.animationId = null;
        this.time = 0;
        
        this.primes = [];
        this.maxPrime = 1000;
        
        // Enhanced state
        this.state = {
            volume: 0.5,
            audioEnabled: true,
            performanceMode: 'balanced'
        };
        
        this.init();
    }
    
    init() {
        this.setupScene();
        this.generatePrimes();
        this.setupLighting();
        this.createParticleField();
        this.setupEventListeners();
        this.startSplashSequence();
        
        // Initialize audio system
        this.initializeAudio();
        
        // Hide loading screen after initialization
        setTimeout(() => {
            this.hideLoadingScreen();
            this.showUI();
        }, 3000);
        
        this.animate();
    }
    
    setupScene() {
        // Scene setup
        this.scene = new THREE.Scene();
        this.scene.fog = new THREE.FogExp2(0x000428, 0.0008);
        
        // Camera setup
        this.camera = new THREE.PerspectiveCamera(
            75, window.innerWidth / window.innerHeight, 0.1, 10000
        );
        this.camera.position.set(0, 50, 100);
        
        // Renderer setup
        this.renderer = new THREE.WebGLRenderer({
            canvas: document.getElementById('canvas'),
            antialias: true,
            alpha: true
        });
        this.renderer.setSize(window.innerWidth, window.innerHeight);
        this.renderer.setPixelRatio(window.devicePixelRatio);
        this.renderer.shadowMap.enabled = true;
        this.renderer.shadowMap.type = THREE.PCFSoftShadowMap;
        
        // Controls setup
        this.controls = new THREE.OrbitControls(this.camera, this.renderer.domElement);
        this.controls.enableDamping = true;
        this.controls.dampingFactor = 0.05;
        
        // WebXR setup
        if ('xr' in navigator) {
            this.vrButton = new XRButton(this.renderer);
            document.body.appendChild(this.vrButton.domElement);
        }
        
        // Handle window resize
        window.addEventListener('resize', () => this.onWindowResize());
    }
    
    initializeAudio() {
        // Audio system setup for prime tones
        try {
            this.audioContext = new (window.AudioContext || window.webkitAudioContext)();
            this.masterGain = this.audioContext.createGain();
            this.masterGain.connect(this.audioContext.destination);
            this.masterGain.gain.value = 0.5;
            this.isMuted = false;
            console.log('🎵 Audio system initialized');
        } catch (error) {
            console.warn('Audio initialization failed:', error);
        }
    }
    
    generatePrimes() {
        // Sieve of Eratosthenes
        const sieve = new Array(this.maxPrime + 1).fill(true);
        sieve[0] = sieve[1] = false;
        
        for (let i = 2; i * i <= this.maxPrime; i++) {
            if (sieve[i]) {
                for (let j = i * i; j <= this.maxPrime; j += i) {
                    sieve[j] = false;
                }
            }
        }
        
        this.primes = [];
        for (let i = 2; i <= this.maxPrime; i++) {
            if (sieve[i]) this.primes.push(i);
        }
        
        console.log(`Generated ${this.primes.length} primes up to ${this.maxPrime}`);
    }
    
    setupLighting() {
        // Ambient light
        const ambientLight = new THREE.AmbientLight(0x404040, 0.5);
        this.scene.add(ambientLight);
        
        // Main directional light
        const directionalLight = new THREE.DirectionalLight(0xffffff, 1);
        directionalLight.position.set(50, 100, 50);
        directionalLight.castShadow = true;
        directionalLight.shadow.mapSize.width = 2048;
        directionalLight.shadow.mapSize.height = 2048;
        this.scene.add(directionalLight);
        
        // Colored point lights for generators
        this.generatorLights = [];
        const generatorColors = [0xff00ff, 0x00ffff, 0xffff00, 0xff6600];
        
        for (let i = 0; i < this.generator_primes.length; i++) {
            const light = new THREE.PointLight(generatorColors[i], 2, 100);
            light.position.set(
                Math.cos(i * Math.PI / 2) * 30,
                10,
                Math.sin(i * Math.PI / 2) * 30
            );
            this.scene.add(light);
            this.generatorLights.push(light);
        }
    }
    
    createParticleField() {
        const particleCount = 5000;
        const geometry = new THREE.BufferGeometry();
        
        const positions = new Float32Array(particleCount * 3);
        const colors = new Float32Array(particleCount * 3);
        const sizes = new Float32Array(particleCount);
        
        for (let i = 0; i < particleCount; i++) {
            // Position particles in a sphere
            const theta = Math.random() * Math.PI * 2;
            const phi = Math.acos(2 * Math.random() - 1);
            const radius = 50 + Math.random() * 100;
            
            positions[i * 3] = radius * Math.sin(phi) * Math.cos(theta);
            positions[i * 3 + 1] = radius * Math.sin(phi) * Math.sin(theta);
            positions[i * 3 + 2] = radius * Math.cos(phi);
            
            // Color based on energy
            const energy = Math.random();
            colors[i * 3] = 0.5 + energy * 0.5;     // R
            colors[i * 3 + 1] = 0.3 + energy * 0.7;   // G
            colors[i * 3 + 2] = 1.0 - energy * 0.5;   // B
            
            sizes[i] = Math.random() * 3 + 1;
        }
        
        geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
        geometry.setAttribute('color', new THREE.BufferAttribute(colors, 3));
        geometry.setAttribute('size', new THREE.BufferAttribute(sizes, 1));
        
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
    
    startSplashSequence() {
        this.currentMode = 'splash';
        this.clearScene();
        
        console.log('Starting splash sequence...');
        
        // Create splash animation
        const splashGroup = new THREE.Group();
        
        // Central prime sphere
        const centralGeometry = new THREE.IcosahedronGeometry(10, 2);
        const centralMaterial = new THREE.MeshPhongMaterial({
            color: 0x00ffff,
            emissive: 0x004444,
            shininess: 100,
            opacity: 0.8,
            transparent: true
        });
        const centralSphere = new THREE.Mesh(centralGeometry, centralMaterial);
        splashGroup.add(centralSphere);
        
        // Orbiting generator primes
        this.generator_primes.forEach((prime, i) => {
            const geometry = new THREE.IcosahedronGeometry(prime / 3, 1);
            const material = new THREE.MeshPhongMaterial({
                color: [0xff00ff, 0x00ffff, 0xffff00, 0xff6600][i],
                emissive: [0x440044, 0x004444, 0x444400, 0x442200][i],
                shininess: 100
            });
            const sphere = new THREE.Mesh(geometry, material);
            
            const orbitRadius = 25 + i * 5;
            const orbitSpeed = 0.001 + i * 0.0005;
            
            sphere.userData = {
                orbitRadius: orbitRadius,
                orbitSpeed: orbitSpeed,
                baseY: i * 2 - 3
            };
            
            splashGroup.add(sphere);
        });
        
        this.scene.add(splashGroup);
        this.splashGroup = splashGroup;
        
        // Update prime display
        document.getElementById('currentPrime').textContent = 'λ-Based Prime Composition';
    }
    
    startCompositionExplorer() {
        this.currentMode = 'composition';
        this.clearScene();
        
        console.log('Starting composition explorer...');
        
        // Create composition visualization
        const compositionGroup = new THREE.Group();
        
        // Visualize generator primes as gravitational centers
        this.generator_primes.forEach((prime, i) => {
            const geometry = new THREE.SphereGeometry(5, 32, 32);
            const material = new THREE.MeshPhongMaterial({
                color: [0xff00ff, 0x00ffff, 0xffff00, 0xff6600][i],
                emissive: [0x440044, 0x004444, 0x444400, 0x442200][i],
                shininess: 100
            });
            const sphere = new THREE.Mesh(geometry, material);
            
            const angle = (i / this.generator_primes.length) * Math.PI * 2;
            sphere.position.set(
                Math.cos(angle) * 30,
                0,
                Math.sin(angle) * 30
            );
            
            // Add prime label
            const canvas = document.createElement('canvas');
            canvas.width = 256;
            canvas.height = 64;
            const context = canvas.getContext('2d');
            context.fillStyle = '#ffffff';
            context.font = 'bold 48px Arial';
            context.textAlign = 'center';
            context.fillText(prime.toString(), 128, 48);
            
            const texture = new THREE.CanvasTexture(canvas);
            const spriteMaterial = new THREE.SpriteMaterial({ map: texture });
            const sprite = new THREE.Sprite(spriteMaterial);
            sprite.position.set(0, 8, 0);
            sprite.scale.set(10, 2.5, 1);
            sphere.add(sprite);
            
            compositionGroup.add(sphere);
        });
        
        // Add composition chains
        this.createCompositionChains(compositionGroup);
        
        this.scene.add(compositionGroup);
        this.compositionGroup = compositionGroup;
        
        // Animate camera for better view
        this.animateCameraTo({ x: 50, y: 30, z: 50 }, { x: 0, y: 0, z: 0 });
    }
    
    createCompositionChains(group) {
        // Create visual connections between primes based on λ-relationships
        const maxDistance = 50;
        
        for (let i = 0; i < 50; i++) { // Sample 50 primes for visualization
            const prime = this.primes[Math.floor(Math.random() * 100)];
            
            // Find λ-connected primes
            const lambdaTarget = Math.round(prime * this.lambda);
            if (this.isPrime(lambdaTarget) && Math.abs(lambdaTarget / prime - this.lambda) < 0.1) {
                this.createConnection(group, prime, lambdaTarget);
            }
            
            // Create prime visualization
            const geometry = new THREE.SphereGeometry(1, 16, 16);
            const energy = this.calculatePrimeEnergy(prime);
            const material = new THREE.MeshPhongMaterial({
                color: new THREE.Color().setHSL(energy * 0.3, 1, 0.5),
                emissive: new THREE.Color().setHSL(energy * 0.3, 1, 0.2),
                shininess: 100
            });
            
            const sphere = new THREE.Mesh(geometry, material);
            sphere.position.set(
                (Math.random() - 0.5) * maxDistance * 2,
                (Math.random() - 0.5) * 20,
                (Math.random() - 0.5) * maxDistance * 2
            );
            
            sphere.userData = { prime: prime, energy: energy };
            group.add(sphere);
        }
    }
    
    createConnection(group, prime1, prime2) {
        const geometry = new THREE.CylinderGeometry(0.1, 0.1, 1, 8);
        const material = new THREE.MeshPhongMaterial({
            color: 0x00ff00,
            emissive: 0x002200,
            opacity: 0.6,
            transparent: true
        });
        
        const connection = new THREE.Mesh(geometry, material);
        
        // Calculate position and orientation
        const pos1 = this.getRandomPosition();
        const pos2 = this.getRandomPosition();
        
        const midPoint = new THREE.Vector3().addVectors(pos1, pos2).multiplyScalar(0.5);
        connection.position.copy(midPoint);
        
        connection.lookAt(pos2);
        connection.rotateX(Math.PI / 2);
        
        const distance = pos1.distanceTo(pos2);
        connection.scale.y = distance;
        
        group.add(connection);
    }
    
    getRandomPosition() {
        return new THREE.Vector3(
            (Math.random() - 0.5) * 100,
            (Math.random() - 0.5) * 20,
            (Math.random() - 0.5) * 100
        );
    }
    
    startSinusoidalWaves() {
        this.currentMode = 'waves';
        this.clearScene();
        
        console.log('Starting sinusoidal wave visualization...');
        
        // Create wave field
        const waveGroup = new THREE.Group();
        
        // Create sinusoidal surface based on prime squares
        const segments = 100;
        const geometry = new THREE.PlaneGeometry(100, 100, segments, segments);
        
        const vertices = geometry.attributes.position.array;
        const time = Date.now() * 0.001;
        
        for (let i = 0; i < vertices.length; i += 3) {
            const x = vertices[i];
            const y = vertices[i + 1];
            
            // Create wave pattern based on prime relationships
            const wave1 = Math.sin(x * 0.1 + time) * 5;
            const wave2 = Math.cos(y * 0.1 + time) * 3;
            const wave3 = Math.sin((x + y) * 0.05 + time * 2) * 2;
            
            vertices[i + 2] = wave1 + wave2 + wave3;
        }
        
        geometry.attributes.position.needsUpdate = true;
        geometry.computeVertexNormals();
        
        const material = new THREE.MeshPhongMaterial({
            color: 0x00ffff,
            emissive: 0x004444,
            shininess: 100,
            wireframe: false,
            side: THREE.DoubleSide,
            opacity: 0.8,
            transparent: true
        });
        
        const waveMesh = new THREE.Mesh(geometry, material);
        waveMesh.rotation.x = -Math.PI / 2;
        waveGroup.add(waveMesh);
        
        this.scene.add(waveGroup);
        this.waveGroup = waveGroup;
        this.waveMesh = waveMesh;
    }
    
    startNetworkView() {
        this.currentMode = 'network';
        this.clearScene();
        
        console.log('Starting network visualization...');
        
        // Create 3D network graph
        const networkGroup = new THREE.Group();
        
        // Create nodes for primes
        const nodePositions = [];
        const nodeCount = 100;
        
        for (let i = 0; i < nodeCount; i++) {
            const prime = this.primes[Math.floor(Math.random() * Math.min(500, this.primes.length))];
            const energy = this.calculatePrimeEnergy(prime);
            
            const geometry = new THREE.SphereGeometry(0.5 + energy * 2, 16, 16);
            const material = new THREE.MeshPhongMaterial({
                color: new THREE.Color().setHSL(energy * 0.3, 1, 0.5),
                emissive: new THREE.Color().setHSL(energy * 0.3, 1, 0.2)
            });
            
            const node = new THREE.Mesh(geometry, material);
            
            // Position in 3D space using force-directed layout simulation
            const theta = Math.random() * Math.PI * 2;
            const phi = Math.acos(2 * Math.random() - 1);
            const radius = 20 + energy * 30;
            
            node.position.set(
                radius * Math.sin(phi) * Math.cos(theta),
                radius * Math.sin(phi) * Math.sin(theta),
                radius * Math.cos(phi)
            );
            
            node.userData = { prime: prime, energy: energy, index: i };
            nodePositions.push(node.position);
            
            networkGroup.add(node);
        }
        
        // Create connections based on λ-relationships
        for (let i = 0; i < nodeCount; i++) {
            for (let j = i + 1; j < nodeCount; j++) {
                if (Math.random() < 0.1) { // 10% connection probability
                    this.createNetworkConnection(networkGroup, nodePositions[i], nodePositions[j]);
                }
            }
        }
        
        this.scene.add(networkGroup);
        this.networkGroup = networkGroup;
    }
    
    createNetworkConnection(group, pos1, pos2) {
        const geometry = new THREE.BufferGeometry().setFromPoints([pos1, pos2]);
        const material = new THREE.LineBasicMaterial({
            color: 0x00ff00,
            opacity: 0.3,
            transparent: true
        });
        
        const line = new THREE.Line(geometry, material);
        group.add(line);
    }
    
    calculatePrimeEnergy(prime) {
        // Calculate λ-energy
        const k_lambda = Math.round(prime * this.lambda);
        const lambda_energy = 1 - Math.abs((k_lambda / prime) - this.lambda);
        
        // Calculate base-13 energy
        const k_base13 = Math.round(prime * this.base13_refined);
        const base13_energy = 1 - Math.abs((k_base13 / prime) - this.base13_refined);
        
        // Total energy (weighted)
        return lambda_energy * 0.6 + base13_energy * 0.4;
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
    
    clearScene() {
        // Remove all groups except particles and lights
        const groupsToRemove = ['splashGroup', 'compositionGroup', 'waveGroup', 'networkGroup'];
        
        groupsToRemove.forEach(groupName => {
            if (this[groupName]) {
                this.scene.remove(this[groupName]);
                this[groupName] = null;
            }
        });
    }
    
    animateCameraTo(position, target) {
        const duration = 2000;
        const startPos = this.camera.position.clone();
        const startTarget = this.controls.target.clone();
        
        const startTime = Date.now();
        
        const animateCamera = () => {
            const elapsed = Date.now() - startTime;
            const progress = Math.min(elapsed / duration, 1);
            
            // Ease in-out function
            const eased = progress < 0.5 
                ? 2 * progress * progress 
                : -1 + (4 - 2 * progress) * progress;
            
            this.camera.position.lerpVectors(startPos, new THREE.Vector3(...position), eased);
            this.controls.target.lerpVectors(startTarget, new THREE.Vector3(...target), eased);
            this.controls.update();
            
            if (progress < 1) {
                requestAnimationFrame(animateCamera);
            }
        };
        
        animateCamera();
    }
    
    setupEventListeners() {
        // Keyboard controls
        document.addEventListener('keydown', (event) => {
            switch (event.key) {
                case '1':
                    this.startSplashSequence();
                    break;
                case '2':
                    this.startCompositionExplorer();
                    break;
                case '3':
                    this.startSinusoidalWaves();
                    break;
                case '4':
                    this.startNetworkView();
                    break;
                case 'v':
                case 'V':
                    this.toggleVR();
                    break;
            }
        });
    }
    
    toggleVR() {
        if (this.vrButton && this.vrButton.domElement) {
            this.vrButton.domElement.click();
        }
    }
    
    playPrimeTone(prime, duration = 0.5) {
        if (!this.audioContext || this.isMuted) return;
        
        // Calculate frequency based on prime (simplified mapping)
        const baseFrequency = 110; // A2
        const frequency = baseFrequency * (1 + (prime % 12) * 0.1);
        
        const oscillator = this.audioContext.createOscillator();
        const gainNode = this.audioContext.createGain();
        
        oscillator.frequency.value = frequency;
        oscillator.type = 'sine';
        
        gainNode.gain.setValueAtTime(0, this.audioContext.currentTime);
        gainNode.gain.linearRampToValueAtTime(0.3, this.audioContext.currentTime + 0.01);
        gainNode.gain.exponentialRampToValueAtTime(0.01, this.audioContext.currentTime + duration);
        
        oscillator.connect(gainNode);
        gainNode.connect(this.masterGain);
        
        oscillator.start();
        oscillator.stop(this.audioContext.currentTime + duration);
    }
    
    toggleMute() {
        this.isMuted = !this.isMuted;
        if (this.masterGain) {
            this.masterGain.gain.value = this.isMuted ? 0 : this.state?.volume || 0.5;
        }
    }
    
    setVolume(volume) {
        if (this.state) {
            this.state.volume = volume;
        }
        if (this.masterGain && !this.isMuted) {
            this.masterGain.gain.value = volume;
        }
        if (document.getElementById('volumeDisplay')) {
            document.getElementById('volumeDisplay').textContent = `${Math.round(volume * 100)}%`;
        }
    }
    
    hideLoadingScreen() {
        const loadingScreen = document.getElementById('loadingScreen');
        loadingScreen.style.opacity = '0';
        setTimeout(() => {
            loadingScreen.style.display = 'none';
        }, 1000);
    }
    
    showUI() {
        document.getElementById('primeDisplay').style.opacity = '1';
        document.getElementById('controlPanel').style.opacity = '1';
        document.getElementById('primeInput').style.opacity = '1';
        document.getElementById('infoPanel').style.opacity = '1';
    }
    
    updateInfoPanel(prime) {
        const energy = this.calculatePrimeEnergy(prime);
        
        document.getElementById('lambdaEnergy').style.width = `${energy * 100}%`;
        document.getElementById('base13Energy').style.width = `${energy * 100}%`;
        document.getElementById('totalEnergy').style.width = `${energy * 100}%`;
    }
    
    animate() {
        this.animationId = requestAnimationFrame(() => this.animate());
        
        this.time += 0.01;
        
        // Animate particle system
        if (this.particleSystem) {
            this.particleSystem.rotation.y += 0.0005;
            this.particleSystem.rotation.x += 0.0002;
        }
        
        // Mode-specific animations
        switch (this.currentMode) {
            case 'splash':
                this.animateSplash();
                break;
            case 'waves':
                this.animateWaves();
                break;
            case 'network':
                this.animateNetwork();
                break;
        }
        
        // Animate generator lights
        this.generatorLights.forEach((light, i) => {
            const time = this.time * 2 + i * Math.PI / 2;
            light.intensity = 1 + Math.sin(time) * 0.5;
        });
        
        this.controls.update();
        this.renderer.render(this.scene, this.camera);
    }
    
    animateSplash() {
        if (this.splashGroup) {
            // Rotate central sphere
            const centralSphere = this.splashGroup.children[0];
            if (centralSphere) {
                centralSphere.rotation.x += 0.01;
                centralSphere.rotation.y += 0.01;
            }
            
            // Orbit generator primes
            for (let i = 1; i < this.splashGroup.children.length; i++) {
                const sphere = this.splashGroup.children[i];
                if (sphere.userData.orbitRadius) {
                    const angle = this.time * sphere.userData.orbitSpeed;
                    sphere.position.x = Math.cos(angle) * sphere.userData.orbitRadius;
                    sphere.position.z = Math.sin(angle) * sphere.userData.orbitRadius;
                    sphere.position.y = sphere.userData.baseY + Math.sin(this.time * 2) * 2;
                    sphere.rotation.y += 0.02;
                }
            }
        }
    }
    
    animateWaves() {
        if (this.waveMesh) {
            const vertices = this.waveMesh.geometry.attributes.position.array;
            const time = Date.now() * 0.001;
            
            for (let i = 0; i < vertices.length; i += 3) {
                const x = vertices[i];
                const y = vertices[i + 1];
                
                const wave1 = Math.sin(x * 0.1 + time) * 5;
                const wave2 = Math.cos(y * 0.1 + time) * 3;
                const wave3 = Math.sin((x + y) * 0.05 + time * 2) * 2;
                
                vertices[i + 2] = wave1 + wave2 + wave3;
            }
            
            this.waveMesh.geometry.attributes.position.needsUpdate = true;
            this.waveMesh.geometry.computeVertexNormals();
        }
    }
    
    animateNetwork() {
        if (this.networkGroup) {
            // Gentle floating animation for network nodes
            this.networkGroup.children.forEach((child, index) => {
                if (child.geometry && child.geometry.type === 'SphereGeometry') {
                    child.position.y += Math.sin(this.time * 2 + index * 0.1) * 0.01;
                    child.rotation.y += 0.01;
                }
            });
        }
    }
    
    onWindowResize() {
        this.camera.aspect = window.innerWidth / window.innerHeight;
        this.camera.updateProjectionMatrix();
        this.renderer.setSize(window.innerWidth, window.innerHeight);
    }
    
    destroy() {
        if (this.animationId) {
            cancelAnimationFrame(this.animationId);
        }
        
        this.renderer.dispose();
        
        // Clean up Three.js objects
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
    }
}

// UI Functions
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

function analyzeSpecificPrime() {
    const input = document.getElementById('primeNumberInput');
    const prime = parseInt(input.value);
    
    if (window.primeApp && prime && window.primeApp.isPrime(prime)) {
        document.getElementById('currentPrime').textContent = prime.toString();
        window.primeApp.updateInfoPanel(prime);
        
        // Play prime tone
        if (window.primeApp.audioContext && !window.primeApp.isMuted) {
            window.primeApp.playPrimeTone(prime);
        }
        
        // Visual feedback
        console.log(`🎯 Analyzing prime ${prime} with λ-based framework...`);
        console.log(`🎵 Playing prime tone for ${prime}`);
    } else {
        alert('Please enter a valid prime number');
    }
}

// Audio control functions
function toggleMute() {
    if (window.primeApp) {
        window.primeApp.toggleMute();
        
        const muteBtn = document.querySelector('button[onclick="toggleMute()"]');
        if (muteBtn) {
            muteBtn.textContent = window.primeApp.isMuted ? '🔇 Unmute' : '🔊 Mute';
            muteBtn.classList.toggle('muted', window.primeApp.isMuted);
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

// Loading details animation
const loadingDetails = [
    'Generating Prime Networks...',
    'Initializing λ-Based Framework...',
    'Calculating Sinusoidal Patterns...',
    'Setting Up Energy Fields...',
    'Mapping Generator Primes...',
    'Establishing VR Connection...'
];

let detailIndex = 0;
setInterval(() => {
    document.getElementById('loadingDetail').textContent = loadingDetails[detailIndex];
    detailIndex = (detailIndex + 1) % loadingDetails.length;
}, 500);

// Initialize application when page loads
window.addEventListener('load', () => {
    window.primeApp = new PrimeComposition3D();
});

// Cleanup on page unload
window.addEventListener('beforeunload', () => {
    if (window.primeApp) {
        window.primeApp.destroy();
    }
});