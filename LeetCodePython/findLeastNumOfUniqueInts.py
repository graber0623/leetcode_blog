
def findLeastNumOfUniqueInts(arr, k):
    d = {}
    for x in arr:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
    print(d)
    d = sorted(list(d.values()))## we only need the counts of number
    
    print(d)
    for _ in range(k):
        if d[0] == 0:
            d.pop(0)
        else:
            d[0] -= 1
            if d[0] == 0:
                d.pop(0)
        
    print(d)
    
    return len(d)

a = [5,5,4]
k = 1
b = [4,3,1,1,3,3,2]
j = 3

print(findLeastNumOfUniqueInts(a,k))
