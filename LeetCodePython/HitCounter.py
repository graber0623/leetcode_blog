class HitCounter:

    def __init__(self):
        self.queue = []

    def hit(self, timestamp: int) -> None:
        self.queue.append(timestamp)
        

    def getHits(self, timestamp: int) -> int:
        return len(self.queue) - bisect_right(self.queue, timestamp - 300)
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)