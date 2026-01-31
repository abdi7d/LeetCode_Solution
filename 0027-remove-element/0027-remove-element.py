class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Pointer for the position of the next valid element
        i = 0

        # Traverse the list
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]  # Move valid element to the next position
                i += 1

        # i is now the new length of the array without val
        return i
