# Definition for a binary tree node.
from typing import List
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stack = []
        if not root:
            return ans
        
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
                
            top = stack.pop()
            ans.append(top.val)
            
            root = top.right
        return ans
        