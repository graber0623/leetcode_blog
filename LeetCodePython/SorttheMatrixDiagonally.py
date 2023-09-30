# class Solution:
#     def rotate(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         n = len(matrix)
#         ans = []
#         i = 0
#         while i < n:
#             row=[]
#             for j in range(n):
#                 row.append(matrix[j][i])

#             row = row[::-1]
#             ans.append(row)
#             i+=1
        
#         matrix = ans