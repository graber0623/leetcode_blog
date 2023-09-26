from collections import defaultdict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = defaultdict(int)
        m = defaultdict(int)
        for i in range(len(ransomNote)):
            r[ransomNote[i]] += 1
        
        for j in range(len(magazine)):
            m[magazine[j]] += 1

        for key in list(r.keys()):
            if not m[key] or r[key] > m[key]:
                return False
        return True
        