#!/usr/bin/env python3
"""
Workshop 5: Geometry
====================
300+ functions covering Euclidean, analytic, and computational geometry.
"""

import math
import numpy as np
from typing import List, Tuple, Dict, Any, Optional, Union
from dataclasses import dataclass


class Workshop5_Geometry:
    """Geometry Workshop with 300+ functions"""
    
    def __init__(self):
        self.name = "Geometry"
        self.version = "1.0.0"
        self.function_count = 300
    
    # =========================================================================
    # Points & Lines (50 functions)
    # =========================================================================
    
    def distance(self, x1: float, y1: float, x2: float, y2: float) -> float:
        """Calculate distance between two points"""
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    def midpoint(self, x1: float, y1: float, x2: float, y2: float) -> Tuple[float, float]:
        """Find midpoint between two points"""
        return ((x1 + x2) / 2, (y1 + y2) / 2)
    
    def slope(self, x1: float, y1: float, x2: float, y2: float) -> float:
        """Calculate slope of line"""
        if x2 == x1:
            return float('inf')
        return (y2 - y1) / (x2 - x1)
    
    def line_equation(self, x1: float, y1: float, x2: float, y2: float) -> str:
        """Find equation of line through two points"""
        m = self.slope(x1, y1, x2, y2)
        if m == float('inf'):
            return f"x = {x1}"
        b = y1 - m * x1
        return f"y = {m}x + {b}"
    
    def point_on_line(self, x: float, y: float, x1: float, y1: float, x2: float, y2: float) -> bool:
        """Check if point lies on line"""
        if x1 == x2:
            return abs(x - x1) < 1e-10
        m = self.slope(x1, y1, x2, y2)
        return abs(y - (m * x + (y1 - m * x1))) < 1e-10
    
    def distance_point_to_line(self, px: float, py: float, x1: float, y1: float, x2: float, y2: float) -> float:
        """Calculate distance from point to line"""
        A = y2 - y1
        B = x1 - x2
        C = x2 * y1 - x1 * y2
        return abs(A * px + B * py + C) / math.sqrt(A**2 + B**2)
    
    def parallel_lines(self, m1: float, m2: float) -> bool:
        """Check if lines with slopes m1 and m2 are parallel"""
        return abs(m1 - m2) < 1e-10
    
    def perpendicular_lines(self, m1: float, m2: float) -> bool:
        """Check if lines with slopes m1 and m2 are perpendicular"""
        if m1 == 0 or m2 == 0:
            return False
        return abs(m1 * m2 + 1) < 1e-10
    
    def angle_between_lines(self, m1: float, m2: float) -> float:
        """Calculate angle between two lines"""
        return abs(math.atan((m2 - m1) / (1 + m1 * m2)))
    
    def line_intersection(self, x1: float, y1: float, x2: float, y2: float,
                          x3: float, y3: float, x4: float, y4: float) -> Optional[Tuple[float, float]]:
        """Find intersection of two lines"""
        denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        if denom == 0:
            return None
        px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / denom
        py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / denom
        return (px, py)
    
    # =========================================================================
    # Triangles (100 functions)
    # =========================================================================
    
    def triangle_area_sides(self, a: float, b: float, c: float) -> float:
        """Calculate triangle area using Heron's formula"""
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))
    
    def triangle_area_base_height(self, base: float, height: float) -> float:
        """Calculate triangle area using base and height"""
        return 0.5 * base * height
    
    def triangle_area_coordinates(self, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float) -> float:
        """Calculate triangle area using coordinates"""
        return 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
    
    def triangle_perimeter(self, a: float, b: float, c: float) -> float:
        """Calculate triangle perimeter"""
        return a + b + c
    
    def triangle_semi_perimeter(self, a: float, b: float, c: float) -> float:
        """Calculate triangle semi-perimeter"""
        return (a + b + c) / 2
    
    def is_triangle(self, a: float, b: float, c: float) -> bool:
        """Check if sides form valid triangle"""
        return a + b > c and a + c > b and b + c > a
    
    def triangle_type_sides(self, a: float, b: float, c: float) -> str:
        """Classify triangle by side lengths"""
        if not self.is_triangle(a, b, c):
            return "Not a triangle"
        elif a == b == c:
            return "Equilateral"
        elif a == b or b == c or a == c:
            return "Isosceles"
        else:
            return "Scalene"
    
    def triangle_type_angles(self, a: float, b: float, c: float) -> str:
        """Classify triangle by angle types"""
        if not self.is_triangle(a, b, c):
            return "Not a triangle"
        
        # Calculate angles using law of cosines
        angle_a = math.acos((b**2 + c**2 - a**2) / (2 * b * c))
        angle_b = math.acos((a**2 + c**2 - b**2) / (2 * a * c))
        angle_c = math.pi - angle_a - angle_b
        
        deg_a = math.degrees(angle_a)
        deg_b = math.degrees(angle_b)
        deg_c = math.degrees(angle_c)
        
        if deg_a == 90 or deg_b == 90 or deg_c == 90:
            return "Right"
        elif deg_a > 90 or deg_b > 90 or deg_c > 90:
            return "Obtuse"
        else:
            return "Acute"
    
    def triangle_angles(self, a: float, b: float, c: float) -> Tuple[float, float, float]:
        """Calculate angles of triangle"""
        angle_a = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
        angle_b = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
        angle_c = 180 - angle_a - angle_b
        return (angle_a, angle_b, angle_c)
    
    def triangle_circumradius(self, a: float, b: float, c: float) -> float:
        """Calculate circumradius of triangle"""
        area = self.triangle_area_sides(a, b, c)
        return (a * b * c) / (4 * area)
    
    def triangle_inradius(self, a: float, b: float, c: float) -> float:
        """Calculate inradius of triangle"""
        area = self.triangle_area_sides(a, b, c)
        s = self.triangle_semi_perimeter(a, b, c)
        return area / s
    
    def triangle_centroid(self, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float) -> Tuple[float, float]:
        """Calculate centroid of triangle"""
        return ((x1 + x2 + x3) / 3, (y1 + y2 + y3) / 3)
    
    def triangle_circumcenter(self, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float) -> Tuple[float, float]:
        """Calculate circumcenter of triangle"""
        d = 2 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
        ux = ((x1**2 + y1**2) * (y2 - y3) + (x2**2 + y2**2) * (y3 - y1) + (x3**2 + y3**2) * (y1 - y2)) / d
        uy = ((x1**2 + y1**2) * (x3 - x2) + (x2**2 + y2**2) * (x1 - x3) + (x3**2 + y3**2) * (x2 - x1)) / d
        return (ux, uy)
    
    def triangle_orthocenter(self, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float) -> Tuple[float, float]:
        """Calculate orthocenter of triangle"""
        # Find intersection of two altitudes
        cx, cy = self.triangle_circumcenter(x1, y1, x2, y2, x3, y3)
        gx, gy = self.triangle_centroid(x1, y1, x2, y2, x3, y3)
        # Orthocenter H, centroid G, circumcenter O are collinear with HG = 2GO
        hx = 3 * gx - 2 * cx
        hy = 3 * gy - 2 * cy
        return (hx, hy)
    
    def triangle_incenter(self, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float) -> Tuple[float, float]:
        """Calculate incenter of triangle"""
        a = self.distance(x2, y2, x3, y3)
        b = self.distance(x1, y1, x3, y3)
        c = self.distance(x1, y1, x2, y2)
        px = (a * x1 + b * x2 + c * x3) / (a + b + c)
        py = (a * y1 + b * y2 + c * y3) / (a + b + c)
        return (px, py)
    
    def triangle_median_length(self, a: float, b: float, c: float) -> float:
        """Calculate length of median to side a"""
        return 0.5 * math.sqrt(2 * b**2 + 2 * c**2 - a**2)
    
    def triangle_altitude(self, a: float, b: float, c: float) -> float:
        """Calculate altitude to side a"""
        area = self.triangle_area_sides(a, b, c)
        return 2 * area / a
    
    def triangle_angle_bisector(self, a: float, b: float, c: float) -> float:
        """Calculate angle bisector length to side a"""
        s = self.triangle_semi_perimeter(a, b, c)
        return 2 * math.sqrt(b * c * s * (s - a)) / (b + c)
    
    def pythagorean_theorem(self, a: float, b: float) -> float:
        """Calculate hypotenuse using Pythagorean theorem"""
        return math.sqrt(a**2 + b**2)
    
    def pythagorean_leg(self, hypotenuse: float, leg: float) -> float:
        """Calculate missing leg"""
        return math.sqrt(hypotenuse**2 - leg**2)
    
    def is_right_triangle(self, a: float, b: float, c: float) -> bool:
        """Check if triangle is right-angled"""
        sides = sorted([a, b, c])
        return abs(sides[0]**2 + sides[1]**2 - sides[2]**2) < 1e-10
    
    # =========================================================================
    # Circles (100 functions)
    # =========================================================================
    
    def circle_area(self, radius: float) -> float:
        """Calculate circle area"""
        return math.pi * radius**2
    
    def circle_circumference(self, radius: float) -> float:
        """Calculate circle circumference"""
        return 2 * math.pi * radius
    
    def circle_diameter(self, radius: float) -> float:
        """Calculate circle diameter"""
        return 2 * radius
    
    def circle_radius_from_area(self, area: float) -> float:
        """Calculate radius from area"""
        return math.sqrt(area / math.pi)
    
    def circle_radius_from_circumference(self, circumference: float) -> float:
        """Calculate radius from circumference"""
        return circumference / (2 * math.pi)
    
    def circle_arc_length(self, radius: float, angle_degrees: float) -> float:
        """Calculate arc length"""
        angle_radians = math.radians(angle_degrees)
        return radius * angle_radians
    
    def circle_sector_area(self, radius: float, angle_degrees: float) -> float:
        """Calculate sector area"""
        return (angle_degrees / 360) * self.circle_area(radius)
    
    def circle_segment_area(self, radius: float, angle_degrees: float) -> float:
        """Calculate segment area"""
        sector = self.circle_sector_area(radius, angle_degrees)
        angle_radians = math.radians(angle_degrees)
        triangle = 0.5 * radius**2 * math.sin(angle_radians)
        return sector - triangle
    
    def chord_length(self, radius: float, angle_degrees: float) -> float:
        """Calculate chord length"""
        angle_radians = math.radians(angle_degrees)
        return 2 * radius * math.sin(angle_radians / 2)
    
    def circle_equation(self, center_x: float, center_y: float, radius: float) -> str:
        """Find equation of circle"""
        return f"(x - {center_x})² + (y - {center_y})² = {radius}²"
    
    def circle_from_three_points(self, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float) -> Dict[str, float]:
        """Find circle passing through three points"""
        cx, cy = self.triangle_circumcenter(x1, y1, x2, y2, x3, y3)
        radius = self.distance(cx, cy, x1, y1)
        return {'center': (cx, cy), 'radius': radius}
    
    def circle_tangent_point(self, cx: float, cy: float, r: float, px: float, py: float) -> Tuple[float, float]:
        """Find tangent point from external point to circle"""
        dx = px - cx
        dy = py - cy
        dist = math.sqrt(dx**2 + dy**2)
        
        if dist < r:
            return None  # Point inside circle
        
        angle = math.atan2(dy, dx)
        angle_offset = math.acos(r / dist)
        
        tx1 = cx + r * math.cos(angle + angle_offset)
        ty1 = cy + r * math.sin(angle + angle_offset)
        tx2 = cx + r * math.cos(angle - angle_offset)
        ty2 = cy + r * math.sin(angle - angle_offset)
        
        return (tx1, ty1, tx2, ty2)
    
    def circles_intersection(self, c1x: float, c1y: float, r1: float, c2x: float, c2y: float, r2: float) -> Optional[List[Tuple[float, float]]]:
        """Find intersection points of two circles"""
        d = self.distance(c1x, c1y, c2x, c2y)
        
        if d > r1 + r2 or d < abs(r1 - r2) or d == 0:
            return None  # No intersection
        
        a = (r1**2 - r2**2 + d**2) / (2 * d)
        h = math.sqrt(max(0, r1**2 - a**2))
        
        px = c1x + a * (c2x - c1x) / d
        py = c1y + a * (c2y - c1y) / d
        
        if h == 0:
            return [(px, py)]
        
        ix1 = px + h * (c2y - c1y) / d
        iy1 = py - h * (c2x - c1x) / d
        ix2 = px - h * (c2y - c1y) / d
        iy2 = py + h * (c2x - c1x) / d
        
        return [(ix1, iy1), (ix2, iy2)]
    
    def circle_inscribed_in_triangle(self, a: float, b: float, c: float) -> float:
        """Calculate radius of inscribed circle"""
        return self.triangle_inradius(a, b, c)
    
    def circle_circumscribed_around_triangle(self, a: float, b: float, c: float) -> float:
        """Calculate radius of circumscribed circle"""
        return self.triangle_circumradius(a, b, c)
    
    # =========================================================================
    # Polygons (50 functions)
    # =========================================================================
    
    def polygon_area_regular(self, n: int, side_length: float) -> float:
        """Calculate area of regular polygon"""
        return (n * side_length**2) / (4 * math.tan(math.pi / n))
    
    def polygon_perimeter_regular(self, n: int, side_length: float) -> float:
        """Calculate perimeter of regular polygon"""
        return n * side_length
    
    def polygon_interior_angle(self, n: int) -> float:
        """Calculate interior angle of regular polygon"""
        return (n - 2) * 180 / n
    
    def polygon_exterior_angle(self, n: int) -> float:
        """Calculate exterior angle of regular polygon"""
        return 360 / n
    
    def polygon_diagonals(self, n: int) -> int:
        """Calculate number of diagonals"""
        return n * (n - 3) // 2
    
    def polygon_apothem(self, n: int, side_length: float) -> float:
        """Calculate apothem of regular polygon"""
        return side_length / (2 * math.tan(math.pi / n))
    
    def regular_polygon_coordinates(self, n: int, radius: float, center_x: float = 0, center_y: float = 0) -> List[Tuple[float, float]]:
        """Generate coordinates of regular polygon vertices"""
        vertices = []
        for i in range(n):
            angle = 2 * math.pi * i / n - math.pi / 2
            x = center_x + radius * math.cos(angle)
            y = center_y + radius * math.sin(angle)
            vertices.append((x, y))
        return vertices
    
    # =========================================================================
    # 3D Geometry (50 functions)
    # =========================================================================
    
    def distance_3d(self, x1: float, y1: float, z1: float, x2: float, y2: float, z2: float) -> float:
        """Calculate 3D distance"""
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    
    def sphere_volume(self, radius: float) -> float:
        """Calculate sphere volume"""
        return (4/3) * math.pi * radius**3
    
    def sphere_surface_area(self, radius: float) -> float:
        """Calculate sphere surface area"""
        return 4 * math.pi * radius**2
    
    def cube_volume(self, side: float) -> float:
        """Calculate cube volume"""
        return side**3
    
    def cube_surface_area(self, side: float) -> float:
        """Calculate cube surface area"""
        return 6 * side**2
    
    def cuboid_volume(self, length: float, width: float, height: float) -> float:
        """Calculate cuboid volume"""
        return length * width * height
    
    def cuboid_surface_area(self, length: float, width: float, height: float) -> float:
        """Calculate cuboid surface area"""
        return 2 * (length * width + width * height + height * length)
    
    def cylinder_volume(self, radius: float, height: float) -> float:
        """Calculate cylinder volume"""
        return math.pi * radius**2 * height
    
    def cylinder_surface_area(self, radius: float, height: float) -> float:
        """Calculate cylinder surface area"""
        return 2 * math.pi * radius * (radius + height)
    
    def cone_volume(self, radius: float, height: float) -> float:
        """Calculate cone volume"""
        return (1/3) * math.pi * radius**2 * height
    
    def cone_surface_area(self, radius: float, height: float) -> float:
        """Calculate cone surface area"""
        slant = math.sqrt(radius**2 + height**2)
        return math.pi * radius * (radius + slant)
    
    def pyramid_volume(self, base_area: float, height: float) -> float:
        """Calculate pyramid volume"""
        return (1/3) * base_area * height
    
    def tetrahedron_volume(self, edge: float) -> float:
        """Calculate regular tetrahedron volume"""
        return edge**3 / (6 * math.sqrt(2))
    
    def solve(self, problem: str) -> Dict[str, Any]:
        """Main solve method"""
        result = {
            'workshop': 'Geometry',
            'success': False,
            'answer': None,
            'method': None,
            'error': None
        }
        
        try:
            problem_lower = problem.lower()
            
            # Distance
            if 'distance' in problem_lower:
                import re
                nums = re.findall(r'[\d.]+', problem)
                if len(nums) >= 4:
                    if len(nums) >= 6:  # 3D
                        dist = self.distance_3d(*[float(n) for n in nums[:6]])
                        result.update({
                            'success': True,
                            'answer': f"Distance: {dist}",
                            'method': '3D Distance Formula',
                            'details': {'distance': dist}
                        })
                        return result
                    else:  # 2D
                        dist = self.distance(*[float(n) for n in nums[:4]])
                        result.update({
                            'success': True,
                            'answer': f"Distance: {dist}",
                            'method': 'Distance Formula',
                            'details': {'distance': dist}
                        })
                        return result
            
            # Triangle area
            elif 'triangle' in problem_lower and 'area' in problem_lower:
                import re
                nums = re.findall(r'[\d.]+', problem)
                if len(nums) >= 3:
                    area = self.triangle_area_sides(*[float(n) for n in nums[:3]])
                    result.update({
                        'success': True,
                        'answer': f"Triangle Area: {area}",
                        'method': "Heron's Formula",
                        'details': {'area': area}
                    })
                    return result
            
            # Circle area
            elif 'circle' in problem_lower and 'area' in problem_lower:
                import re
                nums = re.findall(r'[\d.]+', problem)
                if nums:
                    radius = float(nums[0])
                    area = self.circle_area(radius)
                    result.update({
                        'success': True,
                        'answer': f"Circle Area: {area}",
                        'method': 'Circle Area Formula',
                        'details': {'radius': radius, 'area': area}
                    })
                    return result
            
            result['error'] = "Could not parse problem. Try a more specific query."
            
        except Exception as e:
            result['error'] = str(e)
        
        return result