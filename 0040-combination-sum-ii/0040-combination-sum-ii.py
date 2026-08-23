class Solution:
    def combinationSum2(self, candidates, target):
        res = []
        candidates.sort()

        def backtrack(start, path, total):
            if total == target:
                res.append(path[:])
                return
            if total > target:
                return

            prev = -1
            for i in range(start, len(candidates)):
                if candidates[i] == prev:
                    continue  # skip duplicates at same level
                path.append(candidates[i])
                backtrack(i + 1, path, total + candidates[i])  # move forward
                path.pop()
                prev = candidates[i]

        backtrack(0, [], 0)
        return res
s = Solution()
print(s.combinationSum2([10,1,2,7,6,1,5], 8))
# Output: [[1,1,6],[1,2,5],[1,7],[2,6]]

print(s.combinationSum2([2,5,2,1,2], 5))
# Output: [[1,2,2],[5]]
