class Solution(object):
    def gcdOfOddEvenSums(self, n):
        """
        :type n: int
        :rtype: int
        """
        # sumOdd = n^2
        # sumEven = n * (n + 1)
        # gcd(sumOdd, sumEven) = n
        return n


# Example usage
if __name__ == "__main__":
    s = Solution()
    print(s.gcdOfOddEvenSums(4))  # Output: 4
    print(s.gcdOfOddEvenSums(5))  # Output: 5
    print(s.gcdOfOddEvenSums(10)) # Output: 10
