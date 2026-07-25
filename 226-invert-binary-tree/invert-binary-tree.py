class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        # Swap left and right subtrees
        root.left, root.right = root.right, root.left

        # Recursively invert left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root