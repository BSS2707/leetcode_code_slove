# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        ans = []

        def dfs(node, curr_path, curr_sum):
            if not node:
                return

            curr_path.append(node.val)
            curr_sum += node.val

            if not node.left and not node.right:
                if curr_sum == targetSum:
                    ans.append(curr_path[:])
            else:
                dfs(node.left, curr_path, curr_sum)
                dfs(node.right, curr_path, curr_sum)

            curr_path.pop()

        dfs(root, [], 0)
        return ans