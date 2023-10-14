class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(nums)

        ans = -1
        for i in range(n):
            if i != nums[i]:
                ans = i
                break

        if ans == -1:
            return n
        else:
            return ans
