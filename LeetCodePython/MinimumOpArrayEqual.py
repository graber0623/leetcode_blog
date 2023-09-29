class Solution:
    def minOperations(self, n: int) -> int:
        ans = 0
        for i in range(n-1,-1,-2):
            ans+=(2*i)/2

        return int(ans)