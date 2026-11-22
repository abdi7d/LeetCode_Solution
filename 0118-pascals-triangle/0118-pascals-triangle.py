class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        triangle: list[list[int]] = []

        for row_idx in range(numRows):
            row = [1] * (row_idx + 1)
            for col_idx in range(1, row_idx):
                row[col_idx] = (
                    triangle[row_idx - 1][col_idx - 1]
                    + triangle[row_idx - 1][col_idx]
                )
            triangle.append(row)

        return triangle
