from typing import List
from typing import Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        ans = []
        stack.append(root)
        while not stack.empty():
            current = stack.pop()
            ans.append(current.val)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        return ans
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def preorder(root: TreeNode):
            if not root:
                return
            res.append(root.val)
            preorder(root.left)
            preorder(root.right)
        res = list()
        preorder(root)
        return res

                