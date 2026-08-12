class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        character_list = set()
        l = 0
        maxLen = 0

        for r in range(len(s)):
            #condition to move left 
            while s[r] in character_list:
                character_list.remove(s[l])
                l += 1
            #add r to the set 
            character_list.add(s[r])
            maxLen = max(maxLen, r - l + 1)
        return maxLen
                
            
