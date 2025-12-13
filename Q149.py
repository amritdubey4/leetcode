"""
LeetCode Q149: Max Points on a Line
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum 
number of points that lie on the same straight line.
"""

class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        if len(points) <= 2:
            return len(points)
        
        max_points = 1
        
        for i in range(len(points)):
            slopes = {}
            same_point = 1
            
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                
                if x1 == x2 and y1 == y2:
                    same_point += 1
                    continue
                
                dx = x2 - x1
                dy = y2 - y1
                
                # Normalize slope
                if dx == 0:
                    slope = float('inf')
                else:
                    gcd = self._gcd(dy, dx)
                    slope = (dy // gcd, dx // gcd)
                
                slopes[slope] = slopes.get(slope, 0) + 1
            
            max_points = max(max_points, same_point)
            for count in slopes.values():
                max_points = max(max_points, same_point + count)
        
        return max_points
    
    def _gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

