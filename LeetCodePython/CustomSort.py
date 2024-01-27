from collections import defaultdict
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        od = defaultdict(int)
        ans = [''] * len(s)

        for i in range(len(order)):
            od[order[i]] = i

        for j in range(len(s)):
            if not od[s[j]]:
                ans[j] = s[j]
            else:
                ans[od[s[j]]] = s[j]
            
        return ''.join(ans)
