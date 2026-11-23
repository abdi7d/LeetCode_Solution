class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        res = max(nums)
        curr_min, curr_max = 1, 1

        for num in nums:
            # Store curr_max * num before updating curr_max
            temp = curr_max * num
            
            curr_max = max(num, temp, curr_min * num)
            curr_min = min(num, temp, curr_min * num)
            
            res = max(res, curr_max)
            
        return res
