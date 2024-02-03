class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            c = 0
            for j in range(len(nums)):
                if i == j:
                    continue
                elif nums[i] > nums[j]:
                    c+=1

            ans.append(c)

        return ans
