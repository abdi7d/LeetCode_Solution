class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        # handle negative exponent
        if n < 0:
            x = 1 / x
            n = -n
        
        result = 1
        
        while n > 0:
            
            # if n is odd
            if n % 2 == 1:
                result *= x
            
            x *= x
            n //= 2
        
        return result