class Solution:
    def bestClosingTime(self, customers: str) -> int:
        y = []
        n = []
        for i in range(len(customers)):
            if customers[i] == 'Y':
                y.append(0)
                n.append(1)
            else:
                y.append(1)
                n.append(0)

        m = 1000000
        ans = 0
        for i in range(len(customers)+1):
            if sum(y[:i]+n[i:]) < m:
                m = sum(y[:i] + n[i:])
                ans = i

        return ans

        class Solution:
    def bestClosingTime(self, customers: str) -> int:
        max_score = score = 0
        best_hour = -1

        for i, c in enumerate(customers):
            score += 1 if c == 'Y' else -1
            if score > max_score:
                max_score, best_hour = score, i
                
        return best_hour + 1
