class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # copy last row
        dp = triangle[-1][:]
        
        # iterate from second-last row upward
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = triangle[i][j] + min(dp[j], dp[j+1])
        
        return dp[0]