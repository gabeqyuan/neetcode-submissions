class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        '''
        removing leafs approach 
        intuition : the roots will always be in the middle of the tree. so removing leaves of the tree those cannot be the minimum roots because they are only connected by less edges than the roots would be. 
        '''
        if n == 1:
            return [0]
        adj = defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        edge_count = {} # {node: 2}
        #leaves of the tree in a queue for easy access and can append and pop
        leaves = deque()
        for node, nei in adj.items(): 
            if len(nei) == 1: #means its a leaf
                leaves.append(node)
            edge_count[node] = len(nei)

        while leaves: 
            #stop condition is if n (num nodes) is 2 or less (max amount of nodes as roots)
            if n <= 2:
                return list(leaves)
            # if not we need to iterate through the leaves and then check if the neighbors are leaves to be added 
            for i in range(len(leaves)):
                node = leaves.popleft()
                n -= 1
                # we need to decremeent the edge counts 
                for neighbor in adj[node]:
                    edge_count[neighbor] -= 1
                    if edge_count[neighbor] == 1:
                        leaves.append(neighbor)





        