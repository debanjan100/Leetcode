class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, path):
            if not node:
                return 0
            path = path * 10 + node.val
            if not node.left and not node.right:
                return path
            return dfs(node.left, path) + dfs(node.right, path)
        
        return dfs(root, 0)