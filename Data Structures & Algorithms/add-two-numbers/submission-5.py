# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1curr = l1
        l2curr = l2 
        head = ListNode(0, 0)
        res = head
        carry = 0

        while l1curr or l2curr: #walking thru the longest linked list
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
            if add > 9:
                add = add % 10
            
            node = ListNode(add, None)
            head.next = node
            head = node
        if carry != 0:
            node = ListNode(carry, None)
            head.next = node
            

        return res.next
            
                    
