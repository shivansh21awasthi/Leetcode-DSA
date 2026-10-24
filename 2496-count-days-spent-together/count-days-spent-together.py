class Solution:
    def countDaysTogether(self, aa: str, la: str, ab: str, lb: str) -> int:
        days = [31,28,31,30,31,30,31,31,30,31,30,31]

        def f(s):
            m, d = map(int, s.split('-'))
            return sum(days[:m-1]) + d

        return max(0, min(f(la), f(lb)) - max(f(aa), f(ab)) + 1)