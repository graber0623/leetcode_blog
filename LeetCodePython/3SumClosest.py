from itertools import combinations
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        a = combinations(nums, 3)
        ans = 1000000
        for sub in a:
            if abs(sum(sub) - target) < abs(ans - target):
                ans = sum(sub)
        return ans
## Time Limit

## Two Pointer with one for loop