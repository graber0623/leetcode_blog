from collections import defaultdict
# def findRelativeRanks(score):
#     d = defaultdict(int)
#     for i, value in enumerate(score):
#         d[i] = value
#     #print(d)
#     return_list = [" "] * len(score)

#     s = sorted(d.items(), key = lambda item: item[1], reverse = True)
#     print(s)
#     for j in range(len(s)):
#         if j == 0:
#             return_list[s[j][0]] = "Gold Medal"
#         elif j == 1:
#             return_list[s[j][0]] = "Silver Medal"
#         elif j == 2:
#             return_list[s[j][0]] = "Bronze Medal"
#         else:
#             return_list[s[j][0]] = str(s[j][1])

#     return return_list

print(findRelativeRanks([10,3,8,9,4]))

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        d = defaultdict(int)
        for i, value in enumerate(score):
            d[i] = value
        #print(d)
        return_list = [" "] * len(score)

        s = sorted(d.items(), key = lambda item: item[1], reverse = True)
        #print(s)
        for j in range(len(s)):
            if j == 0:
                return_list[s[j][0]] = "Gold Medal"
            elif j == 1:
                return_list[s[j][0]] = "Silver Medal"
            elif j == 2:
                return_list[s[j][0]] = "Bronze Medal"
            else:
                return_list[s[j][0]] = str(j+1)

        return return_list