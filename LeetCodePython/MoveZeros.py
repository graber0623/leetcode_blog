class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s = []
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                s.append(nums.pop(i))
            else:
                i+=1

        for j in range(len(s)):
            nums.append(s[j])