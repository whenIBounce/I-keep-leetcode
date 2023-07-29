from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy_node = ListNode(-101)
        dummy_node.next = head
        p = dummy_node
        q = p.next
        r = q.next 
        while r:
            if q.val != r.val:
                p = p.next 
                q = q.next 
                r = r.next 
            else:
                while r and r.val == q.val:
                    r = r.next 
                q = r
                p.next = q
                r = (r.next if r else None)
        return dummy_node.next

def printList(node: ListNode):
    while node:
        print(node.val, end = " ")
        node = node.next
    print()

# creating a list [1,2,3,4,5]
head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(5)
head.next.next.next.next.next.next = ListNode(5)
head.next.next.next.next.next.next.next = ListNode(5)
head.next.next.next.next.next.next.next.next = ListNode(5)
head.next.next.next.next.next.next.next.next.next = ListNode(5)

print("Original list:")
printList(head)

solution = Solution()

# reversing between position 2 and 4
new_head = solution.deleteDuplicates(head)

print("List after removing nth node from the end:")
printList(new_head)


