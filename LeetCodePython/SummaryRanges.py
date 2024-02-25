class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []

        if len(nums) == 1:
            return [str(x) for x in nums]
        start = nums[0]
        ans = []
        for i in range(1,len(nums)):
        
            if nums[i] != nums[i-1] + 1:
                if nums[i-1] != start:
                    ans.append(str(start)+'->'+str(nums[i-1]))
                else:
                    ans.append(str(nums[i-1]))
                start = nums[i]
            
            if i == len(nums)-1:
                if nums[i] == start:
                    ans.append(str(nums[i]))
                else:
                    ans.append(str(start)+'->'+str(nums[i]))




        return ans
                
