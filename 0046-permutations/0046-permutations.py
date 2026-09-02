class Solution:
    def permute(self, nums):
        res = []
        
        def backtrack(path, remaining):
            if not remaining:
                res.append(path)
                return
            for i in range(len(remaining)):
                backtrack(path + [remaining[i]], remaining[:i] + remaining[i+1:])
        
        backtrack([], nums)
        return res
s = Solution()

print(s.permute([1,2,3]))
# [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

print(s.permute([0,1]))
# [[0,1],[1,0]]

print(s.permute([1]))
# [[1]]
