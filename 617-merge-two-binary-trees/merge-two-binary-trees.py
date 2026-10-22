class Solution:

    def mergeTrees(
        self, root1: TreeNode | None, root2: TreeNode | None
    ) -> TreeNode | None:

        def dfs(node1, node2):
            if node1 and node2:
                # If both nodes exist, combine their values to form a new super node
                root = TreeNode(node1.val + node2.val)
                # And add its children by joining the children from both nodes
                root.left = dfs(node1.left, node2.left)
                root.right = dfs(node1.right, node2.right)
                # Finally return this super node
                return root
            else:
                # Otherwise return the one that exists or None if neither exists
                return node1 or node2

        # Start the search in the head or roots of both trees
        return dfs(root1, root2)
