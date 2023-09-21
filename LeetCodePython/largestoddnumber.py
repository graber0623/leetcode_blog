# def largestOddNumber(num):
#     m = 0
#     for i in range(len(num)):
#         for j in range(i+1, len(num)+1):
#             a = int(num[i:j])
#             print("subnum:   ",  a)
#             if a %2== 1:
#                 m = max(m, a)
#             print("max:   ", m)
#     return a

# print(largestOddNumber("35427"))

class Solution:
    def largestOddNumber(self, num: str) -> str:
        l = 0
        r = len(num)
        while l < r:
            if int(num[r-1]) % 2 == 1:
                return num[l:r]
            
            if int(num[r-1]) % 2 ==0:
                r-=1
            else:
                l+=1
        
        return ""