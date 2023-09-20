a = [1,0,0,1,1,0,0,0,1]




class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if 1 not in nums:
            return 0
        if 0 not in nums:
            return len(nums) - 1

        zeros = [-1]
        max_length = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros.append(i)
        zeros.append(len(nums))
        for j in range(0, len(zeros)-2):
            max_length = max(max_length, zeros[j+2] - zeros[j] - 2)

        return max_length
