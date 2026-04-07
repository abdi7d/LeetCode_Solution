class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        rows = [""] * numRows
        curr_row = 0
        direction = -1  # will flip
        
        for char in s:
            rows[curr_row] += char
            
            # change direction at top/bottom
            if curr_row == 0 or curr_row == numRows - 1:
                direction *= -1
            
            curr_row += direction
        
        return "".join(rows) 