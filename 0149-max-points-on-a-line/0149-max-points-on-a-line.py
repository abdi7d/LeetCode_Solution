import collections
import math

class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n  # Any 1 or 2 points will always form a straight line
        
        max_points_on_line = 1
        
        for i in range(n):
            slopes = collections.defaultdict(int)
            x1, y1 = points[i]
            
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dx = x2 - x1
                dy = y2 - y1
                
                # Normalize the slope fractions to avoid floating-point inaccuracies
                gcd = math.gcd(dx, dy)
                dx //= gcd
                dy //= gcd
                
                # Ensure uniform sign representation for identical lines
                if dx < 0 or (dx == 0 and dy < 0):
                    dx = -dx
                    dy = -dy
                
                slopes[(dy, dx)] += 1
            
            # Local max includes the current anchor point (+1)
            if slopes:
                current_max = max(slopes.values()) + 1
                max_points_on_line = max(max_points_on_line, current_max)
                
        return max_points_on_line
