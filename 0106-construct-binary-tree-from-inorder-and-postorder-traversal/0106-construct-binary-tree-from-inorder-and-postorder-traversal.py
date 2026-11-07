# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
        if not inorder or not postorder:
            return None

        pos = {val: i for i, val in enumerate(inorder)}

        def build(in_left, in_right):
            if in_left > in_right:
                return None

            root_val = postorder.pop()
            root = TreeNode(root_val)

            idx = pos[root_val]

            # Build right subtree first because postorder is popped from the end
            root.right = build(idx + 1, in_right)
            root.left = build(in_left, idx - 1)

            return root

        return build(0, len(inorder) - 1)