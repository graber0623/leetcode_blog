# from collections import defaultdict
# class Solution:
#     def isIsomorphic(self, s: str, t: str) -> bool:
#         ds = defaultdict(int)
#         dt = defaultdict(int)
#         for i in range(len(s)):
#             ds[s[i]] +=1
#             dt[t[i]] +=1

#         dsv = sorted(list(ds.values()))
#         dtv = sorted(list(dt.values()))

#         if len(dsv) != len(dtv):
#             return False

#         for i in range(len(dsv)):
#             if dsv[i] != dtv[i]:
#                 return False
#         return True            
# Time Complexity : O(n)
class Solution(object):
    def isIsomorphic(self, s, t):
        map1 = []
        map2 = []
        for idx in s:
            map1.append(s.index(idx))
        for idx in t:
            map2.append(t.index(idx))
        if map1 == map2:
            return True
        return False