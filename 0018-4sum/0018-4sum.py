class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n - 3):
            # Skip duplicate for i
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                # Skip duplicate for j
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left, right = j + 1, n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])

                        # Skip duplicates for left and right
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1

                        left += 1
                        right -= 1

                    elif total < target:
                        left += 1
                    else:
                        right -= 1

        return res
s = Solution()
print(s.fourSum([1,0,-1,0,-2,2], 0))
# Output: [[-2,-1,1,2], [-2,0,0,2], [-1,0,0,1]]

print(s.fourSum([2,2,2,2,2], 8))
# Output: [[2,2,2,2]]
