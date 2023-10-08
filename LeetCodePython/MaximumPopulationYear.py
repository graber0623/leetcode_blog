class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        # max_count = 1
        # logs = sorted(logs, key = lambda x : (x[0],x[1]))
        
        # for i in range(1,len(logs)):
        #     if logs[i-1][1] > logs[i][0]:
        #         max_count +=
        delta = [0] * 101

        year1950 = 1950

        for l in logs:
            for year in range(l[0],l[1]):
                delta[year-year1950] +=1

        
        max_count = max(delta)

        for year in range(len(delta)):
            if delta[year] == max_count:
                return year+year1950



        
