class Solution:
    def minOperations(self, nums: list[int], x: int, k: int) -> int:
        n = len(nums)

        lower = SortedList()
        upper = SortedList()
        lsum = usum = 0

        def add(num):
            nonlocal lsum, usum

            if not lower or num <= lower[-1]:
                lower.add(num)
                lsum += num
            else:
                upper.add(num)
                usum += num

            balance()

        def remove(num):
            nonlocal lsum, usum

            if num in lower:
                lower.remove(num)
                lsum -= num
            else:
                upper.remove(num)
                usum -= num

            balance()

        def balance():
            nonlocal lsum, usum

            while len(lower) < len(upper):
                v = upper[0]
                upper.remove(v)
                usum -= v

                lower.add(v)
                lsum += v

            while len(lower) > len(upper) + 1:
                v = lower[-1]
                lower.remove(v)
                lsum -= v

                upper.add(v)
                usum += v

        def get_cost():
            m = lower[-1]

            left = m * len(lower) - lsum
            right = usum - m * len(upper)

            return left + right

        for i in range(x):
            add(nums[i])

        costs = [get_cost()]

        for i in range(x, n):
            remove(nums[i - x])
            add(nums[i])

            costs.append(get_cost())

        m = len(costs)

        dp = [[float("inf")] * (k + 1) for _ in range(m + x + 1)]

        for i in range(m + x + 1):
            dp[i][0] = 0

        for i in range(m - 1, -1, -1):
            for j in range(1, k + 1):
                dp[i][j] = dp[i + 1][j]

                if i + x <= m + x:
                    dp[i][j] = min(
                        dp[i][j],
                        costs[i] + dp[i + x][j - 1]
                    )

        return dp[0][k]