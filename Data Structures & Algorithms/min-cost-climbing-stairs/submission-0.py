class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        #can start at cost[0] or cost[1]
        #manipulate cost array 

        for i in range(len(cost) - 3, -1, -1):
            cost[i] = min(cost[i] + cost[i + 1], cost[i] + cost[i + 2])

        return min(cost[0], cost[1])

