class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []

        def backtrack(start, subset):
            res.append(subset[:])

            for i in range(start, len(nums)):
                # Skip duplicates at the same level
                if i > start and nums[i] == nums[i - 1]:
                    continue

                subset.append(nums[i])
                backtrack(i + 1, subset)
                subset.pop()

        backtrack(0, [])
        return res