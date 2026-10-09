class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        fresh = 0
        rows = len(grid)
        cols = len(grid[0])
        rotten = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    rotten.append((r, c))
                
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        while rotten and fresh > 0:
            for i in range(len(rotten)):
                row, col = rotten.popleft()
                for rowMove, colMove in directions:
                    if row + rowMove < 0 or row + rowMove >= len(grid) or col + colMove < 0 or col + colMove >= len(grid[0]) or grid[row + rowMove][col + colMove] == 0:
                        continue 
                    if grid[row + rowMove][col + colMove] == 1:
                        grid[row + rowMove][col + colMove] = 2
                        fresh -= 1
                        rotten.append((row + rowMove, col + colMove))
            
            time += 1

        return time if fresh == 0 else -1

