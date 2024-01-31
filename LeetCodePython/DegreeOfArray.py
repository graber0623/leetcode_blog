from collections import defaultdict
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        d = defaultdict(list)
        for i, num in enumerate(nums):
            d[num].append(i)
        m = 5000000
        for key in list(d.keys()):
    
            if d[key][-1]-d[key][0]+1 != 1:
                m = min(m, d[key][-1]-d[key][0]+1)

        return m