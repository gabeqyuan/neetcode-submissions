class Solution:

    def encode(self, strs: List[str]) -> str:
        length = len(strs)
        string = ""
        for index, value in enumerate(strs):
            string += str(len(value)) + "#"
            string += value
        return string
    def decode(self, s: str) -> List[str]:
        stringList = []
        length = len(s)
        i = 0
        while i < length:
            j = i
            while s[j] != "#":
                j += 1

            buildLength = int(s[i:j])
            j += 1

            stringList.append(s[j:j + buildLength])
            i = j + buildLength
        return stringList
                
            
