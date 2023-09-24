


class Solution: ## DAMM IT ALMOST>.... FUCK!
    def shortestBridge(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(i, j, l, started):
            if i < 0 or i >= m or j < 0 or j >=n or grid[i][j] == -1:
                return m*n
            if grid[i][j] == 1 and started == 1 and l == 1:
                return m*n

            if grid[i][j] == 1 and started == 1:
                return l
            elif grid[i][j] == 1 and started == 0:
                grid[i][j] = -1
                l1 = dfs(i-1, j, l+1, 1)
                l2 = dfs(i+1, j, l+1, 1)
                l3 = dfs(i, j+1, l+1, 1)
                l4 = dfs(i, j-1, l+1, 1)
                return min(l1,l2,l3,l4)
            elif grid[i][j] == 0 and started == 1:
                grid[i][j] = -1
                l1 = dfs(i-1, j, l+1, 1)
                l2 = dfs(i+1, j, l+1, 1)
                l3 = dfs(i, j+1, l+1, 1)
                l4 = dfs(i, j-1, l+1, 1)
                return min(l1,l2,l3,l4)
            else:
                return m*n
    
        min_length = m*n

        for i in range(m):
            for j in range(n):
                re = dfs(i,j,0,0)
                min_length = min(min_length, re-1)

        return min_length
# class Solution:
#     def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
#         m = len(grid)
#         n = len(grid[0])
        
#         def dfs(i,j,size):
#             if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
#                 return size
            
#             grid[i][j] = 0
#             size += 1
        
#             size = dfs(i+1, j,size)
#             size = dfs(i-1, j,size)
#             size = dfs(i, j+1,size)
#             size = dfs(i, j-1,size)
#             return size
        
            
        
#         max_size = 0
#         for i in range(m):
#             for j in range(n):
#                 s = dfs(i, j, 0)
#                 max_size = max(s, max_size)
    
                
        
# #         return max_size
    
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         r = len(grid)
#         c = len(grid[0])
#         if r == 0:
#             return 0
#         def dfs(i, j):
#             if i<0 or i>=r or j<0 or j>=c or grid[i][j] =="0":
#                 return
#             grid[i][j]="0"
#             dfs(i, j-1)
#             dfs(i, j+1)
#             dfs(i-1, j)
#             dfs(i+1, j)
#             return 1
#         count =0
#         for i in range(r):
#             for j in range(c):
#                 if grid[i][j] =="1":
#                     count += dfs(i,j)
#         return count
            
            
        