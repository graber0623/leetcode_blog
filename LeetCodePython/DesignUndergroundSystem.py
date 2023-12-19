from collections import defaultdict
class UndergroundSystem:

    def __init__(self):
        self.inProgress = defaultdict(list)
        self.finished = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.inProgress[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation = self.inProgress[id][0]
        startTime = self.inProgress[id][1]

        self.finished[startStation +'/'+stationName].append(t-startTime)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return mean(self.finished[startStation +'/'+ endStation])


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)