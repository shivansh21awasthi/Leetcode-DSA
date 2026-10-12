class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        MOD = 10**9 + 7
        bit_count = [0] * 32
        for num in nums:
            for b in range(32):
                if num & (1 << b):
                    bit_count[b] += 1
        res = [0] * len(nums)
        for b in range(32):
            for i in range(bit_count[b]):
                res[i] |= (1 << b)
        res.sort(reverse=True)
        ans = sum(x * x for x in res[:k]) % MOD
        return ans
