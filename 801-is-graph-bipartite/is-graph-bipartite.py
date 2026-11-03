from collections import deque

class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        n = len(graph)
        color = [0] * n

        for i in range(n):

            if color[i] != 0:
                continue

            q = deque([i])
            color[i] = 1

            while q:
                node = q.popleft()

                for nei in graph[node]:

                    if color[nei] == 0:
                        color[nei] = -color[node]
                        q.append(nei)

                    elif color[nei] == color[node]:
                        return False

        return True