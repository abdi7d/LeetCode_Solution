class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        
        # 1. find pivot
        i = n - 2
        
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        # 2. find next larger element
        if i >= 0:
            
            j = n - 1
            
            while nums[j] <= nums[i]:
                j -= 1
            
            nums[i], nums[j] = nums[j], nums[i]
        
        # 3. reverse suffix
        left = i + 1
        right = n - 1
        
        while left < right:
            
            nums[left], nums[right] = nums[right], nums[left]
            
            left += 1
            right -= 1