class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        n = len(piles)
        
        left = 1
        right = max(piles) 

        result = right
        while left <= right:
            middle = (left + right) // 2
            time = 0
            for i in range(n): #5 when middle = 2 5.0/2 = 2.5 -> 3
                time += math.ceil(float(piles[i]) / middle)
            if time <= h:
                result = middle 
                right = middle - 1
            else:
                left = middle + 1

        return result

