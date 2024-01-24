from collections import defaultdict
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        d = defaultdict(int)
        allusers = set()
        lostusers = set()
        for match in matches:
            d[match[1]] += 1
            allusers.add(match[0])
            lostusers.add(match[1])
        
        zeros = []
        ones = []

        for user in allusers:
            if user not in lostusers:
                zeros.append(user)
        
        for lostuser in lostusers:
            if d[lostuser] == 1:
                ones.append(lostuser)

        return [sorted(zeros), sorted(ones)]