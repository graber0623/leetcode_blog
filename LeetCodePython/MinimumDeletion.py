
from collections import defaultdict
class Solution:
    def minDeletions(self, s: str) -> int:
        d = defaultdict(int)
        ans = 0
        
        for i in range(len(s)):
            d[s[i]] +=1

        items = sorted(d.items(), key = lambda x : x[1], reverse = True)
        last_count = items[0][1]
        current_deletions = 0
        for j in range(1, len(items)):

            if last_count <= items[j][1]:
                if last_count == 0 or last_count == 1:
                    current_deletions = items[j][1]
                else: current_deletions = abs(last_count - items[j][1]) +1
                ans += current_deletions
                last_count = items[j][1] - current_deletions

            else:
                last_count = items[j][1]

        return ans
