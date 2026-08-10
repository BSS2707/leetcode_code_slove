class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n = len(haystack)
        m = len(needle)

        # Loop through possible starting positions
        for i in range(n - m + 1):
            if haystack[i:i+m] == needle:
                return i
        return -1


# Example usage
sol = Solution()
print(sol.strStr("sadbutsad", "sad"))     # Output: 0
print(sol.strStr("leetcode", "leeto"))    # Output: -1
