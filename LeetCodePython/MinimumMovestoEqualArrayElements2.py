class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums = sorted(nums)

        standard_index = len(nums)//2

        c = 0

        for i in range(len(nums)):
            c+= abs(nums[i] - nums[standard_index])
        
        return c