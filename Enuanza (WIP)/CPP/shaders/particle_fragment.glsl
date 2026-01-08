#version 410 core

in vec4 ParticleColor;
in float ParticleLife;

out vec4 FragColor;

uniform float time;

void main()
{
    // Create circular particles
    vec2 coord = gl_PointCoord - vec2(0.5);
    float distance = length(coord);
    
    if (distance > 0.5) {
        discard;
    }
    
    // Create soft edges
    float alpha = 1.0 - smoothstep(0.3, 0.5, distance);
    
    // Base color with pulsing effect
    vec3 color = ParticleColor.rgb;
    
    // Add rainbow effect based on time and life
    float rainbowEffect = sin(time * 2.0 + ParticleLife * 5.0) * 0.3;
    color.r += rainbowEffect;
    color.g += sin(time * 3.0 + ParticleLife * 3.0) * 0.3;
    color.b += cos(time * 4.0 + ParticleLife * 2.0) * 0.3;
    
    // Apply life-based fading
    alpha *= ParticleLife;
    
    // Add glow for high-energy particles
    float glow = sin(time * 5.0) * 0.5 + 0.5;
    color += vec3(0.2, 0.4, 0.8) * glow * 0.5;
    
    // Clamp values
    color = clamp(color, 0.0, 1.0);
    alpha = clamp(alpha, 0.0, 1.0);
    
    FragColor = vec4(color, alpha);
}