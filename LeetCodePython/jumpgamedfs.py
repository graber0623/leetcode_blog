# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         ans = False
#         n = len(nums)
#         def dfs(i):
#             nonlocal nums, n, ans

#             if i >= n-1:
#                 ans = True
#                 return

#             if nums[i] == 0:
#                 return
                
#             for j in range(1, nums[i]+1):
#                 dfs(i+j)
            
#         dfs(0)
#         return ans

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        ans = False
        n = len(nums)
        visited = [0] * n
        def dfs(i):
            nonlocal nums, n, ans, visited

            if i >= n-1:
                ans = True
                return

            if nums[i] == 0:
                return
            
            if visited[i] == 1:
                return
            
            visited[i] = 1
                
            for j in range(1, nums[i]+1):
                dfs(i+j)
            
        dfs(0)
        return ans