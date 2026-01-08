#version 410 core

in vec3 FragPos;
in vec3 Normal;
in vec2 TexCoord;
in float VertexHeight;

out vec4 FragColor;

uniform vec3 lightPos;
uniform vec3 lightColor;
uniform vec3 viewPos;
uniform float time;
uniform vec3 objectColor;

void main()
{
    // Ambient lighting
    float ambientStrength = 0.2;
    vec3 ambient = ambientStrength * lightColor;
    
    // Diffuse lighting
    vec3 norm = normalize(Normal);
    vec3 lightDir = normalize(lightPos - FragPos);
    float diff = max(dot(norm, lightDir), 0.0);
    vec3 diffuse = diff * lightColor;
    
    // Specular lighting
    float specularStrength = 0.5;
    vec3 viewDir = normalize(viewPos - FragPos);
    vec3 reflectDir = reflect(-lightDir, norm);
    float spec = pow(max(dot(viewDir, reflectDir), 0.0), 32);
    vec3 specular = specularStrength * spec * lightColor;
    
    // Prime-based color calculation
    vec3 baseColor = objectColor;
    
    // Add pulsing effect based on time and height
    float pulse = sin(time * 2.0 + VertexHeight * 5.0) * 0.3 + 0.7;
    baseColor *= pulse;
    
    // Lambda-based color shifting
    float lambdaEffect = sin(time * 1.618 + FragPos.x) * 0.1;
    baseColor.r += lambdaEffect;
    baseColor.b -= lambdaEffect;
    
    // Combine lighting
    vec3 result = (ambient + diffuse + specular) * baseColor;
    
    // Add glow effect for high-energy primes
    float glowIntensity = sin(time * 3.0) * 0.5 + 0.5;
    result += vec3(0.1, 0.3, 0.6) * glowIntensity * 0.3;
    
    // Ensure color values are in valid range
    result = clamp(result, 0.0, 1.0);
    
    FragColor = vec4(result, 1.0);
}