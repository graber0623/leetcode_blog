from collections import defaultdict
class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
        n = len(arrays)
        d = defaultdict(int)

        for l in arrays:
            for num in l:
                d[num] += 1
        ans = []
        for key in list(d.keys()):
            if d[key] == n:
                ans.append(key)

        return ans