class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        last_i = 0
        sum = 0 
        for i in range(2,len(nums)+1,2):
            sum += min(nums[last_i:i])
            last_i = i
        
        return sum
a = [1,2,3,4]
print(a[2:4])