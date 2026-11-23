class Solution:
    def numSquares(self, n: int) -> int:
        # Worst case: n is made of all 1s (1^2 + 1^2 + ... + 1^2)
        dp = [i for i in range(n + 1)]
        
        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
                
        return dp[n]
