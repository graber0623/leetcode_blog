class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        count = 0
        ans = []
        def dfs(i, p):
            nonlocal count, n, s, ans
            if i >= n:
                if p not in ans:
                    ans.append(p)
                count +=1
                return
            if s[i] == "0":
                return
            
            if int(s[i:i+2]) > 26:
                p.append(s[i])
                dfs(i+1, p.copy())
            else:
                p.append(s[i])
                dfs(i+1, p.copy())
                p.pop()
                p.append(s[i:i+2])
                dfs(i+2, p.copy()) 
                p.pop()
                
        dfs(0, [])
        return len(ans)