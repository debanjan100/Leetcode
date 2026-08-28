class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Base case: an empty tree is symmetric
        if not root:
            return True
            
        def is_mirror(p, q):
            # If both nodes are empty, they match
            if p is None and q is None:
                return True
            # If only one node is empty, they do not match
            if p is None or q is None:
                return False
            # Check current values and mirror-match the child nodes
            return (p.val == q.val and 
                    is_mirror(p.left, q.right) and 
                    is_mirror(p.right, q.left))
                    
        # Compare the left and right subtrees of the root
        return is_mirror(root.left, root.right)
