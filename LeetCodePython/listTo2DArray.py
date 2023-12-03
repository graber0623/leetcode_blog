from collections import defaultdict
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        d = defaultdict(int)

        for num in nums:
            d[num] +=1
        
        ans = []
        for i in range(max(d.values())):
            res = []
            for k in d.keys():
                if d[k] != 0:
                    d[k] -= 1
                    res.append(k)
            ans.append(res)
        
        return ans

