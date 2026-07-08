class Solution:
    def reverse(self, x):
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        res = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x != 0:
            digit = x % 10
            x //= 10

            # Check overflow before adding digit
            if res > (INT_MAX - digit) // 10:
                return 0

            res = res * 10 + digit

        return sign * res


# --- Local testing ---
if __name__ == "__main__":
    s = Solution()
    print(s.reverse(123))        # 321
    print(s.reverse(-123))       # -321
    print(s.reverse(120))        # 21
    print(s.reverse(1534236469)) # 0 (overflow)
