class Solution:
    def minPartitions(self, n: str) -> int:
        l = list(n)
        m = 0
        for i in range(len(l)):
            m = max(m, int(l[i]))

        return m