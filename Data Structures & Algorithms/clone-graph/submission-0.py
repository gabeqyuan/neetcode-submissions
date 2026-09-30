"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        seen = {}
        if not node:
            return None

        def dfs(node): 
            #if node alr cloned just return that 
            if node in seen:
                return seen[node]
            
            #firstly we need to make the deep copy of the current node that we are in 
            deep = Node(node.val)
            #then we need to add it to the seen set so we don't count duplicates
            seen[node] = deep 
            #for dfs we need to loop through all neighbors to get every node
            for neighbor in node.neighbors:
                #check seen 
                deep.neighbors.append(dfs(neighbor))
            return deep                

            
        return dfs(node)

            
            


