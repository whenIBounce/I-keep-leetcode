from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverseK(pre: ListNode, k:int) -> ListNode:
            cur = pre.next
            for _ in range(k-1):
                next = cur.next
                cur.next = next.next
                next.next = pre.next
                pre.next = next
            return cur #cur is the end of the reversed linked list
        dummy_node = ListNode(-1)
        dummy_node.next = head
        p = head
        newPre = dummy_node
        while p:
            for _ in range(k):
                if not p:
                    return dummy_node.next
                p = p.next
            newPre = reverseK(newPre, k)
        return dummy_node.next
def printList(node: ListNode):
    while node:
        print(node.val, end = " ")
        node = node.next
    print()

# creating a list [1,2,3,4,5]
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)


print("Original list:")
printList(head)

solution = Solution()

# reversing between position 2 and 4
new_head = solution.reverseKGroup(head, 1)

print("List after reversal in group l:")
printList(new_head)