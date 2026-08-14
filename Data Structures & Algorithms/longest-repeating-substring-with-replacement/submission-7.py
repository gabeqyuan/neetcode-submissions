class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maximum = 0
        chars = set(s)
        for cs in chars:
            count = 0
            left = 0 
            for right in range(len(s)):
                if s[right] == cs:
                    count += 1
                while (right - left + 1) - count > k:
                    if s[left] == cs:
                        count -= 1
                    left += 1
                
                maximum = max(maximum, right - left + 1)

        return maximum

            


        