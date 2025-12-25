/*
 * Math Utilities - SIMD Optimized
 */

#ifndef MATH_UTILS_HPP
#define MATH_UTILS_HPP

#include <cmath>
#include <immintrin.h> // For SIMD
#include <algorithm>

namespace privanna::math {

// Vector3 with SIMD optimization
struct alignas(16) Vector3 {
    union {
        struct { float x, y, z, w; };
        __m128 simd;
    };
    
    Vector3(float x = 0, float y = 0, float z = 0) : x(x), y(y), z(z), w(0) {}
    Vector3(__m128 v) : simd(v) {}
    
    Vector3 operator+(const Vector3& other) const {
        return Vector3(_mm_add_ps(simd, other.simd));
    }
    
    Vector3 operator-(const Vector3& other) const {
        return Vector3(_mm_sub_ps(simd, other.simd));
    }
    
    Vector3 operator*(float scalar) const {
        return Vector3(_mm_mul_ps(simd, _mm_set1_ps(scalar)));
    }
    
    float dot(const Vector3& other) const {
        __m128 result = _mm_mul_ps(simd, other.simd);
        result = _mm_hadd_ps(result, result);
        result = _mm_hadd_ps(result, result);
        return _mm_cvtss_f32(result);
    }
    
    float length_squared() const {
        return dot(*this);
    }
    
    float length() const {
        return std::sqrt(length_squared());
    }
    
    Vector3 normalized() const {
        float len = length();
        return len > 0 ? *this * (1.0f / len) : Vector3();
    }
};

// Matrix4x4 with SIMD optimization
struct alignas(16) Matrix4x4 {
    union {
        float m[16];
        __m128 rows[4];
    };
    
    Matrix4x4() {
        // Identity matrix
        rows[0] = _mm_set_ps(0, 0, 0, 1);
        rows[1] = _mm_set_ps(0, 0, 1, 0);
        rows[2] = _mm_set_ps(0, 1, 0, 0);
        rows[3] = _mm_set_ps(1, 0, 0, 0);
    }
    
    Vector3 transform_point(const Vector3& point) const {
        __m128 result = _mm_mul_ps(point.simd, rows[0]);
        result = _mm_add_ps(result, _mm_mul_ps(point.simd, rows[1]));
        result = _mm_add_ps(result, _mm_mul_ps(point.simd, rows[2]));
        result = _mm_add_ps(result, rows[3]);
        return Vector3(result);
    }
};

// Math constants
constexpr float PI = 3.14159265358979323846f;
constexpr float TWO_PI = 2.0f * PI;
constexpr float HALF_PI = PI * 0.5f;
constexpr float EPSILON = 1e-6f;

// Fast math functions
inline float fast_sqrt(float x) {
    return _mm_cvtss_f32(_mm_sqrt_ss(_mm_set_ss(x)));
}

inline float fast_inv_sqrt(float x) {
    return _mm_cvtss_f32(_mm_rsqrt_ss(_mm_set_ss(x)));
}

inline float fast_abs(float x) {
    return std::abs(x);
}

inline float fast_min(float a, float b) {
    return _mm_cvtss_f32(_mm_min_ss(_mm_set_ss(a), _mm_set_ss(b)));
}

inline float fast_max(float a, float b) {
    return _mm_cvtss_f32(_mm_max_ss(_mm_set_ss(a), _mm_set_ss(b)));
}

inline float fast_clamp(float x, float min_val, float max_val) {
    return fast_min(fast_max(x, min_val), max_val);
}

inline float fast_lerp(float a, float b, float t) {
    return a + (b - a) * fast_clamp(t, 0.0f, 1.0f);
}

inline bool fast_equals(float a, float b, float epsilon = EPSILON) {
    return fast_abs(a - b) < epsilon;
}

// Random number generator
class FastRandom {
private:
    uint32_t state_;
    
public:
    FastRandom(uint32_t seed = 12345) : state_(seed) {}
    
    uint32_t next_uint32() {
        state_ = state_ * 1103515245 + 12345;
        return state_;
    }
    
    float next_float() {
        return (next_uint32() & 0xFFFFFF) / static_cast<float>(0xFFFFFF);
    }
    
    float next_float(float min_val, float max_val) {
        return fast_lerp(min_val, max_val, next_float());
    }
    
    Vector3 next_unit_vector() {
        float theta = next_float(0.0f, TWO_PI);
        float phi = next_float(0.0f, PI);
        float sin_phi = std::sin(phi);
        return Vector3(
            sin_phi * std::cos(theta),
            sin_phi * std::sin(theta),
            std::cos(phi)
        );
    }
};

} // namespace privanna::math

#endif // MATH_UTILS_HPP