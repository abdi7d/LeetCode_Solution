class Solution:
    def findPeakGrid(self, mat: list[list[int]]) -> list[int]:
        m = len(mat) # number of rows 
        n = len(mat[0]) # number of columns
        
        def findPeakInRow(row):
            left, right = 0, n - 1
            while left < right:
                mid = (left + right) // 2
                if mat[row][mid] > mat[row][mid + 1]:
                    right = mid
                else:
                    left = mid + 1
            return left
        
        left, right = 0, m - 1
        while left < right:
            mid = (left + right) // 2
            peak_col = findPeakInRow(mid)
            if mat[mid][peak_col] > mat[mid + 1][peak_col]:
                right = mid
            else:
                left = mid + 1
        
        peak_col = findPeakInRow(left)
        return [left, peak_col]