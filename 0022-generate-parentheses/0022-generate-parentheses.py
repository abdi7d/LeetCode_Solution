class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        def backtrack(curr, open_count, close_count):
            
            # complete string
            if len(curr) == 2 * n:
                result.append(curr)
                return
            
            # add '('
            if open_count < n:
                backtrack(
                    curr + "(",
                    open_count + 1,
                    close_count
                )
            
            # add ')'
            if close_count < open_count:
                backtrack(
                    curr + ")",
                    open_count,
                    close_count + 1
                )
        
        backtrack("", 0, 0)
        return result