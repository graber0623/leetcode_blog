class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left =[]
        eq = []
        right =[] 
        for i in range(len(nums)):
            if nums[i] == pivot:
                eq.append(nums[i])
            elif nums[i] < pivot:
                left.append(nums[i])
            else:
                right.append(nums[i])
        
        return left+eq+right