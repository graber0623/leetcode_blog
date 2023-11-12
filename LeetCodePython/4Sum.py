class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        ans = []
        comb = []
        
        def dfs(c, sub_nums):
            nonlocal ans, target
            if len(c) == 4 and sum(c) == target:
                if sorted(c) not in ans:
                    ans.append(sorted(c))
                return
            
            if len(c) > 4:
                return
        
        
            for i in range(len(sub_nums)):
                c.append(sub_nums[i])
                dfs(c.copy(), sub_nums[i+1:])
                c.pop()
        
        dfs(comb,nums)

        return ans
