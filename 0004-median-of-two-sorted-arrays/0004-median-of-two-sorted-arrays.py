class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # ensure nums1 is smaller
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        x = len(nums1)
        y = len(nums2)
        
        left, right = 0, x
        
        while left <= right:
            
            partitionX = (left + right) // 2
            partitionY = (x + y + 1) // 2 - partitionX
            
            maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minRightX = float('inf') if partitionX == x else nums1[partitionX]
            
            maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minRightY = float('inf') if partitionY == y else nums2[partitionY]
            
            # correct partition
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                
                # odd total length
                if (x + y) % 2 == 1:
                    return max(maxLeftX, maxLeftY)
                
                # even total length
                return (
                    max(maxLeftX, maxLeftY) +
                    min(minRightX, minRightY)
                ) / 2
            
            # move left
            elif maxLeftX > minRightY:
                right = partitionX - 1
            
            # move right
            else:
                left = partitionX + 1