# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # My solution, works but not elegant enough
    def hasCycle2(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        while True:
            if (not slow) or (not fast):
                return False
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                return False
            if fast == slow:
                return True
            
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or head.next:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            #! if not slow or (not fast) or (not fast.next):
            if (not fast) or (not fast.next):
                return False
            slow = slow.next
            fast = fast.next.next
        return True

