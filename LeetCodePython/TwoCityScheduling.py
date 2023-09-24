# class Solution:
#     def twoCitySchedCost(self, costs: List[List[int]]) -> int:
#         ncount = int(len(costs)/2)


#         costs = sorted(costs, key = lambda x: abs(x[0]-x[1]), reverse = True)

#         A = 0
#         B = 0
#         sum = 0
#         for i in range(ncount*2):
#             if A < ncount and B < ncount:
#                 if costs[i][0] < costs[i][1]:
#                     sum += costs[i][0]
#                     A +=1
#                 elif costs[i][0] > costs[i][1]:
#                     sum += costs[i][1]
#                     B +=1
#                 else:
#                     sum += costs[i][0]
#                     if A > B:
#                         A+=1
#                     else:
#                         B+=1

#             elif A == ncount:
#                 sum += costs[i][1]
#                 B+=1

#             elif B == ncount:
#                 sum += costs[i][0]

#         return sum