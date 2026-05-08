# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head:
            return None
        
        if not n:
            return head

        
        
        fast = head
        while fast and n > 0:
            fast = fast.next
            n -= 1
        
        if not fast:
            if n == 0:
                return head.next
            else:
                return head
        
        slow, prev = head, None
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next
        
        prev.next = slow.next
        return head