class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        gratified = 0

        s = sorted(s)
        g = sorted(g)

        while s and g:
            if s[0] >= g[0]:
                s.pop(0)
                g.pop(0)
                gratified +=1
            else:
                s.pop(0)

        return gratified
## NOT GOOT RUNTIME