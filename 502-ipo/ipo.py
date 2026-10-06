import heapq
import operator

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        projects = []
        for idx in range(len(profits)):
            projects.append((capital[idx], profits[idx]))

        projects.sort(key=operator.itemgetter(0))

        n = len(projects)
        i = 0
        max_heap = []

        for _ in range(k):
            while i < n and projects[i][0] <= w:
                heapq.heappush(max_heap, -projects[i][1])
                i += 1

            if not max_heap:
                break

            w += -heapq.heappop(max_heap)

        return w
