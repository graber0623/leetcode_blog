from collections import defaultdict
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        a = set(list(allowed))
        ans = 0
        for word in words:
            for i in range(len(word)):
                if word[i] not in a:
                    ans += 1
                    break
        
        return len(words) - ans
        