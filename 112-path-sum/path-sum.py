class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        # Base case 1: If the current node is None, there's no path from this node.
        if not root:
            return False
        
        # Subtract the current node's value from the target sum.
        # This new targetSum represents the sum needed from the remaining path.
        targetSum -= root.val
        
        # Base case 2: If the current node is a leaf node (no children).
        if not root.left and not root.right:
            # Check if the remaining targetSum is 0. If it is, we found a path.
            return targetSum == 0
            
        # Recursive step: Explore the left and right subtrees.
        # We need to find a path in either the left OR the right subtree.
        # Pass the updated targetSum to the children.
        left_path_found = self.hasPathSum(root.left, targetSum)
        right_path_found = self.hasPathSum(root.right, targetSum)
        
        # Return True if a path was found in either the left or right subtree.
        return left_path_found or right_path_found