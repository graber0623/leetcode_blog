class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        l = [[0]*n]

        new_block = l[-1].copy()
        new_block[index] = 1
        l.append(new_block)
        maxSum -= 1
        print(l)
        print(maxSum)
        count = 1
        while maxSum > 0:
            new_block = l[-1].copy()
            for i in range(len(new_block)):
                if l[-1][i] == 1:
                    if i-1 >= 0: new_block[i-1] = 1
                    if i+1 < n: new_block[i+1] = 1
                    
            maxSum -= sum(new_block)
            if maxSum < 0:
                break
            else:
                l.append(new_block)
                count +=1
            print(l)
            print(maxSum)
        
        return count
                



# class Solution:
#     def maxValue(self, n: int, index: int, maxSum: int) -> int:
#         l = [[0]*n]

#         new_block = l[-1].copy()
#         new_block[index] = 1
#         l.append(new_block)
#         maxSum -= 1

#         while maxSum > 0:

#             new_block = l[-1].copy()
#             for i in range(len(new_block)):
#                 if l[-1][i] == 1:
#                     if i-1 >= 0: new_block[i-1] = 1
#                     if i+1 < n: new_block[i+1] = 1
#             maxSum -= sum(new_block)
#             if maxSum <= sum(new_block)+1:
#                 break
#             else:
#                 l.append(new_block)

#         return len(l)
            
