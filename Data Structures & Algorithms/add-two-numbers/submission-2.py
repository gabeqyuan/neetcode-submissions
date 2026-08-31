# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1Curr = l1
        l2Curr = l2
        newHead = ListNode(0, None)
        result = newHead
        carry = 0
        while l2Curr or l1Curr:
            if l2Curr == None:
                l2Val = 0
            else:
                l2Val = l2Curr.val
                l2Curr = l2Curr.next

            if l1Curr == None:
                l1Val = 0
            else:
                l1Val = l1Curr.val
                l1Curr = l1Curr.next

            add = l2Val + l1Val + carry
            carry = add//10

            if add >= 10:
                add = add % 10

            new = ListNode(add, None)
            newHead.next = new 
            newHead = new
        if carry != 0:
            new = ListNode(carry, None)
            newHead.next = new
        return result.next


