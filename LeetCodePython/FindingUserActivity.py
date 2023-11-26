from collections import defaultdict
class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        d = defaultdict(list)

        for action in logs:
            uid = action[0]
            minute = action[1]
            if minute not in d[uid]:
                d[uid].append(minute)
        ans = [0] * k
        for key in d.keys():
            ans[len(d[key])-1] += 1
        
        return ans
                