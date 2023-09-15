class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0]) 
        start_c = image[sr][sc]
        def dfs(i,j):
            nonlocal image, color, m, n, start_c
            if i < 0 or i >= m or j < 0 or j>= n:
                return
            if image[i][j] != start_c:
                return
            if image[i][j] == color:
                return
            image[i][j] = color
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        
        dfs(sr, sc)
        return image