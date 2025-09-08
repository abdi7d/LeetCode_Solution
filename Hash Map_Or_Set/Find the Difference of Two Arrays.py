class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # Set-based solution
        set1, set2 = set(nums1), set(nums2)
        # return [list(set1 - set2), list(set2 - set1)]
        return [list(set1.difference(set2)), list(set2.difference(set1))]

        # Time Complexity: O(n + m)
        # Space Complexity: O(n + m)
        
"""
# Manual traversal 
        # res1, res2 = [], []
    
        # for x in nums1:
        #     if x not in nums2 and x not in res1:
        #         res1.append(x)
        
        # for y in nums2:
        #     if y not in nums1 and y not in res2:
        #         res2.append(y)
        
        # return [res1, res2]

# Time Complexity: O(n·m + n² + m²)
# Space Complexity: O(n + m)
"""