class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return False if len(list(nums))==len(set(nums)) else True
        