class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        nums.sort()
        print(nums)
        return nums[-k]