class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        nums = sorted(nums)
        max_diff = 0
        for i in range(1,len(nums)):
            max_diff = max(max_diff, nums[i]-nums[i-1])

        return max_diff