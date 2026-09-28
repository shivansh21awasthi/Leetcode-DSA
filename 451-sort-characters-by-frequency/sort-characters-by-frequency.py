
class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        heap = [(-count, ch) for ch, count in freq.items()]
        heapq.heapify(heap)
        result = []
        while heap:
            count, ch = heapq.heappop(heap)
            result.append(ch * -count)

        return "".join(result)
