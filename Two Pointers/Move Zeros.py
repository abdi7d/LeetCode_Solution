class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        # First pointer: Pointer to place the next non-zero element(position to place the next non-zero element)
        last_non_zero = 0

        # # Second pointer: scan the list (Move non-zeroes forward)
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_non_zero] = nums[i]
                nums[i] = nums[last_non_zero]
                last_non_zero += 1