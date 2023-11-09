from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        d = defaultdict(int)
        for i in range(n):
            d[nums[i]] +=1
        ans = []
        for key in d.keys():
            if d[key] > n/3:
                ans.append(key)

        return ans