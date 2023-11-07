from collections import defaultdict
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        d = defaultdict(int)

        for i in arr:
            d[i] +=1

        d = list(sorted(d.values()))

        for i in range(1, len(d)):
            if d[i] == d[i-1]:
                return False

        return True
        