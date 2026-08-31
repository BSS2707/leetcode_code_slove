class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        # dp[i][j] = does s[:i] match p[:j]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True  # empty string matches empty pattern

        # Handle patterns starting with '*' that can match empty string
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]

        # Fill DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '?' or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    # '*' can match empty (dp[i][j-1]) or one more char (dp[i-1][j])
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]

        return dp[m][n]
sol = Solution()
print(sol.isMatch("aa", "a"))     # False
print(sol.isMatch("aa", "*"))     # True
print(sol.isMatch("cb", "?a"))    # False
print(sol.isMatch("adceb", "*a*b")) # True
print(sol.isMatch("acdcb", "a*c?b")) # False
