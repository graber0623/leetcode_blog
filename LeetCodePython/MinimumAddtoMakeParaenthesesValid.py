class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        c = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(1)
            elif s[i] == ")" and len(stack) == 0:
                c.append(1)
            elif s[i] == ")" and len(stack) > 0:
                stack.pop()


        return len(stack) + len(c)

