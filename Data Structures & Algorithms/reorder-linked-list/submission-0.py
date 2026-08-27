# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head 
        fast = head.next
        while fast and fast.next: 
            slow = slow.next 
            fast = fast.next.next
        secondHalf = slow.next 
        slow.next = None 
        prev = None 
        while secondHalf:
            temp = secondHalf.next 
            secondHalf.next = prev 
            prev = secondHalf
            secondHalf = temp 

        #beginning of second half is prev because second is null at the end of the while 
        second = prev
        first = head 
        while second:
            #break links so store next nodes
            firstTemp = first.next
            secondTemp = second.next

            #reorder
            first.next = second
            second.next = firstTemp

            #next steps
            second = secondTemp
            first = firstTemp


    



        
