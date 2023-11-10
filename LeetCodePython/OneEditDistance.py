class Solution:
    # O(n) time | O(1) space
    # n = length of s or t, they should be similar in size
    def isOneEditDistance(self, s: str, t: str) -> bool:
        # Check for valid input string sizes and equality
        if abs(len(s) - len(t)) > 1 or s == t:
            return False
        
        p1, p2 = 0, 0
        alreadyEdited = False

        while p1 < len(s) and p2 < len(t):
            if s[p1] == t[p2]:
                p1 += 1
                p2 += 1
            else:
                if alreadyEdited:
                    return False
                       
                alreadyEdited = True
                needDelete = len(s) > len(t)
                needInsert = len(s) < len(t)
                needReplace = len(s) == len(t)

                if needDelete:
                    p1 += 1
                if needInsert:
                    p2 += 1
                if needReplace:
                    p1 += 1
                    p2 += 1

        return True
# from collections import defaultdict
# from collections import Counter
# class Solution:
#     def isOneEditDistance(self, s: str, t: str) -> bool:
#         if abs(len(s) - len(t)) > 1:
#             return False
#         s = sorted(s)
#         t = sorted(t)
#         if s == t:
#             return False
        
#         sc = Counter(s)
#         tc = Counter(t)

#         diff_count = 0
#         all_keys = list(set(list(sc.keys()) + list(tc.keys())))
#         for key in all_keys:
#             if not tc[key]:
#                 diff_count += sc[key]
#             elif not sc[key]:
#                 diff_count += tc[key]
#             elif sc[key] != tc[key]:
#                 diff_count += abs(sc[key]-tc[key])

#         if diff_count == 1:
#             return True
#         else:
#             return False

        
        


# # from collections import defaultdict
# # class Solution:
# #     def isOneEditDistance(self, s: str, t: str) -> bool:
# #         if abs(len(s) - len(t)) > 1:
# #             return False
# #         s = sorted(s)
# #         t = sorted(t)
# #         if s == t:
# #             return False
# #         if len(s) <= len(t):
# #             shorter = s
# #             longer = t
# #         else:
# #             shorter = t
# #             longer = s
        
# #         i = 0
# #         j = 0
# #         diff_count = 0
# #         while i < len(shorter)-1:
# #             if shorter[i] == longer[j]:
# #                 i += 1
# #                 j += 1
# #             else:
# #                 diff_count += 1
# #                 j+=1
            
# #         if diff_count > 1:
# #             return False
# #         else:
# #             return True

