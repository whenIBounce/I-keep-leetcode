from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0:
            return None
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        root = TreeNode(postorder[-1])
        numOfLeftNodes = inorder.index(root.val)
        left = self.buildTree(inorder[:numOfLeftNodes], postorder[:numOfLeftNodes])
        right = self.buildTree(inorder[numOfLeftNodes+1:], postorder[numOfLeftNodes:-1])
        root.left = left
        root.right = right
        return root