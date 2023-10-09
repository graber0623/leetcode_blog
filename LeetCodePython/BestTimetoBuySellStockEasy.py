class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_position = prices[0]
        for i in range(1,len(prices)):
            min_position = min(prices[i], min_position)
            profit = max(profit, prices[i] - min_position)

        return profit