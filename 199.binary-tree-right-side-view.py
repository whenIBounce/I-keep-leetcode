from typing import Optional
#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    #dfs解法
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def traverse(root: TreeNode, depth: int):
            nonlocal res
            if not root:
                return
            if len(res) == depth:
                res.append(root.val)
            traverse(root.right, depth+1)
            traverse(root.left, depth+1)
        res = []
        traverse(root, 0)
        return res
    #bfs解法
    def rightSideView2(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        queue = [root]
        res.append(root.val)
        while queue:
            count = len(queue)
            for i in range(count):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if queue: res.append(queue[-1].val)
        return res
            

