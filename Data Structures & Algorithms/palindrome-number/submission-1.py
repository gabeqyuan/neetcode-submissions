class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        rev = 0
        temp = x
        while temp != 0:
            add = temp % 10
            temp = temp // 10 
            rev = rev * 10
            rev += add
        return rev == x