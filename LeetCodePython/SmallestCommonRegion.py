from collections import defaultdict
class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        r = defaultdict(str)
        for i in range(len(regions)):
            for j in range(1,len(regions[i])):
                r[regions[i][j]]=(regions[i][0])
        
        print(r)

        r1_path = set()
        r1 = region1
        while r1 != '':
            r1_path.add(r1)
            if r[r1]:
                r1 = r[r1]
            else:
                r1 = ''

        r2 = region2
        ans = ''
        while r2 != '':
            if r2 in r1_path:
                ans = r2
                break
            else:
                r2 = r[r2]

        return ans
        



        