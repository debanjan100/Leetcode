class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        res = []
        stack = []
        curr = root
        
        while curr or stack:
            # 1. Go as far left as possible
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # 2. Process the leftmost node
            curr = stack.pop()
            res.append(curr.val)
            
            # 3. Move to the right subtree
            curr = curr.right
            
        return res
