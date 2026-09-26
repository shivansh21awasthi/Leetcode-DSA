class Solution:
    def isHappy(self, n: int) -> bool:
        seen = []
        while n != 1 and n not in seen:
            seen.append(n)  
            total = 0
            for digit in str(n):
                total += int(digit) ** 2
            n = total
        return n == 1
