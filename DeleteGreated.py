class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        grid = [sorted(x, reverse = True) for x in grid]
        sum = 0

        for i in range(len(grid[0])):
            max_poped = 0
            for j in range(len(grid)):
                poped = grid[j][i]
                max_poped = max(max_poped, poped)
            sum+=max_poped
        
        return sum

