class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        def digit_sum(x):
            s = 0
            while x > 0:
                s += x % 10
                x //= 10
            return s

        target = sorted(nums, key=lambda x: (digit_sum(x), x))
        pos = {}
        i = 0
        for num in target:
            pos[num] = i
            i += 1

        nums = nums[:]
        swaps = 0
        for i in range(len(nums)):
            while pos[nums[i]] != i:
                j = pos[nums[i]]
                nums[i], nums[j] = nums[j], nums[i]
                swaps += 1
        return swaps
