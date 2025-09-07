class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        answer = []
        for i in nums1:
            for j in nums2:
                if nums1[i] !=nums2[j]:
                    answer.append(nums1[i])
                else:
                    continue
        for k in nums2:
            for l  in nums1:
                if nums1[k] !=nums2[l]:
                    answer.append(nums1[k])
                else:
                    continue

nums1 = [1, 2, 3]
nums2 = [2, 4, 6]

