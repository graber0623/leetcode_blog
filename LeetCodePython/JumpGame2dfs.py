class Solution:

    def jump(self, nums: List[int]) -> int:

        ans = 100000

        n = len(nums)

        visited = [0] * n

        def dfs(i, jumps):

            nonlocal nums, n, ans, visited


 

            if i >= n-1:

                ans = min(ans, jumps)

                return


 

            if nums[i] == 0:

                return

           

            if visited[i] == 1:

                return

           

            visited[i] = 1

            jumps += 1


 

            for j in range(1, nums[i]+1):

                dfs(i+j, jumps)

           

        dfs(0,0)

        return ans