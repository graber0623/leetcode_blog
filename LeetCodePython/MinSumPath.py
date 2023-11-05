# class Solution:
#     def minPathSum(self, grid: List[List[int]]) -> int:
        
#         ans = 8000001
#         m = len(grid[0])
#         n = len(grid)
#         def dfs(i, j, s):
#             nonlocal m, n, ans

#             s += grid[j][i]
#             if i == m-1 and j == n-1:
#                 ans = min(ans, s)
#                 return
#             if 0 <= i < m-1:
#                 dfs(i+1, j, s)
#             if 0 <= j < n-1:
#                 dfs(i, j+1, s)

#         dfs(0, 0, 0)

#         return ans
            

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        m, n = len(grid), len(grid[0])
        dp = [[float('inf')] * n for _ in range(m)]
        
        def dfs(i, j):
            if i >= m or j >= n:
                return float('inf')
            if i == m - 1 and j == n - 1:
                return grid[i][j]
            if dp[i][j] != float('inf'):
                return dp[i][j]
            
            dp[i][j] = grid[i][j] + min(dfs(i + 1, j), dfs(i, j + 1))
            return dp[i][j]
        
        return dfs(0, 0)

# Example usage:
# sol = Solution()
# print(sol.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))  # Output: 7

