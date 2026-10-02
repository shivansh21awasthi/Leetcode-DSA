import heapq
from typing import List

class Solution:
    def fillCups(self, amount: List[int]) -> int:
        max_heap = [-c for c in amount if c > 0]
        heapq.heapify(max_heap)  
        seconds = 0
        while len(max_heap) > 1:
            first = -heapq.heappop(max_heap)
            second = -heapq.heappop(max_heap)    
            seconds += 1
            if first - 1 > 0:
                heapq.heappush(max_heap, -(first - 1))
            if second - 1 > 0:
                heapq.heappush(max_heap, -(second - 1))
        if max_heap:
            seconds += -max_heap[0]
            
        return seconds