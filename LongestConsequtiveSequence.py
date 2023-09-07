a = [0,3,7,2,5,8,4,6,0,1]
def lcs( nums):
    if len(nums) <= 1:
        return len(nums)
    
    nums = sorted(nums)
    possible = []
    c = 0
    for i in range(0,len(nums)):
        
        c+=1
        print("===========")
        print(i)
        print(c)
        print(possible)
        print("============")
        if i == len(nums)-1:
            possible.append(c)

        elif nums[i] == nums[i+1]-1:
            
            continue
        elif nums[i] == nums[i+1]:
            c -=1
            
        else:
            possible.append(c)
            c = 0
    return max(possible)

    
print(lcs(a))

## 0 0 1 2 3 4 5 6 7 8

# a = sorted([0, -1])
# print(a)