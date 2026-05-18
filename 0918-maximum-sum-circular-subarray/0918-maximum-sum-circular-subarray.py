class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = sum(nums)
        
        currentMax = maxSum = nums[0]
        currentMin = minSum = nums[0]
        
        for num in nums[1:]:
            
            # Kadane max
            currentMax = max(num, currentMax + num)
            maxSum = max(maxSum, currentMax)
            
            # Kadane min
            currentMin = min(num, currentMin + num)
            minSum = min(minSum, currentMin)
        
        # all numbers negative
        if maxSum < 0:
            return maxSum
        
        return max(
            maxSum,
            total - minSum
        )