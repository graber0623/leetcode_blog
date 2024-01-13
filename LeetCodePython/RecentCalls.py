class RecentCounter:

    def __init__(self):
        self.que=[]

    def ping(self, t: int) -> int:
        i = 0
        while i <len(self.que) and self.que[i]< t-3000:
            i+=1
        self.que = self.que[i:]
        self.que.append(t)
        #print(self.que)
        return len(self.que)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)