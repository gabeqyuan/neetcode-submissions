class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-n for n in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            max_stone = heapq.heappop(heap)
            second_stone = heapq.heappop(heap)
            if max_stone == second_stone:
                continue 
            else:
                max_stone = max_stone - second_stone
                heapq.heappush(heap, max_stone)
        
        return -heap[0] if heap else 0
