from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for c, p in prerequisites:
            graph[p].append(c)
            indegree[c] += 1

        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        while q:
            c = q.popleft()
            numCourses -= 1

            for nc in graph[c]:
                indegree[nc] -= 1

                if indegree[nc] == 0:
                    q.append(nc)

        return numCourses == 0