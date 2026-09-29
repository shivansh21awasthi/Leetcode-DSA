class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        freq = Counter(words)
        heap = [(-count, word) for word, count in freq.items()]
        heapq.heapify(heap)
        result = []
        for _ in range(k):
            count, word = heapq.heappop(heap)
            result.append(word)

        return result
