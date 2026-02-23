class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        n = len(grid)

        # Count rows
        row_count = {}
        for row in grid:
            row_tuple = tuple(row)
            row_count[row_tuple] = row_count.get(row_tuple, 0) + 1

        result = 0

        # Check columns
        for c in range(n):
            col = tuple(grid[r][c] for r in range(n))
            result += row_count.get(col, 0)

        return result