from typing import List
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # This infact is preorder traversal
    def postorderTraversal2(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        ans = []
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop()
            ans.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)            
        return ans[::-1]
    
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        ans = []
        stack = []
        prev = None

        # 主要思想：
        # 由于在某颗子树访问完成以后，接着就要回溯到其父节点去
        # 因此可以用prev来记录访问历史，在回溯到父节点时，可以由此来判断，上一个访问的节点是否为右子树
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            # 从栈中弹出的元素，左子树一定是访问完了的
            root = stack.pop()

            # 现在需要确定的是是否有右子树，或者右子树是否访问过
            # 如果没有右子树，或者右子树访问完了，也就是上一个访问的节点是右子节点时
            # 说明可以访问当前节点
            if not root.right or prev == root.right:
                ans.append(root.val)
                # 更新历史访问记录，这样回溯的时候父节点可以由此判断右子树是否访问完成
                prev = root
                root = None
            else:
                stack.append(root)
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
result = solution.postorderTraversal(root)

# Print the result
# 1 2 4 7 8 6 5
print(result)

