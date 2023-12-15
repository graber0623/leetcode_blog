class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points = sorted(points, key = lambda x : (x[0], x[1]))
        
        m = 0
        for i in range(1,len(points)):
            m = max(m, points[i][0]-points[i-1][0])

        return m