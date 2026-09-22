import heapq

class MedianFinder:

    def __init__(self):
        self.heap1 = []
        self.heap2 = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.heap1, -num)
        
        if self.heap2 and -self.heap1[0] > self.heap2[0]:
            x = -heapq.heappop(self.heap1)
            heapq.heappush(self.heap2, x)

        if len(self.heap1) > len(self.heap2) + 1:
            x = -heapq.heappop(self.heap1)
            heapq.heappush(self.heap2, x)
        elif len(self.heap2) > len(self.heap1):
            x = heapq.heappop(self.heap2)
            heapq.heappush(self.heap1, -x)

    def findMedian(self) -> float:
        if len(self.heap1) > len(self.heap2):
            return float(-self.heap1[0])
        return (-self.heap1[0] + self.heap2[0]) / 2.0