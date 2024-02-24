class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n=len(points)
        points = sorted(points, key = lambda x: x[1])
        maxa=-float('inf')
 
        ans=0

        for i in range(0,n):
            if maxa<points[i][0]:
                ans+=1
                maxa=points[i][1]

        return ans

