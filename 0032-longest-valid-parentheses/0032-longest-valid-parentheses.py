class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [-1]  # base index
        max_len = 0
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:  # char == ')'
                stack.pop()
                if not stack:
                    stack.append(i)  # reset base
                else:
                    max_len = max(max_len, i - stack[-1])
        
        return max_len
sol = Solution()
print(sol.longestValidParentheses("(()"))      # Output: 2
print(sol.longestValidParentheses(")()())"))   # Output: 4
print(sol.longestValidParentheses(""))         # Output: 0
