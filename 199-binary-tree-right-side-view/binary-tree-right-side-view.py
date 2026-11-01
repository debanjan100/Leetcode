from collections import deque

class Solution:
    def rightSideView(self, root):
        if not root:
            return []
        res, q = [], deque([root])

        while q:
            size = len(q)
            for i in range(size):
                node = q.popleft()
                # if last node of this level → visible
                if i == size - 1:
                    res.append(node.val)
                # push children
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res