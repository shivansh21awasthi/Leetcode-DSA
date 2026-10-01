from sortedcontainers import SortedList
from typing import List

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        window = SortedList(nums[:k])
        res = []
        
        for i in range(k, len(nums) + 1):
            if k % 2 == 1:
                res.append(float(window[k // 2]))
            else:
                res.append((window[k // 2 - 1] + window[k // 2]) / 2.0)
            if i < len(nums):
                window.remove(nums[i - k])
                window.add(nums[i])
                
        return res