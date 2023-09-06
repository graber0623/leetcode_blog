def countAndSay(n):
    if n == 1:
        return "1"
    
    cache = [1]
    for i in range(1,n):
        new_cache = []
        for j in range(max(cache), -1, -1):
            j_count = cache.count(j)
            if j_count > 0:
                new_cache.append(j_count)
                new_cache.append(j)
        cache = new_cache
    
    return "".join([str(x) for x in cache]) 

print(countAndSay(4))