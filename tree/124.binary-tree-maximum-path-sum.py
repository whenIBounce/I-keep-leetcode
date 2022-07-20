# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = float('-inf')

        def get_max_gain(node) -> int:
            nonlocal max_path
            if node == None:
                return 0
            gain_on_left = max(0, get_max_gain(node.left))
            gain_on_right = max(0, get_max_gain(node.right))
            current_max_path = node.val + gain_on_left + gain_on_right

            max_path = max(max_path, current_max_path)

            return node.val + max(gain_on_left, gain_on_right)

        get_max_gain(root)
        return max_path
