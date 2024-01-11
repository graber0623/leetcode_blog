class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ma = -100000
        for i in range(len(nums)-(k-1)):
            ma = max(sum(nums[i:i+k]) / k, ma)

        return ma