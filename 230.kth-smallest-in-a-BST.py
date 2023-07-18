from typing import Optional
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmalles2(self, root: Optional[TreeNode], k: int) -> int:
        inorder = [] # Don't need this
        stack = []
        count = 0 # Don't need this neither
        
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            inorder.append(root.val)
            count += 1
            if count == k:
                return root.val
            
            root = root.right
            
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
            
        