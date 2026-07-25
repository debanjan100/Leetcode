class Solution {
  public:
    int maxDepth(TreeNode *root) {
        // Base case: if the root is null, return 0
        if (root == nullptr) {
            return 0;
        }

        // Recursively calculate the maximum depth of the left and right subtrees
        int leftDepth = maxDepth(root->left);
        int rightDepth = maxDepth(root->right);
        // Return the maximum depth among the left and right subtrees, plus 1 for the current level
        return max(leftDepth, rightDepth) + 1;
    }
};
