from collections import defaultdict
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        r = defaultdict(int)
        new = list(map(list, zip(*grid)))
        print(new)
        for i in range(len(grid)):
            r[str(grid[i])]+=1

        c = 0 
        for j in range(len(grid)):
            if r[str(new[j])]:
                c += r[str(new[j])]

        return c