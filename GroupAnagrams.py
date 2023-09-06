# def groupAnagrams(strs):
#     output = []

#     while len(strs) > 0:
#         print(strs)
#         l = [strs[0]]
#         i = 1
#         pop_list = [0]
#         for i in range(1, len(strs)):
#             if sorted(l[0]) == sorted(strs[i]):
#                 l.append(strs[i])
#                 pop_list.append(i)

#         for j in range(len(pop_list)):
#             strs.pop(pop_list[j] - j)
#         print(l)
#         print(pop_list)

#         output.append(l)
#     return output
    
# print(groupAnagrams(["",""]))


def groupAnagrams(strs): ## using Hash
    hash_dict = {}
    for str in strs:
        sorted_str = "".join(sorted(str))
        if sorted_str in hash_dict:
            hash_dict[sorted_str].append(str)
        else:
            hash_dict[sorted_str] = [str]
    return list(hash_dict.values())

print(groupAnagrams(["",""]))

# d = {"a":["a","a"], "b":["b","b"]}
# print(d)

# d["a"].append("a")
# print(d)

# d["c"] = ["c"]
# print(d)

# if d["e"]:
#     d["e"].append("e")
# else:
#     d["e"] = ["e"]
    
# print(d)
