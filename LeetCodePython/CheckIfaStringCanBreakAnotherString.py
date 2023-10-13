class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        ls1 = sorted(list(s1))
        ls2 = sorted(list(s2))
        rls1 = True
        for i in range(len(ls1)):
            if ls1[i] <= ls2[i]:
                continue
            else:
                rls1 = False
        rls2 = True
        for i in range(len(ls1)):
            if ls2[i] <= ls1[i]:
                continue
            else:
                rls2 = False
        return rls1 or rls2
        

