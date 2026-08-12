class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def bfs(r, c):
            if r >= len(grid) or c >= len(grid[0]) or r < 0 or c < 0 or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0
            return 1 + bfs(r + 1, c) + bfs(r, c + 1) + bfs(r, c - 1) + bfs(r - 1, c)

        maxArea = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    maxArea = max(bfs(row, col), maxArea)
                    print(maxArea)
        
        return maxArea
