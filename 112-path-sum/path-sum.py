class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        if root == None:
            return False
        return self.dfs(root, targetSum)
    def dfs(self, root, targetSum):
        if root == None:
            return False
        if targetSum - root.val == 0 and root.left == None and root.right == None:
            return True
        if root.left != None:
            left = self.dfs(root.left, targetSum - root.val)
        else:
            left = False
        if left == True:
            return True
        if root.right != None:
            right = self.dfs(root.right, targetSum - root.val)
        else:
            right = False
        return right