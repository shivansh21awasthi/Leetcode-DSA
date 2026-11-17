class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        cost = [[inf] * n for _ in range(n)]
        
        for i in range(n):
            for j in range(i, n):
                length = j - i + 1
                min_changes = inf
                for d in range(1, length):
                    if length % d == 0:
                        cur = 0
                        for group in range(d):
                            l = group
                            r = length - d + group
                            while l < r:
                                if s[i + l] != s[i + r]:
                                    cur += 1
                                l += d
                                r -= d
                        min_changes = min(min_changes, cur)
                cost[i][j] = min_changes
                
        dp = [[inf] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        
        for c in range(1, k + 1):
            for i in range(1, n + 1):
                for j in range(c - 1, i):
                    dp[i][c] = min(dp[i][c], dp[j][c - 1] + cost[j][i - 1])
                    
        return dp[n][k]