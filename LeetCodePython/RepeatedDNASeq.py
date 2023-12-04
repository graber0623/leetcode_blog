from collections import defaultdict
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ans = []
        if len(s) <= 10:
            return ans
        d = defaultdict(int)
        for i in range(0,len(s)-9):
            d[s[i:i+10]] += 1

        for key in list(d.keys()):
            if d[key] > 1:
                ans.append(key)
        
        return ans