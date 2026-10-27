class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        # Base case: an empty tree is univalued
        if root is None:
            return True
        
        # Check if left child has a different value
        if root.left is not None and root.left.val != root.val:
            return False
            
        # Check if right child has a different value
        if root.right is not None and root.right.val != root.val:
            return False
            
        # Recursively validate both subtrees
        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
