class Solution:
    def myAtoi(self, s):
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        i, n = 0, len(s)

        # Step 1: Skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1

        # Step 2: Handle sign
        sign = 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1

        # Step 3: Convert digits
        num = 0
        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord('0')
            # Overflow check
            if num > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            num = num * 10 + digit
            i += 1

        return sign * num
s = Solution()
print(s.myAtoi("42"))          # 42
print(s.myAtoi("   -042"))     # -42
print(s.myAtoi("1337c0d3"))    # 1337
print(s.myAtoi("0-1"))         # 0
print(s.myAtoi("words and 987")) # 0
print(s.myAtoi("91283472332")) # 2147483647 (clamped)
