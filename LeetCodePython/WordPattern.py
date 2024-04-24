

from collections import defaultdict

class Solution:

    def wordPattern(self, pattern: str, s: str) -> bool:

        s = s.split(' ')

        d = defaultdict(str)

        T = True

        for i in range(len(pattern)):

            if d[s[i]]:

                if d[s[i]] != pattern[i]:

                    T = False

                    break

            else:

                d[s[i]] = pattern[i]

        return T