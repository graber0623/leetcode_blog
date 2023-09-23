class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        L = len(s)
        last = {}
        for i in range(L):
            last[s[i]] = i
        i = 0
        ans = []
        while i<L:
            end = last[s[i]]
            j = i+1
            while j < end:
                if last[s[j]] > end:
                    end = last[s[j]]
                j+=1

            ans.append(end-i+1)
            i = end+1
        return ans
        



