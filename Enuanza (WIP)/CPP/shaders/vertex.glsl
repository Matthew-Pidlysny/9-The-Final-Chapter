#version 410 core

layout (location = 0) in vec3 aPos;
layout (location = 1) in vec3 aNormal;
layout (location = 2) in vec2 aTexCoord;

out vec3 FragPos;
out vec3 Normal;
out vec2 TexCoord;
out float VertexHeight;

uniform mat4 model;
uniform mat4 view;
uniform mat4 projection;
uniform float time;

void main()
{
    FragPos = vec3(model * vec4(aPos, 1.0));
    Normal = mat3(transpose(inverse(model))) * aNormal;
    TexCoord = aTexCoord;
    VertexHeight = aPos.y;
    
    // Add wave animation
    vec3 animatedPos = aPos;
    animatedPos.y += sin(time + aPos.x * 2.0) * 0.1;
    animatedPos.x += cos(time + aPos.z * 2.0) * 0.05;
    
    gl_Position = projection * view * model * vec4(animatedPos, 1.0);
}