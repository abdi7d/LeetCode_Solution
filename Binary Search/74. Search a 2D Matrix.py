class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        m = len(matrix)        # number of rows
        n = len(matrix[0])     # number of columns
        
        low, high = 0, m * n - 1
        
        while low <= high:
            mid = (low + high) // 2
            row = mid // n
            col = mid % n
            
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return False
