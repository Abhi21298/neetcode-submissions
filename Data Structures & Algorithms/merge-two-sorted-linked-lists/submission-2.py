# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1 and not list2:
            return None
        elif not list1:
            return list2
        elif not list2:
            return list1
        
        dummy = ListNode(0, None)
        res = dummy
        while list1 and list2:
            if list1.val < list2.val:
                dummy.next = list1
                dummy = list1
                list1 = list1.next
            else:
                dummy.next = list2
                dummy = list2
                list2 = list2.next
        
        if list1:
            dummy.next = list1
        else:
            dummy.next = list2
        
        return res.next

        