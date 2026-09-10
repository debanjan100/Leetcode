class Solution:
    def averageOfSubtree(self, root):
        self.count = 0

        def trav(node):
            if node is None:
                return (0, 0)

            leftSum, leftCount = trav(node.left)
            rightSum, rightCount = trav(node.right)

            subtreeSum = leftSum + rightSum + node.val
            subtreeCount = leftCount + rightCount + 1

            if subtreeSum // subtreeCount == node.val:
                self.count += 1

            return (subtreeSum, subtreeCount)

        trav(root)
        return self.count