class Solution:
    def searchRange(self, nums, target):
        def findLeft(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        def findRight(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        left_index = findLeft(nums, target)
        right_index = findRight(nums, target)

        # Check if target exists
        if left_index <= right_index and left_index < len(nums) and nums[left_index] == target:
            return [left_index, right_index]
        else:
            return [-1, -1]
s = Solution()
print(s.searchRange([5,7,7,8,8,10], 8))   # [3,4]
print(s.searchRange([5,7,7,8,8,10], 6))   # [-1,-1]
print(s.searchRange([], 0))               # [-1,-1]
