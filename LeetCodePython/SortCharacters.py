from collections import defaultdict
class Solution:
    def frequencySort(self, s: str) -> str:
        d = defaultdict(int)
        for i in range(len(s)):
            d[s[i]] += 1

        z = sorted(d.items(), key=lambda x : (-1*x[1],x[0]))
        ans = ''
        for item in z:
            ans += item[0] * item[1]
        
        return ans
    