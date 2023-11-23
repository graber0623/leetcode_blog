# from collections import defaultdict
# class Solution:
#     def isReflected(self, points: List[List[int]]) -> bool:
#         if len(points) == 1:
#             return True
#         yd = defaultdict(int)
#         for i in range(len(points)):
#             if yd[points[i][1]]:
#                 return True
#             else:
#                 yd[points[i][1]] = 1

#         return False