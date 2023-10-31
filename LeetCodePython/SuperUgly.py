class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        super_ugly = [1]

        idx = [0] * len(primes)

        prod = [p for p in primes]

        while len(super_ugly) < n:
            next_ugly = min(prod)
            super_ugly.append(next_ugly)

            for i in range(len(primes)):
                if next_ugly == prod[i]:
                    idx[i] += 1
                    prod[i] = primes[i] * super_ugly[idx[i]]

        return super_ugly[-1]