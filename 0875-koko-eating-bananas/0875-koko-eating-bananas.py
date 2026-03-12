class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        
        left, right = 1, max(piles)
        
        while left < right:
            mid = (left + right) // 2
            
            hours = 0
            for p in piles:
                hours += math.ceil(p / mid)
            
            if hours <= h:
                right = mid
            else:
                left = mid + 1
        
        return left