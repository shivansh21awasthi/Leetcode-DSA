class Solution:
    def sortPermutation(self, nums):
        ans = -1

        for i, x in enumerate(nums):
            if x != i:
                if ans == -1:
                    ans = x
                else:
                    ans &= x

        return max(ans, 0)