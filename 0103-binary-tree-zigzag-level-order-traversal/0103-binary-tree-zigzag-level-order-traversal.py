from collections import deque

class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []

        result = []
        q = deque([root])
        leftToRight = True

        while q:
            level_size = len(q)
            level = []

            for _ in range(level_size):
                node = q.popleft()

                if leftToRight:
                    level.append(node.val)
                else:
                    level.insert(0, node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            result.append(level)
            leftToRight = not leftToRight

        return result