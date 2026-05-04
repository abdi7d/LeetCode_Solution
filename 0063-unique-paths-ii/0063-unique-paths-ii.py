class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        
        dp = [[0] * cols for _ in range(rows)]
        
        # start position
        if obstacleGrid[0][0] == 1:
            return 0
        dp[0][0] = 1
        
        # first column
        for i in range(1, rows):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = dp[i-1][0]
        
        # first row
        for j in range(1, cols):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = dp[0][j-1]
        
        # fill grid
        for i in range(1, rows):
            for j in range(1, cols):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[rows-1][cols-1]