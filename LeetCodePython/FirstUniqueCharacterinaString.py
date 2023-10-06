from collections import defaultdict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = defaultdict(int)
        for i in range(len(s)):
            d[s[i]] +=1

        for key in list(d.keys()):
            if d[key] == 1:
                return key
        
        return -1