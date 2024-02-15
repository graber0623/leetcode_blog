import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        c = math.prod(nums)
        re = [0]*len(nums)
        for j in range(len(nums)):
            if nums[j] != 0:
                re[j] = int(c/nums[j])
            else:
                re[j] = math.prod(nums[:j]+nums[j+1:])
        
        return re
        