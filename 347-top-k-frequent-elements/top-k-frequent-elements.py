
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = Counter(nums)
        minheap = []

        for num, count in freq.items():
            heapq.heappush(minheap, (count, num))
            if len(minheap) > k:
                heapq.heappop(minheap)
        return [num for count, num in minheap]
