class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = [False] * len(candies)
        m = max(candies)
        for i in range(len(candies)):
            
            if extraCandies + candies[i] >= m:
                ans[i] = True

        return ans