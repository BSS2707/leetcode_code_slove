class Solution:
    def combinationSum(self, candidates, target):
        res = []

        def backtrack(start, path, total):
            if total == target:
                res.append(path[:])
                return
            if total > target:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path, total + candidates[i])  # allow reuse
                path.pop()

        backtrack(0, [], 0)
        return res
s = Solution()
print(s.combinationSum([2,3,6,7], 7))
# Output: [[2,2,3],[7]]

print(s.combinationSum([2,3,5], 8))
# Output: [[2,2,2,2],[2,3,3],[3,5]]

print(s.combinationSum([2], 1))
# Output: []
