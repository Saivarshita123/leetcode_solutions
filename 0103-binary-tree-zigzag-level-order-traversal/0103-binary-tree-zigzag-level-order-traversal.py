from collections import deque

class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []

        result = []
        queue = deque([root])
        leftToRight = True

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # reverse if zigzag requires it
            if not leftToRight:
                level.reverse()

            result.append(level)
            leftToRight = not leftToRight  # flip direction

        return result
