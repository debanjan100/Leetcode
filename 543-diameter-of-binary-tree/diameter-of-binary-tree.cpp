/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int maxpath;
    int solve(TreeNode*root){
        if(root==NULL){
                return 0;
        }

        int l=solve(root->left);
        int r=solve(root->right);

        int curved=l+r+1;
        int anyone=1+max(l,r);

        maxpath=max({maxpath,curved,anyone});

        return anyone;

    }

    int diameterOfBinaryTree(TreeNode* root) {
        
        maxpath=INT_MIN;
        solve(root);

        return maxpath-1;
    }
};