from collections import defaultdict

class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = defaultdict(int)

        for i in range(len(s)):
            d[s[i]] += 1
        
        no_ones = 0
        count = 0
        for char_count in d.values():
            if char_count % 2 == 0:
                count += char_count

            else:
                if no_ones == 1:
                    count += char_count - 1
                else:
                    count += char_count
                    no_ones +=1

        return count
        