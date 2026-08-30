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
        newHead = None
        first = head
        oldToNew = {}
        while first:
            new = Node(first.val, None, None)
            oldToNew[first] = new
            first = first.next
        second = head
        while second:
            prev = oldToNew[second]
            if second.next:
                link = oldToNew[second.next]
            else:
                link = None
            prev.next = link
            prev.val = second.val
            if second.random:
                prev.random = oldToNew[second.random]
            else: 
                prev.random = None
            second = second.next
        if head:
            return oldToNew[head]
        else: 
            return newHead




        


        