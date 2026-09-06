class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # Handle negative exponent
        if n < 0:
            x = 1 / x
            n = -n

        result = 1.0
        while n > 0:
            # If n is odd, multiply result by current x
            if n % 2 == 1:
                result *= x
            # Square x and halve n
            x *= x
            n //= 2

        return result
sol = Solution()
print(sol.myPow(2.0, 10))   # 1024.0
print(sol.myPow(2.1, 3))    # 9.261000000000001
print(sol.myPow(2.0, -2))   # 0.25
