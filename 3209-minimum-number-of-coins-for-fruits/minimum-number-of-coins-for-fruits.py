import heapq
from typing import List

class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        n = len(prices)
        pq = []
        curr_cost = 0
        
        for i in range(n - 1, -1, -1):
            while pq and pq[0][1] > 2 * i + 2:
                heapq.heappop(pq)
                
            if 2 * i + 2 >= n:
                curr_cost = prices[i]
            else:
                curr_cost = prices[i] + pq[0][0]
                
            heapq.heappush(pq, (curr_cost, i))
            
        return curr_cost