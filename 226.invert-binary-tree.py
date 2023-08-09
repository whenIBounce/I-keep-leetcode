from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    #DFS
    def invertTree2(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        left = self.invertTree(root.right)
        right = self.invertTree(root.left)
        root.left = left
        root.right = right
        return root
    #BFS
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = []
        queue.push(root)
        while(queue):
            node = queue.pop(0)
            newRight = node.left
            node.left = node.right
            node.right = newRight
            if node.left:
                queue.push(node.left)
            if node.right:
                queue.append(node.right)
        return root