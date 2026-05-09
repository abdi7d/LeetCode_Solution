class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        path = []
        
        def backtrack(start, remaining):
            
            # found valid combination
            if remaining == 0:
                result.append(path[:])
                return
            
            # exceeded target
            if remaining < 0:
                return
            
            for i in range(start, len(candidates)):
                
                path.append(candidates[i])
                
                # i (not i+1) because reuse allowed
                backtrack(i, remaining - candidates[i])
                
                path.pop()
        
        backtrack(0, target)
        return result