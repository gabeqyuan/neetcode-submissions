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
        substringChars = {}
        substring = s2[start:end]
        for ch in substring:
            if ch in substringChars:
                substringChars[ch] += 1
            else: 
                substringChars[ch] = 1
        while end <= len(s2):
            if permChars == substringChars:
                return True
            substring = s2[start:end]
            if end == len(s2):
                break
            substringChars[s2[start]] -= 1
            if substringChars[s2[start]] == 0:
                substringChars.pop(s2[start])
            if s2[end] in substringChars:
                substringChars[s2[end]] += 1
            else:
                substringChars[s2[end]] = 1
            start += 1
            end += 1
        return False




