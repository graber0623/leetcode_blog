class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs = sorted(costs)
        count = 0
        for i in range(len(costs)):
            if coins < costs[i]:
                break
            else:
                coins -= costs[i]
                count +=1
        return count