class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m, n = len(s), len(t)
        
        # dp[i][j] = number of subsequences of s[:i] that equal t[:j]
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Base case: empty t can always be formed (1 way)
        for i in range(m + 1):
            dp[i][0] = 1
        
        # Fill DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        
        return dp[m][n]
sol = Solution()
print(sol.numDistinct("rabbbit", "rabbit"))  # Output: 3
print(sol.numDistinct("babgbag", "bag"))     # Output: 5
