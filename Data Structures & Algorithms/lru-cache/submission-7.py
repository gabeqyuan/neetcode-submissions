class LRUCache:
    class Node: 
        def __init__ (self, key, value):
            self.key = key
            self.val = value
            self.prev = None
            self.next = None 

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # mapping key to node
        self.LRU = self.Node(0,0)
        self.MRU = self.Node(0,0)
        self.LRU.next = self.MRU
        self.MRU.prev = self.LRU

    def remove(self, node):
        prev = node.prev
        nextN = node.next
        prev.next = nextN
        nextN.prev = prev

    def insert(self, node): 
        prev = self.MRU.prev
        nextN = self.MRU
        prev.next = node
        nextN.prev = node
        node.prev = prev
        node.next = nextN


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = self.Node(key,value)
        self.insert(self.cache[key])
        if len(self.cache) > self.cap:
            lru = self.LRU.next
            self.remove(lru)
            del self.cache[lru.key]
