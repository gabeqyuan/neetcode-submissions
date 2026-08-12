class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        left = 0
        right = len(s) - 1 
        lowercase = s.lower()


        while left <= right:
            if not s[left].isalnum():
                left += 1
                continue
            if not lowercase[right].isalnum():
                right -= 1
                continue
            if lowercase[left] == lowercase[right]:
                left += 1
                right -= 1
                continue
            else:
                return False
        return True