
from collections import defaultdict
def minSteps(s, t):
    d = defaultdict(int)
    for i in range(len(s)):
        d[s[i]] += 1
    
    t = sorted(t)
    change_count = 0 
    
    for i in range(len(t)):
        if d[t[i]]:
            d[t[i]] -= 1
        elif not d[t[i]] or d[t[i]] == 0:
            change_count +=1
            
    return change_count
    
    
# print(minSteps("anagram", "mangaar"))


# s = "bab", t = "aba"
# s = "leetcode", t = "practice"
# s = "anagram", t = "mangaar"
print(counter("leetcode"))