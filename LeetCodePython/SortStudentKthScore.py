class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        d = {}
        for i in range(len(score)):
            d[score[i][k]] = score[i]

        d = sorted(d.items(), reverse = True)
        a = []
        for i in range(len(d)):
            a.append(d[i][1])
        return a

        
#         return sorted(score, key=lambda x: x[k], reverse = True)


