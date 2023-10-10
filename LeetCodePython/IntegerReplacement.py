class Solution:
    def integerReplacement(self, n: int) -> int:
        min_count = 2**31 - 1
        def dfs(num, c):
            nonlocal min_count
            if num == 1:
                min_count = min(min_count, c)
                return
            
            if num%2 == 0:
                dfs(num//2, c+1)
            else:
                dfs(num-1, c+1)
                dfs(num+1, c+1)
        dfs(n, 0)

        return min_count