class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        ans = 0
        # "M", "G", "P"
        ans = sum(travel) * 3
        for garb in garbage:
            ans += len(garb)
        
        ## "M"
        for i in range(len(garbage)-1, 0, -1):
            if "M" not in garbage[i]:
                ans -= travel[i-1]
                continue
            else:
                break
        for i in range(len(garbage)-1, 0, -1):
            if "G" not in garbage[i]:
                ans -= travel[i-1]
                continue
            else:
                break        
        for i in range(len(garbage)-1, 0, -1):
            if "P" not in garbage[i]:
                ans -= travel[i-1]
                continue
            else:
                break
        return ans