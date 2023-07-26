from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween2(self, head: ListNode, left: int, right: int) -> ListNode:
        def reverse_linked_list(head: ListNode):
            pre = None
            cur = head
            while cur:
                next = cur.next
                cur.next = pre
                pre = cur
                cur = next
        # using a dummy node to avoid edge cases
        dummy_node = ListNode(-1)
        dummy_node.next = head
        precursor = dummy_node
    
        # 1. locating precursor, succ and left_node, right_node
        for _ in range(left - 1): #using for loop 
            precursor = precursor.next
        right_node = precursor
        for _ in range(right - left + 1):
            right_node = right_node.next
        left_node = precursor.next
        succ = right_node.next

        # 2. cutting the reversed part, and reverse it
        precursor.next = None
        right_node.next = None
        reverse_linked_list(left_node)
        
        # 3. connecting precurson, reversed and succ
        precursor.next = right_node
        left_node.next = succ
        return dummy_node.next            
    
    # 头插法，太美了
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy_node = ListNode(-1)
        dummy_node.next = head
        pre = dummy_node
        for _ in range(left - 1):
            pre = pre.next

        cur = pre.next
        
        for _ in range(right - left):
            next = cur.next
            cur.next = next.next
            next.next = pre.next
            pre.next = next
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
new_head = solution.reverseBetween(head, 1, 2)

print("List after reversal between 2 and 4:")
printList(new_head)
