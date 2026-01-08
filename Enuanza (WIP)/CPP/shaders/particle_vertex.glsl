#version 410 core

layout (location = 0) in vec3 aPos;
layout (location = 1) in vec4 aColor;
layout (location = 2) in float aLife;
layout (location = 3) in float aSize;

out vec4 ParticleColor;
out float ParticleLife;

uniform mat4 view;
uniform mat4 projection;
uniform float time;

void main()
{
    ParticleColor = aColor;
    ParticleLife = aLife;
    
    // Apply particle animation
    vec3 animatedPos = aPos;
    animatedPos.y += sin(time + aPos.x * 10.0) * aLife * 0.1;
    animatedPos.x += cos(time + aPos.z * 10.0) * aLife * 0.05;
    
    // Billboarding: make particles face the camera
    vec4 viewPos = view * vec4(animatedPos, 1.0);
    gl_Position = projection * viewPos;
    
    // Set point size based on particle size and life
    gl_PointSize = aSize * 1000.0 * aLife / length(viewPos.xyz);
}