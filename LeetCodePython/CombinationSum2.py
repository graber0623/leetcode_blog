
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        ans = []
        comb = []
        i = 0
        def dfs(c, sub_candidates):
            nonlocal ans, target

            if sum(c) == target:
                if c not in ans:
                    ans.append(c)
                return
            if sum(c) > target:
                return

            for i in range(len(sub_candidates)):
                c.append(sub_candidates[i])
                dfs(c.copy(), sub_candidates[i+1:])
                c.pop()

        dfs(comb, candidates)

        return ans
                


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(start, target, path):
            if target == 0:
                ans.append(path)
                return
            if target < 0:
                return

            for i in range(start, len(candidates)):
                # Skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                dfs(i + 1, target - candidates[i], path + [candidates[i]])

        candidates.sort()  # Sort to handle duplicates
        ans = []
        dfs(0, target, [])
        return ans