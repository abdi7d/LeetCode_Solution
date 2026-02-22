class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7

        if n <= 2:
            return n

        dp0 = 1  # dp[n-3]
        dp1 = 1  # dp[n-2]
        dp2 = 2  # dp[n-1]

        for _ in range(3, n + 1):
            dp = (2 * dp2 + dp0) % MOD
            dp0, dp1, dp2 = dp1, dp2, dp

        return dp2