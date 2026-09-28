class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        temp = abs(x) 

        while temp != 0:
            rev = rev * 10 
            add = temp % 10 
            rev += add 
            temp = temp // 10 
        
        if x < 0:
            rev = rev * -1
        if (rev < -2**31) or rev > (2**31 - 1):
            return 0
        
        return rev 
