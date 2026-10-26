class Solution:
    def countIslands(self, grid, k):
        m, n = len(grid), len(grid[0])
        ans = 0

        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        for r in range(m):
            for c in range(n):

                if grid[r][c] > 0:

                    total = 0
                    q = deque([(r, c)])

                    total += grid[r][c]
                    grid[r][c] = 0

                    while q:
                        x, y = q.popleft()

                        for dx, dy in dirs:
                            nx, ny = x + dx, y + dy

                            if (0 <= nx < m and
                                0 <= ny < n and
                                grid[nx][ny] > 0):

                                total += grid[nx][ny]
                                q.append((nx, ny))
                                grid[nx][ny] = 0

                    if total % k == 0:
                        ans += 1

        return ans