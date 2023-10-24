from collections import defaultdict
# class Solution:
#     def removeDuplicateLetters(self, s: str) -> str:
#         d = defaultdict(int)
#         for i in range(len(s)):
#             d[s[i]] +=1
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        seen = set()
        last_occ = defaultdict(int)

        for i in range(len(s)):
            last_occ[s[i]] = i

        for i, c in enumerate(s):
            if c not in seen:

                while stack and c < stack[-1] and i < last_occ[stack[-1]]:
                    seen.discard(stack.pop())
                seen.add(c)
                stack.append(c)

        return "".join(stack)
