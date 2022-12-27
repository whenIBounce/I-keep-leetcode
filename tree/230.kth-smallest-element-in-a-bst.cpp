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
    int kthSmallest(TreeNode* root, int k) {
        vector<TreeNode*> a;
        inorder_traverse(root, a);
        return a[k-1]->val;
    }
    void inorder_traverse(TreeNode* root, vector<TreeNode*> &arr){
        if(!root){
            return;
        }
        inorder_traverse(root->left, arr);
        arr.push_back(root);
        inorder_traverse(root->right, arr);
    }
};