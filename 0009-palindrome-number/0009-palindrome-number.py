class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        
        original = x
        reversed_num = 0
        
        while x != 0:
            digit = x % 10
            x //= 10
            reversed_num = reversed_num * 10 + digit
        
        return original == reversed_num


# Testing
s = Solution()
print(s.isPalindrome(121))   # True
print(s.isPalindrome(-121))  # False
print(s.isPalindrome(10))    # False
