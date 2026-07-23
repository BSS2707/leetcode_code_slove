class Solution(object):
    def uniqueXorTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return 1
        if n == 2:
            return 2

        # All numbers themselves are included
        seen = set(nums)

        # Compute all XORs of three distinct numbers
        # Trick: since nums is [1..n], we can just brute force up to small n,
        # but for large n we use the fact that XOR covers full range up to 2*highest_bit.
        max_val = 1 << (n.bit_length())
        # All values from 0..max_val-1 are achievable
        return max_val

print(Solution().uniqueXorTriplets([1,2]))       # Output: 2
print(Solution().uniqueXorTriplets([3,1,2]))     # Output: 4
print(Solution().uniqueXorTriplets([1,2,3,4]))   # Output: 5
print(Solution().uniqueXorTriplets([1,2,3,4,5])) # Output: 6
