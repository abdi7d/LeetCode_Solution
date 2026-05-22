class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        result = 0
        
        # check all 32 bits
        for i in range(32):
            
            bitSum = 0
            
            for num in nums:
                
                if (num >> i) & 1:
                    bitSum += 1
            
            # unique bit survives
            if bitSum % 3:
                
                # handle negative numbers
                if i == 31:
                    result -= (1 << 31)
                else:
                    result |= (1 << i)
        
        return result