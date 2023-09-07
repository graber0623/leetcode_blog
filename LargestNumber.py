# def largetNumber(nums):
#     d = {}
#     # for i in nums:
#     #     if d[int(str(i)[0])]:
#     #         d[int(str(i)[0])] = [i]
#     #     else:
#     #         d[int(str(i)[0])].append(i)



# def largestNumber(nums):
#     def compareAndSort(x,y):
#         xs = str(x)
#         ys = str(y)
#         maxi = max(len(xs), len(ys))
#         mini = min(len(xs), len(ys))
#         for i in range(maxi):
#             if i < mini:
#                 if xs[i] == ys[i]:
#                     continue
#                 elif xs[i] > ys[i]:
#                     first_return = x
#                     second_return = y
#                     return first_return, second_return
#                 else:
#                     first_return = y
#                     second_return = x
#                     return first_return, second_return
#             elif i >= mini and len(xs) .....................ha...........

a = [3,30,34,5,9]
def largestNumber(nums):
    if max(nums) == 0:
        return "0"
    nums = [str(x) for x in nums]
    
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] > nums[j] + nums[i]:
                continue
            else:
                a = nums[i]
                b = nums[j]
                nums[i] = b
                nums[j] = a
    return "".join(nums)

print(largestNumber(a))
                    
# a = sorted(["1", "34"])
# print(a)

# a = [1,2,3,4]
# a[2] = 7
# print(a)

