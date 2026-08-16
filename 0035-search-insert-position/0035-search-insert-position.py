class Solution:
    def searchInsert(self, nums, target):
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        # If not found, left will be the correct insertion index
        return left


# Demo runs
s = Solution()
print(s.searchInsert([1,3,5,6], 5))  # Output: 2
print(s.searchInsert([1,3,5,6], 2))  # Output: 1
print(s.searchInsert([1,3,5,6], 7))  # Output: 4
print(s.searchInsert([1,3,5,6], 0))  # Output: 0
