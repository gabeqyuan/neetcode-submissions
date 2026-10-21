class TrieNode:
    def __init__(self):
        self.children = {} #children["a"] = TrieNode()
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode() #empty root

    def insert(self, word: str) -> None:
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        #curr is last 
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return curr.endOfWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for ch in prefix:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return True 
        