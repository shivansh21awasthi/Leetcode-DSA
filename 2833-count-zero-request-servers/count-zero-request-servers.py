from collections import defaultdict

class Solution:
    def countServers(self, n, logs, x, queries):
        logs.sort(key=lambda log: log[1])

        indexed = []
        for i in range(len(queries)):
            indexed.append((queries[i], i))

        indexed.sort()

        count = defaultdict(int)
        ans = [0] * len(queries)

        left = 0
        right = 0
        active = 0

        for q, idx in indexed:

            while right < len(logs) and logs[right][1] <= q:
                server = logs[right][0]

                if count[server] == 0:
                    active += 1

                count[server] += 1
                right += 1

            while left < len(logs) and logs[left][1] < q - x:
                server = logs[left][0]

                count[server] -= 1

                if count[server] == 0:
                    active -= 1

                left += 1

            ans[idx] = n - active

        return ans