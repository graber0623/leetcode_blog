class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        # a = 0
        # while k > 0:
        #     m = min(costs)
        #     costs.remove(m)
        #     a+=m
        #     k-= 1
        # return a

        s = sorted(costs)
        return sum(s[:k])