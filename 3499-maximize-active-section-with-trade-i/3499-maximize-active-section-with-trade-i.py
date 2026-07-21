class Solution:
    def maxActiveSectionsAfterTrade(self, s):
        ans = s.count('1')

        # Add 1 at both ends
        s = '1' + s + '1'

        # Store lengths of consecutive groups
        groups = []
        i = 0

        while i < len(s):
            j = i

            while j < len(s) and s[j] == s[i]:
                j += 1

            groups.append((s[i], j - i))
            i = j

        best = 0

        # Pattern: 0-block, 1-block, 0-block
        for i in range(1, len(groups) - 1):
            if (groups[i][0] == '1' and
                groups[i - 1][0] == '0' and
                groups[i + 1][0] == '0'):

                gain = groups[i - 1][1] + groups[i + 1][1]
                best = max(best, gain)

        return ans + best


print(Solution().maxActiveSectionsAfterTrade("01"))       # 1
print(Solution().maxActiveSectionsAfterTrade("0100"))     # 4
print(Solution().maxActiveSectionsAfterTrade("1000100"))  # 7
print(Solution().maxActiveSectionsAfterTrade("01010"))    # 4