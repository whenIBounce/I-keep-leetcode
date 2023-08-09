from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        root = TreeNode(preorder[0])
        
        numOfNodesInLeft = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:numOfNodesInLeft+1], inorder[:numOfNodesInLeft])
        root.right = self.buildTree(preorder[1+numOfNodesInLeft:], inorder[numOfNodesInLeft+1:])
        return root
        