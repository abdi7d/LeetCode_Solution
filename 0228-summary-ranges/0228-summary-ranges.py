class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        i = 0
        
        while i < len(nums):
            start = nums[i]
            
            # expand range
            while i + 1 < len(nums) and nums[i + 1] == nums[i] + 1:
                i += 1
            
            end = nums[i]
            
            # build string
            if start == end:
                res.append(str(start))
            else:
                res.append(f"{start}->{end}")
            
            i += 1
        
        return res