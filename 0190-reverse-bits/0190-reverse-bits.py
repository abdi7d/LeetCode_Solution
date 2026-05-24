class Solution:
    def reverseBits(self, n: int) -> int:
        
        result = 0
        
        for _ in range(32):
            
            # shift result left
            result <<= 1
            
            # add last bit of n
            result |= (n & 1)
            
            # shift n right
            n >>= 1
        
        return result