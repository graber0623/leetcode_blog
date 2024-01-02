class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = []
        for i in range(len(temperatures)-1):
            l = len(ans)
            for j in range(i+1, len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    ans.append(j-i)
                    break

            
            if len(ans) == l:
                ans.append(0)
        
        ans.append(0)
        return ans

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans=[0]*len(temperatures)
        stack=[]

        for i , t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                tempt ,tempi= stack.pop()
                ans[tempi] = i - tempi
            stack.append([t,i])
        return ans        