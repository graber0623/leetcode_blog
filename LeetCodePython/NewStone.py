class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        lj = set(list(jewels))
        ls = list(stones)
        ans = 0
        for stone in ls:
            if stone in lj:
                ans +=1 

        return ans