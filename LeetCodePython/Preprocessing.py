import re
from collections import defaultdict
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.sub(r"[!?',;.]", " ", paragraph.lower())
        par = paragraph.split(" ")
        d = defaultdict(int)
        b = set(banned)
        for word in par:
            if word in banned:
                continue
            d[word]+=1

        dd = sorted(d.items(), key = lambda x: x[1], reverse = True)
        return dd[0][0]