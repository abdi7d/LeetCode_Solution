class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left, right = 0, len(nums) - 1
        
        while left < right:
            
            mid = (left + right) // 2
            
            # minimum in right half
            if nums[mid] > nums[right]:
                left = mid + 1
            
            # minimum in left half including mid
            else:
                right = mid
        
        return nums[left]