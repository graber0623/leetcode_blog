from collections import defaultdict
import math

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d = defaultdict(int)

        for num in nums:
            d[num] += 1

        ans = 0
        for key in list(d.keys()):
            if d[key] > 1:
                for i in range(d[key]-1, 0, -1):
                    ans+=i  
        return ans