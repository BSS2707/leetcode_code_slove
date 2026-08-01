class Solution(object):
    def isValid(self, s):
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in mapping.values():  # opening bracket
                stack.append(char)
            elif char in mapping:  # closing bracket
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
            else:
                return False  # invalid character
        
        return not stack
print(Solution().isValid("()"))       # True
print(Solution().isValid("()[]{}"))   # True
print(Solution().isValid("(]"))       # False
print(Solution().isValid("([])"))     # True
print(Solution().isValid("([)]"))     # False
