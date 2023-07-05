from typing import List
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # dfs
    def preorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        stack = []
        stack.append(root)
        while stack:
            tmp = stack.pop()
            ans.append(tmp.val)
            if tmp.right:
                stack.append(tmp.right)
            if tmp.left:
                stack.append(tmp.left)
        
        return ans
    
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        stack = []

        while stack or root:
            while root:
                ans.append(root.val)
                stack.append(root)
                root = root.left
            root = stack.pop()
            root = root.right
        return ans

# Create a binary tree
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(2)
root.right.left = TreeNode(7)
root.right.right = TreeNode(8)

# Create an instance of the Solution class
solution = Solution()

# Perform postorder traversal
result = solution.preorderTraversal(root)

# Print the result: 5 4 1 2 6 7 8
print(result)