# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root.left is None and root.right is None:
            return True

        in_order = []

        def in_order_traversel(root) -> bool:
            nonlocal in_order
            if root == None:
                return True

            left = in_order_traversel(root.left)
            if len(in_order) > 0 and in_order[-1] >= root.val:
                return False
            in_order.append(root.val)
            right = in_order_traversel(root.right)

            return left and right

        return in_order_traversel(root)
