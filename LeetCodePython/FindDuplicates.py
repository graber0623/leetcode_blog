class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        ans = []
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                ans.append(nums[i])

        return list(set(ans))