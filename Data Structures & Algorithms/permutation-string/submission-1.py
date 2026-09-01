class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        windowLength = len(s1)
        start = 0 
        end = windowLength
        permChars = {}
        for ch in s1:
            if ch in permChars:
                permChars[ch] += 1
            else: 
                permChars[ch] = 1
        while end != len(s2) + 1:
            substring = s2[start:end]
            substringChars = {}
            for ch in substring:
                if ch in substringChars:
                    substringChars[ch] += 1
                else: 
                    substringChars[ch] = 1
            if permChars == substringChars:
                return True
            start += 1
            end += 1
        return False




