class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        
        piles = sorted(piles)
        ans = 0
        for i in range(int(len(piles)/3), len(piles),2):
            ans += piles[i]

        return ans