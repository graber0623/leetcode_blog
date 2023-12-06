from collections import defaultdict
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        d = defaultdict(list)
        for i in range(len(pattern)):
            d[pattern[i]].append(i)

        pattern_list = sorted(list(d.values()), key = lambda x: len(x))

        ans = []
        for word in words:
            di = defaultdict(list)
            for j in range(len(word)):
                di[word[j]].append(j)

            word_pattern = sorted(list(di.values()), key = lambda x: len(x))

            if pattern_list == word_pattern:
                ans.append(word)

        return ans
