/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        int min_v = min(p->val, q->val);
        int max_v = max(p->val, q->val);
        if(root->val <= max_v && root->val >= min_v){
            return root;
        }
        if(max_v < root->val){
            return lowestCommonAncestor(root->left, p, q);
        }else{
            return lowestCommonAncestor(root->right, p, q);
        }
    }
};