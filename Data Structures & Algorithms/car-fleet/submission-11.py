class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sort = []
        for i in range(len(position)):
            posTuple = (position[i], speed[i])
            sort.append(posTuple)
        sort = sorted(sort)
        sort = list(reversed(sort))

        timeAhead = 0
        fleets = 0
        for a, b in sort:
            time = (target-a)/b
            if time > timeAhead:
                fleets += 1
                timeAhead = time

        return fleets


