class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        
        shift = 0
        
        # remove differing bits
        while left < right:
            
            left >>= 1
            right >>= 1
            
            shift += 1
        
        # restore common prefix
        return left << shift