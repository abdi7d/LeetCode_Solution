class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        used = [False] * len(nums)
        
        def backtrack():
            
            # full permutation formed
            if len(path) == len(nums):
                result.append(path[:])
                return
            
            for i in range(len(nums)):
                
                if used[i]:
                    continue
                
                used[i] = True
                path.append(nums[i])
                
                backtrack()
                
                path.pop()
                used[i] = False
        
        backtrack()
        return result