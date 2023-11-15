class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
            
        max_length = 1
        found = False
        def dfs(sub):
            nonlocal max_length, found
            if len(list(set(sub))) <= 2:
                max_length = max(max_length, len(sub))
                found = True
                return
            # if found == True:
            #     return
            if len(sub) == 1:
                return
            dfs(sub[:-1])
            dfs(sub[1:])

        dfs(s)
        return max_length
    
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        
        s = list(s)
        n = len(s)
        if n == 1:
            return 1
        
        for i in range(n,0,-1):
            for j in range(0, n-i + 1):
                if len(list(set(s[j:j+i]))) == 2:
                    return i
        return 1