def groupAnagrams(strs):
    output = []

    while len(strs) > 0:
        print(strs)
        l = [strs[0]]
        i = 1
        pop_list = [0]
        for i in range(1, len(strs)):
            print(l[0], "vs", strs[i])
            if sorted(l[0]) == sorted(strs[i]):
                l.append(strs[i])
                pop_list.append(i)

        for j in range(len(pop_list)):
            strs.pop(pop_list[j] - j)
        print(l)
        print(pop_list)

        output.append(l)
    return output
    
print(groupAnagrams(["",""]))
