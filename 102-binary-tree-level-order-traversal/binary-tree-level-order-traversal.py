from collections import deque

class Solution:
    def levelOrder(self, root):
        if not root:
            return []

        ans = []
        queue = deque([root])

        while queue:
            level = []
            size = len(queue)

            for _ in range(size):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            ans.append(level)

        return ans