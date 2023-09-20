def minOperation(nums):
    op = 0
    nums = sorted(nums)
    while nums:
        print(nums, op)
        poped = nums.pop(0)
        nums = [x-poped for x in nums]
        if poped != 0:
            op+=1
    return op
    
a = [1,5,0,3,5]

print(minOperation(a))