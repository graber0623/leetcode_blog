# FIRST ATTEMP -- WRONG!
# def lengthOfLIS(nums):
#     if len(nums) == 1: return 1

#     dp_nums = [min(nums)]
#     min_index = nums.index(dp_nums[-1])
#     new_nums = nums[min_index+1:]
#     i = 1
#     while len(new_nums) > 0:
#         print(dp_nums)
#         print(new_nums)
#         if min(new_nums) <= dp_nums[-1]:
#             new_nums.remove(min(new_nums))
#         else:
#             dp_nums.append(min(new_nums))
#             min_index = new_nums.index(dp_nums[-1])
#             new_nums = new_nums[min_index+1:]

#     return len(dp_nums)

# print(lengthOfLIS([1,3,6,7,9,4,10,5,6])) ## WRONG ANSWER FOR THIS

def lengthOfLIS(nums):
    cache = [1] * len(nums)
    
    for i in range(len(nums) -1, -1, -1):
        for j in range(i+1, len(nums)):
            if nums[i] < nums[j]:
                cache[i] = max(cache[i], 1+cache[j])
            print(" =================== ")
            print(i,   j)
            print(cache)
            print(nums)
            print(" =================== ")
    
    return max(cache)

print(lengthOfLIS([1,3,6,7,9,4,10,5,6]))