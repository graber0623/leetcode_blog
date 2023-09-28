from math import sqrt
class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ans = []
        for circle in queries:
            c = 0
            x = circle[0]
            y = circle[1]
            r = circle[2]
            for point in points:
                if r >= sqrt((point[0]-x)**2 + (point[1]-y)**2):
                    c+=1

            ans.append(c)

        return ans