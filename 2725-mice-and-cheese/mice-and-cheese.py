import heapq

class Solution:
    def miceAndCheese(self, reward1: list[int], reward2: list[int], k: int) -> int:
        total = sum(reward2)
        heap = []
        for i in range(len(reward1)):
            gain = reward1[i] - reward2[i]
            heapq.heappush(heap, -gain)
        for _ in range(k):
            total += -heapq.heappop(heap)

        return total
