from typing import List
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        stack = []
        
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            ans.append(root.val)
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
result = solution.inorderTraversal(root)

# Print the result: 1 4 2 5 7 6 8
print(result)