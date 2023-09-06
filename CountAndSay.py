## Wrong Answer
# def countAndSay(n):
#     if n == 1:
#         return "1"
    
#     cache = [1]
#     for i in range(1,n):
#         new_cache = []
#         for j in range(max(cache), -1, -1):
#             j_count = cache.count(j)
#             if j_count > 0:
#                 new_cache.append(j_count)
#                 new_cache.append(j)
#         cache = new_cache
    
#     return "".join([str(x) for x in cache]) 

# print(countAndSay(4)) ## Wrong with 5

def countAndSay(n): ## runtime 71 %, Memory 15.5% ...hnmmm
    if n == 1:
        return "1"

    cache = [1]
    for _ in range(1,n):
        new_cache = []
        j = 0
        count = 0
        while j < len(cache):
            if j == len(cache)-1:
                count +=1
                new_cache.append(count)
                new_cache.append(cache[j])
            elif cache[j] == cache[j+1]:
                count +=1
            else:
                count +=1
                new_cache.append(count)
                new_cache.append(cache[j])
                count = 0
            j+=1
        cache = new_cache
    return "".join([str(x) for x in cache])

print(countAndSay(5))
                
                
            
