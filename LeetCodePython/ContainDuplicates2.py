from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = defaultdict(list)

        for i in range(len(nums)):
            d[nums[i]].append(i)

        for key in list(d.keys()):
            for ii in range(len(d[key])):
                for jj in range(ii+1,len(d[key])):
                    if abs(d[key][ii]-d[key][jj]) <= k:
                        return True

        
        return False