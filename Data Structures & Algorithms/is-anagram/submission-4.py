class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    # iterate through each string and create a hash table
    # each letter as the key and each time they appear increase the count by one 
        if len(s) != len(t):
            return False
        s_map = {}
        t_map = {}

        for i in range(len(s)):
            s_map[s[i]] = 1 + s_map.get(s[i], 0)
            t_map[t[i]] = 1 + t_map.get(t[i], 0)
        for k in s_map:
            if s_map != t_map:
                return False

        return True
