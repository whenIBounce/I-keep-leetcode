from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k==0:
            return head
        
        cur = head
        n = 1
        while cur.next:
            n += 1
            cur = cur.next
        
        if (add:= n - k%n) == n:
            return head
        #连成环，再断开
        cur.next = head
        
        for _ in range(add):
            cur = cur.next
        
        ret = cur.next
        cur.next = None
        return ret      
    # First attempt works, but not very concise
    def rotateRight2(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k==0:
            return head
        
        p = head
        n = 1
        while p.next:
            n += 1
            p = p.next
            
        k = k % n
        if k == 0:
            print("k == 0")
            return head

        p.next = head
        
        newTail = head
        for _ in range(n-k-1):
            newTail = newTail.next
            
        newHead = newTail.next
        newTail.next = None
        return newHead

def printList(node: ListNode):
    while node:
        print(node.val, end = " ")
        node = node.next
    print()

# creating a list [1,2,3,4,5]
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(5)
# head.next.next.next.next.next = ListNode(5)
# head.next.next.next.next.next.next = ListNode(5)
# head.next.next.next.next.next.next.next = ListNode(5)
# head.next.next.next.next.next.next.next.next = ListNode(5)
# head.next.next.next.next.next.next.next.next.next = ListNode(5)

print("Original list:")
printList(head)

solution = Solution()

# reversing between position 2 and 4
new_head = solution.rotateRight(head, 1)

print("List after rotating:")
printList(new_head)

