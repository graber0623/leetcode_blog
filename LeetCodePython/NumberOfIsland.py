# def noi(grid): ## VERY WRONG
#     m = len(grid)
#     n = len(grid[0])
#     c = 0
#     def dfs(i ,j, last_point, count):
        
#         if grid[i][j] != last_point:
#             count +=1
        
#         last_point = grid[i][j]
#         if i < n-1 and j < m-1:
#             dfs(i+1, j, last_point, count)
#             dfs(i, j+1, last_point, count)
        
#         elif i < n-1 and j >= m -1:
#             dfs(i+1, j, last_point, count)
        
#         elif i >= n-1 and j < m-1:
#             dfs(i, j+1, last_point, count)
#         else:
#             return
    
#     dfs(0,0,0, c)
#     return c

# def noi(grid):
#     n = len(grid[0])
#     m = len(grid)
#     c = 0
#     def dfs(i, j):
#         if grid[i][j] == "1":
#             grid[i][j] == "-1"
        
#         if 0 <= i and i < n-1:
#             dfs(i + 1, j)
            
#         if 0 <= j and j < m-1:
#             dfs(i, j+1)
            
#     for x in range(n):
#         for y in range(m):
#             if grid[x][y] == "1":
#                 c +=1
#                 dfs(x, y)
#     return c

def noi(grid):
    n = len(grid)
    m = len(grid[0])
    c = 0
    
    def dfs(i, j):
        if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] != "1":
            return
        grid[i][j] = "-1"

        # Explore adjacent cells
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

            
    for x in range(n):
        for y in range(m):
            if grid[x][y] == "1":
                c +=1
                dfs(x, y)
    return c
            
            
    

a = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

print(noi(a))