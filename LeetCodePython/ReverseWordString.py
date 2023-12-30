import re
class Solution:
    def reverseWords(self, s: str) -> str:
        sl = re.split(r'\s+', s.strip())
        sl = sl[::-1]
        ans = ' '.join(sl)
        
        return ans