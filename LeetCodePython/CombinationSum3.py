class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [1,2,3,4,5,6,7,8,9]
        ans = []
        def dfs(arr, sub_nums):
            nonlocal k, n, ans

            arr.append(sub_nums[0])

            if len(arr) == k and sum(arr) == n:
                ans.append(arr)
                return
            

            if len(arr) >= k or sum(arr) >=n:
                return

            for i in range(1, len(sub_nums)):
                if sub_nums[i] + sum(arr) > n:
                    break
                dfs(arr.copy(), sub_nums[i:])

        for j in range(len(nums)):
            dfs([], nums[j:])

        return ans
            

            