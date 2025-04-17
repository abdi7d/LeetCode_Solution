            # Approach 
#  use two nested loops

'''
Two nested loop:
1st loop to iterate over all list elements 
2nd loop to iterate from current of 1st loop till end 

coditional: if nums[i] + nums[j] == target 
                return 

'''
class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    return[i,j]

