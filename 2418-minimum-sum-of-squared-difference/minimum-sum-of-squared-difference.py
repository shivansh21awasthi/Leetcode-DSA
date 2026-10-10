class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        n = len(nums1)
        diffs = [abs(nums1[i] - nums2[i]) for i in range(n)]
        k = k1 + k2
        maxDiff = max(diffs)

        freq = [0] * (maxDiff + 1)
        for d in diffs:
            freq[d] += 1

        for d in range(maxDiff, 0, -1):
            if freq[d] > 0 and k > 0:
                moves = min(k, freq[d])
                freq[d] -= moves
                freq[d - 1] += moves
                k -= moves

        ans = 0
        for d in range(maxDiff + 1):
            if freq[d] > 0:
                ans += freq[d] * d * d
        return ans
