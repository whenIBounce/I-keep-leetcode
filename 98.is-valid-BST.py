# Definition for a binary tree node.
from typing import List
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inorder = []
        stack = []
        if not root:
            return True
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
                
            root = stack.pop()
            if not inorder:
                inorder.append(root.val)
            elif inorder and inorder[-1] < root.val:
                inorder.append(root.val)
            else:
                return False
            
            root = root.right
        
        return True