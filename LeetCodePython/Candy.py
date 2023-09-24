## MY FIRST HARD QUESTION

##FAILED!!

def candy(r):
    n = len(r)
    dp = [1] * n
    
    for i in range(n-1):
        if r[i] < r[i+1]:
            dp[i+1] = max(1+dp[i], dp[i+1])
            
    for i in range(n-2, -1, -1):
        if r[i+1] < r[i]:
            dp[i+1] = max(1+dp[i+1], dp[i])
            
    return sum(dp)
    
    
class Solution:
    def candy(self, ratings: List[int]) -> int:
        if len(ratings) == 1:
            return 1
        
        dp = [1] * len(ratings)
        if ratings[0] > ratings[1]:
            dp[0] +=1

        for i in range(1, len(ratings)-1):
            if ratings[i] <= ratings[i-1] and ratings[i] <= ratings[i+1]:
                dp[i] = 1
            elif ratings[i] == ratings[i-1] and ratings[i] > ratings[i+1]:
                dp[i] = dp[i-1] +1 
            elif ratings[i] > ratings[i-1] :
                dp[i] = dp[i-1] +1

        if ratings[-1] > ratings[-2]:
            dp[-1] = dp[-2] +1
        else:
            dp[-1] = 1

        return sum(dp)