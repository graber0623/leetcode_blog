# def insert(intervals, newInterval):
    
#     m = intervals[-1][1]
    
#     line = [0] * (m+1)

#     for partition in intervals:
#         ps = partition[0]
#         pe = partition[1]
#         for i in range(ps, pe+1):
#             line[i] +=1
            
            
#     for j in range(newInterval[0],newInterval[1]+1):
#         line[j] +=1
#     ans = []
#     part =[]
           
#     for i in range(0,len(line)):
#         if i >= 1 and len(part) == 0:
#             part.append(line[i])
#         elif i == 0 and len(part) ==1:
#             part.append(line[i])
#             ans.append(part)
#             part = []
            
#     return ans


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        i = 0
        n = len(intervals)

        # Add intervals that come before the new interval
        while i < n and intervals[i][1] < newInterval[0]:
            ans.append(intervals[i])
            i += 1

        # Merge overlapping intervals with the new interval
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        ans.append(newInterval)

        # Add intervals that come after the new interval
        while i < n:
            ans.append(intervals[i])
            i += 1

        return ans
