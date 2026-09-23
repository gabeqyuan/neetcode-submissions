# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l2curr = l2 
        l1curr = l1
        head = ListNode(0, 0)
        result = head 
        carry = 0

        while l2curr or l1curr:
            if l2curr == None:
                l2val = 0
            else:
                l2val = l2curr.val
                l2curr = l2curr.next 

            if l1curr == None:
                l1val = 0
            else:
                l1val = l1curr.val
                l1curr = l1curr.next 

            add = l2val + l1val + carry
            carry = add // 10
            add = add % 10

            new = ListNode(add, None)
            head.next = new 
            head = new
        if carry != 0:
            new = ListNode(carry, None)
            head. next = new


            
            





        return result.next 
