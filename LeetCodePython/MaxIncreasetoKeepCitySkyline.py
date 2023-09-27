class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        c = 0
        for i in range(n):
            for j in range(n):
                hori_building = grid[i]
                
                verti_building = []
                for x in range(n):
                    verti_building.append(grid[x][j])

                changable = min(max(hori_building), max(verti_building))
                
                if changable > grid[i][j]:
                    c += (changable - grid[i][j])


        return c
    
## WOULD BE FASTER IF I COULD MAKE A DICTIONARY FOR MAX POSSIBLE OR ARRAY