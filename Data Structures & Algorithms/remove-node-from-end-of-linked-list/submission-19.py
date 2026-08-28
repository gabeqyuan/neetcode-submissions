# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = head
        first = dummy 
        for i in range(n):
            first = first.next
        second = head
        temp = None
        while first:
            temp = second
            second = second.next
            first = first.next
        if temp == None:
            head = second.next
            second.next = None 
            return head
        temp.next = second.next
        return head
        

