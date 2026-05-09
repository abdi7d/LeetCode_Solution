class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        diag = set()       # row - col
        anti_diag = set()  # row + col
        
        result = 0
        
        def backtrack(row):
            nonlocal result
            
            # placed queens successfully
            if row == n:
                result += 1
                return
            
            for col in range(n):
                
                if (col in cols or
                    row - col in diag or
                    row + col in anti_diag):
                    continue
                
                # place queen
                cols.add(col)
                diag.add(row - col)
                anti_diag.add(row + col)
                
                backtrack(row + 1)
                
                # remove queen
                cols.remove(col)
                diag.remove(row - col)
                anti_diag.remove(row + col)
        
        backtrack(0)
        return result