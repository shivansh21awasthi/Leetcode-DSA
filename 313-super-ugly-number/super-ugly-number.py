class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ugly = [1] * n
        k = len(primes)
        idx = [0] * k
        next_vals = [p for p in primes]
        
        for i in range(1, n):
            ugly[i] = min(next_vals)
            
            for j in range(k):
                if ugly[i] == next_vals[j]:
                    idx[j] += 1
                    next_vals[j] = ugly[idx[j]] * primes[j]
        
        return ugly[-1]
