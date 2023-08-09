from typing import Optional
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList2(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        # Step 1: duplicate the nodes
        dummy = head
        while head:
            node = Node(head.val)
            node.next = head.next
            head.next = node
            head = head.next.next
        # Step 2: copy random pointers
        pointer1 = dummy
        pointer2 = dummy.next
        while pointer1:
            pointer2.random = (pointer1.random.next if pointer1.random else None)
            pointer1 = pointer1.next.next
            pointer2 = (pointer2.next.next if pointer2.next else None)
        # Step 3: seperate the copied nodes from the original one
        res = Node(1)
        head = dummy.next
        res.next = head
        while head.next:
            head.next = head.next.next
            head = head.next
        return res.next
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        # Step 1: duplicate the nodes
        p = head
        while p:
            node = Node(p.val)
            node.next = p.next
            p.next = node
            p = p.next.next
        # Step 2: copy random pointers
        p = head
        while p:
            p.next.random = (p.random.next if p.random else None)
            p = p.next.next
        # Step 3: seperate the copied nodes from the original one
        dummy = Node(-1)
        p = head
        cur = dummy
        while p:
            cur.next = p.next
            p = p.next.next
            cur = cur.next
        return dummy.next