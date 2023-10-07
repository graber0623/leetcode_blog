from collections import defaultdict
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = defaultdict(list)
        for i in range(len(groupSizes)):
            d[groupSizes[i]].append(i)
        ans = []
        d = list(sorted(d.items()))
        for item in d:
            if item[0]== len(item[1]):
                ans.append(item[1])

            else:
                l = item[0]
                lst = item[1]
                for i in range(0,len(lst), l):
                    ans.append(lst[i:i+l])
        return ans
