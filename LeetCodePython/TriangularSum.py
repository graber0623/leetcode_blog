class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        
        def bfs(l):
            if len(l) == 1:
                return l[0]
            new = []
            for i in range(1,len(l)):
                new.append((l[i-1] + l[i])% 10)
            
            return bfs(new)

        return bfs(nums)