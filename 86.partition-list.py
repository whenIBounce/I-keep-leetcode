from typing import Optional 
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy1 = ListNode(-1)
        dummy2 = ListNode(-1)
        small = dummy1
        ge = dummy2 #ge stands for greater or equal to
        
        while head:
            next = head.next
            if head.val < x:
                small.next = head
                small = small.next
                small.next = None
            else:
                ge.next = head
                ge = ge.next
                ge.next = None
            head = next
        
        small.next = dummy2.next
        return dummy1.next

def printList(node: ListNode):
    while node:
        print(node.val, end = " ")
        node = node.next
    print()

# creating a list [1,2,3,4,5]
head = ListNode(1)
head.next = ListNode(4)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(2)
head.next.next.next.next.next.next = ListNode(9)
head.next.next.next.next.next.next.next = ListNode(5)


print("Original list:")
printList(head)

solution = Solution()

new_head = solution.partition(head, 3)

print("List after partition:")
printList(new_head)