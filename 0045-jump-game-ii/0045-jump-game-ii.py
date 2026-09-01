class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        jumps = 0
        farthest = 0
        current_end = 0
        
        # iterate until the second last index
        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])
            
            # when we reach the end of the current jump range
            if i == current_end:
                jumps += 1
                current_end = farthest
        
        return jumps
print(Solution().jump([2,3,1,1,4]))  # Output: 2
print(Solution().jump([2,3,0,1,4]))  # Output: 2
