"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        # hashmap to tracker
        tracker = {None: None}

        curr = head
        while curr:
            tracker[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            copy = tracker[curr]
            copy.next = tracker[curr.next]
            copy.random = tracker[curr.random]
            curr = curr.next
        
        return tracker[head]
