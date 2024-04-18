from collections import defaultdict
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = defaultdict(int)

        for i in range(len(nums)):
            d[nums[i]] +=1

        c = 0
        for key in d.keys():
            if d[key] > 1:
                c = key

        return c