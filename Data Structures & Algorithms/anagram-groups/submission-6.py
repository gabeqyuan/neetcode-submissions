class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hash map with a different letters as a key, the it's value is another 
        #array of words with those groupings of letters 

        result = defaultdict(list)
        for s in strs:
            count = [0] * 26 # initialize count to zero for each of 26 letters
            for c in s:
                count[ord(c) - ord("a" )] += 1

            result[tuple(count)].append(s)
        return list(result.values())

