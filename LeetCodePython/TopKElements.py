from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for n in nums:
            d[n] +=1
        
        d = sorted(d, key = lambda x:d[x], reverse = True)
        
        # print(d)
        return d[:k]
    