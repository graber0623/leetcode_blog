from collections import defaultdict
class Leaderboard:

    def __init__(self):
        self.scoreboard = defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        self.scoreboard[playerId] += score

    def top(self, K: int) -> int:
        dl = sorted(self.scoreboard.values(), reverse = True)
        return sum(dl[0:K])

    def reset(self, playerId: int) -> None:
        self.scoreboard[playerId] = 0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)