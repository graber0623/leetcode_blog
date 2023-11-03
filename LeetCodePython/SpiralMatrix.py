class Solution:
    def spiralOrder(self, matrix):
        movement = 'row_plus'
        n = len(matrix) #j
        m = len(matrix[0]) #i
        ans = []
        def dfs(i, j, last_move):
            nonlocal matrix, ans, m, n
            if len(ans) == m*n:
                return
            
            ans.append(matrix[j][i])
            matrix[j][i] = -1000 #landed
            print(ans)
            if last_move == 'row_plus':
                if 0<= i < m-1:
                    if matrix[j][i+1] == -1000:
                        last_move = 'col_plus'
                        dfs(i,j+1,last_move)
                    else:
                        dfs(i+1, j, last_move)
              
                elif i == m-1:
                    last_move = 'col_plus'
                    dfs(i, j+1, last_move)
            
            elif last_move == 'col_plus':
                if 0<= j < n-1:
                    if matrix[j+1][i] == -1000:
                        last_move = 'row_minus'
                        dfs(i-1,j,last_move)
                    else:
                        dfs(i, j+1, last_move)
              
                elif j == n-1:
                    last_move = 'row_minus'
                    dfs(i-1, j, last_move)

            elif last_move == 'row_minus':
                if 0 < i <=m-1:
                    if matrix[j][i-1] == -1000:
                        last_move = 'col_minus'
                        dfs(i,j-1,last_move)
                    else:
                        dfs(i-1, j, last_move)
              
                elif i == 0:
                    last_move = 'col_minus'
                    dfs(i,j-1,last_move)
            
            elif last_move == 'col_minus':
                if 0 < j <=n-1:
                    if matrix[j-1][i] == -1000:
                        last_move = 'row_plus'
                        dfs(i+1,j,last_move)
                    else:
                        dfs(i, j-1, last_move)
              
                elif j == 0:
                    last_move = 'row_plus'
                    dfs(i+1,j,last_move) 
        
        dfs(0,0,'row_plus')

        return ans
d = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

# print(m[0][1])

print(Solution.spiralOrder(Solution, d))