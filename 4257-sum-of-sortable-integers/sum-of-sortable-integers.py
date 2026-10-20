class Solution:
    def sortableIntegers(self, nums):
        n = len(nums)
        target = sorted(nums)

        def kmp_search(text, pattern):
            m = len(pattern)

            lps = [0] * m
            j = 0

            for i in range(1, m):
                while j > 0 and pattern[i] != pattern[j]:
                    j = lps[j - 1]

                if pattern[i] == pattern[j]:
                    j += 1
                    lps[i] = j

            j = 0
            for x in text:
                while j > 0 and x != pattern[j]:
                    j = lps[j - 1]

                if x == pattern[j]:
                    j += 1

                if j == m:
                    return True

            return False

        divisors = []

        d = 1
        while d * d <= n:
            if n % d == 0:
                divisors.append(d)
                if d * d != n:
                    divisors.append(n // d)
            d += 1

        ans = 0

        for k in divisors:
            ok = True

            for start in range(0, n, k):
                a = nums[start:start + k]
                b = target[start:start + k]

                if not kmp_search(a + a, b):
                    ok = False
                    break

            if ok:
                ans += k

        return ans