# class Solution:
#     def maxProfit(self, prices: List[int], fee: int) -> int:
        
def maxProfit(prices, fee) -> int:
    print(prices)
    pos=-prices[0]
    print(pos)
    profit=0
    n=len(prices)
    for i in range(1,n):
        print(prices[i])
        print("pos : ",pos, "   ", profit-prices[i])
        pos=max(pos,profit-prices[i])
        
        print("profit : " ,profit, "    ", pos+prices[i]-fee)
        profit=max(profit,pos+prices[i]-fee)
        
        print("changed : ",pos, "    ", profit)


    return profit 

print(maxProfit([10,2,9,3,1,4,9], 2))

