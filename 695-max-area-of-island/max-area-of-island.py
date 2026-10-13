# from collections import deque

# class Solution:
#     def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
#         rows= len(grid)
#         cols= len(grid[0])
#         maxarea = 0

#         directions = [(-1,0),(1,0),(0,-1),(0,1)]

#         for r in range(rows):
#             for c in range(cols):
#                 if grid[r][c] == 1: 
#                     area = 0
#                     queue = deque()
#                     queue.append((r,c))
#                     grid[r][c] = 0     

#                     while queue:
#                         r, c = queue.popleft()
#                         area += 1
#                         for dr, dc in directions:
#                             nr, nc = r+dr, c+dc
#                             if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
#                                 grid[nr][nc] = 0
#                                 queue.append((nr,nc))

#                     maxarea = max(maxarea, area)

#         return maxarea

#DFS

class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c) -> int:
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0
            grid[r][c] = 0  
            area = 1         
            area += dfs(r+1, c)
            area += dfs(r-1, c)
            area += dfs(r, c+1)
            area += dfs(r, c-1)
            return area

        maxarea = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1: 
                    maxarea = max(maxarea, dfs(r,c))

        return maxarea
