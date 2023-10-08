
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def dfs(ar):
            nonlocal candidates, target
            if sum(ar) == target:
                ar.remove(0)
                ar = sorted(ar)
                if ar not in ans:
                    ans.append(ar.copy())
                return
            elif sum(ar) > target:
                return
            for num in candidates:
                ar.append(num)
                dfs(ar.copy())
                ar.remove(num)
        
        dfs([0])

        return ans