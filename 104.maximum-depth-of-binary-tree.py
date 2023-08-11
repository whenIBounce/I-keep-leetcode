from typing import Optional
#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # DFS
    def maxDepth2(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left),self.maxDepth(root.right))+1
    # BFS
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ans = 0
        queue = []
        queue.append(root)
        while(queue):
            size = len(queue)
            while(size>0):
                node = queue.pop(0)
                queue.append(node.left)
                queue.append(node.right)
                size -= 1
            ans += 1
        return ans