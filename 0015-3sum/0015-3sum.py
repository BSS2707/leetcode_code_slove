class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n):
            # Skip duplicate first elements
            if i > 0 and nums[i] == nums[i-1]:
                continue

            target = -nums[i]
            left, right = i+1, n-1

            while left < right:
                s = nums[left] + nums[right]
                if s == target:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # Skip duplicates for left and right
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif s < target:
                    left += 1
                else:
                    right -= 1

        return res
print(Solution().threeSum([-1,0,1,2,-1,-4]))
# Output: [[-1,-1,2], [-1,0,1]]

print(Solution().threeSum([0,1,1]))
# Output: []

print(Solution().threeSum([0,0,0]))
# Output: [[0,0,0]]

