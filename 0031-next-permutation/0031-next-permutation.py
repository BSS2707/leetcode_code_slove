class Solution:
    def nextPermutation(self, nums):
        # Step 1: Find pivot
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            # Step 2: Find successor
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            # Step 3: Swap
            nums[i], nums[j] = nums[j], nums[i]

        # Step 4: Reverse suffix
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
s = Solution()

nums = [1,2,3]
s.nextPermutation(nums)
print(nums)  # [1,3,2]

nums = [3,2,1]
s.nextPermutation(nums)
print(nums)  # [1,2,3]

nums = [1,1,5]
s.nextPermutation(nums)
print(nums)  # [1,5,1]

nums = [2,3,1]
s.nextPermutation(nums)
print(nums)  # [3,1,2]
