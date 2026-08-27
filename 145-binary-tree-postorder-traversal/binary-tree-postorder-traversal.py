class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        def postorder(root):
            if not root:
                return
            
            postorder(root.left)
            postorder(root.right)
            res.append(root.val)

        postorder(root)
        return res