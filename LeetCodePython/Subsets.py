class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        ans.append([])
        n = len(nums)
        def dfs(i, sub):
            nonlocal ans, nums, n
            if i > n-1:
                if sub not in ans:
                    ans.append(sub.copy())
                return

            sub.append(nums[i])
            if sub not in ans:
                ans.append(sub.copy())

            for j in range(i+1, n):
                dfs(j, sub.copy())
        
        for x in range(n):
            dfs(x, [])
        
        return ans
        