from collections import defaultdict
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = defaultdict(int)
        for n in nums:
            d[n] +=1

        d = sorted(d.items(), key = lambda x : x[1])
        return d[0][0]
