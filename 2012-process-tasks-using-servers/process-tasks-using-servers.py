import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        free = []
        busy = []

        for i in range(len(servers)):
            heapq.heappush(free, (servers[i], i))

        ans = []
        time = 0

        for i in range(len(tasks)):
            time = max(time, i)

            while busy and busy[0][0] <= time:
                finish, weight, idx = heapq.heappop(busy)
                heapq.heappush(free, (weight, idx))

            if not free:
                time = busy[0][0]

                while busy and busy[0][0] <= time:
                    finish, weight, idx = heapq.heappop(busy)
                    heapq.heappush(free, (weight, idx))

            weight, idx = heapq.heappop(free)

            ans.append(idx)

            heapq.heappush(
                busy,
                (time + tasks[i], weight, idx)
            )

        return ans