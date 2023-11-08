class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            return True
        return False
    
from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ds = defaultdict(int)
        dt = defaultdict(int)
        for i in range(len(s)):
            ds[s[i]] +=1

        for j in range(len(t)):
            dt[t[j]] +=1

        for key in ds.keys():
            if not dt[key]:
                return False
            if dt[key] != ds[key]:
                return False
        
        for key in dt.keys():
            if not ds[key]:
                return False
            if dt[key] != ds[key]:
                return False
        return True