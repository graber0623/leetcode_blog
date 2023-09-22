# def countSubstrings(s,t):
#     ss = []
#     for i in range(len(s)):
#         for j in range(i+1, len(s)+1):
#             ss.append(s[i:j])
#     tt = []
#     for i in range(len(t)):
#         for j in range(i+1, len(t)+1):
#             tt.append(t[i:j])

#     min_len = min(len(ss), len(tt))
#     #ss = sorted(ss, key=len)
#     #tt = sorted(tt, key=len)

#     #ss = ss[:min_len]
#     #tt = tt[:min_len]

#     #print(ss, tt)
#     #last_point = 0
#     count = 0
#     for s_sub in ss:
#         for t_sub in tt:
#             if s_sub != t_sub:
#                 diff_count = 0
#     # for lengths in range(min(len(s), len(t)), 0, -1):
#     #     same_len_ss = ss[last_point : last_point + lengths]
#     #     same_len_tt = tt[last_point : last_point + lengths]
#     #     for s_sub in same_len_ss:
#     #         for t_sub in same_len_tt:
#     #             if s_sub != t_sub:
#     #                 diff_count = 0
#     #                 for index in range(len(t_sub)):
#     #                     if s_sub[index] != t_sub[index]:
#     #                         diff_count += 1
#     #                     if diff_count >= 2:
#     #                         break
#     #                 if diff_count == 1:
#     #                     count += 1

#     return count
# s = "aba"
# t = "baba"

# print(countSubstrings(s,t))

# ## FUCK!