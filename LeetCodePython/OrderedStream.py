class OrderedStream:

    def __init__(self, n: int):
        self.l = [0] * n

    def insert(self, idKey: int, value: str) -> List[str]:
        self.l[idKey-1] = value
        rightkey = idKey-1
        for i in range(idKey, len(self.l)):
            if self.l[i] != 0:
                rightkey +=1
            else:
                break
        return self.l[idKey-1:rightkey +1]

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)