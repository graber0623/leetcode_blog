class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        if ruleKey == 'type':
            j = 0
        elif ruleKey == 'color':
            j = 1
        else:
            j = 2

        ans = 0
        for l in items:
            if l[j] == ruleValue:
                ans +=1
        
        return ans