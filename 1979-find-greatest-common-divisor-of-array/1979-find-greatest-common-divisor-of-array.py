class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        smallest = min(nums)
        largest = max(nums)
        
        # Euclidean algorithm for GCD
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a
        
        return gcd(smallest, largest)
s = Solution()
print(s.findGCD([2,5,6,9,10]))  # Output: 2
print(s.findGCD([7,5,6,8,3]))   # Output: 1
print(s.findGCD([3,3]))         # Output: 3
