class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        n = len(nums)
        closest_sum = float('inf')
        
        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                
                # Update closest sum if better
                if abs(curr_sum - target) < abs(closest_sum - target):
                    closest_sum = curr_sum
                
                # Move pointers
                if curr_sum < target:
                    left += 1
                elif curr_sum > target:
                    right -= 1
                else:
                    return curr_sum  # Exact match found
        
        return closest_sum
s = Solution()
print(s.threeSumClosest([-1,2,1,-4], 1))   # Output: 2
print(s.threeSumClosest([0,0,0], 1))       # Output: 0
print(s.threeSumClosest([1,1,1,0], -100))  # Output: 2
