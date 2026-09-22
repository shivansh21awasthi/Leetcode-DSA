import heapq

class SeatManager:
    def __init__(self, n: int):
        self.minheap = list(range(1, n+1))
        heapq.heapify(self.minheap)

    def reserve(self) -> int:
        return heapq.heappop(self.minheap)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.minheap, seatNumber)
