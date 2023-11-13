from collections import defaultdict
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) == 0 and n == 1:
            return 1
        d = defaultdict(list)
        truster = set()
        for i in range(len(trust)):
            truster.add(trust[i][0])
            d[trust[i][1]].append(trust[i][0])

        for key in d.keys():
            if len(d[key]) == n-1 and key not in truster:
                    return key
        return -1