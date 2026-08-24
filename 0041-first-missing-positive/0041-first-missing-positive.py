class Solution(object):
    def firstMissingPositive(self, nums):
        n = len(nums)
        
        # Place each number in its correct position if possible
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        
        # Find the first index where nums[i] != i+1
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        return n + 1
print(Solution().firstMissingPositive([3,4,-1,1]))  # Output: 2
