def rs(s):
    if len(s) == 1:
        return s
    
    d = {}
    
    for i in range(s):
        if s[i] in d:
            d[s[i]] +=1
        else:
            d[s[i]] = 1
            
    s_char = sorted(d.ketys(), key= lambda x: d[x], reverse=True)
    
    if d[s_char[0]] > (len(s)+1)//2:
        return ""
    
    res = [""] * len(s)
    
    i = 0
    for char in s_char:
        for _ in range(d[char]):
            if i >= len(s):
                i = 1
            res[i] = char
            print(res, char)
            i += 2
            
    return "".join(res)
## NOT MY SOLUTION
