class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        character_list = set()
        maxLen = 0
        left = 0

        for right in range(len(s)):
            while s[right] in character_list:
                character_list.remove(s[left])
                left += 1
            character_list.add(s[right])
            maxLen = max(maxLen, right - left + 1)
        return maxLen
                
            
