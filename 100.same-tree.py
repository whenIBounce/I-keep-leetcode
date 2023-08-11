from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pq = []
        qq = []
        if (p and not q) or (q and not p) or (p.val != q.val):
            return False
        pq.append(p)
        qq.append(q)
        while pq or qq:
            pnode = pq.pop(0)
            qnode = qq.pop(0)
            if (pnode and not qnode) or (qnode and not pnode):
                return False
            pleft, qleft, pright, qright = pnode.left, qnode.left, pnode.right, qnode.right
            if (pleft and not qleft) or (pright and not qright) or (qleft and not pleft) or(qright and not pright):
                return False
            if (pleft and qleft) and (pleft.val != qleft.val):
                return False
            if (pright and qright) and (pright.val != qright.val):
                return False if (pleft and qleft):
                pq.append(pleft)
                qq.append(qleft)
            if (pright and qright):
                pq.append(pright)
                qq.append(qright)
        return True
            
            
        