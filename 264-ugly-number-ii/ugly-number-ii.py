
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        seen = {1}
        
        for _ in range(n):
            ugly = heapq.heappop(heap)
            for f in (2, 3, 5):
                nxt = ugly * f
                if nxt not in seen:
                    seen.add(nxt)
                    heapq.heappush(heap, nxt)
        
        return ugly
