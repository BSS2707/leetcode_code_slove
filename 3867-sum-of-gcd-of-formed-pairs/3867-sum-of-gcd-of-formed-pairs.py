class Solution(object):
    def gcdSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Custom gcd function (works in Python 2 and 3)
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        n = len(nums)
        
        # Step 1: Build prefixGcd
        prefixGcd = []
        mxi = nums[0]
        for i in range(n):
            mxi = max(mxi, nums[i])
            prefixGcd.append(gcd(nums[i], mxi))
        
        # Step 2: Sort prefixGcd
        prefixGcd.sort()
        
        # Step 3: Pair smallest with largest and compute gcd
        total = 0
        left, right = 0, n - 1
        while left < right:
            total += gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1
        
        return total
s = Solution()
print(s.gcdSum([2,6,4]))   # Output: 2
print(s.gcdSum([3,6,2,8])) # Output: 5
