from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        rows= len(grid)
        cols= len(grid[0])
        maxarea = 0

        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1: 
                    area = 0
                    queue = deque()
                    queue.append((r,c))
                    grid[r][c] = 0     

                    while queue:
                        r, c = queue.popleft()
                        area += 1
                        for dr, dc in directions:
                            nr, nc = r+dr, c+dc
                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                                grid[nr][nc] = 0
                                queue.append((nr,nc))

                    maxarea = max(maxarea, area)

        return maxarea
