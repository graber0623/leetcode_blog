class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        
        curr_min = 10000000000
        max_num = 0
        for i in range(len(nums)):
            max_num = max(max_num, nums[i] - curr_min)
            curr_min = min(curr_min, nums[i])

        if max_num ==0:
            return -1
        else:
            return max_num